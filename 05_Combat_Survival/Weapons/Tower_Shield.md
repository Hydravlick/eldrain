---
type: weapon_frame
status: active
system: combat_survival
frame_id: tower_shield
display_name: Ростовой щит
weapon_family: shield
frame_vector: kinetics
vector_scope: commitment
activates_on:
  - covered_advance
  - brace
  - lower_recovery
primary_window_function: mitigate
creates_window:
  - covered_advance
implicit_keyword: full_cover
exploits_window:
  - none
mitigates_window:
  - ranged_line
exposure_channels:
  - flank
  - weight
  - low_mobility
  - hazard_hold
frame_power: 4
exposure_weight: 5
mastery_unlock:
  - braced_angle_shift
mvp_verdict: specialist
mvp_reason: Проверяет покрытое продвижение и фланги, но легко создаёт скучный щитовой оптимум.
sort_order: 620
tags:
  - weapon_frame
  - weapons
  - shield
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Ростовой щит

Ростовой щит создаёт покрытое продвижение и закрывает линию, но платит весом, флангами, низкой мобильностью и плохим удержанием опасной среды.

## Варианты

### Ростовой Щит (Tower Shield) [1H]
[variant_id:: tower_shield]
[tier:: 1]
[weight:: 15kg]
[guard_input:: Hold]
[guard_mechanic:: raise_cover -> covered_advance -> lower_recovery]

Дверь от сейфа или машины.

- **Мувсет:** поднятое положение позволяет медленно продвигаться под прикрытием; опускание щита для атаки открывает долгую фазу recovery.
- **Implicit:** `full_cover` двигает команду через линию, но не защищает от обхода.
- **Слабость:** сильно режет скорость и делает обход фланга главным наказанием.

### Стеновой Бункер (Wall Bunker) [1H]
[variant_id:: wall_bunker]
[tier:: 2]
[weight:: 20kg]
[guard_input:: Hold]
[guard_mechanic:: brace_lock -> full_immunity (no_advance)]

Более грубая и тяжёлая плита, рассчитанная не на продвижение, а на удержание точки.

- **Мувсет:** полностью статичная стойка без фазы продвижения — щит либо полностью поднят и неуязвим спереди, либо полностью опущен.
- **Implicit:** `full_cover` здесь абсолютен спереди, пока щит поднят, но не даёт никакого covered_advance.
- **Слабость:** ещё тяжелее и медленнее Ростового Щита; полная неподвижность делает обход фланга почти гарантированным при любой задержке.
- **Отличие:** даёт полную фронтальную неуязвимость вместо частичного прикрытия на ходу, но полностью жертвует мобильностью Ростового Щита.
