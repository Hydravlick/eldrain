import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANAGEMENT = ROOT / "09_Project_Management"


class ManagementHygieneTests(unittest.TestCase):
    def test_risk_register_has_only_active_statuses(self) -> None:
        text = (MANAGEMENT / "Risk_Register.md").read_text(encoding="utf-8")
        mvp_decisions, _ = text.split("## Оставить На Потом", 1)
        rows = [
            line
            for line in mvp_decisions.splitlines()
            if re.match(r"^\| R\d+ \|", line)
        ]
        statuses = {line.split("|")[4].strip() for line in rows}
        self.assertTrue(statuses <= {"in_progress"}, statuses)

    def test_active_plans_have_no_completed_checkbox(self) -> None:
        for path in MANAGEMENT.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            frontmatter = text.split("---", 2)[1] if text.startswith("---") else ""
            is_active_plan = "status: active" in frontmatter and (
                "type: project_plan" in frontmatter or "type: implementation_plan" in frontmatter
            )
            if is_active_plan:
                self.assertNotRegex(text, r"(?m)^- \[[xX]\]", path.name)


if __name__ == "__main__":
    unittest.main()
