from pathlib import Path
import tempfile
import unittest

from tools.vault_guard import check_frontmatter, check_owners

ROOT = Path(__file__).resolve().parents[1]


class ManagementHygieneTests(unittest.TestCase):
    def test_current_management_has_no_gameplay_authority_or_invalid_metadata(self):
        violations = check_frontmatter(ROOT) + check_owners(ROOT)
        self.assertEqual([v for v in violations if Path(v.path).parts[0] == "09_Project_Management"], [])

    def test_task_completion_is_independent_of_document_status(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            folder = root / "09_Project_Management"
            folder.mkdir()
            (folder / "Plan.md").write_text("---\ntype: project_plan\nstatus: active\n---\n- [x] Finished batch\n- [ ] Next batch\n", encoding="utf-8")
            self.assertEqual(check_frontmatter(root) + check_owners(root), [])

    def test_new_management_filename_is_not_a_policy_violation(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            folder = root / "09_Project_Management"
            folder.mkdir()
            (folder / "Experiment.md").write_text("---\ntype: research_plan\nstatus: deferred\n---\n", encoding="utf-8")
            self.assertEqual(check_frontmatter(root) + check_owners(root), [])


if __name__ == "__main__":
    unittest.main()
