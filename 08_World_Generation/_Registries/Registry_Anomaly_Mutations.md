---
type: registry
status: active
system: world_generation_registry
registry_type: anomaly_mutations
tags:
  - database
  - anomalies
  - mutation_lines
  - tier_progression
related_files:
  - "[[08_World_Generation/Anomaly/16_Anomaly_Mutation_Lines|Anomaly_Mutation_Lines]]"
  - "[[08_World_Generation/_Registries/Registry_Mobs|Registry_Mobs]]"
  - "[[08_World_Generation/_Registries/Registry_Biomes|Registry_Biomes]]"
---
# Реестр: линии мутаций Аномалий

> **Логика:** инстанс выбирает одну законченную линию при генерации. Phase Shift активирует следующую стадию той же линии. Реестр не хранит балансные числа и не заменяет биом или стандартный пул мобов.

## Чужая вода

[anomaly_family:: foreign_water]
[location_tags:: port]
[standard_ecology:: port_foreign_water]
[active_evolving_lines:: 1]

### Посев

[mutation_line:: foreign_water_sowing]
[location_tags:: port]
[line_function:: reproduction]
[resident_line_name:: Посев]
[line_status:: active]

#### T1 — Носители

[mutation_stage:: foreign_water_sowing_t1]
[tier_expression:: 1]
[inherited_tells:: three_lobed_sacs|sweet_rot|green_film]
[mob_additions:: sackhead]
[base_ecology_effect:: none]
[prefab_state:: seeded_drains]
[weather_state:: none]
[study_output:: recognize_sowing_line]
[production_class:: variant]

#### T2 — Ложная роща

[mutation_stage:: foreign_water_sowing_t2]
[tier_expression:: 2]
[inherited_tells:: three_lobed_sacs|sweet_rot|green_film]
[mob_additions:: rootgrabber]
[base_ecology_effect:: wet_route_growth]
[prefab_state:: false_grove]
[weather_state:: toxic_pollen_pockets]
[study_output:: confirm_spore_weather]
[production_class:: variant]

#### T3 — Споровый дождь

[mutation_stage:: foreign_water_sowing_t3]
[tier_expression:: 3]
[inherited_tells:: three_lobed_sacs|sweet_rot|green_film]
[mob_additions:: shedder]
[base_ecology_effect:: rain_activated_growth]
[prefab_state:: covered_route_windows]
[weather_state:: spore_rain]
[study_output:: read_rain_windows]
[production_class:: set_piece]

### Голодные формы

[mutation_line:: foreign_water_hungry_forms]
[location_tags:: port]
[line_function:: morphogenesis]
[resident_line_name:: Голодные формы]
[line_status:: active]

#### T1 — Прихватыши

[mutation_stage:: foreign_water_hungry_forms_t1]
[tier_expression:: 1]
[inherited_tells:: excess_handles|wet_creak|literal_function]
[mob_additions:: grabber_mimic]
[base_ecology_effect:: none]
[prefab_state:: tagged_small_mimics]
[weather_state:: none]
[study_output:: recognize_hungry_forms]
[production_class:: variant]

#### T2 — Обросшие

[mutation_stage:: foreign_water_hungry_forms_t2]
[tier_expression:: 2]
[inherited_tells:: excess_handles|wet_creak|literal_function]
[mob_additions:: doorgulper]
[mob_variants:: hungry_broodpack|hungry_jawshield|hungry_false_bowl|hungry_second_shell]
[base_ecology_effect:: one_visible_graft]
[eligible_standard_mobs:: drifter|deep_brute|deep_shaman|armored_crab]
[prefab_state:: tagged_large_mimics]
[weather_state:: pre_rain_swelling]
[study_output:: confirm_graft_family]
[production_class:: variant]

#### T3 — Голодный дождь

[mutation_stage:: foreign_water_hungry_forms_t3]
[tier_expression:: 3]
[inherited_tells:: excess_handles|wet_creak|literal_function]
[mob_additions:: houseeater]
[mob_variants:: hungry_broodpack|hungry_jawshield|hungry_false_bowl|hungry_second_shell]
[base_ecology_effect:: rain_activated_grafts]
[eligible_standard_mobs:: drifter|deep_brute|deep_shaman|armored_crab]
[prefab_state:: awakened_mimics]
[weather_state:: hungry_rain]
[study_output:: read_awakening_rhythm]
[production_class:: set_piece]

### Белый ответ

[mutation_line:: foreign_water_white_response]
[location_tags:: port]
[line_function:: defense]
[resident_line_name:: Белый ответ]
[line_status:: active]

#### T1 — Звон воды

[mutation_stage:: foreign_water_white_response_t1]
[tier_expression:: 1]
[inherited_tells:: white_trace|water_chime|withdrawing_condensation]
[mob_additions:: ringer]
[base_ecology_effect:: local_signal_target]
[prefab_state:: finite_local_response]
[weather_state:: none]
[study_output:: recognize_white_response]
[production_class:: state]

#### T2 — Белый след

[mutation_stage:: foreign_water_white_response_t2]
[tier_expression:: 2]
[inherited_tells:: white_trace|water_chime|withdrawing_condensation]
[mob_additions:: white_runner]
[base_ecology_effect:: tolerance_or_redirectable_mark]
[prefab_state:: open_ordinary_doors_and_release]
[weather_state:: warm_condensation]
[study_output:: redirect_local_response]
[production_class:: state]

#### T3 — Белая лихорадка

[mutation_stage:: foreign_water_white_response_t3]
[tier_expression:: 3]
[inherited_tells:: white_trace|water_chime|withdrawing_condensation]
[mob_additions:: licker]
[base_ecology_effect:: bounded_linked_response]
[prefab_state:: linked_finite_response]
[weather_state:: white_fever_fog]
[study_output:: read_and_redirect_signal]
[production_class:: set_piece]

## Шаблон новой линии

```text
[mutation_line:: family_line]
[line_function:: fiction_only]
[resident_line_name:: Народное название]
[line_status:: proposal]

[mutation_stage:: family_line_t1]
[tier_expression:: 1]
[inherited_tells:: visual|sound|behavior]
[mob_additions:: mob_id]
[base_ecology_effect:: bounded_behavior]
[prefab_state:: prepared_state]
[weather_state:: state_or_none]
[study_output:: player_knowledge]
[production_class:: state_or_variant_or_set_piece]
```
