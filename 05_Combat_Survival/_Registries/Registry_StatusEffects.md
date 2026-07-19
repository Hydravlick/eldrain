---
type: registry
status: active
system: combat_survival_registry
registry_type: status_effects
tags: [database, combat, effects, windows]
related_files:
  - "[[05_Combat_Survival/Status_Effects|Status_Effects]]"
  - "[[05_Combat_Survival/Combat_Three_Debts|Combat_Three_Debts]]"
  - "[[08_World_Generation/_Registries/Registry_Environment_States|Registry Environment States]]"
---
# Реестр: Статусные Эффекты

## Контракт Записи

```markdown
[effect_id:: template_effect]
[effect_category:: injury|condition|control|exposure|mental]
[condition_family:: none | contamination]
[contaminant_source:: none | source_id]
[ingress_paths:: none | inhalation | contaminated_wound | ingestion]
[ingress_amplifier:: none | active_bleed]
[application_mode:: threshold|buildup|direct|reaction]
[primary_window_function:: create|exploit|mitigate]
[creates_window:: none]
[exploits_window:: none]
[mitigates_window:: none]
[control_family:: none]
[combat_role:: interrupt | pressure | attrition | self_debt]
[conflict_group:: none | action_control | restoration_interference]
[repeat_rule:: unique|refresh|intensity|independent|diminishing]
[counter_action:: none]
[persistence:: action|encounter|raid|life]
[telegraph:: none]
[failure_feedback:: none]
[field_capacity_loss:: none | rule_id]
[balance_state:: prototype]
```

`field_capacity_loss` объявляется только для тяжёлой травмы, среды или другого читаемого последствия; обычный урон не получает его автоматически. `balance_state:: prototype` означает, что числовая длительность, buildup и сила эффекта проверяются в прототипе. Поведение окна, контригра и repeat rule уже являются каноном.

## Бюджет статуса: не геройский шутер

Статус — читаемое последствие попадания, ошибки или добровольно принятого долга. Он не должен превращать одну способность в самостоятельную победу над другой Пешкой. Каждая запись выбирает один главный `combat_role`:

- `interrupt` — мгновенный исход для уже `interruptible` действия, а не удерживаемый статус; он быстро возвращает управление и не гарантирует последующее попадание;
- `pressure` меняет один ближайший выбор: позицию, лечение, линию или ответ на источник; он не является жёстким контролем;
- `attrition` может остаться до конца рейда, но не лишает базового движения, прицеливания или доступа к оружию/утилитам; это цена лечения, снаряжения, маршрута или извлечения;
- `self_debt` — добровольная цена собственной опасной процедуры, а не эффект, который враг навязывает цели.

Одна запись не совмещает жёсткий контроль, высокий урон, запрет лечения и долговременное ухудшение. `action_control` допускает один полный эффект за раз: следующий эффект той же группы превращается в читаемый срыв действия либо не усиливает текущее ограничение. `restoration_interference` также не складывает несколько полных правил: активным остаётся одно объявленное правило восстановления, а другой источник лишь обновляет телеграф или заменяет его по заранее указанному приоритету.

Постоянное или рейдовое последствие не должно быть наградой за удачный PvP-hit. Потеря `FieldCapacity` допустима только как медленно читаемый итог тяжёлой травмы, медицинской ошибки или конкретной среды — никогда как скрытый множитель урона в активной перестрелке.

## Граница глобального статуса

Этот реестр хранит последствия, которые читаются одинаково в нескольких мирах: травму тела, контроль, телесную экспозицию, восстановление и ментальное давление. Локальный след, метка среды, состояние префаба или погодного инстанса сюда не попадает: он принадлежит [[08_World_Generation/_Registries/Registry_Environment_States|реестру средовых состояний]].

Статус может быть условием средового инстанса, но не образует с ним автоматическую реакцию. Конкретный инстанс публикует свой источник, телеграф, последствие и путь отказа.

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
[combat_role:: attrition]
[conflict_group:: none]
[repeat_rule:: independent]
[counter_action:: stop_and_bandage]
[persistence:: raid]
[telegraph:: visible_wound, blood_trace, strained_breath]
[failure_feedback:: renewed_bleeding_on_exertion]
[balance_state:: prototype]

Открытая рана создаёт цену лечения и заметный след, но не делает цель бесплатной добычей. Бинт занимает руки и время; отдельные раны имеют собственные источники. Движение может сделать след заметнее, но не превращает рану в автоматическую боевую казнь.

### Увечье
[effect_id:: cripple]
[effect_category:: injury]
[application_mode:: threshold]
[primary_window_function:: create]
[creates_window:: route_limited]
[exploits_window:: none]
[mitigates_window:: none]
[control_family:: none]
[combat_role:: attrition]
[conflict_group:: none]
[repeat_rule:: unique]
[counter_action:: brace_or_splint]
[persistence:: raid]
[telegraph:: failed_step, limb_pose, pain_response]
[failure_feedback:: route_action_refused]
[balance_state:: prototype]

