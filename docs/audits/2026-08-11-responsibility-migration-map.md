# Pass B responsibility migration map — 2026-08-11

## Scope and verdict

**FRAGILE — complete execution queue closed; unresolved ownership remains explicit.** This
map covers all 116 route owners under `03_Factions_Societies` through
`08_World_Generation`. The 25 scanner-source paths from the prose manifest seed
the detailed entries below. Every route owner now has an evidence-backed
`DETAILED` decision rather than disappearing from Pass B. The map is not itself an edit batch
and does not change a `KEEP` scanner disposition into edit authorization.

The architecture contract requires one mechanic owner for each player-facing
interaction and a separate shared-system owner only where a value or lifecycle
is actually universal. Current detailed decisions contain sixteen `MISSING_OWNER`
rows across explicit owner-gap classes and one `SOURCE_CONFLICT`; no target is
invented for unresolved rows.

Excluded: `02_World_Lore`, all generated route pages, `00_Index.md`, and every
non-owner dependency until a selected route owner makes it directly relevant.

- Route-owner coverage: **116/116**.
- Detailed decisions: **132** — 114 `KEEP`, 16 `MISSING_OWNER`, 1 `SOURCE_CONFLICT`, 1 `MIGRATED`.
- Remaining owner audit queue: none.

## Evidence classes

- **AUTHOR CONSTRAINT:** `01_Core_Vision/01_Vision.md` requires observable
  condition, cost, and failure trace for magic; `01_Core_Vision/02_Core_Loop.md`
  assigns each loop step to its detailed owner rather than the loop overview.
- **GDD FACT:** `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`
  states that an interface record links a faction to one interaction and that
  its `mechanic_owner_ref` resolves eligibility, cost, state, reward, and
  failure. `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`
  assigns policy to one domain owner and labels absent owners `MISSING_OWNER`.
- **GDD FACT:** `07_Gear_Inventory/Thermos_System.md` separates definitions,
  assembly instances, and the Assembly Resolver; its current models and modules
  remain blocked until topology, contracts, ownership links, and calibration
  exist.
- **STRUCTURAL INFERENCE:** a repeated atomic registry field is not duplicated
  normative prose when its record contract makes the field independently
  queryable and declares the resolver elsewhere.
- **EMPIRICAL UNKNOWN / CONTENT GAP:** numeric status values, encounter tuning,
  Thermos topology, coverage, and calibration remain intentionally unresolved;
  none creates a second rule owner.

## Migration index

| Migration | Source | Current role | Decision | Status |
|---|---|---|---|---|
| M-01a | First Reception admission | INTERFACE REGISTRY | Move duplicated continuity lifecycle to Spawn Logic | MIGRATED |
| M-01b | First Reception return | INTERFACE REGISTRY | Retain record boundary | KEEP |
| M-01c | First Reception assessment | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01d | Storehouse reserve release | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01e | Contour attestation | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01f | Weighing provenance | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01g | Artel load order | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01h | Cathedral rite | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01i | Proving repeatability | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01j | Circle temporary pause | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-03 | District grammar | LORE / ENTITY | Retain social grammar | KEEP |
| M-04 | Keepers late reveal | LORE / ENTITY | Retain entity narrative | KEEP |
| M-05 | Quest archive grammar | MECHANIC | Retain quest owner | KEEP |
| M-06 | Reputation consequence | MECHANIC | Retain reputation owner | KEEP |
| M-07 | Race × Spec record | CONTENT INSTANCE | Retain atomic combo record | KEEP |
| M-08 | Active parameter contracts | INTERFACE REGISTRY | Retain contract registry | KEEP |
| M-09 | Status policy contract | SYSTEM | Reconcile active owner with pending contract | SOURCE_CONFLICT |
| M-10 | Foundling history | LORE / ENTITY | Retain Origin context with owner | KEEP |
| M-11 | Status effect records | CONTENT INSTANCE | Retain atomic effect records | KEEP |
| M-13 | Three Debts trace | MECHANIC | Retain combat owner | KEEP |
| M-14 | Traversal geography | MECHANIC | Retain traversal owner | KEEP |
| M-15 | Weapon-frame guidance | PRESENTATION | Retain design guide | KEEP |
| M-16 | Condenser frame records | CONTENT INSTANCE | Retain frame records | KEEP |
| M-17 | Needle frame records | CONTENT INSTANCE | Retain frame records | KEEP |
| M-18 | Pulse frame records | CONTENT INSTANCE | Retain frame records | KEEP |
| M-19 | Scatter frame records | CONTENT INSTANCE | Retain frame records | KEEP |
| M-20 | Rez nature and wallet | MECHANIC | Retain currency owner | KEEP |
| M-21 | Thermos module records | CONTENT INSTANCE | Block pending domain owners | MISSING_OWNER |
| M-22 | Thermos model records | CONTENT INSTANCE | Retain blocked topology | KEEP |
| M-23 | Mutation-line records | CONTENT INSTANCE | Retain line records | KEEP |
| M-24 | Biome-tier records | CONTENT INSTANCE | Retain biome records | KEEP |
| M-25 | Environment-state records | CONTENT INSTANCE | Await exact dungeon resolver | MISSING_OWNER |
| M-26 | Mob and variant records | CONTENT INSTANCE | Retain physiology records | KEEP |
| M-27 | Hub weather presentation | PRESENTATION | Retain downstream link | KEEP |
| M-28 | Реестр: городские Очаги и фракционные адреса | REGISTRY | Retain declared owner boundary | KEEP |
| M-29 | Гражданский порядок Элдрейна | LORE / ENTITY | Block pending civic-order resolver | MISSING_OWNER |
| M-30 | Анатомия Очага | LORE / ENTITY | Block pending Hearth-interaction resolver | MISSING_OWNER |
| M-31 | Поручения, адрес вклада и допуски | MECHANIC | Retain declared owner boundary | KEEP |
| M-32 | Реестр: семейства взаимодействий | REGISTRY | Retain declared owner boundary | KEEP |
| M-33 | Реестр: Расы | REGISTRY | Retain declared owner boundary | KEEP |
| M-34 | Реестр: грамматика и границы навыков | REGISTRY | Retain declared owner boundary | KEEP |
| M-35 | Реестр: Практики / специализации | REGISTRY | Retain declared owner boundary | KEEP |
| M-36 | Реестр личных тегов | REGISTRY | Retain declared owner boundary | KEEP |
| M-37 | Контракт морфологии тела | SYSTEM | Retain declared owner boundary | KEEP |
| M-38 | Адаптивный арсенал и профильные ёмкости | MECHANIC | Retain declared owner boundary | KEEP |
| M-39 | Философия навыков и билдостроения | SYSTEM | Retain declared owner boundary | KEEP |
| M-40 | Логика Спавна и Снаряжения Оболочек | MECHANIC | Retain declared owner boundary | KEEP |
| M-41 | Личные теги: свойства прожитой Пешки | MECHANIC | Retain declared owner boundary | KEEP |
| M-42 | Chronicle: память, а не дерево перков | MECHANIC | Retain declared owner boundary | KEEP |
| M-43 | Реестр оружейных фреймов | REGISTRY | Retain declared owner boundary | KEEP |
| M-44 | Механика: Акустический Шум | MECHANIC | Retain declared owner boundary | KEEP |
| M-45 | Система: Баллистика и Броня | MECHANIC | Retain declared owner boundary | KEEP |
| M-46 | Баллистика PvE: Покров и Рабочий Цикл | MECHANIC | Retain declared owner boundary | KEEP |
| M-47 | Медицина, здоровье и необходимые расходники | MECHANIC | Retain declared owner boundary | KEEP |
| M-48 | Акустический Протокол и VOIP | MECHANIC | Retain declared owner boundary | KEEP |
| M-49 | Механика: Диссонанс (Dissonance) | MECHANIC | Retain declared owner boundary | KEEP |
| M-50 | Полевые Операции с Лутом | MECHANIC | Retain declared owner boundary | KEEP |
| M-51 | Охота на фронтире Аномалии | MECHANIC | Retain declared owner boundary | KEEP |
| M-52 | Система: Магия и Батареи | MECHANIC | Retain declared owner boundary | KEEP |
| M-53 | Маски: Ключ от Мира | MECHANIC | Retain declared owner boundary | KEEP |
| M-54 | Механика: Физика Движения | MECHANIC | Retain declared owner boundary | KEEP |
| M-55 | Механика: Пороги Давления Аномалии (Dissonance Thresholds) | MECHANIC | Retain declared owner boundary | KEEP |
| M-56 | Оружие: Магострельный Канон и Тиры | MECHANIC | Retain declared owner boundary | KEEP |
| M-57 | Оружие: ближний бой | MECHANIC | Retain declared owner boundary | KEEP |
| M-58 | Оружие: дальний бой | MECHANIC | Retain declared owner boundary | KEEP |
| M-59 | Адресный Бартер | MECHANIC | Retain declared owner boundary | KEEP |
| M-60 | Ограниченные Чертежи | MECHANIC | Retain declared owner boundary | KEEP |
| M-61 | Вариантный Ингредиент | MECHANIC | Retain declared owner boundary | KEEP |
| M-62 | Экономика: От Риска к Адресу | MECHANIC | Retain declared owner boundary | KEEP |
| M-63 | Экстракция, стабилизация и наследие сектора | MECHANIC | Retain declared owner boundary | KEEP |
| M-64 | Распределение Лута | MECHANIC | Retain declared owner boundary | KEEP |
| M-65 | Происхождение Лута и Цикл Синхронизации | MECHANIC | Retain declared owner boundary | KEEP |
| M-66 | Физическая Передача Между Игроками | MECHANIC | Retain declared owner boundary | KEEP |
| M-67 | Цикл Ресурсов: Состав и Адрес | MECHANIC | Retain declared owner boundary | KEEP |
| M-68 | Return Manifest Contract | SYSTEM | Retain declared owner boundary | KEEP |
| M-69 | Расходы и Вывод Валюты (Money Sinks) | MECHANIC | Retain declared owner boundary | KEEP |
| M-70 | Адреса, Поставщики и Мастера | MECHANIC | Retain declared owner boundary | KEEP |
| M-71 | Реестр: LimitedBlueprint | REGISTRY | Retain declared owner boundary | KEEP |
| M-72 | Реестр: необходимые расходники и экспедиционные предметы | REGISTRY | Retain declared owner boundary | KEEP |
| M-73 | Реестр: Адресные RecipeTransaction | REGISTRY | Retain declared owner boundary | KEEP |
| M-74 | Реестр: Маски и Шлемы (Protective Gear) | REGISTRY | Retain declared owner boundary | KEEP |
| M-75 | Реестр: Предметы и Ресурсы (General Items) | REGISTRY | Retain declared owner boundary | KEEP |
| M-76 | Реестр интерфейсов Термоса | INTERFACE / REGISTRY | Retain declared owner boundary | KEEP |
| M-77 | Грамматика Аффиксов | MECHANIC | Retain declared owner boundary | KEEP |
| M-78 | Механика: Контейнеры и Слоты (Containers Hierarchy) | MECHANIC | Retain declared owner boundary | KEEP |
| M-79 | Механика: Диссонанс Предмета (Dissonance Value) | MECHANIC | Retain declared owner boundary | KEEP |
| M-80 | Кукла Персонажа (Equipment Slots) | MECHANIC | Retain declared owner boundary | KEEP |
| M-81 | Визуальный язык Термоса | MECHANIC | Retain declared owner boundary | KEEP |
| M-82 | Прогрессия Снаряжения | MECHANIC | Retain declared owner boundary | KEEP |
| M-83 | Механика: Архитектура Инвентаря (Mass & Access) | MECHANIC | Retain declared owner boundary | KEEP |
| M-84 | Система: Удобство и Сортировка (QoL) | MECHANIC | Retain declared owner boundary | KEEP |
| M-85 | Атрибуты Предмета и UI (Item Passport) | PRESENTATION | Retain declared owner boundary | KEEP |
| M-86 | Процесс Обыска (Interaction Loop) | MECHANIC | Retain declared owner boundary | KEEP |
| M-87 | Механика: Физический Вес (Physical Weight) | MECHANIC | Retain declared owner boundary | KEEP |
| M-88 | Архитектура Схрона и Менеджмент (Stash & Organization) | MECHANIC | Retain declared owner boundary | KEEP |
| M-89 | Сборка Термоса | SYSTEM | Retain declared owner boundary | KEEP |
| M-90 | Термос: носимая система экипировки | SYSTEM | Retain declared owner boundary | KEEP |
| M-91 | Реестр: Объекты Карты (Map Table Objects) | REGISTRY | Retain declared owner boundary | KEEP |
| M-92 | Registry: Raid Interfaces | INTERFACE / REGISTRY | Explicit UI_PROJECTION gap remains blocked | MISSING_OWNER |
| M-93 | Ядро Аномалии: Правила Арены | MECHANIC | Retain declared owner boundary | KEEP |
| M-94 | Опасности Среды | MECHANIC | Retain declared owner boundary | KEEP |
| M-95 | Insertion Logic | SYSTEM | Retain declared owner boundary | KEEP |
| M-96 | Нестабильные Пороги: обычный выход | SYSTEM | Retain declared owner boundary | KEEP |
| M-97 | Система линий мутаций Аномалии | MECHANIC | Retain declared owner boundary | KEEP |
| M-98 | Apex Last Hour | SYSTEM | Explicit UI_PROJECTION gap remains blocked | MISSING_OWNER |
| M-99 | Система: Аномалии (The Anomaly Engine) | MECHANIC | Retain declared owner boundary | KEEP |
| M-100 | CityState и жизненный цикл городских явлений | SYSTEM | Retain declared owner boundary | KEEP |
| M-101 | Ночные Верстаки | MECHANIC | Retain declared owner boundary | KEEP |
| M-102 | Динамическая Погода | SYSTEM | Retain declared owner boundary | KEEP |
| M-103 | Ротация Активных и Stable-Секторов | SYSTEM | Retain declared owner boundary | KEEP |
| M-104 | Слоты Сложности (Tier Spread) | MECHANIC | Retain declared owner boundary | KEEP |
| M-105 | Асинхронные таймеры и regional service | SYSTEM | Retain declared owner boundary | KEEP |
| M-106 | Жизненный цикл сервера | SYSTEM | Explicit LIFECYCLE_RESOLVER gap remains blocked | MISSING_OWNER |
| M-107 | Гейт-проверка | MECHANIC | Retain declared owner boundary | KEEP |
| M-108 | Логика Респавна Лута | MECHANIC | Retain declared owner boundary | KEEP |
| M-109 | Топология Мира: Паттерн "Цветок" | SYSTEM | Retain declared owner boundary | KEEP |
| M-110 | Система Сокетов (Socket System) | SYSTEM | Retain declared owner boundary | KEEP |
| M-111 | Стратегии Генерации Города | SYSTEM | Retain declared owner boundary | KEEP |
| M-112 | Асинхронная Архитектура Мира | SYSTEM | Retain declared owner boundary | KEEP |
| M-113 | Правила Наполнения Сектора | SYSTEM | Retain declared owner boundary | KEEP |
| M-114 | Слой Связности (Connectivity Layer) | MECHANIC | Retain declared owner boundary | KEEP |
| M-115 | Протокол Данных Мини-карты | PRESENTATION | Retain declared owner boundary | KEEP |
| M-116 | Raid Approach and Entry | SYSTEM | Explicit UI_PROJECTION gap remains blocked | MISSING_OWNER |
| M-117 | Egress Solvency | SYSTEM | Retain declared owner boundary | KEEP |
| M-118 | Жизненный цикл ревизии локации | SYSTEM | Retain declared owner boundary | KEEP |
| M-119 | Хаб: Операционный Бункер | MECHANIC | Retain declared owner boundary | KEEP |
| M-120 | Живая Миниатюра: Карта Рейдов и Адресов | MECHANIC | Retain declared owner boundary | KEEP |
| M-121 | Сервисы Хаба: Работа Через Диораму | MECHANIC | Retain declared owner boundary | KEEP |
| M-122 | Интерактивный Стол: Мирная Проекция | MECHANIC | Retain declared owner boundary | KEEP |
| M-123 | Система Группы: Протокол "Стол" | MECHANIC | Retain declared owner boundary | KEEP |
| M-124 | Гроссбух: Архитектура Сохранений | MECHANIC | Retain declared owner boundary | KEEP |
| M-125 | Целостность Реальности (Security & Validation) | MECHANIC | Retain declared owner boundary | KEEP |

## Complete route-owner coverage

This list is the Pass B work queue, not a blanket approval. `DETAILED` points
to an existing entry below. `AUDIT_REQUIRED` means the executor must read that
owner and its direct dependencies, then replace the coverage status with
`DETAILED` and add a supported `KEEP`, `MIXED_AUTHORITY`,
`DUPLICATE_RULE`, `MISSING_OWNER`, or `SOURCE_CONFLICT` entry before the
owner can close. Primary responsibility is seeded from current metadata and
must be corrected when owner-scoped evidence disagrees.

### 03_Factions_Societies

- [owner_path:: 03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md] [primary_responsibility:: INTERFACE_REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-01a..M-01j]
- [owner_path:: 03_Factions_Societies/_Registries/Registry_Factions.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-28]
- [owner_path:: 03_Factions_Societies/Lore/City_District_Social_Grammar.md] [primary_responsibility:: LORE_ENTITY] [coverage_status:: DETAILED] [detail_ref:: M-03]
- [owner_path:: 03_Factions_Societies/Lore/Civic_Order.md] [primary_responsibility:: LORE_ENTITY] [coverage_status:: DETAILED] [detail_ref:: M-29]
- [owner_path:: 03_Factions_Societies/Lore/Hearth_Anatomy.md] [primary_responsibility:: LORE_ENTITY] [coverage_status:: DETAILED] [detail_ref:: M-30]
- [owner_path:: 03_Factions_Societies/Pledge_Contracts.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-31]
- [owner_path:: 03_Factions_Societies/Reputation_Rules.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-06]
### 04_Player_Entities

