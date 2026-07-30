from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Violation:
    code: str
    path: str
    detail: str


STRICT_TOP_LEVEL = {
    ".agents", ".gitignore", ".obsidian", "AGENTS.md", "00_Index.md",
    "01_Core_Vision", "02_World_Lore", "03_Factions_Societies", "04_Player_Entities",
    "05_Combat_Survival", "06_Economy_Loot", "07_Gear_Inventory", "08_World_Generation",
    "09_Project_Management", "Images", "tools",
}
STRICT_MANAGEMENT = {
    "Architecture_MVP.md", "TODO.md", "Risk_Register.md", "Refactor_Unresolved_Registry_2026-07-23.md",
}
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
ROUTE_TEXT_FIELDS = {"index_summary", "read_when"}


def project_files(root: Path) -> list[Path]:
    return [p for p in root.rglob("*") if p.is_file() and ".git" not in p.relative_to(root).parts]


def markdown_files(root: Path) -> list[Path]:
    return [p for p in project_files(root) if p.suffix.lower() == ".md"]


def frontmatter_lines(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return []
    end = text.find("\n---", 4)
    return text[4:end].splitlines() if end >= 0 else []


def parse_frontmatter(path: Path) -> dict[str, object]:
    data: dict[str, object] = {}
    for line in frontmatter_lines(path):
        if ":" not in line or line.startswith((" ", "-")):
            continue
        key, value = (part.strip() for part in line.split(":", 1))
        if value.startswith("[") and value.endswith("]"):
            data[key] = [x.strip().strip('"\'') for x in value[1:-1].split(",") if x.strip()]
        elif value.startswith('"') and value.endswith('"'):
            try:
                data[key] = json.loads(value)
            except json.JSONDecodeError:
                data[key] = value.strip('"')
        else:
            data[key] = value.strip('"\'')
    return data


def iter_wikilinks(text: str) -> Iterable[str]:
    in_dataview = False
    for line in text.splitlines():
        if line.startswith("```"):
            language = line[3:].strip().lower()
            if in_dataview:
                in_dataview = False
            elif language in {"dataview", "dataviewjs"}:
                in_dataview = True
            continue
        for match in WIKILINK.finditer(line):
            target = match.group(1)
            if not (in_dataview and "${" in target):
                yield target


def resolve_wikilink(source: Path, target: str, corpus: set[Path]) -> Path | None:
    target = target.replace("\\|", "|").split("|", 1)[0].split("#", 1)[0].split("^", 1)[0].strip()
    if not target or "${" in target:
        return None
    root = next((parent for parent in [source.parent, *source.parents] if any(p.parent == parent for p in corpus)), source.parent)
    candidates = [p for p in corpus if p.name == f"{target}.md" or p.stem == target]
    exact = [
        p for p in corpus
        if p.as_posix() in {f"{target}.md", target}
        or p.as_posix().endswith(f"/{target}.md")
        or p.as_posix().endswith(f"/{target}")
    ]
    if len(exact) == 1:
        return exact[0]
    return candidates[0] if len(candidates) == 1 else None


def check_links(root: Path) -> list[Violation]:
    corpus = set(project_files(root))
    violations: list[Violation] = []
    for source in markdown_files(root):
        for target in iter_wikilinks(source.read_text(encoding="utf-8")):
            if "${" not in target and resolve_wikilink(source, target, corpus) is None:
                violations.append(Violation("MISSING_LINK_TARGET", str(source.relative_to(root)), target))
    return violations


def check_frontmatter(root: Path) -> list[Violation]:
    violations: list[Violation] = []
    for path in markdown_files(root):
        relative = path.relative_to(root)
        if relative.parts and relative.parts[0] in {"01_Core_Vision", "02_World_Lore", "03_Factions_Societies", "04_Player_Entities", "05_Combat_Survival", "06_Economy_Loot", "07_Gear_Inventory", "08_World_Generation"}:
            data = parse_frontmatter(path)
            if data and data.get("status") != "active":
                violations.append(Violation("NONACTIVE_PAGE", str(relative), str(data.get("status"))))
            if data.get("owns") and not data.get("canonical_id"):
                violations.append(Violation("OWNER_MISSING_CANONICAL_ID", str(relative), "owns requires canonical_id"))
            for line in frontmatter_lines(path):
                key, separator, value = line.partition(":")
                if key in ROUTE_TEXT_FIELDS and separator and value.strip() and not value.lstrip().startswith(('"', "'")):
                    violations.append(Violation("ROUTE_TEXT_NOT_QUOTED", str(relative), f"{key} must be quoted"))
    return violations


def check_index(root: Path) -> list[Violation]:
    index = root / "00_Index.md"
    if not index.exists():
        return []
    corpus = set(project_files(root))
    violations: list[Violation] = []
    for target in iter_wikilinks(index.read_text(encoding="utf-8")):
        resolved = resolve_wikilink(index, target, corpus)
        if resolved is not None and resolved.suffix == ".md" and parse_frontmatter(resolved).get("status") not in (None, "active"):
            violations.append(Violation("INDEX_TARGET_NOT_ACTIVE", "00_Index.md", target))
    return violations


def check_owners(root: Path) -> list[Violation]:
    seen: dict[str, Path] = {}
    violations: list[Violation] = []
    for path in markdown_files(root):
        if path.name == "00_Index.md":
            continue
        values = parse_frontmatter(path).get("owns", [])
        if isinstance(values, str):
            values = [values]
        for value in values:
            if value in seen:
                violations.append(Violation("DUPLICATE_OWNS", str(path.relative_to(root)), f"{value}; also {seen[value].relative_to(root)}"))
            else:
                seen[value] = path
    return violations


def check_surface(root: Path, strict: bool) -> list[Violation]:
    violations: list[Violation] = []
    for local in (root / ".obsidian" / "workspace.json", root / ".obsidian" / "workspace-mobile.json", root / ".superpowers", root / "_Archive", root / "10_Reference"):
        if local.exists():
            violations.append(Violation("FORBIDDEN_LOCAL_STATE", str(local.relative_to(root)), "physically present"))
    if strict:
        for child in root.iterdir():
            if child.name != ".git" and child.name not in STRICT_TOP_LEVEL:
                violations.append(Violation("FORBIDDEN_TOP_LEVEL_PATH", child.name, "not allowlisted"))
        management = root / "09_Project_Management"
        if management.exists():
            for path in management.iterdir():
                if path.is_file() and path.suffix == ".md" and path.name not in STRICT_MANAGEMENT:
                    violations.append(Violation("FORBIDDEN_PROJECT_MANAGEMENT_FILE", str(path.relative_to(root)), "not allowlisted"))
    return violations


def run(root: Path, strict: bool) -> list[Violation]:
    return check_links(root) + check_frontmatter(root) + check_index(root) + check_owners(root) + check_surface(root, strict)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    violations = run(args.root.resolve(), args.strict)
    for violation in violations:
        print(f"{violation.code}\t{violation.path}\t{violation.detail}")
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
