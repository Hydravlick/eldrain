"""Weapon identity/publication tests; temporary records are not GDD content."""
from __future__ import annotations

import tempfile
import unittest
import copy
from pathlib import Path

import yaml

from tools.check_overhaul_contracts import (Record, published, run_identity_checks as run,
    validate_records, check_set_input_contracts, validate_set_schema, read_set_schema)


def frame(identifier="language", **changes):
    data = dict(type="entity", entity_kind="weapon_frame", frame_id=identifier,
                status="active", publication_state="canonical", canonical_content=True,
                spatial_job="hold a line", positioning_contract="outside contact",
                bodily_organization="declared grip", operation_classes=["contact"],
                commitment_character="committed reach", natural_debt="lost angle",
                counterplay_contract="close distance", variation_limits="same spatial job",
                learnability_prior="visible working end", boundary_notes="position transfers")
    data.update(changes)
    return Record(Path(identifier + ".md"), data, "")


def pattern(identifier="construction", frame_id="language", **changes):
    data = dict(type="entity", entity_kind="weapon_pattern", pattern_id=identifier,
                frame_id=frame_id, status="active", publication_state="canonical",
                canonical_content=True, hand_requirement="one_hand", primary_operation="contact",
                supports_aim=False, operation_ids=["contact"])
    data.update(changes)
    return Record(Path(identifier + ".md"), data, "[operation_id:: contact]\nConcrete operation.")


