from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable
from urllib.parse import unquote, urlsplit

try:
    from tools.document_model import ACTIVE, GAMEPLAY_ROOTS, MODEL, MetadataError, is_gameplay, load_yaml, parse_frontmatter, route_metadata
except ModuleNotFoundError:
    from document_model import ACTIVE, GAMEPLAY_ROOTS, MODEL, MetadataError, is_gameplay, load_yaml, parse_frontmatter, route_metadata


@dataclass(frozen=True)
class Violation:
    code: str
    path: str
    detail: str


WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
MARKDOWN_LINK = re.compile(r"!?\[[^\[\]\n]*\]\((<[^>]+>|[^)\n]+)\)")
EXCLUDED_DIRS = {".git", ".obsidian", ".venv", "node_modules", "__pycache__", ".stversions", ".stfolder"}


def project_files(root: Path) -> list[Path]:
    # Prune application/dependency state before walking it.
    import os
    result = []
    for base, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED_DIRS)
        result.extend(Path(base) / name for name in sorted(files))
    return result


def markdown_files(root: Path) -> list[Path]:
    return [p for p in project_files(root) if p.suffix.lower() == ".md"]


def document_text(text: str) -> str:
    """Ignore literal code examples; keep frontmatter links and ordinary embeds."""
    result = []
    fence = ""
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if not fence:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = ""
            continue
        if not fence:
            result.append(re.sub(r"(`+).*?\1", "", line))
    return "\n".join(result)


def iter_wikilinks(text: str) -> Iterable[str]:
    for match in WIKILINK.finditer(document_text(text)):
        yield match.group(1)


def link_parts(target: str) -> tuple[str, str]:
    target = target.replace("\\|", "|").split("|", 1)[0].strip()
    path, _, fragment = target.partition("#")
    return unquote(path), unquote(fragment)


def resolve_wikilink(source: Path, target: str, corpus: set[Path]) -> Path | None:
    target, _ = link_parts(target)
    if not target:
        return source
    target = target.replace("\\", "/")
    exact = [p for p in corpus if p.as_posix() in {target, target + ".md"}
             or p.as_posix().endswith("/" + target) or p.as_posix().endswith("/" + target + ".md")]
    if len(exact) == 1:
        return exact[0]
    local = [p for p in exact if p.parent == source.parent]
    if len(local) == 1 and "/" not in target:
        return local[0]
    if "/" in target:
        return None
    names = [p for p in corpus if p.name == target or p.stem == target]
    if len(names) == 1:
        return names[0]
    if not names:
        aliases = []
        for path in corpus:
            if path.suffix.lower() != ".md":
                continue
            try:
                values = parse_frontmatter(path).get("aliases", [])
            except MetadataError:
                continue
            if target in (values if isinstance(values, list) else [values]):
                aliases.append(path)
        if len(aliases) == 1:
            return aliases[0]
    return None


def fragment_exists(path: Path, fragment: str) -> bool:
    if not fragment or path.suffix.lower() != ".md":
        return True
    text = document_text(path.read_text(encoding="utf-8-sig"))
    if fragment.startswith("^"):
        return bool(re.search(r"(?m)(?:^|\s)" + re.escape(fragment) + r"\s*$", text))
    headings = re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", text)
    expected = fragment.split("#")[-1].casefold()
    return any(expected in {h.casefold(), re.sub(r"[^\w\s-]", "", h).replace(" ", "-").casefold()} for h in headings)


