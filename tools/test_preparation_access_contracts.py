"""Contract regression tests; abstract traces publish no game content."""
import copy
import tempfile
import unittest
from pathlib import Path

from tools.check_overhaul_contracts import (
    PREPARATION_ACCESS_CONTRACTS, check_preparation_access_contracts,
    validate_preparation_access_contract, read_named_contract,
)


class PreparationAccessTests(unittest.TestCase):
    def test_current_owners(self):
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(check_preparation_access_contracts(root), [])

    def test_each_published_contract_rejects_every_changed_boundary(self):
        for name, (_, expected) in PREPARATION_ACCESS_CONTRACTS.items():
            self.assertEqual(validate_preparation_access_contract(name, expected), [])
            for key, value in expected.items():
                changed = copy.deepcopy(expected)
                changed[key] = not value if type(value) is bool else None
                with self.subTest(contract=name, field=key):
                    self.assertTrue(validate_preparation_access_contract(name, changed))

    def test_missing_or_duplicate_owner_contract_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertTrue(check_preparation_access_contracts(root))
            path = root / 'owner.md'
            path.write_text('```yaml\nx: {}\n```\n```yaml\nx: {}\n```', encoding='utf-8')
            with self.assertRaises(ValueError):
                read_named_contract(path, 'x')

    def test_active_declarations_cannot_restore_hidden_state_or_large_access(self):
        source = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative, _ in PREPARATION_ACCESS_CONTRACTS.values():
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text((source / relative).read_text(encoding='utf-8'), encoding='utf-8')
            self.assertEqual(check_preparation_access_contracts(root), [])
            target = root / '07_Gear_Inventory' / 'Injected.md'
            for declaration in ('[module_def_id:: long_thread_battery_rack]',
                                '[battery_access_positions:: 20]',
                                '[GlobalAimState:: true]',
                                '[selected_focus_recipient:: A]'):
                with self.subTest(declaration=declaration):
                    target.write_text('---\nstatus: active\n---\n' + declaration, encoding='utf-8')
                    self.assertTrue(check_preparation_access_contracts(root))
            target.unlink()
            # Rejected alternatives in root rationale never become published state.
            (root / 'Milestone rationale.md').write_text(
                'Rejected: GlobalAimState, supports_aim, battery queue.', encoding='utf-8')
            self.assertEqual(check_preparation_access_contracts(root), [])

    def test_focus_counts_physical_owners_not_slots_or_support_votes(self):
        rule = PREPARATION_ACCESS_CONTRACTS['weapon_focus_contract'][1]
        self.assertEqual(rule['owner_count'], 'distinct_weapon_itemids')
        self.assertEqual(rule['required_owner_count'], 1)
        self.assertEqual(rule['support_field'], 'supports_focus')
        # 2H repeated across slots has one identity; each dual pair has two.
        for slots, count in ((('A', None), 1), (('H', 'H'), 1),
                             (('pistol', 'knife'), 2), (('knife', 'pistol'), 2),
                             (('pistol', 'sawed_off'), 2), (('pistol_A', 'pistol_B'), 2)):
            self.assertEqual(len(set(slots) - {None}), count)
        self.assertFalse(rule['dual_available'])
        self.assertFalse(rule['changes_channels'])

    def test_preparation_does_not_gate_ability_targeting_on_weapon(self):
        preparation = PREPARATION_ACCESS_CONTRACTS['preparation_contract'][1]
        ability = PREPARATION_ACCESS_CONTRACTS['profile_preparation_contract'][1]
        self.assertEqual(preparation['max_uncommitted'], 1)
        self.assertTrue(preparation['selection_before_claims'])
        self.assertFalse(preparation['replaces_committed_concurrency'])
        self.assertFalse(ability['targeting_requires_weapon_focus'])
        self.assertEqual(ability['variant_binding'], 'latched')

    def test_physical_mount_trace_and_no_virtual_refill(self):
        rule = PREPARATION_ACCESS_CONTRACTS['battery_access_contract'][1]
        self.assertFalse(rule['cargo_immediate'])
        self.assertTrue(rule['generic_ready_eligible'])
        self.assertTrue(rule['dedicated_ready_eligible'])
        self.assertTrue(rule['drained_occupies_position'])
        self.assertEqual(rule['discharge_placement'], 'unchanged')
        self.assertEqual(rule['refill_sequence'], [
            'remove_stow_or_drop_drained', 'retrieve_full_from_cargo', 'place_full'])

    def test_tab_four_paths_and_no_key_down_toggle(self):
        rule = PREPARATION_ACCESS_CONTRACTS['player_menu_contract'][1]
        self.assertEqual(rule['key_down'], 'pending_only')
        self.assertEqual(rule['closed_tap'], 'persistent')
        self.assertEqual(rule['persistent_tap'], 'closed')
        self.assertEqual(rule['closed_hold_threshold'], 'temporary')
        self.assertEqual(rule['temporary_release'], 'closed')
        self.assertEqual(rule['persistent_hold_release'], 'persistent')

    def test_switch_is_barrier_not_held_input_remap(self):
        rule = PREPARATION_ACCESS_CONTRACTS['set_switch_input_contract'][1]
        self.assertTrue(rule['cancels_uncommitted_preparation'])
        self.assertEqual(rule['execution_boundary'], 'earliest_legal_action_boundary')
        self.assertFalse(rule['old_held_intent_reinterpreted'])


if __name__ == '__main__':
    unittest.main()
