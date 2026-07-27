---
type: registry
status: active
system: gear_inventory
registry_type: thermos_models
tags: [thermos, registry, topology, fit]
related_files:
  - "[[07_Gear_Inventory/Thermos_System|Thermos System]]"
  - "[[07_Gear_Inventory/Thermos_Assembly|Thermos Assembly]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces|Thermos Interfaces]]"
  - "[[07_Gear_Inventory/Equipment_PaperDoll|Equipment Paper Doll]]"
---
# Реестр моделей Термоса

> [!important] Definition, не assembly
> Эта страница хранит свойства модели. Конкретная посадка, `fit_revision`, selected pattern, occupied nodes, damage и `stitched_state` принадлежат assembly instance. `slot_count` — derived сумма capacity реальных nodes и не хранится; `slot_layout` и `fit_profiles` удалены.

## Контракт модели

```markdown
[model_def_id:: stable_model_id]
[fit_envelope:: MorphologyEnvelope | UNKNOWN]
[mount_nodes:: node_id/body_region/capacity_units/accepted_mount_classes | UNKNOWN]
[base_service_support_delta:: plate 0, optic 0, seal 0, conduit 0, rig 0, weave 0]
[assembly_policy:: hub_stitch_only]
[physical_mass:: value | UNKNOWN]
[definition_status:: blocked_topology | approved]
```

Models remain blocked until the actual topology, fit envelope, mass and Paper Doll mapping exist. Model support delta is the only definition-level capacity contribution; support modules are tested against authored BaseServiceCapacity before any delta participates.

### Городской серийный Термос
[model_def_id:: civic_standard]
[fit_envelope:: UNKNOWN]
[mount_nodes:: UNKNOWN]
[base_service_support_delta:: plate 0, optic 0, seal 0, conduit 0, rig 0, weave 0]
[assembly_policy:: hub_stitch_only]
[physical_mass:: UNKNOWN]
[definition_status:: blocked_topology]

Ремонтируемая городская неокультурная основа; её реальная топология и профессиональная подгонка ещё не авторизированы.

### Шаблон Термоса
[model_def_id:: template_thermos]
[fit_envelope:: UNKNOWN]
[mount_nodes:: UNKNOWN]
[base_service_support_delta:: plate 0, optic 0, seal 0, conduit 0, rig 0, weave 0]
[assembly_policy:: hub_stitch_only]
[physical_mass:: UNKNOWN]
[definition_status:: blocked_topology]

Форматная запись, не игровой предмет.

```dataview
TABLE model_def_id, fit_envelope, physical_mass, definition_status
FROM "07_Gear_Inventory/_Registries/Registry_Thermoses"
WHERE model_def_id
```
