---
type: registry
status: active
system: gear_inventory_registry
registry_type: blueprints
category: blueprints
tags: [database, loot, trade, schematics, recipe_transaction]
related_files:
  - "[[06_Economy_Loot/Blueprints|Blueprints]]"
  - "[[07_Gear_Inventory/_Registries/Registry_CraftingRecipes|Registry_CraftingRecipes]]"
---
# Реестр: Чертежи

Реестр хранит физические носители и зарегистрированные права исполнения. Старые списки готового фракционного снаряжения выведены из активного наполнения: Очаг может открыть Мастера, доверие или регистрацию, но не заменяет рейд источником ценной вещи и всех её входов.

## Контракт записи

```text
blueprint_id
recipe_ids
custody: physical | registered
use_model: consumable | limited | permanent
address
transfer_rule
local_conditions
source
balance_state
```

- `physical` занимает место, может быть потерян и используется полевой станцией;
- `registered` существует только у указанного адреса и не передаётся дропом;
- `consumable` сгорает после зафиксированного исхода;
- `limited` теряет одно применение;
- `permanent` возвращает носитель либо сохраняет регистрацию;
- `source` обязан назвать рейд, контракт, Мастера или исследование, а не абстрактный уровень аккаунта.

## Неопознанный носитель

### Повреждённый планшет

[blueprint_id:: damaged_unknown_carrier]
[recipe_ids:: unknown]
[custody:: physical]
[use_model:: limited]
[address:: proving_houses|field_station]
[transfer_rule:: physical_item]
[local_conditions:: identification_required]
[source:: raid_archive_or_workshop]
[balance_state:: unknown]

До идентификации игрок видит цивилизацию, материальный язык и возможное семейство операции, но не точный результат. Дома Пробы могут зарегистрировать знание, восстановить часть страниц либо вернуть физический носитель; конкретный исход задаётся отдельной RecipeTransaction.

## Шаблон

### Шаблон Чертежа

[blueprint_id:: template_blueprint]
[recipe_ids:: template_recipe]
[custody:: physical]
[use_model:: consumable|limited|permanent]
[address:: public|hearth_id|table_id|master_id|field_station]
[transfer_rule:: physical_item|registered_nontransferable]
[local_conditions:: none]
[source:: source_id]
[balance_state:: unknown]

- **Player-facing promise:** какую новую операцию позволяет выполнить носитель.
- **Custody feedback:** где он хранится и чем рискует игрок.
- **Execution gate:** какой адрес, станция или состояние мира всё ещё требуется.
