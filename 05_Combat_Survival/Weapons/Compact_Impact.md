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
implicit_keyword: concussion
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
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Компактный ударник

Компактный ударник создаёт короткое окно дезориентации вблизи. Он дешевле по обязательству, чем тяжёлый пролом, но просит войти в опасную дистанцию.

## Варианты

### Булава / Дубинка (Mace) [1H]
[variant_id:: mace]
[tier:: 1]
[weight:: 3.5kg] | [dmg:: 30]
[heat:: 0] | [dissonance_pulse:: 0]
[combo_chain:: Body Tap -> Head Swing -> Shoulder Check]
[alt_action:: Hilt Bash]
[combo_reset:: пауза после Ready возвращает цепочку к Body Tap]

Компактный вес для короткого силового обмена.

- **Мувсет:** широкий Capsule Sweep вблизи; три удара нарастающей стоимости, последний (Shoulder Check) — почти толчок телом.
- **Implicit:** `concussion` открывает follow-up, но не держит дальний подход.
- **Слабость:** требует входа в опасную дистанцию и плохо догоняет отходящую цель.

### Аварийные Тиски (Emergency Tongs) [1H]
[variant_id:: emergency_tongs]
[tier:: 1]
[weight:: 1.2kg] | [dmg:: 18]
[heat:: 0] | [dissonance_pulse:: 0]
[combo_chain:: Down Chop -> Reverse Uppercut]
[alt_action:: None]
[combo_reset:: 3-го удара нет; серия обрывается длинной фазой Recovery после 2-го]

Импровизированный инструмент вместо оружия: узкий вертикальный Capsule Sweep, не цепляет стены.

- **Мувсет:** быстрый рубящий сверху вниз (Windup 0.3s), затем почти мгновенный обратный рез снизу вверх (Active Frames через 0.15s).
- **Implicit:** `concussion` срабатывает раньше и дешевле, чем у Булавы, но без третьего удара для закрепления окна.
- **Слабость:** промах вторым ударом оставляет игрока полностью открытым; бесполезен против цели, читающей стрейф.
- **Отличие:** легче и быстрее Булавы почти вдвое, но теряет продолженную атаку и не имеет alt-действия.
