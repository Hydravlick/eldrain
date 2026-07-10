---
type: weapon_frame
status: active
system: combat_survival
frame_id: needle_blade
display_name: Игольный клинок
weapon_family: blade
frame_vector: shadow
vector_scope: commitment
activates_on:
  - thrust
  - precision_recovery
primary_window_function: exploit
creates_window:
  - none
implicit_keyword: needle_point
exploits_window:
  - joint_exposed
mitigates_window:
  - none
exposure_channels:
  - line_commit
  - shield_angle
  - armor_check
frame_power: 3
exposure_weight: 2
mastery_unlock:
  - joint_followup
mvp_verdict: specialist
mvp_reason: Полезен для точной дуэли и сочленений, но сеттинговый сигнал слабее магострела.
sort_order: 130
tags:
  - weapon_frame
  - weapons
  - blade
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Игольный клинок

Игольный клинок превращает точную линию укола в попытку найти сочленение. Он силён против раскрытой защиты, но не обязан пробивать броню без правильного угла.

## Варианты

### Рапира / Эсток (Estoc) [1H]
[variant_id:: estoc]
[tier:: 1]
[weight:: 1.2kg] | [dmg:: 25]
[heat:: 0] | [dissonance_pulse:: 0]
[combo_chain:: Probe Thrust -> Committed Thrust -> Withdraw Cut]
[alt_action:: Parry]
[combo_reset:: пауза после Ready возвращает цепочку к Probe Thrust]

Тонкий клинок для уколов в сочленения брони.

- **Мувсет:** линейные выпады на дистанции.
- **Implicit:** `needle_point` требует видимой линии и не пробивает пластину магически.
- **Слабость:** крит требует попадания в уязвимую зону; твёрдая пластина продолжает блокировать удар по физическим правилам.

### Монтажный Стилет (Rigging Stiletto) [1H]
[variant_id:: rigging_stiletto]
[tier:: 1]
[weight:: 0.9kg] | [dmg:: 20]
[heat:: 0] | [dissonance_pulse:: 0]
[combo_chain:: Upper-Right Diagonal -> Upper-Left Diagonal -> Deep Thrust]
[alt_action:: None]
[combo_reset:: пауза после Ready возвращает цепочку к Upper-Right Diagonal]

Промышленный такелажный инструмент вместо оружия: очень узкий Capsule Sweep строго вперёд.

- **Мувсет:** два коротких диагональных реза (справа-сверху, затем слева-сверху), завершающихся глубоким прямым уколом с бонусным уроном по уже раненой цели.
- **Implicit:** `needle_point` здесь читается не через угол брони, а через уже открытую (раненую) зону — третий удар именно за это награждает.
- **Слабость:** нет останавливающего действия; тяжёлая цель просто игнорирует укол и наносит встречный удар в размен.
- **Отличие:** легче и быстрее Эстока, с явным бонусом по добиванию, но без парирующего alt-действия и без такой же чистой линии выпада.
