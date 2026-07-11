---
type: weapon_frame
status: active
system: combat_survival
frame_id: compact_impact_1h
display_name: Компактный ударник, одна рука
weapon_family: blunt
grip: one_hand
skill_interfaces: [impact_surface, contact_surface, free_hand]
frame_vector: kinetics
vector_scope: commitment
activates_on: [swing, impact, close_recovery]
primary_window_function: create
creates_window: [disorientation]
implicit_keyword: local_concussion
implicit_rule: Короткая масса создаёт краткое окно дезориентации только после близкого чистого контакта; она не удерживает дальний вход и не ломает строй сама.
exploits_window: [none]
mitigates_window: [none]
exposure_channels: [close_commit, shield_angle]
mastery_unlock: [concussion_followup, close_reset]
sort_order: 210
tags: [weapon_frame, melee, blunt, one_hand]
related_files:
  - "[[05_Combat_Survival/Weapon_Melee|Weapon_Melee]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Компактный ударник, одна рука

Этот фрейм делает одно короткое окно для смены оружия, отхода или чужого удара. Он существует для тесных комнат, а не как запасной молот на все случаи.

## Экземпляры

### Ключ ударной задвижки [1H]
[instance_id:: valve_striker]
[load_tier:: 1]
[rarity_band:: rusty..rare]
[origin_kind:: local_sector]
[origin_function:: аварийное открытие заклинивших клапанов]
[spawn_profile:: pump_station_locker]
[moveset_profile:: Body Tap -> Valve Arc -> Shoulder Clear]
[commitment_cost:: широкий второй контакт цепляет угол и оставляет короткий recovery]
[handedness:: one_hand]
[combo_chain:: Body Tap -> Valve Arc -> Shoulder Clear]
[alt_action:: Hilt Check]
[combo_reset:: пауза после Ready возвращает к Body Tap]

Вес у головки рассчитан на короткий силовой толчок, а не на дальний размах. Попадание по телу создаёт момент сбитой готовности, но игрок всё равно находится в опасной дистанции.

### Печной подбиватель [1H]
[instance_id:: kiln_tapper]
[load_tier:: 1]
[rarity_band:: uncommon..rare]
[origin_kind:: foreign_snapshot]
[origin_function:: выравнивание керамических кожухов горячего контура]
[spawn_profile:: source_kiln_cache]
[moveset_profile:: Short Ring -> Down Set -> Reset]
[commitment_cost:: вертикальный второй удар читаем и плохо преследует отход]
[handedness:: one_hand]
[combo_chain:: Short Ring -> Down Set]
[alt_action:: Heat Check]
[combo_reset:: пауза после Ready возвращает к Short Ring]

Керамическая накладка даёт чистый звон и хорошо сообщает попадание, но ударник теряет часть силы на тяжёлой пластине.
