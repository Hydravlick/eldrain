---
type: registry
status: active
system: player_entities_registry
registry_type: personal_tags
tags: [database, personal_tags, mastery, mutations, relics]
related_files:
  - "[[04_Player_Entities/Tags_System|Personal Tags]]"
  - "[[04_Player_Entities/Trait_Development|Chronicle]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Arsenal and Proficiency]]"
  - "[[04_Player_Entities/Shell_Foundlings|Найдёныши]]"
  - "[[05_Combat_Survival/_Registries/Registry_StatusEffects|Registry Status Effects]]"
  - "[[08_World_Generation/_Registries/Registry_Environment_States|Registry Environment States]]"
---
# Реестр личных тегов

> Реестр хранит механические свойства конкретных Пешек. Биография, Chronicle и Origin Continuation живут рядом, но не маскируются под perks.

## Правила реестра

- У одной Пешки не более трёх Personal Tags; Origin занимает одно обычное место.
- Каждый тег имеет `tag_form:: light | situational`.
- `light` меняет один параметр одного действия или состояния и публикует точное число.
- `situational` использует `trigger -> rule_shift -> tell -> counter/debt` и не даёт отдельную кнопку.
- Тег читает только зарегистрированный сигнал каналов `body`, `action`, `craft` или `environment`.
- `rarity` описывает частоту источника, а не потенциал человека.
- Постоянный скрытый коэффициент не меняет базовый урон, автоматический RPM, полёт импульса или точность.
- Frame-вариант `tag_kind:: mastery` дополнительно публикует один `mastery_frame`, `mastery_step:: 1` и собственную `mastery_expression`. Он всегда combat-facing: два таких тега могут провести базу `0` до нормального `prof 2`, а базу `1` — до `prof 3`. Освоение обычного действия вроде перевязки остаётся action-mastery и не участвует в FrameProf.
- `design_status:: concept` и `prototype` не означают финальную калибровку.

## Шаблон лёгкого тега

```markdown
[id:: template_light_tag]
[tag:: template_light_tag]
[tag_form:: light]
[tag_kind:: first_return|origin|mastery|mutation|scar|relic_imprint]
[source_kind:: first_return|origin|practice|anomaly|relic|breakline]
[source_event:: event_or_item_id]
[rarity:: common]
[owner_domain:: body|action|frame_action|relic_carrier]
[setting_channel:: body|action|craft|environment]
[signal_ref:: registered_signal_id]
[physical_or_action_owner:: owner_id]
[trigger:: persistent_local_condition]
[affected_parameter:: one_local_parameter]
[modifier:: explicit_value_and_unit]
[rule_shift:: none]
[tell_owner:: exact_breakdown_and_sensory_cue]
[tell_observer:: external_cue_if_counter_timing_changes]
[cost_or_debt:: none|time|battery|exposure|injury|route|slot]
[counterplay:: none|named_current_response]
[stack_group:: group_id]
[exclusive_with:: none]
[design_status:: prototype]
```

Для Frame-варианта `tag_kind:: mastery` к любому шаблону обязательны дополнительные поля:

```markdown
[mastery_frame:: frame_id]
[mastery_step:: 1]
[mastery_expression:: named_sidegrade_of_one_frame_phase]
[mastery_expression_phase:: draw|windup|contact|recovery|guard|manual_cycle]
```

`mastery_step` собирается открытой формулой proficiency и не считается вторым ситуационным эффектом. `mastery_expression` остаётся единственным собственным механическим правилом тега и продолжает работать при достижении потолка `prof 3`.

## Шаблон ситуационного тега