- [owner_path:: 04_Player_Entities/_Registries/Registry_Combos.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-07]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Interaction_Families.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-32]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Parameter_Contracts.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-08,M-09]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Races.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-33]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Skill_Types.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-34]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Specs.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-35]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Tags.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-36]
- [owner_path:: 04_Player_Entities/Body_Morphology_Contract.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-37]
- [owner_path:: 04_Player_Entities/Proficiency_Arsenal.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-38]
- [owner_path:: 04_Player_Entities/Shell_Foundlings.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-10]
- [owner_path:: 04_Player_Entities/Skill_Build_Philosophy.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-39]
- [owner_path:: 04_Player_Entities/Spawn_Logic.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-40]
- [owner_path:: 04_Player_Entities/Tags_System.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-41]
- [owner_path:: 04_Player_Entities/Trait_Development.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-42]
### 05_Combat_Survival

- [owner_path:: 05_Combat_Survival/_Registries/Registry_StatusEffects.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-11]
- [owner_path:: 05_Combat_Survival/_Registries/Registry_Weapons.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-43]
- [owner_path:: 05_Combat_Survival/Acoustic_Stealth.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-44]
- [owner_path:: 05_Combat_Survival/Ballistics_Armor.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-45]
- [owner_path:: 05_Combat_Survival/Ballistics_PvE.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-46]
- [owner_path:: 05_Combat_Survival/Combat_Consumables.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-47]
- [owner_path:: 05_Combat_Survival/Combat_Three_Debts.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-13]
- [owner_path:: 05_Combat_Survival/Communication_Vox.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-48]
- [owner_path:: 05_Combat_Survival/Dissonance_System.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-49]
- [owner_path:: 05_Combat_Survival/Field_Crafting.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-50]
- [owner_path:: 05_Combat_Survival/Hunt_Frontier_Loop.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-51]
- [owner_path:: 05_Combat_Survival/Magic_Batteries.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-52]
- [owner_path:: 05_Combat_Survival/Masks_Filters.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-53]
- [owner_path:: 05_Combat_Survival/Movement_Physics.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-54]
- [owner_path:: 05_Combat_Survival/Status_Effects.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-09]
- [owner_path:: 05_Combat_Survival/Threat_Thresholds.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-55]
- [owner_path:: 05_Combat_Survival/Traversal_Core.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-14]
- [owner_path:: 05_Combat_Survival/Weapon_Core.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-56]
- [owner_path:: 05_Combat_Survival/Weapon_Melee.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-57]
- [owner_path:: 05_Combat_Survival/Weapon_Ranged.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-58]
### 06_Economy_Loot

- [owner_path:: 06_Economy_Loot/Barter_System.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-59]
- [owner_path:: 06_Economy_Loot/Blueprints.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-60]
- [owner_path:: 06_Economy_Loot/Craft_Modifiers.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-61]
- [owner_path:: 06_Economy_Loot/Currency_Rez.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-20]
- [owner_path:: 06_Economy_Loot/Economy_Core.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-62]
- [owner_path:: 06_Economy_Loot/Extraction_Stabilization_Loop.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-63]
- [owner_path:: 06_Economy_Loot/Loot_Distribution.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-64]
- [owner_path:: 06_Economy_Loot/Loot_Sync_Cycle.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-65]
- [owner_path:: 06_Economy_Loot/P2P_Interaction.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-66]
- [owner_path:: 06_Economy_Loot/Resource_Cycle.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-67]
- [owner_path:: 06_Economy_Loot/Return_Manifest_Contract.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-68]
- [owner_path:: 06_Economy_Loot/Sinks_Insurance.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-69]
- [owner_path:: 06_Economy_Loot/Vendor_Logic.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-70]
### 07_Gear_Inventory

- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Blueprints.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-71]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Consumables.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-72]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_CraftingRecipes.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-73]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Headwear.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-74]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Items.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-75]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces.md] [primary_responsibility:: INTERFACE_REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-76]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Thermos_Modules.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-21]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Thermoses.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-22]
- [owner_path:: 07_Gear_Inventory/Affix_Grammar.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-77]
- [owner_path:: 07_Gear_Inventory/Containers_Slots.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-78]
- [owner_path:: 07_Gear_Inventory/Dissonance_Value.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-79]
- [owner_path:: 07_Gear_Inventory/Equipment_PaperDoll.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-80]
- [owner_path:: 07_Gear_Inventory/Fashion_Gear.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-81]
- [owner_path:: 07_Gear_Inventory/Gear_Progression.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-82]
- [owner_path:: 07_Gear_Inventory/Inventory_Architecture.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-83]
- [owner_path:: 07_Gear_Inventory/Inventory_QoL.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-84]
- [owner_path:: 07_Gear_Inventory/Item_Attributes_UI.md] [primary_responsibility:: PRESENTATION] [coverage_status:: DETAILED] [detail_ref:: M-85]
- [owner_path:: 07_Gear_Inventory/Looting_Process.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-86]
- [owner_path:: 07_Gear_Inventory/Physical_Weight.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-87]
- [owner_path:: 07_Gear_Inventory/Stash_Architecture.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-88]
- [owner_path:: 07_Gear_Inventory/Thermos_Assembly.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-89]
- [owner_path:: 07_Gear_Inventory/Thermos_System.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-90]
### 08_World_Generation

- [owner_path:: 08_World_Generation/_Registries/Registry_Anomaly_Mutations.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-23]
- [owner_path:: 08_World_Generation/_Registries/Registry_Biomes.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-24]
- [owner_path:: 08_World_Generation/_Registries/Registry_Environment_States.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-25]
- [owner_path:: 08_World_Generation/_Registries/Registry_Mobs.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-26]
- [owner_path:: 08_World_Generation/_Registries/Registry_POIs.md] [primary_responsibility:: REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-91]
- [owner_path:: 08_World_Generation/_Registries/Registry_Raid_Interfaces.md] [primary_responsibility:: INTERFACE_REGISTRY] [coverage_status:: DETAILED] [detail_ref:: M-92]
- [owner_path:: 08_World_Generation/Anomaly/00_Anomaly_Core_Loop.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-93]
- [owner_path:: 08_World_Generation/Anomaly/05_Hazards_Traps.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-94]
- [owner_path:: 08_World_Generation/Anomaly/13_Insertion_Logic.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-95]
- [owner_path:: 08_World_Generation/Anomaly/14_Extraction_System.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-96]
- [owner_path:: 08_World_Generation/Anomaly/16_Anomaly_Mutation_Lines.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-97]
- [owner_path:: 08_World_Generation/Anomaly/17_Apex_Last_Hour.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-98]
- [owner_path:: 08_World_Generation/Anomaly/Anomaly_System.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-99]
- [owner_path:: 08_World_Generation/City_State/Civic_Event_Lifecycle.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-100]
- [owner_path:: 08_World_Generation/Generation/02_Mechanic_Night_Benches.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-101]
- [owner_path:: 08_World_Generation/Generation/03_Dynamic_Weather.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-102]
- [owner_path:: 08_World_Generation/Generation/04_Global_Map_Rotation.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-103]
- [owner_path:: 08_World_Generation/Generation/05_Difficulty_Slots.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-104]
- [owner_path:: 08_World_Generation/Generation/06_Async_Timers.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-105]
- [owner_path:: 08_World_Generation/Generation/07_Server_Lifecycle.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-106]
- [owner_path:: 08_World_Generation/Generation/08_Gate_Check.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-107]
- [owner_path:: 08_World_Generation/Generation/09_Loot_Respawn.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-108]
- [owner_path:: 08_World_Generation/Generation/10_World_Topology.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-109]
- [owner_path:: 08_World_Generation/Generation/11_Socket_System.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-110]
- [owner_path:: 08_World_Generation/Generation/12_Generation_Strategies.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-111]
- [owner_path:: 08_World_Generation/Generation/13_Async_Double_Buffer.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-112]
- [owner_path:: 08_World_Generation/Generation/14_Sector_Content_Rules.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-113]
- [owner_path:: 08_World_Generation/Generation/15_Traversal_Shortcuts.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-114]
- [owner_path:: 08_World_Generation/Generation/16_UI_Map_Protocol.md] [primary_responsibility:: PRESENTATION] [coverage_status:: DETAILED] [detail_ref:: M-115]
- [owner_path:: 08_World_Generation/Generation/19_Raid_Approach_and_Entry.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-116]
- [owner_path:: 08_World_Generation/Generation/20_Egress_Solvency.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-117]
- [owner_path:: 08_World_Generation/Generation/21_Location_Revision_Lifecycle.md] [primary_responsibility:: SYSTEM] [coverage_status:: DETAILED] [detail_ref:: M-118]
- [owner_path:: 08_World_Generation/Hub/00_Hub_Environment.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-119]
- [owner_path:: 08_World_Generation/Hub/01_Hub_Map_Table.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-120]
- [owner_path:: 08_World_Generation/Hub/02_Hub_Services_Interaction.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-121]
- [owner_path:: 08_World_Generation/Hub/03_Hub_Map_Interaction.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-122]
- [owner_path:: 08_World_Generation/Hub/04_Time_Atmosphere.md] [primary_responsibility:: PRESENTATION] [coverage_status:: DETAILED] [detail_ref:: M-27]
- [owner_path:: 08_World_Generation/Hub/05_Party_Syndicate.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-123]
- [owner_path:: 08_World_Generation/Persistence_Ledger.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-124]
- [owner_path:: 08_World_Generation/Reality_Integrity.md] [primary_responsibility:: MECHANIC] [coverage_status:: DETAILED] [detail_ref:: M-125]

## Entry evidence and boundaries

### M-01a — `first_reception.continuity_admission_presentation`

- Source evidence: `03_Factions_Societies/Lore/The_First_Reception.md`, `## Протокол нулевого ростера`, formerly duplicated the Continuity Admission predicate, Ward creation, Welfare, tag, and raid-entry lifecycle already resolved in Spawn Logic.
- Target owner: `04_Player_Entities/Spawn_Logic.md#2. Первый Приём при ContinuityAdmissionAllowed` owns that resolution; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` retains the normalized participation record.
- Entity role: First Reception is `PROVIDER`.
- Mechanic owner: `04_Player_Entities/Spawn_Logic.md`.
- Universal system owner: `04_Player_Entities/Lifecycle_Roster.md` owns shared roster lifecycle; it is a dependency, not this interaction's resolver.
- Does not own: PawnID creation, continuity epoch, readiness resolution, welfare eligibility, tag assignment, or lifecycle settlement.
- Direct consumers and linked pages: `04_Player_Entities/Spawn_Logic.md`, `04_Player_Entities/Lifecycle_Roster.md`, and `03_Factions_Societies/Lore/The_First_Reception.md`.
- Preserved meaning: First Reception remains the civic `PROVIDER` that presents one named living candidate, while the roster predicate, atomic Ward creation, Welfare, tag, and raid-entry resolution remain singular in their existing owners.
- Required skill or handoff: architecture lead, curator boundary check, and lorekeeper faction-interface check; no further handoff changes the evidence.
- Approval and validation: `MIGRATED`. The full duplicated lore section was replaced with an entity-facing summary and direct links to Spawn Logic, Lifecycle Roster, and this interface record; the record now names its resolved Ready-Ward result. Validate protected structure, exact diffs, and the non-empty `does_not_own` boundary.

### M-01b — `first_reception.first_return_presentation`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### first_reception.first_return_presentation`, lines 95–108; scanner line 106.
- Target owner: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` owns this normalized participation record.
- Entity role: First Reception is `PRESENTER`.
- Mechanic owner: `04_Player_Entities/Tags_System.md`.
- Universal system owner: none; `04_Player_Entities/Trait_Development.md` is a dependency, not a universal resolver for the presentation.
- Does not own: First Return predicate, TagID assignment, Dawn settlement, tag-slot accounting, or combat resolution.
- Direct consumers and linked pages: `04_Player_Entities/Tags_System.md`, `04_Player_Entities/Trait_Development.md`, and `03_Factions_Societies/Lore/The_First_Reception.md`.
- Preserved meaning: an immutable revealed TagID and a readable result cross one bounded interface.
- Required skill or handoff: architecture lead, curator boundary check, and lorekeeper faction-interface check; no further handoff changes the evidence.
- Approval and validation: no migration. Validate one non-missing mechanic owner and this record's non-empty `does_not_own` boundary.

### M-01c — `first_reception.quarantine_assessment`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### first_reception.quarantine_assessment`, lines 114–127; scanner lines 124–125.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: First Reception is `WITNESS`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `04_Player_Entities/Lifecycle_Roster.md` is a dependency and cannot be inferred as resolver.
- Does not own: personhood, custody, property, permanent access, city-wide quarantine, or treatment resolution.
- Direct consumers and linked pages: `04_Player_Entities/Lifecycle_Roster.md` and `03_Factions_Societies/Lore/The_First_Reception.md`.
- Preserved meaning: identity, observed signs, assessed risk, uncertainty, and expiry remain the minimum boundary.
- Required skill or handoff: lorekeeper confirms witness authority is not runtime authority; architecture lead confirms dependency is not ownership.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define the assessment state machine and source of truth.

### M-01d — `common_storehouses.emergency_reserve_release`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### common_storehouses.emergency_reserve_release`, lines 129–142; scanner line 138.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Common Storehouses is `PROVIDER`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `06_Economy_Loot/Economy_Core.md` is a dependency and cannot be inferred as resolver.
- Does not own: item prices, Welfare predicate, vendor-stock generation, stash capacity, or debt settlement.
- Direct consumers and linked pages: `06_Economy_Loot/Economy_Core.md` and `03_Factions_Societies/Lore/The_Common_Storehouses.md`.
- Preserved meaning: branch, reserve, protected minimum, amount, reason, witnesses, and review time remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define release, refusal, review, and failure handling.

### M-01e — `contour_chamber.evidence_attestation`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### contour_chamber.evidence_attestation`, lines 144–157; scanner line 153.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Contour Chamber is `WITNESS`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `08_World_Generation/Hub/01_Hub_Map_Table.md` is a dependency and cannot be inferred as resolver.
- Does not own: guilt, ownership, biological status, global truth, route eligibility, or fog-of-war resolution.
- Direct consumers and linked pages: `08_World_Generation/Hub/01_Hub_Map_Table.md` and `03_Factions_Societies/Lore/The_Contour_Chamber.md`.
- Preserved meaning: observation, place, time, method, witnesses, uncertainty, and version remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define attestation scope, versioning, and refusal.

### M-01f — `weighing_houses.provenance_adjudication`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### weighing_houses.provenance_adjudication`, lines 159–172; scanner line 168.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Weighing Houses is `WITNESS`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `06_Economy_Loot/Loot_Sync_Cycle.md` is a dependency and cannot be inferred as resolver.
- Does not own: human guilt, universal property law, item value, barter result, debt collection, or physical transfer.
- Direct consumers and linked pages: `06_Economy_Loot/Loot_Sync_Cycle.md` and `03_Factions_Societies/Lore/The_Weighing_Houses.md`.
- Preserved meaning: object identity, transfer signatures, custody, conflicts, scope, and expiry remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define the evidence and adjudication lifecycle.

### M-01g — `support_artels.infrastructure_load_order`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### support_artels.infrastructure_load_order`, lines 174–187; scanner line 183.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Support Artels is `WITNESS`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `08_World_Generation/Hub/01_Hub_Map_Table.md` is a dependency and cannot be inferred as resolver.
- Does not own: district evacuation, player access, item durability, armor repair, route generation, or permanent ownership.
- Direct consumers and linked pages: `08_World_Generation/Hub/01_Hub_Map_Table.md` and `03_Factions_Societies/Lore/The_Support_Artels.md`.
- Preserved meaning: structure, observed load, local testimony, calculation holder, and review time remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define recommendation lifetime and release conditions.

### M-01h — `cathedral.ritual_stress_service`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### cathedral.ritual_stress_service`, lines 189–202; scanner line 198.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Cathedral of All Faiths is `PROVIDER`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `05_Combat_Survival/Status_Effects.md` is a dependency and cannot be inferred as resolver.
- Does not own: proof of gods, generic combat buff, status resolution, relic effects, contract reward, or raid alliance.
- Direct consumers and linked pages: `05_Combat_Survival/Status_Effects.md` and `03_Factions_Societies/Lore/The_Cathedral.md`.
- Preserved meaning: participant consent, rite, state, duration, failure, and exit remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define the stress-state transition, refusal, and failure.

### M-01i — `proving_houses.repeatability_attestation`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### proving_houses.repeatability_attestation`, lines 204–217; scanner line 213.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Proving Houses is `WITNESS`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `07_Gear_Inventory/_Registries/Registry_CraftingRecipes.md` is a dependency and cannot be inferred as resolver.
- Does not own: all research, education, item identification, recipe unlock, crafting result, or universal sales ban.
- Direct consumers and linked pages: `07_Gear_Inventory/_Registries/Registry_CraftingRecipes.md` and `03_Factions_Societies/Lore/The_Proving_Houses.md`.
- Preserved meaning: sample owner, conditions, independent repetitions, failure mode, and harm owner remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define the attestation state and review outcome.

### M-01j — `circle_of_interposition.temporary_pause`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### circle_of_interposition.temporary_pause`, lines 219–232; scanner line 228.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Circle of Interposition is `PROVIDER`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `03_Factions_Societies/Pledge_Contracts.md` is a dependency and cannot be inferred as resolver.
- Does not own: guilt, investigation, custody, property, biological status, permanent imprisonment, or city-wide law.
- Direct consumers and linked pages: `03_Factions_Societies/Pledge_Contracts.md` and `03_Factions_Societies/Lore/The_Circle_of_Interposition.md`.
- Preserved meaning: subject, harm, pause holder, witness, scope, expiry, and release condition remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define the timed-pause state, extension, and release.

### M-03 — district grammar