Повреждённая нога или привод делает дорогими спринт, прыжок и вертикальный маршрут, но не отбирает у цели базовое движение и возможность стрелять. Шина либо поддерживающая способность возвращает ограниченную функцию ценой рук, времени или предмета.

### Кантрипное Напряжение
[effect_id:: cantrip_strain]
[effect_category:: injury]
[application_mode:: direct]
[primary_window_function:: create]
[creates_window:: body_debt]
[exploits_window:: none]
[mitigates_window:: none]
[control_family:: cantrip_body_debt]
[combat_role:: self_debt]
[conflict_group:: none]
[repeat_rule:: intensity]
[counter_action:: hub_rest_or_treatment]
[persistence:: raid]
[stages:: clear, strained, scarred, broken]
[telegraph:: conductor_specific_body_tell, ability_preview]
[failure_feedback:: permanent_scar_or_function_failure]
[balance_state:: prototype]

Первое применение переводит Пешку из `Clear` в `Strained`. Повтор до лечения создаёт постоянный Scar tag из допустимого семейства проводника и переводит острое состояние в `Scarred`. Дальнейшая перегрузка создаёт `Broken`: связанная функция отказывает, Пешка теряет сознание либо погибает по контракту способности. Все кантрипы одной Пешки используют эту запись совместно.

## Контроль

### Потеря устойчивости
[effect_id:: stagger]
[effect_category:: condition]
[condition_family:: none]
[contaminant_source:: none]
[ingress_paths:: none]
[ingress_amplifier:: none]
[application_mode:: direct]
[primary_window_function:: create]
[creates_window:: weapon_settle_delayed]
[exploits_window:: none]
[mitigates_window:: none]
[control_family:: none]
[combat_role:: pressure]
[conflict_group:: none]
[repeat_rule:: diminishing]
[counter_action:: cover_and_reset_stance]
[persistence:: action]
[telegraph:: head_impact, posture_break, audio_drop]
[failure_feedback:: posture_recovery_and_weapon_settle]
[balance_state:: prototype]

Тяжёлый удар на короткое время нарушает устойчивость: после движения или разворота оружию дольше вернуться в собранное состояние. Пешка сохраняет камеру, движение, выстрел и доступ к действиям; эффект не отменяет уже начатое действие и не создаёт бесплатное окно убийства.

### Ослепление
[effect_id:: blind]
[effect_category:: control]
[condition_family:: none]
[contaminant_source:: none]
[ingress_paths:: none]
[ingress_amplifier:: none]
[application_mode:: direct]
[primary_window_function:: create]
[creates_window:: long_range_reading_limited]
[exploits_window:: distance_dependence]
[mitigates_window:: close_reading]
[control_family:: none]
[combat_role:: pressure]
[conflict_group:: none]
[repeat_rule:: diminishing]
[counter_action:: close_distance_or_cleanse]
[persistence:: encounter]
[telegraph:: flash_or_material_splash]
[failure_feedback:: reading_range_return]
[balance_state:: prototype]

Blind ограничивает дальность надёжного чтения как личный туман: вблизи видны тело, оружие и направление угрозы, а за границей теряются детали, силуэты и уверенное опознание. Он не выключает экран, не уводит камеру и не создаёт ложных целей. Источник определяет световую, грязевую или эфирную форму.

### Разрыв Канала
[effect_id:: silence]
[effect_category:: control]
[condition_family:: none]
[contaminant_source:: none]
[ingress_paths:: none]
[ingress_amplifier:: none]
[application_mode:: direct]
[primary_window_function:: create]
[creates_window:: interruptible_skills_locked]
[exploits_window:: active_terminal]
[mitigates_window:: weapon_or_body_action]
[control_family:: skill_lock]
[combat_role:: pressure]
[conflict_group:: action_control]
[repeat_rule:: diminishing]
[counter_action:: break_source | leave_field | break_tether]
[persistence:: encounter]
[telegraph:: circuit_dropout, muted_harmonics]
[failure_feedback:: channel_reconnect]
[balance_state:: prototype]

Silence на большее время блокирует новое применение только тех P/Q/E, что явно объявлены `[interrupt_rule:: interruptible]`. Оружие, предметы, телесные действия и независимые устройства остаются доступными. Направленный источник, tether, зона и аура допустимы как разные способы доставки, но каждый обязан показать свою линию, границу либо носитель и собственный путь выхода.

## Контаминация

`contamination` — семейство веществ, которые попадают в тело лишь через объявленный физический путь. Это не payload к любому bleed: активная рана может ускорить контакт с веществом, но не создаёт вещество и не даёт атакующему новый эффект без его источника.

### Отравление
[effect_id:: poison]
[effect_category:: condition]
[condition_family:: contamination]
[contaminant_source:: declared_reagent]
[ingress_paths:: inhalation | contaminated_wound | ingestion]
[ingress_amplifier:: active_bleed]
[application_mode:: buildup]
[primary_window_function:: create]
[creates_window:: decontamination_pressure]
[exploits_window:: declared_ingress_path]
[mitigates_window:: none]
[control_family:: none]
[combat_role:: attrition]
[conflict_group:: none]
[repeat_rule:: intensity]
[counter_action:: antidote_or_decontaminate]
[persistence:: raid]
[telegraph:: altered_breath, skin_color, contaminated_material]
[failure_feedback:: worsening_or_stabilization]
[balance_state:: prototype]

