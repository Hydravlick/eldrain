---
status: active
system: gear_inventory
registry_type: thermos_modules
tags:
  - thermos
  - modules
  - registry
  - topology
  - service
related_files:
  - "[[07_Gear_Inventory/Thermos_System|Thermos System]]"
  - "[[07_Gear_Inventory/Thermos_Assembly|Thermos Assembly]]"
  - "[[07_Gear_Inventory/Registries/Registry_Thermoses|Thermos Models]]"
  - "[[07_Gear_Inventory/Registries/Registry_Thermos_Interfaces|Thermos Interfaces]]"
  - "[[04_Player_Entities/Registries/Registry_Parameter_Contracts|Parameter Contracts]]"
type: registry
index_route: owner
index_group: gear_inventory
index_order: 70
index_summary: "Хранит схему и записи: Реестр модулей Термоса."
read_when: Когда нужен контракт «Реестр модулей Термоса» и его границы с соседними владельцами.
---
# Реестр модулей Термоса

> [!important] Definition, не assembly
> Definition хранит только модель модуля. Selected pattern, occupied nodes, damage, active body interface и stitched state принадлежат assembly instance. Все записи ниже `blocked_calibration`: нет законченных patterns, ParameterContracts и pattern-bound plate coverage.

## Контракт

```markdown
[module_def_id:: stable_module_id]
[allowed_mount_patterns:: UNKNOWN | pattern_id: required_claims(body_region/mount_class/capacity_units)]
[service_load:: UNKNOWN | plate 0, optic 0, seal 0, conduit 0, rig 0, weave 0]
[service_support_delta:: none | plate 0, optic 0, seal 0, conduit 0, rig 0, weave 0]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT | effect_id]
[coverage_contract_ids:: none | UNKNOWN | pattern_id:CoverageContractID]
[concept_effects:: non-authoritative migration note]
[physical_mass:: value | UNKNOWN]
[persistent_dissonance_signature:: UNKNOWN | signature_id]
[dissonance_contributor_rules:: concept_note | registered_rule_id]
[body_interface_kind:: none | InterfaceKind]
[selectable_interface_effect_id:: none | MISSING_PARAMETER_CONTRACT | EffectID]
[ui_search_aliases:: aliases]
[module_type:: functional | battery_rack | template]
[active_cell_capacity_delta:: none | value]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required | split_required | proven_atomic]
[publication_status:: blocked_calibration | approved]
[balance_state:: concept | prototype | unknown]
```

Размещение, service legality и atomicity определяет [[07_Gear_Inventory/Thermos_Assembly#Правила definition binding]].

## Candidate records

### Навеска «Базальт»
[module_def_id:: basalt_shell]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: UNKNOWN]
[concept_effects:: coverage chest/arm_guards/shoulder_pads/shin_guards; environment resistance 55; segmented conduit fuses; cargo interaction]
[physical_mass:: 22kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: armor-shell concept]
[body_interface_kind:: none]
[selectable_interface_effect_id:: none]
[ui_search_aliases:: basalt, shell, armor]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: unknown]
Тяжёлая навеска; plate coverage contracts отсутствуют.

### Сборка «Хранитель Очага»
[module_def_id:: hearth_keeper]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: UNKNOWN]
[concept_effects:: coverage l_shoulder/r_shoulder/thighs/chest_center; environment resistance 70; frontal energy manifold]
[physical_mass:: 18kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: hearth protection concept]
[body_interface_kind:: none]
[selectable_interface_effect_id:: none]
[ui_search_aliases:: hearth, keeper, protection]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: split_required]
[publication_status:: blocked_calibration]
[balance_state:: unknown]
Трёхсемейная assembly требует split или доказательства атомарности.

### Сбруя «Наёмник»
[module_def_id:: mercenary_rig]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: UNKNOWN]
[concept_effects:: coverage upper_chest/stomach/forearms; environment resistance 35; bracer conduit branch; mobility/support exchange]
[physical_mass:: 12kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: mercenary rig concept]
[body_interface_kind:: none]
[selectable_interface_effect_id:: none]
[ui_search_aliases:: mercenary, rig]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: unknown]
Сбруя наёмника.