def check_links(root: Path, strict: bool = False) -> list[Violation]:
    corpus = set(project_files(root))
    violations = []
    for source in sorted(p for p in corpus if p.suffix.lower() == ".md"):
        text = source.read_text(encoding="utf-8-sig")
        links = [(target, resolve_wikilink(source, target, corpus), link_parts(target)[1])
                 for target in iter_wikilinks(text)]
        for match in MARKDOWN_LINK.finditer(document_text(text)):
            raw = match.group(1).strip()
            if raw.startswith("<"):
                raw = raw[1:-1]
            if urlsplit(raw).scheme or raw.startswith("//"):
                continue
            target, _, fragment = raw.partition("#")
            resolved = (source.parent / unquote(target)).resolve() if target else source
            links.append((raw, resolved if resolved.exists() else None, unquote(fragment)))
        for target, resolved, fragment in links:
            if resolved is None:
                violations.append(Violation("MISSING_LINK_TARGET", str(source.relative_to(root)), target))
            elif strict and not fragment_exists(resolved, fragment):
                violations.append(Violation("MISSING_LINK_FRAGMENT", str(source.relative_to(root)), target))
    return violations


def metadata_or_empty(path: Path) -> dict:
    try:
        return parse_frontmatter(path)
    except MetadataError:
        return {}


def check_frontmatter(root: Path) -> list[Violation]:
    violations = []
    for path in markdown_files(root):
        rel = path.relative_to(root)
        game = is_gameplay(path, root)
        management = rel.parts[0] == MODEL["management_root"]
        if not game and not management and path.name != "00_Index.md":
            continue
        try:
            data = parse_frontmatter(path)
        except MetadataError as exc:
            violations.append(Violation("INVALID_YAML", str(rel), str(exc)))
            continue
        if game:
            for key in ("type", "status", "system"):
                if not isinstance(data.get(key), str) or not data[key].strip():
                    violations.append(Violation("MISSING_METADATA", str(rel), key))
            for key, value in data.items():
                if isinstance(value, dict) or (isinstance(value, list) and any(isinstance(v, (dict, list)) for v in value)):
                    violations.append(Violation("NONFLAT_PROPERTY", str(rel), key))
        if "status" in data and (not isinstance(data["status"], str) or data["status"] not in MODEL["statuses"]):
            violations.append(Violation("INVALID_STATUS", str(rel), str(data["status"])))
        if data.get("index_route") not in (None, "owner"):
            violations.append(Violation("INVALID_ROUTE_ROLE", str(rel), str(data["index_route"])))
        if data.get("index_route") == "owner" and data.get("status") == ACTIVE:
            if not game:
                violations.append(Violation("ROUTE_OUTSIDE_GAMEPLAY", str(rel), "route owner must be in a gameplay domain"))
            for error in route_metadata(data):
                violations.append(Violation("INVALID_ROUTE_METADATA", str(rel), error))
        if data.get("owns") and not data.get("canonical_id"):
            violations.append(Violation("OWNER_MISSING_CANONICAL_ID", str(rel), "owns requires canonical_id"))
        if game and data.get("status") == ACTIVE and data.get("canonical_id") and data.get("index_route") != "owner":
            violations.append(Violation("OWNER_NOT_ROUTABLE", str(rel), "declared active owner requires a route"))
        for field in ("canonical_id", "feature_id"):
            if field in data and (not isinstance(data[field], str) or not data[field].strip()):
                violations.append(Violation("INVALID_OWNER_METADATA", str(rel), field))
        if "owns" in data:
            values = data["owns"] if isinstance(data["owns"], list) else [data["owns"]]
            if any(not isinstance(v, str) or not v.strip() for v in values):
                violations.append(Violation("INVALID_OWNER_METADATA", str(rel), "owns must contain rule keys"))
    return violations


def check_index(root: Path) -> list[Violation]:
    corpus = set(project_files(root))
    violations = []
    for index in [root / "00_Index.md", *(root / name / "00_Routes.md" for name in GAMEPLAY_ROOTS)]:
        if not index.exists():
            continue
        for target in iter_wikilinks(index.read_text(encoding="utf-8-sig")):
            path = resolve_wikilink(index, target, corpus)
            if path and path.suffix == ".md" and metadata_or_empty(path).get("status") != ACTIVE:
                violations.append(Violation("INDEX_TARGET_NOT_ACTIVE", str(index.relative_to(root)), target))
    return violations


