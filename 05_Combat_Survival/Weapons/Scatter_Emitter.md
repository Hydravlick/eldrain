---
type: weapon_frame
status: active
system: combat_survival
frame_id: scatter_emitter
display_name: Веерный эмиттер
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on: [charge, cone_release, vent_recovery]
primary_window_function: create
creates_window: [melee_entry]
exploits_window: [none]
mitigates_window: [enemy_entry]
exposure_channels: [heat, short_range, reload_timing, open_line]
frame_power: 3
exposure_weight: 4
mastery_unlock: [cone_discipline]
mvp_verdict: core_support
mvp_reason: "Хорошо показывает Heat и контроль входа, но в одиночку может стать слишком понятным магическим дробовиком."
sort_order: 430
tags: [weapon_frame, weapons, arcanegun]
related_files:
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
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
[implicit:: stagger_cone]
[implicit_rule:: ближний веер создаёт melee_entry и останавливает вход; на средней дистанции эффект распадается в Heat и разброс]
[input_pattern:: tap: pressure pump -> hold: cone release -> recovery: hot vent]
[combo_reset:: после vent_recovery следующий цикл снова начинается с pressure pump]

Выплескивает веер нестабильной энергии. Не про точность, а про остановку входа.

- **Implicit:** `stagger_cone` покупает пространство, но быстро сжигает темп.
- **Слабость:** на средней дистанции урон распадается, Heat копится быстро.
