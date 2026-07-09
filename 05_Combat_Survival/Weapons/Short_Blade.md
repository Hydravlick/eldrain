---
type: weapon_frame
status: active
system: combat_survival
frame_id: short_blade
display_name: Короткий клинок
weapon_family: blade
frame_vector: shadow
vector_scope: commitment
activates_on: [draw, lunge, backstab_recovery]
primary_window_function: exploit
creates_window: [none]
exploits_window: [back_exposed, stagger_entry]
mitigates_window: [none]
exposure_channels: [armor_check, front_exchange, close_commit]
frame_power: 2
exposure_weight: 2
mastery_unlock: [silent_draw, faster_recovery]
mvp_verdict: core_pair
mvp_reason: "Нужен как дешёвое добивание после окна, но сам по себе слишком похож на обычный RPG-нож."
sort_order: 110
tags: [weapon_frame, weapons, blade]
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Короткий клинок

Короткий клинок не делает Пешку `shadow`-архетипом. Он показывает, что в момент входа игрок выставился под броню, фронтальный обмен и риск застрять в клинче.

## Варианты

### Боевой нож (Combat Shiv) [1H]
[variant_id:: combat_shiv]
[tier:: 1]
[weight:: 0.5kg] | [dmg:: 15]
[heat:: 0]
[dissonance_pulse:: 0]
[implicit:: ambush]
[implicit_rule:: первый вход из спины, укрытия или чужого stagger получает короткий Recovery; фронтальный обмен не усиливается]
[input_pattern:: tap: quick jab -> hold: low lunge -> hold: close rip]
[combo_reset:: пауза после Ready возвращает цепочку к quick jab]

Короткий клинок для грязной работы в клинче.

- **Мувсет:** быстрые колющие удары с малым расходом стамины.
- **Implicit:** `ambush` делает нож добиванием окна, а не универсальным DPS.
- **Слабость:** почти не решает броню и честный фронтальный обмен.
