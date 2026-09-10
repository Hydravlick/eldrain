"""Structural weapon publication/identity checks, not a gameplay resolver."""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

try:
    from tools.document_model import GAMEPLAY_ROOTS, MetadataError, parse_frontmatter, load_yaml
except ModuleNotFoundError:
    from document_model import GAMEPLAY_ROOTS, MetadataError, parse_frontmatter, load_yaml


KINDS = {"weapon_frame": "frame_id", "weapon_pattern": "pattern_id"}
PUBLICATION = {
    "canonical": ("active", True),
    "diagnostic_fixture": ("draft", False),
    "legacy_weapon_scaffolding": ("deprecated", False),
    "unpublished": ("draft", False),
}
FRAME_FIELDS = (
    "spatial_job", "positioning_contract", "bodily_organization", "operation_classes",
    "commitment_character", "natural_debt", "counterplay_contract", "variation_limits",
    "learnability_prior", "boundary_notes",
)
RUNTIME_FIELDS = {
    "item_id", "itemid", "condition", "damage", "heat", "magazine", "magazine_state",
    "magazine_current", "device_state", "provenance", "custody", "current_recovery", "current_action_debt",
}
FRAME_FORBIDDEN = {
    "moveset", "moveset_profile", "primary_operation", "alt_operation", "aim_operation",
    "magazine_capacity", "shot_consumption", "reload_service_ref", "operation_ids", "nativeaction", "native_action", "combo_chain", "pattern_id",
}


@dataclass
class Record:
    path: Path
    data: dict
    body: str


def published(data: dict) -> bool:
    return (data.get("status") == "active" and data.get("publication_state") == "canonical"
            and data.get("canonical_content") is True)


