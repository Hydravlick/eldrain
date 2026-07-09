---
type: weapon_frame
status: active
system: combat_survival
frame_id: tower_shield
display_name: Ростовой щит
weapon_family: shield
frame_vector: kinetics
vector_scope: commitment
activates_on: [covered_advance, brace, lower_recovery]
primary_window_function: mitigate
creates_window: [covered_advance]
exploits_window: [none]
mitigates_window: [ranged_line]
exposure_channels: [flank, weight, low_mobility, hazard_hold]
frame_power: 4
exposure_weight: 5
mastery_unlock: [braced_angle_shift]
mvp_verdict: specialist
mvp_reason: "Проверяет покрытое продвижение и фланги, но легко создаёт скучный щитовой оптимум."
sort_order: 620
tags: [weapon_frame, weapons, shield]
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Ростовой щит

Ростовой щит создаёт покрытое продвижение и закрывает линию, но платит весом, флангами, низкой мобильностью и плохим удержанием опасной среды.

## Варианты

### Ростовой Щит (Tower Shield) [1H]
[variant_id:: tower_shield]
[tier:: 1]
[weight:: 15kg]
[implicit:: full_cover]
[implicit_rule:: braced advance закрывает фронтальную линию, пока игрок платит весом, флангами и плохой реакцией на опасную среду]
[input_pattern:: tap: raise cover -> hold: covered step -> recovery: lower brace]
[combo_reset:: после lower_recovery следующий цикл снова начинается с raise cover]

Дверь от сейфа или машины.

- **Implicit:** `full_cover` двигает команду через линию, но не защищает от обхода.
- **Слабость:** сильно режет скорость и делает обход фланга главным наказанием.