class WeaponIdentityTests(unittest.TestCase):
    def test_empty_content_is_valid(self):
        self.assertEqual(validate_records([]), [])

    def test_two_patterns_share_a_frame_without_mastery_or_item_state(self):
        self.assertEqual(validate_records([frame(), pattern("one"), pattern("two")]), [])

    def test_only_full_publication_tuple_is_canonical(self):
        self.assertTrue(published(frame().data))
        for changes in ({"status": "draft"}, {"canonical_content": "true"},
                        {"canonical_content": False}, {"publication_state": "diagnostic_fixture"}):
            with self.subTest(changes=changes):
                self.assertFalse(published(frame(**changes).data))
                self.assertTrue(validate_records([frame(**changes)]))

    def test_legacy_is_excluded_and_does_not_require_new_schema(self):
        legacy = Record(Path("old.md"), dict(type="entity", entity_kind="weapon_frame",
            frame_id="old", status="deprecated", publication_state="legacy_weapon_scaffolding",
            canonical_content=False, mastery_unlock=["old_technique"]), "[instance_id:: old_model]")
        self.assertEqual(validate_records([legacy]), [])
        self.assertFalse(published(legacy.data))
        self.assertTrue(validate_records([legacy, pattern(frame_id="old")]))

    def test_missing_and_duplicate_ids_fail(self):
        for records in ([frame(), frame()], [frame(), pattern(), pattern()],
                        [pattern(frame_id="missing")], [frame(frame_id="")]):
            with self.subTest(records=records):
                self.assertTrue(validate_records(records))

    def test_canonical_pattern_cannot_use_fixture_frame(self):
        fixture = frame("fixture_language", status="draft", publication_state="diagnostic_fixture",
                        canonical_content=False)
        self.assertTrue(validate_records([fixture, pattern(frame_id="fixture_language")]))
        trial = pattern("fixture_construction", "fixture_language", status="draft",
                        publication_state="diagnostic_fixture", canonical_content=False)
        self.assertEqual(validate_records([fixture, trial]), [])

    def test_draft_may_be_incomplete_but_is_not_published(self):
        draft = Record(Path("draft.md"), dict(type="entity", entity_kind="weapon_pattern",
            pattern_id="draft", status="draft", publication_state="unpublished", canonical_content=False), "")
        self.assertEqual(validate_records([draft]), [])
        self.assertFalse(published(draft.data))

    def test_required_envelope_and_operation_fields(self):
        for record, key in ((frame(), "natural_debt"), (frame(), "operation_classes"),
                            (pattern(), "primary_operation"), (pattern(), "supports_aim")):
            record.data.pop(key)
            with self.subTest(key=key):
                self.assertTrue(validate_records([record]))

    def test_aim_and_alt_reference_real_operation_definitions(self):
        self.assertTrue(validate_records([frame(), pattern(supports_aim=True)]))
        self.assertTrue(validate_records([frame(), pattern(alt_operation="missing")]))
        self.assertTrue(validate_records([frame(), pattern(aim_operation="contact")]))
        p = pattern(supports_aim=True, aim_operation="aim", alt_operation="alt",
                    operation_ids=["contact", "aim", "alt"])
        p.body += "\n[operation_id:: aim]\n[operation_id:: alt]"
        self.assertEqual(validate_records([frame(), p]), [])
        p.body = p.body.replace("[operation_id:: aim]", "")
        self.assertTrue(validate_records([frame(), p]))

    def test_active_definition_rejects_mastery_and_local_prof(self):
        for key in ("mastery_unlock", "MasteryContribution", "mastery_required", "prof",
                    "proficiency", "prof3_moveset", "mastery_expression"):
            with self.subTest(key=key):
                self.assertTrue(validate_records([frame(), pattern(**{key: "forbidden"})]))
        p = pattern()
        p.body += "\n[mastery_step:: 1]"
        self.assertTrue(validate_records([frame(), p]))

    def test_legacy_construction_id_is_not_a_new_definition_id(self):
        p = pattern()
        p.body += "\n[instance_id:: repeatable_model]"
        self.assertTrue(validate_records([frame(), p]))

    def test_no_runtime_state_or_exact_moveset_on_frame(self):
        for key in ("moveset", "moveset_profile", "magazine", "heat", "current_recovery"):
            with self.subTest(key=key):
                self.assertTrue(validate_records([frame(**{key: "wrong_owner"})]))
        for key in ("provenance", "custody", "condition", "current_action_debt"):
            with self.subTest(key=key):
                self.assertTrue(validate_records([frame(), pattern(**{key: "wrong_owner"})]))

    def test_disk_discovery_and_profile_reference_check(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            folder = root / "05_Combat_Survival"
            folder.mkdir()
            for record in (frame(), pattern()):
                (folder / record.path).write_text("---\n" + yaml.safe_dump(record.data) +
                    "---\n" + record.body, encoding="utf-8")
            self.assertEqual(run(root), [])
            combos = root / "04_Player_Entities/Registries/Registry_Combos.md"
            combos.parent.mkdir(parents=True)
            combos.write_text("[legacy_weapon_frame:: old]\n[weapon_frame:: language]", encoding="utf-8")
            self.assertEqual(run(root), [])
            combos.write_text("[weapon_frame:: old]", encoding="utf-8")
            self.assertTrue(run(root))

    def test_loot_view_no_longer_reads_legacy_instances(self):
        path = Path(__file__).resolve().parents[1] / "tools/dataview/sector_difficulty/view.js"
        text = path.read_text(encoding="utf-8-sig")
        self.assertNotIn('parseTagId(block, "instance_id")', text)
        self.assertIn('p.entity_kind === "weapon_pattern"', text)
        self.assertIn('p.publication_state === "canonical"', text)
        self.assertIn('p.canonical_content === true', text)

    def test_unfiltered_weapon_query_is_a_publication_error(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = root / "05_Combat_Survival/Registries/Registry_Weapons.md"
            registry.parent.mkdir(parents=True)
            registry.write_text('```dataview\nTABLE frame_id\nWHERE entity_kind = "weapon_frame"\n```',
                                encoding="utf-8")
            self.assertTrue(run(root))
            registry.write_text('```dataview\nTABLE frame_id\nWHERE entity_kind = "weapon_frame" '
                                'AND status = "active" AND publication_state = "canonical" '
                                'AND canonical_content = true\n```', encoding="utf-8")
            self.assertEqual(run(root), [])
            registry.write_text('```dataview\nTABLE frame_id\nWHERE entity_kind = "weapon_frame" '
                                'AND status = "draft" AND publication_state = "diagnostic_fixture" '
                                'AND canonical_content = false\n```', encoding="utf-8")
            self.assertEqual(run(root), [])


class SetInputContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = Path(__file__).resolve().parents[1]
        for name in ("01_Core_Vision/Input_Contract.md", "07_Gear_Inventory/Equipment_PaperDoll.md"):
            dest = self.root / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes((self.repo / name).read_bytes())
        self.input = self.root / "01_Core_Vision/Input_Contract.md"
        self.set_page = self.root / "07_Gear_Inventory/Equipment_PaperDoll.md"

    def test_current_input_and_set_contracts_are_valid(self):
        self.assertEqual(check_set_input_contracts(self.root), [])

    def test_exactly_one_active_input_owner(self):
        self.input.with_name("Duplicate.md").write_bytes(self.input.read_bytes())
        self.assertTrue(check_set_input_contracts(self.root))
        self.input.with_name("Duplicate.md").unlink()
        self.input.unlink()
        self.assertTrue(check_set_input_contracts(self.root))

    def test_same_context_binding_collision_is_rejected(self):
        text = self.input.read_text(encoding="utf-8-sig")
        self.input.write_text(text.replace('[default_binding:: RMB]', '[default_binding:: Mouse1]'), encoding="utf-8")
        self.assertTrue(check_set_input_contracts(self.root))

    def test_explicit_disjoint_ui_context_can_reuse_binding(self):
        with self.input.open('a', encoding='utf-8') as stream:
            stream.write('\n### UI test intent\n[action_id:: ui_test]\n[default_binding:: LeftAlt]\n'
                         '[input_mode:: press]\n[context:: inventory_transfer]\n'
                         '[gameplay_owner:: [[07_Gear_Inventory/Inventory_QoL]]]\n[consumer_role:: ui_request]\n')
        self.assertEqual(check_set_input_contracts(self.root), [])

    def test_aim_is_not_alt_and_switch_cantrip_are_unassigned(self):
        original = self.input.read_text(encoding='utf-8-sig')
        for old, new in (('[action_id:: aim]', '[action_id:: alt]'),
                         ('[default_binding:: LeftAlt]', '[default_binding:: RMB]'),
                         ('[default_binding:: TBD]', '[default_binding:: X]')):
            with self.subTest(new=new):
                self.input.write_text(original.replace(old, new), encoding='utf-8')
                self.assertTrue(check_set_input_contracts(self.root))

    def test_missing_or_duplicated_channels_fail(self):
        original = self.input.read_text(encoding='utf-8-sig')
        for replacement in ('removed_channel', 'weapon_channel_1'):
            self.input.write_text(original.replace('[action_id:: weapon_channel_2]',
                f'[action_id:: {replacement}]'), encoding='utf-8')
            self.assertTrue(check_set_input_contracts(self.root))

    def test_input_cannot_own_execution_or_hands(self):
        original = self.input.read_text(encoding='utf-8-sig')
        for key in ('action_execution.eligibility', 'weapon_set.wield_state'):
            self.input.write_text(original.replace('owns:', f'owns:\n  - {key}', 1), encoding='utf-8')
            self.assertTrue(check_set_input_contracts(self.root))

    def test_consumer_is_not_redirected_to_input_resolver(self):
        original = self.input.read_text(encoding='utf-8-sig')
        self.input.write_text(original.replace('[gameplay_owner:: [[07_Gear_Inventory/Equipment_PaperDoll]]]',
            '[gameplay_owner:: [[01_Core_Vision/Input_Contract]]]'), encoding='utf-8')
        self.assertTrue(check_set_input_contracts(self.root))

    def test_single_dual_and_2h_share_the_declared_mapping(self):
        schema = read_set_schema(self.set_page)
        mapping = schema['channel_mapping']
        self.assertEqual(mapping['single_1h']['weapon_channel_2']['operation_field'], 'alt_operation')
        self.assertEqual(mapping['dual_1h']['weapon_channel_2'],
                         dict(recipient_slots=[2], operation_field='primary_operation'))
        self.assertEqual(schema['layout_shapes']['two_handed'], [[1, 2]])
        self.assertEqual(mapping['two_handed']['weapon_channel_1']['recipient_slots'], [1, 2])

    def test_fake_2h_and_internal_selected_weapon_are_rejected(self):
        schema = read_set_schema(self.set_page)
        for key in ('selected_weapon', 'lead_role', 'offhand_weapon', 'DualWieldPermission',
                    'DualWieldProf', 'mastery_required'):
            candidate = copy.deepcopy(schema)
            candidate[key] = 'required'
            with self.subTest(key=key):
                self.assertTrue(validate_set_schema(candidate))
        candidate = copy.deepcopy(schema)
        candidate['layout_shapes']['two_handed'] = [[1], [2]]
        self.assertTrue(validate_set_schema(candidate))

    def test_wrong_channel_and_non_action_eligibility_fail(self):
        schema = read_set_schema(self.set_page)
        candidate = copy.deepcopy(schema)
        candidate['channel_mapping']['dual_1h']['weapon_channel_2']['operation_field'] = 'alt_operation'
        self.assertTrue(validate_set_schema(candidate))
        candidate = copy.deepcopy(schema)
        candidate['eligibility_owner'] = 'WEAPON_SET'
        self.assertTrue(validate_set_schema(candidate))

    def test_set_owner_does_not_gain_custody_or_action_debt(self):
        text = self.set_page.read_text(encoding='utf-8-sig')
        self.set_page.write_text(text.replace('owns:', 'owns:\n  - inventory.custody', 1), encoding='utf-8')
        self.assertTrue(check_set_input_contracts(self.root))


class BatteryCutoverTests(unittest.TestCase):
    """Mutate published contracts, not a pretend gameplay implementation."""
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        source = Path(__file__).resolve().parents[1]
        self.paths = [
            "05_Combat_Survival/Magic_Batteries.md",
            "05_Combat_Survival/Weapon_Ranged.md",
            "04_Player_Entities/Skill_Execution.md",
            "04_Player_Entities/Registries/Registry_Parameter_Contracts.md",
            "07_Gear_Inventory/Registries/Registry_Thermos_Modules.md",
        ]
        for name in self.paths:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text((source / name).read_text(encoding="utf-8"), encoding="utf-8")

    def check(self):
        from tools.check_overhaul_contracts import check_energy_contracts
        return check_energy_contracts(self.root)

    def mutate(self, index, before, after):
        path = self.root / self.paths[index]
        body = path.read_text(encoding="utf-8")
        self.assertIn(before, body)
        path.write_text(body.replace(before, after), encoding="utf-8")

    def test_contracts_accept_zero_weapon_content(self):
        self.assertEqual(self.check(), [])

    def test_missing_energy_owner_fails(self):
        (self.root / self.paths[0]).unlink()
        self.assertTrue(self.check())

    def test_battery_has_no_charge_counter_or_partial_state(self):
        self.mutate(0, "internal_charge_counter: false", "internal_charge_counter: true")
        self.assertTrue(self.check())
        self.mutate(0, "internal_charge_counter: true", "internal_charge_counter: false")
        self.mutate(0, "states: [Full, Drained]", "states: [Full, Partial, Drained]")
        self.assertTrue(self.check())

    def test_one_transaction_preserves_physical_item(self):
        self.mutate(0, "transactions_per_full_state: 1", "transactions_per_full_state: 3")
        self.assertTrue(self.check())
        self.mutate(0, "transactions_per_full_state: 3", "transactions_per_full_state: 1")
        self.mutate(0, "preserves_item_id: true", "preserves_item_id: false")
        self.assertTrue(self.check())

    def test_before_and_after_commit_are_atomic(self):
        self.mutate(0, "after_commit: [source_drained, result_applied]", "after_commit: [source_drained]")
        self.assertTrue(self.check())

    def test_one_reload_one_battery_one_recipient(self):
        self.mutate(0, "recipients_per_action: 1", "recipients_per_action: 2")
        self.assertTrue(self.check())

    def test_partial_reload_cost_and_full_no_transaction(self):
        self.mutate(0, "remainder_changes_cost: false", "remainder_changes_cost: true")
        self.assertTrue(self.check())
        self.mutate(0, "remainder_changes_cost: true", "remainder_changes_cost: false")
        self.mutate(0, "full_recipient: no_transaction", "full_recipient: consume_source")
        self.assertTrue(self.check())

    def test_shared_magazine_and_switch_reset_fail(self):
        self.mutate(1, "runtime_owner: ItemID", "runtime_owner: WeaponSet")
        self.assertTrue(self.check())
        self.mutate(1, "runtime_owner: WeaponSet", "runtime_owner: ItemID")
        self.mutate(1, "switch_preserves_state: true", "switch_preserves_state: false")
        self.assertTrue(self.check())

    def test_depletion_cannot_remap_and_reload_cannot_reset_heat(self):
        self.mutate(1, "depletion_remaps_channel: false", "depletion_remaps_channel: true")
        self.assertTrue(self.check())
        self.mutate(1, "depletion_remaps_channel: true", "depletion_remaps_channel: false")
        self.mutate(0, "resets: []", "resets: [Heat]")
        self.assertTrue(self.check())

    def test_binding_and_source_exclusion_required(self):
        self.mutate(0, "recipient_binding: immutable", "recipient_binding: retarget_on_switch")
        self.assertTrue(self.check())
        self.mutate(0, "recipient_binding: retarget_on_switch", "recipient_binding: immutable")
        self.mutate(0, "source_reservation_owner: Inventory", "source_reservation_owner: none")
        self.assertTrue(self.check())

    def test_qe_is_opt_in_whole_battery_not_magazine(self):
        self.mutate(2, "source_count: 1", "source_count: 2")
        self.assertTrue(self.check())
        self.mutate(2, "source_count: 2", "source_count: 1")
        self.mutate(2, "uses_weapon_magazine: false", "uses_weapon_magazine: true")
        self.assertTrue(self.check())

    def test_old_active_resource_fields_fail_but_history_is_allowed(self):
        path = self.root / "05_Combat_Survival/Old.md"
        path.write_text("---\nstatus: active\n---\n[weapon_reserve:: 3]\n", encoding="utf-8")
        self.assertTrue(self.check())
        path.write_text("---\nstatus: deprecated\n---\n[weapon_reserve:: 3]\n", encoding="utf-8")
        self.assertEqual(self.check(), [])

    def test_old_queue_cannot_reenter_parameter_publication(self):
        path = self.root / self.paths[3]
        with path.open("a", encoding="utf-8") as f:
            f.write("\n### Old\n[parameter_contract_id:: prepared_battery_queue_capacity]\n[status:: active]\n")
        self.assertTrue(self.check())

    def test_deprecated_rack_cannot_publish_old_effect(self):
        self.mutate(4, "[publication_status:: deprecated]", "[publication_status:: approved]")
        self.assertTrue(self.check())

    def test_pattern_magazine_is_optional_and_runtime_is_forbidden(self):
        self.assertEqual(validate_records([frame(), pattern()]), [])
        self.assertTrue(validate_records([frame(), pattern(magazine_current=3)]))
        self.assertTrue(validate_records([frame(magazine_capacity=8)]))
        self.assertTrue(validate_records([frame(), pattern(magazine_capacity=8)]))
        p = pattern(magazine_capacity=8, shot_consumption=1,
                    reload_service_ref="[[05_Combat_Survival/Magic_Batteries]]")
        self.assertEqual(validate_records([frame(), p]), [])
        p.data["shot_consumption"] = 0
        self.assertTrue(validate_records([frame(), p]))


class ProficiencyCutoverTests(unittest.TestCase):
    def check_list(self, value, active=None):
        from tools.check_overhaul_contracts import validate_frame_proficiencies
        return validate_frame_proficiencies(value, set() if active is None else active)

    def test_empty_assignments_are_valid(self):
        self.assertEqual(self.check_list([]), [])

    def test_relation_is_to_one_canonical_frame(self):
        self.assertEqual(self.check_list([dict(frame_id="F", proficiency=2)], {"F"}), [])
        self.assertTrue(self.check_list([dict(frame_id="legacy", proficiency=2)]))

    def test_pattern_item_and_set_keys_are_rejected(self):
        for key in ("pattern_id", "item_id", "set_id"):
            self.assertTrue(self.check_list([{key:"F", "proficiency":2}], {"F"}))

    def test_levels_are_discrete_and_not_bonus_fields(self):
        for level in (-1,4,True,"2",2.5):
            self.assertTrue(self.check_list([dict(frame_id="F", proficiency=level)], {"F"}))
        self.assertTrue(self.check_list([dict(frame_id="F", proficiency=2, mastery_bonus=1)], {"F"}))

    def test_duplicate_frame_assignment_fails(self):
        self.assertTrue(self.check_list([dict(frame_id="F", proficiency=n) for n in (1,2)], {"F"}))

    def test_definition_cannot_own_current_prof(self):
        for make in (frame, pattern):
            for field in ("current_prof", "owner_prof", "frame_proficiencies"):
                record = make(**{field:2})
                records = [record] if make is frame else [frame(), record]
                self.assertTrue(validate_records(records))

    def check_docs(self, replacements=()):
        from tools.check_overhaul_contracts import check_proficiency_contracts
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = Path(__file__).resolve().parents[1]
            for name in ("04_Player_Entities/Proficiency_Arsenal.md", "04_Player_Entities/Skill_Build_Philosophy.md",
                         "04_Player_Entities/Registries/Registry_Combos.md", "04_Player_Entities/Registries/Registry_Tags.md"):
                body = (source/name).read_text(encoding="utf-8")
                for before, after in replacements:
                    body = body.replace(before, after)
                target=root/name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(body, encoding="utf-8")
            return check_proficiency_contracts(root)

    def test_published_contract_and_legacy_assignments_coexist(self):
        self.assertEqual(self.check_docs(), [])

    def test_prof1_full_moveset_and_no_prof3_technique(self):
        for before,after in (("admitted_moveset: full_pattern","admitted_moveset: reduced"),
                             ("exceptional_technique_required: false","exceptional_technique_required: true")):
            self.assertTrue(self.check_docs([(before,after)]))

    def test_natural_debt_and_spatial_choice_remain(self):
        for key in ("natural_debt_preserved", "spatial_job_may_outweigh_level"):
            self.assertTrue(self.check_docs([(key+": true",key+": false")]))

    def test_no_universal_mastery_or_speed(self):
        self.assertTrue(self.check_docs([("mastery_dependency: false","mastery_dependency: true")]))
        self.assertTrue(self.check_docs([("universal_modifiers: []","universal_modifiers: [weapon_speed]")]))

    def test_profile_budget_and_assembly_legality_are_separate(self):
        for before,after in (("owns_service_capacity: false","owns_service_capacity: true"),
                             ("authored_source: FieldProfile","authored_source: Proficiency"),
                             ("legality_owner: Thermos_Assembly","legality_owner: Proficiency")):
            self.assertTrue(self.check_docs([(before,after)]))

    def test_mastery_prototype_cannot_return_as_active(self):
        self.assertTrue(self.check_docs([("[design_status:: deprecated]","[design_status:: approved]")]))


class PawnEcologyTests(unittest.TestCase):
    """Mutation checks on authority contracts; no content or gameplay simulation."""
    files = (
        "04_Player_Entities/Skill_Build_Philosophy.md",
        "04_Player_Entities/Tags_System.md",
        "04_Player_Entities/Combat_Profile_Pipeline.md",
        "04_Player_Entities/Shell_Construction.md",
        "03_Factions_Societies/Quest_Engine.md",
        "04_Player_Entities/Grimoire_Truth_Triangulation.md",
    )

    def check_docs(self, replacements=(), extra=None):
        from tools.check_overhaul_contracts import check_pawn_ecology_contracts
        source = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in self.files:
                text = (source/name).read_text(encoding="utf-8")
                for old, new in replacements:
                    text = text.replace(old, new)
                path = root/name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
            if extra:
                path = root/extra[0]
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(extra[1], encoding="utf-8")
            return check_pawn_ecology_contracts(root)

    def test_owner_contracts_accept_empty_content(self):
        self.assertEqual(self.check_docs(), [])

    def test_separate_passive_engine_rejected(self):
        self.assertTrue(self.check_docs([("separate_passive_engine: false", "separate_passive_engine: true")]))

    def test_duplicate_grammar_owner_rejected(self):
        self.assertTrue(self.check_docs(extra=("04_Player_Entities/Other.md",
            "---\nstatus: active\ntype: system\nowns: [passive.effect_engine]\n---\n")))

    def test_profile_provenance_and_personal_slot_are_not_interchangeable(self):
        for old, new in (("p_provenance: deterministic_field_profile", "p_provenance: random_roll"),
                         ("p_uses_personal_acquisition_slot: false", "p_uses_personal_acquisition_slot: true")):
            with self.subTest(old=old):
                self.assertTrue(self.check_docs([(old, new)]))

    def test_p_cannot_reenter_active_operation_slots(self):
        self.assertTrue(self.check_docs([("active_operation_slots: [Q, E]", "active_operation_slots: [P, Q, E]")]))
        self.assertTrue(self.check_docs(extra=("04_Player_Entities/BadSkill.md",
            "---\nstatus: active\ntype: registry\n---\n[skill_slot:: P | Q | E]\n")))

    def test_projection_cannot_apply_or_resolve_or_write(self):
        for key in ("applies_modifiers", "resolves_gameplay", "writes_gameplay_state"):
            with self.subTest(key=key):
                self.assertTrue(self.check_docs([(key+": false", key+": true")]))

    def test_profile_cannot_store_items_or_finished_build(self):
        for key in ("concrete_itemids", "finished_build"):
            self.assertTrue(self.check_docs([(key+": false", key+": true")]))

    def test_trait_cannot_own_service_capacity(self):
        self.assertTrue(self.check_docs([("grants_service_capacity: false", "grants_service_capacity: true")]))
        self.assertTrue(self.check_docs(extra=("04_Player_Entities/BadTrait.md",
            "---\nstatus: active\ntype: system\nowns: [trait.base_service_capacity]\n---\n")))

    def test_unfinished_work_re_evaluates_in_both_work_owners(self):
        for key in ("unfinished_work_on_capability_loss", "unfinished_on_capability_loss", "unfinished_on_executor_loss"):
            self.assertTrue(self.check_docs([(key+": re_evaluate", key+": delete")]))

    def test_completed_result_does_not_require_author_alive(self):
        for key in ("completed_obligation_requires_author_alive", "established_fact_requires_author_alive"):
            self.assertTrue(self.check_docs([(key+": false", key+": true")]))
        self.assertTrue(self.check_docs([("completed_result_on_author_death: not_reversed", "completed_result_on_author_death: deleted")]))

    def test_no_capability_inheritance_or_retirement_reward(self):
        for key in ("unique_capability_transferred", "copies_executor_capability", "transfers_embodied_capability", "work_result_is_retirement_reward"):
            self.assertTrue(self.check_docs([(key+": false", key+": true")]))

    def test_no_parked_value_or_opportunity_mega_owner(self):
        for key in ("indefinite_parked_value", "opportunity_list_owner"):
            self.assertTrue(self.check_docs([(key+": false", key+": true")]))

    def test_history_is_not_subject_to_active_semantic_checks(self):
        body = "---\nstatus: deprecated\ntype: registry\n---\n[skill_slot:: P]\n"
        self.assertEqual(self.check_docs(extra=("04_Player_Entities/Old.md", body)), [])
        self.assertEqual(self.check_docs(extra=("10_Reference/Old.md", body.replace("deprecated", "active"))), [])


if __name__ == "__main__":
    unittest.main()
