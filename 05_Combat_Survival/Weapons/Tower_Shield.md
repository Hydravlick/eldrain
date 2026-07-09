---
type: weapon_frame
status: active
system: combat_survival
frame_id: tower_shield
display_name: Ростовой щит
weapon_family: shield
frame_vector: kinetics
vector_scope: commitment
activates_on: [covered_advance, brace, lower_recovery]
primary_window_function: mitigate
creates_window: [covered_advance]
exploits_window: [none]
mitigates_window: [ranged_line]
exposure_channels: [flank, weight, low_mobility, hazard_hold]
frame_power: 4
exposure_weight: 5
implicit_keyword: full_cover
implicit_rule: "Braced advance закрывает фронтальную линию, пока игрок платит весом, флангами и плохой реакцией на опасную среду."
mastery_unlock: [braced_angle_shift]
mvp_verdict: specialist
mvp_reason: "Проверяет покрытое продвижение и фланги, но легко создаёт скучный щитовой оптимум."
sort_order: 620
tags: [weapon_frame, weapons, shield]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Ростовой щит

Ростовой щит создаёт покрытое продвижение и закрывает линию, но платит весом, флангами, низкой мобильностью и плохим удержанием опасной среды.

## Варианты

### Ростовой Щит (Tower Shield) [1H]
[variant_id:: tower_shield] | [tier:: 1] | [weight:: 15kg] | [setting_status:: mvp]
[guard_input:: Hold Brace / Tap Lower] | [guard_mechanic:: full_cover -> lower_recovery]
[combo_reset:: после lower_recovery следующий цикл снова начинается с raise cover]

*Дверь от сейфа или машины.*
- **Отличие:** базовый тест полной линии укрытия и фланговой цены.
- **Implicit:** `full_cover` двигает команду через линию, но не защищает от обхода.
- **Слабость:** сильно режет скорость и делает фланг главным наказанием.

### Дозорная дверь (Watch Door) [1H]
[variant_id:: watch_door] | [tier:: 1] | [weight:: 11kg] | [setting_status:: prototype]
[guard_input:: Hold Cover / Tap Set Foot] | [guard_mechanic:: partial_cover -> brace_lock]
[combo_reset:: снятие brace_lock возвращает цикл к Hold Cover]

*Облегчённая дверь-щит для удержания коридора, а не открытого поля.*
- **Отличие:** легче переносится, но хуже закрывает ноги и фланг.
- **Implicit:** `full_cover` становится частичным и требует правильного коридора.
- **Слабость:** не прощает открытую площадку и обход.

### Переборочный щит (Bulkhead Shield) [1H]
[variant_id:: bulkhead_shield] | [tier:: 2] | [weight:: 18kg] | [setting_status:: prototype]
[guard_input:: Hold Anchor / Tap Angle Shift] | [guard_mechanic:: full_cover -> braced_angle_shift]
[combo_reset:: Angle Shift требует полного brace перед новым продвижением]

*Тяжёлая переборка с рукоятями, рассчитанная на командное продвижение.*
- **Отличие:** лучше переживает дальнюю линию, но почти убивает мобильность.
- **Implicit:** `full_cover` покупает командное окно ценой носителя.
- **Слабость:** опасная среда, фланг и вес быстро превращают защиту в ловушку.
