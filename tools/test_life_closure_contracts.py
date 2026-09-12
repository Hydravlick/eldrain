"""Batch 9B declaration/ownership guards; no gameplay or UX simulation."""
import copy
import re
import unittest
from pathlib import Path

from tools.check_overhaul_contracts import read_named_contract
from tools.document_model import GAMEPLAY_ROOTS, parse_frontmatter
from tools.vault_guard import fragment_exists, iter_wikilinks, link_parts, project_files, resolve_wikilink


ROOT = Path(__file__).resolve().parents[1]
LIFE = '04_Player_Entities/Life_Closure.md'
ROSTER = '04_Player_Entities/Lifecycle_Roster.md'
IDENTITY = '04_Player_Entities/Entity_Grimoire.md'
CONSUMERS = [
    '04_Player_Entities/Tags_System.md',
    '04_Player_Entities/Shell_Construction.md',
    '01_Core_Vision/Features/Pawn_Lifecycle.md',
    '03_Factions_Societies/Quest_Engine.md',
    '03_Factions_Societies/Reputation_Rules.md',
    '03_Factions_Societies/Pledge_Contracts.md',
    '04_Player_Entities/Grimoire_Truth_Triangulation.md',
    '06_Economy_Loot/Barter_System.md',
    '06_Economy_Loot/Vendor_Logic.md',
    '08_World_Generation/Hub/Hub_Services_Interaction.md',
    '03_Factions_Societies/Lore/The_Keepers.md',
    '02_World_Lore/The_Anchor.md',
]


class LifeClosureContractsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.life = read_named_contract(ROOT / LIFE, 'life_closure_contract')
        cls.roster = read_named_contract(ROOT / ROSTER, 'closure_roster_projection')
        cls.recognition = read_named_contract(ROOT / IDENTITY, 'keeper_recognition_boundary')

    def assert_offer(self, contract):
        self.assertEqual(contract['eligibility'], 'authored_history_facts_and_terminal_opportunity')
        self.assertIs(contract['universal_progress_gate'], False)
        self.assertEqual(contract['specific_fact_requirement'], 'causal_only')
        self.assertEqual(contract['offer_state'], 'OFFER_AVAILABLE')
        self.assertEqual(set(contract['accept_requires']), {
            'explicit_confirmation', 'living_ready_pawn_in_hub',
            'valid_offer_conditions', 'authoritative_presence'})
        self.assertEqual(contract['decline_scope'], 'specific_offer')
        self.assertIs(contract['decline_irreversible'], True)
        self.assertIs(contract['independent_future_offer_allowed'], True)
        self.assertEqual(contract['defer'], 'same_offer_while_real_conditions_hold')
        self.assertEqual(contract['reroll_sources'], [])
        self.assertIs(contract['immediate_hub_decision_required'], False)
        self.assertIs(contract['artificial_pressure_timer'], False)

    def assert_consequence(self, contract):
        self.assertEqual(set(contract['downstream_requires']), {
            'named_owner', 'specific_unresolved_matter',
            'new_terminal_causal_fact', 'specifically_authored_consequence'})
        self.assertEqual(contract['downstream_result_unit'], 'unresolved_matter_and_terminal_action')
        self.assertEqual(set(contract['downstream_dedup']), {
            'resolution_delivery', 'same_cause_across_pawn_ids'})
        for key in ('generic_per_pawn_payout', 'generic_account_power',
                    'pawn_metrics_as_reward', 'closed_pawn_as_service_condition'):
            self.assertIs(contract[key], False)
        self.assertEqual(contract['result_continuation_owner'], 'result_domain')

    def test_optional_life_ending_has_no_universal_trait_gate(self):
        self.assertEqual(self.life['owner'], 'LIFE_CLOSURE')
        self.assertEqual(self.life['role'], 'optional_field_life_ending')
        self.assertEqual(self.life['long_life_without_closure'], 'valid')
        self.assertIs(self.life['ordinary_reward_required'], False)
        self.assert_offer(self.life)

    def test_refusal_defer_and_confirmation_are_offer_scoped(self):
        self.assert_offer(self.life)
        self.assertIs(self.roster['offer_alone_changes_readiness'], False)
        self.assertIs(self.roster['declined_offer_changes_readiness'], False)

    def test_accepted_civic_resolution_is_terminal_roster_input(self):
        self.assertEqual(self.life['result'], 'immutable_LifeClosureResolution')
        self.assertEqual(self.life['ordinary_outcome'], 'CLOSED_CIVIC')
        self.assertEqual(self.roster['owner'], 'LIFECYCLE_ROSTER')
        self.assertEqual(self.roster['source'], 'LifeClosureResolution')
        self.assertEqual(self.roster['accepted_civic_state'], 'CLOSED')
        self.assertEqual(self.roster['repeated_resolution'], 'same_projection')
        for key in ('accepted_redeploy', 'accepted_recruit_or_spawn',
                    'accepted_ordinary_cargo', 'inherited_embodied_value'):
            self.assertIs(self.life[key], False)
        self.assertIs(self.roster['accepted_civic_deployable'], False)
        self.assertIs(self.roster['accepted_civic_recruitable'], False)

    def test_death_and_completed_work_cannot_mint_closure_rewards(self):
        self.assertIs(self.life['death_creates_closure'], False)
        self.assertEqual(self.life['unfinished_work'], 're_evaluate_by_work_owner')
        self.assertEqual(self.life['completed_result_timing'], 'work_completion')
        self.assertIs(self.life['completed_result_reissued'], False)

    def test_downstream_requires_owner_and_new_terminal_cause(self):
        self.assert_consequence(self.life)

    def test_new_pawn_id_cannot_repeat_a_resolved_matter(self):
        self.assert_consequence(self.life)
        for change in ({'downstream_result_unit': 'PawnID'},
                       {'downstream_dedup': ['resolution_delivery']},
                       {'generic_per_pawn_payout': True}):
            candidate = dict(self.life, **change)
            with self.subTest(change=change), self.assertRaises(AssertionError):
                self.assert_consequence(candidate)

    def test_closed_pawn_is_not_a_passive_service_dependency(self):
        self.assert_consequence(self.life)
        with self.assertRaises(AssertionError):
            self.assert_consequence(dict(self.life, closed_pawn_as_service_condition=True))

    def test_recognition_is_not_a_counter_or_terminal_reward(self):
        self.assertEqual(self.recognition['basis'], 'consequences_across_lives')
        for key in ('closure_counter', 'death_counter', 'retired_counter',
                    'biography_score', 'implies_pawn_terminal_offer', 'implies_terminal_reward'):
            self.assertIs(self.recognition[key], False)
        for key in ('keeper_recognition_creates_offer', 'keeper_recognition_counter',
                    'keeper_terminal_branch_registered'):
            self.assertIs(self.life[key], False)
        self.assertEqual(self.life['keeper_terminal_rewards'], [])
        self.assertEqual(set(self.life['keeper_extension_requires']), {
            'physical_fate', 'informed_consent', 'terminal_necessity', 'receiving_owner'})
        self.assertIs(self.roster['undefined_keeper_outcome_is_civic'], False)

    def test_mutations_cannot_restore_generic_gate_or_unowned_payout(self):
        for field, value in (
            ('universal_progress_gate', True), ('decline_scope', 'all_future_closure'),
            ('independent_future_offer_allowed', False), ('reroll_sources', ['reconnect']),
            ('accept_requires', ['valid_offer_conditions']),
            ('defer', 'refresh_offer'), ('artificial_pressure_timer', True),
        ):
            candidate = copy.deepcopy(self.life)
            candidate[field] = value
            with self.subTest(field=field), self.assertRaises(AssertionError):
                self.assert_offer(candidate)
        for requirement in self.life['downstream_requires']:
            candidate = copy.deepcopy(self.life)
            candidate['downstream_requires'].remove(requirement)
            with self.subTest(missing=requirement), self.assertRaises(AssertionError):
                self.assert_consequence(candidate)

    def test_old_fork_and_duplicate_closure_authority_are_absent(self):
        active = [p for domain in GAMEPLAY_ROOTS for p in (ROOT / domain).rglob('*.md')
                  if parse_frontmatter(p).get('status') == 'active']
        owners = []
        for source in active:
            content = source.read_text(encoding='utf-8-sig')
            if re.search(r'^life_closure_contract:', content, re.MULTILINE):
                owners.append(source.relative_to(ROOT).as_posix())
            self.assertNotIn('RETURN_TO_FIELD_FOREVER', content, source)
        self.assertEqual(owners, [LIFE])
        closure = (ROOT / LIFE).read_text(encoding='utf-8-sig')
        self.assertNotRegex(closure, r'(?is)3\s+reserved.{0,90}3\s+revealed')

    def test_owner_consumer_links_and_research_noncanon_boundary(self):
        corpus = set(project_files(ROOT))
        for relative in [LIFE, ROSTER, IDENTITY, *CONSUMERS]:
            source = ROOT / relative
            for target in iter_wikilinks(source.read_text(encoding='utf-8-sig')):
                with self.subTest(source=relative, target=target):
                    resolved = resolve_wikilink(source, target, corpus)
                    self.assertIsNotNone(resolved)
                    self.assertTrue(fragment_exists(resolved, link_parts(target)[1]))
        research = parse_frontmatter(ROOT / '10_Reference/Research_Life_Closure_Batch9A.md')
        self.assertEqual(research['type'], 'reference')
        self.assertEqual(research['status'], 'draft')
        self.assertIs(research['canonical_content'], False)


if __name__ == '__main__':
    unittest.main()
