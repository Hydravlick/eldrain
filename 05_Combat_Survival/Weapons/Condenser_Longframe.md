---
type: weapon_frame
status: active
system: combat_survival
frame_id: condenser_longframe
display_name: Конденсаторный длинник
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on:
  - aim_hold
  - charge
  - shot_recovery
primary_window_function: create
creates_window:
  - weakspot_open
exploits_window:
  - exposed_weakspot
mitigates_window:
  - none
exposure_channels:
  - open_line
  - flank
  - charge_interrupt
  - heat
frame_power: 4
exposure_weight: 4
mastery_unlock:
  - stable_charge_cancel
mvp_verdict: stretch_core
mvp_reason: Сильный магопанк-сигнал, но для первого MVP опасен снайперским уклоном и безопасной дистанцией.
sort_order: 420
tags:
  - weapon_frame
  - weapons
  - arcanegun
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
---
# Конденсаторный длинник

Конденсаторный длинник выигрывает время на удержании линии. Пока заряд стабилизируется, игрок видимо выставляется под фланг, прерывание и Heat.

## Варианты

### Конденсаторный Длинник (Condenser Longframe) [2H]
[variant_id:: condenser_longframe]
[tier:: 2]
[weight:: 4.5kg] | [dmg:: 75]
[impulse_cost:: 1]
[charge_time:: 0.8s]
[heat:: 45]
[bloom:: medium]
[dissonance_pulse:: 6]
[implicit:: shield_breaker]
[implicit_rule:: стабильный удержанный заряд раскрывает щит или weakspot; сбитый заряд превращается в Heat и потерянный темп]
[input_pattern:: tap: range check -> hold: stabilize charge -> release: shield break]
[combo_reset:: потеря линии или пауза после Recovery возвращает цикл к range check]

Дальний фрейм с удержанием заряда. Силен, если игрок успел стабилизировать импульс.

- **Implicit:** `shield_breaker` награждает позицию и удержание линии, а не быстрый повторный огонь.
- **Слабость:** плох под давлением; сбитый заряд уходит в Heat и Dissonance.