- Source evidence: `03_Factions_Societies/Lore/City_District_Social_Grammar.md`, `## Район как зависимость`, line 31.
- Target owner: `03_Factions_Societies/Lore/City_District_Social_Grammar.md`.
- Entity role: district identity, social dependency, temporary authority, and civic memory.
- Mechanic owner: none claimed; location geometry and routes are expressly deferred to world-generation owners.
- Universal system owner: `08_World_Generation/City_State/Civic_Event_Lifecycle.md` only for shared CivicEvent outcomes.
- Does not own: geometry, POI, street generation, routes, or physical state.
- Direct consumers and linked pages: `03_Factions_Societies/Lore/City_Genesis.md`, `03_Factions_Societies/Lore/Civic_Order.md`, `03_Factions_Societies/Lore/Civic_Ethos_Under_Lamps.md`, `03_Factions_Societies/Lore/Hearth_Anatomy.md`, `03_Factions_Societies/Lore/The_Cathedral.md`, `08_World_Generation/Anomaly/Anomaly_System.md`, `08_World_Generation/City_State/Civic_Event_Lifecycle.md`, and `08_World_Generation/Districts/City_Center.md`.
- Preserved meaning: the candidate supplies a concrete social test, not a location-generation rule.
- Required skill or handoff: lorekeeper evidence applied; no handoff because no runtime rule is asserted.
- Approval and validation: no migration; preserve the stated physical-location boundary.

### M-04 — Keepers late reveal

- Source evidence: `03_Factions_Societies/Lore/The_Keepers.md`, `## Позднее Прямое Общение`, line 177.
- Target owner: `03_Factions_Societies/Lore/The_Keepers.md`.
- Entity role: the Keepers observe and eventually present a narrative recognition of the Shard.
- Mechanic owner: none is asserted by the candidate paragraph.
- Universal system owner: none.
- Does not own: roster metaphysics, late-meta progression predicate, Tag assignment, contract lifecycle, reward, or access resolution.
- Direct consumers and linked pages: `03_Factions_Societies/Quest_Engine.md`, `03_Factions_Societies/_Registries/Registry_Factions.md`, `03_Factions_Societies/Pledge_Contracts.md`, `03_Factions_Societies/Lore/Faction_Address_System.md`, and `03_Factions_Societies/Lore/The_Circle_of_Interposition.md`; these links do not transfer runtime ownership.
- Preserved meaning: the late reveal is causal lore with intentionally incomplete Keeper knowledge.
- Required skill or handoff: lorekeeper verdict `CANON` for entity/narrative placement; no additional handoff.
- Approval and validation: no migration; any implementation of the late condition requires a separately scoped mechanic-owner audit.

### M-05 — quest archive grammar

- Source evidence: `03_Factions_Societies/Quest_Engine_Grammar.md`, `## 7. Сохранение и журнал` and `### Гроссбух`, line 230.
- Target owner: `03_Factions_Societies/Quest_Engine_Grammar.md`; `03_Factions_Societies/Quest_Engine.md` is its direct mechanic dependency.
- Entity role: an issuer or address may supply a contract seed but owns no archive result.
- Mechanic owner: Quest Engine.
- Universal system owner: none.
- Does not own: faction identity, roster state, hub POI state, or server lifecycle.
- Direct consumers and linked pages: `03_Factions_Societies/Quest_Engine.md`, `03_Factions_Societies/Reputation_Rules.md`, `03_Factions_Societies/Lore/Faction_Address_System.md`, `04_Player_Entities/Trait_Development.md`, `04_Player_Entities/Shell_Foundlings.md`, `04_Player_Entities/Lifecycle_Roster.md`, `08_World_Generation/Hub/01_Hub_Map_Table.md`, and `08_World_Generation/Generation/07_Server_Lifecycle.md`.
- Preserved meaning: archive fields describe the player-visible contract outcome and remain queryable.
- Required skill or handoff: architecture and curator evidence; no specialist question remained.
- Approval and validation: no migration; retain the listed direct-owner links.

### M-06 — reputation consequence

- Source evidence: `03_Factions_Societies/Reputation_Rules.md`, `### Спорный контракт`, line 55.
- Target owner: `03_Factions_Societies/Reputation_Rules.md`.
- Entity role: a Hearth or faction supplies an address and in-world consequence.
- Mechanic owner: Reputation Rules.
- Universal system owner: none proven.
- Does not own: faction membership, generic vendor stock, contract lifecycle, or a city-wide hidden score.
- Direct consumers and linked pages: `03_Factions_Societies/_Registries/Registry_Factions.md`, `03_Factions_Societies/Lore/Faction_Address_System.md`, `03_Factions_Societies/Lore/The_Circle_of_Interposition.md`, `06_Economy_Loot/Vendor_Logic.md`, and `03_Factions_Societies/Pledge_Contracts.md`.
- Preserved meaning: a contested contract carries a political consequence visible to the player.
- Required skill or handoff: lorekeeper confirms the faction framing does not grant resolver authority.
- Approval and validation: no migration; keep explicit feedback and negative membership boundary.

### M-07 — Race × Spec record

- Source evidence: `04_Player_Entities/_Registries/Registry_Combos.md`, `## Крыса × Ладчик`, line 259.
- Target owner: `04_Player_Entities/_Registries/Registry_Combos.md`.
- Entity role: a combo is an authored player-content coordinate, not a faction or runtime entity.
- Mechanic owner: Combat Profile Pipeline consumes the selected record.
- Universal system owner: none; the registry delegates P/Q/E contracts and module effects.
- Does not own: personal MasteryContribution, inherited unknown abilities, P/Q/E resolution, or module-effect policy.
- Direct consumers and linked pages: `04_Player_Entities/MVP_3x3_Design_Contract.md`, `04_Player_Entities/_Registries/Registry_Races.md`, `04_Player_Entities/_Registries/Registry_Specs.md`, `04_Player_Entities/Combat_Profile_Pipeline.md`, `04_Player_Entities/Proficiency_Arsenal.md`, and `07_Gear_Inventory/Thermos_System.md`.
- Preserved meaning: repeated profile fields are atomic content-instance records; pending cells remain pending.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration; do not normalize repeated fields into prose.

### M-08 — active parameter contracts

- Source evidence: `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`, `## Активные домены`, lines 44–128; scanner lines 61–63, 74, 102, and 114.
- Target owner: `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`.
- Entity role: sources submit modifier requests; none receives entity-level authority from the registry.
- Mechanic owner: the declared domain owners, including Weapon Ranged, Skill Build Philosophy, Dissonance System, Ballistics Armor, Physical Weight, and Magic Batteries.
- Universal system owner: each named `domain_owner` only inside its own parameter domain.
- Does not own: source values, unrelated domains, or a global rating.
- Direct consumers and linked pages: `04_Player_Entities/Combat_Profile_Pipeline.md`, `04_Player_Entities/Skill_Build_Philosophy.md`, `05_Combat_Survival/Magic_Batteries.md`, `05_Combat_Survival/Dissonance_System.md`, `07_Gear_Inventory/Thermos_Assembly.md`, and `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces.md`.
- Preserved meaning: the record maps authority to modify a result without duplicating the result’s values.
- Required skill or handoff: architecture lead and curator boundary check; no handoff.
- Approval and validation: no migration; retain one declared domain owner per active contract.

### M-09 — status application policy

- Source evidence: `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`, `### status_application_policy` and its warning, lines 80–93; `05_Combat_Survival/Status_Effects.md`, `## 3. Применение` and `## 5. Повтор и Hard Control`; and the record contract in `05_Combat_Survival/_Registries/Registry_StatusEffects.md`.
- Target owner: `SOURCE_CONFLICT`. The active route owner `05_Combat_Survival/Status_Effects.md` already defines application modes, repeat rules, hard-control diminishing, and shared control-family history, while the pending parameter contract still declares `domain_owner:: MISSING_OWNER`.
- Entity role: none.
- Mechanic owner: `05_Combat_Survival/Status_Effects.md` is the active mechanic owner; the registry remains the atomic effect-record owner and is not a universal resolver.
- Universal system owner: the current evidence points to `05_Combat_Survival/Status_Effects.md` for shared application and repeat policy, but the parameter-contract projection disagrees. Do not create a second owner to conceal that conflict.
- Does not own: individual effect values, source-local action results, environmental scene instances, or undocumented cross-domain priority/floor/cap rules.
- Direct consumers and linked pages: `05_Combat_Survival/_Registries/Registry_StatusEffects.md`, `08_World_Generation/_Registries/Registry_Environment_States.md`, and `05_Combat_Survival/Dissonance_System.md`.
- Preserved meaning: atomic effect records and the global-versus-local environment boundary stay intact; no source may invent an undocumented priority, floor, or cap.
- Required skill or handoff: architecture lead reconciles the two active owners; curator verifies registry and environment boundaries.
- Approval and validation: **APPROVAL_REQUIRED** for one architecture decision. If `Status_Effects.md` is confirmed as the domain owner, `eldraine-gdd-author` updates `status_application_policy` and removes the stale missing-owner warning; otherwise the decision must name one exact replacement owner and migrate the existing policy before consumers change.

### M-10 — Foundling history

- Source evidence: `04_Player_Entities/Shell_Foundlings.md`, `## 2. Исторический срез`, line 42.
- Target owner: `04_Player_Entities/Shell_Foundlings.md`; no migration.
- Entity role: Foundling origin and historical context inside the active owner for rescue, custody, and Origin.
- Mechanic owner: `04_Player_Entities/Shell_Foundlings.md` resolves rescue, custody, OriginTag assignment/reveal, Origin Continuation, and their consequences; the historical slice supplies authored Origin context to those rules.
- Universal system owner: none.
- Does not own: world-wide chronology, a replacement `02_World_Lore` authority, or universal metaphysics.
- Direct consumers and linked pages: `07_Gear_Inventory/Physical_Weight.md`, `04_Player_Entities/Trait_Development.md`, `04_Player_Entities/Lifecycle_Roster.md`, `06_Economy_Loot/Extraction_Stabilization_Loop.md`, `03_Factions_Societies/Quest_Engine.md`, `03_Factions_Societies/Quest_Engine_Grammar.md`, and `03_Factions_Societies/Lore/The_First_Reception.md`.
- Preserved meaning: origin place and catastrophe-relative epoch shape dialogue, relationships, OriginTag source, and Origin Continuation without changing human value or power budget.
- Required skill or handoff: lorekeeper verdict `COMPATIBLE`; entity-owned context supports this mechanic owner and does not require a separate lore owner.
- Approval and validation: no migration. Keep the historical slice in `Shell_Foundlings.md` and preserve its explicit boundaries.

### M-11 — status effect records

- Source evidence: `05_Combat_Survival/_Registries/Registry_StatusEffects.md`, effect-record headings from `### Кровотечение` through `### Насыщение восстановления`, scanner lines 92, 112, 139, 163, 187, 215, 234, 237, 239, 283, 285, 289, and 310.
- Target owner: `05_Combat_Survival/_Registries/Registry_StatusEffects.md`.
- Entity role: none.
- Mechanic owner: `05_Combat_Survival/Status_Effects.md` supplies effect mechanics; the registry supplies atomic instances.
- Universal system owner: none claimed by an individual record.
- Does not own: local environment-state ownership, automatic reactions, or a universal application resolver.
- Direct consumers and linked pages: `05_Combat_Survival/Status_Effects.md`, `05_Combat_Survival/Combat_Three_Debts.md`, and `08_World_Generation/_Registries/Registry_Environment_States.md`.
- Preserved meaning: repeat, telegraph, counter-action, and persistence fields are independently comparable content data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration; retain the global-versus-local boundary.

### M-13 — Three Debts trace

- Source evidence: `05_Combat_Survival/Combat_Three_Debts.md`, `## 2. Общий цикл действия`, line 55.
- Target owner: `05_Combat_Survival/Combat_Three_Debts.md`.
- Entity role: none.
- Mechanic owner: Combat Three Debts.
- Universal system owner: none; subordinate systems retain their own debt implementation.
- Does not own: weapon values, movement physics, status resolution, Dissonance calculation, or ability synergy.
- Direct consumers and linked pages: `05_Combat_Survival/Weapon_Core.md`, `05_Combat_Survival/Hunt_Frontier_Loop.md`, `05_Combat_Survival/Magic_Batteries.md`, `05_Combat_Survival/Movement_Physics.md`, `05_Combat_Survival/Acoustic_Stealth.md`, `05_Combat_Survival/Status_Effects.md`, `05_Combat_Survival/Dissonance_System.md`, and `04_Player_Entities/Ability_Synergy.md`.
- Preserved meaning: counterplay traces and the no-idle-punishment boundary remain the combat contract.
- Required skill or handoff: architecture evidence; no specialist evidence changes the ownership finding.
- Approval and validation: no migration.

### M-14 — Traversal geography

- Source evidence: `05_Combat_Survival/Traversal_Core.md`, `## 1. Тактическая География`, line 18.
- Target owner: `05_Combat_Survival/Traversal_Core.md`.
- Entity role: none.
- Mechanic owner: Traversal Core.
- Universal system owner: none.
- Does not own: movement physics implementation or generated world topology.
- Direct consumers and linked pages: `05_Combat_Survival/Movement_Physics.md` and `08_World_Generation/Generation/10_World_Topology.md`.
- Preserved meaning: the closed Pass A direct opening and all three-echelon tactical trade-offs.
- Required skill or handoff: curator confirms A-05-01 is closed; no Pass B edit follows.
- Approval and validation: no migration; Pass A commit remains the only authorized change.

### M-15 — weapon-frame guidance

- Source evidence: `05_Combat_Survival/Weapon_Manifesto.md`, `## 5. Фазы столкновения`, line 102.
- Target owner: `05_Combat_Survival/Weapon_Manifesto.md`.
- Entity role: a frame is a designed tool, not a player class.
- Mechanic owner: Weapon Core, Weapon Melee, and Weapon Ranged resolve runtime weapon rules.
- Universal system owner: Combat Three Debts supplies the shared cost grammar.
- Does not own: a frame record, weapon registry values, ballistic result, AI response resolver, or Anomaly behavior resolver.
- Direct consumers and linked pages: `05_Combat_Survival/Combat_Three_Debts.md`, `05_Combat_Survival/Weapon_Core.md`, `05_Combat_Survival/Weapon_Melee.md`, `05_Combat_Survival/Weapon_Ranged.md`, `04_Player_Entities/Combat_Profile_Pipeline.md`, and `08_World_Generation/Content/World_Atlas/Sectors/Port/00_Port_Manifest.md`.
- Preserved meaning: loud fire has information consequences for anomaly, AI, and players without making the manifesto a runtime owner.
- Required skill or handoff: architecture and curator evidence; no further handoff.
- Approval and validation: no migration.

### M-16 — Condenser frame records

- Source evidence: `05_Combat_Survival/Weapons/Condenser_Rig_2H.md`, `## Экземпляры`, scanner line 66.
- Target owner: `05_Combat_Survival/Weapons/Condenser_Rig_2H.md`.
- Entity role: authored weapon-frame instance.
- Mechanic owner: Weapon Ranged and Weapon Core.
- Universal system owner: Combat Three Debts for common commitment debt.
- Does not own: generic status rules, item registry ownership, or all ranged-gun behavior.
- Direct consumers and linked pages: `05_Combat_Survival/Weapon_Ranged.md`, `05_Combat_Survival/Magic_Batteries.md`, and `05_Combat_Survival/_Registries/Registry_Weapons.md`.
- Preserved meaning: parallel fields remain atomic frame data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration.

### M-17 — Needle frame records

- Source evidence: `05_Combat_Survival/Weapons/Needle_Thrower_2H.md`, `## Экземпляры`, scanner line 64.
- Target owner: `05_Combat_Survival/Weapons/Needle_Thrower_2H.md`.
- Entity role: authored weapon-frame instance.
- Mechanic owner: Weapon Ranged and Weapon Core.
- Universal system owner: Combat Three Debts.
- Does not own: generic status rules, item registry ownership, or all ranged-gun behavior.
- Direct consumers and linked pages: `05_Combat_Survival/Weapon_Ranged.md` and `05_Combat_Survival/_Registries/Registry_Weapons.md`.
- Preserved meaning: parallel fields remain atomic frame data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration.

### M-18 — Pulse frame records

- Source evidence: `05_Combat_Survival/Weapons/Pulse_Tool_1H.md`, `## Экземпляры`, scanner line 67.
- Target owner: `05_Combat_Survival/Weapons/Pulse_Tool_1H.md`.
- Entity role: authored weapon-frame instance.
- Mechanic owner: Weapon Ranged and Weapon Core.
- Universal system owner: Combat Three Debts.
- Does not own: generic status rules, item registry ownership, or all ranged-gun behavior.
- Direct consumers and linked pages: `05_Combat_Survival/Weapon_Ranged.md`, `05_Combat_Survival/Magic_Batteries.md`, and `05_Combat_Survival/_Registries/Registry_Weapons.md`.
- Preserved meaning: parallel fields remain atomic frame data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration.

### M-19 — Scatter frame records

- Source evidence: `05_Combat_Survival/Weapons/Scatter_Valve_2H.md`, `## Экземпляры`, scanner lines 66–67.
- Target owner: `05_Combat_Survival/Weapons/Scatter_Valve_2H.md`.
- Entity role: authored weapon-frame instance.
- Mechanic owner: Weapon Ranged and Weapon Core.
- Universal system owner: Combat Three Debts.
- Does not own: generic status rules, item registry ownership, or all ranged-gun behavior.
- Direct consumers and linked pages: `05_Combat_Survival/Weapon_Ranged.md`, `05_Combat_Survival/Magic_Batteries.md`, and `05_Combat_Survival/_Registries/Registry_Weapons.md`.
- Preserved meaning: parallel fields remain atomic frame data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration.

### M-20 — Rez nature and wallet

- Source evidence: `06_Economy_Loot/Currency_Rez.md`, `## 1. Природа Валюты`, line 24.
- Target owner: `06_Economy_Loot/Currency_Rez.md`.
- Entity role: Rez is a physical economic item, not an independent lore institution.
- Mechanic owner: Currency Rez.
- Universal system owner: Economy Core for economy-wide lifecycle only.
- Does not own: inventory slot capacity, Economy Core rules, battery behavior, or combat-damage resolution.
- Direct consumers and linked pages: `07_Gear_Inventory/Containers_Slots.md`, `06_Economy_Loot/Economy_Core.md`, and `05_Combat_Survival/Magic_Batteries.md`.
- Preserved meaning: physical currency, aggregated UI, spending order, and the non-Rez combat-cost boundary.
- Required skill or handoff: architecture evidence; no specialist handoff.
- Approval and validation: no migration.

### M-21 — Thermos module records

