---
type: weapon_frame
status: active
system: combat_survival
frame_id: catalyst_focus
display_name: Фокус реальности
weapon_family: catalyst
frame_vector: aether
vector_scope: commitment
activates_on:
  - charge
  - channel
  - backlash_recovery
primary_window_function: create
creates_window:
  - reality_exposed
exploits_window:
  - none
mitigates_window:
  - anomalous_immunity
exposure_channels:
  - backlash
  - dissonance_pulse
  - living_target_tempo
  - interrupt
frame_power: 4
exposure_weight: 5
mastery_unlock:
  - safer_channel_break
mvp_verdict: anomaly_specialist
mvp_reason: Самый уникальный аномальный инструмент, но слишком дорогой и контекстный для главного стартового MVP.
sort_order: 510
tags:
  - weapon_frame
  - weapons
  - catalyst
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
---
# Фокус реальности

Фокус реальности раскрывает аномальное тело, но делает пользователя заметным и наказуемым через backlash, Dissonance и прерывание канала.

## Варианты

### Фокус Реальности (Reality Focus) [2H]
[variant_id:: reality_focus]
[tier:: 2]
[weight:: 3.0kg] | [dmg:: 55]
[impulse_cost:: 1]
[charge_item:: reality_charge]
[charge_time:: 1.0s]
[heat:: 40]
[bloom:: medium]
[dissonance_pulse:: 8]
[implicit:: reality_burn]
[implicit_rule:: подготовленный заряд заставляет аномальное тело принять нормальный урон; против живой цели это дорогой и медленный импульс]
[input_pattern:: tap: anchor focus -> hold: channel reality -> release: burn pulse]
[combo_reset:: прерывание или backlash возвращает цикл к anchor focus]

Проводник, который заставляет аномальное тело принять нормальные законы.

- **Implicit:** `reality_burn` решает аномальную защиту, но громко зовёт ответ мира.
- **Расход:** тратит подготовленный `Reality Charge`, `Overcharge Cell` или стабилизатор. Не списывает сырой Рез из кошелька во время рейда.
- **Слабость:** высокий Dissonance, backlash без батареи, слабый темп против живых гуманоидов.
