---
type: navigation
status: active
version: 2.0
tags: [root, index, map]
---

# ELDRAIN: Навигатор Проекта (Master Index)

> **Текущий статус архитектуры:** v2.0 (Cluster System)
> **Старый GDD:** [[00_Core/GDD_Main|GDD_Main v1.2]] (Частично устарел, использовать как архив идей).
> **Актуальная архитектура:** [[00_Core/Game_Architecture_MVP|Game_Architecture_MVP v2.0]]

---

##  00. CORE (Фундамент)
*Базовые документы, определяющие видение и структуру.*

* [[00_Core/Vision|Видение и Атмосфера]] — High Concept, мудборд, стилистика.
* [[00_Core/Game_Architecture_MVP|Архитектура Проекта]] — Структура папок и пайплайн.
* [[00_Core/Loop|Core Gameplay Loop]] — Основной цикл игры.
* [[00_Core/Glossary|Глоссарий]] — Термины и определения.
* *(Архив)* [[00_Core/GDD_Main|GDD Main (Legacy)]]

## 00. VARIABLES (Реестры и Матрицы)
*Балансные таблицы и списки сущностей.*

* **Сущности:** [[00_Variables/00_Archetype_Matrix|Матрица Архетипов]] | [[00_Variables/00_Character_Matrix|Матрица Персонажей]] | [[00_Variables/00_Biome_Matrix|Биомы]]
* **Реестры (Registry):**
    * [[00_Variables/Registry_Items|Предметы (Items)]] | [[00_Variables/Registry_Weapons|Оружие]] | [[00_Variables/Registry_Armors|Броня]]
    * [[00_Variables/Registry_Mobs|Мобы]] | [[00_Variables/Registry_Factions|Фракции]] | [[00_Variables/Registry_Races|Расы]]
    * [[00_Variables/Registry_CraftingRecipes|Крафт]] | [[00_Variables/Registry_Blueprints|Чертежи]] | [[00_Variables/Registry_Consumables|Расходники]]
    * [[00_Variables/Registry_StatusEffects|Статус-эффекты]] | [[00_Variables/Registry_Tags|Теги]] | [[00_Variables/Registry_POIs|Точки интереса (POI)]]

---

## 10. MECHANICS (Игровая Логика)

### 01. Player Core (Персонаж)
* [[10_Mechanics/01_Player_Core/01_Entity_Grimoire|Сущность и Гримуар]] — Мета-прогрессия.
* [[10_Mechanics/01_Player_Core/02_Shell_Specification|Спецификация Оболочки]] — Характеристики тела.
* [[10_Mechanics/01_Player_Core/03_Shell_Construction|Конструктор Оболочки]] — Сборка персонажа.
* [[10_Mechanics/01_Player_Core/04_Attributes_TOUCH|Система Атрибутов (TOUCH)]]
* [[10_Mechanics/01_Player_Core/05_Ability_Synergy|Синергия Способностей]]
* [[10_Mechanics/01_Player_Core/06_Proficiency_Arsenal|Владение Оружием]]
* [[10_Mechanics/01_Player_Core/07_Tags_System|Система Тегов]]

### 02. Action & Combat (Бой)
* **Физика:** [[10_Mechanics/02_Action_Combat/01_Movement_Physics|Передвижение]] | [[10_Mechanics/02_Action_Combat/04_Ballistics_Armor|Баллистика и Броня]]
* **Оружие:** [[10_Mechanics/02_Action_Combat/08_Weapon_Core|Ядро Оружия]] | [[10_Mechanics/02_Action_Combat/09_Weapon_Melee|Ближний бой]] | [[10_Mechanics/02_Action_Combat/10_Weapon_Ranged|Стрельба]]
* **Системы:** [[10_Mechanics/02_Action_Combat/02_Acoustic_Stealth|Акустика (Стелс)]] | [[10_Mechanics/02_Action_Combat/03_Resonance_System|Резонанс]] | [[10_Mechanics/02_Action_Combat/07_Entropy_System|Энтропия]]
* **Прочее:** [[10_Mechanics/02_Action_Combat/12_Magic_Batteries|Маго-Батареи]] | [[10_Mechanics/02_Action_Combat/13_Masks_Filters|Маски и Фильтры]] | [[10_Mechanics/02_Action_Combat/15_Field_Crafting|Полевой Крафт]]

