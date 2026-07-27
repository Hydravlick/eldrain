---
type: system
status: active
system: thermos_assembly
tags: [thermos, assembly_resolver, fit, topology, service, instances]
related_files:
  - "[[07_Gear_Inventory/Thermos_System|Термос]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces|Интерфейсы Термоса]]"
  - "[[04_Player_Entities/_Registries/Registry_Parameter_Contracts|Параметрические контракты]]"
---
# Сборка Термоса

> Этот owner разрешает только fit, node topology, service legality, commit и revisioned projection. Он не владеет баллистикой, массой, Диссонансом, экономикой или policy эффекта.

## 1. Runtime entities

```yaml
ThermosAssemblyInstance:
  thermos_instance_id: ItemID
  model_def_id: ThermosModelID
  fitted_for_morphology: MorphologyEnvelopeID
  fit_revision: integer
  installed_module_ids: [ItemID]
  active_body_interface_module_id: ItemID | null
  assembly_revision: integer
  state: committed_hub | deployed | lost

InstalledModule:
  module_instance_id: ItemID
  module_def_id: ModuleDefID
  thermos_instance_id: ItemID
  selected_pattern_id: PatternID
  occupied_nodes: [NodeClaim]
  damage_state: intact | impaired | disabled | destroyed
  stitched_state: stitched_locked
```

`AssemblyDraft` и preset существуют отдельно от живого instance: они хранят definition IDs, desired patterns и предпочтения замены, но не владеют ItemID. Inventory reservation связывает реальные вещи только в prepare/commit-транзакции. Один ItemID резервируется единожды; atomic swap переносит весь набор на новую assembly revision либо не меняет ничего. Ghost plan — UI-просмотр без reservation и без клонирования.

`deployed` запрещает remount, refit и смену `active_body_interface_module_id`. Damage меняет effect eligibility/output по доменному контракту, но не освобождает occupied node. Loss assembly/ItemID остаётся физической потерей.

Повреждение support-модуля в рейде может отключить его runtime-эффект и `ServiceSupportDelta`, но не запускает каскадный демонтаж или повторную монтажную legality-проверку. Committed topology и service reservation остаются зафиксированы до мастера. Если активный Опорный контур отключён, другой установленный контур не включается автоматически: скрытого failover/priority нет.

## 2. Единственный resolver pass

```text
1. Definition completeness
2. FitQuote: compatible | refit_required | incompatible
3. Prepare unique ItemID reservations against expected custody/condition revisions
4. Mount patterns: existing nodes, accepted classes, claims and spatial conflicts
5. Read authored BaseServiceCapacity
6. Aggregate SupportLoad <= Base for six families
7. Compute FinalServiceCapacity; validate UsedServiceCapacity for all modules
8. Validate EffectContract binding -> existing ParameterContract, stack group and protected-debt declaration
9. Atomic custody/assembly commit; stitch lock; increment assembly_revision
10. Emit derived AssemblySnapshot
```

Один pass возвращает все errors с owner и actionable reason. `refit_required` завершает pass до ItemID prepare: лишь Hub professional создаёт следующий `fit_revision`. Любой отказ после prepare освобождает reservation либо безопасно восстанавливается из durable transaction journal; живая сборка до commit не меняется.

Assembly Resolver проверяет существование и совместимость EffectContract, но не читает обратно applied/final effect, итоговую массу, Dissonance, readiness, Tier, Rarity или цену. Эти downstream-результаты не могут повысить capacity и разрешить собственный источник.

## 3. Revisioned projection

```yaml
AssemblySnapshot:
  assembly_revision: integer
  fit: compatible
  occupied_nodes: [NodeClaim]
  service: {base, support_load, final, used, remaining}
  active_body_interface_module_id: ItemID | null
  installed_effect_bindings: [EffectBindingRef]
  pattern_coverage_bindings: [PatternCoverageBindingRef]
  physical_mass_input_revision: integer
  dissonance_input_revision: integer
  assembly_legality: valid
```

Assembly публикует revisioned `PatternCoverageBinding`; [[05_Combat_Survival/Ballistics_Armor|Ballistics]] единолично строит `ResolvedCoverageSnapshot` и владеет hit resolution. [[07_Gear_Inventory/Equipment_PaperDoll|PaperDoll]] показывает этот же Ballistics-owned snapshot, а не рассчитывает покрытие повторно. Physical Weight и Dissonance consume assembly inputs и владеют своими derived outputs. Только один валидный установленный body-interface module может быть активен; его output следует тому же ParameterContract path, что любой эффект.

## 4. Invariants and acceptance fixtures

- OR patterns and AND claims are distinct: wrists are alternatives; a yoke with shoulders+spine is one all-required pattern.
- A support module pays its load before its delta helps; tags/Chronicle/status/consumables/self or mutual loops fail eligibility.
- A hybrid may share physical mass but cannot erase separate service or same-raid effect debt.
- Unknown topology, effect owner/tell/failure, ItemID reservation or installability blocks commit.
- Raid PaperDoll is read-only; disabled module never opens field respec.

Shadow resolver records legacy/new results, assembly revision, domain revisions and mismatch reason. Remove old resolver only after fixtures pass: compatible/refit/incompatible; OR/AND nodes; support boundary; mutual support; hybrid; collision; damage; duplicate ItemID; atomic swap.

1. Two drafts request one ItemID: exactly one commit succeeds.
2. Support at Base is eligible; one point over Base fails even if delta would make Final sufficient.
3. Destroyed module keeps node claim until Hub removal.
4. Damaged plate updates one PatternCoverageBinding revision; Ballistics выпускает один ResolvedCoverageSnapshot, одинаково читаемый hit resolver и PaperDoll.
5. Missing ParameterContract либо undeclared required Dissonance source semantics остаются `blocked_calibration`; явно объявленное `none` допустимо.
6. Deployed assembly refuses refit, pattern change and interface switch.
