---
type: weapon_frame
status: active
system: combat_survival
frame_id: hook_polearm
display_name: Обход щита
weapon_family: polearm
frame_vector: kinetics
vector_scope: commitment
activates_on: [hook, reap_recovery]
primary_window_function: exploit
creates_window: [none]
exploits_window: [shield_flank]
mitigates_window: [none]
exposure_channels: [close_commit, whiff_recovery, armor_check]
frame_power: 3
exposure_weight: 3
implicit_keyword: reap
implicit_rule: "Кривое лезвие лучше цепляет край щита, руку или боковой угол, если игрок не принимает прямой обмен."
mastery_unlock: [hook_reset]
mvp_verdict: support
mvp_reason: "Показывает фрейм как ответ на щит и угол, но требует уже понятной мили-геометрии."
sort_order: 320
tags: [weapon_frame, weapons, polearm]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Обход щита

Этот фрейм не проламывает защиту напрямую, а ищет боковой угол и край щита. Он силён против неверно поставленного блока, но слабее держит прямой вход.

## Варианты

### Боевая коса (War Scythe) [2H]
[variant_id:: war_scythe] | [tier:: 1] | [weight:: 4.0kg] | [dmg:: 42] | [setting_status:: mvp]
[combo_chain:: draw cut -> shield reap -> step reset] | [alt_action:: haft shove]
[combo_reset:: пауза после Ready возвращает цепочку к draw cut]

*Лезвие под углом, заходящее за блок.*
- **Отличие:** базовый вариант обхода щита без магического пробития.
- **Implicit:** `reap` использует неверный угол защиты, но хуже держит прямой вход.
- **Слабость:** требует правильного угла и пространства под лезвие.

### Портовый багор (Dock Billhook) [2H]
[variant_id:: dock_billhook] | [tier:: 1] | [weight:: 3.6kg] | [dmg:: 34] | [setting_status:: prototype]
[combo_chain:: hook wrist -> pull line -> knee cut] | [alt_action:: drag object]
[combo_reset:: если pull line сорван, цепочка возвращается к hook wrist]

*Багор для тросов и грузов, переделанный под людей и щиты.*
- **Отличие:** лучше тянет предметы и руки, но хуже наносит чистый урон.
- **Implicit:** `reap` создаёт тактический угол, а не гарантированный крит.
- **Слабость:** промах открывает близкий вход противника.

### Кабельная коса (Cable Scythe) [2H]
[variant_id:: cable_scythe] | [tier:: 2] | [weight:: 4.6kg] | [dmg:: 39] | [setting_status:: prototype]
[combo_chain:: cable feint -> side reap -> anchor pull] | [alt_action:: line snag]
[combo_reset:: обрыв линии возвращает цепочку к cable feint]

*Коса с коротким страховочным кабелем для контроля края щита.*
- **Отличие:** лучше удерживает ошибку цели, но несёт риск запутаться.
- **Implicit:** `reap` получает больше времени на боковом угле.
- **Слабость:** сложнее читать и опаснее в тесной свалке.
