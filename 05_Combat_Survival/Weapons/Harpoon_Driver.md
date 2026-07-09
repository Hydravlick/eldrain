---
type: weapon_frame
status: active
system: combat_survival
frame_id: harpoon_driver
display_name: Гарпунный драйвер
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on: [aim_hold, tether_shot, miss_recovery]
primary_window_function: create
creates_window: [tether_control]
exploits_window: [none]
mitigates_window: [escape_route]
exposure_channels: [miss_recovery, weight, open_line, reload_timing]
frame_power: 4
exposure_weight: 4
mastery_unlock: [tether_recover]
mvp_verdict: core_support
mvp_reason: "Очень сеттинговый фрейм контроля, но лучше как второй MVP после ручного разрядника."
sort_order: 440
tags: [weapon_frame, weapons, arcanegun]
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
---
# Гарпунный драйвер

Гарпунный драйвер создаёт `tether_control`, но каждый промах оставляет игрока с тяжёлым фреймом, открытой линией и потерянным темпом.

## Варианты

### Гарпунный Драйвер (Harpoon Driver) [2H]
[variant_id:: harpoon_driver]
[tier:: 2]
[weight:: 6.0kg] | [dmg:: 40]
[impulse_cost:: 1]
[charge_time:: 0.7s]
[heat:: 30]
[bloom:: low]
[dissonance_pulse:: 5]
[implicit:: tether]
[implicit_rule:: попадание создаёт tether_control до разрыва линии, сброса троса или добивания; промах забирает темп]
[input_pattern:: tap: line aim -> hold: coil tension -> release: tether shot]
[combo_reset:: после miss_recovery или разрыва троса цикл возвращается к line aim]

Катушка разгоняет гарпун с тросом. Главная ценность — фиксация, а не урон.

- **Implicit:** `tether` создаёт командное окно, но не заменяет убийство.
- **Слабость:** промах оставляет игрока с тяжёлым фреймом и потерянным темпом.
