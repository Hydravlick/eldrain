"""Pre-9 owner/declaration guards; no health or treatment runtime implementation."""
import copy
import re
import unittest
from pathlib import Path

from tools.check_overhaul_contracts import read_named_contract
from tools.document_model import GAMEPLAY_ROOTS, parse_frontmatter
from tools.vault_guard import fragment_exists, iter_wikilinks, link_parts, project_files, resolve_wikilink


ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    'health_contract': '05_Combat_Survival/Combat_Consumables.md',
    'scar_contract': '04_Player_Entities/Tags_System.md',
    'scar_treatment_transaction': '06_Economy_Loot/Barter_System.md',
    'hub_scar_service': '08_World_Generation/Hub/Hub_Services_Interaction.md',
    'cantrip_scar_handoff': '05_Combat_Survival/Magic_Batteries.md',
}


class HealthScarContractsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contracts = {name: read_named_contract(ROOT / path, name) for name, path in SOURCES.items()}
        cls.active = [(p, parse_frontmatter(p)) for domain in GAMEPLAY_ROOTS
                      for p in (ROOT / domain).rglob('*.md')
                      if parse_frontmatter(p).get('status') == 'active']

    def assert_health_owner(self, records):
        owners = [path for path, data in records if data.get('canonical_id') == 'HEALTH'
                  or any(key.startswith('health.') for key in data.get('owns', []))]
        self.assertEqual(owners, [ROOT / SOURCES['health_contract']])

    def assert_health_boundary(self, health):
        self.assertEqual(health['player_values'], ['MaxCapacity', 'FieldCapacity', 'CurrentHP'])
        self.assertEqual(health['invariant'], '0 <= CurrentHP <= FieldCapacity <= MaxCapacity')
        self.assertEqual(health['permanent_loss_source'], 'concrete_scar')
        self.assertEqual(health['permanent_capacity_loss_target'], 'MaxCapacity')
        self.assertEqual(health['resolved_scar_capacity_effect'], 'remove_only_source_loss_then_recalculate')
        self.assertEqual(health['maximum_recalculation'], 'source_scoped_idempotent')
        self.assertEqual(health['after_maximum_change'], ['clamp_field_to_maximum', 'clamp_current_to_field'])
        self.assertEqual(health['health_snapshot_update'], 'atomic')
        self.assertIs(health['maximum_increase_fills_health'], False)
        self.assertEqual(health['ordinary_damage_target'], 'CurrentHP')
        self.assertEqual(health['ordinary_heal_ceiling'], 'FieldCapacity')
        self.assertEqual(health['field_medicine_ceiling'], 'MaxCapacity')

    def assert_paid_treatment(self, transaction):
        self.assertEqual(transaction['owner'], 'RecipeTransaction')
        self.assertEqual(transaction['target'], ['PawnID', 'ScarID', 'scar_revision'])
        self.assertEqual(set(transaction['requires']), {
            'living_patient_in_hub', 'eligible_active_scar', 'available_service',
            'declared_nonempty_resource_inputs', 'confirmed_resource_custody', 'player_confirmation'})
        self.assertEqual(transaction['resource_reservation_owner'], 'Inventory')
        self.assertEqual(transaction['result_owner'], 'Tags_System_Body_and_HEALTH')
        self.assertEqual(transaction['atomic_commit'], 'consume_inputs_and_resolve_target_scar')
        self.assertEqual(transaction['before_commit_failure'], 'inputs_and_scar_unchanged')
        self.assertEqual(transaction['retry'], 'same_result_no_second_charge_or_effect')
        for key in ('target_rebinding', 'facility_writes_health', 'waiting_timer', 'daily_cooldown',
                    'random_result', 'universal_scar_currency', 'resurrection'):
            self.assertIs(transaction[key], False)

    def test_one_health_owner_and_no_stale_active_base_capacity(self):
        self.assert_health_owner(self.active)
        self.assertEqual(self.contracts['health_contract']['owner'], 'HEALTH')
        self.assertEqual(self.contracts['health_contract']['runtime_record'], 'BodyID')
        declarations = []
        for path, _ in self.active:
            body = path.read_text(encoding='utf-8-sig')
            self.assertIsNone(re.search(r'\bBaseCapacity\b', body), str(path))
            if re.search(r'^health_contract:', body, re.M):
                declarations.append(path)
        self.assertEqual(declarations, [ROOT / SOURCES['health_contract']])
        duplicate = (ROOT / '08_World_Generation/Hub/Other_Health.md',
                     {'status': 'active', 'owns': ['health.values_and_bounds']})
        with self.assertRaises(AssertionError):
            self.assert_health_owner(self.active + [duplicate])

    def test_three_values_and_source_scoped_capacity_resolution(self):
        self.assert_health_boundary(self.contracts['health_contract'])
        for field, value in (('player_values', ['MaxCapacity', 'ScarredCapacity', 'FieldCapacity', 'CurrentHP']),
                             ('permanent_capacity_loss_target', 'FieldCapacity'),
                             ('resolved_scar_capacity_effect', 'remove_all_losses'),
                             ('after_maximum_change', ['clamp_current_to_field']),
                             ('ordinary_heal_ceiling', 'MaxCapacity')):
            changed = copy.deepcopy(self.contracts['health_contract'])
            changed[field] = value
            with self.subTest(field=field), self.assertRaises(AssertionError):
                self.assert_health_boundary(changed)

    def test_free_hub_recovery_preserves_scar_and_permanent_loss(self):
        health = self.contracts['health_contract']
        self.assertEqual(health['hub_recovery_cost'], 'free')
        self.assertEqual(health['hub_recovery_requires'], 'living_pawn_and_confirmed_hub_recovery_context')
        self.assertEqual(health['hub_recovery_result'], 'fill_field_and_current_to_current_maximum')
        self.assertIs(health['hub_recovery_removes_scar'], False)
        self.assertIs(health['hub_recovery_restores_permanent_loss'], False)
        self.assertIs(health['resurrection'], False)
        self.assertEqual(health['lethal_resolution_owner'], 'LIFECYCLE_RESOLVER')

    def test_scar_is_a_specific_pawn_consequence_not_universal_hp_loss(self):
        scar = self.contracts['scar_contract']
        self.assertEqual(scar['identity'], ['PawnID', 'ScarID'])
        self.assertEqual(scar['health_resolver'], self.contracts['health_contract']['owner'])
        self.assertEqual(scar['record_owner'], 'Tags_System')
        self.assertEqual(scar['consequence_source'], 'concrete_scar_definition')
        self.assertEqual(scar['treatment_eligibility'], 'scar_and_service_specific')
        self.assertEqual(scar['treatment_result'], 'resolve_target_scar_consequence_only')
        self.assertIs(scar['treatment_keeps_history'], True)
        for key in ('universal_hp_loss', 'basic_hub_removal', 'treatment_frees_lifetime_slot',
                    'treatment_changes_reveal_history', 'automatic_expiry'):
            self.assertIs(scar[key], False)

    def test_facility_delegates_confirmed_real_resource_transaction(self):
        self.assert_paid_treatment(self.contracts['scar_treatment_transaction'])
        service = self.contracts['hub_scar_service']
        self.assertEqual(service['transaction_owner'], self.contracts['scar_treatment_transaction']['owner'])
        self.assertEqual(service['eligibility_owner'], self.contracts['scar_contract']['record_owner'])
        self.assertEqual(service['health_preview_owner'], self.contracts['health_contract']['owner'])
        for key in ('direct_health_writes', 'universal_scar_eligibility', 'basic_recovery_includes_scar_treatment'):
            self.assertIs(service[key], False)
        for field, value in (('requires', ['available_service', 'player_confirmation']),
                             ('atomic_commit', 'consume_inputs_only'),
                             ('retry', 'charge_again'), ('facility_writes_health', True),
                             ('waiting_timer', True), ('resurrection', True)):
            changed = copy.deepcopy(self.contracts['scar_treatment_transaction'])
            changed[field] = value
            with self.subTest(field=field), self.assertRaises(AssertionError):
                self.assert_paid_treatment(changed)

    def test_cantrip_cannot_exchange_permanent_price_for_temporary_strain(self):
        handoff = self.contracts['cantrip_scar_handoff']
        self.assertEqual(handoff['scar_owner'], self.contracts['scar_contract']['record_owner'])
        self.assertEqual(handoff['capacity_owner'], self.contracts['health_contract']['owner'])
        self.assertIs(handoff['universal_capacity_loss'], False)
        self.assertIs(handoff['validate_scar_before_commit'], True)
        self.assertEqual(handoff['illegal_scar_result'], 'reject_before_effect_and_cost')
        self.assertIs(handoff['ordinary_hub_clears_acute_only'], True)
        self.assertEqual(handoff['permanent_removal'], 'confirmed_targeted_scar_treatment')

    def test_owner_links_and_heading_targets(self):
        corpus = set(project_files(ROOT))
        for relative in SOURCES.values():
            source = ROOT / relative
            for target in iter_wikilinks(source.read_text(encoding='utf-8-sig')):
                with self.subTest(source=relative, target=target):
                    resolved = resolve_wikilink(source, target, corpus)
                    self.assertIsNotNone(resolved)
                    self.assertTrue(fragment_exists(resolved, link_parts(target)[1]))


if __name__ == '__main__':
    unittest.main()
