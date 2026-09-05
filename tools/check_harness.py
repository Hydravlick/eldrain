"""Check discoverability and local resource integrity, independent of prompt wording."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

try:
    from tools.document_model import MetadataError, load_yaml, parse_frontmatter
    from tools.vault_guard import MARKDOWN_LINK, Violation, document_text
except ModuleNotFoundError:
    from document_model import MetadataError, load_yaml, parse_frontmatter
    from vault_guard import MARKDOWN_LINK, Violation, document_text


def discover(root: Path) -> dict[str, Path]:
    return {path.parent.name: path for path in sorted((root / ".agents/skills").glob("*/SKILL.md"))}


def check(root: Path) -> list[Violation]:
    skills = discover(root)
    violations = []
    if not skills:
        violations.append(Violation("NO_SKILLS", ".agents/skills", "no discoverable SKILL.md"))
    for name, path in skills.items():
        rel = str(path.relative_to(root))
        try:
            data = parse_frontmatter(path)
        except MetadataError as exc:
            violations.append(Violation("INVALID_SKILL_YAML", rel, str(exc)))
            continue
        if data.get("name") != name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            violations.append(Violation("INVALID_SKILL_NAME", rel, name))
        if not isinstance(data.get("description"), str) or not data["description"].strip():
            violations.append(Violation("MISSING_SKILL_DESCRIPTION", rel, name))
        ui = path.parent / "agents/openai.yaml"
        if not ui.exists():
            continue
        try:
            metadata = load_yaml(ui.read_text(encoding="utf-8-sig"))
        except MetadataError as exc:
            violations.append(Violation("INVALID_SKILL_UI", str(ui.relative_to(root)), str(exc)))
            continue
        policy = metadata.get("policy", {})
        interface = metadata.get("interface", {})
        if not isinstance(policy, dict) or type(policy.get("allow_implicit_invocation", True)) is not bool:
            violations.append(Violation("INVALID_INVOCATION_POLICY", rel, "expected boolean"))
        if not isinstance(interface, dict):
            violations.append(Violation("INVALID_SKILL_UI", rel, "interface must be a mapping"))
        else:
            prompt = interface.get("default_prompt", "")
            if not isinstance(prompt, str) or (prompt and f"${name}" not in prompt):
                violations.append(Violation("INVALID_SKILL_INVOCATION", rel, "default prompt must invoke this skill"))
    sources = list((root / ".agents").rglob("*.md"))
    if (root / "AGENTS.md").exists():
        sources.append(root / "AGENTS.md")
    for path in sources:
        text = path.read_text(encoding="utf-8-sig")
        for match in MARKDOWN_LINK.finditer(document_text(text)):
            target = match.group(1).strip("<>").split("#", 1)[0]
            if not target or urlsplit(target).scheme:
                continue
            if not (path.parent / unquote(target)).exists():
                violations.append(Violation("MISSING_HARNESS_RESOURCE", str(path.relative_to(root)), target))
        for name in set(re.findall(r"\beldraine-[a-z]+(?:-[a-z]+)*", text)):
            if name not in skills:
                violations.append(Violation("UNKNOWN_LOCAL_SKILL", str(path.relative_to(root)), name))
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    root = args.root.resolve()
    violations = check(root)
    for violation in violations:
        print(f"{violation.code}\t{violation.path}\t{violation.detail}")
    print(f"Harness: {len(discover(root))} skills, {len(violations)} violation(s)")
    return int(bool(violations))


if __name__ == "__main__":
    raise SystemExit(main())
