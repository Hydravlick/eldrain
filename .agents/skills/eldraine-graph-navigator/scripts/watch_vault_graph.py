#!/usr/bin/env python3
"""Watch an Eldraine vault and rebuild the Markdown dependency graph."""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import build_vault_graph


def log(message: str) -> None:
    try:
        print(message, flush=True)
    except Exception:
        pass


def vault_signature(root: Path, include_archive: bool = False) -> tuple[tuple[str, int, int], ...]:
    files = build_vault_graph.iter_markdown_files(root, include_archive=include_archive)
    signature = []
    for path in files:
        stat = path.stat()
        signature.append((build_vault_graph.normalize_path(path.relative_to(root)), stat.st_mtime_ns, stat.st_size))
    return tuple(signature)


def rebuild(root: Path, out_dir: Path, cache_path: Path, include_archive: bool = False) -> None:
    graph = build_vault_graph.build_graph(root, include_archive=include_archive, cache_path=cache_path)
    build_vault_graph.write_outputs(graph, out_dir)
    summary = graph["summary"]
    log(
        f"Graph refreshed: {summary['nodes']} nodes, {summary['edges']} edges, "
        f"parsed {summary['cache_parsed']}, reused {summary['cache_reused']}."
    )


def watch(root: Path, out_dir: Path, cache_path: Path, interval: float, include_archive: bool = False) -> None:
    previous = None
    log(f"Watching {root} every {interval:g}s. Press Ctrl+C to stop.")
    while True:
        current = vault_signature(root, include_archive=include_archive)
        if current != previous:
            rebuild(root, out_dir, cache_path, include_archive=include_archive)
            previous = current
        time.sleep(interval)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Watch a Markdown vault and refresh the graph when notes change.")
    parser.add_argument("root", nargs="?", default=".", help="Vault root. Defaults to current directory.")
    parser.add_argument("--out", default=".agents/graph", help="Output directory for graph artifacts.")
    parser.add_argument("--cache", default=None, help="Incremental cache path. Defaults to <out>/vault-graph-cache.json.")
    parser.add_argument("--interval", type=float, default=2.0, help="Polling interval in seconds.")
    parser.add_argument("--include-archive", action="store_true", help="Include _Archive notes in the graph.")
    parser.add_argument("--once", action="store_true", help="Build once, then exit.")
    parser.add_argument("--pid", default=None, help="Write the watcher process id to this file.")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    out_dir = Path(args.out)
    cache_path = Path(args.cache) if args.cache else build_vault_graph.default_cache_path(out_dir)

    if args.pid:
        pid_path = Path(args.pid)
        pid_path.parent.mkdir(parents=True, exist_ok=True)
        pid_path.write_text(str(os.getpid()), encoding="utf-8")

    if args.once:
        rebuild(root, out_dir, cache_path, include_archive=args.include_archive)
        return 0

    try:
        watch(root, out_dir, cache_path, args.interval, include_archive=args.include_archive)
    except KeyboardInterrupt:
        log("Stopped graph watcher.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
