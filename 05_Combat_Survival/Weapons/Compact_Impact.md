---
type: weapon_frame
status: active
system: combat_survival
frame_id: compact_impact
display_name: Компактный ударник
weapon_family: blunt
frame_vector: kinetics
vector_scope: commitment
activates_on:
  - swing
  - headshot_recovery
primary_window_function: create
creates_window:
  - disorientation
exploits_window:
  - none
mitigates_window:
  - none
exposure_channels:
  - close_commit
  - shield_angle
frame_power: 2
exposure_weight: 2
mastery_unlock:
  - concussion_followup
mvp_verdict: core_pair
mvp_reason: Хороший базовый инструмент ближнего контроля, но сеттингово почти не объясняет Элдрейн.
sort_order: 220
tags:
  - weapon_frame
  - weapons
  - blunt
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Компактный ударник

Компактный ударник создаёт короткое окно дезориентации вблизи. Он дешевле по обязательству, чем тяжёлый пролом, но просит войти в опасную дистанцию.

## Варианты

### Булава / Дубинка (Mace) [1H]
[variant_id:: mace]
[tier:: 1]
[weight:: 3.5kg] | [dmg:: 30]
[heat:: 0]
[dissonance_pulse:: 0]
[implicit:: concussion]
[implicit_rule:: удар по голове, маске или жёсткой зоне создаёт короткую дезориентацию, если игрок вошёл в опасную дистанцию]
[input_pattern:: tap: body tap -> hold: head swing -> hold: shoulder check]
[combo_reset:: пауза после Ready возвращает цепочку к body tap]

Компактный вес для короткого силового обмена.

- **Implicit:** `concussion` открывает follow-up, но не держит дальний подход.
- **Слабость:** требует входа в опасную дистанцию и плохо догоняет отходящую цель.