### Обвязка «Собиратель»
[module_def_id:: scavenger_wrap]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: UNKNOWN]
[concept_effects:: single chest-heart plate; environment resistance 15; cargo/load distribution without Ready Access slots]
[physical_mass:: 6kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: scavenger cargo concept]
[body_interface_kind:: none]
[selectable_interface_effect_id:: none]
[ui_search_aliases:: scavenger, wrap, cargo]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: unknown]
Обвязка добытчика.

### Кассета активных ячеек «Долгая нить»
[module_def_id:: long_thread_battery_rack]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: none]
[concept_effects:: prepared battery queue capacity +1 for one assigned circuit; no damage/range/Heat/Recovery/Bloom bonus]
[physical_mass:: UNKNOWN]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: battery queue concept]
[body_interface_kind:: none]
[selectable_interface_effect_id:: none]
[ui_search_aliases:: long thread, battery rack, cells]
[module_type:: battery_rack]
[active_cell_capacity_delta:: +1]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: prototype]
Увеличивает только подготовленную очередь батарей назначенного контура.

### Эфирная ветвь «Проводник»
[module_def_id:: conduit_robe]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: UNKNOWN]
[concept_effects:: coverage r_shoulder/back_spine; environment resistance 40; spine conduit branch; energy/cantrip function]
[physical_mass:: 3kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: conduit/cantrip concept]
[body_interface_kind:: none]
[selectable_interface_effect_id:: none]
[ui_search_aliases:: conduit, robe]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: unknown]
Эфирная ветвь.

### Вуали «Призрак»
[module_def_id:: wraith_veils]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: none]
[concept_effects:: mobility/stealth silhouette exchange; environment resistance 20; no false plate silhouette]
[physical_mass:: 2kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: stealth/mobility concept]
[body_interface_kind:: none]
[selectable_interface_effect_id:: none]
[ui_search_aliases:: wraith, veils, stealth]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: unknown]
Вуали Призрака.

### Противовесное ярмо
[module_def_id:: counterweight_yoke]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: none]
[concept_effects:: sustained_carry_limit: increased; physical mass 8kg]
[physical_mass:: 8kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: discovery record: turn commitment parameter; any runtime effect requires a declared ParameterContract]
[body_interface_kind:: load_bearing]
[selectable_interface_effect_id:: MISSING_PARAMETER_CONTRACT]
[ui_search_aliases:: counterweight, yoke, carry]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: prototype]
Опорный контур переноски.

### Пневматическая распорка
[module_def_id:: pneumatic_brace]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: none]
[concept_effects:: brace_hold_limit: extended; activation Heat +10; movement noise +8]
[physical_mass:: 4kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: discovery record: activation Heat and movement-noise parameters; any runtime effect requires a declared ParameterContract]
[body_interface_kind:: none]
[selectable_interface_effect_id:: none]
[ui_search_aliases:: pneumatic, brace]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: prototype]
Пневматическая распорка.

### Тонкомоторная сбруя
[module_def_id:: fine_motor_harness]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: none]
[concept_effects:: powered_tool_precision: increased; heavy_tool_hold: reduced]
[physical_mass:: 2kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: motor concept]
[body_interface_kind:: motor_control]
[selectable_interface_effect_id:: MISSING_PARAMETER_CONTRACT]
[ui_search_aliases:: fine motor, harness]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: prototype]
Тонкомоторная сбруя.

### Сервосухожилие
[module_def_id:: servo_tendon]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: none]
[concept_effects:: device_interaction_time: reduced; Heat +8 per interaction; rigid handwear incompatible]
[physical_mass:: 3kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: discovery record: interaction Heat and rigid-handwear parameters; any runtime effect requires a declared ParameterContract]
[body_interface_kind:: none]
[selectable_interface_effect_id:: none]
[ui_search_aliases:: servo, tendon]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: prototype]
Сервосухожилие.

