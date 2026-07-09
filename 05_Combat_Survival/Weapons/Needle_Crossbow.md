---
type: weapon_frame
status: active
system: combat_survival
frame_id: needle_crossbow
display_name: Игольный дальнобой
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on: [wind, aim_hold, bolt_recovery]
primary_window_function: exploit
creates_window: [none]
exploits_window: [soft_zone_exposed, concealment]
mitigates_window: [none]
exposure_channels: [slow_wind, armor_check, low_stagger]
frame_power: 2
exposure_weight: 2
implicit_keyword: puncture
implicit_rule: "Тихий болт лучше добирает мягкую зону из укрытия; по тяжёлой пластине почти не создаёт stagger."
mastery_unlock: [quiet_rewind]
mvp_verdict: specialist
mvp_reason: "Нужен как тихий T1 Specialist, но главный MVP без батареи плохо показывает магипанк."
sort_order: 450
tags: [weapon_frame, weapons, arcanegun]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Игольный дальнобой

Игольный дальнобой даёт тихий exploit по мягким зонам и укрытию. Он не даёт сильный stagger и легко проваливается против тяжёлой пластины.

## Варианты

### Игольный Арбалет (Needle Crossbow) [2H]
[variant_id:: needle_crossbow] | [tier:: 1] | [power_source:: mechanical] | [weight:: 2.4kg] | [dmg:: 35] | [heat:: 0] | [bloom:: low] | [dissonance_pulse:: 0] | [setting_status:: mvp]
[fire_input:: Hold: aim settle / Release: quiet shot] | [reload_mechanic:: wind bolt]
[combo_reset:: после bolt_recovery следующий выстрел снова требует wind bolt]

*Механический дальнобойный фрейм без батареи. Тихий, но медленный.*
- **Отличие:** базовый тихий ответ без батарейной цены.
- **Implicit:** `puncture` делает арбалет нишей тишины, а не дешёвым магострелом.
- **Слабость:** долгий взвод, слабый stagger, плохая работа против тяжёлых пластин.

### Сточный игольник (Gutter Bolter) [2H]
[variant_id:: gutter_bolter] | [tier:: 1] | [power_source:: mechanical] | [weight:: 1.9kg] | [dmg:: 28] | [heat:: 0] | [bloom:: medium] | [dissonance_pulse:: 0] | [setting_status:: prototype]
[fire_input:: Tap: snap bolt / Hold: settle bolt] | [reload_mechanic:: hand crank]
[combo_reset:: ручной crank возвращает цикл к snap bolt]

*Лёгкий болтомёт для маршрутов, где шум хуже слабого урона.*
- **Отличие:** легче и быстрее достаётся, но хуже пробивает даже мягкую броню.
- **Implicit:** `puncture` требует раскрытой цели.
- **Слабость:** почти не создаёт окно самостоятельно.

### Гильдейский бесшумный ворот (Silent Windlass) [2H]
[variant_id:: silent_windlass] | [tier:: 2] | [power_source:: mechanical] | [weight:: 3.0kg] | [dmg:: 38] | [heat:: 0] | [bloom:: low] | [dissonance_pulse:: 0] | [setting_status:: prototype]
[fire_input:: Hold: breath settle / Release: needle drop] | [reload_mechanic:: geared windlass]
[combo_reset:: geared windlass требует полной перезарядки перед новым aim_hold]

*Дорогой механический дальнобой для тихой команды.*
- **Отличие:** покупает надёжную тишину и повторяемость, не повышая магическую силу.
- **Implicit:** `puncture` лучше добирает уже открытую мягкую зону.
- **Слабость:** дорогой для своей узкой роли и слаб против тяжёлых целей.