Яд требует объявленного реагента и его пути в тело. Он создаёт медицинское давление и необходимость очистки, но не получает универсальный true damage и не становится автоматическим следствием любого ранения.

### Заражение Спорами
[effect_id:: spore_growth]
[effect_category:: condition]
[condition_family:: contamination]
[contaminant_source:: port_spore_rain]
[ingress_paths:: inhalation | contaminated_wound]
[ingress_amplifier:: active_bleed]
[application_mode:: buildup]
[primary_window_function:: create]
[creates_window:: integrity_reduced, treatment_pressure]
[exploits_window:: unsealed_breathing]
[mitigates_window:: none]
[control_family:: none]
[combat_role:: attrition]
[conflict_group:: none]
[repeat_rule:: intensity]
[counter_action:: filter_purge_or_medical_service]
[persistence:: raid]
[telegraph:: coughing, visible_spores, filter_alarm]
[failure_feedback:: breathing_failure_or_purge]
[field_capacity_loss:: spore_capacity_steps]
[balance_state:: prototype]

Споры — отсроченное медицинское последствие контакта со споровым дождём, а не боевой debuff площади. Незащищённое дыхание и открытая рана — разные пути; `active_bleed` лишь ускоряет второй, но не накладывает заражение с первого попадания. Споры снижают доступную целостность или функцию дыхания ступенями, читаемыми через тело и фильтр. Тяжёлое заражение требует редкого полевого средства или сервиса Хаба.

## Восстановление и его срыв

### Подавление восстановления
[effect_id:: healing_suppression]
[effect_category:: condition]
[application_mode:: direct]
[primary_window_function:: exploit]
[creates_window:: restore_weakened]
[exploits_window:: active_restore]
[mitigates_window:: none]
[control_family:: none]
[combat_role:: pressure]
[conflict_group:: restoration_interference]
[repeat_rule:: diminishing]
[counter_action:: break_source_or_reposition]
[persistence:: encounter]
[telegraph:: disrupted_conduit, uneven_restore_pulse]
[failure_feedback:: reduced_restore_with_visible_loss]
[field_capacity_loss:: none]
[balance_state:: prototype]

Снижает входящее восстановление `CurrentHP`, но не запрещает лечение полностью, не уменьшает `FieldCapacity` и не выключает медицинский предмет без отдельного правила.

### Дробление восстановления
[effect_id:: restoration_fracture]
[effect_category:: condition]
[application_mode:: reaction]
[primary_window_function:: exploit]
[creates_window:: delayed_restore]
[exploits_window:: active_restore]
[mitigates_window:: none]
[control_family:: none]
[combat_role:: pressure]
[conflict_group:: restoration_interference]
[repeat_rule:: diminishing]
[counter_action:: hold_line_or_clear_conduit]
[persistence:: encounter]
[telegraph:: split_restore_shards, interrupted_body_pattern]
[failure_feedback:: restore_arrives_in_delayed_parts]
[field_capacity_loss:: none]
[balance_state:: prototype]

Не уничтожает заявленный heal, а дробит его на читаемые отложенные части. Цель должна пережить интервалы, а лекарь — удержать линию/поле; это создаёт окно фокуса без обязательного абсолютного antiheal.

### Насыщение восстановления
[effect_id:: restore_saturation]
[effect_category:: condition]
[application_mode:: direct]
[primary_window_function:: mitigate]
[creates_window:: repeat_restore_reduced]
[exploits_window:: none]
[mitigates_window:: none]
[control_family:: none]
[combat_role:: pressure]
[conflict_group:: restoration_interference]
[repeat_rule:: diminishing]
[counter_action:: wait_or_change_response]
[persistence:: encounter]
[telegraph:: fading_restore_mark]
[failure_feedback:: next_restore_weakened_or_stabilizing]
[field_capacity_loss:: none]
[balance_state:: prototype]

Общее состояние цели после батарейного восстановления. Повторный heal от любого источника не складывается в полную силу: он ослабляется либо выполняет только заранее объявленную стабилизацию. Смена лекаря не сбрасывает насыщение.

## Среда не является таблицей реакций

Нет глобальной таблицы, где две иконки автоматически создают третий эффект. Контаминация требует объявленный источник и честный путь в тело — открытую заражённую рану, дыхание или иной физический доступ, — но это правило применения конкретной среды или реагента, а не комбинация иконок.

Средовой инстанс может читать один глобальный статус либо собственное `local_state_id` и менять одну локальную ситуацию: маршрут, видимость, поведение врага, работу устройства или доступ к префабу. Его контракт хранится в [[08_World_Generation/_Registries/Registry_Environment_States|реестре средовых состояний]].
