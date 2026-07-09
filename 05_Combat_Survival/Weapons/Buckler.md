---
type: weapon_frame
status: active
system: combat_survival
frame_id: buckler
display_name: Малый парирующий щит
weapon_family: shield
frame_vector: kinetics
vector_scope: commitment
activates_on:
  - parry_window
  - block_recovery
primary_window_function: mitigate
creates_window:
  - parry_stagger
exploits_window:
  - none
mitigates_window:
  - melee_entry
exposure_channels:
  - mistimed_block
  - ranged_line
  - close_commit
frame_power: 2
exposure_weight: 2
mastery_unlock:
  - parry_reset
mvp_verdict: core_pair
mvp_reason: Хорошая пара к handcannon/ножу для чтения commitment, но сам по себе слишком жанровый.
sort_order: 610
tags:
  - weapon_frame
  - weapons
  - shield
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Малый парирующий щит

Малый щит живёт на точном окне парирования. Он снижает цену ближнего входа, но ошибка открывает руку, корпус и линию выстрела.

## Варианты

### Баклер (Buckler) [1H]
[variant_id:: buckler]
[tier:: 1]
[weight:: 1.0kg]
[implicit:: tight_parry]
[implicit_rule:: точный block в parry_window создаёт parry_stagger; ранний или поздний блок открывает руку и линию]
[input_pattern:: tap: cover twitch -> hold: parry catch -> recovery: guard return]
[combo_reset:: после block_recovery следующий блок снова начинается с cover twitch]

Маленький кулачный щит.

- **Implicit:** `tight_parry` снижает цену входа только при точном чтении удара.
- **Слабость:** окно блока очень маленькое; ошибка оставляет руку и корпус открытыми.
