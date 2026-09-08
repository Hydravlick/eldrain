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
consumer_migration: pending
related_files:
  - "[[07_Gear_Inventory/Equipment_PaperDoll]]"
  - "[[05_Combat_Survival/Weapon_Core]]"
  - "[[05_Combat_Survival/Weapon_Ranged]]"
  - "[[05_Combat_Survival/Magic_Batteries]]"
  - "[[04_Player_Entities/Skill_Execution]]"
  - "[[05_Combat_Survival/Combat_Three_Debts]]"
---

# Контракт ввода

Игрок может переназначить Aim с Left Alt на Mouse4 и продолжить прицеливаться тем же способом. Меняется физическая кнопка; возможность оружия прицеливаться, подготовка и решение выстрелить остаются у gameplay owners.

## Ответственность

Input Contract владеет semantic action IDs, default bindings, режимами событий ввода, контекстами, reservation/collision policy и rebinding. Он передаёт намерение соответствующему потребителю:

```text
physical binding
→ semantic input intent
→ gameplay operation
→ Action eligibility / execution
```

Подготовленные Set A/B, hand slots, active Set, фактическая occupancy и физическая перестройка относятся к Weapon Set / [[07_Gear_Inventory/Equipment_PaperDoll|Equipment PaperDoll]]. Эта область не владеет глобальной картой кнопок. Pattern определяет Primary, optional Alt, поддержку Aim и физический смысл подготовки. Допуск и исполнение запроса определяет [[05_Combat_Survival/Combat_Three_Debts#Допуск, claims и release|Action contract]].

Input Contract не выбирает reload recipient, не исполняет Switch Set или Q/E, не хранит hand occupancy, magazine или Heat и не разрешает Commitment/Recovery. `gameplay_owner` в записях ниже указывает место gameplay-ответственности, а не input resolver.

## Схема записей и текущий объём

Один блок третьего уровня содержит одну запись с `action_id`, `default_binding`, `input_mode`, `context`, `gameplay_owner` и `consumer_role`. Поля записаны в Dataview-compatible inline-формате; frontmatter страницы остаётся плоским. Records принадлежат этой странице и не должны повторяться в потребительских документах как другая карта bindings.

Режимы событий:

- `press` — одно явное намерение на нажатие; удержание само по себе не повторяет его.
- `hold` — намерение поддерживается удержанием; отпускание завершает именно это намерение, не создавая выстрел.
- `operation_edges` — нажатие, удержание и отпускание передаются как события одного намерения. Определение операции задаёт, какие из них используются. Этот режим сам не вводит charge, release-fire, autorepeat, tap/hold threshold или дополнительное действие.

В этой версии фиксируются шесть принятых semantic actions и их default bindings. Потребители ещё не мигрированы: разделение channels по конфигурации Weapon Set, конкретные Aim/service operations и старые локальные bindings будут интегрированы отдельным batch. Ссылка на существующий owner не означает, что его прежняя schema уже заменена. Клавиши Switch Set и cantrip здесь не назначаются.

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

### Aim

[action_id:: aim]
[default_binding:: LeftAlt]
[input_mode:: hold]
[context:: gameplay]
[gameplay_owner:: [[05_Combat_Survival/Weapon_Core]]]
[consumer_role:: pattern_aim_operation]

`Aim` — semantic action, `Left Alt` — её default binding. Aim не является Alt или Fire. Поддержку и физику Aim определяет Pattern; отсутствие этой операции не переназначает кнопку на другую.

### Reload

[action_id:: reload]
[default_binding:: R]
[input_mode:: press]
[context:: gameplay]
[gameplay_owner:: [[05_Combat_Survival/Magic_Batteries]]]
[consumer_role:: reload_service_intent]

Запись передаёт reload/service intent. Выбор получателя и транзакция принадлежат gameplay-процедуре; Input Contract их не рассчитывает.

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

## Контексты, reservation и rebinding

`gameplay` означает управление Пешкой при отсутствии перехватывающего UI/text-input контекста. Ввод, принятый сфокусированным интерфейсом или текстовым полем, не должен одновременно уходить в gameplay. Закрытие интерфейса не превращает уже удерживаемую кнопку в новое игровое намерение.

В пересекающихся контекстах одна физическая комбинация не назначается двум независимым semantic actions со скрытым приоритетом. Настройка должна показать конфликт и потребовать его разрешить до принятия mapping. Повторное использование комбинации допустимо в явно взаимоисключающих контекстах; во время события должен быть понятен единственный получатель.

Default `LeftAlt` зарезервирован для `aim` в gameplay. Старое назначение Alt как ability/cantrip modifier требует отдельной миграции потребителя; оно не получает приоритет над этой записью и не должно исполняться вместе с Aim. Новый cantrip binding остаётся открытым. Inventory `Alt+Click` проверяется в своём UI-контексте, а не становится второй combat operation.

Rebinding меняет только физическое назначение и отображаемые подсказки. `action_id`, режим событий и gameplay meaning сохраняются. Замена binding во время удержания не создаёт новое нажатие и не меняет получателя уже начатого намерения.

## Связь намерения с операцией

**Уже начатый или буферизованный semantic input intent остаётся связан с исходной operation/recipient и не переинтерпретируется после изменения Set/context/state.** Gameplay consumer фиксирует эту связь при разрешении исходного запроса; следующие события удержания/отпускания относятся к нему же.

Изменение channel assignment, depletion, потеря Aim support или смена предмета могут сделать исходную операцию невозможной. Тогда применяется её cancel/failure/no-op outcome. Старый input не превращается в новую атаку, выстрел, Aim или Reload; удерживаемая кнопка не запускает операцию предмета новой Set.

```text
press/hold LMB on Set A
→ switch to Set B
→ old input fires Set B weapon: forbidden
```

Отмена намерения не очищает долг уже начатого Action. Его остаток и release принадлежат Action contract. Точные buffering windows, политика повторных запросов и choreography контекстных переходов остаются prototype-bound.
