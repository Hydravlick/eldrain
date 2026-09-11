---
status: active
system: player_entities_registry
registry_type: personal_tags
tags:
  - database
  - personal_tags
  - mutations
  - relics
related_files:
  - "[[04_Player_Entities/Tags_System|Personal Tags]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Arsenal and Proficiency]]"
  - "[[04_Player_Entities/Shell_Foundlings|Найдёныши]]"
  - "[[05_Combat_Survival/Registries/Registry_StatusEffects|Registry Status Effects]]"
  - "[[08_World_Generation/Registries/Registry_Environment_States|Registry Environment States]]"
type: registry
index_route: owner
index_group: player_entities
index_order: 70
index_summary: "Хранит схему и записи: Реестр личных тегов."
read_when: Когда нужен контракт «Реестр личных тегов» и его границы с соседними владельцами.
---
# Реестр личных тегов

> Реестр хранит механические свойства конкретных Пешек. Биография не образует отдельного runtime-слоя, а Origin Continuation остаётся контрактом Quest Engine; ни то ни другое не маскируется под perks.

## Правила реестра

Реестр хранит Personal Trait definitions и их personal provenance. Deterministic P хранится в Field Profile ([[04_Player_Entities/Registries/Registry_Combos|Registry Combos]]) и использует ту же [[04_Player_Entities/Tags_System#Общая semantic grammar P и Personal Trait|semantic rule grammar]]. Personal acquisition-поля и места не являются требованиями P; отдельного effect engine для P нет.

Пожизненные места, формы, сигналы и ограничения действия определяет [[04_Player_Entities/Tags_System]]; отношение Pawn ↔ Frame определяется [[04_Player_Entities/Proficiency_Arsenal]].

Существующие concept/prototype records используют рабочие `light / situational` и поля соответствующего authoring template. Это не окончательная taxonomy или обязательный closed source catalogue для будущего Trait Grammar. Утверждённые semantic/lifecycle boundaries принадлежат Tags System. `design_status:: concept` и `prototype` не означают финальную калибровку.

Поле `source_kind` не разрешает выдачу свойства; ограничения, включая `breakline`, задаёт [[04_Player_Entities/Tags_System#3. Не дерево и не валюта|Tags System]].

## Рабочий шаблон лёгкого тега (prototype-bound)

```markdown
[id:: template_light_tag]
[tag:: template_light_tag]
[tag_form:: light]
[tag_kind:: first_return|origin|mutation|scar|relic_imprint]
[source_kind:: first_return|origin|practice|anomaly|relic|breakline]
[source_event:: event_or_item_id]
[rarity:: common]
[owner_domain:: body|action|pattern_operation|relic_carrier]
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

Universal Mastery не входит в Trait schema и не превращается автоматически в Personal Trait.

## Рабочий шаблон ситуационного тега (prototype-bound)

```markdown
[id:: template_situational_tag]
[tag:: template_situational_tag]
[tag_form:: situational]
[tag_kind:: first_return|origin|mutation|scar|relic_imprint]
[source_kind:: first_return|origin|practice|anomaly|relic|breakline]
[source_event:: event_or_item_id]
[rarity:: uncommon]
[owner_domain:: body|action|pattern_operation|relic_carrier]
[setting_channel:: body|action|craft|environment]
[signal_ref:: registered_signal_id]
[physical_or_action_owner:: owner_id]
[trigger:: visible_condition]
[affected_parameter:: none|one_local_parameter]
[modifier:: none|explicit_value_and_unit]
[rule_shift:: one_automatic_rule]
[tell_owner:: exact_ui_and_sensory_cue]
[tell_observer:: external_cue_if_immediate_response_changes | not_required]
[cost_or_debt:: time|cargo|battery|exposure|injury|route|slot|none]
[counterplay:: named_current_response | not_applicable_to_private_effect]
[stack_group:: group_id]
[exclusive_with:: none]
[design_status:: prototype]
```

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

`Trouble -> Leverage -> Residue`, личная цель, адрес, свидетель, спорный груз и Origin Continuation не являются механическими тегами. Они остаются Quest-, Trace-, custody- или lifecycle-содержанием у своих владельцев. Прототипы, в которых тег фактически создавал квест или цельную активную способность, удалены из этого реестра.

## Проверка записи

Тег не проходит в `approved`, если:

- `signal_ref` не существует в активном реестре или authored action contract;
- `light` не публикует один `affected_parameter` и точный `modifier`;
- `situational` не публикует условие, rule shift и необходимую информацию участникам; внешний tell и контрмера требуются, когда меняется непосредственный ответ противника;
- один коэффициент влияет на несколько независимых действий;
- механика требует знания Race, Spec, другого tag ID, rarity или скрытого будущего;
- Origin получает дополнительное место или отдельный силовой пул;
- один tag запускает второй напрямую;
- KIA или отказ от спасённого человека является самым дешёвым рероллом.
