---
type: weapon_frame
status: active
system: combat_survival
frame_id: needle_crossbow
display_name: Игольный дальнобой
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on:
  - wind
  - aim_hold
  - bolt_recovery
primary_window_function: exploit
creates_window:
  - none
implicit_keyword: puncture
exploits_window:
  - soft_zone_exposed
  - concealment
mitigates_window:
  - none
exposure_channels:
  - slow_wind
  - armor_check
  - low_stagger
frame_power: 2
exposure_weight: 2
mastery_unlock:
  - quiet_rewind
mvp_verdict: specialist
mvp_reason: Нужен как тихий T1 Specialist, но главный MVP без батареи плохо показывает магипанк.
sort_order: 450
tags:
  - weapon_frame
  - weapons
  - arcanegun
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Игольный дальнобой

Игольный дальнобой даёт тихий exploit по мягким зонам и укрытию. Он не даёт сильный stagger и легко проваливается против тяжёлой пластины.

## Варианты

### Игольный Арбалет (Needle Crossbow) [2H]
[variant_id:: needle_crossbow]
[tier:: 1]
[power_source:: mechanical]
[weight:: 2.4kg] | [dmg:: 35]
[impulse_cost:: 0]
[heat:: 0]
[bloom:: low]
[dissonance_pulse:: 0]
[fire_input:: Tap (Semi-Auto)]
[reload_mechanic:: Single-load]

Механический дальнобойный фрейм без батареи. Тихий, но медленный.

- **Мувсет:** бесшумный выстрел без трассеров, накладывающий стакующееся кровотечение на цель.
- **Implicit:** `puncture` делает арбалет нишей тишины, а не дешёвым магострелом без цены.
- **Слабость:** долгая анимация Recovery после каждого выстрела — стрелок замирает на месте, чтобы взвести механизм заново; слабый stagger и плохая работа против тяжёлых пластин.

### Скорострельный Игольник (Repeating Needler) [1H]
[variant_id:: repeating_needler]
[tier:: 2]
[power_source:: mechanical]
[weight:: 1.6kg] | [dmg:: 22]
[impulse_cost:: 0]
[heat:: 0]
[bloom:: medium]
[dissonance_pulse:: 0]
[fire_input:: Tap (Semi-Auto)]
[reload_mechanic:: Pump]

Облегчённый магазинный вариант того же механического дальнобоя: жертвует тишиной ради скорости.

- **Мувсет:** быстрая помповая перезарядка вместо полного взвода — заметно короче Recovery, но каждый болт оставляет видимый трассер и звук.
- **Implicit:** `puncture` срабатывает чаще за счёт скорострельности, но накопление кровотечения на удар слабее.
- **Слабость:** заметен на слух и по трассеру, теряя нишевое преимущество тишины; урон за выстрел ниже, чем у Арбалета.
- **Отличие:** быстрее перезаряжается и легче Арбалета, но теряет его главное преимущество — бесшумность.
