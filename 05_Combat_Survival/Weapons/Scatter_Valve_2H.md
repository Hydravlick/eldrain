---
type: weapon_frame
status: active
system: combat_survival
frame_id: scatter_valve_2h
display_name: Веерный клапан, две руки
weapon_family: arcanegun
grip: two_hand
skill_interfaces: [conduit, brace]
activates_on: [brace, valve_open, volley_lock, vent_recovery]
commitment: locked_cone_through_volley_and_vent
primary_window_function: create
creates_window: [entry_denied]
implicit_keyword: linked_scatter
implicit_rule: Один открытый клапан выпускает связанную гроздь слабых импульсов по закреплённому конусу; частичный контакт давит на вход, но не даёт бесплатного тяжёлого контроля.
exploits_window: [none]
mitigates_window: [melee_entry]
exposure_channels: [heat, short_range, noise, open_line, vent_recovery]
mastery_unlock: [valve_recover, cone_hold]
sort_order: 430
tags: [weapon_frame, ranged, arcanegun, two_hand]
related_files:
  - "[[05_Combat_Survival/Weapon_Ranged|Weapon_Ranged]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Веерный клапан, две руки

Фрейм получает терпимость к ошибке прицеливания не через магазин, а через одну связанную очередь. Игрок выбирает конус до первого импульса и выплачивает Heat после последнего.

## Экземпляры

### Клапан дверного давления [2H]
[instance_id:: doorway_pressure_valve]
[load_tier:: 1]
[rarity_band:: rusty..rare]
[origin_kind:: local_sector]
[origin_function:: аварийное удержание дверного проёма]
[spawn_profile:: emergency_cabinet]
[moveset_profile:: Brace Doorway -> Three Pulse Sweep -> Manual Vent]
[commitment_cost:: весь триплет фиксирует конус; после него нужны обе руки для сброса]
[handedness:: two_hand]
[energy_mode:: battery]
[emission_profile:: triplet pressure sweep]
[cadence_gate:: manual_vent]
[impulse_cost:: 1]
[fire_input:: Hold to Brace -> Release Valve]
[reload_mechanic:: route new battery only when reserve is empty]

Три слабых импульса приходят с короткой внутренней задержкой. Один-два касания создают шум и давление; сильный срыв входа требует полного близкого контакта всей грозди.

### Камышовый продуватель [2H]
[instance_id:: reedbed_sweeper]
[load_tier:: 2]
[rarity_band:: uncommon..rare]
[origin_kind:: foreign_snapshot]
[origin_function:: расчистка плотной влажной поросли перед проходом]
[spawn_profile:: source_field_cache]
[moveset_profile:: Low Brace -> Wide Triplet -> Heat Purge]
[commitment_cost:: широкий веер хуже держит одну цель и оставляет тяжёлый тепловой след]
[handedness:: two_hand]
[energy_mode:: battery]
[emission_profile:: wide triplet sweep]
[cadence_gate:: heat_purge]
[impulse_cost:: 1]
[fire_input:: Hold to Brace -> Release Valve]
[reload_mechanic:: route new battery only when reserve is empty]

Этот экземпляр лучше строит краткую преграду в густой среде, но хуже наносит точный урон и заметнее для Аномалии.
