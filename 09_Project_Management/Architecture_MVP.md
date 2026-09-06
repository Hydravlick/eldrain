---
type: project_management
status: active
system: project_management
version: 4
---

# Архитектура GDD и границы MVP

Локальный vault — рабочая поверхность, Git — история и восстановление. Архитектура отвечает за размещение и связность документов; игровые решения принимают активные владельцы в доменах `01_`–`08_`.

## Два пути чтения

Новому дизайнеру: [[01_Core_Vision/GDD_Main]] → [[01_Core_Vision/01_Vision]] → [[01_Core_Vision/02_Core_Loop]] → [[01_Core_Vision/Feature_Map]] → Feature. Feature объясняет цель, сценарии, ожидаемую динамику, UX, зависимости и проверку.

Для правки правила: [[00_Index]] → доменный Route → System/Mechanic → Registry или authored Entity/Content. Lore объясняет людей, историю и причинность мира. View, Base и граф показывают связи источников и не принимают игровое решение.

Feature-страницы находятся в `01_Core_Vision/Features`: это общий путь игрока поверх доменов. Системы поддерживают несколько Features; создавать копию владельца внутри каждой Feature нельзя. Обратные связи и пропуски видны в [[01_Core_Vision/Views/Feature_Owner_Coverage]].

## Домены

| Блок | Роль | Якорные файлы |
|:---|:---|:---|
| `01_Core_Vision` | Концепция, тон, основной цикл | [[01_Core_Vision/GDD_Main]], [[01_Core_Vision/02_Core_Loop]], [[01_Core_Vision/Glossary]] |
| `02_World_Lore` | Ковчег, Коллапс, Якорь, Сущность, магипанк и культуры | [[02_World_Lore/The_Ark]], [[02_World_Lore/The_Collapse]], [[02_World_Lore/The_Anchor]], [[02_World_Lore/Protocol_Resonance]], [[02_World_Lore/Culture_Language]] |
| `03_Factions_Societies` | Фракции, репутация, поручения, допуски, контракты и становление города | [[03_Factions_Societies/Registries/Registry_Factions]], [[03_Factions_Societies/Registries/Registry_Faction_Interfaces]], [[03_Factions_Societies/Reputation_Rules]], [[03_Factions_Societies/Pledge_Contracts]], [[03_Factions_Societies/Quest_Engine]], [[03_Factions_Societies/Lore/City_Genesis]], [[03_Factions_Societies/Lore/Civic_Ethos_Under_Lamps]], [[03_Factions_Societies/Lore/Civic_Order]], [[03_Factions_Societies/Lore/Hearth_Anatomy]], [[03_Factions_Societies/Lore/City_District_Social_Grammar]] |
| `04_Player_Entities` | смертные Пешки, полевой профиль `Race × Spec`, ростер, теги и жизненные последствия | [[04_Player_Entities/Lifecycle_Roster]], [[04_Player_Entities/MVP_3x3_Design_Contract]], [[04_Player_Entities/Combat_Profile_Pipeline]], [[04_Player_Entities/Tags_System]], [[04_Player_Entities/Life_Closure]], [[04_Player_Entities/Registries/Registry_Races]], [[04_Player_Entities/Registries/Registry_Specs]], [[04_Player_Entities/Registries/Registry_Combos]] |
| `05_Combat_Survival` | Бой, магострелы, батареи, статусы, выживание | [[05_Combat_Survival/Combat_Three_Debts]], [[05_Combat_Survival/Weapon_Core]], [[05_Combat_Survival/Magic_Batteries]], [[05_Combat_Survival/Status_Effects]], [[05_Combat_Survival/Dissonance_System]] |
| `06_Economy_Loot` | Рез, бартер, чертежи, экстракция и стабилизация лута | [[06_Economy_Loot/Extraction_Stabilization_Loop]], [[06_Economy_Loot/Economy_Core]], [[06_Economy_Loot/Currency_Rez]], [[06_Economy_Loot/Loot_Distribution]], [[06_Economy_Loot/Barter_System]], [[06_Economy_Loot/Blueprints]], [[06_Economy_Loot/Craft_Modifiers]] |
| `07_Gear_Inventory` | Инвентарь, экипировка, предметы, крафт-реестры | [[07_Gear_Inventory/Inventory_Architecture]], [[07_Gear_Inventory/Thermos_System]], [[07_Gear_Inventory/Thermos_Assembly]], [[07_Gear_Inventory/Registries/Registry_Thermoses]], [[07_Gear_Inventory/Registries/Registry_Thermos_Modules]], [[07_Gear_Inventory/Registries/Registry_Thermos_Interfaces]], [[07_Gear_Inventory/Gear_Progression]], [[07_Gear_Inventory/Equipment_PaperDoll]], [[07_Gear_Inventory/Registries/Registry_Items]] |
| `08_World_Generation` | Сервер, таймеры, аномалии, вход, выход, атлас | [[08_World_Generation/Generation/Server_Lifecycle]], [[08_World_Generation/Generation/Raid_Approach_and_Entry]], [[08_World_Generation/Generation/Egress_Solvency]], [[08_World_Generation/Anomaly/Apex_Last_Hour]], [[08_World_Generation/Anomaly/Anomaly_Core_Loop]] |
| `09_Project_Management` | Канбан, риски, планы, техническая кухня | [[09_Project_Management/TODO]], [[09_Project_Management/Risk_Register]], [[09_Project_Management/Architecture_MVP]] |


