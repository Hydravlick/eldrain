---
type: skill_device_concept
status: deferred
system: player_entities
device_id: tether_link
display_name: Тросовая связь
skill_type: mobility
tags: [skill_device, route, movement, deferred]
related_files:
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
  - "[[04_Player_Entities/_Registries/Registry_Skill_Types|Registry_Skill_Types]]"
---
# Тросовая связь

> Этот материал больше не описывает оружейный фрейм. Трос меняет маршрут, положение или спасение и поэтому принадлежит P/Q/E либо устройству навыка, а не арсеналу оружия.

Тросовая связь работает с одной линией, а не с зоной замедления. Её сила зависит от опоры, линии и того, переживёт ли пользователь собственное Commitment. Конкретная Combo должна назвать источник, энергетический контракт, контр-окно, Recovery и исход разрыва до возвращения идеи в активный контент.

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