- Source evidence: `07_Gear_Inventory/_Registries/Registry_Thermos_Modules.md`, `## Candidate records`, scanner lines 76–444.
- Target owner: `MISSING_OWNER` for the listed effect domains; `07_Gear_Inventory/_Registries/Registry_Thermos_Modules.md` remains the definition-record owner.
- Entity role: module definition is a content instance supplied to assembly.
- Mechanic owner: Thermos Assembly resolves an installed instance; declared ParameterContracts resolve runtime effects when they exist.
- Universal system owner: `MISSING_OWNER` for the module outputs listed as absent in Parameter Contracts.
- Does not own: selected pattern, occupied nodes, damage, stitched state, active body interface, or local effect-policy invention.
- Direct consumers and linked pages: `07_Gear_Inventory/Thermos_System.md`, `07_Gear_Inventory/Thermos_Assembly.md`, `07_Gear_Inventory/_Registries/Registry_Thermoses.md`, `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces.md`, and `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`.
- Preserved meaning: all records stay `blocked_calibration`; `concept_effects` remain nonauthoritative discovery fields and atomicity remains a review requirement.
- Required skill or handoff: architecture lead identifies the owner gap; curator confirms structured repetition is not itself duplication.
- Approval and validation: **APPROVAL_REQUIRED** for each parameter domain. Do not make a module installable until its exact owner, contract, topology, coverage, and calibration are present.

### M-22 — Thermos model records

- Source evidence: `07_Gear_Inventory/_Registries/Registry_Thermoses.md`, `### Городской серийный Термос` and `### Шаблон Термоса`, scanner lines 52, 53, and 55.
- Target owner: `07_Gear_Inventory/_Registries/Registry_Thermoses.md`.
- Entity role: model definition supplied to an assembly instance.
- Mechanic owner: Thermos Assembly resolves fitting and committed assembly state.
- Universal system owner: Thermos System owns shared definition-versus-instance boundary.
- Does not own: fit revision, selected pattern, occupied nodes, damage, stitched state, active effects, or derived slot count.
- Direct consumers and linked pages: `07_Gear_Inventory/Thermos_System.md`, `07_Gear_Inventory/Thermos_Assembly.md`, `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces.md`, and `07_Gear_Inventory/Equipment_PaperDoll.md`.
- Preserved meaning: `blocked_topology` is an explicit content gap, not missing authority or an invitation to infer topology.
- Required skill or handoff: architecture and curator evidence; no handoff.
- Approval and validation: no migration; preserve the block until topology, fit envelope, mass, and Paper Doll mapping exist.

### M-23 — mutation-line records

- Source evidence: `08_World_Generation/_Registries/Registry_Anomaly_Mutations.md`, active tier records, scanner lines 56, 68, 100, 114, 116, 118, 149, and 162.
- Target owner: `08_World_Generation/_Registries/Registry_Anomaly_Mutations.md`.
- Entity role: anomaly-line and tier content instance.
- Mechanic owner: `08_World_Generation/Anomaly/Anomaly_System.md` resolves the overarching anomaly system.
- Universal system owner: none beyond the anomaly system’s shared lifecycle.
- Does not own: a global monster stat resolver, local scene state, or a second weather owner.
- Direct consumers and linked pages: `08_World_Generation/Anomaly/16_Anomaly_Mutation_Lines.md`, `08_World_Generation/_Registries/Registry_Mobs.md`, and `08_World_Generation/_Registries/Registry_Biomes.md`.
- Preserved meaning: repeated tier fields express intentionally parallel authored content.
- Required skill or handoff: curator evidence; no handoff.
- Approval and validation: no migration.

### M-24 — biome-tier records

- Source evidence: `08_World_Generation/_Registries/Registry_Biomes.md`, Port tier records, scanner lines 67, 81, 92, and 105.
- Target owner: `08_World_Generation/_Registries/Registry_Biomes.md`.
- Entity role: biome and threat-tier content instance.
- Mechanic owner: no separate mechanic resolver is claimed; `08_World_Generation/_Registries/Registry_Biomes.md` is the sole content owner for the biome-tier record.
- Universal system owner: none; numerical pressure is an empirical calibration issue.
- Does not own: loot table ownership, spawn resolver, a global mob rating, or a weather result resolver.
- Direct consumers and linked pages: `08_World_Generation/_Registries/Registry_Anomaly_Mutations.md`. The source names no canonical path for its generic map-generator reader, so no additional consumer is inferred.
- Preserved meaning: `env_pressure`, `gate_pulse`, and filter-rating values remain explicitly prototype-level.
- Required skill or handoff: architecture evidence distinguishes content gap from authority finding.
- Approval and validation: no migration.

### M-25 — environment-state records

- Source evidence: `08_World_Generation/_Registries/Registry_Environment_States.md`, `### Метка глубины`, scanner line 119.
- Target owner: `08_World_Generation/_Registries/Registry_Environment_States.md`.
- Entity role: a local scene-state instance with one local consequence.
- Mechanic owner: the record-local IDs `dungeon_commitment` and `dungeon_exit_rule` are not canonical paths; their resolver is `MISSING_OWNER` for this map entry.
- Universal system owner: none; a status aftermath is only a declared aftermath, never the scene’s owner.
- Does not own: a global status resolver, generic effect stack, or automatic reaction table.
- Direct consumers and linked pages: `05_Combat_Survival/_Registries/Registry_StatusEffects.md`, `08_World_Generation/Anomaly/Anomaly_System.md`, `08_World_Generation/_Registries/Registry_Anomaly_Mutations.md`, and `08_World_Generation/Content/World_Atlas/Sectors/Port/01_Foreign_Water_Mutation_Lines.md`.
- Preserved meaning: telegraph, choice, refusal, termination, and local consequence remain inseparable scene data.
- Required skill or handoff: architecture and curator evidence; no handoff.
- Approval and validation: **APPROVAL_REQUIRED** for the `mark_of_greed` resolver. A future bounded owner must map `dungeon_commitment` and `dungeon_exit_rule` to one canonical state machine while preserving one primary scene axis and consequence.

### M-26 — mob and variant records

- Source evidence: `08_World_Generation/_Registries/Registry_Mobs.md`, mutation-line and Hungry Form records, scanner lines 294–479.
- Target owner: `08_World_Generation/_Registries/Registry_Mobs.md`.
- Entity role: mob or mutation-variant content instance.
- Mechanic owner: each local `physiology_contract` and `action_contract` resolves its body and actions.
- Universal system owner: none; encounter numbers stay local to the MobID.
- Does not own: player-stat conversion, universal RPG debuffs, hidden rating variants, or a second status owner.
- Direct consumers and linked pages: `08_World_Generation/Anomaly/16_Anomaly_Mutation_Lines.md`, `08_World_Generation/Content/World_Atlas/Sectors/Port/01_Foreign_Water_Mutation_Lines.md`, and `08_World_Generation/_Registries/Registry_Anomaly_Mutations.md`.
- Preserved meaning: repeated tactical fields are the readable projection of local contracts.
- Required skill or handoff: curator evidence; no handoff.
- Approval and validation: no migration; preserve explicit compatible status interfaces and player-readable counterplay.

### M-27 — Hub weather presentation

- Source evidence: `08_World_Generation/Hub/04_Time_Atmosphere.md`, `## 2. Рейд: Аномальная Погода`, line 31.
- Target owner: `08_World_Generation/Hub/04_Time_Atmosphere.md`.
- Entity role: none.
- Mechanic owner: `08_World_Generation/Generation/03_Dynamic_Weather.md` owns the complete weather contract.
- Universal system owner: none.
- Does not own: physics, route, gear, enemy, trap, or exit resolution.
- Direct consumers and linked pages: `08_World_Generation/Generation/03_Dynamic_Weather.md`.
- Preserved meaning: weather is gameplay-relevant while this page only communicates the atmosphere and routing boundary.
- Required skill or handoff: architecture and curator evidence; no handoff.
- Approval and validation: no migration; retain the downstream contract link.

### M-28 — Реестр: городские Очаги и фракционные адреса

- **Source evidence:** `03_Factions_Societies/_Registries/Registry_Factions.md`, `# Реестр: городские Очаги и фракционные адреса`, and `## Игровая модель`; its frontmatter direct dependencies were inspected.
- **Target owner:** `03_Factions_Societies/_Registries/Registry_Factions.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** faction identity, address records, and their references do not resolve pledges, reputation changes, quest state, or barter outcomes.
- **Direct consumers and linked pages:** `03_Factions_Societies/Lore/Faction_Address_System`, `03_Factions_Societies/Lore/Civic_Ethos_Under_Lamps`, `03_Factions_Societies/Lore/The_Circle_of_Interposition`, `03_Factions_Societies/Pledge_Contracts`.
- **Preserved meaning:** `03_Factions_Societies/_Registries/Registry_Factions.md` preserves `# Реестр: городские Очаги и фракционные адреса` and `## Игровая модель`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect, vault-curator, and lorekeeper evidence; no additional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-29 — Гражданский порядок Элдрейна

- **Source evidence:** `03_Factions_Societies/Lore/Civic_Order.md`, `# Гражданский порядок Элдрейна`, and `## Основной закон`; its frontmatter direct dependencies were inspected.
- **Target owner:** `03_Factions_Societies/Lore/Civic_Order.md`.
- **Entity role:** entity and institutional lore.
- **Mechanic owner:** `MISSING_OWNER` for a player-facing civic-order transaction. `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` can record a future relation but cannot resolve it.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the city’s in-world recognition of collective decisions does not resolve player reputation, quest access, sanctions, or an interface transaction.
- **Direct consumers and linked pages:** `03_Factions_Societies/Lore/Hearth_Anatomy`, `03_Factions_Societies/Lore/Civic_Ethos_Under_Lamps`, `03_Factions_Societies/Lore/City_Genesis`, `03_Factions_Societies/Lore/The_Circle_of_Interposition`.
- **Preserved meaning:** `03_Factions_Societies/Lore/Civic_Order.md` preserves `# Гражданский порядок Элдрейна` and `## Основной закон`: identity, institutional memory, and in-world authority remain lore rather than a runtime contract.
- **Required skill or handoff:** system-architect, vault-curator, and lorekeeper evidence; no additional specialist handoff was required.
- **Approval and validation:** no migration; `APPROVAL_REQUIRED` until an exact civic-order mechanic owner exists.

### M-30 — Анатомия Очага

- **Source evidence:** `03_Factions_Societies/Lore/Hearth_Anatomy.md`, `# Анатомия Очага`, and `## Что такое Очаг`; its frontmatter direct dependencies were inspected.
- **Target owner:** `03_Factions_Societies/Lore/Hearth_Anatomy.md`.
- **Entity role:** entity and institutional lore.
- **Mechanic owner:** `MISSING_OWNER` for a generic Hearth interaction. `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` records a concrete relation only after its exact mechanic owner is named.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the identity, recognition, and internal forms of a Hearth do not resolve a player verb, eligibility, reward, runtime state, or failure.
- **Direct consumers and linked pages:** `03_Factions_Societies/Lore/Civic_Order`, `03_Factions_Societies/_Registries/Registry_Factions`, `03_Factions_Societies/_Registries/Registry_Faction_Interfaces`, `03_Factions_Societies/Lore/Faction_Address_System`.
- **Preserved meaning:** `03_Factions_Societies/Lore/Hearth_Anatomy.md` preserves `# Анатомия Очага` and `## Что такое Очаг`: identity, institutional memory, and in-world authority remain lore rather than a runtime contract.
- **Required skill or handoff:** system-architect, vault-curator, and lorekeeper evidence; no additional specialist handoff was required.
- **Approval and validation:** no migration; `APPROVAL_REQUIRED` until a concrete Hearth interaction names its resolver.

### M-31 — Поручения, адрес вклада и допуски

- **Source evidence:** `03_Factions_Societies/Pledge_Contracts.md`, `# Поручения, адрес вклада и допуски`, and `## 1. Поручение`; its frontmatter direct dependencies were inspected.
- **Target owner:** `03_Factions_Societies/Pledge_Contracts.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `03_Factions_Societies/Pledge_Contracts.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** a pledge contract does not turn a Hearth into a runtime owner of reputation, quest continuation, raid admission, or vendor resolution.
- **Direct consumers and linked pages:** `03_Factions_Societies/_Registries/Registry_Factions`, `03_Factions_Societies/Lore/Faction_Address_System`, `03_Factions_Societies/Lore/The_Circle_of_Interposition`, `03_Factions_Societies/Reputation_Rules`.
- **Preserved meaning:** `03_Factions_Societies/Pledge_Contracts.md` preserves `# Поручения, адрес вклада и допуски` and `## 1. Поручение`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect, vault-curator, and lorekeeper evidence; no additional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-32 — Реестр: семейства взаимодействий

- **Source evidence:** `04_Player_Entities/_Registries/Registry_Interaction_Families.md`, `# Реестр: семейства взаимодействий`, and `## 1. Закрытая грамматика`; its frontmatter direct dependencies were inspected.
- **Target owner:** `04_Player_Entities/_Registries/Registry_Interaction_Families.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Реестр: семейства взаимодействий owner does not absorb `04_Player_Entities/Skill_Build_Philosophy`, `04_Player_Entities/Combat_Profile_Pipeline`, `05_Combat_Survival/Magic_Batteries`, `07_Gear_Inventory/Inventory_Architecture`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `04_Player_Entities/Skill_Build_Philosophy`, `04_Player_Entities/Combat_Profile_Pipeline`, `05_Combat_Survival/Magic_Batteries`, `07_Gear_Inventory/Inventory_Architecture`.
- **Preserved meaning:** `04_Player_Entities/_Registries/Registry_Interaction_Families.md` preserves `# Реестр: семейства взаимодействий` and `## 1. Закрытая грамматика`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-33 — Реестр: Расы

- **Source evidence:** `04_Player_Entities/_Registries/Registry_Races.md`, `# Реестр: Расы`, and `## Статическая навигация`; its frontmatter direct dependencies were inspected.
- **Target owner:** `04_Player_Entities/_Registries/Registry_Races.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Реестр: Расы owner does not absorb `04_Player_Entities/MVP_3x3_Design_Contract`, `04_Player_Entities/_Registries/Registry_Combos`, `09_Project_Management/People_Design_Framework`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `04_Player_Entities/MVP_3x3_Design_Contract`, `04_Player_Entities/_Registries/Registry_Combos`, `09_Project_Management/People_Design_Framework`.
- **Preserved meaning:** `04_Player_Entities/_Registries/Registry_Races.md` preserves `# Реестр: Расы` and `## Статическая навигация`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-34 — Реестр: грамматика и границы навыков

- **Source evidence:** `04_Player_Entities/_Registries/Registry_Skill_Types.md`, `# Реестр: грамматика и границы навыков`, and `## 1. Общий контракт и условные продолжения`; its frontmatter direct dependencies were inspected.
- **Target owner:** `04_Player_Entities/_Registries/Registry_Skill_Types.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Реестр: грамматика и границы навыков owner does not absorb `04_Player_Entities/Skill_Build_Philosophy`, `04_Player_Entities/Ability_Synergy`, `05_Combat_Survival/_Registries/Registry_StatusEffects`, `07_Gear_Inventory/_Registries/Registry_Consumables`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `04_Player_Entities/Skill_Build_Philosophy`, `04_Player_Entities/Ability_Synergy`, `05_Combat_Survival/_Registries/Registry_StatusEffects`, `07_Gear_Inventory/_Registries/Registry_Consumables`.
- **Preserved meaning:** `04_Player_Entities/_Registries/Registry_Skill_Types.md` preserves `# Реестр: грамматика и границы навыков` and `## 1. Общий контракт и условные продолжения`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-35 — Реестр: Практики / специализации

- **Source evidence:** `04_Player_Entities/_Registries/Registry_Specs.md`, `# Реестр: Практики / специализации`, and `## Статическая навигация`; its frontmatter direct dependencies were inspected.
- **Target owner:** `04_Player_Entities/_Registries/Registry_Specs.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Реестр: Практики / специализации owner does not absorb `04_Player_Entities/MVP_3x3_Design_Contract`, `04_Player_Entities/_Registries/Registry_Combos`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `04_Player_Entities/MVP_3x3_Design_Contract`, `04_Player_Entities/_Registries/Registry_Combos`.
- **Preserved meaning:** `04_Player_Entities/_Registries/Registry_Specs.md` preserves `# Реестр: Практики / специализации` and `## Статическая навигация`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-36 — Реестр личных тегов

- **Source evidence:** `04_Player_Entities/_Registries/Registry_Tags.md`, `# Реестр личных тегов`, and `## Правила реестра`; its frontmatter direct dependencies were inspected.
- **Target owner:** `04_Player_Entities/_Registries/Registry_Tags.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Реестр личных тегов owner does not absorb `04_Player_Entities/Tags_System`, `04_Player_Entities/Trait_Development`, `04_Player_Entities/Proficiency_Arsenal`, `04_Player_Entities/Shell_Foundlings`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `04_Player_Entities/Tags_System`, `04_Player_Entities/Trait_Development`, `04_Player_Entities/Proficiency_Arsenal`, `04_Player_Entities/Shell_Foundlings`.
- **Preserved meaning:** `04_Player_Entities/_Registries/Registry_Tags.md` preserves `# Реестр личных тегов` and `## Правила реестра`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-37 — Контракт морфологии тела

- **Source evidence:** `04_Player_Entities/Body_Morphology_Contract.md`, `# Контракт морфологии тела`, and `## 1. Владелец`; its frontmatter direct dependencies were inspected.
- **Target owner:** `04_Player_Entities/Body_Morphology_Contract.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `04_Player_Entities/Body_Morphology_Contract.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** the Контракт морфологии тела owner does not absorb `04_Player_Entities/Shell_Construction`, `07_Gear_Inventory/Thermos_Assembly`, `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `04_Player_Entities/Shell_Construction`, `07_Gear_Inventory/Thermos_Assembly`, `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces`.
- **Preserved meaning:** `04_Player_Entities/Body_Morphology_Contract.md` preserves `# Контракт морфологии тела` and `## 1. Владелец`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-38 — Адаптивный арсенал и профильные ёмкости

