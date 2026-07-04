---
type: registry
status: active
system: gear_inventory_registry
registry_type: crafting
tags: [database, economy, recipe_transaction, blueprints, decorators]
related_files:
  - "[[06_Economy_Loot/Barter_System|Barter_System]]"
  - "[[06_Economy_Loot/Blueprints|Blueprints]]"
  - "[[06_Economy_Loot/Craft_Modifiers|Craft_Modifiers]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Blueprints|Registry_Blueprints]]"
---
# Реестр: RecipeTransaction

Этот реестр хранит конкретные сделки. Универсальные правила принадлежат [[06_Economy_Loot/Barter_System|Barter System]], чертежи — [[06_Economy_Loot/Blueprints|Blueprints]], а Decorators — [[06_Economy_Loot/Craft_Modifiers|Craft Modifiers]].

Старые сферы прямого повышения редкости, полный reroll готовой вещи и отдельный POE-подобный цикл выведены из канона. Конкретные старые рецепты возвращаются только после проверки реестров предметов, модулей, аффиксов и реальных MVP-потребителей.

## Контракт записи

```text
recipe_id
address
station
public_or_blueprint
inputs
decorator_slots
local_conditions
service_cost
commitment
outcomes
output_state
balance_state
```

- `address` принимает последствия сделки;
- `public_or_blueprint` указывает публичный рецепт либо `blueprint_id`;
- `decorator_slots` перечисляет только допустимые семейства;
- `local_conditions` хранит фазу, погоду, питание станции, навык или доверие;
- `commitment` определяет время, шум и момент расхода входов;
- `outcomes` перечисляет рабочий результат, отходы и разрешённые Defect/Corruption-ветви;
- `balance_state` остаётся `unknown`, пока входы и выход не проверены на полной экономике.

## Публичная полевая сделка: болты из крепежа

[recipe_id:: field_bolts_from_fasteners]
[address:: field_station]
[station:: workbench]
[public_or_blueprint:: public]
[decorator_slots:: yield|reliability]
[local_conditions:: station_powered]
[output_state:: native]
[balance_state:: unknown]

Игрок перерабатывает подходящий крепёж в механические боеприпасы. Сделка использует только рейдовый инвентарь, занимает руки, создаёт `AcousticEvent` и не подключается к Схрону.

## Шаблон сделки

### Шаблон RecipeTransaction

[recipe_id:: template_recipe]
[address:: master_id]
[station:: station_id]
[public_or_blueprint:: blueprint_id|public]
[decorator_slots:: guide|yield|reliability|signature|risk|none]
[local_conditions:: condition_id|none]
[output_state:: stable|volatile|native]
[balance_state:: unknown]

- **Inputs:** структурированные ID и количества после калибровки.
- **Commitment:** время, занятые руки, шум и момент фиксации.
- **Outcomes:** основной результат, отходы и допустимые Defect/Corruption-исходы.
- **Player-facing reason:** почему этот адрес способен совершить такую операцию.
