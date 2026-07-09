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
mastery_unlock: [committed_retarget]
mvp_verdict: specialist
mvp_reason: "Силен как тест веса, дверей и guard break, но риск универсального пролома слишком высок для главного MVP."
sort_order: 210
tags: [weapon_frame, weapons, blunt]
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Тяжёлый ударник

Тяжёлый ударник обещает пролом, но просит игрока заранее принять долгий замах и дорогой recovery. Это не универсальная кинетика, а моментная ставка телом и весом.

## Варианты

### Кувалда (Sledgehammer) [2H]
[variant_id:: sledgehammer]
[tier:: 1]
[weight:: 8kg] | [dmg:: 55]
[heat:: 0]
[dissonance_pulse:: 0]
[implicit:: breach]
[implicit_rule:: полный windup создаёт guard_break по стойке, двери или пластине; неполный контакт даёт только stagger]
[input_pattern:: tap: short slam -> hold: overhead breach -> hold: recovery shove]
[combo_reset:: пауза после Recovery возвращает цепочку к short slam]

Инструмент, превращённый в оружие. Медленный и неотвратимый.

- **Мувсет:** вертикальный удар пробивает блок, горизонтальный сбивает с ног.
- **Implicit:** `breach` покупается телеграфом и тяжёлым recovery.
- **Слабость:** долгий замах и тяжёлый recovery делают промах дорогим.
