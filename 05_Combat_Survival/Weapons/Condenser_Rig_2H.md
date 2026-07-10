---
type: weapon_frame
status: active
system: combat_survival
frame_id: condenser_rig_2h
display_name: Конденсаторная рама, две руки
weapon_family: arcanegun
grip: two_hand
frame_vector: ballistics
vector_scope: commitment
activates_on: [aim_hold, charge, emission, charge_recovery]
primary_window_function: create
creates_window: [weakspot_open]
implicit_keyword: held_line
implicit_rule: Двуручный контур удерживает и стабилизирует сильный импульс по одной линии, но заранее показывает намерение и плохо переживает давление вблизи.
exploits_window: [none]
mitigates_window: [prepared_cast]
exposure_channels: [telegraph, open_line, heat, weight, interrupt]
mastery_unlock: [charge_recover, brace_hold]
sort_order: 420
tags: [weapon_frame, ranged, arcanegun, two_hand]
related_files:
  - "[[05_Combat_Survival/Weapon_Ranged|Weapon_Ranged]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Конденсаторная рама, две руки

Рама превращает занятое положение в сильный один импульс. Она не получает право стать лучшей винтовкой: телеграф, линия, Heat и потеря рук остаются видимыми.

## Экземпляры

### Линзовая рама обходчика [2H]
[instance_id:: survey_lens_rig]
[load_tier:: 2]
[rarity_band:: uncommon..rare]
[origin_kind:: local_sector]
[origin_function:: измерение устойчивости дальних опор и трещин]
[spawn_profile:: survey_station_cache]
[moveset_profile:: Brace -> Measured Charge -> Line Release]
[commitment_cost:: удержание линии фиксирует корпус и обнуляет попытку скрыться]
[handedness:: two_hand]
[energy_mode:: battery]
[emission_profile:: held precision impulse]
[cadence_gate:: condenser_cooldown]
[impulse_cost:: 1]
[fire_input:: Hold to Charge -> Release]
[reload_mechanic:: route new battery only when reserve is empty]

Обходчик видит слабую точку в конструкции и в бою требует той же дисциплины: хорошего угла и спокойного корпуса.

### Грозовой измеритель [2H]
[instance_id:: storm_measure_rig]
[load_tier:: 3]
[rarity_band:: rare..epic]
[origin_kind:: foreign_snapshot]
[origin_function:: фиксация атмосферных разрядов и опасных фронтов]
[spawn_profile:: stitched_trace]
[moveset_profile:: Ground Brace -> Long Charge -> Vent Release]
[commitment_cost:: после длинного выпуска рама требует вентиляции и запрещает быстрый перенос]
[handedness:: two_hand]
[energy_mode:: battery]
[emission_profile:: long held impulse]
[cadence_gate:: forced_vent]
[impulse_cost:: 2]
[fire_input:: Hold to Charge -> Release]
[reload_mechanic:: vent reserve before replacement]

Редкая рама может стабильно вести сильный импульс, но тратит два заряда и оставляет владельца в самом читаемом положении на карте.
