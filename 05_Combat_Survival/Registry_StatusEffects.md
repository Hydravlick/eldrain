---
type: registry
status: active
system: combat_survival_registry
registry_type: status_effects
tags: [database, combat, effects, windows]
related_files:
  - "[[05_Combat_Survival/Status_Effects|Status_Effects]]"
  - "[[05_Combat_Survival/Combat_Three_Debts|Combat_Three_Debts]]"
---
# Реестр: Статусные Эффекты

## Контракт Записи

```markdown
[effect_id:: template_effect]
[effect_category:: injury|condition|control|exposure|mental]
[application_mode:: threshold|buildup|direct|reaction]
[primary_window_function:: create|exploit|mitigate]
[creates_window:: none]
[exploits_window:: none]
[mitigates_window:: none]
[control_family:: none]
[repeat_rule:: unique|refresh|intensity|independent|diminishing]
[counter_action:: none]
[persistence:: action|encounter|raid]
[telegraph:: none]
[failure_feedback:: none]
[balance_state:: prototype]
```

`balance_state:: prototype` означает, что числовая длительность, buildup и сила эффекта проверяются в прототипе. Поведение окна, контригра и repeat rule уже являются каноном.

## Физические Травмы

### Кровотечение
[effect_id:: bleed]
[effect_category:: injury]
[application_mode:: threshold]
[primary_window_function:: create]
[creates_window:: treatment_pressure]
[exploits_window:: movement_commitment]
[mitigates_window:: passive_recovery]
[control_family:: none]
[repeat_rule:: independent]
[counter_action:: stop_and_bandage]
[persistence:: raid]
[telegraph:: visible_wound, blood_trace, strained_breath]
[failure_feedback:: renewed_bleeding_on_exertion]
[balance_state:: prototype]

Открытая рана создаёт выбор между движением и лечением. Рывок, тяжёлое действие и повторный контакт усиливают давление конкретной раны. Бинт занимает руки и время; отдельные раны имеют собственные источники.

### Увечье
[effect_id:: cripple]
[effect_category:: injury]
[application_mode:: threshold]
[primary_window_function:: create]
[creates_window:: route_limited]
[exploits_window:: none]
[mitigates_window:: none]
[control_family:: movement_impair]
[repeat_rule:: unique]
[counter_action:: brace_or_splint]
[persistence:: raid]
[telegraph:: failed_step, limb_pose, pain_response]
[failure_feedback:: route_action_refused]
[balance_state:: prototype]

Повреждённая нога или привод ухудшает спринт, прыжок и вертикальные маршруты. Шина либо поддерживающая способность возвращает ограниченную функцию ценой рук, времени или предмета.

## Контроль

### Оглушение
[effect_id:: stun]
[effect_category:: control]
[application_mode:: direct]
[primary_window_function:: create]
[creates_window:: action_interrupted]
[exploits_window:: exposed_commitment]
[mitigates_window:: none]
[control_family:: hard_interrupt]
[repeat_rule:: diminishing]
[counter_action:: resilience_and_spacing]
[persistence:: action]
[telegraph:: head_impact, posture_break, audio_drop]
[failure_feedback:: interrupted_action_and_control_return]
[balance_state:: prototype]

Первое успешное оглушение создаёт короткое полное окно. Повтор той же control-family сокращается, затем оставляет только interrupt. Полная длительность не обновляется бесконечно.

### Ослепление
[effect_id:: blind]
[effect_category:: control]
[application_mode:: direct]
[primary_window_function:: create]
[creates_window:: vision_disrupted]
[exploits_window:: exposed_angle]
[mitigates_window:: target_lock]
[control_family:: sensory_disrupt]
[repeat_rule:: diminishing]
[counter_action:: cover_and_cleanse]
[persistence:: encounter]
[telegraph:: flash_or_material_splash]
[failure_feedback:: partial_vision_return]
[balance_state:: prototype]

Эффект ухудшает контраст, дальнее чтение и необязательные метки, но не удаляет критический HUD и весь экран. Источник определяет световую, грязевую или эфирную форму.

### Разрыв Канала
[effect_id:: silence]
[effect_category:: control]
[application_mode:: direct]
[primary_window_function:: create]
[creates_window:: casting_blocked]
[exploits_window:: prepared_cast]
[mitigates_window:: aether_channel]
[control_family:: channel_disrupt]
[repeat_rule:: diminishing]
[counter_action:: break_source_or_use_weapon]
[persistence:: encounter]
[telegraph:: circuit_dropout, muted_harmonics]
[failure_feedback:: channel_reconnect]
[balance_state:: prototype]

Silence блокирует указанный эфирный или device-канал, а не все Q/E без разбора. Оружие, телесные действия и явно независимые механические устройства остаются доступными.

## Conditions

### Промокание
[effect_id:: wet]
[effect_category:: condition]
[application_mode:: direct]
[primary_window_function:: create]
[creates_window:: conductive_state]
[exploits_window:: burn_exposure]
[mitigates_window:: burn_persistence]
[control_family:: none]
[repeat_rule:: refresh]
[counter_action:: leave_water_and_dry]
[persistence:: encounter]
[telegraph:: soaked_material, dripping, heavy_cloth]
[failure_feedback:: visible_drying]
[balance_state:: prototype]

