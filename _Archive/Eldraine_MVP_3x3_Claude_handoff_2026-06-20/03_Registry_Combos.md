---
type: registry
status: active
system: player_entities_registry
registry_type: combos
tags: [database, builds, proficiency, mvp]
related_files:
  - "[[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]]"
  - "[[04_Player_Entities/_Registries/Registry_Races|Registry Races]]"
  - "[[04_Player_Entities/_Registries/Registry_Specs|Registry Specs]]"
  - "[[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile Pipeline]]"
---
# Реестр: ячейки Race × Spec

> Реестр содержит девять проектных слотов MVP. Старые curated-комбинации выведены из канона: они не образовывали целостную матрицу и смешивали черновые способности с утверждёнными правилами.
>
> Главный фильтр проектирования: [[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]].

## Зафиксированная матрица

| | Авангард `assault` | Технократ `support` | Странник `scout` |
|---|---|---|---|
| Ёж `hedgehog` | `hedgehog_assault` | `hedgehog_support` | `hedgehog_scout` |
| Крыса `rat` | `rat_assault` | `rat_support` | `rat_scout` |
| Белка `squirrel` | `squirrel_assault` | `squirrel_support` | `squirrel_scout` |

Жаба, Ящерица, Страж и Догмат остаются expansion-направлениями. Для них не создаются фиктивные готовые комбо до отдельного прохода.

## Контракт записи

Завершённая ячейка хранит:

```markdown
[id:: template_combo]
[req_race:: template_race]
[req_spec:: template_spec]
[design_status:: approved]
[creates_window:: route_open, concealment]
[exploits_window:: blind, distraction]
[mitigates_window:: trap_pressure]
[creates_state:: none]
[exploits_state:: low_visibility]
[position_role:: route_control]
[resource_pressure:: tools, bolts]
[thrives_on:: confined_space, low_visibility]
[mitigates:: traps]
[preferred_targets:: stationary_lurker, support_core]
[bad_matchups:: detection, open_sightline, swarm]
[route_affinity:: confined_space, alternate_route]
[solo_gaps:: armor, sustained_pressure]
[condition_bonus:: ...]
[tradeoff:: ...]
[arsenal_type:: blade] | [prof:: 2]
[armor_axis:: stealth] | [prof:: 2]
```

После полей идут фантазия, повторяемый цикл, смешанные `P/Q/E`, 2–4 доктрины, результаты успеха/отхода/провала и заметки прототипа.

`design_status:: pending` означает, что слот существует, но способности, арсенал и доктрины не являются каноном.

---

## Ёж × Авангард

[id:: hedgehog_assault]
[req_race:: hedgehog]
[req_spec:: assault]
[design_status:: pending]
[base_weakness:: hazard]

Проектный слот. Не наследует автоматически старого «Джаггернаута», стационарную турель или «Сенсорную Броню».

---

## Ёж × Технократ

[id:: hedgehog_support]
[req_race:: hedgehog]
[req_spec:: support]
[design_status:: pending]
[base_weakness:: shadow]

Проектный слот. Сила должна рождаться из смешения телесной массы и инженерной методологии, а не из универсальной роли танка.

---

## Ёж × Странник

[id:: hedgehog_scout]
[req_race:: hedgehog]
[req_spec:: scout]
[design_status:: pending]
[base_weakness:: hazard]

Проектный слот. Мобильность Странника не обязана означать рывок; допустимы маршрутизация, контролируемый перенос массы и подготовленное изменение позиции.

---

## Крыса × Авангард

[id:: rat_assault]
[req_race:: rat]
[req_spec:: assault]
[design_status:: pending]
[base_weakness:: kinetics]

Проектный слот. Третий хват и техническая биология должны менять способ ведения оружейного давления, а не давать бесплатную скорость действий.

---

## Крыса × Технократ

[id:: rat_support]
[req_race:: rat]
[req_spec:: support]
[design_status:: pending]
[base_weakness:: shadow, kinetics, detection]
[ability_model:: mono_vector_fusion]

Проектный слот. Совпадение `tech + tech` усиливает глубину технического исполнения, но не выдаёт бесплатный второй вектор.

---

## Крыса × Странник

[id:: rat_scout]
[req_race:: rat]
[req_spec:: scout]
[design_status:: pending]
[base_weakness:: detection]

Проектный слот. Должен работать через маршрут, инструмент и чтение пространства, не превращаясь в обязательный пик для закрытых локаций.

---

## Белка × Авангард

[id:: squirrel_assault]
[req_race:: squirrel]
[req_spec:: assault]
[design_status:: foundation_approved]
[base_weakness:: tech]

### Утверждённая пассивная основа: «Инерционный заряд»

- заряд возникает от **значимого импульса движения**, а не от пройденных метров;
- источники: разгон, смена траектории, контролируемое приземление, смена высоты, выход из давления, перенос оружейной отдачи телом;
- повтор одного безопасного движения даёт убывающую отдачу;
- накопленный импульс готовит тяжёлое действие Авангарда, а не даёт постоянный DPS или бесплатное ускорение;
- точные пороги, расход заряда, оружейные связи и `Q/E` не утверждены.

Предложение «низкий заряд = высокая точность, нагрев = низкая точность, заряженный выстрел» остаётся примером возможного чтения, а не главным или каноническим решением.

---

## Белка × Технократ

[id:: squirrel_support]
[req_race:: squirrel]
[req_spec:: support]
[design_status:: pending]
[base_weakness:: shadow]

Проектный слот. Перегрузка — сильное направление фантазии, но требует цены, телеграфа и восстановления; не должна производить бесплатные батареи или бесконечное питание устройств.

---

## Белка × Странник

[id:: squirrel_scout]
[req_race:: squirrel]
[req_spec:: scout]
[design_status:: pending]
[base_weakness:: ballistics]

Проектный слот. Это наиболее мобильная методология матрицы, но мобильность должна жить в теле и маршруте; способности остаются медленными, ситуативными и уязвимыми.
