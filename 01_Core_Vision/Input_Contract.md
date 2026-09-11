---
type: system_contract
status: active
system: player_input
canonical_id: INPUT_CONTRACT
owns:
  - input.semantic_actions
  - input.default_bindings
  - input.modes_and_contexts
  - input.reservation_and_rebinding
  - input.intent_binding
index_route: owner
index_group: core_vision
index_order: 50
index_summary: "Определяет semantic input actions, default bindings, контексты и сохранение исходного намерения."
read_when: "Читайте при назначении кнопок, проверке конфликтов ввода, rebinding или передаче намерения gameplay owner."
tags:
  - input
  - bindings
  - intent
binding_schema: inline_action_records
related_files:
  - "[[07_Gear_Inventory/Equipment_PaperDoll]]"
  - "[[05_Combat_Survival/Weapon_Core]]"
  - "[[05_Combat_Survival/Weapon_Ranged]]"
  - "[[05_Combat_Survival/Magic_Batteries]]"
  - "[[04_Player_Entities/Skill_Execution]]"
  - "[[05_Combat_Survival/Combat_Three_Debts]]"
---

# Контракт ввода

Игрок может переназначить Weapon Focus с Left Alt на Mouse4 и продолжить прицеливаться тем же способом. Меняется физическая кнопка; возможность оружия прицеливаться, подготовка и решение выстрелить остаются у gameplay owners.

## Ответственность

Input Contract владеет semantic action IDs, default bindings, режимами событий ввода, контекстами, reservation/collision policy и rebinding. Он передаёт намерение соответствующему потребителю:

```text
physical binding
→ semantic input intent
→ gameplay operation
→ Action eligibility / execution
```