## Типы и источник значения

| Тип | Ответственность |
|---|---|
| `core_concept` | Vision, обещание, основной цикл и замысел |
| `feature` | законченная возможность, её сценарии и полнота интеграции |
| `system` | связная модель состояний, переходов и разрешения |
| `mechanic` | локальное действие или правило |
| `content` | авторская конфигурация правил или сценарий; `content_kind` уточняет семейство |
| `entity` | самостоятельная идентичность; `entity_kind` различает race, spec, faction, weapon_frame и location |
| `registry` | схема, стабильные записи и bounded interfaces; для каталога сущностей сами значения остаются на сущностях |
| `lore` | факты мира, культура, вера и историческая причинность |
| `view` | производное представление с `upstream_sources` |
| `index` | навигация |
| `project_management` | открытая работа, риск, решение о размещении |

Race/Spec и оружейный Frame имеют самостоятельные страницы. Их YAML — источник стабильных полей; семейные реестры читают их. Предметы, рецепты, теги и ячейки Combo остаются блоками реестра, пока им не нужен самостоятельный контекст. Вариант оружия остаётся внутри Frame. Большой реестр можно разделить по семейству без изменения ID и формата записи; отдельный файл на каждый ID не обязателен.

Контракт фракционной идентичности и направленных отношений — [[03_Factions_Societies/Registries/Registry_Factions]]; участие институтов в игре — [[03_Factions_Societies/Registries/Registry_Faction_Interfaces]]. Lore не разрешает награду, услугу или право на выход. Лорную синтезирующую прозу сохраняют, даже когда игровое правило переезжает.

## Имена и представления

Домены сохраняют числовой порядок; `00_Index` и `00_Routes` обозначают входы навигации. `01_Vision` → `02_Core_Loop` остаётся короткой последовательностью знакомства. В таблицах Порта `01`–`03` означают реальную сложность, также указанную в properties. Независимые системы Generation, Anomaly и Hub имеют семантические имена; их номера не образовывали pipeline.

`Registries`, `Views`, `Lore` и семейства контента обозначают ответственность. `_Matrices` больше нет. Матрица Двойного Парадокса остаётся System, потому что определяет топологию; Synergy Map читает её. Item Calibration Matrix — View, а состав испытаний задаёт [[07_Gear_Inventory/Calibration_Contract]].

DataviewJS сохраняется. Три таблицы сложности Порта вызывают один `tools/dataview/sector_difficulty/view.js`, передавая свойства wrapper. Ссылки на источники находятся в свойствах; путь custom view — техническая зависимость. Тестовые fixtures находятся в `tools/tests/fixtures`.

## MVP, зрелость и доказательства

[[01_Core_Vision/Build_Extraction_Concept_Slice]] и [[08_World_Generation/Content/Hunt_Frontier_Slice]] задают связный срез; [[09_Project_Management/TODO]] хранит незавершённые работы, [[09_Project_Management/Risk_Register]] — риски и необходимые свидетельства. Не весь объём каждой major Feature входит в первый прототип.

`status: active` означает актуальное описание, а не реализованную систему. `maturity: specified` означает описанные связи; `validation_state: untested` означает отсутствие подтверждённого результата испытаний. Значения `prototype_ready` и `validated` допустимы только после соответствующего свидетельства, а не после проверки Markdown.

## Читаемость и обслуживание

Первый экран объясняет ситуацию до схемы. Схема должна позволять исполнить правило без толкования метафоры. Обещание, цикл, условия и исключения раскрываются по сложности страницы; маленькой Mechanic не нужны пустые разделы. Машинный ключ отделён от имени, а атмосферная фраза сохраняется, когда объясняет цену, последствие или взгляд жителя.

Routes строятся из свойств источников и не редактируются вручную. Для переименования используется установленный Obsidian CLI, затем проверяются ссылки и arbitrary literals в скриптах, запросах и конфигурации. Валидаторы проверяют структуру, но не заменяют чтение и design review.
