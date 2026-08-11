from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))


class CanonicalGuidanceTests(unittest.TestCase):
    def test_agents_limits_current_corpus_to_zero_through_nine(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("`00_Index.md` and the `01_` through `09_` directories", agents)
        self.assertIn("Active owner pages under `01_` through `08_` establish current game rules", agents)

    def test_agents_allows_context_without_canon_authority(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Contextual materials may be opened without a separate user request", agents)
        self.assertIn("Current-canon claims cite active owners", agents)

    def test_every_eldraine_skill_has_affirmative_canon_language(self) -> None:
        self.assertEqual(len(SKILLS), 11)
        for skill in SKILLS:
            text = skill.read_text(encoding="utf-8")
            self.assertIn("## Active Canon Language", text, skill.as_posix())
            self.assertIn("Describe the accepted target state affirmatively", text, skill.as_posix())
            self.assertIn("Historical context belongs outside active rule statements", text, skill.as_posix())


if __name__ == "__main__":
    unittest.main()
