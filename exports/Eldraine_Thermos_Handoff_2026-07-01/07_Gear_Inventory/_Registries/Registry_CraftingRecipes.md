---
type: registry
status: active
system: gear_inventory_registry
registry_type: crafting
tags: [database, economy, upgrade, blueprints]
related_files:
  - "[[07_Gear_Inventory/Thermos_System|Thermos_System]]"
  - "[[07_Gear_Inventory/Civic_Attire|Civic_Attire]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Attire|Registry_Attire]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Thermoses|Registry_Thermoses]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Thermos_Modules|Registry_Thermos_Modules]]"
---
> [!TODO] Рецепты линий Чужой воды
> - [ ] После утверждения ингредиентов добавить рецепты для исследования линии, погодных контрмер и перенаправления Белого ответа.
> - [ ] Не делать одну ветку обязательным источником универсально лучшего расходника или экипировки.
> - **Основа:** [[08_World_Generation/_Registries/Registry_Anomaly_Mutations|Registry_Anomaly_Mutations]]. Стоимость и выход рецептов этой правкой не меняются.
# Реестр: Крафт и Модификации (Workshop)

> **Логика:** Крафт требует **Верстак** (в Хабе или найденный в рейде) и **Чертеж** (Blueprint).
> **Rarity Upgrades:** Сферы взаимодействуют с Энтропией предмета, повышая его редкость и меняя аффиксы, но не Tier конструкции.
> **Термос и модули:** модель и модули являются отдельными предметами. Rarity не меняет `slot_count` или `module_cost` автоматически; функциональный монтаж выполняет только профессионал в Хабе.
> **Requirements:** `[rep:: faction_id : level]` — требование репутации для покупки чертежа.

---

## 1. Сферы Трансмутации (Upgrade Spheres)
*Аналог валюты/орбов из PoE. Используются для повышения редкость и реролла статов.*

### Сфера Потока (Orb of Flux)
[item:: orb_flux]
*Сгусток нестабильной энергии.*
- **Эффект:** Превращает **Обычный (White)** предмет в **Необычный (Green)**.
- **Свойства:** Добавляет 1-2 случайных аффикса (свойства).
- **Дроп:** Дома Пробы, Рунный Стол или временная лавка экспериментального мастера.

### Сфера Власти (Orb of Power)
[item:: orb_power]
*Стабилизированная структура эфира.*
- **Эффект:** Превращает **Необычный (Green)** предмет в **Редкий (Blue)**.
- **Свойства:** Добавляет аффикс из другого допустимого семейства. Не повышает базовый урон или броню автоматически.
- **Дроп:** Рейды, Боссы.

### Сфера Хаоса (Orb of Chaos)
[item:: orb_chaos]
*Энергия чистой случайности.*
- **Эффект:** Полностью меняет (Reroll) все аффиксы на **Редком** предмете.
- **Риск:** Нет риска поломки, но можно получить бесполезные статы.

### Сфера Коллапса (Entropy Orb)
[item:: orb_entropy]
*Запрещенный артефакт. Выглядит как черная дыра в миниатюре.*
- **Эффект:** "Оскверняет" (Corrupt) предмет.
- **Результаты (Ролл 1d4):**
    1.  **Прорыв:** Предмет получает Corruption-правило с сильным эффектом и встроенной ценой.
    2.  **Мутация:** Меняется существующий рабочий цикл или тип взаимодействия, но не возникает бесплатный универсальный урон.
    3.  **Стазис:** Предмет "замораживается" (нельзя больше менять, статы не меняются).
    4.  **Аннигиляция:** Предмет превращается в горстку `[item:: scrap_metal]` (Уничтожается).

## Реестр: Рецепты Крафта (Assembly Lines)

> **Формула Крафта:** `[Input A] + [Input B] + [Blueprint Item] = [Output]`
> **Blueprint Consumption:** Если чертеж одноразовый, он исчезает при нажатии "Собрать". Если многоразовый — остается в слоте.

---

## Перешив мирской одежды

### Извлечение Cut Module
[recipe:: attire_cut_module_extraction]
[input_category:: attire]
[output_category:: cut_module]
[balance_state:: unknown]

Мастер распарывает один экземпляр Attire и извлекает только указанный в Registry_Attire Cut Module.

- Исходный наряд уничтожается необратимо.
- Операция недоступна, пока право disputed, contract или soulbound не разрешено подходящим адресом.
- Cut Module наследует attire_id и происхождение до завершения крафта, но не считается вторым оригиналом.
- Один наряд создаёт один модуль; числовой выход не масштабируется редкостью.

### Встройка культурного принципа
[recipe:: cultural_module_integration]
[input_category:: thermos_module|cut_module|supporting_materials]
[output_category:: thermos_module]
[balance_state:: unknown]

Cut Module встраивается в совместимый модуль Термоса и его допустимую module_axis. Сам Термос при этом не расходуется.

- Результат не повышает Tier, базовую защиту или Rarity автоматически.
- Новая функция либо увеличивает соответствующий `module_cost`, либо получает другую явную цену.
- Телесную посадку задаёт fit_profile выбранного Термоса, а не native_fit уничтоженной одежды.
- Итог сохраняет cultural_cut_module для происхождения, визуального следа и Dataview.
- Установить результат можно только у профессионала; в Аномалии найденный или созданный модуль остаётся Cargo.
- Точные материалы, цена услуги и время работы остаются UNKNOWN до балансного прохода.

