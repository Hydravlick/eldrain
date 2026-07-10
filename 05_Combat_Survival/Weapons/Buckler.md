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
implicit_keyword: tight_parry
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
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Малый парирующий щит

Малый щит живёт на точном окне парирования. Он снижает цену ближнего входа, но ошибка открывает руку, корпус и линию выстрела.

## Варианты

### Баклер (Buckler) [1H]
[variant_id:: buckler]
[tier:: 1]
[weight:: 1.0kg]
[guard_input:: Hold]
[guard_mechanic:: parry_window (0.2s) -> active_block]

Маленький кулачный щит.

- **Мувсет:** узкое зашитое временное окно (parry window) в момент начала анимации блока, переходящее в обычный active block.
- **Implicit:** `tight_parry` снижает цену входа только при точном чтении удара.
- **Слабость:** окно блока очень маленькое; ошибка оставляет руку и корпус открытыми.

### Шипастый Баклер (Spiked Buckler) [1H]
[variant_id:: spiked_buckler]
[tier:: 2]
[weight:: 1.6kg]
[guard_input:: Hold]
[guard_mechanic:: parry_window (0.35s) -> counter_thrust]

Тот же кулачный щит, но с вбитым в центр шипом для ответного удара.

- **Мувсет:** более широкое окно парирования, но вместо перехода в обычный active block точный блок сразу открывает короткий counter_thrust шипом.
- **Implicit:** `tight_parry` здесь конвертируется в урон, а не только в открытое окно для другого оружия.
- **Слабость:** тяжелее и медленнее поднимается; после counter_thrust щит на мгновение не может парировать повторно.
- **Отличие:** шире окно парирования и даёт собственный урон через контрудар, но за счёт веса и отсутствия обычного sustained block Баклера.
