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
# Реестр: LimitedBlueprint

## 1. Ответственность и обещание

Реестр хранит только физические ограниченные инструкции для редких именованных схем. Вынесенный носитель даёт несколько будущих применений, но не заменяет извлечённый состав и подходящий мирный адрес.

Базовый фильтр, батарея, ремонт, лечение и другие центральные услуги не требуют чертежа.

## 2. Рабочий цикл

См. [[06_Economy_Loot/Blueprints#2. Рабочий цикл]].

## 3. Активный контракт

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
- мирный адрес должен существовать в Registry_POIs;
- отсутствие текущего Stable-адреса не расходует носитель;
- preview, несовместимый состав и отмена до Commitment не уменьшают применения;
- после идентификации `recipe_ids` и точный результат становятся видимыми;
- числовое количество применений задаётся конкретной записью после калибровки.

## 4. Повреждённый носитель

### Повреждённый планшет

[blueprint_id:: damaged_unknown_carrier]
[recipe_ids:: unknown_until_identified]
[custody:: physical]
[use_model:: limited]
[uses_remaining:: unknown_until_identified]
[address_ids:: stable_mechanic_service]
[transfer_rule:: physical_item]
[identification_state:: unknown]
[source:: raid_archive_or_workshop]
[balance_state:: unknown]

До идентификации игрок видит цивилизацию, материальный язык и вероятный тип обработки, но не точный результат. Мирный мастер раскрывает `recipe_ids`, остаток применений и exact outcome; если текущего адреса нет, носитель остаётся в Схроне до подходящего Stable-цикла.

## 5. Сознательно отложено

См. [[06_Economy_Loot/Blueprints#4. Сознательно отложено]].

## 6. Шаблон LimitedBlueprint

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

Шаблон не допускает рейдовый адрес. Ограниченный носитель является редкой ставкой послерейдового планирования, а не условием обычного полевого производства.