```markdown
[id:: template_situational_tag]
[tag:: template_situational_tag]
[tag_form:: situational]
[tag_kind:: first_return|origin|mastery|mutation|scar|relic_imprint]
[source_kind:: first_return|origin|practice|anomaly|relic|breakline]
[source_event:: event_or_item_id]
[rarity:: uncommon]
[owner_domain:: body|action|frame_action|relic_carrier]
[setting_channel:: body|action|craft|environment]
[signal_ref:: registered_signal_id]
[physical_or_action_owner:: owner_id]
[trigger:: visible_condition]
[affected_parameter:: none|one_local_parameter]
[modifier:: none|explicit_value_and_unit]
[rule_shift:: one_automatic_rule]
[tell_owner:: exact_ui_and_sensory_cue]
[tell_observer:: external_sensory_cue]
[cost_or_debt:: time|cargo|battery|exposure|injury|route|slot|none]
[counterplay:: named_current_response]
[stack_group:: group_id]
[exclusive_with:: none]
[design_status:: prototype]
```

## Prototype: Frame-mastery

### Обратная ножевая хватка

**Тултип:** `Короткий рез: мастерство +1. При занятой второй руке Frame можно извлечь обратным хватом. До завершения первого Recovery нельзя поставить блок или сменить предмет.`

[id:: reverse_knife_grip]
[tag:: reverse_knife_grip]
[tag_form:: situational]
[tag_kind:: mastery]
[source_kind:: practice]
[source_event:: survived_close_contact_with_offhand_occupied]
[rarity:: uncommon]
[owner_domain:: frame_action]
[setting_channel:: action]
[signal_ref:: short_cut_1h.draw_with_offhand_occupied]
[physical_or_action_owner:: short_cut_1h.draw]
[mastery_frame:: short_cut_1h]
[mastery_step:: 1]
[mastery_expression:: allow_reverse_grip_draw_while_offhand_occupied_then_lock_guard_and_item_swap_until_first_recovery]
[mastery_expression_phase:: draw]
[trigger:: draw_short_cut_1h_while_offhand_is_occupied]
[affected_parameter:: none]
[modifier:: none]
[rule_shift:: reverse_grip_draw_is_allowed_and_guard_plus_item_swap_remain_locked_until_first_recovery_ends]
[tell_owner:: reverse_grip_icon_and_locked_guard_swap_inputs]
[tell_observer:: visible_reverse_grip_and_committed_first_attack_pose]
[cost_or_debt:: lost_guard_and_item_swap_until_first_recovery]
[counterplay:: force_or_feint_the_committed_first_contact_then_punish_recovery]
[stack_group:: short_cut_1h_draw_expression]
[exclusive_with:: other_short_cut_1h_draw_rewrites]
[design_status:: prototype]

* **Как работает накопление:** для hero-kit с `BaseFrameProf 0` тег открывает полевое владение `1`; второй mastery-тег `short_cut_1h` с другой expression доведёт его до нормального `2`. При базовом `2` этот тег даст мастерство `3`. При базовом `3` уровень не изменится, но обратная хватка останется доступна.
* **Почему это не скрытый бонус:** карточка показывает `база + mastery = итог`, стойка видна в руках, а цена существует в том же коротком обмене.

## Prototype: ситуационная телесная мутация

### Токсичная кровь

[id:: toxic_blood]
[tag:: toxic_blood]
[tag_form:: situational]
[tag_kind:: mutation]
[source_kind:: anomaly]
[source_event:: compatible_toxic_blood_exposure]
[rarity:: rare]
[owner_domain:: body]
[setting_channel:: body]
[signal_ref:: bleed, poison]
[physical_or_action_owner:: circulatory_system]
[trigger:: fresh_penetrating_or_cutting_wound_at_contact_distance]
[affected_parameter:: none]
[modifier:: none]
[rule_shift:: fresh_blood_physically_applies_registered_poison_exposure_to_unsealed_contact_target]
[tell_owner:: darkened_vessels_before_raid_and_visible_toxic_spray_on_trigger]
[tell_observer:: dark_vessels_visible_at_close_range_and_colored_spray_on_wound]
[cost_or_debt:: active_bleed_and_normal_treatment_pressure]
[counterplay:: maintain_distance_or_use_sealed_contact_layer_or_stop_contact_pressure]
[stack_group:: mutation_contact_response]
[exclusive_with:: none]
[design_status:: prototype]

