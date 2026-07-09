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
mastery_unlock: [sweet_spot_recover]
mvp_verdict: support
mvp_reason: "Нужен для проверки reach и геометрии, но главный MVP не должен быть обычной алебардой."
sort_order: 310
tags: [weapon_frame, weapons, polearm]
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Дистанционная древка

Дистанционная древка создаёт контроль входа и наказывает прямую попытку сблизиться. Её моментная экспозиция появляется, когда цель проходит в мёртвую зону или обходит угол удара.

## Варианты

### Алебарда (Halberd) [2H]
[variant_id:: halberd]
[tier:: 1]
[weight:: 5.5kg] | [dmg:: 45]
[sweet_spot_range:: 1.7-2.4m]
[heat:: 0]
[dissonance_pulse:: 0]
[implicit:: sweet_spot]
[implicit_rule:: рабочая голова даёт полный эффект только в outer band; древко вблизи сохраняет контакт, но теряет пролом]
[input_pattern:: tap: brace poke -> hold: head sweep -> hold: haft recover]
[combo_reset:: пауза после Ready возвращает цепочку к brace poke]

Топор на длинной палке с шипом.

- **Мувсет:** укол на дистанции, рубящий swing вблизи.
- **Implicit:** `sweet_spot` читается дистанцией и контактом головы, а не скрытым множителем.
- **Слабость:** вплотную древко наносит слабый урон; обход сбоку ломает дистанционный контроль.
