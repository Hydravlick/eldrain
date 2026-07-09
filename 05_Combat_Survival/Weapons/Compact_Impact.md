---
type: weapon_frame
status: active
system: combat_survival
frame_id: compact_impact
display_name: Компактный ударник
weapon_family: blunt
frame_vector: kinetics
vector_scope: commitment
activates_on: [swing, headshot_recovery]
primary_window_function: create
creates_window: [disorientation]
exploits_window: [none]
mitigates_window: [none]
exposure_channels: [close_commit, shield_angle]
frame_power: 2
exposure_weight: 2
implicit_keyword: concussion
implicit_rule: "Удар по голове, маске или жёсткой зоне создаёт короткую дезориентацию, если игрок вошёл в опасную дистанцию."
mastery_unlock: [concussion_followup]
mvp_verdict: core_pair
mvp_reason: "Хороший базовый инструмент ближнего контроля, но сеттингово почти не объясняет Элдрейн."
sort_order: 220
tags: [weapon_frame, weapons, blunt]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Компактный ударник

Компактный ударник создаёт короткое окно дезориентации вблизи. Он дешевле по обязательству, чем тяжёлый пролом, но просит войти в опасную дистанцию.

## Варианты

### Булава / Дубинка (Mace) [1H]
[variant_id:: mace] | [tier:: 1] | [weight:: 3.5kg] | [dmg:: 30] | [setting_status:: mvp]
[combo_chain:: body tap -> head swing -> shoulder check] | [alt_action:: hilt jam]
[combo_reset:: пауза после Ready возвращает цепочку к body tap]

*Компактный вес для короткого силового обмена.*
- **Отличие:** простая, дешёвая и читаемая дезориентация.
- **Implicit:** `concussion` открывает follow-up, но не держит дальний подход.
- **Слабость:** требует входа в опасную дистанцию и плохо догоняет отходящую цель.

### Сигнальная дубинка (Signal Baton) [1H]
[variant_id:: signal_baton] | [tier:: 1] | [weight:: 1.8kg] | [dmg:: 22] | [setting_status:: prototype]
[combo_chain:: wrist snap -> mask knock -> step through] | [alt_action:: lamp flash]
[combo_reset:: после lamp flash цепочка возвращается к wrist snap]

*Лёгкая дубинка с простым сигнальным узлом, не полноценный магострел.*
- **Отличие:** хуже по урону, но лучше как контроль в тесноте и проверка маски.
- **Implicit:** `concussion` читается ударом по голове или маске.
- **Слабость:** не решает броню и почти не работает через блок.

### Утяжелённый кастет (Weighted Knuckle) [1H]
[variant_id:: weighted_knuckle] | [tier:: 1] | [weight:: 0.9kg] | [dmg:: 18] | [setting_status:: prototype]
[combo_chain:: jab bump -> jaw hook -> clinch shove] | [alt_action:: grab assist]
[combo_reset:: разрыв клинча возвращает цепочку к jab bump]

*Инструмент для Пешек, которые хотят держать вторую руку свободной.*
- **Отличие:** самый мобильный вариант, но требует почти полного close_commit.
- **Implicit:** `concussion` появляется из точного контакта, а не из массы.
- **Слабость:** опасен против длинного оружия и щита.
