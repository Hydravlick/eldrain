#!/usr/bin/env python3
"""Validate that a prose rewrite preserves protected Markdown and design data."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
from typing import Callable


def frontmatter(text: str) -> str:
    match = re.match(r"\A---\s*\n.*?\n---\s*(?:\n|\Z)", text, re.DOTALL)
    return match.group(0) if match else ""


def fenced_blocks(text: str) -> list[str]:
    blocks: list[str] = []
    current: list[str] = []
    marker = ""
    for line in text.splitlines(keepends=True):
        match = re.match(r"^\s*(```+|~~~+)", line)
        if match and not current:
            marker = match.group(1)[0]
            current = [line]
            continue
        if current:
            current.append(line)
            if match and match.group(1)[0] == marker:
                blocks.append("".join(current))
                current = []
                marker = ""
    if current:
        blocks.append("".join(current))
    return blocks


def regex_items(pattern: str, text: str, flags: int = 0) -> list[str]:
    return re.findall(pattern, text, flags)


def markdown_link_targets(text: str) -> list[str]:
    obsidian = regex_items(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text)
    markdown = regex_items(r"\[[^\]]+\]\(([^\)]+)\)", text)
    return obsidian + markdown


def compare(code: str, before: object, after: object) -> dict[str, object] | None:
    if before == after:
        return None
    return {"code": code, "before": before, "after": after}


def validate(before: str, after: str) -> list[dict[str, object]]:
    extractors: list[tuple[str, Callable[[str], object]]] = [
        ("FRONTMATTER", frontmatter),
        ("HEADING_STRUCTURE", lambda text: regex_items(r"^#{1,6}\s+.*$", text, re.MULTILINE)),
        ("FENCED_CODE", fenced_blocks),
        ("TABLE", lambda text: regex_items(r"^\s*\|.*\|\s*$", text, re.MULTILINE)),
        ("BLOCKQUOTE", lambda text: regex_items(r"^\s*>.*$", text, re.MULTILINE)),
        ("INLINE_CODE", lambda text: Counter(regex_items(r"`[^`\n]+`", text))),
        ("LINK_TARGET", lambda text: Counter(markdown_link_targets(text))),
        ("RULE_ID", lambda text: Counter(regex_items(r"\b[A-Z][A-Z0-9_]*(?:-[A-Z0-9_]+)*-\d{2,}\b", text))),
        ("NUMERIC_LITERAL", lambda text: Counter(regex_items(r"(?<![\w.])-?\d+(?:[.,]\d+)?%?", text))),
        ("FORMULA", lambda text: regex_items(r"^.*(?:=|≤|≥|\$).*$", text, re.MULTILINE)),
    ]
    violations: list[dict[str, object]] = []
    for code, extractor in extractors:
        difference = compare(code, extractor(before), extractor(after))
        if difference:
            violations.append(difference)
    return violations


def serializable(value: object) -> object:
    if isinstance(value, Counter):
        return dict(value)
    if isinstance(value, list):
        return [serializable(item) for item in value]
    if isinstance(value, dict):
        return {key: serializable(item) for key, item in value.items()}
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    args = parser.parse_args()
    violations = validate(
        args.before.read_text(encoding="utf-8"),
        args.after.read_text(encoding="utf-8"),
    )
    payload = {"valid": not violations, "violations": serializable(violations)}
    if args.json:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if violations:
            for item in violations:
                print(item["code"])
        else:
            print("Rewrite preserves protected invariants.")
    return 0 if not violations else 1


if __name__ == "__main__":
    raise SystemExit(main())