def check_owners(root: Path) -> list[Violation]:
    seen = {}
    violations = []
    for path in markdown_files(root):
        data = metadata_or_empty(path)
        if data.get("status") != ACTIVE:
            continue
        if data.get("type") == "view":
            # Derived views have their own contract, never an ownership claim.
            continue
        rel = str(path.relative_to(root))
        if not is_gameplay(path, root):
            management_rule = path.relative_to(root).parts[0] == MODEL["management_root"] and data.get("type") in MODEL["system_types"]
            if data.get("owns") or data.get("canonical_id") or data.get("type") == "feature" or management_rule:
                violations.append(Violation("OWNERSHIP_OUTSIDE_GAMEPLAY", rel, "context/management cannot own gameplay"))
            continue
        if data.get("type") == "feature" and (data.get("owns") or data.get("canonical_id")):
            violations.append(Violation("FEATURE_RULE_OWNERSHIP", rel, "feature references system owners"))
        owns = data.get("owns", [])
        owns = owns if isinstance(owns, list) else [owns]
        entries = [("DUPLICATE_OWNS", v) for v in owns]
        entries += [(f"DUPLICATE_{key.upper()}", data[key]) for key in ("canonical_id", "feature_id") if data.get(key)]
        for code, value in entries:
            if not isinstance(value, str):
                continue
            key = (code, value)
            if key in seen:
                violations.append(Violation(code, rel, f"{value}; also {seen[key]}"))
            else:
                seen[key] = rel
    return violations


def check_features(root: Path) -> list[Violation]:
    corpus = set(project_files(root))
    violations = []
    for path in markdown_files(root):
        data = metadata_or_empty(path)
        if data.get("type") != "feature":
            continue
        rel = str(path.relative_to(root))
        if data.get("status") == ACTIVE:
            for key in MODEL["feature_required"]:
                if not data.get(key):
                    violations.append(Violation("FEATURE_MISSING_FIELD", rel, key))
        if data.get("owns") or data.get("canonical_id"):
            if data.get("status") != ACTIVE:
                violations.append(Violation("FEATURE_RULE_OWNERSHIP", rel, "feature references system owners"))
        for key in MODEL["feature_link_lists"]:
            if key not in data:
                continue
            values = data[key]
            if not isinstance(values, list) or any(not isinstance(v, str) or not WIKILINK.fullmatch(v) for v in values):
                violations.append(Violation("FEATURE_INVALID_LINK_LIST", rel, key))
                continue
            for value in values:
                target = resolve_wikilink(path, value[2:-2], corpus)
                target_data = metadata_or_empty(target) if target and target.suffix == ".md" else {}
                if not target:
                    violations.append(Violation("FEATURE_MISSING_TARGET", rel, value))
                elif key == "system_owners" and not (
                    is_gameplay(target, root) and target_data.get("status") == ACTIVE
                    and target_data.get("index_route") == "owner"
                    and target_data.get("type") in MODEL["system_types"]
                ):
                    violations.append(Violation("FEATURE_INVALID_SYSTEM_OWNER", rel, value))
        if "production_disciplines" in data and (
            not isinstance(data["production_disciplines"], list)
            or any(not isinstance(v, str) for v in data["production_disciplines"])
        ):
            violations.append(Violation("FEATURE_INVALID_DISCIPLINES", rel, "expected text list"))
    return violations


