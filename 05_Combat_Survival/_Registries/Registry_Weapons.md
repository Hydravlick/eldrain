---
type: registry
status: active
system: combat_survival_registry
registry_type: weapon_frames
tags:
  - weapons
  - frames
  - instances
  - arsenal
related_files:
  - "[[05_Combat_Survival/Weapon_Manifesto|Weapon_Manifesto]]"
  - "[[04_Player_Entities/Combat_Profile_Pipeline|Combat_Profile_Pipeline]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[04_Player_Entities/_Registries/Registry_Combos|Registry_Combos]]"
  - "[[06_Economy_Loot/Loot_Distribution|Loot_Distribution]]"
---
# Реестр оружейных фреймов

> Frame задаёт хват, локальные фазы действия, `commitment`, `exposure_channels`, постоянное поведение (`implicit`) и неснимаемый долг. Экземпляр задаёт moveset или поведение выпуска, происхождение, диапазон редкости и контекст появления. Полный authored hero-kit владеет допуском к Frame и `prof`, а не именами предметов.

## Контракт доступа

```text
AllowedFrames(hero_kit_id) = Registry_Combos[hero_kit_id].weapon_frame
FrameProf(hero_kit_id, frame_id) = Registry_Combos[hero_kit_id].prof
EligibleInstance = authored Frame + matching grip + load tier + rarity band + spawn profile
```

- `Registry_Combos` хранит законченный authored-перечень `[weapon_frame:: ...] | [prof:: ...] | [combat_role:: ...]` каждого hero-kit `Race × Spec`; списки родителей не складываются формулой.
- Chronicle, Origin trait, редкость Пешки и история использования не добавляют и не блокируют Frame, не сдвигают `prof` и не меняют gunfeel двух Пешек одного hero-kit.
- Экземпляр не может менять `grip`, `activates_on`, `commitment`, `exposure_channels`, `implicit_keyword` или основную функцию окна своего Frame.
- `load_tier` говорит о допустимой энергетической нагрузке; `rarity_band` говорит, в каких цветах может существовать Pattern. Это разные оси.

## Контракт экземпляра

Каждый блок `###` на странице фрейма содержит:

```markdown
[instance_id:: stable_id]
[load_tier:: 1]
[rarity_band:: rusty..rare]
[origin_kind:: local_sector | city_frontier | foreign_snapshot]
[origin_function:: зачем предмет существовал]
[spawn_profile:: где генератор имеет право его положить]
[moveset_profile:: телесная последовательность или выпуск]
[commitment_cost:: какой долг остаётся]
[handedness:: one_hand | two_hand]
```

Дальний экземпляр дополнительно хранит `[energy_mode]`, `[emission_profile]`, `[cadence_gate]` и цену импульса, если пользуется батарейным резервом. Аксессуар хранит `[guard_input]` и `[guard_mechanic]`.

## Фреймы

```dataview
TABLE WITHOUT ID
  file.link AS "Фрейм",
  grip AS "Хват",
  weapon_family AS "Семейство",
  implicit_keyword AS "Поведение",
  primary_window_function AS "Работа",
  join(activates_on, ", ") AS "Фазы действия",
  commitment AS "Обязательство",
  join(creates_window, ", ") AS "Создаёт",
  join(exploits_window, ", ") AS "Использует",
  join(exposure_channels, ", ") AS "Цена"
FROM "05_Combat_Survival/Weapons"
WHERE type = "weapon_frame"
SORT sort_order ASC
```

## Краткая роль фреймов

| Канал | Фреймы | Зачем существует |
|:---|:---|:---|
| Ближний | `short_cut_1h`, `point_tool_1h`, `compact_impact_1h` | использовать мягкую зону, линию стыка или создать короткий срыв в тесноте |
| Ближний | `breach_impact_2h`, `reach_line_2h`, `hook_reach_2h` | изменить путь, удержать внешний радиус или сместить край защиты |
| Дальний | `pulse_tool_1h`, `condenser_rig_2h`, `scatter_valve_2h`, `needle_thrower_2h` | по-разному доставить поражение на линии, в конусе или в открытую мягкую зону |

## Лут и Tier Аномалии

`anomaly_phase` не повышает качество всего лута. Генератор сначала выбирает источник мира, POI и фазовое состояние, затем Pattern из его `spawn_profile` и допустимую `rarity_band`.

- T1 держит цельную местную базу и городской след.
- T2 открывает профильные комнаты, владельцев, Trace и рабочие запасы катастрофы.
- T3 разрешает редкий `stitched_trace` из другого слепка только в читаемом сшитом POI; Common-база сектора остаётся.

Иностранный серый предмет может быть редок в Порту по вероятности появления, не становясь Rare по качеству. Редкий местный Pattern не обязан ждать T3.

## Проверка

Проверка контракта реестра должна сверять активные ID Frame, хват, локальные фазы, `commitment`, `exposure_channels`, данные экземпляров и authored arsenal/prof hero-kit. Отдельная проверка подтверждает, что Chronicle не меняет Frame, gunfeel или `prof`. Числа урона, Heat, точные задержки и веса остаются предметом прототипа, а не скрытого Power Score. Трос, заслон и аномальная процедура являются устройствами навыков и не входят в активный список Frame.
