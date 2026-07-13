---
type: registry
status: active
system: world_generation_registry
registry_type: environment_states
tags: [database, environment, anomaly, local_states, traces]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_StatusEffects|Registry Status Effects]]"
  - "[[08_World_Generation/Anomaly/Anomaly_System|Anomaly System]]"
  - "[[08_World_Generation/_Registries/Registry_Anomaly_Mutations|Registry Anomaly Mutations]]"
  - "[[08_World_Generation/Content/World_Atlas/Sectors/Port/01_Foreign_Water_Mutation_Lines|Чужая вода: линии мутаций Порта]]"
---
# Реестр: локальные средовые состояния

> **Среда — третий игрок рейда.** Она не раздаёт универсальные дебаффы и не участвует в таблице элементальных реакций. Она перестраивает конкретную сцену: что видно, где можно укрыться, какой маршрут стал шумным, кого заметит местная система и сколько времени стоит задержка.

## Как игрок читает среду

Средовое состояние начинается не с иконки, а с понятной сцены:

| Шаг | Что происходит для игрока |
|---|---|
| **Замечает** | Слышит, видит или телом ощущает телеграф: звон воды, белую волну, шорох спор по фильтру. |
| **Понимает** | Может назвать местное правило: Белый ответ увидит след; открытый маршрут под дождём плох; быстрый выход теперь закрыт. |
| **Выбирает** | Меняет маршрут, тратит местный ресурс, пользуется укрытием, переносит риск на другую цель или принимает обязательство. |
| **Вкладывается** | Теряет время, шумит, остаётся на виду, расходует фильтр или отказывается от удобного пути. |
| **Получает ответ** | Мир меняет ровно объявленную часть сцены: приходит конечный ответ, открывается префаб, сужается безопасный маршрут. |
| **Живёт с последствием** | Успех открывает ход; ошибка меняет следующую сцену. Это не скрытый числовой штраф. |

Среда может быть смертельно опасной, но опасность должна быть причинной: игрок видит, какое правило сработало, и способен ответить действием, а не только снять новый значок состояния.

## Контракт записи

```markdown
[state_id:: template_environment_state]
[state_family:: recognition_trace | local_material | local_signal]
[state_scope:: instance]
[world_owner:: anomaly_family_or_dungeon_id]
[host:: pawn | mob | route | prefab | device]
[applies_to:: target_kind]
[pre_tell:: visible_or_audible_cue]
[scene_axis:: route | information | tempo | shelter | local_response | device_access]
[player_choice:: local_action_or_route]
[recognition_owner:: local_system_id]
[consequence_mode:: redirect_response | deny_quick_exit | reveal | permit | deny | attract | exposure_pressure]
[counter_or_refusal:: local_action_or_route]
[termination:: leave | clear_trace | transfer | resolve_source | phase_end]
[contact_amplifier:: none | active_bleed]
[status_aftermath:: none | effect_id]
[purge_class:: none]
```

Один инстанс обязан иметь один главный `scene_axis` и одно игроко-читаемое последствие. Общая форма записи может повторяться в других мирах, но `world_owner`, распознающий субъект, выбор игрока и путь отказа всегда принадлежат конкретной среде. `status_aftermath` допустим лишь после объявленного контакта со средой; он не заменяет сцену и не является её основным содержанием. `contact_amplifier` ускоряет только уже начавшийся контакт с этой средой и никогда не создаёт его сам.

## Пример сцены: споровый дождь

Споровый дождь — не заклинание площади и не генератор «стаков». Он звучит по металлу, оседает на стекле маски и меняет ценность открытых крыш, навесов, фильтра и скорости маршрута. Игрок может переждать под укрытием, быстро пройти открытый участок, потратить ресурс фильтра или сменить путь.