### Компрессионное плетение
[module_def_id:: compression_weave]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: none]
[concept_effects:: post_impact_stability: extended]
[physical_mass:: 2kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: post-impact/stamina concept]
[body_interface_kind:: layer_support]
[selectable_interface_effect_id:: MISSING_PARAMETER_CONTRACT]
[ui_search_aliases:: compression, weave]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: prototype]
Компрессионное плетение.

### Решётка рубцовых пластин
[module_def_id:: scar_plate_lattice]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: UNKNOWN]
[concept_effects:: chest/back plate lattice; soft_layer_impact_tolerance: increased; physical mass 6kg]
[physical_mass:: 6kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: discovery record: mass and movement parameters; coverage UNKNOWN; any runtime effect requires a declared ParameterContract]
[body_interface_kind:: layer_support]
[selectable_interface_effect_id:: MISSING_PARAMETER_CONTRACT]
[ui_search_aliases:: scar, plate, lattice]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: prototype]
Coverage contract ids are UNKNOWN.

### Проводящая коса
[module_def_id:: conductor_braid]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: none]
[concept_effects:: body_to_thermos_heat_transfer: earlier]
[physical_mass:: 1kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: discovery record: Dissonance load parameter; any runtime effect requires a declared ParameterContract]
[body_interface_kind:: thermal_conduction]
[selectable_interface_effect_id:: MISSING_PARAMETER_CONTRACT]
[ui_search_aliases:: conductor, braid, thermal]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: prototype]
Проводящая коса.

### Шунт перегрева
[module_def_id:: overheat_shunt]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: none]
[concept_effects:: overload_threshold: increased; cantrip_backlash_outcome +1 step]
[physical_mass:: 2kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: discovery record: backlash and pulse parameters; any runtime effect requires a declared ParameterContract]
[body_interface_kind:: none]
[selectable_interface_effect_id:: none]
[ui_search_aliases:: overheat, shunt]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: prototype]
Шунт перегрева.

### Усатая антенна
[module_def_id:: whisker_array]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: none]
[concept_effects:: local_environment_cue_lead: earlier]
[physical_mass:: 1kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: discovery record: Dissonance load parameter; any runtime effect requires a declared ParameterContract]
[body_interface_kind:: sensory_gain]
[selectable_interface_effect_id:: MISSING_PARAMETER_CONTRACT]
[ui_search_aliases:: whisker, antenna, sensory]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: prototype]
Усатая антенна.

### Сетка эхо-линз
[module_def_id:: echo_lens_mesh]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: none]
[concept_effects:: cue_lead: earlier; injury_threshold: reduced; Heat-warning false positives enabled]
[physical_mass:: 2kg]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: discovery record: cue, injury, and Heat-warning false-positive parameters; any runtime effect requires a declared ParameterContract]
[body_interface_kind:: none]
[selectable_interface_effect_id:: none]
[ui_search_aliases:: echo, lens, detection]
[module_type:: functional]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: prototype]
Сетка эхо-линз.

### Шаблон модуля Термоса
[module_def_id:: template_thermos_module]
[allowed_mount_patterns:: UNKNOWN]
[service_load:: UNKNOWN]
[service_support_delta:: none]
[effect_contract_ids:: MISSING_PARAMETER_CONTRACT]
[coverage_contract_ids:: UNKNOWN]
[concept_effects:: format only]
[physical_mass:: UNKNOWN]
[persistent_dissonance_signature:: UNKNOWN]
[dissonance_contributor_rules:: none]
[body_interface_kind:: none]
[selectable_interface_effect_id:: none]
[ui_search_aliases:: template]
[module_type:: template]
[active_cell_capacity_delta:: none]
[install_policy:: hub_stitch_only]
[atomicity_status:: atomicity_review_required]
[publication_status:: blocked_calibration]
[balance_state:: unknown]
Форматная запись, не игровой предмет.

```dataview
TABLE module_def_id, physical_mass, body_interface_kind, publication_status, balance_state
FROM "07_Gear_Inventory/Registries/Registry_Thermos_Modules"
WHERE module_def_id
```
