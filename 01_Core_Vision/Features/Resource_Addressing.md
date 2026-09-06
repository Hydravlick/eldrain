---
type: feature
status: active
system: player_experience
feature_id: resource_addressing
feature_order: 11
display_name: Найти добыче применение
player_promise: Выбрать, превратить ли вынесенный состав в следующий рейд, специальную сборку или вклад в город.
expected_dynamics: Знание рецептов делает выбор яснее, но не сводит всё имущество к одному лучшему конвертеру.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[06_Economy_Loot/Resource_Cycle]]"
  - "[[06_Economy_Loot/Barter_System]]"
  - "[[06_Economy_Loot/Vendor_Logic]]"
  - "[[06_Economy_Loot/Blueprints]]"
  - "[[06_Economy_Loot/Craft_Modifiers]]"
  - "[[06_Economy_Loot/Economy_Core]]"
data_sources:
  - "[[07_Gear_Inventory/Registries/Registry_CraftingRecipes]]"
  - "[[07_Gear_Inventory/Registries/Registry_Items]]"
  - "[[07_Gear_Inventory/Registries/Registry_Blueprints]]"
ux_surfaces:
  - "[[08_World_Generation/Hub/Hub_Map_Table]]"
  - "[[08_World_Generation/Hub/Hub_Services_Interaction]]"
production_disciplines:
  - UX
  - narrative
  - gameplay
  - QA
validation:
  - "[[01_Core_Vision/Features/Resource_Addressing#Проверка гипотезы]]"
---

# Найти добыче применение

Выбрать, превратить ли вынесенный состав в следующий рейд, специальную сборку или вклад в город.

Сохранить конкретную полезность Common-добычи и осмысленный выбор адреса.

## За минуту

Извлечённый состав сопоставляется с известными адресами. Игрок сравнивает точные результаты, выбирает услугу и подтверждает сделку. Её результат сохраняет происхождение входов и меняет подготовку следующего выхода.

## Сценарии и границы

- Один ингредиент подходит для sustain и sidegrade: выбрать, чем пожертвовать.
- Рецепт совпал по составу, но не по происхождению: увидеть отказ до передачи.
- Внешний мастер недоступен: использовать ограниченный центральный минимум.
- Повторная пакетная сделка исполняет только опубликованное точное совпадение.

Не создавать вторую ресурсную систему, универсальную топку, рыночный арбитраж или тайный рецепт, который обязана не решить wiki.

## Кто исполняет и что видит игрок

Правила и переходы: [[06_Economy_Loot/Resource_Cycle]], [[06_Economy_Loot/Barter_System]], [[06_Economy_Loot/Vendor_Logic]], [[06_Economy_Loot/Blueprints]], [[06_Economy_Loot/Craft_Modifiers]], [[06_Economy_Loot/Economy_Core]].

Данные и авторские экземпляры: [[07_Gear_Inventory/Registries/Registry_CraftingRecipes]], [[07_Gear_Inventory/Registries/Registry_Items]], [[07_Gear_Inventory/Registries/Registry_Blueprints]].

Игроковые экраны, сигналы и объяснение отказа: [[08_World_Generation/Hub/Hub_Map_Table]], [[08_World_Generation/Hub/Hub_Services_Interaction]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Знание рецептов делает выбор яснее, но не сводит всё имущество к одному лучшему конвертеру.

- **Наблюдаем:** Опытный игрок выбирает разные назначения одного состава в зависимости от следующей работы.
- **Доказательство и способ наблюдения:** Сравнение решений до/после публикации рецептов и при накопленном богатстве; проверка замкнутых цепей услуг.
- **Опровержение:** Один адрес поглощает весь лут или безопасные сделки устойчиво финансируют себя без рейда.
- **Ответ:** Пересмотреть составы и назначение результатов у владельцев рецептов и экономики.

## MVP и производство

Первый срез: Одна находка с основным и альтернативным адресом, недостающий ингредиент и исполненная RecipeTransaction. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

Курсы, replacement cost и ветеранское накопление не доказаны; числовой baseline ещё нужен.

Economy/content design задаёт конечный рецепт; UX показывает недостающее; narrative объясняет интерес адресата; QA проверяет расход и отказ без скрытого контракта.
