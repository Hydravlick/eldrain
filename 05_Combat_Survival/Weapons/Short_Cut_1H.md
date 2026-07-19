---
type: weapon_frame
status: active
system: combat_survival
frame_id: short_cut_1h
display_name: Короткий рез, одна рука
weapon_family: blade
grip: one_hand
skill_interfaces: [edge, contact_surface, free_hand]
activates_on: [draw, cut, close_recovery]
commitment: front_line_draw_until_close_recovery
primary_window_function: exploit
creates_window: [none]
implicit_keyword: draw_cut
implicit_rule: Рабочая кромка держится в тесной геометрии и использует уже открытую мягкую зону, но не выигрывает честный фронтальный обмен.
exploits_window: [soft_zone_exposed, stagger_entry]
mitigates_window: [none]
exposure_channels: [front_exchange, armor_check, close_commit]
mastery_unlock: [quiet_draw, cut_recover]
sort_order: 110
tags: [weapon_frame, melee, blade, one_hand]
related_files:
  - "[[05_Combat_Survival/Weapon_Melee|Weapon_Melee]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Короткий рез, одна рука

Фрейм для короткой рабочей кромки в дверях, на лестнице и в клинче. Он не делает персонажа скрытным сам по себе: риск начинается, когда рука входит под броню и остаётся на передней линии.

## Экземпляры

### Рассольный свежевальщик [1H]
[instance_id:: brine_flenser]
[load_tier:: 1]
[rarity_band:: rusty..rare]
[origin_kind:: foreign_snapshot]
[origin_function:: разделка крупной морской добычи]
[spawn_profile:: stitched_trace]
[moveset_profile:: Short Draw -> Hooked Pull -> Reset]
[commitment_cost:: крюк требует остаться у цели; промах оставляет руку перед корпусом]
[handedness:: one_hand]
[combo_chain:: Short Draw -> Hooked Pull]
[alt_action:: Grip Reverse]
[combo_reset:: пауза после Ready возвращает к Short Draw]

Короткий клинок из солёного слепка: его крюк тянет рез на себя и особенно хорошо использует уже повреждённую мягкую зону. В Порту появляется только как узнаваемый след сшитого POI, а не в случайном ящике.

### Кронный резак [1H]
[instance_id:: canopy_leaf_cutter]
[load_tier:: 1]
[rarity_band:: uncommon..rare]
[origin_kind:: foreign_snapshot]
[origin_function:: срез живой листвы и волокнистых переплетений]
[spawn_profile:: source_garden_cache]
[moveset_profile:: Down Chop -> Inside Slice -> Reset]
[commitment_cost:: короткая рубка не держит дистанцию и теряет темп по твёрдой пластине]
[handedness:: one_hand]
[combo_chain:: Down Chop -> Inside Slice]
[alt_action:: Branch Clear]
[combo_reset:: пауза после Ready возвращает к Down Chop]

Плоская кромка рассчитана на плотную растительность, поэтому не цепляет дверную раму широким замахом. Она надёжна в тесноте, но не получает бесплатного пробоя брони.
