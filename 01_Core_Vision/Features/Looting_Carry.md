---
type: feature
status: active
system: player_experience
feature_id: looting_carry
feature_order: 6
display_name: Найти, выбрать и унести
player_promise: Выбрать полезную добычу и физически доставить её к выходу под давлением.
expected_dynamics: Игрок оставляет ценную вещь по понятной маршрутной причине, а не из-за непонятного интерфейса.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[04_Player_Entities/Interaction_Constraints]]"
  - "[[07_Gear_Inventory/Looting_Process]]"
  - "[[07_Gear_Inventory/Inventory_Architecture]]"
  - "[[07_Gear_Inventory/Physical_Weight]]"
  - "[[07_Gear_Inventory/Containers_Slots]]"
  - "[[06_Economy_Loot/Loot_Distribution]]"
  - "[[05_Combat_Survival/Field_Crafting]]"
  - "[[04_Player_Entities/Shell_Foundlings]]"
data_sources:
  - "[[07_Gear_Inventory/Registries/Registry_Items]]"
  - "[[07_Gear_Inventory/Registries/Registry_Consumables]]"
  - "[[08_World_Generation/Registries/Registry_Mobs]]"
ux_surfaces:
  - "[[07_Gear_Inventory/Item_Attributes_UI]]"
  - "[[07_Gear_Inventory/Inventory_QoL]]"
production_disciplines:
  - UX
  - animation
  - audio
  - level design
  - QA
validation:
  - "[[01_Core_Vision/Features/Looting_Carry#Проверка гипотезы]]"
---

# Найти, выбрать и унести

Выбрать полезную добычу и физически доставить её к выходу под давлением.

Превратить состав груза, доступ к вещам и маршрут в связанные решения.

## За минуту

Обыск раскрывает содержимое постепенно. Игрок сравнивает находку с текущим грузом, размещает её в доступной зоне и продолжает путь. Работа с узлом или переноска человека меняет физическое обязательство и план отхода.

## Сценарии и границы

- Взять полезный ингредиент вместо более тяжёлой находки.
- Прервать обыск, когда появился чужой след.
- Передать груз союзнику без второго экземпляра.
- Нести Найдёныша и отказаться от несовместимого груза.

Не определять награду ценником и не превращать обыск или перенос в автоматическую экстракцию.

## Кто исполняет и что видит игрок

Правила и переходы: [[04_Player_Entities/Interaction_Constraints]], [[07_Gear_Inventory/Looting_Process]], [[07_Gear_Inventory/Inventory_Architecture]], [[07_Gear_Inventory/Physical_Weight]], [[07_Gear_Inventory/Containers_Slots]], [[06_Economy_Loot/Loot_Distribution]], [[05_Combat_Survival/Field_Crafting]], [[04_Player_Entities/Shell_Foundlings]].

Данные и авторские экземпляры: [[07_Gear_Inventory/Registries/Registry_Items]], [[07_Gear_Inventory/Registries/Registry_Consumables]], [[08_World_Generation/Registries/Registry_Mobs]].

Игроковые экраны, сигналы и объяснение отказа: [[07_Gear_Inventory/Item_Attributes_UI]], [[07_Gear_Inventory/Inventory_QoL]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Игрок оставляет ценную вещь по понятной маршрутной причине, а не из-за непонятного интерфейса.

- **Наблюдаем:** Изменение груза меняет доступ, путь или готовность; игрок замечает это до необратимой ошибки.
- **Доказательство и способ наблюдения:** Наблюдение обыска под угрозой, смены носителя и маршрутов с разным грузом.
- **Опровержение:** Перенос всегда сводится к максимальному value/kg или интерфейс прячет причину отказа.
- **Ответ:** Пересмотреть адресную полезность, bulk/access-сигналы и физическую цену переноски.

## MVP и производство

Первый срез: Одна спорная находка, смена custody, рост нагрузки и физическая потеря; один предмет проходит до итогового Stash. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

Проверять после появления общего знания цен и маршрутов; бытовой loot не должен стать мусорным налогом.

UX объясняет занятую руку и недоступное действие; animation показывает перенос; gameplay и QA проверяют гонку за одним ItemID и исчезновение носителя.
