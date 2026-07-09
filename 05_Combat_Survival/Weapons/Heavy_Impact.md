---
type: weapon_frame
status: active
system: combat_survival
frame_id: heavy_impact
display_name: Тяжёлый ударник
weapon_family: blunt
frame_vector: kinetics
vector_scope: commitment
activates_on: [windup, impact, heavy_recovery]
primary_window_function: create
creates_window: [guard_break]
exploits_window: [none]
mitigates_window: [none]
exposure_channels: [windup_interrupt, dodge_punish, noise, weight]
frame_power: 4
exposure_weight: 5
implicit_keyword: breach
implicit_rule: "Полный windup создаёт guard_break по стойке, двери или пластине; неполный контакт даёт только stagger."
mastery_unlock: [committed_retarget]
mvp_verdict: specialist
mvp_reason: "Силен как тест веса, дверей и guard break, но риск универсального пролома слишком высок для главного MVP."
sort_order: 210
tags: [weapon_frame, weapons, blunt]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Тяжёлый ударник

Тяжёлый ударник обещает пролом, но просит игрока заранее принять долгий замах и дорогой recovery. Это не универсальная кинетика, а моментная ставка телом и весом.

## Варианты

### Кувалда (Sledgehammer) [2H]
[variant_id:: sledgehammer] | [tier:: 1] | [weight:: 8kg] | [dmg:: 55] | [setting_status:: mvp]
[combo_chain:: short slam -> overhead breach -> recovery shove] | [alt_action:: door check]
[combo_reset:: пауза после Recovery возвращает цепочку к short slam]

*Инструмент, превращённый в оружие. Медленный и неотвратимый.*
- **Отличие:** базовый тест пролома, дверей и наказуемого замаха.
- **Implicit:** `breach` покупается телеграфом и тяжёлым recovery.
- **Слабость:** долгий замах делает промах дорогим.

### Заклёпочный молот (Rivet Maul) [2H]
[variant_id:: rivet_maul] | [tier:: 1] | [weight:: 6.5kg] | [dmg:: 48] | [setting_status:: prototype]
[combo_chain:: side bump -> rivet drop -> brace recover] | [alt_action:: plate dent]
[combo_reset:: если цель вышла из guard_break, цепочка возвращается к side bump]

*Молот с короткой тяжёлой головой для работы по креплениям и пластинам.*
- **Отличие:** меньше урон, но быстрее возвращает стойку после контакта с бронёй.
- **Implicit:** `breach` лучше раскрывает крепления и щиты, чем мягкое тело.
- **Слабость:** всё ещё требует прямого входа и места для замаха.

### Карьерный клин-молот (Quarry Wedge) [2H]
[variant_id:: quarry_wedge] | [tier:: 2] | [weight:: 9kg] | [dmg:: 62] | [setting_status:: prototype]
[combo_chain:: set feet -> wedge crash -> stuck pull] | [alt_action:: anchor stance]
[combo_reset:: застревание в материале сбрасывает цикл к set feet]

*Осадный инструмент, которым проще расколоть проход, чем догнать живую цель.*
- **Отличие:** сильнее по дверям, оболочкам и крупной стойке.
- **Implicit:** `breach` создаёт окно для команды, но не даёт бесплатного follow-up.
- **Слабость:** вес, шум и stuck pull делают его плохим ответом на мобильную цель.
