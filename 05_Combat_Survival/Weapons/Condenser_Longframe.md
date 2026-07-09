---
type: weapon_frame
status: active
system: combat_survival
frame_id: condenser_longframe
display_name: Конденсаторный длинник
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on: [aim_hold, charge, shot_recovery]
primary_window_function: create
creates_window: [weakspot_open]
exploits_window: [exposed_weakspot]
mitigates_window: [none]
exposure_channels: [open_line, flank, charge_interrupt, heat]
frame_power: 4
exposure_weight: 4
implicit_keyword: shield_breaker
implicit_rule: "Стабильный удержанный заряд раскрывает щит или weakspot; сбитый заряд превращается в Heat и потерянный темп."
mastery_unlock: [stable_charge_cancel]
mvp_verdict: stretch_core
mvp_reason: "Сильный магопанк-сигнал, но для первого MVP опасен снайперским уклоном и безопасной дистанцией."
sort_order: 420
tags: [weapon_frame, weapons, arcanegun]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
---
# Конденсаторный длинник

Конденсаторный длинник выигрывает время на удержании линии. Пока заряд стабилизируется, игрок видимо выставляется под фланг, прерывание и Heat.

## Варианты

### Конденсаторный Длинник (Condenser Longframe) [2H]
[variant_id:: condenser_longframe] | [tier:: 2] | [weight:: 4.5kg] | [dmg:: 75] | [impulse_cost:: 1] | [charge_time:: 0.8s] | [heat:: 45] | [bloom:: medium] | [dissonance_pulse:: 6] | [setting_status:: prototype]
[fire_input:: Hold: stabilize charge / Release: shield break] | [reload_mechanic:: capacitor rack]
[combo_reset:: потеря линии или пауза после Recovery возвращает цикл к range check]

*Дальний фрейм с удержанием заряда. Силен, если игрок успел стабилизировать импульс.*
- **Отличие:** главный образ дальнего заряда, но не стартовый якорь MVP.
- **Implicit:** `shield_breaker` награждает позицию и удержание линии, а не быстрый повторный огонь.
- **Слабость:** плох под давлением; сбитый заряд уходит в Heat и Dissonance.

### Смотровой длинник (Survey Longframe) [2H]
[variant_id:: survey_longframe] | [tier:: 1] | [weight:: 3.8kg] | [dmg:: 58] | [impulse_cost:: 1] | [charge_time:: 1.1s] | [heat:: 50] | [bloom:: medium] | [dissonance_pulse:: 5] | [setting_status:: prototype]
[fire_input:: Hold: slow sight / Release: survey shot] | [reload_mechanic:: exposed coil swap]
[combo_reset:: flinch или шаг из стойки возвращает цикл к slow sight]

*Переделанный измерительный контур, который стреляет медленно и честно.*
- **Отличие:** дешевле и хуже держит давление, зато хорошо показывает цену линии.
- **Implicit:** `shield_breaker` требует долгого aim_hold.
- **Слабость:** любой прессинг ломает цикл.

### Палатный стабилизатор (Chamber Longframe) [2H]
[variant_id:: chamber_longframe] | [tier:: 2] | [weight:: 5.2kg] | [dmg:: 68] | [impulse_cost:: 1] | [charge_time:: 0.6s] | [heat:: 38] | [bloom:: low] | [dissonance_pulse:: 7] | [setting_status:: prototype]
[fire_input:: Hold: braced line / Release: clean puncture] | [reload_mechanic:: sealed condenser]
[combo_reset:: vent cycle возвращает цикл к braced line]

*Более стабильная гильдейская сборка для команды, которая может защитить стрелка.*
- **Отличие:** ниже риск сбитого заряда, выше цена и след.
- **Implicit:** `shield_breaker` становится повторяемее, но не безопаснее.
- **Слабость:** делает носителя заметной целью и просит прикрытия.
