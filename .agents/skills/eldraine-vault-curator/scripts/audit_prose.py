#!/usr/bin/env python3
"""Detect prose-health candidates in bounded Markdown files without rewriting."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Iterable


FORMULAIC_PATTERNS = (
    re.compile(r"\bне\s+(?:просто|только)\b.{0,140}\b(?:а|но\s+и)\b", re.IGNORECASE),
    re.compile(r"\b(?:важно|стоит)\s+(?:отметить|подчеркнуть)\b", re.IGNORECASE),
    re.compile(r"\bв\s+конечном\s+сч[её]те\b", re.IGNORECASE),
    re.compile(r"\b(?:not\s+just|not\s+only)\b.{0,140}\b(?:but|but\s+also)\b", re.IGNORECASE),
)


def prose_lines(text: str) -> list[tuple[int, str]]:
    """Return lines eligible for prose checks, excluding protected Markdown."""
    result: list[tuple[int, str]] = []
    in_frontmatter = False
    in_fence = False
    fence = ""
    for number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if number == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue
        fence_match = re.match(r"^\s*(```+|~~~+)", line)
        if fence_match:
            marker = fence_match.group(1)[0]
            if not in_fence:
                in_fence = True
                fence = marker
            elif marker == fence:
                in_fence = False
                fence = ""
            continue
        if in_fence or not stripped:
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            continue
        if stripped.startswith(("#", ">")):
            continue
        cleaned = re.sub(r"`[^`\n]+`", "", line)
        cleaned = re.sub(r"\[\[[^\]|]+(?:\|([^\]]+))?\]\]", lambda m: m.group(1) or "", cleaned)
        cleaned = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", cleaned)
        if cleaned.strip():
            result.append((number, cleaned.strip()))
    return result


def finding(code: str, path: Path, line: int, evidence: str, reason: str, severity: str) -> dict[str, object]:
    return {
        "code": code,
        "path": str(path),
        "line": line,
        "evidence": evidence,
        "reason": reason,
        "severity": severity,
    }


def audit_text(path: Path, text: str) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    eligible = prose_lines(text)
    for line_number, line in eligible:
        for pattern in FORMULAIC_PATTERNS:
            if pattern.search(line):
                findings.append(
                    finding(
                        "FORMULAIC_PROSE",
                        path,
                        line_number,
                        line,
                        "Formulaic contrast or announcement may be hiding the concrete rule.",
                        "medium",
                    )
                )
                break

    paragraphs: list[tuple[int, str]] = []
    current_line = 0
    current: list[str] = []
    previous = 0
    for line_number, line in eligible:
        if re.match(r"^(?:[-*+]\s+|\d+[.)]\s+)", line):
            if current:
                paragraphs.append((current_line, " ".join(current)))
                current = []
            paragraphs.append((line_number, line))
            previous = line_number
            continue
        if current and line_number > previous + 1:
            paragraphs.append((current_line, " ".join(current)))
            current = []
        if not current:
            current_line = line_number
        current.append(line)
        previous = line_number
    if current:
        paragraphs.append((current_line, " ".join(current)))

    for line_number, paragraph in paragraphs:
        if len(re.findall(r"\b[\w-]+\b", paragraph, re.UNICODE)) > 140:
            findings.append(
                finding(
                    "OVERLONG_PARAGRAPH",
                    path,
                    line_number,
                    paragraph[:240],
                    "Paragraph exceeds 140 words and may bury the adopted rule.",
                    "low",
                )
            )

    seen: dict[str, int] = {}
    for line_number, line in eligible:
        for sentence in re.split(r"(?<=[.!?])\s+", line):
            normalized = re.sub(r"[^\w]+", " ", sentence.casefold()).strip()
            if len(normalized) < 30:
                continue
            if normalized in seen:
                findings.append(
                    finding(
                        "DUPLICATE_SENTENCE",
                        path,
                        line_number,
                        sentence,
                        f"Sentence repeats line {seen[normalized]}.",
                        "medium",
                    )
                )
            else:
                seen[normalized] = line_number
    return findings


def audit_paths(paths: Iterable[Path]) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    for path in paths:
        findings.extend(audit_text(path, path.read_text(encoding="utf-8")))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    findings = audit_paths(args.paths)
    payload = {"findings": findings, "count": len(findings)}
    if args.json:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for item in findings:
            print(f"{item['path']}:{item['line']} {item['code']}: {item['evidence']}")
        print(f"Findings: {len(findings)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