* **Почему это тег:** отдельной атаки нет; сначала тело получает физическую рану, затем изменённая кровь становится источником зарегистрированного `poison`.
* **Почему это не бесплатный навык:** владелец действительно ранен и сохраняет обычную цену Bleed. Противник может не входить в контакт, использовать герметичный слой либо прекратить давление после первого tell.
* **Что не утверждено:** радиус контакта, buildup, длительность poison и допустимые материалы защиты.

## Prototype: лёгкое освоенное свойство

### Выученный перевязочный ритм

[id:: learned_bandage_rhythm]
[tag:: learned_bandage_rhythm]
[tag_form:: light]
[tag_kind:: mastery]
[source_kind:: practice]
[source_event:: completed_field_treatment_practice]
[rarity:: common]
[owner_domain:: action]
[setting_channel:: action]
[signal_ref:: stop_and_bandage]
[physical_or_action_owner:: bandage_commitment]
[trigger:: using_standard_bandage_on_self]
[affected_parameter:: bandage_commitment_time]
[modifier:: TEST_VALUE_seconds]
[rule_shift:: none]
[tell_owner:: final_treatment_time_breakdown_and_distinct_prepared_hand_pose]
[tell_observer:: shortened_hand_sequence_must_remain_animated]
[cost_or_debt:: none]
[counterplay:: punish_the_visible_treatment_commitment]
[stack_group:: personal_treatment_time]
[exclusive_with:: none]
[design_status:: prototype]

* **Граница:** это один явный параметр одного действия, а не Dexterity, которая ускоряет лечение, двери, reload и revive одновременно.
* **Что не утверждено:** величина изменения и правило получения mastery.

## Зарезервированные направления

### Роговой шов

[id:: horn_seam]
[tag:: horn_seam]
[tag_form:: situational]
[tag_kind:: mutation]
[source_kind:: anomaly]
[signal_ref:: pending_registered_body_or_craft_signal]
[design_status:: concept]

Название и телесная фантазия приняты как направление. До `prototype` нужно определить конкретный шов, trigger, физический материал, автоматический ответ, внешний tell и контрмеру. Общий бонус брони или скрытое снижение урона не проходит контракт.

### Жар под кожей

[id:: heat_under_skin]
[tag:: heat_under_skin]
[tag_form:: situational]
[tag_kind:: mutation]
[source_kind:: anomaly]
[setting_channel:: action]
[signal_ref:: stationary_action_state_and_pending_body_heat_rule]
[design_status:: concept]

Принято направление персонажа, для которого неподвижность создаёт телесную проблему и меняет роль привычного оружия. До `prototype` нужно зарегистрировать телесный Heat отдельно от Heat конкретного Frame, определить buildup, вентиляцию движением, внешний tell и последствия. Тег не получает абстрактный урон «за стояние» без материального источника.

## Исключённый старый шаблон

`Trouble -> Leverage -> Residue`, личная цель, адрес, свидетель, спорный груз и Origin Continuation не являются механическими тегами. Они остаются Chronicle/Quest-содержанием. Прототипы, в которых тег фактически создавал квест или цельную активную способность, удалены из этого реестра.

## Проверка записи

Тег не проходит в `approved`, если:

- `signal_ref` не существует в активном реестре или authored action contract;
- `light` не публикует один `affected_parameter` и точный `modifier`;
- `situational` не публикует trigger, rule shift, внешний tell и текущую контрмеру;
- один коэффициент влияет на несколько независимых действий;
- механика требует знания Race, Spec, другого tag ID, rarity или скрытого будущего;
- Origin получает дополнительное место или отдельный силовой пул;
- один tag запускает второй напрямую;
- KIA или отказ от спасённого человека является самым дешёвым рероллом.
