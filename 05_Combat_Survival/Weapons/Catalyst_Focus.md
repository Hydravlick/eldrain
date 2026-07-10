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
implicit_keyword: reality_burn
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
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
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
[charge_time:: 1.0s]
[heat:: 40]
[bloom:: medium]
[dissonance_pulse:: 8]
[cast_input:: Hold to Channel -> Release to Burn]
[draw_mechanic:: Reality Charge]
[setting_status:: TBD]

Проводник, который заставляет аномальное тело принять нормальные законы.

- **Мувсет:** якорный фокус удерживается, канал стабилизируется, затем выброс сжигает аномальную защиту.
- **Implicit:** `reality_burn` решает аномальную защиту, но громко зовёт ответ мира.
- **Расход:** тратит подготовленный `Reality Charge` — заранее собранный стабилизатор. Не списывает сырой Рез из кошелька во время рейда.
- **Слабость:** высокий Dissonance, backlash без батареи, слабый темп против живых гуманоидов.

### Аномальный Стержень (Anomaly Rod) [2H]
[variant_id:: anomaly_rod]
[tier:: 3]
[weight:: 2.4kg] | [dmg:: 65]
[impulse_cost:: 0]
[charge_time:: 0.5s]
[heat:: 55]
[bloom:: high]
[dissonance_pulse:: 12]
[cast_input:: Hold to Channel -> Release to Burn]
[draw_mechanic:: Raw Aether]
[setting_status:: TBD]

Та же логика выброса, но без подготовленной батареи: стержень тянет Raw Aether прямо из окружения.

- **Мувсет:** тот же цикл удержания и выброса, но заметно короче время накопления заряда — расплата идёт через Dissonance, а не через время подготовки.
- **Implicit:** `reality_burn` срабатывает быстрее и без расходника, но каждый выброс ощутимо громче для мира.
- **Расход:** тянет `Raw Aether` напрямую, не требуя подготовленного `Reality Charge`; не подходит для тихого прохождения.
- **Слабость:** ещё выше Dissonance и Heat, чем у Фокуса Реальности; backlash при прерывании канала ощутимо опаснее.
- **Отличие:** быстрее заряжается и не требует расходника, но платит куда более высоким Dissonance и Heat, чем Фокус Реальности.
