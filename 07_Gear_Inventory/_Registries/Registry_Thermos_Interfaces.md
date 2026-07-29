---
type: registry
status: active
index_route: owner
index_group: gear_inventory
index_order: 60
index_summary: "Задаёт правила и последствия системы «Реестр интерфейсов Термоса»."
read_when: "Читайте при изменении входов, состояний, стоимости или последствий системы «Реестр интерфейсов Термоса»."
system: thermos_interfaces
tags: [thermos, interfaces, ownership, assembly]
related_files:
  - "[[07_Gear_Inventory/Thermos_System|Термос]]"
  - "[[07_Gear_Inventory/Thermos_Assembly|Сборка Термоса]]"
  - "[[04_Player_Entities/Body_Morphology_Contract|Морфология тела]]"
  - "[[07_Gear_Inventory/Inventory_Architecture|Inventory Custody]]"
---
# Реестр интерфейсов Термоса

Одна строка — одна направленная связь. `OWNER` разрешает результат; `PROVIDER` публикует bounded input; `CONSUMER` читает revisioned output. Роль не передаёт runtime-власть.

| Interface ID | Provider | Role | Consumer | Owner | Result / failure | Does not own |
|---|---|---|---|---|---|---|
| `THR-IF-001-BODY-ENVELOPE` | [[04_Player_Entities/Body_Morphology_Contract|Body Morphology]] | PROVIDER | Assembly Resolver | `BODY_MORPHOLOGY` | immutable `MorphologySnapshot@revision`; absent → no FitQuote, blocked | refit/topology/service |
| `THR-IF-002-BASE-SERVICE` | [[04_Player_Entities/_Registries/Registry_Combos|full hero-kit]] | PROVIDER | Assembly Resolver | Registry_Combos authored hero-kit | BaseServiceCapacity; absent family → declared unavailable | support delta/final legality |
| `THR-IF-003-MODEL-DEFINITION` | [[07_Gear_Inventory/_Registries/Registry_Thermoses|Thermos Model Registry]] | PROVIDER | Assembly Resolver | `THERMOS_MODEL_REGISTRY` | envelope/nodes/model delta; incomplete → blocked_topology | instance state/effects |
| `THR-IF-004-MODULE-DEFINITION` | [[07_Gear_Inventory/_Registries/Registry_Thermos_Modules|Thermos Module Registry]] | PROVIDER | Assembly Resolver | `THERMOS_MODULE_REGISTRY` | patterns/load/effects; missing field → blocked_calibration | ItemID/active state |
| `THR-IF-005-ITEMID-RESERVATION` | [[07_Gear_Inventory/Inventory_Architecture|Inventory Custody]] | PROVIDER | Assembly Resolver | `INVENTORY_CUSTODY` | unique prepare/atomic swap; duplicate → commit fails untouched | draft ownership/effect legality |
| `THR-IF-006-FIT-QUOTE` | Assembly Resolver | OWNER | Hub professional/UI | [[07_Gear_Inventory/Thermos_Assembly|Assembly Resolver]] | compatible/refit_required/incompatible; refit required → no commit | body/BaseService mutation |
| `THR-IF-007-TOPOLOGY` | model nodes + module pattern | PROVIDER | Assembly Resolver | Assembly Resolver | selected pattern/nodes; conflict → blocked | effect policy/service delta |
| `THR-IF-008-SERVICE-LEGALITY` | BaseService + module loads | PROVIDER | Assembly Resolver | Assembly Resolver | Support/Final/Used; self funding/overflow → blocked | parameter policy/mass |
| `THR-IF-009-EFFECT-RESOLUTION` | EffectContract request + debt | PROVIDER | ParameterContract resolver | [[04_Player_Entities/_Registries/Registry_Parameter_Contracts|Parameter Contract owner]] | requested/applied/floor/final/reason; invalid → inactive/blocked | topology/local priority-floor-cap |
| `THR-IF-010-ASSEMBLY-SNAPSHOT` | Assembly Resolver | OWNER | PaperDoll/Ballistics/Weight/Dissonance | Assembly Resolver | immutable revision input; failed commit keeps prior revision | combat/mass/Dissonance result |
| `THR-IF-011-COVERAGE` | committed pattern geometry/effect eligibility | PROVIDER | Ballistics; then PaperDoll consumes its output | [[05_Combat_Survival/Ballistics_Armor|Ballistics Armor]] | PatternCoverageBinding → ResolvedCoverageSnapshot; missing collision contract → no installable plate | topology/service |
| `THR-IF-012-PHYSICAL-MASS` | installed ItemIDs + base mass | PROVIDER | Physical Weight | [[07_Gear_Inventory/Physical_Weight|Physical Weight]] | mass graph → TotalLoad/load stage; missing mass → no commit | fit/topology/service |
| `THR-IF-013-DISSONANCE` | source signature/contributor rule | PROVIDER | Dissonance resolver | [[05_Combat_Survival/Dissonance_System|Dissonance System]] | declared `none` is valid; undeclared required source blocks; one event per occurrence | second Pulse/Gate override |
| `THR-IF-014-ECONOMY-QUOTE` | model/module/refit request | PROVIDER | Economy quote | [[06_Economy_Loot/Economy_Core|Economy]] | acquisition/refit/replacement quote; unavailable blocks purchase | fit/topology/service |

## Invariants

1. Provider publishes only named input; no interface duplicates owner result.
2. Failed input returns readable blocked/reason, never guessed fallback.
3. Assembly revision is the sole cross-consumer projection; consumers never rebuild legality.
4. Economy can deny acquisition without rewriting a legally owned assembly; disabled effect never frees nodes or refunds service.