### Споровый дождь Порта
[state_id:: port_spore_rain]
[state_family:: local_material]
[state_scope:: instance]
[world_owner:: port_sowing_T3]
[host:: route | prefab]
[applies_to:: exposed_traveler]
[pre_tell:: familiar_scent, settling_spores, filter_hiss]
[scene_axis:: route]
[player_choice:: covered_route | leave_exposure | filter | seal_wound]
[recognition_owner:: port_sowing_weather]
[consequence_mode:: exposure_pressure]
[counter_or_refusal:: covered_route | leave_exposure | filter | seal_wound | decontaminate]
[termination:: leave | phase_end]
[contact_amplifier:: active_bleed]
[status_aftermath:: spore_growth]
[purge_class:: none]

Дождь сначала создаёт контакт: незащищённое дыхание или открытая рана остаются в споровой среде. `active_bleed` ускоряет этот контакт только через заражённую рану; сама рана не создаёт спор и не позволяет атакующему наложить `spore_growth` вне дождя. Фильтр отвечает за дыхание, герметизация раны — за её путь, укрытие и выход из зоны разрывают контакт целиком, а очистка работает уже после него.

Это делает bleed значимым условием Порта, но не обязательным билдом: дождь публичен, его телеграф видят обе стороны, а выигрыш от ранения исчезает, если цель закроет рану или сменит сцену. В прототипе нужно отдельно проверить, не начинают ли игроки брать bleed во все портовые комплекты; если да, ускорение остаётся только у уже накопленного средового контакта, а не у первого попадания в дождь.

## Семейство: распознаваемый след

`recognition_trace` означает: локальная среда получила читаемое основание узнать цель и применить собственное правило. Это одно семейство грамматики, а не один общий эффект.

| Состояние | Владелец | Что распознаёт среда | Последствие | Путь отказа |
|---|---|---|---|---|
| `white_trace` | Белый ответ Порта | цель для конечного местного ответа | перенаправляемая погоня или открытие подготовленного префаба | очистить или перенести след, разорвать контакт, уйти в сухой карман |
| `mark_of_greed` | обязательство подземелья | Пешку, принявшую риск глубины | запрет быстрых выходов | завершить источник либо пережить Phase Shift в обязательстве |

### Белый след
[state_id:: white_trace]
[state_family:: recognition_trace]
[state_scope:: instance]
[world_owner:: foreign_water_white_response]
[host:: pawn | mob]
[applies_to:: signal_trap_target]
[pre_tell:: water_chime, withdrawing_condensation, white_wave]
[scene_axis:: local_response]
[player_choice:: clear_trace | transfer_trace | break_contact | dry_pocket]
[recognition_owner:: finite_local_response]
[consequence_mode:: redirect_response]
[counter_or_refusal:: clear_trace | transfer_trace | break_contact | dry_pocket]
[termination:: clear_trace | transfer | phase_end]
[contact_amplifier:: none]
[status_aftermath:: none]
[purge_class:: none]

Белый след не даёт Белому ответу всезнание: он лишь создаёт локальную линию распознавания. Игрок может очистить след, перенаправить ответ на другую подходящую цель либо использовать открытый префаб до прихода конечного резерва.

### Метка глубины
[state_id:: mark_of_greed]
[state_family:: recognition_trace]
[state_scope:: instance]
[world_owner:: dungeon_commitment]
[host:: pawn]
[applies_to:: dungeon_entrant]
[pre_tell:: dungeon_entry_commitment]
[scene_axis:: route]
[player_choice:: resolve_source | outlast_phase_shift]
[recognition_owner:: dungeon_exit_rule]
[consequence_mode:: deny_quick_exit]
[counter_or_refusal:: resolve_source | outlast_phase_shift]
[termination:: resolve_source | phase_end]
[contact_amplifier:: none]
[status_aftermath:: none]
[purge_class:: none]

Метка глубины не является наказанием за нажатие кнопки и не лечится purge. Она объявляет, что Пешка приняла обязательство опасного подземелья: быстрый выход закрыт, пока не завершён источник Метки либо не пережит следующий Phase Shift внутри обязательства.
