---
type: system
status: active
index_route: owner
index_group: gear_inventory
index_order: 220
index_summary: "Задаёт правила и последствия системы «Термос: носимая система экипировки»."
read_when: "Читайте при изменении входов, состояний, стоимости или последствий системы «Термос: носимая система экипировки»."
system: thermos_wearable_equipment
tags: [thermos, wearable_equipment, assembly, service_capacity, hub]
related_files:
  - "[[07_Gear_Inventory/Thermos_Assembly|Сборка Термоса]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces|Интерфейсы Термоса]]"
  - "[[04_Player_Entities/_Registries/Registry_Parameter_Contracts|Параметрические контракты]]"
---
# Термос: носимая система экипировки

> Термос — одна носимая вещь, которую в Хабе раскрывают на столе и вшивают в неё ответ на следующую вылазку. Он несёт покрытие, перчатки, обувь, обвязку, герметизацию, оптику, проводящие ветви и utility-функции; после Deploy шов уже не спрашивает, передумал ли хозяин.

Термос не является набором независимых бронеслотов и не создаёт общий рейтинг силы. Игрок выбирает известную физическую конфигурацию, её обслуживаемые функции и видимые долги; неизвестной остаётся Аномалия, а не правило собственной экипировки.

## 1. Четыре слоя сущностей

| Слой | Хранит | Не хранит |
|---|---|---|
| `ThermosModelDefinition` | `model_def_id`, `fit_envelope`, `mount_nodes`, базовую support-delta модели, `hub_stitch_only` | владельца, refit, свободные nodes, итоговое покрытие/массу/Диссонанс |
| `ModuleDefinition` | `module_def_id`, allowed mount patterns, `service_load`, EffectContracts, базовую массу, Dissonance contributor rules, body interface при наличии | ItemID, выбранный pattern, active/damage/stitch state |
| `InstalledModule` | `module_instance_id`, definition, Thermos instance, selected pattern, occupied nodes, damage, stitched state | policy эффекта или состояние других instances |
| `ThermosAssemblyInstance` | Thermos ItemID, fitted morphology, `fit_revision`, installed ItemIDs, `assembly_revision`, active body interface | definition values, резерв ItemID в черновике, собственный эффект |

Definition описывает тип вещи; instance — реальную вещь. `fit_state`, свободные nodes, `Used`, `Final`, `Remaining`, coverage, масса и Диссонанс всегда derived из revisioned assembly snapshot.

## 2. Семь authority contracts

| Вопрос | Единственный owner | Термос передаёт | Не делает |
|---|---|---|---|
| Fit | [[07_Gear_Inventory/Thermos_Assembly|Assembly Resolver]] | body/model/refit inputs | не меняет Body, hero-kit или tag |
| Topology | Assembly Resolver | mount patterns и node claims | не выводит effect из позиции |
| Service legality | Assembly Resolver | authored BaseServiceCapacity и service load | не создаёт capacity из tag/Chronicle/status/consumable |
| Effect policy | [[04_Player_Entities/_Registries/Registry_Parameter_Contracts|Parameter Contract owner]] | modifier request + intrinsic debt | не задаёт priority/floor/cap |
| Physical mass | [[07_Gear_Inventory/Physical_Weight|Physical Weight]] | instances и base mass | не решает fit/topology/service |
| Dissonance | [[05_Combat_Survival/Dissonance_System|Dissonance System]] | persistent signature/contributor rule | не создаёт второй Pulse |
| Economy | [[06_Economy_Loot/Economy_Core|Economy]] | acquisition/refit/replacement request | не определяет legality |

`effect_axis` — derived search/UI label и не участвует в legality.

## 3. Шесть service families

`plate`, `optic`, `seal`, `conduit`, `rig`, `weave` называют обслуживание, а не эффект. `BaseServiceCapacity(hero-kit, family)` — authored поле полного hero-kit; оно не выводится из Race/Spec и не является XP.

```text
Base(family) = BaseServiceCapacity(hero-kit, family)
SupportLoad(family) = sum(service_load всех support-source modules по family)
SupportSourcesEligible iff SupportLoad(family) <= Base(family) для каждого family
FinalServiceCapacity = Base + ThermosModel.base_service_support_delta
  + sum(ServiceSupportDelta eligible support-module instances)
UsedServiceCapacity = sum(service_load ВСЕХ installed modules, включая supports)
AssemblyValid iff SupportSourcesEligible AND UsedServiceCapacity <= FinalServiceCapacity
```

Support-source сначала должен поместиться в authored Base; его delta не финансирует его установку. Personal Tags, Chronicle, временный status, расходник, self-funding module и взаимно включающаяся support-цепочка не добавляют capacity. Hybrid занимает topology один раз, но платит `service_load` каждому работающему family.

## 4. Effect contract и hybrid atomicity

```yaml
effect_id: stable_id
target_parameter_contract: parameter_contract_id
modifier_request: one_named_parameter_operation
activation_mode: passive | procedure | conditional
condition: declared_signal_or_state
intrinsic_debt: same_raid_cost
debt_lock: protected | mitigable_by_domain_policy
tell: readable_world_feedback
failure_state: declared_failure
```

Модуль — source, не resolver. Его request проходит один ParameterContract; owner решает stack, priority, protected floor, cap, requested/applied/final и reason. Три и более независимых функций по умолчанию разбиваются на assembly/preset. Один atomic hybrid допустим только при общем mechanism, trigger/lifecycle, failure-state и vulnerability. Каждая независимая функция платит service и same-raid debt; один mass fact не списывается как три разных долга.

## 5. Fit, lock и disclosure

Fit возвращает только `compatible`, `refit_required` или `incompatible`. Refit выполняет Hub professional и создаёт `fit_revision`; он не меняет Body, hero-kit, Personal Tags или BaseServiceCapacity.

До commit игрок видит: (1) silhouette/patterns/service/exchanges; (2) один resolver-pass со всеми ошибками; (3) snapshot покрытия, массы, Диссонанса, функций и ближайшей уязвимости. В рейде остаётся consequence-only reading: установлено/повреждено/отключено и действующие последствия. Remount, refit и interface switch запрещены после Deploy.

## 6. Assembly validation и acceptance

Все текущие модели остаются `blocked_topology`, а модули — `blocked_calibration`, пока не существуют topology, EffectContracts, domain-owner links, coverage/collision data и калибровка.

Assembly validation закрепляет одного domain owner для каждого результата и записывает revision assembly, domain revisions и причину mismatch. Revisioned assembly snapshot является единственным входом для capacity, legality `slot_count/slot_layout/module_positions`, состояния body interface и UI calculations; definition не хранит этот live state. Публикация snapshot допускается только после fixture validation.

- Один результат fit/topology/service/effect/mass/Dissonance/economy имеет одного owner.
- Definition не содержит live state; одна definition работает в нескольких assemblies без shared state.
- Aggregate SupportLoad проверяется до delta; self/mutual funding невозможен.
- One resolver pass возвращает все ошибки и один revisioned snapshot.
- Draft/preset не владеет ItemID; commit резервирует реальный ItemID ровно раз atomically.
- Damage не освобождает node; loss реален; ghost plan не клонирует вещь.
- Один committed `PatternCoverageBinding` читает Ballistics и выпускает единственный `ResolvedCoverageSnapshot`, который затем одинаково показывает PaperDoll; mass/Dissonance выводят свои owners.
- Source не содержит local priority/floor/cap; protected-floor tooltip показывает requested/applied/floor/final/reason/revision.
