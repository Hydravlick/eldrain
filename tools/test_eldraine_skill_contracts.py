from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read_skill(name: str) -> str:
    path = ROOT / ".agents" / "skills" / name / "SKILL.md"
    return path.read_text(encoding="utf-8") if path.exists() else ""


class EldraineSkillContractTests(unittest.TestCase):
    def assert_terms(self, skill: str, *terms: str) -> None:
        text = read_skill(skill)
        self.assertTrue(text, f"missing skill: {skill}")
        for term in terms:
            self.assertIn(term, text, f"{skill} is missing contract term: {term}")

    def test_curator_is_explicit_and_detect_first(self) -> None:
        self.assert_terms(
            "eldraine-vault-curator",
            "Detect First",
            "explicit approval",
            "smallest safe repair",
            "FORMULAIC_PROSE",
            "Protected Invariants",
        )
        metadata = ROOT / ".agents" / "skills" / "eldraine-vault-curator" / "agents" / "openai.yaml"
        self.assertTrue(metadata.exists(), "curator UI metadata is missing")
        self.assertIn("allow_implicit_invocation: false", metadata.read_text(encoding="utf-8"))

    def test_curator_has_valid_minimal_frontmatter(self) -> None:
        text = read_skill("eldraine-vault-curator")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        self.assertIsNotNone(match, "curator frontmatter is missing")
        fields = {}
        for line in match.group(1).splitlines():
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
        self.assertEqual(set(fields), {"name", "description"})
        self.assertEqual(fields["name"], "eldraine-vault-curator")
        self.assertTrue(fields["description"].startswith("Use when"))
        self.assertNotIn("TODO", text)
        self.assertLess(len(text.splitlines()), 500)

    def test_architect_formalizes_rules_and_dependencies(self) -> None:
        self.assert_terms(
            "eldraine-system-architect",
            "PRECONDITION",
            "TRIGGER",
            "RESOLUTION",
            "POSTCONDITION",
            "Orphan rule",
            "Circular dependency",
            "Bottleneck rule",
            "Validation hypothesis",
        )

    def test_balance_modeler_has_complete_formula_contract(self) -> None:
        self.assert_terms(
            "eldraine-balance-modeler",
            "Canonical owner",
            "Evidence status",
            "Valid range",
            "Normal output",
            "Extreme behavior",
            "Worked example",
            "Tuning knobs",
            "Breakpoints",
        )

    def test_gdd_author_separates_experience_rule_and_implementation(self) -> None:
        self.assert_terms(
            "eldraine-gdd-author",
            "Executable Mechanic Contract",
            "Player promise",
            "Player loop",
            "Rule state machine",
            "Behavior versus implementation",
            "Function pass",
            "Rule pass",
            "Voice pass",
            "Brevity pass",
        )

    def test_crash_test_covers_lifecycle_and_concurrency_edges(self) -> None:
        self.assert_terms(
            "eldraine-crash-test",
            "Simultaneous events",
            "Cancellation mid-process",
            "Invalid or lost target",
            "Unavailable POI",
            "Conflicting reservation",
            "Save/load",
            "Offline time skip",
            "Pawn unavailable",
        )

    def test_player_experience_has_feel_axes_and_observable_test(self) -> None:
        self.assert_terms(
            "eldraine-player-experience",
            "Responsiveness",
            "Impact",
            "Rhythm",
            "Clarity",
            "Payoff",
            "Observable playtest",
        )

    def test_lorekeeper_has_voice_and_delivery_contracts(self) -> None:
        self.assert_terms(
            "eldraine-lorekeeper",
            "Voice Pillars",
            "SURFACE",
            "ENGAGED",
            "DEEP",
            "causal rule required for play",
            "What They Would Never Say",
        )

    def test_narrative_impact_maps_gameplay_visibility(self) -> None:
        self.assert_terms(
            "eldraine-narrative-impact",
            "Story beat",
            "World-state change",
            "Gameplay surface",
            "Observation point",
            "Player interpretation",
            "Visibility delay",
            "Canonical owner",
        )

    def test_location_designer_has_bounded_environmental_story_brief(self) -> None:
        self.assert_terms(
            "eldraine-location-designer",
            "Environmental Storytelling Brief",
            "What happened here",
            "What the player should infer",
            "What remains mysterious",
            "narratively significant POI",
        )


if __name__ == "__main__":
    unittest.main()