### 03. Economy (Экономика)
* [[10_Mechanics/03_Economy/00_Economy_Core|Ядро Экономики]]
* [[10_Mechanics/03_Economy/01_Currency_Rez|Валюта (Rez)]] | [[10_Mechanics/03_Economy/02_Premium_Shards|Премиум]]
* [[10_Mechanics/03_Economy/06_Barter_System|Бартер]] | [[10_Mechanics/03_Economy/12_Auction_House|Аукцион]]
* [[10_Mechanics/03_Economy/13_Item_Degradation|Износ Предметов]] | [[10_Mechanics/03_Economy/14_Resource_Cycle|Цикл Ресурсов]]

### 04. Inventory (Инвентарь)
* [[10_Mechanics/04_Inventory_Gear/01_Grid_Architecture|Сетка Инвентаря]]
* [[10_Mechanics/04_Inventory_Gear/02_Containers_Slots|Контейнеры и Слоты]]
* [[10_Mechanics/04_Inventory_Gear/03_Physical_Weight|Вес и Нагрузка]]
* [[10_Mechanics/04_Inventory_Gear/06_Equipment_PaperDoll|Кукла Персонажа (PaperDoll)]]
* [[10_Mechanics/04_Inventory_Gear/08_Looting_Process|Процесс Лутинга]]
* [[10_Mechanics/04_Inventory_Gear/09_Stash_Architecture|Схрон (Stash)]]

### 05. World Systems (Мир)
* **Хаб:** [[10_Mechanics/05_World_Systems/01_Hub/00_Hub_Environment|Среда Хаба]] | [[10_Mechanics/05_World_Systems/01_Hub/02_Hub_Services_Interaction|Сервисы]]
* **Генерация:** [[10_Mechanics/05_World_Systems/02_Generation/01_World_Concept_Palimpsest|Концепт Палимпсеста]] | [[10_Mechanics/05_World_Systems/02_Generation/03_Dynamic_Weather|Погода]] | [[10_Mechanics/05_World_Systems/02_Generation/11_Socket_System|Система Сокетов]]
* **Аномалии:** [[10_Mechanics/05_World_Systems/03_Anomaly/Anomaly_System|Система Аномалий]] | [[10_Mechanics/05_World_Systems/03_Anomaly/14_Extraction_System|Эвакуация]]
* **Глобально:** [[10_Mechanics/05_World_Systems/04_Global_Rules/01_Quest_Engine|Квесты]] | [[10_Mechanics/05_World_Systems/04_Global_Rules/03_Persistence_Ledger|Персистентность]]

---

## 20. LORE (Нарратив)

### Фундамент Мира
* [[20_Lore/01_World_Foundation/The_Collapse|Коллапс]]
* [[20_Lore/01_World_Foundation/The_Entity|Сущность]]
* [[20_Lore/01_World_Foundation/Magipunk_Physics|Магипанк Физика]]
* [[20_Lore/01_World_Foundation/The_Anchor|Якорь]]

### Фракции и Общество
* [[20_Lore/02_Societies_Factions/Social_Political_Order|Социальный Строй]]
* [[20_Lore/02_Societies_Factions/The_Cathedral|Собор]]
* [[20_Lore/02_Societies_Factions/The_Cartographers|Картографы]]
* [[20_Lore/02_Societies_Factions/The_Keepers|Хранители]]

### Расы и Культура
* [[20_Lore/04_Species_Cultures/Culture_Language|Язык и Культура]]
* [[20_Lore/04_Species_Cultures/Races/New_Races|Новые Расы]]

### Быт
* [[20_Lore/05_Daily_Life/Fashion_Gear|Мода и Снаряжение]]
* [[20_Lore/05_Daily_Life/Currency_Rezs|Валюта (Лор)]]

---

## 30. CONTENT (Атлас)
*Карты секторов и контент.*

* **Сектор: Порт**
    * [[30_Content/World_Atlas/Sectors/Port/00_Port_Manifest|Манифест Порта]]
    * Таблицы Сложности: [[30_Content/World_Atlas/Sectors/Port/Tables/01_Difficulty|T1]] | [[30_Content/World_Atlas/Sectors/Port/Tables/02_Difficulty|T2]] | [[30_Content/World_Atlas/Sectors/Port/Tables/03_Difficulty|T3]]
