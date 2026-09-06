---
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
  - "[[04_Player_Entities/Registries/Registry_Combos|Registry_Combos]]"
  - "[[06_Economy_Loot/Loot_Distribution|Loot_Distribution]]"
type: registry
index_route: owner
index_group: combat_survival
index_order: 20
index_summary: "Хранит схему и записи: Реестр оружейных фреймов."
read_when: Когда нужен контракт «Реестр оружейных фреймов» и его границы с соседними владельцами.
---
# Реестр оружейных фреймов

> Frame задаёт хват, локальные фазы действия, `commitment`, `exposure_channels`, постоянное поведение (`implicit`) и неснимаемый долг. Экземпляр задаёт moveset или поведение выпуска, происхождение, диапазон редкости и контекст появления. Полный authored полевой профиль владеет допуском к Frame и `prof`, а не именами предметов.

## Контракт доступа

См. [[04_Player_Entities/Proficiency_Arsenal#Контракт доступа]].

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
WHERE entity_kind = "weapon_frame"
SORT sort_order ASC
```

## Краткая роль фреймов

| Канал | Фреймы | Зачем существует |
|:---|:---|:---|
| Ближний | `short_cut_1h`, `point_tool_1h`, `compact_impact_1h` | использовать мягкую зону, линию стыка или создать короткий срыв в тесноте |
| Ближний | `breach_impact_2h`, `reach_line_2h`, `hook_reach_2h` | изменить путь, удержать внешний радиус или сместить край защиты |
| Дальний | `pulse_tool_1h`, `condenser_rig_2h`, `scatter_valve_2h`, `needle_thrower_2h` | по-разному доставить поражение на линии, в конусе или в открытую мягкую зону |

## Лут и Tier Аномалии

См. [[06_Economy_Loot/Loot_Distribution#Лут и Tier Аномалии]].

## Проверка

Проверка контракта реестра должна сверять активные ID Frame, хват, локальные фазы действия, `commitment`, `exposure_channels`, данные экземпляров, authored BaseFrameProf и личный MasteryContribution. Отдельная проверка подтверждает, что биография не меняет механику, каждый Frame-mastery tag касается одного Frame и имеет строгий XOR между `mastery_step:: 1` и named sidegrade-expression, итог не превышает `3`, expression не даёт скрытого шага, а физический запрет не обходится. Числа урона, Heat, точные задержки и веса остаются предметом прототипа, а не скрытого Power Score. Трос, заслон и аномальная процедура являются устройствами навыков и не входят в активный список Frame.
