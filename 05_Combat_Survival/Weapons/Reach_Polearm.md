---
type: weapon_frame
status: active
system: combat_survival
frame_id: reach_polearm
display_name: Дистанционная древка
weapon_family: polearm
frame_vector: kinetics
vector_scope: commitment
activates_on:
  - brace
  - poke
  - swing_recovery
primary_window_function: create
creates_window:
  - distance_control
implicit_keyword: sweet_spot
exploits_window:
  - none
mitigates_window:
  - melee_entry
exposure_channels:
  - dead_zone
  - flank
  - whiff_recovery
  - weight
frame_power: 4
exposure_weight: 4
mastery_unlock:
  - sweet_spot_recover
mvp_verdict: support
mvp_reason: Нужен для проверки reach и геометрии, но главный MVP не должен быть обычной алебардой.
sort_order: 310
tags:
  - weapon_frame
  - weapons
  - polearm
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Дистанционная древка

Дистанционная древка создаёт контроль входа и наказывает прямую попытку сблизиться. Её моментная экспозиция появляется, когда цель проходит в мёртвую зону или обходит угол удара.

## Варианты

### Алебарда (Halberd) [2H]
[variant_id:: halberd]
[tier:: 1]
[weight:: 5.5kg] | [dmg:: 45]
[sweet_spot_range:: 1.7-2.4m]
[heat:: 0] | [dissonance_pulse:: 0]
[combo_chain:: Brace Poke -> Haft Push -> Brace Poke]
[alt_action:: Head Sweep]
[combo_reset:: пауза после Ready возвращает цепочку к Brace Poke]

Топор на длинной палке с шипом. Active Frames по оси Z держатся экстремально долго.

- **Мувсет:** длинный прямой выпад, фиксирующий дистанцию; короткий тычок древком от себя наносит всего 1 урон, но отталкивает врага и сбивает ему Windup, освобождая место для повторного выпада.
- **Implicit:** `sweet_spot` читается дистанцией и контактом головы, а не скрытым множителем.
- **Слабость:** мёртвая зона в упор — если враг прошёл остриё, оружие теряет до 80% урона; обход сбоку ломает дистанционный контроль.

### Дозорное Копьё (Sentry Pike) [2H]
[variant_id:: sentry_pike]
[tier:: 1]
[weight:: 3.6kg] | [dmg:: 30]
[sweet_spot_range:: 1.2-1.9m]
[heat:: 0] | [dissonance_pulse:: 0]
[combo_chain:: Brace Poke -> Brace Poke]
[alt_action:: None]
[combo_reset:: пауза после Ready возвращает цепочку к Brace Poke]

Облегчённое древко без топорного навершия: только прямой укол, без рубящей фазы.

- **Мувсет:** два одинаковых быстрых укола подряд, без отдельного alt-действия и без рубящего свинга Алебарды.
- **Implicit:** `sweet_spot` срабатывает раньше по дистанции (ближе к цели), но с меньшим окном подтверждения контакта.
- **Слабость:** ниже урон и короче эффективная дистанция, чем у Алебарды; полностью зависит от повторного укола, поскольку нет альтернативного действия.
- **Отличие:** легче почти в полтора раза и быстрее возвращается в стойку, чем Алебарда, но заметно слабее в уроне и держит меньшую дистанцию.