- **Source evidence:** `04_Player_Entities/Proficiency_Arsenal.md`, `# Адаптивный арсенал и профильные ёмкости`, and `## 1. Именованный арсенал hero-kit`; its frontmatter direct dependencies were inspected.
- **Target owner:** `04_Player_Entities/Proficiency_Arsenal.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `04_Player_Entities/Proficiency_Arsenal.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Адаптивный арсенал и профильные ёмкости owner does not absorb `05_Combat_Survival/_Registries/Registry_Weapons`, `04_Player_Entities/_Registries/Registry_Combos`, `04_Player_Entities/MVP_3x3_Design_Contract`, `07_Gear_Inventory/Thermos_System`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/_Registries/Registry_Weapons`, `04_Player_Entities/_Registries/Registry_Combos`, `04_Player_Entities/MVP_3x3_Design_Contract`, `07_Gear_Inventory/Thermos_System`.
- **Preserved meaning:** `04_Player_Entities/Proficiency_Arsenal.md` preserves `# Адаптивный арсенал и профильные ёмкости` and `## 1. Именованный арсенал hero-kit`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-39 — Философия навыков и билдостроения

- **Source evidence:** `04_Player_Entities/Skill_Build_Philosophy.md`, `# Философия навыков и билдостроения`, and `## 1. Один контракт для P, Q и E`; its frontmatter direct dependencies were inspected.
- **Target owner:** `04_Player_Entities/Skill_Build_Philosophy.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `04_Player_Entities/Skill_Build_Philosophy.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** the Философия навыков и билдостроения owner does not absorb `04_Player_Entities/Ability_Synergy`, `04_Player_Entities/Combat_Profile_Pipeline`, `04_Player_Entities/_Registries/Registry_Interaction_Families`, `04_Player_Entities/MVP_3x3_Design_Contract`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `04_Player_Entities/Ability_Synergy`, `04_Player_Entities/Combat_Profile_Pipeline`, `04_Player_Entities/_Registries/Registry_Interaction_Families`, `04_Player_Entities/MVP_3x3_Design_Contract`.
- **Preserved meaning:** `04_Player_Entities/Skill_Build_Philosophy.md` preserves `# Философия навыков и билдостроения` and `## 1. Один контракт для P, Q и E`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-40 — Логика Спавна и Снаряжения Оболочек

- **Source evidence:** `04_Player_Entities/Spawn_Logic.md`, `# Логика Спавна и Снаряжения Оболочек`, and `## 1. Выжившая Пешка (Survivor State)`; its frontmatter direct dependencies were inspected.
- **Target owner:** `04_Player_Entities/Spawn_Logic.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `04_Player_Entities/Spawn_Logic.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Логика Спавна и Снаряжения Оболочек owner does not absorb `04_Player_Entities/Lifecycle_Roster`, `04_Player_Entities/Tags_System`, `04_Player_Entities/Trait_Development`, `06_Economy_Loot/Economy_Core`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `04_Player_Entities/Lifecycle_Roster`, `04_Player_Entities/Tags_System`, `04_Player_Entities/Trait_Development`, `06_Economy_Loot/Economy_Core`.
- **Preserved meaning:** `04_Player_Entities/Spawn_Logic.md` preserves `# Логика Спавна и Снаряжения Оболочек` and `## 1. Выжившая Пешка (Survivor State)`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-41 — Личные теги: свойства прожитой Пешки

- **Source evidence:** `04_Player_Entities/Tags_System.md`, `# Личные теги: свойства прожитой Пешки`, and `## 1. Что считается тегом`; its frontmatter direct dependencies were inspected.
- **Target owner:** `04_Player_Entities/Tags_System.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `04_Player_Entities/Tags_System.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Личные теги: свойства прожитой Пешки owner does not absorb `04_Player_Entities/Trait_Development`, `04_Player_Entities/_Registries/Registry_Tags`, `04_Player_Entities/Proficiency_Arsenal`, `04_Player_Entities/Combat_Profile_Pipeline`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `04_Player_Entities/Trait_Development`, `04_Player_Entities/_Registries/Registry_Tags`, `04_Player_Entities/Proficiency_Arsenal`, `04_Player_Entities/Combat_Profile_Pipeline`.
- **Preserved meaning:** `04_Player_Entities/Tags_System.md` preserves `# Личные теги: свойства прожитой Пешки` and `## 1. Что считается тегом`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-42 — Chronicle: память, а не дерево перков

- **Source evidence:** `04_Player_Entities/Trait_Development.md`, `# Chronicle: память, а не дерево перков`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `04_Player_Entities/Trait_Development.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `04_Player_Entities/Trait_Development.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Chronicle: память, а не дерево перков owner does not absorb `04_Player_Entities/Tags_System`, `04_Player_Entities/_Registries/Registry_Tags`, `04_Player_Entities/Lifecycle_Roster`, `04_Player_Entities/Shell_Foundlings`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `04_Player_Entities/Tags_System`, `04_Player_Entities/_Registries/Registry_Tags`, `04_Player_Entities/Lifecycle_Roster`, `04_Player_Entities/Shell_Foundlings`.
- **Preserved meaning:** `04_Player_Entities/Trait_Development.md` preserves `# Chronicle: память, а не дерево перков` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-43 — Реестр оружейных фреймов

- **Source evidence:** `05_Combat_Survival/_Registries/Registry_Weapons.md`, `# Реестр оружейных фреймов`, and `## Контракт доступа`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/_Registries/Registry_Weapons.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Реестр оружейных фреймов owner does not absorb `05_Combat_Survival/Weapon_Manifesto`, `04_Player_Entities/Combat_Profile_Pipeline`, `04_Player_Entities/Proficiency_Arsenal`, `04_Player_Entities/_Registries/Registry_Combos`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Weapon_Manifesto`, `04_Player_Entities/Combat_Profile_Pipeline`, `04_Player_Entities/Proficiency_Arsenal`, `04_Player_Entities/_Registries/Registry_Combos`.
- **Preserved meaning:** `05_Combat_Survival/_Registries/Registry_Weapons.md` preserves `# Реестр оружейных фреймов` and `## Контракт доступа`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-44 — Механика: Акустический Шум

- **Source evidence:** `05_Combat_Survival/Acoustic_Stealth.md`, `# Механика: Акустический Шум`, and `## 1. Назначение`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Acoustic_Stealth.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Acoustic_Stealth.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Механика: Акустический Шум owner does not absorb `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/Hunt_Frontier_Loop`, `05_Combat_Survival/Dissonance_System`, `05_Combat_Survival/Movement_Physics`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/Hunt_Frontier_Loop`, `05_Combat_Survival/Dissonance_System`, `05_Combat_Survival/Movement_Physics`.
- **Preserved meaning:** `05_Combat_Survival/Acoustic_Stealth.md` preserves `# Механика: Акустический Шум` and `## 1. Назначение`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-45 — Система: Баллистика и Броня

- **Source evidence:** `05_Combat_Survival/Ballistics_Armor.md`, `# Система: Баллистика и Броня`, and `## 1. PvE: Покров и Способ Вскрытия`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Ballistics_Armor.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Ballistics_Armor.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Система: Баллистика и Броня owner does not absorb `05_Combat_Survival/Movement_Physics`, `05_Combat_Survival/Hunt_Frontier_Loop`, `07_Gear_Inventory/Thermos_System`, `07_Gear_Inventory/Thermos_Assembly`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Movement_Physics`, `05_Combat_Survival/Hunt_Frontier_Loop`, `07_Gear_Inventory/Thermos_System`, `07_Gear_Inventory/Thermos_Assembly`.
- **Preserved meaning:** `05_Combat_Survival/Ballistics_Armor.md` preserves `# Система: Баллистика и Броня` and `## 1. PvE: Покров и Способ Вскрытия`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-46 — Баллистика PvE: Покров и Рабочий Цикл

- **Source evidence:** `05_Combat_Survival/Ballistics_PvE.md`, `# Баллистика PvE: Покров и Рабочий Цикл`, and `## 1. Покров Не Является Gear Check`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Ballistics_PvE.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Ballistics_PvE.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Баллистика PvE: Покров и Рабочий Цикл owner does not absorb `08_World_Generation/_Registries/Registry_Mobs`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `08_World_Generation/_Registries/Registry_Mobs`.
- **Preserved meaning:** `05_Combat_Survival/Ballistics_PvE.md` preserves `# Баллистика PvE: Покров и Рабочий Цикл` and `## 1. Покров Не Является Gear Check`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-47 — Медицина, здоровье и необходимые расходники

- **Source evidence:** `05_Combat_Survival/Combat_Consumables.md`, `# Медицина, здоровье и необходимые расходники`, and `## 1. Граница расходников и навыков`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Combat_Consumables.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Combat_Consumables.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Медицина, здоровье и необходимые расходники owner does not absorb `07_Gear_Inventory/_Registries/Registry_Consumables`, `05_Combat_Survival/_Registries/Registry_StatusEffects`, `04_Player_Entities/Skill_Build_Philosophy`, `05_Combat_Survival/Magic_Batteries`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `07_Gear_Inventory/_Registries/Registry_Consumables`, `05_Combat_Survival/_Registries/Registry_StatusEffects`, `04_Player_Entities/Skill_Build_Philosophy`, `05_Combat_Survival/Magic_Batteries`.
- **Preserved meaning:** `05_Combat_Survival/Combat_Consumables.md` preserves `# Медицина, здоровье и необходимые расходники` and `## 1. Граница расходников и навыков`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-48 — Акустический Протокол и VOIP

- **Source evidence:** `05_Combat_Survival/Communication_Vox.md`, `# Акустический Протокол и VOIP`, and `## 1.  Канал Связи`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Communication_Vox.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Communication_Vox.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Акустический Протокол и VOIP owner does not absorb `05_Combat_Survival/Acoustic_Stealth`, `05_Combat_Survival/Masks_Filters`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Acoustic_Stealth`, `05_Combat_Survival/Masks_Filters`.
- **Preserved meaning:** `05_Combat_Survival/Communication_Vox.md` preserves `# Акустический Протокол и VOIP` and `## 1.  Канал Связи`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-49 — Механика: Диссонанс (Dissonance)

- **Source evidence:** `05_Combat_Survival/Dissonance_System.md`, `# Механика: Диссонанс (Dissonance)`, and `## 1. Концепция`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Dissonance_System.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Dissonance_System.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Механика: Диссонанс (Dissonance) owner does not absorb `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/Hunt_Frontier_Loop`, `05_Combat_Survival/Acoustic_Stealth`, `07_Gear_Inventory/Dissonance_Value`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/Hunt_Frontier_Loop`, `05_Combat_Survival/Acoustic_Stealth`, `07_Gear_Inventory/Dissonance_Value`.
- **Preserved meaning:** `05_Combat_Survival/Dissonance_System.md` preserves `# Механика: Диссонанс (Dissonance)` and `## 1. Концепция`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-50 — Полевые Операции с Лутом

- **Source evidence:** `05_Combat_Survival/Field_Crafting.md`, `# Полевые Операции с Лутом`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Field_Crafting.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Field_Crafting.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Полевые Операции с Лутом owner does not absorb `08_World_Generation/Generation/02_Mechanic_Night_Benches`, `06_Economy_Loot/Loot_Sync_Cycle`, `06_Economy_Loot/Barter_System`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/02_Mechanic_Night_Benches`, `06_Economy_Loot/Loot_Sync_Cycle`, `06_Economy_Loot/Barter_System`.
- **Preserved meaning:** `05_Combat_Survival/Field_Crafting.md` preserves `# Полевые Операции с Лутом` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-51 — Охота на фронтире Аномалии

- **Source evidence:** `05_Combat_Survival/Hunt_Frontier_Loop.md`, `# Охота на фронтире Аномалии`, and `## 1. Обещание фронтира`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Hunt_Frontier_Loop.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Hunt_Frontier_Loop.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Охота на фронтире Аномалии owner does not absorb `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/Acoustic_Stealth`, `05_Combat_Survival/Dissonance_System`, `05_Combat_Survival/Movement_Physics`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/Acoustic_Stealth`, `05_Combat_Survival/Dissonance_System`, `05_Combat_Survival/Movement_Physics`.
- **Preserved meaning:** `05_Combat_Survival/Hunt_Frontier_Loop.md` preserves `# Охота на фронтире Аномалии` and `## 1. Обещание фронтира`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-52 — Система: Магия и Батареи

- **Source evidence:** `05_Combat_Survival/Magic_Batteries.md`, `# Система: Магия и Батареи`, and `## 1. Канон батарей`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Magic_Batteries.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Magic_Batteries.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Система: Магия и Батареи owner does not absorb `05_Combat_Survival/Combat_Three_Debts`, `02_World_Lore/The_Ark`, `02_World_Lore/Energy_Concept`, `04_Player_Entities/Skill_Build_Philosophy`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Combat_Three_Debts`, `02_World_Lore/The_Ark`, `02_World_Lore/Energy_Concept`, `04_Player_Entities/Skill_Build_Philosophy`.
- **Preserved meaning:** `05_Combat_Survival/Magic_Batteries.md` preserves `# Система: Магия и Батареи` and `## 1. Канон батарей`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-53 — Маски: Ключ от Мира

- **Source evidence:** `05_Combat_Survival/Masks_Filters.md`, `# Маски: Ключ от Мира`, and `## 1. Концепция (Mask Gating)`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Masks_Filters.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Masks_Filters.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Маски: Ключ от Мира owner does not absorb `07_Gear_Inventory/_Registries/Registry_Headwear`, `02_World_Lore/Anomaly_Weather_Systems`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `07_Gear_Inventory/_Registries/Registry_Headwear`, `02_World_Lore/Anomaly_Weather_Systems`.
- **Preserved meaning:** `05_Combat_Survival/Masks_Filters.md` preserves `# Маски: Ключ от Мира` and `## 1. Концепция (Mask Gating)`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-54 — Механика: Физика Движения

- **Source evidence:** `05_Combat_Survival/Movement_Physics.md`, `# Механика: Физика Движения`, and `## 0. Цель Ощущения`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Movement_Physics.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Movement_Physics.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Механика: Физика Движения owner does not absorb `05_Combat_Survival/Combat_Three_Debts`, `07_Gear_Inventory/Physical_Weight`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Combat_Three_Debts`, `07_Gear_Inventory/Physical_Weight`.
- **Preserved meaning:** `05_Combat_Survival/Movement_Physics.md` preserves `# Механика: Физика Движения` and `## 0. Цель Ощущения`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-55 — Механика: Пороги Давления Аномалии (Dissonance Thresholds)

- **Source evidence:** `05_Combat_Survival/Threat_Thresholds.md`, `# Механика: Пороги Давления Аномалии (Dissonance Thresholds)`, and `## 1. Расчет Давления`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Threat_Thresholds.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Threat_Thresholds.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Механика: Пороги Давления Аномалии (Dissonance Thresholds) owner does not absorb `05_Combat_Survival/Dissonance_System`, `08_World_Generation/Generation/19_Raid_Approach_and_Entry`, `08_World_Generation/Generation/08_Gate_Check`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Dissonance_System`, `08_World_Generation/Generation/19_Raid_Approach_and_Entry`, `08_World_Generation/Generation/08_Gate_Check`.
- **Preserved meaning:** `05_Combat_Survival/Threat_Thresholds.md` preserves `# Механика: Пороги Давления Аномалии (Dissonance Thresholds)` and `## 1. Расчет Давления`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-56 — Оружие: Магострельный Канон и Тиры

- **Source evidence:** `05_Combat_Survival/Weapon_Core.md`, `# Оружие: Магострельный Канон и Тиры`, and `## 1. Главный принцип`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Weapon_Core.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Weapon_Core.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Оружие: Магострельный Канон и Тиры owner does not absorb `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/Weapon_Ranged`, `05_Combat_Survival/Magic_Batteries`, `05_Combat_Survival/_Registries/Registry_Weapons`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/Weapon_Ranged`, `05_Combat_Survival/Magic_Batteries`, `05_Combat_Survival/_Registries/Registry_Weapons`.
- **Preserved meaning:** `05_Combat_Survival/Weapon_Core.md` preserves `# Оружие: Магострельный Канон и Тиры` and `## 1. Главный принцип`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-57 — Оружие: ближний бой

- **Source evidence:** `05_Combat_Survival/Weapon_Melee.md`, `# Оружие: ближний бой`, and `## Цикл`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Weapon_Melee.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Weapon_Melee.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Оружие: ближний бой owner does not absorb `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/_Registries/Registry_Weapons`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/_Registries/Registry_Weapons`.
- **Preserved meaning:** `05_Combat_Survival/Weapon_Melee.md` preserves `# Оружие: ближний бой` and `## Цикл`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-58 — Оружие: дальний бой

- **Source evidence:** `05_Combat_Survival/Weapon_Ranged.md`, `# Оружие: дальний бой`, and `## Батарея не магазин`; its frontmatter direct dependencies were inspected.
- **Target owner:** `05_Combat_Survival/Weapon_Ranged.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `05_Combat_Survival/Weapon_Ranged.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Оружие: дальний бой owner does not absorb `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/Magic_Batteries`, `05_Combat_Survival/_Registries/Registry_Weapons`, `04_Player_Entities/_Registries/Registry_Parameter_Contracts`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/Magic_Batteries`, `05_Combat_Survival/_Registries/Registry_Weapons`, `04_Player_Entities/_Registries/Registry_Parameter_Contracts`.
- **Preserved meaning:** `05_Combat_Survival/Weapon_Ranged.md` preserves `# Оружие: дальний бой` and `## Батарея не магазин`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-59 — Адресный Бартер

- **Source evidence:** `06_Economy_Loot/Barter_System.md`, `# Адресный Бартер`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `06_Economy_Loot/Barter_System.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `06_Economy_Loot/Barter_System.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Адресный Бартер owner does not absorb `06_Economy_Loot/Economy_Core`, `06_Economy_Loot/Resource_Cycle`, `06_Economy_Loot/Craft_Modifiers`, `06_Economy_Loot/Blueprints`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Economy_Core`, `06_Economy_Loot/Resource_Cycle`, `06_Economy_Loot/Craft_Modifiers`, `06_Economy_Loot/Blueprints`.
- **Preserved meaning:** `06_Economy_Loot/Barter_System.md` preserves `# Адресный Бартер` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-60 — Ограниченные Чертежи

