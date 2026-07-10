---
type: weapon_frame
status: active
system: combat_survival
frame_id: harpoon_driver
display_name: Гарпунный драйвер
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on:
  - aim_hold
  - tether_shot
  - miss_recovery
primary_window_function: create
creates_window:
  - tether_control
implicit_keyword: tether
exploits_window:
  - none
mitigates_window:
  - escape_route
exposure_channels:
  - miss_recovery
  - weight
  - open_line
  - reload_timing
frame_power: 4
exposure_weight: 4
mastery_unlock:
  - tether_recover
mvp_verdict: core_support
mvp_reason: Очень сеттинговый фрейм контроля, но лучше как второй MVP после ручного разрядника.
sort_order: 440
tags:
  - weapon_frame
  - weapons
  - arcanegun
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
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
[fire_input:: Hold (Windup)]
[reload_mechanic:: Single-load]

Катушка разгоняет гарпун с тросом. Главная ценность — фиксация, а не урон.

- **Мувсет:** линия прицеливания, натяжение катушки, затем выстрел тросом с фиксацией цели.
- **Implicit:** `tether` создаёт командное окно, но не заменяет убийство.
- **Слабость:** промах оставляет игрока с тяжёлым фреймом и потерянным темпом.

### Споровый Разбрызгиватель (Spore Slinger) [2H]
[variant_id:: spore_slinger]
[tier:: 2]
[weight:: 5.0kg] | [dmg:: 15]
[impulse_cost:: 1]
[charge_time:: 0.9s]
[heat:: 25]
[bloom:: medium]
[dissonance_pulse:: 4]
[fire_input:: Hold (Windup)]
[reload_mechanic:: Break-action]

Альтернативный заряд для того же драйвера: вместо троса на одну цель — медленный снаряд, создающий зону.

- **Мувсет:** снаряд летит по дуге и создаёт зону, замедляющую Windup и Recovery всех анимаций внутри неё, а не фиксирует одну цель тросом.
- **Implicit:** `tether` здесь работает как командный контроль зоны, а не привязка конкретного противника.
- **Слабость:** низкая дальность и дуговая траектория делают заряд применимым почти исключительно для удержания дверных проёмов и лестниц.
- **Отличие:** контролирует площадь, а не одну цель, и не оставляет разрыв троса как единую точку провала, но заметно слабее по прямому урону и почти бесполезен на открытой дистанции.
