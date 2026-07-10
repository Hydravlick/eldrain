---
type: weapon_frame
status: active
system: combat_survival
frame_id: reach_line_2h
display_name: Дистанционная линия, две руки
weapon_family: polearm
grip: two_hand
frame_vector: kinetics
vector_scope: commitment
activates_on: [brace, poke, reach_recovery]
primary_window_function: create
creates_window: [distance_control]
implicit_keyword: outer_line
implicit_rule: Рабочая часть удерживает внешний радиус и коридор, но теряет силу в упоре, у стены и при обходе с боковой линии.
exploits_window: [none]
mitigates_window: [melee_entry]
exposure_channels: [dead_zone, flank, wall_contact, weight]
mastery_unlock: [line_recover, measured_push]
sort_order: 310
tags: [weapon_frame, melee, polearm, two_hand]
related_files:
  - "[[05_Combat_Survival/Weapon_Melee|Weapon_Melee]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Дистанционная линия, две руки

Двуручная линия контролирует вход в мостик, коридор или лестницу. Она не получает право на хороший бой в комнате, где сама длина становится долгом.

## Экземпляры

### Глубинный мерник [2H]
[instance_id:: sounding_pole]
[load_tier:: 1]
[rarity_band:: rusty..rare]
[origin_kind:: local_sector]
[origin_function:: измерение дна, течения и устойчивости настила]
[spawn_profile:: channel_service_cache]
[moveset_profile:: Long Probe -> Haft Check -> Long Probe]
[commitment_cost:: древко не даёт сильного контакта в упор и цепляет боковую раму]
[handedness:: two_hand]
[combo_chain:: Long Probe -> Haft Check -> Long Probe]
[alt_action:: Depth Brace]
[combo_reset:: пауза после Ready возвращает к Long Probe]

Узкая рабочая точка проходит по линии канала и заранее показывает, где начинается мёртвая зона владельца.

### Кронный маршрутник [2H]
[instance_id:: canopy_route_pole]
[load_tier:: 1]
[rarity_band:: uncommon..rare]
[origin_kind:: foreign_snapshot]
[origin_function:: проверка мостиков и отметка пути в кроне]
[spawn_profile:: source_route_cache]
[moveset_profile:: Marking Reach -> Push Back -> Reset]
[commitment_cost:: толчок держит линию, но не даёт урона рабочей части]
[handedness:: two_hand]
[combo_chain:: Marking Reach -> Push Back]
[alt_action:: Rail Brace]
[combo_reset:: пауза после Ready возвращает к Marking Reach]

Маркерная головка меньше режет, но лучше читается как средство удержать край маршрута до отхода.
