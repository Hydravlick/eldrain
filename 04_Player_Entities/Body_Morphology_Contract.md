---
type: system
status: active
index_route: owner
index_group: player_entities
index_order: 80
index_summary: "Задаёт правила и последствия системы «Контракт морфологии тела»."
read_when: "Читайте при изменении входов, состояний, стоимости или последствий системы «Контракт морфологии тела»."
system: body_morphology
tags: [body, morphology, fit, ownership, thermos]
related_files:
  - "[[04_Player_Entities/Shell_Construction|Shell Construction]]"
  - "[[07_Gear_Inventory/Thermos_Assembly|Thermos Assembly]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces|Thermos Interfaces]]"
---
# Контракт морфологии тела

> Тело сообщает, чем оно физически является. Снаряжение решает, можно ли подогнать конкретную вещь, но не переписывает тело ради собственной законности.

## 1. Владелец

`BODY_MORPHOLOGY` единолично публикует версионированный `MorphologySnapshot` конкретной Пешки. Snapshot описывает только устойчивую геометрию и физические интерфейсы тела, необходимые внешним системам.

```yaml
MorphologySnapshot:
  pawn_id: PawnID
  morphology_revision: Revision
  morphology_envelope_id: MorphologyEnvelopeID
  body_regions: [BodyRegionID]
  mount_interface_classes: [MountInterfaceClass]
  permanent_constraints: [ConstraintID]
  source_refs: [BodySourceRef]
```

Snapshot не содержит:

- `BaseServiceCapacity`, P/Q/E, proficiency или Personal Tags;
- слоты, nodes, coverage или эффекты Термоса;
- итог `compatible | refit_required | incompatible`;
- массу снаряжения, Dissonance, цену или редкость;
- оценку силы либо человеческой ценности.

## 2. Граница с Термосом

[[07_Gear_Inventory/Thermos_Assembly|Thermos Assembly Resolver]] читает одновременно:

1. `MorphologySnapshot@revision`;
2. `ThermosModelDefinition@revision`;
3. instance-level `FitRecord@fit_revision`.

Только Assembly Resolver публикует один из трёх результатов:

```text
compatible
refit_required
incompatible
```

Подгонка создаёт либо заменяет `FitRecord` конкретного экземпляра Термоса. Она не меняет `MorphologySnapshot`, Race, hero-kit, Personal Tags, Chronicle, P/Q/E или `BaseServiceCapacity`.

## 3. Изменение тела

Новая `morphology_revision` допустима только после отдельно разрешённого постоянного изменения тела у профильного владельца процедуры. Термос, модуль, временный статус, травма рейда или preview мастера не могут сами повысить revision.

После изменения:

- старые assembly drafts становятся stale;
- уже существующие сборки не получают молчаливую совместимость;
- мастер обязан получить новый Fit Quote;
- несовместимый предмет остаётся физическим предметом и может быть передан, продан либо перенастроен, но не Deploy-ится как легальная сборка.

## 4. Инварианты

1. Один `PawnID × morphology_revision` даёт один immutable Snapshot.
2. Morphology не вычисляется из внешности карточки, Civic Attire или установленного предмета.
3. Fit не даёт телу новые mount interfaces и не удаляет permanent constraints.
4. Ошибка или отсутствие body owner даёт `MISSING_MORPHOLOGY_SNAPSHOT`, а не универсальную совместимость.
5. Ни один downstream-потребитель не пишет обратно в `BODY_MORPHOLOGY`.