- **Source evidence:** `06_Economy_Loot/Blueprints.md`, `# Ограниченные Чертежи`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `06_Economy_Loot/Blueprints.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `06_Economy_Loot/Blueprints.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Ограниченные Чертежи owner does not absorb `06_Economy_Loot/Barter_System`, `07_Gear_Inventory/_Registries/Registry_Blueprints`, `07_Gear_Inventory/_Registries/Registry_CraftingRecipes`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Barter_System`, `07_Gear_Inventory/_Registries/Registry_Blueprints`, `07_Gear_Inventory/_Registries/Registry_CraftingRecipes`.
- **Preserved meaning:** `06_Economy_Loot/Blueprints.md` preserves `# Ограниченные Чертежи` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-61 — Вариантный Ингредиент

- **Source evidence:** `06_Economy_Loot/Craft_Modifiers.md`, `# Вариантный Ингредиент`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `06_Economy_Loot/Craft_Modifiers.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `06_Economy_Loot/Craft_Modifiers.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Вариантный Ингредиент owner does not absorb `06_Economy_Loot/Barter_System`, `06_Economy_Loot/Blueprints`, `07_Gear_Inventory/Affix_Grammar`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Barter_System`, `06_Economy_Loot/Blueprints`, `07_Gear_Inventory/Affix_Grammar`.
- **Preserved meaning:** `06_Economy_Loot/Craft_Modifiers.md` preserves `# Вариантный Ингредиент` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-62 — Экономика: От Риска к Адресу

- **Source evidence:** `06_Economy_Loot/Economy_Core.md`, `# Экономика: От Риска к Адресу`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `06_Economy_Loot/Economy_Core.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `06_Economy_Loot/Economy_Core.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Экономика: От Риска к Адресу owner does not absorb `06_Economy_Loot/Extraction_Stabilization_Loop`, `06_Economy_Loot/Barter_System`, `06_Economy_Loot/Resource_Cycle`, `06_Economy_Loot/Vendor_Logic`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Extraction_Stabilization_Loop`, `06_Economy_Loot/Barter_System`, `06_Economy_Loot/Resource_Cycle`, `06_Economy_Loot/Vendor_Logic`.
- **Preserved meaning:** `06_Economy_Loot/Economy_Core.md` preserves `# Экономика: От Риска к Адресу` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-63 — Экстракция, стабилизация и наследие сектора

- **Source evidence:** `06_Economy_Loot/Extraction_Stabilization_Loop.md`, `# Экстракция, стабилизация и наследие сектора`, and `## 1. Главная ставка`; its frontmatter direct dependencies were inspected.
- **Target owner:** `06_Economy_Loot/Extraction_Stabilization_Loop.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `06_Economy_Loot/Extraction_Stabilization_Loop.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Экстракция, стабилизация и наследие сектора owner does not absorb `01_Core_Vision/02_Core_Loop`, `02_World_Lore/The_Entropy`, `04_Player_Entities/Lifecycle_Roster`, `04_Player_Entities/Shell_Foundlings`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `01_Core_Vision/02_Core_Loop`, `02_World_Lore/The_Entropy`, `04_Player_Entities/Lifecycle_Roster`, `04_Player_Entities/Shell_Foundlings`.
- **Preserved meaning:** `06_Economy_Loot/Extraction_Stabilization_Loop.md` preserves `# Экстракция, стабилизация и наследие сектора` and `## 1. Главная ставка`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-64 — Распределение Лута

- **Source evidence:** `06_Economy_Loot/Loot_Distribution.md`, `# Распределение Лута`, and `## 1. Пять осей размещения`; its frontmatter direct dependencies were inspected.
- **Target owner:** `06_Economy_Loot/Loot_Distribution.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `06_Economy_Loot/Loot_Distribution.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Распределение Лута owner does not absorb `06_Economy_Loot/Extraction_Stabilization_Loop`, `07_Gear_Inventory/Containers_Slots`, `08_World_Generation/_Registries/Registry_Biomes`, `08_World_Generation/_Registries/Registry_Anomaly_Mutations`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Extraction_Stabilization_Loop`, `07_Gear_Inventory/Containers_Slots`, `08_World_Generation/_Registries/Registry_Biomes`, `08_World_Generation/_Registries/Registry_Anomaly_Mutations`.
- **Preserved meaning:** `06_Economy_Loot/Loot_Distribution.md` preserves `# Распределение Лута` and `## 1. Пять осей размещения`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-65 — Происхождение Лута и Цикл Синхронизации

- **Source evidence:** `06_Economy_Loot/Loot_Sync_Cycle.md`, `# Происхождение Лута и Цикл Синхронизации`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `06_Economy_Loot/Loot_Sync_Cycle.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `06_Economy_Loot/Loot_Sync_Cycle.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Происхождение Лута и Цикл Синхронизации owner does not absorb `06_Economy_Loot/Extraction_Stabilization_Loop`, `06_Economy_Loot/Barter_System`, `06_Economy_Loot/P2P_Interaction`, `08_World_Generation/Generation/02_Mechanic_Night_Benches`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Extraction_Stabilization_Loop`, `06_Economy_Loot/Barter_System`, `06_Economy_Loot/P2P_Interaction`, `08_World_Generation/Generation/02_Mechanic_Night_Benches`.
- **Preserved meaning:** `06_Economy_Loot/Loot_Sync_Cycle.md` preserves `# Происхождение Лута и Цикл Синхронизации` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-66 — Физическая Передача Между Игроками

- **Source evidence:** `06_Economy_Loot/P2P_Interaction.md`, `# Физическая Передача Между Игроками`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `06_Economy_Loot/P2P_Interaction.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `06_Economy_Loot/P2P_Interaction.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Физическая Передача Между Игроками owner does not absorb `06_Economy_Loot/Extraction_Stabilization_Loop`, `06_Economy_Loot/Loot_Sync_Cycle`, `06_Economy_Loot/Economy_Core`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Extraction_Stabilization_Loop`, `06_Economy_Loot/Loot_Sync_Cycle`, `06_Economy_Loot/Economy_Core`.
- **Preserved meaning:** `06_Economy_Loot/P2P_Interaction.md` preserves `# Физическая Передача Между Игроками` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-67 — Цикл Ресурсов: Состав и Адрес

- **Source evidence:** `06_Economy_Loot/Resource_Cycle.md`, `# Цикл Ресурсов: Состав и Адрес`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `06_Economy_Loot/Resource_Cycle.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `06_Economy_Loot/Resource_Cycle.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Цикл Ресурсов: Состав и Адрес owner does not absorb `06_Economy_Loot/Barter_System`, `06_Economy_Loot/Extraction_Stabilization_Loop`, `06_Economy_Loot/Vendor_Logic`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Barter_System`, `06_Economy_Loot/Extraction_Stabilization_Loop`, `06_Economy_Loot/Vendor_Logic`.
- **Preserved meaning:** `06_Economy_Loot/Resource_Cycle.md` preserves `# Цикл Ресурсов: Состав и Адрес` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-68 — Return Manifest Contract

- **Source evidence:** `06_Economy_Loot/Return_Manifest_Contract.md`, `# Return Manifest Contract`, and `## Responsibility`; its frontmatter direct dependencies were inspected.
- **Target owner:** `06_Economy_Loot/Return_Manifest_Contract.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `06_Economy_Loot/Return_Manifest_Contract.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** the Return Manifest Contract owner does not absorb `04_Player_Entities/Lifecycle_Resolver`, `04_Player_Entities/Last_Thread_Recovery`, `04_Player_Entities/Recovery_Lifecycle`, `06_Economy_Loot/Extraction_Stabilization_Loop`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `04_Player_Entities/Lifecycle_Resolver`, `04_Player_Entities/Last_Thread_Recovery`, `04_Player_Entities/Recovery_Lifecycle`, `06_Economy_Loot/Extraction_Stabilization_Loop`.
- **Preserved meaning:** `06_Economy_Loot/Return_Manifest_Contract.md` preserves `# Return Manifest Contract` and `## Responsibility`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-69 — Расходы и Вывод Валюты (Money Sinks)

- **Source evidence:** `06_Economy_Loot/Sinks_Insurance.md`, `# Расходы и Вывод Валюты (Money Sinks)`, and `## 1. Стабилизация Добычи (Loot Stabilization)`; its frontmatter direct dependencies were inspected.
- **Target owner:** `06_Economy_Loot/Sinks_Insurance.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `06_Economy_Loot/Sinks_Insurance.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Расходы и Вывод Валюты (Money Sinks) owner does not absorb `06_Economy_Loot/Extraction_Stabilization_Loop`, `07_Gear_Inventory/Inventory_QoL`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Extraction_Stabilization_Loop`, `07_Gear_Inventory/Inventory_QoL`.
- **Preserved meaning:** `06_Economy_Loot/Sinks_Insurance.md` preserves `# Расходы и Вывод Валюты (Money Sinks)` and `## 1. Стабилизация Добычи (Loot Stabilization)`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-70 — Адреса, Поставщики и Мастера

- **Source evidence:** `06_Economy_Loot/Vendor_Logic.md`, `# Адреса, Поставщики и Мастера`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `06_Economy_Loot/Vendor_Logic.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `06_Economy_Loot/Vendor_Logic.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Адреса, Поставщики и Мастера owner does not absorb `06_Economy_Loot/Barter_System`, `08_World_Generation/Hub/01_Hub_Map_Table`, `08_World_Generation/Generation/17_Dual_State_POIs`, `03_Factions_Societies/_Registries/Registry_Factions`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Barter_System`, `08_World_Generation/Hub/01_Hub_Map_Table`, `08_World_Generation/Generation/17_Dual_State_POIs`, `03_Factions_Societies/_Registries/Registry_Factions`.
- **Preserved meaning:** `06_Economy_Loot/Vendor_Logic.md` preserves `# Адреса, Поставщики и Мастера` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-71 — Реестр: LimitedBlueprint

- **Source evidence:** `07_Gear_Inventory/_Registries/Registry_Blueprints.md`, `# Реестр: LimitedBlueprint`, and `## 1. Ответственность и обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/_Registries/Registry_Blueprints.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Реестр: LimitedBlueprint owner does not absorb `06_Economy_Loot/Blueprints`, `07_Gear_Inventory/_Registries/Registry_CraftingRecipes`, `08_World_Generation/_Registries/Registry_POIs`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Blueprints`, `07_Gear_Inventory/_Registries/Registry_CraftingRecipes`, `08_World_Generation/_Registries/Registry_POIs`.
- **Preserved meaning:** `07_Gear_Inventory/_Registries/Registry_Blueprints.md` preserves `# Реестр: LimitedBlueprint` and `## 1. Ответственность и обещание`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-72 — Реестр: необходимые расходники и экспедиционные предметы

- **Source evidence:** `07_Gear_Inventory/_Registries/Registry_Consumables.md`, `# Реестр: необходимые расходники и экспедиционные предметы`, and `## 1. Контракт записи`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/_Registries/Registry_Consumables.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Реестр: необходимые расходники и экспедиционные предметы owner does not absorb `05_Combat_Survival/Combat_Consumables`, `05_Combat_Survival/Magic_Batteries`, `05_Combat_Survival/_Registries/Registry_StatusEffects`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Combat_Consumables`, `05_Combat_Survival/Magic_Batteries`, `05_Combat_Survival/_Registries/Registry_StatusEffects`.
- **Preserved meaning:** `07_Gear_Inventory/_Registries/Registry_Consumables.md` preserves `# Реестр: необходимые расходники и экспедиционные предметы` and `## 1. Контракт записи`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-73 — Реестр: Адресные RecipeTransaction

- **Source evidence:** `07_Gear_Inventory/_Registries/Registry_CraftingRecipes.md`, `# Реестр: Адресные RecipeTransaction`, and `## 1. Ответственность и обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/_Registries/Registry_CraftingRecipes.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Реестр: Адресные RecipeTransaction owner does not absorb `06_Economy_Loot/Barter_System`, `06_Economy_Loot/Blueprints`, `06_Economy_Loot/Craft_Modifiers`, `07_Gear_Inventory/_Registries/Registry_Blueprints`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Barter_System`, `06_Economy_Loot/Blueprints`, `06_Economy_Loot/Craft_Modifiers`, `07_Gear_Inventory/_Registries/Registry_Blueprints`.
- **Preserved meaning:** `07_Gear_Inventory/_Registries/Registry_CraftingRecipes.md` preserves `# Реестр: Адресные RecipeTransaction` and `## 1. Ответственность и обещание`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-74 — Реестр: Маски и Шлемы (Protective Gear)

- **Source evidence:** `07_Gear_Inventory/_Registries/Registry_Headwear.md`, `# Реестр: Маски и Шлемы (Protective Gear)`, and `## (T1) Повязка Первопроходца (Pioneer Scarf)`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/_Registries/Registry_Headwear.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Реестр: Маски и Шлемы (Protective Gear) owner does not imply a second resolver beyond its recorded (T1) Повязка Первопроходца (Pioneer Scarf) contract; its own rule terms remain the only authority here.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `07_Gear_Inventory/_Registries/Registry_Headwear.md` preserves `# Реестр: Маски и Шлемы (Protective Gear)` and `## (T1) Повязка Первопроходца (Pioneer Scarf)`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-75 — Реестр: Предметы и Ресурсы (General Items)

- **Source evidence:** `07_Gear_Inventory/_Registries/Registry_Items.md`, `# Реестр: Предметы и Ресурсы (General Items)`, and `## 1. Ресурсы Крафта (Crafting Materials)`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/_Registries/Registry_Items.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Реестр: Предметы и Ресурсы (General Items) owner does not imply a second resolver beyond its recorded 1. Ресурсы Крафта (Crafting Materials) contract; its own rule terms remain the only authority here.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `07_Gear_Inventory/_Registries/Registry_Items.md` preserves `# Реестр: Предметы и Ресурсы (General Items)` and `## 1. Ресурсы Крафта (Crafting Materials)`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-76 — Реестр интерфейсов Термоса

- **Source evidence:** `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces.md`, `# Реестр интерфейсов Термоса`, and `## Invariants`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces.md`.
- **Entity role:** directional interface records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Реестр интерфейсов Термоса owner does not absorb `07_Gear_Inventory/Thermos_System`, `07_Gear_Inventory/Thermos_Assembly`, `04_Player_Entities/Body_Morphology_Contract`, `07_Gear_Inventory/Inventory_Architecture`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `07_Gear_Inventory/Thermos_System`, `07_Gear_Inventory/Thermos_Assembly`, `04_Player_Entities/Body_Morphology_Contract`, `07_Gear_Inventory/Inventory_Architecture`.
- **Preserved meaning:** `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces.md` preserves `# Реестр интерфейсов Термоса` and `## Invariants`: its directional relation fields remain non-normative handoffs.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-77 — Грамматика Аффиксов

- **Source evidence:** `07_Gear_Inventory/Affix_Grammar.md`, `# Грамматика Аффиксов`, and `## 1. Принцип`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Affix_Grammar.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `07_Gear_Inventory/Affix_Grammar.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Грамматика Аффиксов owner does not absorb `07_Gear_Inventory/Gear_Progression`, `06_Economy_Loot/Craft_Modifiers`, `07_Gear_Inventory/_Registries/Registry_CraftingRecipes`, `05_Combat_Survival/_Registries/Registry_Weapons`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `07_Gear_Inventory/Gear_Progression`, `06_Economy_Loot/Craft_Modifiers`, `07_Gear_Inventory/_Registries/Registry_CraftingRecipes`, `05_Combat_Survival/_Registries/Registry_Weapons`.
- **Preserved meaning:** `07_Gear_Inventory/Affix_Grammar.md` preserves `# Грамматика Аффиксов` and `## 1. Принцип`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-78 — Механика: Контейнеры и Слоты (Containers Hierarchy)

- **Source evidence:** `07_Gear_Inventory/Containers_Slots.md`, `# Механика: Контейнеры и Слоты (Containers Hierarchy)`, and `## 1. Иерархия Хранилищ`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Containers_Slots.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `07_Gear_Inventory/Containers_Slots.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Механика: Контейнеры и Слоты (Containers Hierarchy) owner does not imply a second resolver beyond its recorded 1. Иерархия Хранилищ contract; its own rule terms remain the only authority here.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `07_Gear_Inventory/Containers_Slots.md` preserves `# Механика: Контейнеры и Слоты (Containers Hierarchy)` and `## 1. Иерархия Хранилищ`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-79 — Механика: Диссонанс Предмета (Dissonance Value)

- **Source evidence:** `07_Gear_Inventory/Dissonance_Value.md`, `# Механика: Диссонанс Предмета (Dissonance Value)`, and `## 1. Концепция`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Dissonance_Value.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `07_Gear_Inventory/Dissonance_Value.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Механика: Диссонанс Предмета (Dissonance Value) owner does not absorb `06_Economy_Loot/Currency_Rez`, `05_Combat_Survival/Dissonance_System`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Currency_Rez`, `05_Combat_Survival/Dissonance_System`.
- **Preserved meaning:** `07_Gear_Inventory/Dissonance_Value.md` preserves `# Механика: Диссонанс Предмета (Dissonance Value)` and `## 1. Концепция`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-80 — Кукла Персонажа (Equipment Slots)

- **Source evidence:** `07_Gear_Inventory/Equipment_PaperDoll.md`, `# Кукла Персонажа (Equipment Slots)`, and `## 1. Философия: Tactical Goblincore`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Equipment_PaperDoll.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `07_Gear_Inventory/Equipment_PaperDoll.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Кукла Персонажа (Equipment Slots) owner does not absorb `07_Gear_Inventory/Inventory_Architecture`, `07_Gear_Inventory/Fashion_Gear`, `07_Gear_Inventory/Thermos_System`, `05_Combat_Survival/_Registries/Registry_Weapons`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `07_Gear_Inventory/Inventory_Architecture`, `07_Gear_Inventory/Fashion_Gear`, `07_Gear_Inventory/Thermos_System`, `05_Combat_Survival/_Registries/Registry_Weapons`.
- **Preserved meaning:** `07_Gear_Inventory/Equipment_PaperDoll.md` preserves `# Кукла Персонажа (Equipment Slots)` and `## 1. Философия: Tactical Goblincore`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-81 — Визуальный язык Термоса

