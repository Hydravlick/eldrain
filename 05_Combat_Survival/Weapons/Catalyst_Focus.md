---
type: weapon_frame
status: active
system: combat_survival
frame_id: catalyst_focus
display_name: Фокус реальности
weapon_family: catalyst
frame_vector: aether
vector_scope: commitment
activates_on: [charge, channel, backlash_recovery]
primary_window_function: create
creates_window: [reality_exposed]
exploits_window: [none]
mitigates_window: [anomalous_immunity]
exposure_channels: [backlash, dissonance_pulse, living_target_tempo, interrupt]
frame_power: 4
exposure_weight: 5
implicit_keyword: reality_burn
implicit_rule: "Подготовленный заряд заставляет аномальное тело принять нормальный урон; против живой цели это дорогой и медленный импульс."
mastery_unlock: [safer_channel_break]
mvp_verdict: anomaly_specialist
mvp_reason: "Самый уникальный аномальный инструмент, но слишком дорогой и контекстный для главного стартового MVP."
sort_order: 510
tags: [weapon_frame, weapons, catalyst]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
---
# Фокус реальности

Фокус реальности раскрывает аномальное тело, но делает пользователя заметным и наказуемым через backlash, Dissonance и прерывание канала.

## Варианты

### Фокус Реальности (Reality Focus) [2H]
[variant_id:: reality_focus] | [tier:: 2] | [weight:: 3.0kg] | [dmg:: 55] | [impulse_cost:: 1] | [charge_item:: reality_charge] | [charge_time:: 1.0s] | [heat:: 40] | [bloom:: medium] | [dissonance_pulse:: 8] | [setting_status:: prototype]
[cast_input:: Hold to Channel -> Release to Burn] | [draw_mechanic:: Reality Charge]
[combo_reset:: прерывание или backlash возвращает цикл к anchor focus]

*Проводник, который заставляет аномальное тело принять нормальные законы.*
- **Отличие:** базовый аномальный инструмент, не стартовый универсальный кастер.
- **Implicit:** `reality_burn` решает аномальную защиту, но громко зовёт ответ мира.
- **Расход:** тратит подготовленный `Reality Charge`, `Overcharge Cell` или стабилизатор.
- **Слабость:** высокий Dissonance, backlash без батареи, слабый темп против живых гуманоидов.

### Треснувший фокус (Cracked Focus) [2H]
[variant_id:: cracked_focus] | [tier:: 1] | [weight:: 2.4kg] | [dmg:: 38] | [impulse_cost:: 1] | [charge_item:: unstable_reality_charge] | [charge_time:: 1.2s] | [heat:: 55] | [bloom:: high] | [dissonance_pulse:: 9] | [setting_status:: prototype]
[cast_input:: Hold to Channel -> Risk Burn] | [draw_mechanic:: Unstable Charge]
[combo_reset:: любой interrupt возвращает цикл к anchor focus и создаёт backlash]

*Дешёвый фокус с плохой изоляцией, опасный даже при правильной подготовке.*
- **Отличие:** показывает, почему аномальный инструмент нельзя считать обычным оружием.
- **Implicit:** `reality_burn` срабатывает, но цена ошибки резко выше.
- **Слабость:** опасен для пользователя и плохо повторяется.

### Обетная линза (Votive Lens) [1H]
[variant_id:: votive_lens] | [tier:: 2] | [weight:: 1.6kg] | [dmg:: 30] | [impulse_cost:: 1] | [charge_item:: sanctified_charge] | [charge_time:: 0.9s] | [heat:: 35] | [bloom:: low] | [dissonance_pulse:: 10] | [setting_status:: TBD]
[cast_input:: Hold to Mark -> Release to Burn] | [draw_mechanic:: Ritual Charge]
[combo_reset:: потеря метки возвращает цикл к Hold to Mark]

*Слишком ритуальная версия фокуса; полезна как направление, но пока тянет систему в магический артефакт.*
- **Отличие:** потенциально сильная читаемость метки, но лорно требует отдельного прохода.
- **Implicit:** `reality_burn` здесь спорно выглядит как благословение, поэтому вариант скрыт из общих таблиц.
- **Слабость:** не готов к MVP без переработки языка и цены.
