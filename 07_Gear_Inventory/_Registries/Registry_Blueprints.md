---
type: registry
status: active
system: gear_inventory_registry
registry_type: blueprints
category: blueprints
tags: [database, loot, limited_blueprint, physical_custody, recipe_transaction]
related_files:
  - "[[06_Economy_Loot/Blueprints|Blueprints]]"
  - "[[07_Gear_Inventory/_Registries/Registry_CraftingRecipes|Registry_CraftingRecipes]]"
  - "[[08_World_Generation/_Registries/Registry_POIs|Registry_POIs]]"
---
# Реестр: LimitedBlueprint

## 1. Ответственность и обещание

Реестр хранит только физические ограниченные инструкции для редких именованных схем. Вынесенный носитель даёт несколько будущих применений, но не заменяет извлечённый состав и подходящий мирный адрес.

Базовый фильтр, батарея, ремонт, лечение и другие центральные услуги не требуют чертежа.

## 2. Рабочий цикл

1. Физический носитель находится и эвакуируется как обычный груз.
2. Мирный адрес идентификации раскрывает связанную схему и число применений.
3. Карта показывает совместимые центральные или Stable-внешние адреса.
4. RecipeTransaction проверяет носитель и извлечённый состав.
5. После подтверждённого результата `uses_remaining` уменьшается на одно.

Ночной Верстак не исполняет LimitedBlueprint, не читает Схрон и не превращает его в полевую лицензию.

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

Следующие модели не участвуют в активном контракте и шаблоне:

- `consumable` — отдельный одноразовый класс;
- `permanent` — постоянное разблокирование рецепта;
- `registered` — хранение права у аккаунта, Очага или мастера;
- копирование и продажа знания;
- исполнение схемы на полевой станции или Ночном Верстаке.

Их можно вернуть только отдельным авторским решением после проверки limited-модели на hoarding, snowball и ценность потери.

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
