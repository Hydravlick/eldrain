---
type: weapon_frame
status: active
system: combat_survival
frame_id: hook_reach_2h
display_name: Зацепная линия, две руки
weapon_family: polearm
grip: two_hand
frame_vector: kinetics
vector_scope: commitment
activates_on: [hook_swing, pull, hook_recovery]
primary_window_function: create
creates_window: [angle_displaced]
implicit_keyword: edge_hook
implicit_rule: Крючковая рабочая часть ищет край защиты, поручень или неверный угол, но не удерживает прямой вход так же надёжно, как дистанционная линия.
exploits_window: [shield_edge, route_edge]
mitigates_window: [none]
exposure_channels: [open_arc, wall_contact, pull_recovery, weight]
mastery_unlock: [hook_release, angle_recover]
sort_order: 320
tags: [weapon_frame, melee, polearm, two_hand]
related_files:
  - "[[05_Combat_Survival/Weapon_Melee|Weapon_Melee]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Зацепная линия, две руки

Фрейм не «обходит щит магически»: он даёт игроку длинный рычаг для края, перил, ремня или неверно поставленной защиты. Ошибка оставляет широкий открытый сектор.

## Экземпляры

### Швартовый съёмник [2H]
[instance_id:: mooring_reclaimer]
[load_tier:: 1]
[rarity_band:: rusty..rare]
[origin_kind:: local_sector]
[origin_function:: снятие заклинивших швартовов и тросов]
[spawn_profile:: dockwork_cache]
[moveset_profile:: Outside Hook -> Pull Clear -> Reset]
[commitment_cost:: попытка тяги открывает бок и не работает по прямой тяжёлой защите]
[handedness:: two_hand]
[combo_chain:: Outside Hook -> Pull Clear]
[alt_action:: Rope Catch]
[combo_reset:: пауза после Ready возвращает к Outside Hook]

Он силён там, где сама карта даёт край: мостик, перила, дверной косяк, трос. На открытой прямой линии уступает мернику.

### Садовый выборщик [2H]
[instance_id:: orchard_retriever]
[load_tier:: 1]
[rarity_band:: uncommon..rare]
[origin_kind:: foreign_snapshot]
[origin_function:: снятие плодов и опасной поросли с высоты]
[spawn_profile:: source_garden_cache]
[moveset_profile:: High Catch -> Side Draw -> Reset]
[commitment_cost:: верхняя дуга требует свободного объёма и медленно возвращает оружие]
[handedness:: two_hand]
[combo_chain:: High Catch -> Side Draw]
[alt_action:: Branch Hold]
[combo_reset:: пауза после Ready возвращает к High Catch]

Широкий захват помогает снять цель с края, но хуже удерживает прямой лестничный вход.