Wet гасит или ослабляет часть тепловых состояний, но готовит проводящую реакцию и утяжеляет мягкие слои. Он не даёт автоматический процентный множитель урона.

## Exposures

### Ожог
[effect_id:: burn]
[effect_category:: exposure]
[application_mode:: buildup]
[primary_window_function:: create]
[creates_window:: treatment_pressure, route_denied]
[exploits_window:: dry_material]
[mitigates_window:: healing_window]
[control_family:: panic_pressure]
[repeat_rule:: refresh]
[counter_action:: smother_or_water]
[persistence:: encounter]
[telegraph:: heat_haze, smoke, glowing_material]
[failure_feedback:: flame_reduction_and_steam]
[balance_state:: prototype]

Burn вынуждает тушить материал, уходить в воду или принимать продолжающееся давление. Он не требует универсального переката и не удаляет управление у игрока.

### Шок
[effect_id:: shock]
[effect_category:: exposure]
[application_mode:: buildup]
[primary_window_function:: create]
[creates_window:: action_interrupt]
[exploits_window:: conductive_state]
[mitigates_window:: none]
[control_family:: micro_interrupt]
[repeat_rule:: diminishing]
[counter_action:: leave_conductor_or_insulate]
[persistence:: encounter]
[telegraph:: charge_buildup, muscle_tension, material_sparks]
[failure_feedback:: interrupt_and_grounding]
[balance_state:: prototype]

Shock срывает подготовленное действие и временно ухудшает восстановление стамины или стабильности контура. На Wet-поверхности он может создать электрифицированный участок и цепную реакцию без автоматического удвоения урона.

### Коррозия
[effect_id:: corrosion]
[effect_category:: exposure]
[application_mode:: buildup]
[primary_window_function:: create]
[creates_window:: plate_edge_exposed, soft_zone_exposed]
[exploits_window:: damaged_material]
[mitigates_window:: none]
[control_family:: none]
[repeat_rule:: intensity]
[counter_action:: neutralize_and_reposition]
[persistence:: raid]
[telegraph:: bubbling_surface, discoloration, failing_fastener]
[failure_feedback:: material_failure_or_neutralization]
[balance_state:: prototype]

Corrosion действует на конкретный материал, крепление, край пластины или мягкий слой. Она не уменьшает единый Armor Score всего тела.

### Отравление
[effect_id:: poison]
[effect_category:: exposure]
[application_mode:: buildup]
[primary_window_function:: create]
[creates_window:: treatment_pressure]
[exploits_window:: open_wound, inhalation_path]
[mitigates_window:: none]
[control_family:: none]
[repeat_rule:: intensity]
[counter_action:: antidote_or_decontaminate]
[persistence:: raid]
[telegraph:: altered_breath, skin_color, contaminated_material]
[failure_feedback:: worsening_or_stabilization]
[balance_state:: prototype]

Яд должен попасть через рану, дыхание или другой физический путь. Он создаёт длительное давление лечения, но не получает универсальный true damage вне условий конкретного вещества.

### Заражение Спорами
[effect_id:: spore_growth]
[effect_category:: exposure]
[application_mode:: buildup]
[primary_window_function:: create]
[creates_window:: integrity_reduced, treatment_pressure]
[exploits_window:: unsealed_breathing]
[mitigates_window:: none]
[control_family:: none]
[repeat_rule:: intensity]
[counter_action:: filter_purge_or_medical_service]
[persistence:: raid]
[telegraph:: coughing, visible_spores, filter_alarm]
[failure_feedback:: breathing_failure_or_purge]
[balance_state:: prototype]

Споры снижают доступную целостность или функцию дыхания ступенями, читаемыми через тело и фильтр. Тяжёлое заражение требует редкого полевого средства или сервиса Хаба.

## Mental

### Стресс
[effect_id:: stress]
[effect_category:: mental]
[application_mode:: buildup]
[primary_window_function:: create]
[creates_window:: perception_uncertain]
[exploits_window:: traumatic_event]
[mitigates_window:: none]
[control_family:: sensory_disrupt]
[repeat_rule:: intensity]
[counter_action:: safe_light_rest_or_incense]
[persistence:: raid]
[telegraph:: breathing_shift, peripheral_noise, body_tremor]
[failure_feedback:: false_signal_or_recovery]
[balance_state:: prototype]

Stress искажает интерпретацию звука и периферии, но не создаёт ложные системные маркеры, не меняет Friendly Fire и не делает настоящий сигнал неотличимым без возможности проверки.

## Реакции

| Condition | Trigger | Result Window |
|:---|:---|:---|
| `wet` | `shock` | `action_interrupt`, electrified area |
| `wet` | thermal mitigation | steam concealment, reduced burn |
| `oil` | thermal trigger | persistent route denial |
| `gas` | thermal trigger | telegraphed blast window |
| `bleed` | poison exposure | accelerated buildup through open wound |

Числовая сила каждой реакции проверяется отдельно; совпадение тегов не выдаёт автоматический множитель.