- **Source evidence:** `07_Gear_Inventory/Fashion_Gear.md`, `# Визуальный язык Термоса`, and `## 1. Четыре читаемых слоя`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Fashion_Gear.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `07_Gear_Inventory/Fashion_Gear.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Визуальный язык Термоса owner does not absorb `07_Gear_Inventory/Equipment_PaperDoll`, `07_Gear_Inventory/Thermos_System`, `07_Gear_Inventory/_Registries/Registry_Thermoses`, `07_Gear_Inventory/_Registries/Registry_Thermos_Modules`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `07_Gear_Inventory/Equipment_PaperDoll`, `07_Gear_Inventory/Thermos_System`, `07_Gear_Inventory/_Registries/Registry_Thermoses`, `07_Gear_Inventory/_Registries/Registry_Thermos_Modules`.
- **Preserved meaning:** `07_Gear_Inventory/Fashion_Gear.md` preserves `# Визуальный язык Термоса` and `## 1. Четыре читаемых слоя`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-82 — Прогрессия Снаряжения

- **Source evidence:** `07_Gear_Inventory/Gear_Progression.md`, `# Прогрессия Снаряжения`, and `## 1. Обещание Прогрессии`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Gear_Progression.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `07_Gear_Inventory/Gear_Progression.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Прогрессия Снаряжения owner does not absorb `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/Weapon_Core`, `05_Combat_Survival/Magic_Batteries`, `07_Gear_Inventory/Item_Attributes_UI`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `05_Combat_Survival/Combat_Three_Debts`, `05_Combat_Survival/Weapon_Core`, `05_Combat_Survival/Magic_Batteries`, `07_Gear_Inventory/Item_Attributes_UI`.
- **Preserved meaning:** `07_Gear_Inventory/Gear_Progression.md` preserves `# Прогрессия Снаряжения` and `## 1. Обещание Прогрессии`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-83 — Механика: Архитектура Инвентаря (Mass & Access)

- **Source evidence:** `07_Gear_Inventory/Inventory_Architecture.md`, `# Механика: Архитектура Инвентаря (Mass & Access)`, and `## 1. Базовый Принцип`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Inventory_Architecture.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `07_Gear_Inventory/Inventory_Architecture.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Механика: Архитектура Инвентаря (Mass & Access) owner does not absorb `06_Economy_Loot/Extraction_Stabilization_Loop`, `08_World_Generation/Anomaly/14_Extraction_System`, `04_Player_Entities/_Registries/Registry_Interaction_Families`, `07_Gear_Inventory/Thermos_Assembly`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Extraction_Stabilization_Loop`, `08_World_Generation/Anomaly/14_Extraction_System`, `04_Player_Entities/_Registries/Registry_Interaction_Families`, `07_Gear_Inventory/Thermos_Assembly`.
- **Preserved meaning:** `07_Gear_Inventory/Inventory_Architecture.md` preserves `# Механика: Архитектура Инвентаря (Mass & Access)` and `## 1. Базовый Принцип`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-84 — Система: Удобство и Сортировка (QoL)

- **Source evidence:** `07_Gear_Inventory/Inventory_QoL.md`, `# Система: Удобство и Сортировка (QoL)`, and `## 1. Контекстная Иерархия Сортировки`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Inventory_QoL.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `07_Gear_Inventory/Inventory_QoL.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Система: Удобство и Сортировка (QoL) owner does not absorb `06_Economy_Loot/Extraction_Stabilization_Loop`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Extraction_Stabilization_Loop`.
- **Preserved meaning:** `07_Gear_Inventory/Inventory_QoL.md` preserves `# Система: Удобство и Сортировка (QoL)` and `## 1. Контекстная Иерархия Сортировки`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-85 — Атрибуты Предмета и UI (Item Passport)

- **Source evidence:** `07_Gear_Inventory/Item_Attributes_UI.md`, `# Атрибуты Предмета и UI (Item Passport)`, and `## 1. Всплывающая Подсказка (Tooltip)`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Item_Attributes_UI.md`.
- **Entity role:** projection of already-owned state.
- **Mechanic owner:** the linked owner; this page only projects it.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Атрибуты Предмета и UI (Item Passport) owner does not absorb `07_Gear_Inventory/Dissonance_Value`, `07_Gear_Inventory/Gear_Progression`, `05_Combat_Survival/_Registries/Registry_Weapons`, `07_Gear_Inventory/Thermos_System`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `07_Gear_Inventory/Dissonance_Value`, `07_Gear_Inventory/Gear_Progression`, `05_Combat_Survival/_Registries/Registry_Weapons`, `07_Gear_Inventory/Thermos_System`.
- **Preserved meaning:** `07_Gear_Inventory/Item_Attributes_UI.md` preserves `# Атрибуты Предмета и UI (Item Passport)` and `## 1. Всплывающая Подсказка (Tooltip)`: the player-visible projection remains a read of state owned elsewhere.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-86 — Процесс Обыска (Interaction Loop)

- **Source evidence:** `07_Gear_Inventory/Looting_Process.md`, `# Процесс Обыска (Interaction Loop)`, and `## 1. Тайминги и Риск`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Looting_Process.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `07_Gear_Inventory/Looting_Process.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Процесс Обыска (Interaction Loop) owner does not absorb `06_Economy_Loot/Extraction_Stabilization_Loop`, `07_Gear_Inventory/Containers_Slots`, `06_Economy_Loot/Loot_Distribution`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Extraction_Stabilization_Loop`, `07_Gear_Inventory/Containers_Slots`, `06_Economy_Loot/Loot_Distribution`.
- **Preserved meaning:** `07_Gear_Inventory/Looting_Process.md` preserves `# Процесс Обыска (Interaction Loop)` and `## 1. Тайминги и Риск`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-87 — Механика: Физический Вес (Physical Weight)

- **Source evidence:** `07_Gear_Inventory/Physical_Weight.md`, `# Механика: Физический Вес (Physical Weight)`, and `## 1. Разделение понятий`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Physical_Weight.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `07_Gear_Inventory/Physical_Weight.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Механика: Физический Вес (Physical Weight) owner does not imply a second resolver beyond its recorded 1. Разделение понятий contract; its own rule terms remain the only authority here.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `07_Gear_Inventory/Physical_Weight.md` preserves `# Механика: Физический Вес (Physical Weight)` and `## 1. Разделение понятий`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-88 — Архитектура Схрона и Менеджмент (Stash & Organization)

- **Source evidence:** `07_Gear_Inventory/Stash_Architecture.md`, `# Архитектура Схрона и Менеджмент (Stash & Organization)`, and `## 1. Концепция: Общий Склад (Account-Wide)`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Stash_Architecture.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `07_Gear_Inventory/Stash_Architecture.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Архитектура Схрона и Менеджмент (Stash & Organization) owner does not absorb `06_Economy_Loot/Economy_Core`, `07_Gear_Inventory/Inventory_QoL`, `07_Gear_Inventory/Inventory_Architecture`, `03_Factions_Societies/Lore/City_Genesis`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `06_Economy_Loot/Economy_Core`, `07_Gear_Inventory/Inventory_QoL`, `07_Gear_Inventory/Inventory_Architecture`, `03_Factions_Societies/Lore/City_Genesis`.
- **Preserved meaning:** `07_Gear_Inventory/Stash_Architecture.md` preserves `# Архитектура Схрона и Менеджмент (Stash & Organization)` and `## 1. Концепция: Общий Склад (Account-Wide)`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-89 — Сборка Термоса

- **Source evidence:** `07_Gear_Inventory/Thermos_Assembly.md`, `# Сборка Термоса`, and `## 1. Runtime entities`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Thermos_Assembly.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `07_Gear_Inventory/Thermos_Assembly.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** the Сборка Термоса owner does not absorb `07_Gear_Inventory/Thermos_System`, `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces`, `04_Player_Entities/_Registries/Registry_Parameter_Contracts`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `07_Gear_Inventory/Thermos_System`, `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces`, `04_Player_Entities/_Registries/Registry_Parameter_Contracts`.
- **Preserved meaning:** `07_Gear_Inventory/Thermos_Assembly.md` preserves `# Сборка Термоса` and `## 1. Runtime entities`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-90 — Термос: носимая система экипировки

- **Source evidence:** `07_Gear_Inventory/Thermos_System.md`, `# Термос: носимая система экипировки`, and `## 1. Четыре слоя сущностей`; its frontmatter direct dependencies were inspected.
- **Target owner:** `07_Gear_Inventory/Thermos_System.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `07_Gear_Inventory/Thermos_System.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** the Термос: носимая система экипировки owner does not absorb `07_Gear_Inventory/Thermos_Assembly`, `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces`, `04_Player_Entities/_Registries/Registry_Parameter_Contracts`; those linked owners retain their own inputs, state, costs, and failure handling.
- **Direct consumers and linked pages:** `07_Gear_Inventory/Thermos_Assembly`, `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces`, `04_Player_Entities/_Registries/Registry_Parameter_Contracts`.
- **Preserved meaning:** `07_Gear_Inventory/Thermos_System.md` preserves `# Термос: носимая система экипировки` and `## 1. Четыре слоя сущностей`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-91 — Реестр: Объекты Карты (Map Table Objects)

- **Source evidence:** `08_World_Generation/_Registries/Registry_POIs.md`, `# Реестр: Объекты Карты (Map Table Objects)`, and `## Контракт адресного POI`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/_Registries/Registry_POIs.md`.
- **Entity role:** atomic definition records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** a POI record does not resolve anomaly phase, civic-event lifecycle, location revision, generation strategy, or the Hub’s rendered map.
- **Direct consumers and linked pages:** `08_World_Generation/Anomaly/Anomaly_System`, `08_World_Generation/City_State/Civic_Event_Lifecycle`, `08_World_Generation/Generation/21_Location_Revision_Lifecycle`, `08_World_Generation/Generation/12_Generation_Strategies`.
- **Preserved meaning:** `08_World_Generation/_Registries/Registry_POIs.md` preserves `# Реестр: Объекты Карты (Map Table Objects)` and `## Контракт адресного POI`: its atomic record fields remain definitions, while linked mechanics retain resolution.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-92 — Registry: Raid Interfaces

- **Source evidence:** `08_World_Generation/_Registries/Registry_Raid_Interfaces.md`, `# Registry: Raid Interfaces`, and `## Owner-ID convention`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/_Registries/Registry_Raid_Interfaces.md`.
- **Entity role:** directional interface records.
- **Mechanic owner:** the linked mechanic/system owners named by the record.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the registry records directional handoffs; it does not evaluate entry, egress, return delivery, Apex survival, or the missing UI projection.
- **Direct consumers and linked pages:** `04_Player_Entities/Lifecycle_Resolver`, `04_Player_Entities/Last_Thread_Recovery`, `08_World_Generation/Generation/19_Raid_Approach_and_Entry`, `08_World_Generation/Generation/20_Egress_Solvency`.
- **Preserved meaning:** `08_World_Generation/_Registries/Registry_Raid_Interfaces.md` preserves `# Registry: Raid Interfaces` and `## Owner-ID convention`: its directional relation fields remain non-normative handoffs.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Blocked gap:** `UI_PROJECTION` is explicit in the owner; no canonical path is supplied, so it remains `MISSING_OWNER`.
- **Approval and validation:** no migration; `APPROVAL_REQUIRED` until the named owner exists.

### M-93 — Ядро Аномалии: Правила Арены

- **Source evidence:** `08_World_Generation/Anomaly/00_Anomaly_Core_Loop.md`, `# Ядро Аномалии: Правила Арены`, and `## 1. Мета-Правила Сессии`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Anomaly/00_Anomaly_Core_Loop.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Anomaly/00_Anomaly_Core_Loop.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the arena loop does not own the server clock, physical insertion, egress solvency, threshold assignment, or pressure thresholds.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/07_Server_Lifecycle`, `08_World_Generation/Anomaly/14_Extraction_System`, `08_World_Generation/Generation/08_Gate_Check`, `08_World_Generation/Generation/19_Raid_Approach_and_Entry`.
- **Preserved meaning:** `08_World_Generation/Anomaly/00_Anomaly_Core_Loop.md` preserves `# Ядро Аномалии: Правила Арены` and `## 1. Мета-Правила Сессии`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-94 — Опасности Среды

- **Source evidence:** `08_World_Generation/Anomaly/05_Hazards_Traps.md`, `# Опасности Среды`, and `## 1. Аномальные Ловушки`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Anomaly/05_Hazards_Traps.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Anomaly/05_Hazards_Traps.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** hazard and trap content does not own sector topology, global weather, mob physiology, extraction, or player-body resolution.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Anomaly/05_Hazards_Traps.md` preserves `# Опасности Среды` and `## 1. Аномальные Ловушки`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-95 — Insertion Logic

- **Source evidence:** `08_World_Generation/Anomaly/13_Insertion_Logic.md`, `# Insertion Logic`, and `## Responsibility`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Anomaly/13_Insertion_Logic.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Anomaly/13_Insertion_Logic.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** physical breach resolution does not choose the target quote, price of approach, egress solvency, Dawn fate, or Recovery outcome.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/19_Raid_Approach_and_Entry`, `08_World_Generation/Generation/20_Egress_Solvency`, `08_World_Generation/Generation/07_Server_Lifecycle`, `04_Player_Entities/Spawn_Logic`.
- **Preserved meaning:** `08_World_Generation/Anomaly/13_Insertion_Logic.md` preserves `# Insertion Logic` and `## Responsibility`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-96 — Нестабильные Пороги: обычный выход

- **Source evidence:** `08_World_Generation/Anomaly/14_Extraction_System.md`, `# Нестабильные Пороги: обычный выход`, and `## Responsibility`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Anomaly/14_Extraction_System.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Anomaly/14_Extraction_System.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** threshold search and sync do not own exit-count sufficiency, physical custody delivery, Return Manifest, Seal/Apex/Dawn, or Recovery fate.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/20_Egress_Solvency`, `06_Economy_Loot/Return_Manifest_Contract`, `08_World_Generation/Generation/07_Server_Lifecycle`, `08_World_Generation/Anomaly/17_Apex_Last_Hour`.
- **Preserved meaning:** `08_World_Generation/Anomaly/14_Extraction_System.md` preserves `# Нестабильные Пороги: обычный выход` and `## Responsibility`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-97 — Система линий мутаций Аномалии

- **Source evidence:** `08_World_Generation/Anomaly/16_Anomaly_Mutation_Lines.md`, `# Система линий мутаций Аномалии`, and `## Ответственность`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Anomaly/16_Anomaly_Mutation_Lines.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Anomaly/16_Anomaly_Mutation_Lines.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** mutation-line selection and stage transition do not own a global mob-stat resolver, local scene state, or a second weather system.
- **Direct consumers and linked pages:** `08_World_Generation/Anomaly/Anomaly_System`, `08_World_Generation/Generation/07_Server_Lifecycle`, `08_World_Generation/_Registries/Registry_Anomaly_Mutations`, `08_World_Generation/Content/World_Atlas/Sectors/_Sector_Manifest_Template`.
- **Preserved meaning:** `08_World_Generation/Anomaly/16_Anomaly_Mutation_Lines.md` preserves `# Система линий мутаций Аномалии` and `## Ответственность`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-98 — Apex Last Hour

- **Source evidence:** `08_World_Generation/Anomaly/17_Apex_Last_Hour.md`, `# Apex Last Hour`, and `## Responsibility`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Anomaly/17_Apex_Last_Hour.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Anomaly/17_Apex_Last_Hour.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** sealed-Apex survival does not own the clock, ingress closure, per-Presence survival eligibility, manifest delivery, or Recovery fate.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/07_Server_Lifecycle`, `08_World_Generation/Generation/20_Egress_Solvency`, `04_Player_Entities/Recovery_Lifecycle`, `08_World_Generation/_Registries/Registry_Raid_Interfaces`.
- **Preserved meaning:** `08_World_Generation/Anomaly/17_Apex_Last_Hour.md` preserves `# Apex Last Hour` and `## Responsibility`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Blocked gap:** `UI_PROJECTION` is explicit in the owner; no canonical path is supplied, so it remains `MISSING_OWNER`.
- **Approval and validation:** no migration; `APPROVAL_REQUIRED` until the named owner exists.

### M-99 — Система: Аномалии (The Anomaly Engine)

- **Source evidence:** `08_World_Generation/Anomaly/Anomaly_System.md`, `# Система: Аномалии (The Anomaly Engine)`, and `## 0. Что такое Аномалия`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Anomaly/Anomaly_System.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Anomaly/Anomaly_System.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the anomaly ecology does not resolve player status policy, extraction settlement, individual mutation-stage content, or faction lore authority.
- **Direct consumers and linked pages:** `02_World_Lore/The_Ark`, `02_World_Lore/The_Entity`, `03_Factions_Societies/Lore/The_Cathedral`, `05_Combat_Survival/Status_Effects`.
- **Preserved meaning:** `08_World_Generation/Anomaly/Anomaly_System.md` preserves `# Система: Аномалии (The Anomaly Engine)` and `## 0. Что такое Аномалия`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-100 — CityState и жизненный цикл городских явлений

- **Source evidence:** `08_World_Generation/City_State/Civic_Event_Lifecycle.md`, `# CityState и жизненный цикл городских явлений`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/City_State/Civic_Event_Lifecycle.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/City_State/Civic_Event_Lifecycle.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** city-event transitions do not create a pledge, choose a Pawn, grant an individual reward, or determine reputation.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/21_Location_Revision_Lifecycle`, `08_World_Generation/Generation/07_Server_Lifecycle`, `08_World_Generation/Hub/01_Hub_Map_Table`, `03_Factions_Societies/Quest_Engine`.
- **Preserved meaning:** `08_World_Generation/City_State/Civic_Event_Lifecycle.md` preserves `# CityState и жизненный цикл городских явлений` and `## 1. Обещание`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-101 — Ночные Верстаки

- **Source evidence:** `08_World_Generation/Generation/02_Mechanic_Night_Benches.md`, `# Ночные Верстаки`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/02_Mechanic_Night_Benches.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Generation/02_Mechanic_Night_Benches.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** night-bench operation does not resolve field-crafting legality, loot synchronization, or barter settlement.
- **Direct consumers and linked pages:** `05_Combat_Survival/Field_Crafting`, `06_Economy_Loot/Loot_Sync_Cycle`, `06_Economy_Loot/Barter_System`.
- **Preserved meaning:** `08_World_Generation/Generation/02_Mechanic_Night_Benches.md` preserves `# Ночные Верстаки` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-102 — Динамическая Погода

