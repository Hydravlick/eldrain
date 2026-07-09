---
type: weapon_frame
status: active
system: combat_survival
frame_id: heavy_blade
display_name: Тяжёлое лезвие
weapon_family: blade
frame_vector: shadow
vector_scope: commitment
activates_on: [swing, cleave_recovery]
primary_window_function: exploit
creates_window: [soft_zone_exposed]
exploits_window: [soft_zone_exposed]
mitigates_window: [none]
exposure_channels: [whiff_recovery, armor_check, noise]
frame_power: 3
exposure_weight: 3
mastery_unlock: [cleave_chain_control]
mvp_verdict: specialist
mvp_reason: "Хорошо показывает физику траектории и стены, но как главный MVP уводит в обычное фентези."
sort_order: 120
tags: [weapon_frame, weapons, blade]
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Тяжёлое лезвие

Тяжёлое лезвие ставит на широкое движение и мягкие зоны. Оно хорошо добирает цель, которая уже раскрылась, но платит шумом, recovery и плохой работой по твёрдой пластине.

## Варианты

### Мачете / Тесак (Cleaver) [1H]
[variant_id:: cleaver]
[tier:: 1]
[weight:: 1.5kg] | [dmg:: 35]
[heat:: 0]
[dissonance_pulse:: 0]
[implicit:: maim]
[implicit_rule:: повторный рубящий контакт по уже раскрытой мягкой зоне усиливает травму и замедляет отход цели]
[input_pattern:: tap: chop -> hold: drag cut -> hold: committed cleave]
[combo_reset:: пауза после Ready возвращает цепочку к chop]

Тяжёлое лезвие со смещённым центром тяжести.

- **Мувсет:** широкие рубящие удары, задевающие несколько мягких целей.
- **Implicit:** `maim` награждает за уже созданное окно, а не за рубку брони в лоб.
- **Слабость:** заметный recovery после промаха и плохая работа по твёрдой пластине.
