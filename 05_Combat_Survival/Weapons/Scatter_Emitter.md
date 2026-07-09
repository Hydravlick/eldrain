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
implicit_keyword: stagger_cone
implicit_rule: "Ближний веер создаёт melee_entry и останавливает вход; на средней дистанции эффект распадается в Heat и разброс."
mastery_unlock: [cone_discipline]
mvp_verdict: core_support
mvp_reason: "Хорошо показывает Heat и контроль входа, но в одиночку может стать слишком понятным магическим дробовиком."
sort_order: 430
tags: [weapon_frame, weapons, arcanegun]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
---
# Веерный эмиттер

Веерный эмиттер останавливает вход и открывает ближнее окно, но платит короткой дистанцией, Heat и потерей темпа после выпуска.

## Варианты

### Веерный Эмиттер (Scatter Emitter) [2H]
[variant_id:: scatter_emitter] | [tier:: 1] | [weight:: 3.8kg] | [dmg:: 10x6] | [impulse_cost:: 1] | [charge_time:: 0.4s] | [heat:: 50] | [bloom:: high] | [dissonance_pulse:: 5] | [setting_status:: mvp]
[fire_input:: Hold: pressure pump / Release: cone burst] | [reload_mechanic:: hot vent]
[combo_reset:: после vent_recovery следующий цикл снова начинается с pressure pump]

*Выплескивает веер нестабильной энергии. Не про точность, а про остановку входа.*
- **Отличие:** базовый контроль входа и быстрый Heat.
- **Implicit:** `stagger_cone` покупает пространство, но быстро сжигает темп.
- **Слабость:** на средней дистанции урон распадается.

### Решётчатый плеватель (Grate Spitter) [2H]
[variant_id:: grate_spitter] | [tier:: 1] | [weight:: 3.1kg] | [dmg:: 8x7] | [impulse_cost:: 1] | [charge_time:: 0.3s] | [heat:: 60] | [bloom:: very_high] | [dissonance_pulse:: 4] | [setting_status:: prototype]
[fire_input:: Tap: dirty cone / Hold: unsafe spread] | [reload_mechanic:: grate clear]
[combo_reset:: перегрев возвращает цикл к dirty cone]

*Кустарный эмиттер с плохой решёткой рассеивания.*
- **Отличие:** дешевле и шире, но хуже контролирует форму конуса.
- **Implicit:** `stagger_cone` больше про панику входа, чем про урон.
- **Слабость:** быстро засоряется и почти не работает дальше ближней дистанции.

### Напорный мех (Pressure Bellows) [2H]
[variant_id:: pressure_bellows] | [tier:: 2] | [weight:: 4.4kg] | [dmg:: 12x6] | [impulse_cost:: 1] | [charge_time:: 0.5s] | [heat:: 42] | [bloom:: high] | [dissonance_pulse:: 6] | [setting_status:: prototype]
[fire_input:: Hold: build pressure / Release: shaped cone] | [reload_mechanic:: bellows vent]
[combo_reset:: vent cycle возвращает цикл к build pressure]

*Более дисциплинированный эмиттер для удержания дверей и лестниц.*
- **Отличие:** лучше повторяет контроль входа, но тяжелее и заметнее.
- **Implicit:** `stagger_cone` становится инструментом команды.
- **Слабость:** всё ещё просит короткую дистанцию.
