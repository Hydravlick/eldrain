---
type: skill_device_concept
status: deferred
system: player_entities
device_id: anomaly_procedure_rig
display_name: Рама аномальной процедуры
skill_type: anomaly_procedure
tags: [skill_device, anomaly, device, deferred]
related_files:
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
  - "[[04_Player_Entities/_Registries/Registry_Skill_Types|Registry_Skill_Types]]"
---
# Рама аномальной процедуры

> Этот материал больше не описывает оружейный фрейм. Вскрытие аномального правила — работа устройства навыка с явным источником, каналом, контр-окном и Backlash, а не дальняя атака.

Это не посох и не отдельный класс. Рама аномальной процедуры — специализированный прибор для аномального окна; конкретная Combo должна определить его `energy_contract:: device`, источник, цель процедуры, прерывание и последствие ошибки до активации в арсенале Пешки.

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
