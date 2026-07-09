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
mastery_unlock: [hook_reset]
mvp_verdict: support
mvp_reason: "Показывает фрейм как ответ на щит и угол, но требует уже понятной мили-геометрии."
sort_order: 320
tags: [weapon_frame, weapons, polearm]
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Обход щита

Этот фрейм не проламывает защиту напрямую, а ищет боковой угол и край щита. Он силён против неверно поставленного блока, но слабее держит прямой вход.

## Варианты

### Боевая коса (War Scythe) [2H]
[variant_id:: war_scythe]
[tier:: 1]
[weight:: 4.0kg] | [dmg:: 42]
[heat:: 0]
[dissonance_pulse:: 0]
[implicit:: reap]
[implicit_rule:: кривое лезвие лучше цепляет край щита, руку или боковой угол, если игрок не принимает прямой обмен]
[input_pattern:: tap: draw cut -> hold: shield reap -> hold: step reset]
[combo_reset:: пауза после Ready возвращает цепочку к draw cut]

Лезвие под углом, заходящее за блок.

- **Implicit:** `reap` использует неверный угол защиты, но хуже держит прямой вход.
- **Слабость:** хуже держит прямой вход и требует правильного угла.
