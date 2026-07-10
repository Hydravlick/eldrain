---
type: weapon_frame
status: active
system: combat_survival
frame_id: short_blade
display_name: Короткий клинок
weapon_family: blade
frame_vector: shadow
vector_scope: commitment
activates_on:
  - draw
  - lunge
  - backstab_recovery
primary_window_function: exploit
creates_window:
  - none
implicit_keyword: ambush
exploits_window:
  - back_exposed
  - stagger_entry
mitigates_window:
  - none
exposure_channels:
  - armor_check
  - front_exchange
  - close_commit
frame_power: 2
exposure_weight: 2
mastery_unlock:
  - silent_draw
  - faster_recovery
mvp_verdict: core_pair
mvp_reason: Нужен как дешёвое добивание после окна, но сам по себе слишком похож на обычный RPG-нож.
sort_order: 110
tags:
  - weapon_frame
  - weapons
  - blade
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Короткий клинок

Короткий клинок не делает Пешку `shadow`-архетипом. Он показывает, что в момент входа игрок выставился под броню, фронтальный обмен и риск застрять в клинче.

## Варианты

### Боевой нож (Combat Shiv) [1H]
[variant_id:: combat_shiv]
[tier:: 1]
[weight:: 0.5kg] | [dmg:: 15]
[heat:: 0] | [dissonance_pulse:: 0]
[combo_chain:: Quick Jab -> Low Lunge -> Close Rip]
[alt_action:: None]
[combo_reset:: пауза после Ready возвращает цепочку к Quick Jab]

Короткий клинок для грязной работы в клинче.

- **Мувсет:** быстрые колющие удары с малым расходом стамины.
- **Implicit:** `ambush` делает нож добиванием окна, а не универсальным DPS.
- **Слабость:** почти не решает броню и честный фронтальный обмен.

### Шоковый Пуш-нож (Shock Push-Knife) [1H]
[variant_id:: shock_push_knife]
[tier:: 1]
[weight:: 0.4kg] | [dmg:: 8]
[heat:: 0] | [dissonance_pulse:: 1]
[combo_chain:: Left Hook -> Right Hook -> (repeat)]
[alt_action:: None]
[combo_reset:: цепочка не сбрасывается; серия бесконечна, пока не отпущена кнопка]

Хитбоксы привязаны к сокетам кистей: заряженное лезвие бьёт по щитам и барьерам, а не по плоти.

- **Мувсет:** бесконечная левая-правая цепочка хуков с почти нулевым Windup (0.1s), но урон проходит только по энергетическим щитам/барьерам.
- **Implicit:** `ambush` здесь работает как снятие защиты перед настоящим добиванием, а не как прямой урон по здоровью.
- **Слабость:** нулевой урон по здоровью цели; для добивания нужно физически сменить оружие после снятия щита.
- **Отличие:** быстрее и безопаснее в размене, чем Боевой нож, но бесполезен как самостоятельное орудие убийства — только как снятие щита перед сменой оружия.
