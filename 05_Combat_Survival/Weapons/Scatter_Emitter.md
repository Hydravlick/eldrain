---
type: weapon_frame
status: active
system: combat_survival
frame_id: scatter_emitter
display_name: Веерный эмиттер
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on:
  - charge
  - cone_release
  - vent_recovery
primary_window_function: create
creates_window:
  - melee_entry
implicit_keyword: stagger_cone
exploits_window:
  - none
mitigates_window:
  - enemy_entry
exposure_channels:
  - heat
  - short_range
  - reload_timing
  - open_line
frame_power: 3
exposure_weight: 4
mastery_unlock:
  - cone_discipline
mvp_verdict: core_support
mvp_reason: Хорошо показывает Heat и контроль входа, но в одиночку может стать слишком понятным магическим дробовиком.
sort_order: 430
tags:
  - weapon_frame
  - weapons
  - arcanegun
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
---
# Веерный эмиттер

Веерный эмиттер останавливает вход и открывает ближнее окно, но платит короткой дистанцией, Heat и потерей темпа после выпуска.

## Варианты

### Веерный Эмиттер (Scatter Emitter) [2H]
[variant_id:: scatter_emitter]
[tier:: 1]
[weight:: 3.8kg] | [dmg:: 10x6]
[impulse_cost:: 1]
[charge_time:: 0.4s]
[heat:: 50]
[bloom:: high]
[dissonance_pulse:: 5]
[fire_input:: Hold (Windup)]
[reload_mechanic:: Pump]

Выплескивает веер нестабильной энергии. Не про точность, а про остановку входа.

- **Мувсет:** короткий конус дроби вызывает принудительный Stagger, прерывающий любую анимацию цели.
- **Implicit:** `stagger_cone` покупает пространство, но быстро сжигает темп.
- **Слабость:** выстрел сжигает 70% выносливости стрелка; если дистанция не сокращена немедленно или заряд ушёл в молоко, стрелок остаётся без защиты. На средней дистанции урон распадается, Heat копится быстро.

### Дуговой Плевок (Arc Spitter) [1H]
[variant_id:: arc_spitter]
[tier:: 1]
[weight:: 2.2kg] | [dmg:: 6x6]
[impulse_cost:: 1]
[charge_time:: 0.2s]
[heat:: 30]
[bloom:: high]
[dissonance_pulse:: 3]
[fire_input:: Tap (Semi-Auto)]
[reload_mechanic:: Single-load]

Компактная одноручная версия эмиттера с узким конусом и заметно меньшей ценой на теле.

- **Мувсет:** тот же принудительный Stagger, но конус уже и радиус короче — легче удержать угол при выходе из-за укрытия.
- **Implicit:** `stagger_cone` срабатывает надёжнее на близкой дистанции, но слабее толкает несколько целей сразу.
- **Слабость:** заметно ниже урон и радиус охвата, чем у двуручного Эмиттера; всё ещё требует немедленного сближения после выстрела.
- **Отличие:** можно держать одной рукой и дешевле по выносливости, но конус и суммарный урон заметно скромнее Веерного Эмиттера.
