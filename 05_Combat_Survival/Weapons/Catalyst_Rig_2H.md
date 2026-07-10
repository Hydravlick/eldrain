---
type: weapon_frame
status: active
system: combat_survival
frame_id: catalyst_rig_2h
display_name: Катализаторная рама, две руки
weapon_family: catalyst
grip: two_hand
frame_vector: aether
vector_scope: commitment
activates_on: [prepare, channel, release, backlash_recovery]
primary_window_function: create
creates_window: [reality_exposed]
implicit_keyword: reality_assay
implicit_rule: Рама удерживает аномальную защиту в измеримом контуре и открывает её для ответа, но требует подготовленного источника, линии и уязвимого канала.
exploits_window: [none]
mitigates_window: [anomalous_immunity]
exposure_channels: [backlash, dissonance_pulse, interrupt, living_target_tempo]
mastery_unlock: [safe_break, assay_hold]
sort_order: 510
tags: [weapon_frame, ranged, catalyst, two_hand]
related_files:
  - "[[05_Combat_Survival/Weapon_Ranged|Weapon_Ranged]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Катализаторная рама, две руки

Это не посох и не отдельный класс. Катализаторная рама - специализированный прибор для аномального окна; против живой цели её медленный канал остаётся плохим ответом.

## Экземпляры

### Рама памяти осадка [2H]
[instance_id:: memory_assay_rig]
[load_tier:: 2]
[rarity_band:: rare..epic]
[origin_kind:: local_sector]
[origin_function:: измерение нестабильной памяти воды и материалов]
[spawn_profile:: anomaly_research_cache]
[moveset_profile:: Set Probe -> Hold Assay -> Release Burn]
[commitment_cost:: прерванный канал возвращает часть нагрузки в руки и показывает высокий Pulse]
[handedness:: two_hand]
[energy_mode:: prepared_charge]
[emission_profile:: held reality assay]
[cadence_gate:: backlash_clear]
[impulse_cost:: 1]
[cast_input:: Hold to Channel -> Release]
[draw_mechanic:: prepared Reality Charge]

Рама открывает конкретную аномальную защиту для всей команды, но не производит бесплатную батарею и не ускоряет обычную стрельбу.

### Калибратор якорной трещины [2H]
[instance_id:: anchor_calibration_rig]
[load_tier:: 3]
[rarity_band:: epic..artifact]
[origin_kind:: city_frontier]
[origin_function:: проверка аварийного контура перед стабилизацией]
[spawn_profile:: embedded_anomaly_node]
[moveset_profile:: Ground Frame -> Long Channel -> Locked Release]
[commitment_cost:: редкий контур выдерживает глубину, но требует неподвижной точки и привлекает ответ Аномалии]
[handedness:: two_hand]
[energy_mode:: prepared_charge]
[emission_profile:: anchored reality assay]
[cadence_gate:: anchor_cooldown]
[impulse_cost:: 2]
[cast_input:: Hold to Channel -> Release]
[draw_mechanic:: prepared Reality Charge]

Это редкий профессиональный прибор, не универсальное «сильное магическое оружие»: он меняет одну аномальную задачу ценой позиции и заметности.