def check_views(root: Path) -> list[Violation]:
    corpus = set(project_files(root))
    violations = []
    source_field = MODEL["view"]["sources_field"]
    for path in markdown_files(root):
        data = metadata_or_empty(path)
        if data.get("type") != "view":
            continue
        rel = str(path.relative_to(root))
        for field in MODEL["view"]["forbidden_owner_fields"]:
            if field in data:
                violations.append(Violation("VIEW_RULE_OWNERSHIP", rel, field))
        values = data.get(source_field)
        if data.get("status") == ACTIVE and not values:
            violations.append(Violation("VIEW_MISSING_SOURCES", rel, source_field))
        if source_field not in data:
            continue
        if not isinstance(values, list) or any(not isinstance(v, str) or not WIKILINK.fullmatch(v) for v in values):
            violations.append(Violation("VIEW_INVALID_SOURCES", rel, "expected a list of quoted wikilinks"))
            continue
        for value in values:
            target = resolve_wikilink(path, value[2:-2], corpus)
            if target is None:
                violations.append(Violation("VIEW_MISSING_TARGET", rel, value))
            elif target == path:
                violations.append(Violation("VIEW_SELF_SOURCE", rel, value))
    return violations


def check_bases(root: Path) -> list[Violation]:
    violations = []
    for path in project_files(root):
        if path.suffix.lower() != ".base":
            continue
        rel = str(path.relative_to(root))
        try:
            data = load_yaml(path.read_text(encoding="utf-8-sig"))
        except MetadataError as exc:
            violations.append(Violation("INVALID_BASE_YAML", rel, str(exc)))
            continue
        unknown = data.keys() - {"filters", "formulas", "properties", "summaries", "views"}
        if unknown:
            violations.append(Violation("BASE_NONVIEW_DATA", rel, ", ".join(sorted(unknown))))
        views = data.get("views")
        if not isinstance(views, list) or not views or any(not isinstance(v, dict) or not v.get("type") or not v.get("name") for v in views):
            violations.append(Violation("BASE_INVALID_VIEWS", rel, "nonempty named view definitions required"))
            views = []
        def valid_filter(value):
            if isinstance(value, str):
                return bool(value.strip())
            if not isinstance(value, dict) or len(value) != 1:
                return False
            operator, items = next(iter(value.items()))
            return operator in {"and", "or", "not"} and isinstance(items, list) and bool(items) and all(valid_filter(v) for v in items)
        filters = [data["filters"]] if "filters" in data else []
        filters.extend(v["filters"] for v in views if "filters" in v)
        if (not filters or any(not valid_filter(f) for f in filters)
                or ("filters" not in data and any("filters" not in v for v in views))):
            violations.append(Violation("BASE_INVALID_FILTERS", rel, "each view needs a valid source filter, global or local"))
        if any(set(v) & {"owns", "canonical_id", "records", "rows", "data"} for v in views):
            violations.append(Violation("BASE_NONVIEW_DATA", rel, "view contains stored records/authority"))
        formulas = data.get("formulas", {})
        if not isinstance(formulas, dict) or any(not isinstance(v, str) for v in formulas.values()):
            violations.append(Violation("BASE_INVALID_FORMULAS", rel, "expected expression mapping"))
            formulas = {}
        def strings(value):
            if isinstance(value, str):
                yield value
            elif isinstance(value, dict):
                for k, v in value.items():
                    yield k
                    yield from strings(v)
            elif isinstance(value, list):
                for item in value:
                    yield from strings(item)
        references = set(re.findall(r"\bformula\.([\w]+)", "\n".join(strings(data))))
        for name in sorted(references - formulas.keys()):
            violations.append(Violation("BASE_UNDEFINED_FORMULA", rel, name))
    return violations


def check_surface(root: Path, strict: bool = False) -> list[Violation]:
    """Application state and contextual directories are legitimate vault surfaces."""
    return check_bases(root)


def run(root: Path, strict: bool = False) -> list[Violation]:
    return (check_frontmatter(root) + check_links(root, strict) + check_index(root)
            + check_owners(root) + check_features(root) + check_views(root) + check_surface(root, strict))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate vault structure; --strict adds deep-link fragments.")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    violations = run(args.root.resolve(), args.strict)
    for violation in violations:
        print(f"{violation.code}\t{violation.path}\t{violation.detail}")
    print(f"Vault guard: {len(violations)} violation(s)")
    return int(bool(violations))


if __name__ == "__main__":
    raise SystemExit(main())
