---
type: weapon_frame
status: active
system: combat_survival
frame_id: reach_polearm
display_name: Дистанционная древка
weapon_family: polearm
frame_vector: kinetics
vector_scope: commitment
activates_on: [brace, poke, swing_recovery]
primary_window_function: create
creates_window: [distance_control]
exploits_window: [none]
mitigates_window: [melee_entry]
exposure_channels: [dead_zone, flank, whiff_recovery, weight]
frame_power: 4
exposure_weight: 4
implicit_keyword: sweet_spot
implicit_rule: "Рабочая голова даёт полный эффект только во внешнем диапазоне; древко вблизи сохраняет контакт, но теряет пролом."
mastery_unlock: [sweet_spot_recover]
mvp_verdict: support
mvp_reason: "Нужен для проверки reach и геометрии, но главный MVP не должен быть обычной алебардой."
sort_order: 310
tags: [weapon_frame, weapons, polearm]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Дистанционная древка

Дистанционная древка создаёт контроль входа и наказывает прямую попытку сблизиться. Её моментная экспозиция появляется, когда цель проходит в мёртвую зону или обходит угол удара.

## Варианты

### Алебарда (Halberd) [2H]
[variant_id:: halberd] | [tier:: 1] | [weight:: 5.5kg] | [dmg:: 45] | [sweet_spot_range:: 1.7-2.4m] | [setting_status:: mvp]
[combo_chain:: brace poke -> head sweep -> haft recover] | [alt_action:: butt check]
[combo_reset:: пауза после Ready возвращает цепочку к brace poke]

*Топор на длинной палке с шипом.*
- **Отличие:** самый широкий учебный пример sweet spot и мёртвой зоны.
- **Implicit:** `sweet_spot` читается дистанцией и контактом головы.
- **Слабость:** вплотную древко наносит слабый урон; обход сбоку ломает контроль.

### Трубное копьё (Pipe Pike) [2H]
[variant_id:: pipe_pike] | [tier:: 1] | [weight:: 3.2kg] | [dmg:: 32] | [sweet_spot_range:: 1.9-2.7m] | [setting_status:: prototype]
[combo_chain:: line brace -> narrow thrust -> pull back] | [alt_action:: wall plant]
[combo_reset:: цель в dead_zone возвращает цепочку к line brace]

*Простая труба с насаженным жалом, удобная для коридоров.*
- **Отличие:** легче и уже алебарды, лучше держит прямую линию, хуже рубит.
- **Implicit:** `sweet_spot` работает как дисциплина расстояния.
- **Слабость:** почти не отвечает на боковой обход.

### Складная дозорная древка (Watch Pole) [2H]
[variant_id:: watch_pole] | [tier:: 2] | [weight:: 4.8kg] | [dmg:: 38] | [sweet_spot_range:: 1.5-2.2m] | [setting_status:: prototype]
[combo_chain:: extend check -> snap thrust -> lock sweep] | [alt_action:: collapse haft]
[combo_reset:: collapse haft возвращает оружие к extend check]

*Древка с фиксатором, которую можно переносить в тесном маршруте.*
- **Отличие:** платит надёжностью за переносимость и быструю смену длины.
- **Implicit:** `sweet_spot` становится видимым через раскладку древка.
- **Слабость:** фиксатор создаёт отдельный момент сбоя под давлением.
