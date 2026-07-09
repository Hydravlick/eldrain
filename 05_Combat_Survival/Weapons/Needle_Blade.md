---
type: weapon_frame
status: active
system: combat_survival
frame_id: needle_blade
display_name: Игольный клинок
weapon_family: blade
frame_vector: shadow
vector_scope: commitment
activates_on: [thrust, precision_recovery]
primary_window_function: exploit
creates_window: [none]
exploits_window: [joint_exposed]
mitigates_window: [none]
exposure_channels: [line_commit, shield_angle, armor_check]
frame_power: 3
exposure_weight: 2
implicit_keyword: needle_point
implicit_rule: "Удержанная линия укола лучше находит сочленение, если цель уже раскрыта углом, stagger или ошибкой щита."
mastery_unlock: [joint_followup]
mvp_verdict: specialist
mvp_reason: "Полезен для точной дуэли и сочленений, но сеттинговый сигнал слабее магострела."
sort_order: 130
tags: [weapon_frame, weapons, blade]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Игольный клинок

Игольный клинок превращает точную линию укола в попытку найти сочленение. Он силён против раскрытой защиты, но не обязан пробивать броню без правильного угла.

## Варианты

### Рапира / Эсток (Estoc) [1H]
[variant_id:: estoc] | [tier:: 1] | [weight:: 1.2kg] | [dmg:: 25] | [setting_status:: mvp]
[combo_chain:: probe thrust -> committed thrust -> withdraw cut] | [alt_action:: bind blade]
[combo_reset:: пауза после Ready возвращает цепочку к probe thrust]

*Тонкий клинок для уколов в сочленения брони.*
- **Отличие:** самый понятный вариант для дуэли по линии.
- **Implicit:** `needle_point` требует видимой линии и не пробивает пластину магически.
- **Слабость:** крит требует попадания в уязвимую зону.

### Шовный стилет (Seam Stiletto) [1H]
[variant_id:: seam_stiletto] | [tier:: 1] | [weight:: 0.8kg] | [dmg:: 20] | [setting_status:: prototype]
[combo_chain:: mark seam -> short drive -> twist free] | [alt_action:: armor feeler]
[combo_reset:: потеря контакта с целью возвращает цепочку к mark seam]

*Тонкое ремонтное шило, заточенное под щели в защите.*
- **Отличие:** лучше читает швы брони, но почти не держит дистанцию.
- **Implicit:** `needle_point` превращает знание материала в боевое окно.
- **Слабость:** без close_commit и правильного угла становится слабым уколом.

### Контурная игла (Contour Needle) [1H]
[variant_id:: contour_needle] | [tier:: 2] | [weight:: 1.0kg] | [dmg:: 24] | [setting_status:: prototype]
[combo_chain:: line test -> joint slip -> recoil step] | [alt_action:: off-angle feint]
[combo_reset:: смена стороны сбрасывает цепочку к line test]

*Гильдейский клинок с направляющей, помогающей удержать линию укола.*
- **Отличие:** стабильнее в руках техничной Пешки, но дороже теряется.
- **Implicit:** `needle_point` требует подготовки, а не заменяет её.
- **Слабость:** слаб против щита, который не дал ошибочного угла.
