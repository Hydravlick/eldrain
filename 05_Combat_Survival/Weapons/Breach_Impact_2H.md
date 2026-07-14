---
type: weapon_frame
status: active
system: combat_survival
frame_id: breach_impact_2h
display_name: Проломный ударник, две руки
weapon_family: blunt
grip: two_hand
skill_interfaces: [impact_surface, contact_surface, brace]
activates_on: [brace, windup, impact, heavy_recovery]
commitment: both_hands_below_guard_after_committed_impact
primary_window_function: create
creates_window: [breach_open]
implicit_keyword: structural_breach
implicit_rule: Двуручная масса переносит силу в дверь, крепление или стойку, но заранее раскрывает намерение и оставляет владельца без быстрого ответа.
exploits_window: [none]
mitigates_window: [none]
exposure_channels: [windup_interrupt, noise, weight, whiff_recovery]
mastery_unlock: [brace_retarget, measured_breach]
sort_order: 220
tags: [weapon_frame, melee, blunt, two_hand]
related_files:
  - "[[05_Combat_Survival/Weapon_Melee|Weapon_Melee]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Проломный ударник, две руки

Пролом существует для задач, которые не должен закрывать нож: вскрыть закрепление, разрушить хрупкое укрытие, заставить противника сменить угол. Это громкая и медленная ставка.

## Экземпляры

### Свайный осадник [2H]
[instance_id:: pile_head_driver]
[load_tier:: 1]
[rarity_band:: rusty..rare]
[origin_kind:: local_sector]
[origin_function:: посадка опор в мокром грунте]
[spawn_profile:: dockwork_cache]
[moveset_profile:: Brace Push -> Committed Plunge -> Recovery]
[commitment_cost:: после вертикального удара обе руки остаются ниже линии защиты]
[handedness:: two_hand]
[combo_chain:: Brace Push -> Committed Plunge]
[alt_action:: Ground Brace]
[combo_reset:: любой контакт с геометрией возвращает к Brace Push]

Экземпляр лучше работает по креплению и полу, чем по движущейся цели. Его польза в рейде начинается с изменения маршрута, а не с максимального урона.

### Размыкатель ставней [2H]
[instance_id:: shutter_breaker]
[load_tier:: 2]
[rarity_band:: rare..epic]
[origin_kind:: city_frontier]
[origin_function:: аварийное открытие защитных створок]
[spawn_profile:: civic_defense_cache]
[moveset_profile:: Side Lever -> Frame Strike -> Long Recover]
[commitment_cost:: боковой рычаг шумный, требует свободной дуги и долго возвращает руки]
[handedness:: two_hand]
[combo_chain:: Side Lever -> Frame Strike]
[alt_action:: Lock Brace]
[combo_reset:: пауза после Recovery возвращает к Side Lever]

Бывшее оружие обороны фронтира существует как оружие изначально, но его форма всё ещё объясняет задачу: ломать закрытый путь, а не выигрывать дуэль.
