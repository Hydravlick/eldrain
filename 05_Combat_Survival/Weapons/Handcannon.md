---
type: weapon_frame
status: active
system: combat_survival
frame_id: handcannon
display_name: Ручной разрядник
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on: [aim_snap, shot, shot_recovery]
primary_window_function: create
creates_window: [stagger_entry]
exploits_window: [none]
mitigates_window: [none]
exposure_channels: [open_line, noise, heat, reload_timing]
frame_power: 3
exposure_weight: 3
mastery_unlock: [recoil_recover]
mvp_verdict: anchor
mvp_reason: "Главный MVP: один импульс сразу проверяет батарею, Heat, Pulse, шум, stagger, Recovery и нужду в добивании."
sort_order: 410
tags: [weapon_frame, weapons, arcanegun]
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
---
# Ручной разрядник

Ручной разрядник создаёт короткое дальнее давление и `stagger_entry`, но открывает стрелка шумом, линией выстрела, Heat и моментом перезарядки.

## Варианты

### Ручной Разрядник (Spark Handcannon) [1H]
[variant_id:: spark_handcannon]
[tier:: 1]
[weight:: 1.8kg] | [dmg:: 45]
[impulse_cost:: 1]
[heat:: 35]
[bloom:: high]
[dissonance_pulse:: 4]
[implicit:: stopping_pulse]
[implicit_rule:: короткий тяжёлый импульс сбивает вход, спринт или каст, но после выстрела стрелок платит шумом, Heat и recovery]
[input_pattern:: tap: aim snap -> hold: braced pulse -> recovery: vent and reload]
[combo_reset:: после shot_recovery следующий выстрел снова начинается с aim snap]

Грубый одноручный магострел: короткая дистанция, сильный удар, плохая дисциплина разряда.

- **Implicit:** `stopping_pulse` создаёт окно, но редко закрывает бой без добивания.
- **Слабость:** при стрельбе на бегу bloom резко растёт.
