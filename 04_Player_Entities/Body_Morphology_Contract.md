---
status: active
system: body_morphology
tags:
  - body
  - morphology
  - fit
  - ownership
  - thermos
related_files:
  - "[[04_Player_Entities/Shell_Construction|Shell Construction]]"
  - "[[07_Gear_Inventory/Thermos_Assembly|Thermos Assembly]]"
  - "[[07_Gear_Inventory/Registries/Registry_Thermos_Interfaces|Thermos Interfaces]]"
type: system
index_route: owner
index_group: player_entities
index_order: 80
index_summary: "Определяет состояния, разрешение и связи: Контракт морфологии тела."
read_when: Когда нужен контракт «Контракт морфологии тела» и его границы с соседними владельцами.
---
# Контракт морфологии тела

Форма тела и его физические интерфейсы определяют, как можно посадить на Пешку конкретный Термос. Подгонка меняет посадку вещи; геометрия тела и его постоянные ограничения сохраняются.

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

Подгонка создаёт либо заменяет `FitRecord` конкретного экземпляра Термоса. Она не меняет `MorphologySnapshot`, Race, полевой профиль, Personal Tags, P/Q/E или `BaseServiceCapacity`.

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