- **Source evidence:** `08_World_Generation/Generation/03_Dynamic_Weather.md`, `# Динамическая Погода`, and `## 1. Источник Погоды`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/03_Dynamic_Weather.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Generation/03_Dynamic_Weather.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** weather state does not resolve topology, faction access, loot custody, spawn, exit, or combat damage.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Generation/03_Dynamic_Weather.md` preserves `# Динамическая Погода` and `## 1. Источник Погоды`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-103 — Ротация Активных и Stable-Секторов

- **Source evidence:** `08_World_Generation/Generation/04_Global_Map_Rotation.md`, `# Ротация Активных и Stable-Секторов`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/04_Global_Map_Rotation.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Generation/04_Global_Map_Rotation.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** active/stable sector rotation does not publish a location revision, set the server clock, render the Hub, or settle civic events.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/21_Location_Revision_Lifecycle`, `08_World_Generation/Generation/07_Server_Lifecycle`, `08_World_Generation/Hub/01_Hub_Map_Table`, `08_World_Generation/City_State/Civic_Event_Lifecycle`.
- **Preserved meaning:** `08_World_Generation/Generation/04_Global_Map_Rotation.md` preserves `# Ротация Активных и Stable-Секторов` and `## 1. Обещание`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-104 — Слоты Сложности (Tier Spread)

- **Source evidence:** `08_World_Generation/Generation/05_Difficulty_Slots.md`, `# Слоты Сложности (Tier Spread)`, and `## 1. Правило "Трех Аномалий"`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/05_Difficulty_Slots.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Generation/05_Difficulty_Slots.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** tier spread does not set combat numbers, loot tables, admission eligibility, or a global progression rating.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Generation/05_Difficulty_Slots.md` preserves `# Слоты Сложности (Tier Spread)` and `## 1. Правило "Трех Аномалий"`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-105 — Асинхронные таймеры и regional service

- **Source evidence:** `08_World_Generation/Generation/06_Async_Timers.md`, `# Асинхронные таймеры и regional service`, and `## 1. Ответственность`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/06_Async_Timers.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Generation/06_Async_Timers.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** regional service does not own the SessionID clock, phase band, PhaseRevision, Seal/Dawn barrier, or player outcome.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/07_Server_Lifecycle`, `08_World_Generation/Generation/19_Raid_Approach_and_Entry`, `04_Player_Entities/Recovery_Lifecycle`, `08_World_Generation/Hub/01_Hub_Map_Table`.
- **Preserved meaning:** `08_World_Generation/Generation/06_Async_Timers.md` preserves `# Асинхронные таймеры и regional service` and `## 1. Ответственность`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-106 — Жизненный цикл сервера

- **Source evidence:** `08_World_Generation/Generation/07_Server_Lifecycle.md`, `# Жизненный цикл сервера`, and `## 1. Единственный владелец времени и барьеров`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/07_Server_Lifecycle.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Generation/07_Server_Lifecycle.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** server time and barriers do not choose a lifecycle settlement, Recovery outcome, return custody, Hub projection, civic result, or location revision.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/06_Async_Timers`, `08_World_Generation/Generation/20_Egress_Solvency`, `08_World_Generation/Anomaly/17_Apex_Last_Hour`, `08_World_Generation/Anomaly/13_Insertion_Logic`.
- **Preserved meaning:** `08_World_Generation/Generation/07_Server_Lifecycle.md` preserves `# Жизненный цикл сервера` and `## 1. Единственный владелец времени и барьеров`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Blocked gap:** `LIFECYCLE_RESOLVER` is explicit in the owner; no canonical path is supplied, so it remains `MISSING_OWNER`.
- **Approval and validation:** no migration; `APPROVAL_REQUIRED` until the named owner exists.

### M-107 — Гейт-проверка

- **Source evidence:** `08_World_Generation/Generation/08_Gate_Check.md`, `# Гейт-проверка`, and `## Responsibility`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/08_Gate_Check.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Generation/08_Gate_Check.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the admission check does not own weather, threat pressure, mask rules, item calibration, Thermos legality, or topology relocation.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/07_Server_Lifecycle`, `05_Combat_Survival/Threat_Thresholds`, `05_Combat_Survival/Masks_Filters`, `07_Gear_Inventory/Item_Calibration_Matrix`.
- **Preserved meaning:** `08_World_Generation/Generation/08_Gate_Check.md` preserves `# Гейт-проверка` and `## Responsibility`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-108 — Логика Респавна Лута

- **Source evidence:** `08_World_Generation/Generation/09_Loot_Respawn.md`, `# Логика Респавна Лута`, and `## 1. Глобальный Реролл (Global Shift)`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/09_Loot_Respawn.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Generation/09_Loot_Respawn.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** loot refresh does not own item definitions, extraction custody, economy sinks, or server-lifecycle settlement.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Generation/09_Loot_Respawn.md` preserves `# Логика Респавна Лута` and `## 1. Глобальный Реролл (Global Shift)`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-109 — Топология Мира: Паттерн "Цветок"

- **Source evidence:** `08_World_Generation/Generation/10_World_Topology.md`, `# Топология Мира: Паттерн "Цветок"`, and `## 1. Иерархия Генерации`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/10_World_Topology.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Generation/10_World_Topology.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** macro topology does not assign encounter pressure, loot, weather, player physics, or an extraction result.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Generation/10_World_Topology.md` preserves `# Топология Мира: Паттерн "Цветок"` and `## 1. Иерархия Генерации`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-110 — Система Сокетов (Socket System)

- **Source evidence:** `08_World_Generation/Generation/11_Socket_System.md`, `# Система Сокетов (Socket System)`, and `## 1. Структура Данных`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/11_Socket_System.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Generation/11_Socket_System.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** socket data and snap rules do not choose sector content, runtime POI state, or a player's equipment topology.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Generation/11_Socket_System.md` preserves `# Система Сокетов (Socket System)` and `## 1. Структура Данных`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-111 — Стратегии Генерации Города

- **Source evidence:** `08_World_Generation/Generation/12_Generation_Strategies.md`, `# Стратегии Генерации Города`, and `## 1. Гибридный Подход (Skeleton & Meat)`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/12_Generation_Strategies.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Generation/12_Generation_Strategies.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** generation strategy does not publish a live revision, decide rotation, or resolve a session’s runtime state.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Generation/12_Generation_Strategies.md` preserves `# Стратегии Генерации Города` and `## 1. Гибридный Подход (Skeleton & Meat)`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-112 — Асинхронная Архитектура Мира

- **Source evidence:** `08_World_Generation/Generation/13_Async_Double_Buffer.md`, `# Асинхронная Архитектура Мира`, and `## 1. Двойная Буферизация (World A / World B)`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/13_Async_Double_Buffer.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Generation/13_Async_Double_Buffer.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** double buffering does not define gameplay eligibility, phase timing, loot rules, or player-facing state.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Generation/13_Async_Double_Buffer.md` preserves `# Асинхронная Архитектура Мира` and `## 1. Двойная Буферизация (World A / World B)`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-113 — Правила Наполнения Сектора

- **Source evidence:** `08_World_Generation/Generation/14_Sector_Content_Rules.md`, `# Правила Наполнения Сектора`, and `## 0. Обязательный манифест`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/14_Sector_Content_Rules.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Generation/14_Sector_Content_Rules.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** sector-content constraints do not own the global topology, server lifecycle, loot economy, or universal combat resolver.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Generation/14_Sector_Content_Rules.md` preserves `# Правила Наполнения Сектора` and `## 0. Обязательный манифест`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-114 — Слой Связности (Connectivity Layer)

- **Source evidence:** `08_World_Generation/Generation/15_Traversal_Shortcuts.md`, `# Слой Связности (Connectivity Layer)`, and `## 1. Цель Системы`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/15_Traversal_Shortcuts.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Generation/15_Traversal_Shortcuts.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** connectivity shortcuts do not own movement physics, verticality rules, world topology, or hazard resolution.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Generation/15_Traversal_Shortcuts.md` preserves `# Слой Связности (Connectivity Layer)` and `## 1. Цель Системы`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-115 — Протокол Данных Мини-карты

- **Source evidence:** `08_World_Generation/Generation/16_UI_Map_Protocol.md`, `# Протокол Данных Мини-карты`, and `## 1. Проблема Динамики`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/16_UI_Map_Protocol.md`.
- **Entity role:** projection of already-owned state.
- **Mechanic owner:** the linked owner; this page only projects it.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the map protocol presents published data; it does not select POIs, change a revision, gate entry, or resolve an event.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Generation/16_UI_Map_Protocol.md` preserves `# Протокол Данных Мини-карты` and `## 1. Проблема Динамики`: the player-visible projection remains a read of state owned elsewhere.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-116 — Raid Approach and Entry

- **Source evidence:** `08_World_Generation/Generation/19_Raid_Approach_and_Entry.md`, `# Raid Approach and Entry`, and `## Responsibility`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/19_Raid_Approach_and_Entry.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Generation/19_Raid_Approach_and_Entry.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** approach disclosure and commitment do not perform the physical breach, settle egress obligations, set server time, or evaluate the missing UI projection.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/07_Server_Lifecycle`, `08_World_Generation/Anomaly/13_Insertion_Logic`, `08_World_Generation/Generation/20_Egress_Solvency`, `08_World_Generation/_Registries/Registry_Raid_Interfaces`.
- **Preserved meaning:** `08_World_Generation/Generation/19_Raid_Approach_and_Entry.md` preserves `# Raid Approach and Entry` and `## Responsibility`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Blocked gap:** `UI_PROJECTION` is explicit in the owner; no canonical path is supplied, so it remains `MISSING_OWNER`.
- **Approval and validation:** no migration; `APPROVAL_REQUIRED` until the named owner exists.

### M-117 — Egress Solvency

- **Source evidence:** `08_World_Generation/Generation/20_Egress_Solvency.md`, `# Egress Solvency`, and `## Responsibility`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/20_Egress_Solvency.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Generation/20_Egress_Solvency.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** the egress supply envelope does not search or sync a threshold, commit a physical exit, return custody, or set session barriers.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/07_Server_Lifecycle`, `08_World_Generation/Anomaly/14_Extraction_System`, `08_World_Generation/Generation/19_Raid_Approach_and_Entry`, `06_Economy_Loot/Return_Manifest_Contract`.
- **Preserved meaning:** `08_World_Generation/Generation/20_Egress_Solvency.md` preserves `# Egress Solvency` and `## Responsibility`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-118 — Жизненный цикл ревизии локации

- **Source evidence:** `08_World_Generation/Generation/21_Location_Revision_Lifecycle.md`, `# Жизненный цикл ревизии локации`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Generation/21_Location_Revision_Lifecycle.md`.
- **Entity role:** shared state and lifecycle contract.
- **Mechanic owner:** `08_World_Generation/Generation/21_Location_Revision_Lifecycle.md`.
- **Universal system owner:** this owner is the declared shared-system scope; no second universal owner is inferred.
- **Does not own:** location revisions do not rotate the active pool, control the session clock, generate a sector, or resolve a civic contribution.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/04_Global_Map_Rotation`, `08_World_Generation/Generation/07_Server_Lifecycle`, `08_World_Generation/Generation/17_Dual_State_POIs`, `08_World_Generation/Generation/18_POI_Metadata_Registry`.
- **Preserved meaning:** `08_World_Generation/Generation/21_Location_Revision_Lifecycle.md` preserves `# Жизненный цикл ревизии локации` and `## 1. Обещание`: the declared lifecycle/state boundary remains singular and its linked consumers remain consumers.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-119 — Хаб: Операционный Бункер

- **Source evidence:** `08_World_Generation/Hub/00_Hub_Environment.md`, `# Хаб: Операционный Бункер`, and `## 1. Концепция Роли`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Hub/00_Hub_Environment.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Hub/00_Hub_Environment.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the Hub’s operational role and atmosphere do not resolve services, map pins, party admission, economy, or raid state.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Hub/00_Hub_Environment.md` preserves `# Хаб: Операционный Бункер` and `## 1. Концепция Роли`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-120 — Живая Миниатюра: Карта Рейдов и Адресов

- **Source evidence:** `08_World_Generation/Hub/01_Hub_Map_Table.md`, `# Живая Миниатюра: Карта Рейдов и Адресов`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Hub/01_Hub_Map_Table.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Hub/01_Hub_Map_Table.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the table presents a published WorldRevision and choices; it does not publish the revision, settle barter, resolve quests, or transition city events.
- **Direct consumers and linked pages:** `08_World_Generation/Hub/00_Hub_Environment`, `08_World_Generation/Hub/02_Hub_Services_Interaction`, `08_World_Generation/Hub/03_Hub_Map_Interaction`, `08_World_Generation/Generation/07_Server_Lifecycle`.
- **Preserved meaning:** `08_World_Generation/Hub/01_Hub_Map_Table.md` preserves `# Живая Миниатюра: Карта Рейдов и Адресов` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-121 — Сервисы Хаба: Работа Через Диораму

- **Source evidence:** `08_World_Generation/Hub/02_Hub_Services_Interaction.md`, `# Сервисы Хаба: Работа Через Диораму`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Hub/02_Hub_Services_Interaction.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Hub/02_Hub_Services_Interaction.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** the diorama interaction does not resolve barter transactions, Thermos legality, faction contracts, or the WorldRevision it displays.
- **Direct consumers and linked pages:** `08_World_Generation/Hub/01_Hub_Map_Table`, `08_World_Generation/Hub/03_Hub_Map_Interaction`, `06_Economy_Loot/Barter_System`, `07_Gear_Inventory/Thermos_System`.
- **Preserved meaning:** `08_World_Generation/Hub/02_Hub_Services_Interaction.md` preserves `# Сервисы Хаба: Работа Через Диораму` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-122 — Интерактивный Стол: Мирная Проекция

- **Source evidence:** `08_World_Generation/Hub/03_Hub_Map_Interaction.md`, `# Интерактивный Стол: Мирная Проекция`, and `## 1. Обещание`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Hub/03_Hub_Map_Interaction.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Hub/03_Hub_Map_Interaction.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** map interaction does not publish pins, alter location revision, resolve civic events, or create POI metadata.
- **Direct consumers and linked pages:** `08_World_Generation/Hub/01_Hub_Map_Table`, `08_World_Generation/Generation/21_Location_Revision_Lifecycle`, `08_World_Generation/City_State/Civic_Event_Lifecycle`, `08_World_Generation/Generation/17_Dual_State_POIs`.
- **Preserved meaning:** `08_World_Generation/Hub/03_Hub_Map_Interaction.md` preserves `# Интерактивный Стол: Мирная Проекция` and `## 1. Обещание`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-123 — Система Группы: Протокол "Стол"

- **Source evidence:** `08_World_Generation/Hub/05_Party_Syndicate.md`, `# Система Группы: Протокол "Стол"`, and `## 1. Концепция: Совместная Операция`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Hub/05_Party_Syndicate.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Hub/05_Party_Syndicate.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** party formation does not perform insertion, resolve a Pawn’s body state, or select a raid’s hidden target.
- **Direct consumers and linked pages:** `08_World_Generation/Anomaly/13_Insertion_Logic`, `04_Player_Entities/Entity_Grimoire`.
- **Preserved meaning:** `08_World_Generation/Hub/05_Party_Syndicate.md` preserves `# Система Группы: Протокол "Стол"` and `## 1. Концепция: Совместная Операция`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-124 — Гроссбух: Архитектура Сохранений

- **Source evidence:** `08_World_Generation/Persistence_Ledger.md`, `# Гроссбух: Архитектура Сохранений`, and `## 1. Модель "Check-in / Check-out"`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Persistence_Ledger.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Persistence_Ledger.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** check-in/check-out persistence does not own the server clock, raid settlement, item progression, or stash economy.
- **Direct consumers and linked pages:** `08_World_Generation/Generation/07_Server_Lifecycle`, `07_Gear_Inventory/Stash_Architecture`.
- **Preserved meaning:** `08_World_Generation/Persistence_Ledger.md` preserves `# Гроссбух: Архитектура Сохранений` and `## 1. Модель "Check-in / Check-out"`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

### M-125 — Целостность Реальности (Security & Validation)

- **Source evidence:** `08_World_Generation/Reality_Integrity.md`, `# Целостность Реальности (Security & Validation)`, and `## 1. Серверный Авторитаризм`; its frontmatter direct dependencies were inspected.
- **Target owner:** `08_World_Generation/Reality_Integrity.md`.
- **Entity role:** bounded player-facing mechanic.
- **Mechanic owner:** `08_World_Generation/Reality_Integrity.md`.
- **Universal system owner:** none beyond the linked mechanic/system contracts.
- **Does not own:** validation and reporting do not set game rules, combat outcomes, economy balances, player identity, or moderation policy.
- **Direct consumers and linked pages:** no `related_files` entry.
- **Preserved meaning:** `08_World_Generation/Reality_Integrity.md` preserves `# Целостность Реальности (Security & Validation)` and `## 1. Серверный Авторитаризм`: the player action, stated consequence, and direct-dependency boundaries remain in this mechanic.
- **Required skill or handoff:** system-architect and vault-curator evidence; no conditional specialist handoff was required.
- **Approval and validation:** no migration; owner-scoped `KEEP`.

## Approval gate and follow-up

`M-01a` is a completed conflict-free migration: its duplicated First Reception
lifecycle prose now resolves only through `04_Player_Entities/Spawn_Logic.md`,
with Lifecycle Roster retaining the admission predicate and the faction registry
retaining presentation. The remaining explicit blockers are the planned faction
interfaces, the `SOURCE_CONFLICT` for status application policy, missing Thermos
effect-domain owners, the Mark of Greed dungeon resolver, and the explicitly
named lifecycle/UI projection gaps. The Foundling historical slice remains
`KEEP` in `04_Player_Entities/Shell_Foundlings.md`.

All 116 coverage records are now `DETAILED`. `MISSING_OWNER`,
`SOURCE_CONFLICT`, `PENDING_OWNER`, and `APPROVAL_REQUIRED` streams remain
unedited; they block only the named resolver. The M-01a migration updated the
source lore projection and its existing interface record without route or
management-page changes.

Final validation uses `python3 tools/vault_guard.py`; it exits 0 with no output.
