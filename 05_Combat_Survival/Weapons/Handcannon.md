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
implicit_keyword: stopping_pulse
implicit_rule: "Короткий тяжёлый импульс сбивает вход, спринт или каст, но после выстрела стрелок платит шумом, Heat и recovery."
mastery_unlock: [recoil_recover]
mvp_verdict: anchor
mvp_reason: "Главный MVP: один импульс сразу проверяет батарею, Heat, Pulse, шум, stagger, Recovery и нужду в добивании."
sort_order: 410
tags: [weapon_frame, weapons, arcanegun]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
---
# Ручной разрядник

Ручной разрядник создаёт короткое дальнее давление и `stagger_entry`, но открывает стрелка шумом, линией выстрела, Heat и моментом перезарядки.

## Варианты

### Ручной Разрядник (Spark Handcannon) [1H]
[variant_id:: spark_handcannon] | [tier:: 1] | [weight:: 1.8kg] | [dmg:: 45] | [impulse_cost:: 1] | [heat:: 35] | [bloom:: high] | [dissonance_pulse:: 4] | [setting_status:: mvp]
[fire_input:: Tap: aim snap / Hold: braced pulse] | [reload_mechanic:: break-action cell latch]
[combo_reset:: после shot_recovery следующий выстрел снова начинается с aim snap]

*Грубый одноручный магострел: короткая дистанция, сильный удар, плохая дисциплина разряда.*
- **Отличие:** главный MVP-экземпляр: один импульс создаёт окно, но не закрывает бой сам.
- **Implicit:** `stopping_pulse` сбивает вход и требует добивания.
- **Слабость:** при стрельбе на бегу bloom резко растёт.

### Трубный хлопок (Pipe Popper) [1H]
[variant_id:: pipe_popper] | [tier:: 1] | [weight:: 1.2kg] | [dmg:: 34] | [impulse_cost:: 1] | [heat:: 45] | [bloom:: very_high] | [dissonance_pulse:: 3] | [setting_status:: prototype]
[fire_input:: Tap: panic pop / Hold: unsafe brace] | [reload_mechanic:: loose cell shove]
[combo_reset:: перегрев или осечка возвращают цикл к panic pop]

*Дешёвый кустарный разрядник, который страшнее звучит, чем держит темп.*
- **Отличие:** дешевле и легче, но хуже повторяет сильное действие.
- **Implicit:** `stopping_pulse` остаётся, но требует почти идеального момента.
- **Слабость:** быстро перегревается и плохо переносит движение.

### Гильдейский щелкун (Guild Snapper) [1H]
[variant_id:: guild_snapper] | [tier:: 2] | [weight:: 2.0kg] | [dmg:: 48] | [impulse_cost:: 1] | [heat:: 28] | [bloom:: medium] | [dissonance_pulse:: 5] | [setting_status:: prototype]
[fire_input:: Tap: controlled snap / Hold: recoil-set pulse] | [reload_mechanic:: hinged capacitor gate]
[combo_reset:: после reload_timing цикл возвращается к controlled snap]

*Более чистый разрядник с нормальной защёлкой и предсказуемой отдачей.*
- **Отличие:** покупает повторяемость и стабильность, а не право убивать.
- **Implicit:** `stopping_pulse` надёжнее создаёт stagger_entry.
- **Слабость:** дороже потеря и выше диссонансная заметность.
