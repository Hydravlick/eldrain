import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "eldraine-vault-curator"
AUDITOR = SKILL / "scripts" / "audit_prose.py"
VALIDATOR = SKILL / "scripts" / "validate_rewrite.py"


class VaultCuratorToolTests(unittest.TestCase):
    def run_auditor(self, content: str) -> dict:
        self.assertTrue(AUDITOR.exists(), "audit_prose.py is missing")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "note.md"
            path.write_text(content, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(AUDITOR), "--json", str(path)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def run_validator(self, before: str, after: str) -> subprocess.CompletedProcess[str]:
        self.assertTrue(VALIDATOR.exists(), "validate_rewrite.py is missing")
        with tempfile.TemporaryDirectory() as tmp:
            before_path = Path(tmp) / "before.md"
            after_path = Path(tmp) / "after.md"
            before_path.write_text(before, encoding="utf-8")
            after_path.write_text(after, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(VALIDATOR), "--json", str(before_path), str(after_path)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )

    def test_auditor_detects_russian_formulaic_contrast(self) -> None:
        result = self.run_auditor(
            "# Механика\n\nЭто не просто поручение, а мощная система живого хаба.\n"
        )
        codes = {finding["code"] for finding in result["findings"]}
        self.assertIn("FORMULAIC_PROSE", codes)

    def test_auditor_ignores_protected_markdown_regions(self) -> None:
        result = self.run_auditor(
            "---\nsummary: не просто поле, а значение\n---\n\n"
            "```text\nЭто не просто код, а пример.\n```\n\n"
            "| Правило | Это не просто таблица, а запись |\n"
            "|---|---|\n"
        )
        self.assertEqual(result["findings"], [])

    def test_auditor_does_not_merge_list_items_into_long_paragraph(self) -> None:
        content = "# Contract\n\n" + "\n".join(
            f"{index}. One bounded rule." for index in range(1, 61)
        )
        result = self.run_auditor(content)
        codes = {finding["code"] for finding in result["findings"]}
        self.assertNotIn("OVERLONG_PARAGRAPH", codes)

    def test_validator_accepts_prose_only_rewrite(self) -> None:
        before = (
            "---\ntype: system\n---\n# Rule SYS-001\n\n"
            "The system has 10 charges. See [[Path/Owner|Owner]].\n\n"
            "| ID | Value |\n|---|---|\n| SYS-001 | 10 |\n\n"
            "```python\nvalue = 10\n```\n"
        )
        after = before.replace("The system has", "The rule grants")
        result = self.run_validator(before, after)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(json.loads(result.stdout)["valid"])

    def test_validator_rejects_changed_number(self) -> None:
        result = self.run_validator("# Rule\n\nCost: 10.\n", "# Rule\n\nCost: 12.\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("NUMERIC_LITERAL", {item["code"] for item in json.loads(result.stdout)["violations"]})

    def test_validator_rejects_changed_link_target(self) -> None:
        result = self.run_validator(
            "# Rule\n\nSee [[Path/Owner|Owner]].\n",
            "# Rule\n\nSee [[Path/Other|Owner]].\n",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("LINK_TARGET", {item["code"] for item in json.loads(result.stdout)["violations"]})

    def test_validator_rejects_changed_protected_structure(self) -> None:
        before = "---\ntype: system\n---\n# Rule\n\n```text\nA\n```\n"
        after = "---\ntype: lore\n---\n## Rule\n\n```text\nB\n```\n"
        result = self.run_validator(before, after)
        self.assertNotEqual(result.returncode, 0)
        codes = {item["code"] for item in json.loads(result.stdout)["violations"]}
        self.assertTrue({"FRONTMATTER", "HEADING_STRUCTURE", "FENCED_CODE"}.issubset(codes))


if __name__ == "__main__":
    unittest.main()
