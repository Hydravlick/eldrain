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
implicit_keyword: shield_breaker
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
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
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
[fire_input:: Hold (Windup)]
[reload_mechanic:: Single-load]

Дальний фрейм с удержанием заряда. Силен, если игрок успел стабилизировать импульс.

- **Мувсет:** хитскан после стабилизации; калибровка линии вознаграждает удержание позиции, а не повторный огонь.
- **Implicit:** `shield_breaker` награждает позицию и удержание линии, а не быстрый повторный огонь.
- **Слабость:** плох под давлением; сбитый заряд уходит в Heat и Dissonance.

### Гравитационный Дальнобой (Gravity Lobber) [2H]
[variant_id:: gravity_lobber]
[tier:: 3]
[weight:: 7.5kg] | [dmg:: 90]
[impulse_cost:: 2]
[charge_time:: 0.5s]
[heat:: 55]
[bloom:: high]
[dissonance_pulse:: 7]
[fire_input:: Hold (Windup)]
[reload_mechanic:: Break-action]

Навесной снаряд вместо прямой линии: ломает двери и укрытия там, где Длинник только пробивает щели.

- **Мувсет:** снаряд летит по дуге и разрушает физическую геометрию укрытия при попадании — `shield_breaker` здесь буквально ломает щиты и стены, а не только магическую защиту.
- **Implicit:** `shield_breaker` конвертирован в разрушение окружения, а не только выставленного щита цели.
- **Слабость:** блокирует спринт после выстрела; анимация уборки оружия (quickswap) длится 1.2 секунды, в течение которых стрелок не может защищаться.
- **Отличие:** сильнее ломает укрытия и структуры, чем базовый Длинник, но гораздо тяжелее и после выстрела оставляет стрелка беззащитным дольше.
