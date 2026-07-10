---
type: weapon_frame
status: active
system: combat_survival
frame_id: handcannon
display_name: Ручной разрядник
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on:
  - aim_snap
  - shot
  - shot_recovery
primary_window_function: create
creates_window:
  - stagger_entry
implicit_keyword: stopping_pulse
exploits_window:
  - none
mitigates_window:
  - none
exposure_channels:
  - open_line
  - noise
  - heat
  - reload_timing
frame_power: 3
exposure_weight: 3
mastery_unlock:
  - recoil_recover
mvp_verdict: anchor
mvp_reason: "Главный MVP: один импульс сразу проверяет батарею, Heat, Pulse, шум, stagger, Recovery и нужду в добивании."
sort_order: 410
tags:
  - weapon_frame
  - weapons
  - arcanegun
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
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
[fire_input:: Tap (Semi-Auto)]
[reload_mechanic:: Single-load]

Грубый одноручный магострел: короткая дистанция, сильный удар, плохая дисциплина разряда.

- **Мувсет:** быстрый aim snap и одиночный мощный импульс; ставка на стаггер здесь, а не на точность.
- **Implicit:** `stopping_pulse` создаёт окно, но редко закрывает бой без добивания.
- **Слабость:** при стрельбе на бегу bloom резко растёт.

### Линзовый Разрядник (Lens Emitter) [1H]
[variant_id:: lens_emitter]
[tier:: 2]
[weight:: 1.5kg] | [dmg:: 38]
[impulse_cost:: 1]
[heat:: 25]
[bloom:: low]
[dissonance_pulse:: 3]
[fire_input:: Hold (Windup)]
[reload_mechanic:: Single-load]

Прицельная версия разрядника: хитскан вместо грубого импульса, время калибровки сокращено до 0.5 секунды.

- **Мувсет:** во время калибровки разрешены медленные шаги в прицеле, но прыжок или спринт мгновенно сбрасывают фокус.
- **Implicit:** `stopping_pulse` здесь точнее по цели, но требует полной калибровки перед выстрелом, а не мгновенного aim snap.
- **Слабость:** линза даёт яркий блик до выстрела, выдавая позицию стрелка; попытка перестреливаться с нескольких сторон почти всегда заканчивается смертью.
- **Отличие:** ниже bloom и точнее базового Разрядника, но требует полной неподвижности при калибровке и выдаёт позицию до выстрела.