def present(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def keys_in(data):
    if isinstance(data, dict):
        for key, value in data.items():
            yield str(key).lower()
            yield from keys_in(value)
    elif isinstance(data, list):
        for value in data:
            yield from keys_in(value)


def validate_records(records: list[Record]) -> list[str]:
    errors = []
    frames = {}
    seen = set()
    for record in records:
        d = record.data
        kind = d.get("entity_kind")
        if kind not in KINDS:
            continue
        def fail(message):
            errors.append(f"{record.path}: {message}")
        if d.get("type") != "entity":
            fail("weapon definition must be an entity")
        identifier = d.get(KINDS[kind])
        if not present(identifier):
            fail(f"missing {KINDS[kind]}")
        elif (kind, identifier) in seen:
            fail(f"duplicate {KINDS[kind]}: {identifier}")
        else:
            seen.add((kind, identifier))
            if kind == "weapon_frame":
                frames[identifier] = record
        state = d.get("publication_state")
        expected = PUBLICATION.get(state)
        if (expected is None or d.get("status") != expected[0]
                or type(d.get("canonical_content")) is not bool
                or d.get("canonical_content") is not expected[1]):
            fail("invalid weapon publication tuple")
        if state == "legacy_weapon_scaffolding":
            continue  # Historical records are not target schema or fixtures.
        if state == "diagnostic_fixture" and not str(identifier).startswith("fixture_"):
            fail("diagnostic ID must start with fixture_")
        fields = set(keys_in(d))
        fields.update(k.lower() for k in re.findall(r"\[([\w]+)::", record.body))
        for key in sorted(fields):
            if (key in {"instance_id", "current_prof", "owner_prof", "frame_proficiencies", "effectiveprof", "baseframeprof"} or "mastery" in key or key == "prof"
                    or "proficiency" in key or key.startswith("prof_")
                    or re.match(r"prof[0-3]", key)):
                fail(f"legacy or misplaced weapon identity field: {key}")
            if key in RUNTIME_FIELDS or (kind == "weapon_frame" and key in FRAME_FORBIDDEN):
                fail(f"field belongs to a different owner: {key}")
        if state == "unpublished":
            continue  # Drafts may be incomplete, but cannot smuggle in old identity fields.
        required = FRAME_FIELDS if kind == "weapon_frame" else (
            "frame_id", "hand_requirement", "primary_operation", "operation_ids")
        for key in required:
            value = d.get(key)
            if key in {"operation_classes", "operation_ids"}:
                if not isinstance(value, list) or not value or not all(present(v) for v in value):
                    fail(f"{key} must be a nonempty string list")
            elif not present(value):
                fail(f"missing {key}")
        if kind == "weapon_pattern":
            magazine_fields = {"magazine_capacity", "shot_consumption", "reload_service_ref"}
            supplied = magazine_fields.intersection(d)
            if supplied and supplied != magazine_fields:
                fail("magazine model needs capacity, consumption and reload service together")
            if supplied == magazine_fields:
                cap, cost = d["magazine_capacity"], d["shot_consumption"]
                if type(cap) is not int or cap <= 0:
                    fail("magazine_capacity must be a positive integer")
                if type(cost) is int:
                    if cost <= 0 or (type(cap) is int and cost > cap):
                        fail("shot_consumption must fit a positive magazine cost")
                elif not present(cost) or "[[" not in cost:
                    fail("named shot_consumption needs a definition link")
                if not present(d["reload_service_ref"]) or "[[" not in d["reload_service_ref"]:
                    fail("reload_service_ref needs a contract link")
            operations = d.get("operation_ids", [])
            if not isinstance(operations, list) or not all(present(v) for v in operations):
                operations = []
            definitions = re.findall(r"\[operation_id::\s*([^\]\n]+)\]", record.body)
            definitions = [v.strip() for v in definitions]
            if (set(operations) != set(definitions) or len(operations) != len(set(operations))
                    or len(definitions) != len(set(definitions))):
                fail("operation_ids must match unique local operation definitions")
            if type(d.get("supports_aim")) is not bool:
                fail("supports_aim must be boolean")
            if d.get("supports_aim") is True and not present(d.get("aim_operation")):
                fail("Aim support needs aim_operation")
            if d.get("supports_aim") is False and "aim_operation" in d:
                fail("aim_operation requires Aim support")
            for key in ("primary_operation", "alt_operation", "aim_operation"):
                if key in d and d[key] not in operations:
                    fail(f"{key} does not name a local operation")
    for record in records:
        d = record.data
        if d.get("entity_kind") != "weapon_pattern" or d.get("publication_state") == "legacy_weapon_scaffolding":
            continue
        if d.get("publication_state") == "unpublished" and not d.get("frame_id"):
            continue
        parent = frames.get(d.get("frame_id"))
        allowed = {
            "canonical": {"canonical"},
            "diagnostic_fixture": {"canonical", "diagnostic_fixture"},
            "unpublished": {"canonical", "diagnostic_fixture", "unpublished"},
        }.get(d.get("publication_state"), set())
        if parent is None or parent.data.get("publication_state") not in allowed:
            errors.append(f"{record.path}: missing or unpublished/ineligible Frame reference")
    return errors


def discover(root: Path) -> tuple[list[Record], list[str]]:
    records, errors = [], []
    for domain in sorted(GAMEPLAY_ROOTS):
        for path in sorted((root / domain).rglob("*.md")):
            try:
                data = parse_frontmatter(path)
                if data.get("entity_kind") in KINDS:
                    records.append(Record(path.relative_to(root), data, path.read_text(encoding="utf-8-sig")))
            except MetadataError as exc:
                errors.append(f"{path.relative_to(root)}: {exc}")
    return records, errors


def run_identity_checks(root: Path) -> list[str]:
    records, errors = discover(root)
    errors.extend(validate_records(records))
    active_frames = {r.data.get("frame_id") for r in records
                     if r.data.get("entity_kind") == "weapon_frame" and published(r.data)}
    combos = root / "04_Player_Entities/Registries/Registry_Combos.md"
    if combos.exists():
        for identifier in re.findall(r"\[weapon_frame::\s*([^\]]+)\]", combos.read_text(encoding="utf-8-sig")):
            if identifier.strip() not in active_frames:
                errors.append(f"{combos.relative_to(root)}: noncanonical weapon_frame {identifier}")
    # Bounded lint for explicit publication queries. This does not execute Dataview.
    for domain in sorted(GAMEPLAY_ROOTS):
        for path in sorted((root / domain).rglob("*.md")):
            text = path.read_text(encoding="utf-8-sig")
            for query in re.findall(r"```dataview\s*\n(.*?)```", text, flags=re.S):
                if not re.search(r'entity_kind\s*=\s*[\"\']weapon_(?:frame|pattern)[\"\']', query):
                    continue
                valid = False
                for state, (status, canonical) in PUBLICATION.items():
                    predicates = (rf'status\s*=\s*[\"\']{status}[\"\']',
                                  rf'publication_state\s*=\s*[\"\']{state}[\"\']',
                                  rf'canonical_content\s*=\s*{str(canonical).lower()}\b')
                    valid |= all(re.search(p, query) for p in predicates)
                if not valid:
                    errors.append(f"{path.relative_to(root)}: weapon query missing consistent publication predicates")
    return errors


INPUT_KEYS = {
    "input.semantic_actions", "input.default_bindings", "input.modes_and_contexts",
    "input.reservation_and_rebinding", "input.intent_binding",
}
SET_KEYS = {
    "weapon_set.prepared_configuration", "weapon_set.active_set",
    "weapon_set.wield_state", "weapon_set.transition_context",
}
INPUT_TARGETS = {
    "weapon_channel_1": ("LMB", "operation_edges", "07_Gear_Inventory/Equipment_PaperDoll"),
    "weapon_channel_2": ("RMB", "operation_edges", "07_Gear_Inventory/Equipment_PaperDoll"),
    "aim": ("LeftAlt", "hold", "05_Combat_Survival/Weapon_Core"),
    "reload": ("R", "press", "05_Combat_Survival/Magic_Batteries"),
    "profile_q": ("Q", "operation_edges", "04_Player_Entities/Skill_Execution"),
    "profile_e": ("E", "operation_edges", "04_Player_Entities/Skill_Execution"),
    "switch_weapon_set": ("TBD", "press", "07_Gear_Inventory/Equipment_PaperDoll"),
    "cantrip_modifier": ("TBD", "hold", "04_Player_Entities/Skill_Execution"),
}


def normalize_binding(binding: str) -> str:
    aliases = {"lmb": "mouse1", "rmb": "mouse2", "lalt": "leftalt", "alt": "leftalt"}
    keys = re.sub(r"\s+", "", binding.lower()).split("+")
    return "+".join(sorted(aliases.get(key, key) for key in keys))


def read_set_schema(path: Path) -> dict:
    text = path.read_text(encoding="utf-8-sig")
    schemas = []
    for block in re.findall(r"```yaml\s*\n(.*?)```", text, flags=re.S):
        data = load_yaml(block)
        if "weapon_set_contract" in data:
            schemas.append(data["weapon_set_contract"])
    if len(schemas) != 1 or not isinstance(schemas[0], dict):
        raise MetadataError("expected exactly one weapon_set_contract mapping")
    return schemas[0]


def validate_set_schema(schema: dict) -> list[str]:
    """Validate declarative shapes/channels. Never simulate occupancy or execute an Action."""
    errors = []
    expected_fields = {"set_ids", "hand_slots", "item_reference", "placement_fields",
                       "layout_shapes", "channel_mapping", "transition_intent", "eligibility_owner"}
    if set(schema) != expected_fields:
        errors.append("Set schema contains missing/extra responsibility fields")
    for key, expected in (("set_ids", ["A", "B"]), ("hand_slots", [1, 2]),
                          ("item_reference", "ItemID"), ("placement_fields", ["item_ref", "occupies"]),
                          ("transition_intent", "switch_weapon_set"), ("eligibility_owner", "ACTION_EXECUTION")):
        if schema.get(key) != expected:
            errors.append(f"Set contract: invalid {key}")
    shapes = {"single_1h": [[1]], "dual_1h": [[1], [2]], "two_handed": [[1, 2]]}
    if schema.get("layout_shapes") != shapes:
        errors.append("Set shapes must use one 2H placement across both slots")
    mapping = schema.get("channel_mapping")
    if not isinstance(mapping, dict) or set(mapping) != set(shapes):
        errors.append("Set channel_mapping must cover the same three layout shapes")
        return errors
    for shape, placements in shapes.items():
        # Contract acceptance: single/2H use two operations of ONE placement;
        # dual uses the Primary of each placement. This is not a runtime channel resolver.
        expected = {
            "weapon_channel_1": {"recipient_slots": placements[0], "operation_field": "primary_operation"},
            "weapon_channel_2": {"recipient_slots": placements[-1],
                                 "operation_field": "primary_operation" if shape == "dual_1h" else "alt_operation"},
        }
        if mapping[shape] != expected:
            errors.append(f"Set channel mapping violates {shape} contract")
    return errors


def check_set_input_contracts(root: Path) -> list[str]:
    errors = []
    owners = {"INPUT_CONTRACT": [], "WEAPON_SET": []}
    for domain in sorted(GAMEPLAY_ROOTS):
        for path in sorted((root / domain).rglob("*.md")):
            try:
                data = parse_frontmatter(path)
            except MetadataError as exc:
                errors.append(f"{path.relative_to(root)}: {exc}")
                continue
            if data.get("status") != "active":
                continue
            keys = data.get("owns", [])
            if not isinstance(keys, list):
                keys = []  # General metadata diagnostics belong to vault_guard.
            for identifier, prefix in (("INPUT_CONTRACT", "input."), ("WEAPON_SET", "weapon_set.")):
                if data.get("canonical_id") == identifier or any(str(k).startswith(prefix) for k in keys):
                    owners[identifier].append((path, data))
    for identifier, candidates in owners.items():
        if len(candidates) != 1:
            errors.append(f"expected exactly one active {identifier} owner, got {len(candidates)}")
            continue
        path, data = candidates[0]
        expected_keys = INPUT_KEYS if identifier == "INPUT_CONTRACT" else SET_KEYS
        if data.get("canonical_id") != identifier or set(data.get("owns", [])) != expected_keys:
            errors.append(f"{path.relative_to(root)}: {identifier} owns unexpected/missing responsibilities")
        if identifier == "WEAPON_SET":
            try:
                errors.extend(f"{path.relative_to(root)}: {e}" for e in validate_set_schema(read_set_schema(path)))
            except MetadataError as exc:
                errors.append(f"{path.relative_to(root)}: {exc}")
            continue
        text = path.read_text(encoding="utf-8-sig")
        records = {}
        bindings = {}
        for block in re.split(r"^###\s+", text, flags=re.M)[1:]:
            pairs = re.findall(r"^\[([\w]+)::\s*(.*?)\]\s*$", block, flags=re.M)
            record = dict(pairs)
            if "action_id" not in record:
                continue
            action = record["action_id"]
            if len(record) != len(pairs) or action in records:
                errors.append(f"{path.relative_to(root)}: duplicate input action or fields: {action}")
            records[action] = record
            required = {"action_id", "default_binding", "input_mode", "context", "gameplay_owner", "consumer_role"}
            if not required <= record.keys() or not all(present(record.get(k)) for k in required):
                errors.append(f"{path.relative_to(root)}: incomplete input record {action}")
                continue
            if record["input_mode"] not in {"press", "hold", "operation_edges"}:
                errors.append(f"{path.relative_to(root)}: invalid input mode for {action}")
            if record["default_binding"] != "TBD":
                key = (record["context"], normalize_binding(record["default_binding"]))
                if key in bindings:
                    errors.append(f"{path.relative_to(root)}: binding collision {bindings[key]} / {action} in {key[0]}")
                bindings[key] = action
        for action, (binding, mode, consumer) in INPUT_TARGETS.items():
            record = records.get(action, {})
            if (normalize_binding(record.get("default_binding", "")) != normalize_binding(binding)
                    or record.get("input_mode") != mode or record.get("context") != "gameplay"
                    or record.get("gameplay_owner") != f"[[{consumer}]]"):
                errors.append(f"{path.relative_to(root)}: missing or incompatible semantic contract {action}")
    return errors


# Accepted semantic contracts: no runtime energy resolver or tuning numbers.
ENERGY_CONTRACTS = {
    "battery_contract": ("05_Combat_Survival/Magic_Batteries.md", {
        "state_owner": "MAGIC_BATTERIES", "runtime_owner": "ItemID",
        "state_field": "battery_state", "states": ["Full", "Drained"],
        "eligible_source_state": "Full", "transactions_per_full_state": 1,
        "post_state": "Drained", "preserves_item_id": True,
        "internal_charge_counter": False, "partial_state": False,
        "source_reservation_owner": "Inventory",
        "transaction_fields": ["source_item_id", "recipient_ref", "eligibility",
            "service_requirements", "commit_point", "result", "post_state"],
        "atomic_result": True, "before_commit": ["source_full", "recipient_unchanged"],
        "after_commit": ["source_drained", "result_applied"],
    }),
    "reload_contract": ("05_Combat_Survival/Magic_Batteries.md", {
        "intent": "reload", "active_set_recipients": "eligible_incomplete_magazine_itemids",
        "recipient_policy": "most_depleted", "comparator": "prototype_bound",
        "tie_break": "deterministic_prototype_bound", "recipient_visible": True,
        "recipients_per_action": 1, "source_count": 1,
        "source_binding": "immutable", "recipient_binding": "immutable",
        "result": "recipient_magazine_to_capacity", "remainder_changes_cost": False,
        "full_recipient": "no_transaction", "repeated_intent": "re_evaluate_after_completion",
        "resets": [],
    }),
    "magazine_contract": ("05_Combat_Survival/Weapon_Ranged.md", {
        "state_owner": "WEAPON_RANGED", "runtime_owner": "ItemID",
        "current_field": "magazine_current", "capacity_owner": "Pattern",
        "capacity_field": "magazine_capacity", "consumption_field": "shot_consumption",
        "reload_field": "reload_service_ref", "optional_for_pattern": True,
        "shot_recipient": "executing_weapon_itemid", "default_shot_cost": 1,
        "switch_preserves_state": True, "depletion_remaps_channel": False,
    }),
    "skill_battery_contract": ("04_Player_Entities/Skill_Execution.md", {
        "opt_in_field": "battery_source_required", "service_field": "battery_service_ref",
        "source_count": 1, "source_state": "Full", "post_state": "Drained",
        "result": "activation_energy", "reservation_owner": "Inventory",
        "uses_weapon_magazine": False, "transaction_owner": "MAGIC_BATTERIES",
    }),
}
OLD_ENERGY_FIELDS = {
    "charge_count", "initial_charges", "consumed_charges", "remaining_charges",
    "remaining_battery_charges", "battery_charge", "battery_charges", "partial_charge",
    "remaining_energy", "residual_charge", "leftover_impulse", "packet_id",
    "packet_queue", "battery_packet", "battery_queue_capacity", "weapon_reserve",
    "casting_reserve", "casting_reserve_required", "impulse_cost", "active_cell_capacity_delta",
}


def check_energy_contracts(root: Path) -> list[str]:
    errors = []
    for name, (relative, expected) in ENERGY_CONTRACTS.items():
        path = root / relative
        if not path.exists():
            errors.append(f"{relative}: missing energy owner contract {name}")
            continue
        body = path.read_text(encoding="utf-8")
        found = []
        for block in re.findall(r"```yaml\s*\n(.*?)```", body, re.S):
            if not re.search(rf"^{name}:", block, re.M):
                continue
            try:
                value = load_yaml(block)
            except (MetadataError, ValueError) as exc:
                errors.append(f"{relative}: invalid {name}: {exc}")
                continue
            found.append(value.get(name) if isinstance(value, dict) else None)
        if len(found) != 1 or not isinstance(found[0], dict):
            errors.append(f"{relative}: expected exactly one {name} mapping")
            continue
        actual = found[0]
        for key, value in expected.items():
            if actual.get(key) != value or type(actual.get(key)) is not type(value):
                errors.append(f"{relative}: incompatible {name}.{key}")
        if set(actual) != set(expected):
            errors.append(f"{relative}: unexpected or missing {name} fields")

    for domain in sorted(GAMEPLAY_ROOTS):
        for path in sorted((root / domain).rglob("*.md")):
            try:
                metadata = parse_frontmatter(path)
            except MetadataError as exc:
                errors.append(str(exc))
                continue
            if metadata.get("status") != "active":
                continue
            text = path.read_text(encoding="utf-8")
            # Check declared fields/records only. Historical prose and deprecated files
            # may discuss retired vocabulary without defining a live resource.
            for section in re.split(r"(?m)^### ", text):
                if re.search(r"\[(?:status|publication_status|design_status)::\s*deprecated\]", section):
                    continue
                fields = set(k.lower() for k in re.findall(r"\[([\w]+)::", section))
                fields.update(k.lower() for k in re.findall(r"(?m)^\s*([\w]+):(?::)?[ \t]", section))
                bad = fields & OLD_ENERGY_FIELDS
                for key in sorted(bad):
                    errors.append(f"{path.relative_to(root)}: active legacy energy field {key}")
                if re.search(r"\[parameter_contract_id::\s*prepared_battery_queue_capacity\]", section):
                    errors.append(f"{path.relative_to(root)}: active legacy queue parameter")
                if re.search(r"(?:supply_contract::?\s*|authorized_requesters::[^\n]*)(?:battery_impulse|battery_packet)", section):
                    errors.append(f"{path.relative_to(root)}: active legacy energy consumer")
                if ("[module_def_id:: long_thread_battery_rack]" in section
                        and "[publication_status:: approved]" in section):
                    errors.append(f"{path.relative_to(root)}: retired battery rack effect published")
    return errors


PROFICIENCY_FIELDS = {
    "identity": ["pawn_id", "frame_id"], "runtime_owner": "Pawn", "baseline_source": "FieldProfile",
    "relation_field": "frame_proficiencies", "record_fields": ["frame_id", "proficiency"],
    "levels": [0, 1, 2, 3], "admission_level": 1, "admitted_moveset": "full_pattern",
    "exceptional_technique_required": False,
    "handling_axis": "return_to_controlled_readiness_after_commitment",
    "natural_debt_preserved": True, "spatial_job_may_outweigh_level": True,
    "universal_modifiers": [], "mastery_dependency": False, "action_owner": "ACTION_EXECUTION",
    "device_state_owner": "ItemID", "changes_input_mapping": False, "owns_service_capacity": False,
}


def validate_frame_proficiencies(value, canonical_frames: set[str]) -> list[str]:
    """Validate sparse published relationships; never infer missing assignments."""
    if not isinstance(value, list):
        return ["frame_proficiencies must be a list"]
    errors, seen = [], set()
    for record in value:
        if not isinstance(record, dict) or set(record) != {"frame_id", "proficiency"}:
            errors.append("proficiency record needs exactly frame_id and proficiency")
            continue
        identifier, level = record["frame_id"], record["proficiency"]
        if not present(identifier) or identifier not in canonical_frames:
            errors.append("proficiency assignment needs canonical active Frame")
        elif identifier in seen:
            errors.append("duplicate Frame proficiency")
        else:
            seen.add(identifier)
        if type(level) is not int or level not in (0,1,2,3):
            errors.append("proficiency must be integer 0..3")
    return errors


def check_proficiency_contracts(root: Path) -> list[str]:
    errors = []
    required = {
        "proficiency_contract": ("04_Player_Entities/Proficiency_Arsenal.md", PROFICIENCY_FIELDS),
        "profile_service_contract": ("04_Player_Entities/Skill_Build_Philosophy.md", {
            "authored_source": "FieldProfile", "definition_registry": "Registry_Combos",
            "field": "base_service_capacity", "legality_owner": "Thermos_Assembly",
            "proficiency_contributes": False}),
    }
    for name, (relative, expected) in required.items():
        path = root/relative
        if not path.exists():
            errors.append(f"{relative}: missing {name}")
            continue
        mappings = []
        for block in re.findall(r"```yaml\s*\n(.*?)```", path.read_text(encoding="utf-8"), re.S):
            if not re.search(rf"^{name}:", block, re.M):
                continue
            try:
                mappings.append(load_yaml(block).get(name))
            except MetadataError as exc:
                errors.append(f"{relative}: {exc}")
        if len(mappings) != 1 or not isinstance(mappings[0], dict):
            errors.append(f"{relative}: expected one {name}")
            continue
        actual = mappings[0]
        if set(actual) != set(expected):
            errors.append(f"{relative}: incompatible {name} fields")
        for key, value in expected.items():
            if actual.get(key) != value or type(actual.get(key)) is not type(value):
                errors.append(f"{relative}: incompatible {name}.{key}")

    records, discovery_errors = discover(root)
    errors.extend(discovery_errors)
    canonical = {r.data["frame_id"] for r in records
                 if r.data.get("entity_kind") == "weapon_frame" and published(r.data)}
    relation_owners = []
    for domain in sorted(GAMEPLAY_ROOTS):
        for path in sorted((root/domain).rglob("*.md")):
            try:
                data = parse_frontmatter(path)
            except MetadataError as exc:
                errors.append(str(exc))
                continue
            if data.get("status") != "active":
                continue
            owned = data.get("owns", [])
            if (data.get("canonical_id") == "PROFICIENCY_RELATION"
                    or any(str(k).startswith("proficiency.") for k in owned)):
                relation_owners.append(path)
                if (data.get("canonical_id") != "PROFICIENCY_RELATION" or
                        set(owned) != {"proficiency.pawn_frame_relation", "proficiency.admission_and_handling"}):
                    errors.append(f"{path.relative_to(root)}: invalid proficiency owner boundary")
            text = path.read_text(encoding="utf-8")
            if path.name == "Proficiency_Arsenal.md" and "[base_service_capacity::" in text:
                errors.append("Proficiency cannot publish Profile service capacity")
            if "frame_proficiencies" in data:
                if data.get("entity_kind") not in {"pawn", "field_profile"}:
                    errors.append(f"{path.relative_to(root)}: misplaced frame_proficiencies")
                errors.extend(f"{path.relative_to(root)}: {e}" for e in
                              validate_frame_proficiencies(data["frame_proficiencies"], canonical))
            for block in re.split(r"(?m)^#{2,3} ", text):
                if re.search(r"\[(?:design_status|status)::\s*deprecated\]", block):
                    continue
                fields = re.findall(r"\[([\w]+)::", block)
                if any("mastery" in key.lower() for key in fields) or re.search(r"\[tag_kind::\s*mastery\]", block):
                    errors.append(f"{path.relative_to(root)}: active Mastery record")
                if re.search(r"(?mi)^\s*EffectiveProf\s*=", block):
                    errors.append(f"{path.relative_to(root)}: legacy EffectiveProf arithmetic")
                for raw in re.findall(r"(?m)^\[frame_proficiencies::\s*(.*?)\]\s*$", block):
                    try:
                        value = json.loads(raw)
                    except ValueError:
                        errors.append(f"{path.relative_to(root)}: invalid frame_proficiencies JSON")
                        continue
                    errors.extend(f"{path.relative_to(root)}: {e}" for e in validate_frame_proficiencies(value, canonical))
    if len(relation_owners) != 1:
        errors.append("exactly one active Proficiency relation owner required")
    return errors


def run(root: Path) -> list[str]:
    return (run_identity_checks(root) + check_set_input_contracts(root)
            + check_energy_contracts(root) + check_proficiency_contracts(root))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = run(args.root)
    records, _ = discover(args.root)
    counts = {kind: sum(r.data.get("entity_kind") == kind and published(r.data) for r in records)
              for kind in KINDS}
    print(f"Canonical Frames={counts['weapon_frame']}; Patterns={counts['weapon_pattern']}")
    for error in errors:
        print(error)
    print(f"Overhaul contracts: {'FAIL' if errors else 'PASS'} ({len(errors)} violations)")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
