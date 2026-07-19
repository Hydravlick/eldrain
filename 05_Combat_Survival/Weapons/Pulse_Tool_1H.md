---
type: weapon_frame
status: active
system: combat_survival
frame_id: pulse_tool_1h
display_name: Импульсный инструмент, одна рука
weapon_family: arcanegun
grip: one_hand
skill_interfaces: [conduit, impact_surface, free_hand]
activates_on: [aim_snap, emission, pulse_recovery]
commitment: exposed_line_until_hand_settle
primary_window_function: create
creates_window: [stagger_entry]
implicit_keyword: stopping_pulse
implicit_rule: Короткий направленный импульс сбивает готовность на линии, но раскрывает стрелка светом, звуком, Heat и восстановлением руки.
exploits_window: [none]
mitigates_window: [melee_entry]
exposure_channels: [noise, heat, open_line, reload_timing]
mastery_unlock: [pulse_recover, angle_settle]
sort_order: 410
tags: [weapon_frame, ranged, arcanegun, one_hand]
related_files:
  - "[[05_Combat_Survival/Weapon_Ranged|Weapon_Ranged]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Импульсный инструмент, одна рука

Это обычное оружие фронтира, не револьвер и не заклинание в рукояти. Его один импульс покупает разрыв чужого действия, но не делает следующий выстрел бесплатным.

## Экземпляры

### Пульсатор дозорной линии [1H]
[instance_id:: watchline_pulsator]
[load_tier:: 1]
[rarity_band:: rusty..rare]
[origin_kind:: city_frontier]
[origin_function:: защита караванной линии и сигнал остановки]
[spawn_profile:: civic_defense_cache]
[moveset_profile:: Aim Snap -> Stop Pulse -> Hand Settle]
[commitment_cost:: отдача и вспышка оставляют стрелка на линии до возврата руки]
[handedness:: one_hand]
[energy_mode:: battery]
[emission_profile:: single stopping pulse]
[cadence_gate:: recoil_settle]
[impulse_cost:: 1]
[fire_input:: Tap]
[reload_mechanic:: route new battery only when reserve is empty]

Грубый городской пульсатор уместен в любом фронтире: он существует для короткого сигнала опасности, а не для непрерывной стрельбы.

### Карантинный отметчик [1H]
[instance_id:: quarantine_marker]
[load_tier:: 1]
[rarity_band:: uncommon..rare]
[origin_kind:: local_sector]
[origin_function:: остановка заражённого прохода и подача видимого сигнала]
[spawn_profile:: quarantine_cabinet]
[moveset_profile:: Brace Sight -> Mark Pulse -> Forced Lower]
[commitment_cost:: яркая метка выдаёт угол раньше эффекта и требует опустить инструмент]
[handedness:: one_hand]
[energy_mode:: battery]
[emission_profile:: single marked pulse]
[cadence_gate:: sight_cooldown]
[impulse_cost:: 1]
[fire_input:: Hold to Brace -> Release]
[reload_mechanic:: route new battery only when reserve is empty]

Точная калибровка снижает ошибку линии, но не скрывает стрелка и не разрешает стрелять из нескольких углов одновременно.
