from pathlib import Path
import tempfile
import unittest

from tools.check_harness import check, discover
from tools.build_routes import DOMAINS, check as check_routes
from tools.document_model import GAMEPLAY_ROOTS

ROOT = Path(__file__).resolve().parents[1]


class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def skill(self, name="example", body="Do the requested work."):
        return self.write(f".agents/skills/{name}/SKILL.md",
                          f"---\nname: {name}\ndescription: A bounded operation.\n---\n{body}\n")

    def codes(self):
        return {v.code for v in check(self.root)}

    def test_discovery_follows_actual_skill_files(self):
        self.skill("first")
        self.skill("second")
        self.write(".agents/references/playbook.md", "# Supporting workflow")
        self.assertEqual(set(discover(self.root)), {"first", "second"})
        self.assertEqual(check(self.root), [])

    def test_missing_skills_is_reported(self):
        self.assertIn("NO_SKILLS", self.codes())

    def test_invalid_skill_metadata_is_reported(self):
        self.write(".agents/skills/example/SKILL.md", "---\nname: wrong\ndescription: ''\n---\n")
        self.assertTrue({"INVALID_SKILL_NAME", "MISSING_SKILL_DESCRIPTION"} <= self.codes())

    def test_missing_reference_is_reported(self):
        self.skill(body="[Policy](../../policies/missing.md)")
        self.assertIn("MISSING_HARNESS_RESOURCE", self.codes())

    def test_progressive_reference_links_resolve(self):
        self.skill(body="[Policy](../../policies/canon.md)")
        self.write(".agents/policies/canon.md", "[Detail](../references/detail.md)")
        self.write(".agents/references/detail.md", "# Detail")
        self.assertEqual(check(self.root), [])

    def test_policy_is_boolean_not_string(self):
        self.skill()
        self.write(".agents/skills/example/agents/openai.yaml", 'policy:\n  allow_implicit_invocation: "true"\n')
        self.assertIn("INVALID_INVOCATION_POLICY", self.codes())

    def test_optional_ui_can_invoke_actual_skill(self):
        self.skill()
        self.write(".agents/skills/example/agents/openai.yaml", 'interface:\n  default_prompt: "Use $example to do this."\npolicy:\n  allow_implicit_invocation: true\n')
        self.assertEqual(check(self.root), [])

    def test_ui_cannot_invoke_deleted_skill(self):
        self.skill()
        self.write(".agents/skills/example/agents/openai.yaml", 'interface:\n  default_prompt: "Use $obsolete."\n')
        self.assertIn("INVALID_SKILL_INVOCATION", self.codes())

    def test_operational_map_cannot_route_to_missing_local_skill(self):
        self.skill()
        self.write("AGENTS.md", "Use `eldraine-obsolete`.")
        self.assertIn("UNKNOWN_LOCAL_SKILL", self.codes())

    def test_repository_harness_resources_and_discovery_are_valid(self):
        self.assertEqual(check(ROOT), [])

    def test_document_model_and_route_domains_agree(self):
        self.assertEqual(set(DOMAINS), GAMEPLAY_ROOTS)

    def test_current_generated_routes_are_reproducible(self):
        self.assertEqual(check_routes(ROOT), [])


if __name__ == "__main__":
    unittest.main()
