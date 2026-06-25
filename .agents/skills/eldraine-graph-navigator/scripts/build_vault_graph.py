#!/usr/bin/env python3
"""Build a lightweight dependency graph for an Obsidian-style Markdown vault."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
CACHE_VERSION = 1
DEFAULT_EXCLUDED_DIRS = {
    ".agents",
    ".git",
    ".graph",
    ".obsidian",
    ".stfolder",
    ".stversions",
    ".tmp.drivedownload",
    ".tmp.driveupload",
    ".tmp_edge_pdf",
    ".trash",
    "_Archive",
}


def normalize_path(path: Path | str) -> str:
    return Path(path).as_posix().lstrip("./")


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return parse_frontmatter_lines(lines[1:index]), "\n".join(lines[index + 1 :])
    return {}, text


def parse_frontmatter_lines(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key: str | None = None
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("-") and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(stripped[1:].strip().strip('"\''))
            continue
        if ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        current_key = key
        if value.startswith("[") and value.endswith("]"):
            data[key] = [part.strip().strip('"\'') for part in value[1:-1].split(",") if part.strip()]
        elif value == "":
            data[key] = []
        else:
            data[key] = value.strip('"\'')
    return data


def iter_markdown_files(root: Path, include_archive: bool = False) -> list[Path]:
    excluded = set(DEFAULT_EXCLUDED_DIRS)
    if include_archive:
        excluded.discard("_Archive")
    files: list[Path] = []
    for path in root.rglob("*.md"):
        relative_parts = path.relative_to(root).parts
        if any(part in excluded or part.startswith(".tmp") for part in relative_parts[:-1]):
            continue
        if any(part.startswith(".") and part not in {"."} for part in relative_parts[:-1]):
            continue
        files.append(path)
    return sorted(files, key=lambda item: normalize_path(item.relative_to(root)).casefold())


def build_lookup(relative_paths: list[str]) -> dict[str, str | list[str]]:
    lookup: dict[str, str | list[str]] = {}
    buckets: dict[str, list[str]] = defaultdict(list)
    for rel in relative_paths:
        path = Path(rel)
        keys = {rel, rel.removesuffix(".md"), path.name, path.stem}
        for key in keys:
            buckets[normalize_path(key).casefold()].append(rel)
    for key, values in buckets.items():
        unique = sorted(set(values))
        lookup[key] = unique[0] if len(unique) == 1 else unique
    return lookup


def clean_link_target(raw_target: str) -> str:
    target = raw_target.split("|", 1)[0].strip()
    target = target.split("#", 1)[0].strip()
    target = target.replace("%20", " ")
    return normalize_path(target)


def resolve_target(raw_target: str, lookup: dict[str, str | list[str]]) -> str | None:
    target = clean_link_target(raw_target)
    if not target:
        return None
    candidates = [target]
    if not target.lower().endswith(".md"):
        candidates.append(f"{target}.md")
    for candidate in candidates:
        value = lookup.get(normalize_path(candidate).casefold())
        if isinstance(value, str):
            return value
    return None


def extract_links(body: str) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    for match in WIKILINK_RE.finditer(body):
        links.append({"kind": "wikilink", "target": match.group(1).strip()})
    for match in MARKDOWN_LINK_RE.finditer(body):
        target = match.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if ".md" in target.lower():
            links.append({"kind": "markdown", "target": target})
    return links


def parse_note(path: Path, root: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    frontmatter, body = split_frontmatter(text)
    title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    stat = path.stat()
    return {
        "path": normalize_path(path.relative_to(root)),
        "mtime_ns": stat.st_mtime_ns,
        "size": stat.st_size,
        "title": title_match.group(1).strip() if title_match else path.stem,
        "frontmatter": frontmatter,
        "links": extract_links(body),
    }


def load_cache(cache_path: Path | None) -> dict[str, Any]:
    if not cache_path or not cache_path.exists():
        return {"version": CACHE_VERSION, "files": {}}
    try:
        cache = json.loads(cache_path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return {"version": CACHE_VERSION, "files": {}}
    if cache.get("version") != CACHE_VERSION or not isinstance(cache.get("files"), dict):
        return {"version": CACHE_VERSION, "files": {}}
    return cache


def refresh_cache(root: Path, files: list[Path], cache_path: Path | None) -> tuple[dict[str, Any], dict[str, int]]:
    cache = load_cache(cache_path)
    cached_files: dict[str, Any] = cache.get("files", {})
    next_files: dict[str, Any] = {}
    stats = {"reused": 0, "parsed": 0, "removed": 0}

    seen = set()
    for path in files:
        rel = normalize_path(path.relative_to(root))
        seen.add(rel)
        stat = path.stat()
        cached = cached_files.get(rel)
        if cached and cached.get("mtime_ns") == stat.st_mtime_ns and cached.get("size") == stat.st_size:
            next_files[rel] = cached
            stats["reused"] += 1
        else:
            next_files[rel] = parse_note(path, root)
            stats["parsed"] += 1

    stats["removed"] = len(set(cached_files) - seen)
    next_cache = {"version": CACHE_VERSION, "files": dict(sorted(next_files.items()))}
    if cache_path:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(next_cache, ensure_ascii=False, indent=2), encoding="utf-8")
    return next_cache, stats


def build_graph(root: Path | str, include_archive: bool = False, cache_path: Path | str | None = None) -> dict[str, Any]:
    root = Path(root).resolve()
    files = iter_markdown_files(root, include_archive=include_archive)
    relative_paths = [normalize_path(path.relative_to(root)) for path in files]
    lookup = build_lookup(relative_paths)
    cache_file = Path(cache_path).resolve() if cache_path else None
    cache, cache_stats = refresh_cache(root, files, cache_file)

    nodes: dict[str, dict[str, Any]] = {}
    edges: list[dict[str, str]] = []
    broken_links: list[dict[str, str]] = []

    for rel, note in sorted(cache["files"].items()):
        nodes[rel] = {
            "path": rel,
            "title": note.get("title") or Path(rel).stem,
            "frontmatter": note.get("frontmatter") or {},
            "outgoing": [],
            "backlinks": [],
        }
        for link in note.get("links", []):
            resolved = resolve_target(link["target"], lookup)
            if resolved:
                edges.append({"source": rel, "target": resolved, "kind": link["kind"]})
                nodes[rel]["outgoing"].append(resolved)
            else:
                broken_links.append({"source": rel, "target": clean_link_target(link["target"]), "kind": link["kind"]})

    for node in nodes.values():
        node["outgoing"] = sorted(set(node["outgoing"]))

    for edge in edges:
        if edge["target"] in nodes:
            nodes[edge["target"]]["backlinks"].append(edge["source"])

    for node in nodes.values():
        node["backlinks"] = sorted(set(node["backlinks"]))

    orphans = sorted(
        path
        for path, node in nodes.items()
        if not node["outgoing"] and not node["backlinks"]
    )

    return {
        "summary": {
            "nodes": len(nodes),
            "edges": len(edges),
            "broken_links": len(broken_links),
            "orphans": len(orphans),
            "cache_reused": cache_stats["reused"],
            "cache_parsed": cache_stats["parsed"],
            "cache_removed": cache_stats["removed"],
        },
        "nodes": dict(sorted(nodes.items())),
        "edges": sorted(edges, key=lambda edge: (edge["source"], edge["target"], edge["kind"])),
        "broken_links": broken_links,
        "orphans": orphans,
    }


def render_dot(graph: dict[str, Any]) -> str:
    lines = ["digraph eldraine_vault {", "  rankdir=LR;"]
    for path in graph["nodes"]:
        lines.append(f'  "{escape_dot(path)}";')
    for edge in graph["edges"]:
        lines.append(f'  "{escape_dot(edge["source"])}" -> "{escape_dot(edge["target"])}" [label="{edge["kind"]}"];')
    lines.append("}")
    return "\n".join(lines) + "\n"


def escape_dot(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def render_report(graph: dict[str, Any]) -> str:
    summary = graph["summary"]
    lines = [
        "# Eldraine Vault Graph Report",
        "",
        "## Summary",
        "",
        f"- Nodes: {summary['nodes']}",
        f"- Edges: {summary['edges']}",
        f"- Broken links: {summary['broken_links']}",
        f"- Orphans: {summary['orphans']}",
        f"- Cache reused: {summary.get('cache_reused', 0)}",
        f"- Cache parsed: {summary.get('cache_parsed', 0)}",
        f"- Cache removed: {summary.get('cache_removed', 0)}",
        "",
        "## High-Degree Notes",
        "",
    ]
    ranked = sorted(
        graph["nodes"].values(),
        key=lambda node: (len(node["backlinks"]) + len(node["outgoing"]), node["path"]),
        reverse=True,
    )[:20]
    if ranked:
        for node in ranked:
            degree = len(node["backlinks"]) + len(node["outgoing"])
            lines.append(f"- `{node['path']}` - degree {degree}, backlinks {len(node['backlinks'])}, outgoing {len(node['outgoing'])}")
    else:
        lines.append("- None")

    lines.extend(["", "## Broken Links", ""])
    if graph["broken_links"]:
        for link in graph["broken_links"][:50]:
            lines.append(f"- `{link['source']}` -> `{link['target']}` ({link['kind']})")
    else:
        lines.append("- None")

    lines.extend(["", "## Orphans", ""])
    if graph["orphans"]:
        for path in graph["orphans"][:50]:
            lines.append(f"- `{path}`")
    else:
        lines.append("- None")
    lines.append("")
    return "\n".join(lines)


def write_outputs(graph: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "vault-graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / "vault-graph.dot").write_text(render_dot(graph), encoding="utf-8")
    (out_dir / "vault-graph-report.md").write_text(render_report(graph), encoding="utf-8")


def default_cache_path(out_dir: Path) -> Path:
    return out_dir / "vault-graph-cache.json"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build an Obsidian Markdown dependency graph.")
    parser.add_argument("root", nargs="?", default=".", help="Vault root. Defaults to current directory.")
    parser.add_argument("--out", default=".agents/graph", help="Output directory for JSON, DOT, and report files.")
    parser.add_argument("--cache", default=None, help="Incremental cache path. Defaults to <out>/vault-graph-cache.json when set without a value by watcher.")
    parser.add_argument("--include-archive", action="store_true", help="Include _Archive notes in the graph.")
    args = parser.parse_args(argv)

    out_dir = Path(args.out)
    cache_path = Path(args.cache) if args.cache else None
    graph = build_graph(args.root, include_archive=args.include_archive, cache_path=cache_path)
    write_outputs(graph, out_dir)
    summary = graph["summary"]
    print(
        f"Built graph: {summary['nodes']} nodes, {summary['edges']} edges, "
        f"{summary['broken_links']} broken links, {summary['orphans']} orphans, "
        f"cache parsed {summary['cache_parsed']}, reused {summary['cache_reused']}, removed {summary['cache_removed']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
