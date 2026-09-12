---
status: active
system: gear_inventory_registry
registry_type: crafting
tags:
  - database
  - economy
  - recipe_transaction
  - blueprints
  - variant_ingredient
related_files:
  - "[[06_Economy_Loot/Barter_System|Barter_System]]"
  - "[[06_Economy_Loot/Blueprints|Blueprints]]"
  - "[[06_Economy_Loot/Craft_Modifiers|Craft_Modifiers]]"
  - "[[07_Gear_Inventory/Registries/Registry_Blueprints|Registry_Blueprints]]"
type: registry
index_route: owner
index_group: gear_inventory
index_order: 30
index_summary: "Хранит схему и записи: Реестр: Адресные RecipeTransaction."
read_when: "Когда нужен контракт «Реестр: Адресные RecipeTransaction» и его границы с соседними владельцами."
---
# Реестр адресных RecipeTransaction

Реестр является единственным источником подтверждённых мирных сделок. Универсальный цикл принадлежит [[06_Economy_Loot/Barter_System|адресному бартеру]], limited-носители — [[06_Economy_Loot/Blueprints|чертежам]], а правило одного фиксированного варианта — [[06_Economy_Loot/Craft_Modifiers|вариантному ингредиенту]].

Игрок видит точный результат до подтверждения. Сделка не перебрасывает найденные Affix, не повышает Rarity универсальным материалом и не превращает полевую станцию в безопасный магазин внутри Аномалии.

## Active contract

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

- `address_id` должен существовать в [[08_World_Generation/Registries/Registry_POIs|Registry_POIs]];
- `availability` наследует срок адреса, а не создаёт собственное короткое окно;
- `inputs` хранит теги/ID и мультимножество количеств;
- `source_rule` не позволяет купить товар в центре и превратить его в прибыльный ресурсный вход;
- `optional_variant` допускает максимум один объявленный ингредиент с фиксированным свойством;
- `blueprint_id` используется только редкой limited-схемой;
- `exact_outcome` является одним известным результатом, без случайной ветви Affix или Corruption;
- `provenance_result` сохраняет источник значимых входов, адрес и Stable-цикл;
- `balance_state` остаётся `unknown`, пока курс не проверен в полной экономике.

Для адресного лечения Scar запись дополнительно связывает объявленную service eligibility и `exact_outcome = resolve_scar(PawnID, ScarID, scar_revision)`. Результат исполняют Scar/Body и Health по [[06_Economy_Loot/Barter_System#Адресная транзакция лечения Scar|transaction owner]], а не этот реестр. Непустые реальные resource inputs и их положительные количества обязательны; конкретные рецепты лечения здесь пока не публикуются.

## Confirmed records

Подтверждённых RecipeTransaction пока нет. Базовый фильтр остаётся действующей категорией центральной услуги, но его конкретные входы, стоимость и `recipe_id` не утверждены; прежний пример не является каноническим рецептом.

## Adding a record

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

Новая запись допускается только при существующих адресе, входах и результате. Описательный пример без реальных потребителей остаётся вне активного реестра. Исключения принадлежат [[06_Economy_Loot/Barter_System#6. Исключения|адресному бартеру]].