Подготовленные Set A/B, hand slots, active Set, фактическая occupancy и физическая перестройка относятся к Weapon Set / [[07_Gear_Inventory/Equipment_PaperDoll|Equipment PaperDoll]]. Эта область не владеет глобальной картой кнопок. Pattern определяет Primary, optional Alt, поддержку Weapon Focus и физический смысл подготовки. Допуск и исполнение запроса определяет [[05_Combat_Survival/Combat_Three_Debts#Допуск, claims и release|Action contract]].

Input Contract не выбирает reload recipient, не исполняет Switch Set или Q/E, не хранит hand occupancy, magazine или Heat и не разрешает Commitment/Recovery. `gameplay_owner` в записях ниже указывает место gameplay-ответственности, а не input resolver.

## Схема записей и текущий объём

Один блок третьего уровня содержит одну запись с `action_id`, `default_binding`, `input_mode`, `context`, `gameplay_owner` и `consumer_role`. Поля записаны в Dataview-compatible inline-формате; frontmatter страницы остаётся плоским. Records принадлежат этой странице и не должны повторяться в потребительских документах как другая карта bindings.

Режимы событий:

- `press` — одно явное намерение на нажатие; удержание само по себе не повторяет его.
- `hold` — намерение поддерживается удержанием; отпускание завершает именно это намерение, не создавая выстрел.
- `tap_hold` — одна UI invocation: release до threshold означает tap, пересечение threshold — hold; key-down только ожидает различения.
- `operation_edges` — нажатие, удержание и отпускание передаются как события одного намерения. Определение операции задаёт, какие из них используются. Этот режим сам не вводит charge, release-fire, autorepeat, tap/hold threshold или дополнительное действие.

Weapon Set теперь потребляет channels, Weapon Core — Weapon Focus intent; Skill Execution принимает намерения profile actions. Reload направляется в [[05_Combat_Survival/Magic_Batteries|Magic Batteries]] для выбора получателя и запроса service Action; magazine получателя определяет [[05_Combat_Survival/Weapon_Ranged|Weapon Ranged]]. Switch Set получает default Mouse Wheel scroll. Cantrip Variant остаётся с binding TBD; существующий Left Alt для Weapon Focus сохраняется рабочим prototype binding, не окончательным решением эргономики.

### Weapon channel 1

[action_id:: weapon_channel_1]
[default_binding:: LMB]
[input_mode:: operation_edges]
[context:: gameplay]
[gameplay_owner:: [[07_Gear_Inventory/Equipment_PaperDoll]]]
[consumer_role:: weapon_set_channel]

### Weapon channel 2

[action_id:: weapon_channel_2]
[default_binding:: RMB]
[input_mode:: operation_edges]
[context:: gameplay]
[gameplay_owner:: [[07_Gear_Inventory/Equipment_PaperDoll]]]
[consumer_role:: weapon_set_channel]

### Weapon Focus

[action_id:: weapon_focus]
[default_binding:: LeftAlt]
[input_mode:: hold]
[context:: gameplay]
[gameplay_owner:: [[05_Combat_Survival/Weapon_Core]]]
[consumer_role:: pattern_focus_operation]
[binding_status:: prototype_bound]

`Weapon Focus` — semantic action, `Left Alt` — её default binding. Weapon Focus не является Alt или Fire. Поддержку и физику Weapon Focus определяет Pattern; отсутствие этой операции не переназначает кнопку на другую.

### Reload

[action_id:: reload]
[default_binding:: R]
[input_mode:: press]
[context:: gameplay]
[gameplay_owner:: [[05_Combat_Survival/Magic_Batteries]]]
[consumer_role:: reload_service_intent]

Запись передаёт reload/service intent. [[05_Combat_Survival/Magic_Batteries#3. Reload и получатель энергии|Magic Batteries]] выбирает одного eligible recipient активной Set и создаёт service Action request; Input Contract не рассчитывает comparator и не расходует источник. Повтор после завершения является новым намерением с новым выбором получателя. Depletion не создаёт reload вместо weapon channel.

### Profile Q

[action_id:: profile_q]
[default_binding:: Q]
[input_mode:: operation_edges]
[context:: gameplay]
[gameplay_owner:: [[04_Player_Entities/Skill_Execution]]]
[consumer_role:: profile_q_operation]

### Profile E

[action_id:: profile_e]
[default_binding:: E]
[input_mode:: operation_edges]
[context:: gameplay]
[gameplay_owner:: [[04_Player_Entities/Skill_Execution]]]
[consumer_role:: profile_e_operation]

### Switch Weapon Set

[action_id:: switch_weapon_set]
[default_binding:: MouseWheelScroll]
[input_mode:: press]
[context:: gameplay]
[gameplay_owner:: [[07_Gear_Inventory/Equipment_PaperDoll]]]
[consumer_role:: whole_set_transition_request]

Один intentional scroll request меняет Set A на B или B на A. Колесо не выбирает оружие внутри Set. Объединение raw wheel ticks в одно намерение и защита от случайного повторного scroll — input QoL прототипа; очередь не должна неожиданно вернуть только что сменённую Set.

### Cantrip Variant

[action_id:: cantrip_variant]
[default_binding:: TBD]
[input_mode:: hold]
[context:: gameplay]
[gameplay_owner:: [[04_Player_Entities/Skill_Execution]]]
[consumer_role:: latched_cantrip_variant_intent]
[binding_status:: pending_design]

Модификатор выбирает Cantrip operation variant при активации Q/E и фиксирует выбор на всё намерение. Его можно отпустить сразу после активации; дальнейшие hold/release Q/E принадлежат выбранному варианту. Он не активирует способность сам и не заимствует Weapon Focus binding. Поддержка cantrip и цена тела принадлежат gameplay contract. Новый PC/gamepad binding здесь не назначается.

### Player Menu / Inventory

[action_id:: player_menu]
[default_binding:: Tab]
[input_mode:: tap_hold]
[context:: gameplay_or_player_menu]
[gameplay_owner:: [[07_Gear_Inventory/Inventory_QoL]]]
[consumer_role:: menu_invocation]

Одна semantic action доступна при закрытом и открытом player menu. Input различает tap/hold без permanent toggle на key-down; [[07_Gear_Inventory/Inventory_QoL#Player Menu / Inventory|UI owner]] сохраняет persistent/temporary ownership. Threshold остаётся prototype-bound/accessibility setting. Захваченный text input не запускает menu или gameplay одновременно.

## Контексты, reservation и rebinding

`gameplay` означает управление Пешкой при отсутствии перехватывающего UI/text-input контекста. Ввод, принятый сфокусированным интерфейсом или текстовым полем, не должен одновременно уходить в gameplay. Закрытие интерфейса не превращает уже удерживаемую кнопку в новое игровое намерение.

В пересекающихся контекстах одна физическая комбинация не назначается двум независимым semantic actions со скрытым приоритетом. Настройка должна показать конфликт и потребовать его разрешить до принятия mapping. Повторное использование комбинации допустимо в явно взаимоисключающих контекстах; во время события должен быть понятен единственный получатель.

Default `LeftAlt` зарезервирован для `weapon_focus` в gameplay. Прежнее назначение Alt как ability/cantrip modifier — superseded и больше не исполняется в gameplay. Сохраняется `cantrip_variant` с `default_binding: TBD`; он не получает приоритет над Weapon Focus и не запускается вместе с ним. Inventory `Alt+Click` проверяется в своём UI-контексте, а не становится второй combat operation.

Rebinding меняет только физическое назначение и отображаемые подсказки. `action_id`, режим событий и gameplay meaning сохраняются. Замена binding во время удержания не создаёт новое нажатие и не меняет получателя уже начатого намерения.

## Связь намерения с операцией

**Уже начатый или буферизованный semantic input intent остаётся связан с исходной operation/recipient и не переинтерпретируется после изменения Set/context/state.** Gameplay consumer фиксирует эту связь при разрешении исходного запроса; следующие события удержания/отпускания относятся к нему же.

Изменение channel assignment, depletion, потеря Weapon Focus support или смена предмета могут сделать исходную операцию невозможной. Тогда применяется её cancel/failure/no-op outcome. Старый input не превращается в новую атаку, выстрел, Weapon Focus или Reload; удерживаемая кнопка не запускает операцию предмета новой Set.

```text
press/hold LMB on Set A
→ switch to Set B
→ old input fires Set B weapon: forbidden
```

Отмена намерения не очищает долг уже начатого Action. Его остаток и release принадлежат Action contract. Точные buffering windows, политика повторных запросов и choreography контекстных переходов остаются prototype-bound.

## Semantic consumption

```text
binding → semantic intent → operation request → ACTION_EXECUTION eligibility
```

PaperDoll выбирает operation channel по подтверждённой Set и Pattern reference. Weapon Core разрешает Focus operation только единственного weapon owner, поддерживающего её. Control grammar выбирает operation до проверки claims; runtime compatibility не является маршрутизацией кнопки. Ни один из этих шагов не гарантирует исполнение; Input Contract не проверяет руки, не выбирает moveset и не освобождает claims.

Получатель буферизованного weapon intent включает исходные ItemID, operation и Set/revision. При смене контекста новое нажатие разрешается заново; старое удержание не переносится. Один semantic event в одном контексте имеет одного consumer owner. В inventory UI локальный Alt+Click потребляется сфокусированным экраном и не порождает gameplay Weapon Focus.

## Preparation и input barrier

Q/E, Reload и Switch Set явно завершают незавершённую Weapon Focus Preparation по [[05_Combat_Survival/Combat_Three_Debts#Targeting и одна Preparation|Action contract]]. Новый запрос не сохраняет Focus по скрытой совместимости. Q/E самостоятельно выбирают свои target solution и variant.

Switch Set отменяет uncommitted Preparation, затем ожидает ближайшую допустимую Action boundary. Intent хранит исходные operation, recipient и context generation. Raw held LMB/RMB после смены не разрешаются заново против новой Set. То же правило касается ранее удерживаемого Focus; исключение sustained Focus относится только к неотменённому намерению и тому же контексту после legal Recovery.
