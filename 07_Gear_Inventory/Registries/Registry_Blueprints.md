---
status: active
system: gear_inventory_registry
registry_type: blueprints
category: blueprints
tags:
  - database
  - loot
  - limited_blueprint
  - physical_custody
  - recipe_transaction
related_files:
  - "[[06_Economy_Loot/Blueprints|Blueprints]]"
  - "[[07_Gear_Inventory/Registries/Registry_CraftingRecipes|Registry_CraftingRecipes]]"
  - "[[08_World_Generation/Registries/Registry_POIs|Registry_POIs]]"
type: registry
index_route: owner
index_group: gear_inventory
index_order: 10
index_summary: "Хранит схему и записи: Реестр: LimitedBlueprint."
read_when: "Когда нужен контракт «Реестр: LimitedBlueprint» и его границы с соседними владельцами."
---
# Реестр LimitedBlueprint

Реестр хранит подтверждённые физические ограниченные инструкции для редких именованных схем. Вынесенный носитель даёт несколько будущих применений, но не заменяет извлечённый состав и подходящий мирный адрес.

Базовый фильтр, батарея, ремонт, лечение и другие центральные услуги не требуют чертежа. Полный lifecycle принадлежит [[06_Economy_Loot/Blueprints|Ограниченным Чертежам]].

## Active contract

```text
blueprint_id
recipe_ids[]
custody: physical
use_model: limited
uses_remaining
address_ids[]
transfer_rule: physical_item
identification_state: unknown | identified
source
balance_state
```

- носитель можно вынести, потерять и физически передать;
- знание ингредиентов не заменяет предмет;
- мирный адрес должен существовать в [[08_World_Generation/Registries/Registry_POIs|Registry_POIs]];
- отсутствие текущего Stable-адреса не расходует носитель;
- preview, несовместимый состав и отмена до Commitment не уменьшают применения;
- после идентификации `recipe_ids` и точный результат становятся видимыми;
- числовое количество применений задаётся конкретной записью после калибровки.

## Confirmed records

Подтверждённых носителей пока нет. Повреждённый планшет не поддержан действующим рецептом, адресом и источником, поэтому не считается активным контентом.

## Adding a record

```text
[blueprint_id:: blueprint_id]
[recipe_ids:: recipe_id]
[custody:: physical]
[use_model:: limited]
[uses_remaining:: calibrated_value]
[address_ids:: peaceful_address_id]
[transfer_rule:: physical_item]
[identification_state:: identified]
[source:: raid_source_id]
[balance_state:: unknown]
```

Запись не допускает рейдовый адрес. Ограниченный носитель является редкой ставкой послерейдового планирования, а не условием обычного полевого производства. Отложенные модели перечислены у [[06_Economy_Loot/Blueprints#4. Сознательно отложено|системного владельца]].
