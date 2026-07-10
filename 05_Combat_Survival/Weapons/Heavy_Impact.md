---
type: weapon_frame
status: active
system: combat_survival
frame_id: heavy_impact
display_name: Тяжёлый ударник
weapon_family: blunt
frame_vector: kinetics
vector_scope: commitment
activates_on:
  - windup
  - impact
  - heavy_recovery
primary_window_function: create
creates_window:
  - guard_break
implicit_keyword: breach
exploits_window:
  - none
mitigates_window:
  - none
exposure_channels:
  - windup_interrupt
  - dodge_punish
  - noise
  - weight
frame_power: 4
exposure_weight: 5
mastery_unlock:
  - committed_retarget
mvp_verdict: specialist
mvp_reason: Силен как тест веса, дверей и guard break, но риск универсального пролома слишком высок для главного MVP.
sort_order: 210
tags:
  - weapon_frame
  - weapons
  - blunt
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Тяжёлый ударник

Тяжёлый ударник обещает пролом, но просит игрока заранее принять долгий замах и дорогой recovery. Это не универсальная кинетика, а моментная ставка телом и весом.

## Варианты

### Кувалда (Sledgehammer) [2H]
[variant_id:: sledgehammer]
[tier:: 1]
[weight:: 8kg] | [dmg:: 55]
[heat:: 0] | [dissonance_pulse:: 0]
[combo_chain:: Wide Horizontal Sweep -> Overhead Slam]
[alt_action:: Shoulder Shove]
[combo_reset:: пауза после Recovery возвращает цепочку к Wide Horizontal Sweep]

Инструмент, превращённый в оружие. Медленный и неотвратимый.

- **Мувсет:** долгий горизонтальный замах слева направо (Windup 0.6s), задевающий несколько целей; гладкая коллизия со стенами обрывает замах Stagger'ом. Второй удар — тяжёлый вертикальный оверхед, игнорирующий стены и наносящий огромный урон броне.
- **Implicit:** `breach` покупается телеграфом и тяжёлым recovery.
- **Слабость:** начатый замах невозможно остановить; медлительность делает вас мишенью для быстрых уколов.

### Штурмовой Молот (Breaching Maul) [2H]
[variant_id:: breaching_maul]
[tier:: 2]
[weight:: 11kg] | [dmg:: 68]
[heat:: 0] | [dissonance_pulse:: 0]
[combo_chain:: Overhead Slam -> Recovery Reset]
[alt_action:: Brace]
[combo_reset:: удара по геометрии всегда сбрасывает цепочку к Overhead Slam]

Проходческий молот, доработанный под ближний бой: почти вся масса уходит в один удар.

- **Мувсет:** единственный тяжёлый оверхед без горизонтальной фазы; урон по дверям, укрытиям и жёсткой геометрии выше, чем у Кувалды, но нет промежуточного удара для контроля нескольких целей.
- **Implicit:** `breach` здесь даже сильнее заточен под структуры и укрытия, а не под тело.
- **Слабость:** ещё длиннее Windup и Recovery; полностью проигрывает размен любому оружию с блоком или уколом.
- **Отличие:** сильнее пробивает укрытия и структуры, чем Кувалда, но жертвует вторым ударом цепочки и скоростью восстановления.