## Фракционное Снаряжение (Faction Gear)

### Маска "Чистый Воздух" (Keeper Mask)
*Защита от токсинов T1.*
- **Input:**
    - 1x `[blueprint:: keeper_mask]` (Чертеж)
    - 5x `[item:: scrap_metal]` (Каркас)
    - 2x `[item:: gas_filter]` (Фильтры)
    - 1x `[item:: rubber_boots]` (Уплотнитель - разбор)
- **Output:** `[gear:: keeper_mask]`

### Ход Первопроходца (Pathfinder Tread)
*Съёмные подошвы и голенные тяги Термоса: скорость +10%, карабканье.*
- **Input:**
    - 1x `[blueprint:: pathfinder_boots]` (Чертеж)
    - 4x `[item:: swamp_vine]` (Шнуровка)
    - 2x `[item:: chitin_plate]` (Шипы)
- **Output:** `[thermos_module:: pathfinder_boots]`

### Мод "Тихая Поступь" (Silent Soles)
*Шум шагов -40%. Вставляется в нижние крепления Термоса.*
- **Input:**
    - 1x `[blueprint:: silent_soles]` (Чертеж)
    - 5x `[item:: wet_fabric]` (Ткань)
    - 3x `[item:: swamp_vine]` (Амортизатор)
- **Output:** `[mod:: silent_soles]`

### Фантомная вуаль (Phantom Veil)
*Внешний модуль Термоса с активной невидимостью. Чертеж многоразовый.*
- **Input:**
    - 1x `[blueprint:: phantom_cloak]` (Многоразовый Чертеж)
    - 10x `[item:: wet_fabric]`
    - 2x `[item:: sea_tear]` (Жемчуг)
    - 1x `[item:: deep_scale]` (Эссенция)
- **Output:** `[thermos_module:: phantom_cloak]`

### Вольт-Конденсатор (Volt Condenser)
*Электрическая дуга по 2 целям.*
- **Input:**
    - 1x `[blueprint:: volt_condenser]` (Чертеж)
    - 1x `[weapon:: arcanegun]` (Любой конденсаторный фрейм)
    - 3x `[item:: capacitor_cell]` (Накопитель)
- **Output:** `[weapon:: volt_condenser]`

### Ловушка Теслы (Tesla Trap)
*Стационарная турель.*
- **Input:**
    - 1x `[blueprint:: tesla_trap]` (Многоразовый Чертеж)
    - 1x `[item:: battery_large]`
    - 2x `[item:: coral_shard]`
- **Output:** `[gadget:: tesla_trap]`

### Булава Инквизитора (Inquisitor Mace)
*Урон по магам.*
- **Input:**
    - 1x `[blueprint:: inquisitor_mace]` (Чертеж)
    - 1x `[weapon:: blunt]` (Молот-основа)
    - 50x `[item:: old_coins]` (Серебро)
    - 1x `[item:: incense]` (Освящение)
- **Output:** `[weapon:: inquisitor_mace]`

### Гвоздомет "Заклепочник" (Heavy Riveter)
*Тяжелый гарпунно-заклепочный разрядник.*
- **Input:**
    - 1x `[blueprint:: heavy_riveter]` (Чертеж)
    - 20x `[item:: scrap_metal]`
    - 1x `[item:: capacitor_cell]`
- **Output:** `[weapon:: heavy_riveter]`

### Сумка Контрабандиста (Smuggler Bag)
*Защита от сканирования лута.*
- **Input:**
    - 1x `[blueprint:: smuggler_bag]` (Чертеж)
    - 1x `[item:: pouch]`
    - 5x `[item:: chitin_plate]`
- **Output:** `[gear:: smuggler_bag]`

---

## Редкое Снаряжение (Rare Assembly)

### Сабля Призрачного Капитана (Spectral Cutlass)
*Игнорирует броню.*
- **Input:**
    - 1x `[blueprint:: spectral_cutlass]` (Многоразовый Чертеж)
    - 1x `[weapon:: blade]` (Сабля-основа)
    - 1x `[item:: deep_scale]`
    - 3x `[item:: sea_tear]`
- **Output:** `[weapon:: spectral_cutlass]`

---

## Трансмутация (Upgrades)
*Не требует чертежей, требует Сферы.*

### Enchant Weapon (Magic)
- **Input:** 1x `[weapon:: any_white]` + 1x `[item:: orb_flux]`
- **Output:** `[weapon:: random_green]`

### Enchant Weapon (Rare)
- **Input:** 1x `[weapon:: any_green]` + 1x `[item:: orb_power]`
- **Output:** `[weapon:: random_blue]`

### Corrupt Item
- **Input:** 1x `[item:: any]` + 1x `[item:: orb_entropy]`
- **Output:** `[item:: corrupted]` (See Entropy Table)
---

## 0. Нулевой пациент: шаблон рецепта

### Шаблон Рецепта (Template Recipe)
[recipe_id:: template_recipe]
[output_item:: template_item]
[input_item:: scrap_metal]
[station:: field_kit]
[craft_time:: 10s]
*Короткое описание операции.*
- **Вход:** список ресурсов.
- **Выход:** предмет, отходы, шанс редкости или аффикса.
- **Ограничение:** станция, навык, фаза рейда или шум.
