---
type: weapon_frame
status: active
system: combat_survival
frame_id: buckler
display_name: Малый парирующий щит
weapon_family: shield
frame_vector: kinetics
vector_scope: commitment
activates_on: [parry_window, block_recovery]
primary_window_function: mitigate
creates_window: [parry_stagger]
exploits_window: [none]
mitigates_window: [melee_entry]
exposure_channels: [mistimed_block, ranged_line, close_commit]
frame_power: 2
exposure_weight: 2
implicit_keyword: tight_parry
implicit_rule: "Точный block в parry_window создаёт parry_stagger; ранний или поздний блок открывает руку и линию."
mastery_unlock: [parry_reset]
mvp_verdict: core_pair
mvp_reason: "Хорошая пара к handcannon/ножу для чтения commitment, но сам по себе слишком жанровый."
sort_order: 610
tags: [weapon_frame, weapons, shield]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Малый парирующий щит

Малый щит живёт на точном окне парирования. Он снижает цену ближнего входа, но ошибка открывает руку, корпус и линию выстрела.

## Варианты

### Баклер (Buckler) [1H]
[variant_id:: buckler] | [tier:: 1] | [weight:: 1.0kg] | [setting_status:: mvp]
[guard_input:: Tap Parry / Hold Guard] | [guard_mechanic:: parry_window -> active_block]
[combo_reset:: после block_recovery следующий блок снова начинается с cover twitch]

*Маленький кулачный щит.*
- **Отличие:** самый чистый тест точного parry_window.
- **Implicit:** `tight_parry` снижает цену входа только при точном чтении удара.
- **Слабость:** окно блока очень маленькое; ошибка оставляет руку и корпус открытыми.

### Котельная крышка (Kettle Buckler) [1H]
[variant_id:: kettle_buckler] | [tier:: 1] | [weight:: 1.6kg] | [setting_status:: prototype]
[guard_input:: Hold Guard / Tap Bash] | [guard_mechanic:: noisy_block -> weak_parry]
[combo_reset:: после bash цепочка защиты возвращается к Hold Guard]

*Импровизированный щит из толстой крышки и ремня.*
- **Отличие:** легче простить ранний блок, но хуже даёт parry_stagger.
- **Implicit:** `tight_parry` почти отсутствует без точного чтения.
- **Слабость:** шумит и плохо закрывает линию выстрела.

### Шарнирный баклер (Hinged Buckler) [1H]
[variant_id:: hinged_buckler] | [tier:: 2] | [weight:: 1.3kg] | [setting_status:: prototype]
[guard_input:: Tap Parry / Hold Angle] | [guard_mechanic:: tight_parry -> angle_shift]
[combo_reset:: angle_shift возвращает следующий блок к Tap Parry]

*Гильдейский малый щит с шарнирной кромкой.*
- **Отличие:** лучше перестраивает угол после удачного парирования.
- **Implicit:** `tight_parry` становится инструментом входа, но не постоянной защитой.
- **Слабость:** дороже потеря и всё ещё слаб против дальнего давления.
