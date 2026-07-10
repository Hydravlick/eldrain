---
type: weapon_frame
status: active
system: combat_survival
frame_id: tether_launcher_2h
display_name: Тросовый пускатель, две руки
weapon_family: arcanegun
grip: two_hand
frame_vector: ballistics
vector_scope: commitment
activates_on: [aim_hold, tether_launch, pull_hold, miss_recovery]
primary_window_function: create
creates_window: [tether_control]
implicit_keyword: anchored_tether
implicit_rule: Трос связывает цель или край маршрута с точкой пускателя, но промах, разрыв линии и тяжёлый возврат оставляют владельца без темпа.
exploits_window: [none]
mitigates_window: [escape_route]
exposure_channels: [weight, open_line, miss_recovery, reload_timing]
mastery_unlock: [tether_recover, anchor_shift]
sort_order: 440
tags: [weapon_frame, ranged, arcanegun, two_hand]
related_files:
  - "[[05_Combat_Survival/Weapon_Ranged|Weapon_Ranged]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Тросовый пускатель, две руки

Тросовый пускатель работает с одной связью, а не с зоной замедления. Его сила зависит от опоры, линии и того, переживёт ли игрок собственное попадание.

## Экземпляры

### Подъёмный возвращатель [2H]
[instance_id:: salvage_line_launcher]
[load_tier:: 2]
[rarity_band:: uncommon..rare]
[origin_kind:: local_sector]
[origin_function:: возвращение тяжёлого груза с нижнего мокрого уровня]
[spawn_profile:: lift_service_cache]
[moveset_profile:: Anchor Aim -> Cable Launch -> Winch Hold]
[commitment_cost:: пока лебёдка держит линию, обе руки и угол заняты грузом]
[handedness:: two_hand]
[energy_mode:: battery]
[emission_profile:: single anchor cable]
[cadence_gate:: winch_reset]
[impulse_cost:: 1]
[fire_input:: Hold to Aim -> Release Launch]
[reload_mechanic:: reset cable before routing a new battery]

В бою он вытягивает цель только при реальной линии и опоре. Промах не превращается в второй быстрый выстрел.

### Скальный страховщик [2H]
[instance_id:: cliff_rescue_launcher]
[load_tier:: 2]
[rarity_band:: rare..epic]
[origin_kind:: foreign_snapshot]
[origin_function:: фиксация спасательной линии на вертикальном маршруте]
[spawn_profile:: stitched_trace]
[moveset_profile:: High Anchor -> Tension Check -> Pull Hold]
[commitment_cost:: проверка натяжения телеграфирует позицию и не даёт быстро сменить цель]
[handedness:: two_hand]
[energy_mode:: battery]
[emission_profile:: tension-checked tether]
[cadence_gate:: tension_release]
[impulse_cost:: 1]
[fire_input:: Hold to Aim -> Release Launch]
[reload_mechanic:: release tether before routing a new battery]

Точная фиксация лучше переживает вертикаль, но цена не в уроне: владелец дольше остаётся привязан к выбранному углу.
