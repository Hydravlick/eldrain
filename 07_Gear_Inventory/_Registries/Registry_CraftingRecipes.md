---
type: registry
status: active
system: gear_inventory_registry
registry_type: crafting
tags: [database, economy, recipe_transaction, blueprints, variant_ingredient]
related_files:
  - "[[06_Economy_Loot/Barter_System|Barter_System]]"
  - "[[06_Economy_Loot/Blueprints|Blueprints]]"
  - "[[06_Economy_Loot/Craft_Modifiers|Craft_Modifiers]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Blueprints|Registry_Blueprints]]"
---
# Реестр: Адресные RecipeTransaction

## 1. Ответственность и обещание

Этот реестр является единственным источником конкретных мирных сделок. Универсальный цикл принадлежит [[06_Economy_Loot/Barter_System|адресному бартеру]], limited-носители — [[06_Economy_Loot/Blueprints|чертежам]], а правило одного фиксированного варианта — [[06_Economy_Loot/Craft_Modifiers|вариантному ингредиенту]].

Игрок видит точный результат до подтверждения. Сделка не перебрасывает найденные Affix, не повышает Rarity универсальным материалом и не превращает полевую станцию в безопасный магазин внутри Аномалии.

## 2. Рабочий цикл записи

```text
available address
  + matching extracted multiset
  + zero or one fixed variant
  + limited blueprint when required
  -> exact preview
  -> atomic confirmation
  -> provenance-preserving result
```

## 3. Активный контракт

```text
recipe_id
address_id
address_class: central | stable_external
availability: permanent | stable_cycle
inputs
source_rule: raid_extracted | resolved_provenance
optional_variant: zero_or_one | none
blueprint_id: limited | none
service_cost
exact_outcome
provenance_result
balance_state
```

- `address_id` должен существовать в [[08_World_Generation/_Registries/Registry_POIs|Registry_POIs]];
- `availability` наследует срок адреса, а не создаёт собственное короткое окно;
- `inputs` хранит теги/ID и мультимножество количеств;
- `source_rule` не позволяет купить товар в центре и превратить его в прибыльный ресурсный вход;
- `optional_variant` допускает максимум один объявленный ингредиент с фиксированным свойством;
- `blueprint_id` используется только редкой limited-схемой;
- `exact_outcome` является одним известным результатом, без случайной ветви Affix или Corruption;
- `provenance_result` сохраняет источник значимых входов, адрес и Stable-цикл;
- `balance_state` остаётся `unknown`, пока курс не проверен в полной экономике.

## 4. Центральный публичный пример

### Базовый фильтр из извлечённой среды

[recipe_id:: central_basic_filter_service]
[address_id:: central_common_stores]
[address_class:: central]
[availability:: permanent]
[inputs:: multiset(filter_medium, cloth)]
[source_rule:: raid_extracted]
[optional_variant:: none]
[blueprint_id:: none]
[service_cost:: central_basic_service]
[exact_outcome:: basic_filter]
[provenance_result:: processed_at(central_common_stores); preserve_input_manifests]
[balance_state:: unknown]

Публичная сделка поддерживает следующий выход и не требует редкого знания. Точные количества и стоимость не фиксируются до калибровки.

## 5. Внешний sidegrade-шаблон

### Профильная обработка Pattern

[recipe_id:: template_stable_pattern_sidegrade]
[address_id:: stable_mechanic_service]
[address_class:: stable_external]
[availability:: stable_cycle]
[inputs:: multiset(base_pattern, compatible_raid_material)]
[source_rule:: raid_extracted]
[optional_variant:: zero_or_one]
[blueprint_id:: limited|none]
[service_cost:: address_specific_service]
[exact_outcome:: named_pattern_sidegrade]
[provenance_result:: processed_at(stable_mechanic_service); preserve_input_manifests]
[balance_state:: unknown]

- **Базовый выход:** фиксированный sidegrade с объявленной сильной ситуацией и tradeoff.
- **Вариант:** при наличии совместимого ингредиента меняет одно заранее названное свойство результата.
- **Граница:** не перебрасывает Affix базового экземпляра и не создаёт лучший универсальный Tier.
- **Player-facing reason:** уцелевший внешний мастер и оборудование способны выполнить именно эту обработку.

## 6. Исключения

- обычный крафт через полевую станцию не является активной RecipeTransaction;
- Ночной Верстак использует отдельный контракт опасной рейдовой операции;
- публичный рецепт боеприпасов внутри рейда удалён;
- случайные исходы Defect/Corruption не добавляются к мирной сделке;
- один адрес не принимает собственный выход в более выгодную петлю;
- числовой курс не публикуется до проверки safe-profit и доминирования адресов.

## 7. Шаблон новой записи

```text
[recipe_id:: recipe_id]
[address_id:: address_id]
[address_class:: central|stable_external]
[availability:: permanent|stable_cycle]
[inputs:: multiset(item_or_tag, item_or_tag)]
[source_rule:: raid_extracted|resolved_provenance]
[optional_variant:: zero_or_one|none]
[blueprint_id:: limited|none]
[service_cost:: service_cost_id]
[exact_outcome:: outcome_id]
[provenance_result:: processing_rule]
[balance_state:: unknown]
```

Новая запись допускается только при существующих адресе, входах и результате. Описательный пример без реальных потребителей остаётся вне активного реестра.
