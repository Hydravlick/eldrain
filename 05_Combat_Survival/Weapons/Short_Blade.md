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
implicit_keyword: ambush
implicit_rule: "Первый вход из спины, укрытия или чужого stagger получает короткий Recovery; фронтальный обмен не усиливается."
mastery_unlock: [silent_draw, faster_recovery]
mvp_verdict: core_pair
mvp_reason: "Нужен как дешёвое добивание после окна, но сам по себе слишком похож на обычный RPG-нож."
sort_order: 110
tags: [weapon_frame, weapons, blade]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Короткий клинок

Короткий клинок не делает Пешку `shadow`-архетипом. Он показывает, что в момент входа игрок выставился под броню, фронтальный обмен и риск застрять в клинче.

## Варианты

### Боевой нож (Combat Shiv) [1H]
[variant_id:: combat_shiv] | [tier:: 1] | [weight:: 0.5kg] | [dmg:: 15] | [setting_status:: mvp]
[combo_chain:: quick jab -> low lunge -> close rip] | [alt_action:: silent draw]
[combo_reset:: пауза после Ready возвращает цепочку к quick jab]

*Короткий клинок для грязной работы в клинче.*
- **Отличие:** самый дешёвый и читаемый вариант для добивания чужого окна.
- **Implicit:** `ambush` делает нож добиванием окна, а не универсальным DPS.
- **Слабость:** почти не решает броню и честный фронтальный обмен.

### Складной хвостовой нож (Tail-Fold Knife) [1H]
[variant_id:: tail_fold_knife] | [tier:: 1] | [weight:: 0.4kg] | [dmg:: 12] | [setting_status:: prototype]
[combo_chain:: wrist prick -> tail feint -> tendon nick] | [alt_action:: offhand distract]
[combo_reset:: потеря close_commit возвращает цепочку к wrist prick]

*Плоский нож для Пешек, которые работают инструментом почти как третьей рукой.*
- **Отличие:** быстрее достаётся и лучше живёт в тесном маршруте, но хуже завершает бронированную цель.
- **Implicit:** `ambush` раскрывается через спрятанный вход, а не через чистый урон.
- **Слабость:** требует уже выигранной дистанции.

### Стеклянный осколочный кинжал (Glass-Splinter Dagger) [1H]
[variant_id:: glass_splinter_dagger] | [tier:: 2] | [weight:: 0.6kg] | [dmg:: 18] | [setting_status:: prototype]
[combo_chain:: testing cut -> splinter press -> disengage stab] | [alt_action:: break edge]
[combo_reset:: после break edge оружие возвращается к testing cut и теряет стабильность]

*Одноразово усиленный клинок из хрупкого аномального стекла.*
- **Отличие:** лучше наказывает открытую мягкую зону, но несёт риск поломки и следа.
- **Implicit:** `ambush` даёт короткую вспышку преимущества, если игрок не затягивает обмен.
- **Слабость:** плох для повторяемых дуэлей и ремонта в рейде.
