---
type: weapon_frame
status: active
system: combat_survival
frame_id: harpoon_driver
display_name: Гарпунный драйвер
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on: [aim_hold, tether_shot, miss_recovery]
primary_window_function: create
creates_window: [tether_control]
exploits_window: [none]
mitigates_window: [escape_route]
exposure_channels: [miss_recovery, weight, open_line, reload_timing]
frame_power: 4
exposure_weight: 4
implicit_keyword: tether
implicit_rule: "Попадание создаёт tether_control до разрыва линии, сброса троса или добивания; промах забирает темп."
mastery_unlock: [tether_recover]
mvp_verdict: core_support
mvp_reason: "Очень сеттинговый фрейм контроля, но лучше как второй MVP после ручного разрядника."
sort_order: 440
tags: [weapon_frame, weapons, arcanegun]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
---
# Гарпунный драйвер

Гарпунный драйвер создаёт `tether_control`, но каждый промах оставляет игрока с тяжёлым фреймом, открытой линией и потерянным темпом.

## Варианты

### Гарпунный Драйвер (Harpoon Driver) [2H]
[variant_id:: harpoon_driver] | [tier:: 2] | [weight:: 6.0kg] | [dmg:: 40] | [impulse_cost:: 1] | [charge_time:: 0.7s] | [heat:: 30] | [bloom:: low] | [dissonance_pulse:: 5] | [setting_status:: mvp]
[fire_input:: Hold: coil tension / Release: tether shot] | [reload_mechanic:: crank line reset]
[combo_reset:: после miss_recovery или разрыва троса цикл возвращается к line aim]

*Катушка разгоняет гарпун с тросом. Главная ценность — фиксация, а не урон.*
- **Отличие:** главный командный контроль цели.
- **Implicit:** `tether` создаёт командное окно, но не заменяет убийство.
- **Слабость:** промах оставляет игрока с тяжёлым фреймом и потерянным темпом.

### Портовый тросомёт (Dock Tether Gun) [2H]
[variant_id:: dock_tether_gun] | [tier:: 1] | [weight:: 4.8kg] | [dmg:: 28] | [impulse_cost:: 1] | [charge_time:: 0.9s] | [heat:: 35] | [bloom:: medium] | [dissonance_pulse:: 4] | [setting_status:: prototype]
[fire_input:: Hold: line aim / Release: hook shot] | [reload_mechanic:: manual spool]
[combo_reset:: ручная перемотка возвращает цикл к line aim]

*Грузовой инструмент, который держит цель хуже, но доступнее.*
- **Отличие:** дешевле и слабее, хорош для маршрута и объектов.
- **Implicit:** `tether` чаще замедляет, чем полностью фиксирует.
- **Слабость:** долгий manual spool после ошибки.

### Карьерный якорник (Quarry Anchor Driver) [2H]
[variant_id:: quarry_anchor_driver] | [tier:: 2] | [weight:: 7.2kg] | [dmg:: 46] | [impulse_cost:: 1] | [charge_time:: 0.8s] | [heat:: 34] | [bloom:: low] | [dissonance_pulse:: 6] | [setting_status:: prototype]
[fire_input:: Hold: anchor brace / Release: heavy tether] | [reload_mechanic:: locked spool]
[combo_reset:: locked spool требует полного Recovery перед новым aim_hold]

*Тяжёлый драйвер для крупных целей и вытаскивания из укрытия.*
- **Отличие:** сильнее держит крупную цель, но хуже переносится.
- **Implicit:** `tether` становится задачей команды: попасть, удержать, добить.
- **Слабость:** вес и открытая линия делают носителя очевидной целью.
