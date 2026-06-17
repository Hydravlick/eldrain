---
type: archive_log
status: active
tags: [archive, merge_log, refactor]
date: 2026-06-16
---

# Merge Log: Archive Cleanup

Архивные файлы ниже разобраны и больше не являются источниками канона. Сильные идеи перенесены в актуальные системные папки, слабые и дублирующие части отброшены.

## Перенесено

| Архивный источник | Что было ценно | Куда перенесено |
|:---|:---|:---|
| `_Archive/Duplicates/Physical_Weight_v2.md` | `TotalLoad = BodyGear + PocketsContent + BackSlotItem`, Back Slot, `Critical >120%` | [[07_Gear_Inventory/Physical_Weight]], [[07_Gear_Inventory/Inventory_Architecture]] |
| `_Archive/Untitled/Root_Untitled_1.md` | `SessionID` anti-exploit, hot PvP loot, запрет laundering через drop/pickup | [[07_Gear_Inventory/Resonance_Value]], [[06_Economy_Loot/Loot_Sync_Cycle]] |
| `_Archive/Untitled/Root_Untitled.md` | Reality Damage / Reality Injection, стартовый долг, стабилизированные твари как товар | [[06_Economy_Loot/Currency_Rez]], [[06_Economy_Loot/Currency_Rezs_Lore]], [[03_Factions_Societies/Quest_Engine]], [[03_Factions_Societies/Lore/New_Factions]] |
| `_Archive/Untitled/Quest_Engine_Layered_Generation.md` | знание как валюта, breadcrumbs -> jackpot, counter-contracts, доска расследований | [[03_Factions_Societies/Quest_Engine_Grammar]] |
| `_Archive/Duplicates/00_Master_Index_v3.md` | структура старого индекса | Не переносилось: заменено [[00_Index]] |
| `_Archive/Legacy/00_Index_legacy.md` | старое резюме проекта | Не переносилось: актуальные идеи уже живут в [[01_Core_Vision/GDD_Main]] и [[00_Index]] |
| `09_Project_Management/TO-DO_List_Legacy.md` | старый рабочий backlog, полезные narrative seeds, уже интегрированные refactor-задачи | Рабочие задачи очищены в [[09_Project_Management/TODO]], полезные seeds вынесены в [[Reference Notes New]], интегрированные блоки отмечены ниже |
| `Weak Sides.md` | список конфликтов MVP, слабые места лупа, экономика, бой, хаб, сезоны | Риски перенесены в [[09_Project_Management/Risk_Register]], задачи - в [[09_Project_Management/TODO]], полезные seeds - в [[Reference Notes New]] |
| `01_Core_Vision/Loop.md` | старое описание базового лупа | Слито в [[01_Core_Vision/02_Core_Loop]] |
| `01_Core_Vision/Vision.md` | бытовая магия, единство в хаосе, референсы тона | Слито в [[01_Core_Vision/01_Vision]] |
| `01_Core_Vision/03_Glossary.md` | расширенные определения Сущности, Энтропии, Якоря, Реза, Оболочек | Слито в [[01_Core_Vision/Glossary]] |
| `02_World_Lore/01_Cosmogony.md` | космогония, рождение Сущности, роль Коллапса | Слито в [[02_World_Lore/The_Collapse]] и [[02_World_Lore/The_Entity]] |
| `02_World_Lore/02_Anchor_and_Entropy.md` | связка Якоря и Энтропии | Слито в [[02_World_Lore/The_Anchor]] и [[02_World_Lore/The_Entropy]] |
| `02_World_Lore/03_Magipunk_Physics.md` | магия как промышленная технология и батарейная логика | Слито в [[02_World_Lore/Magipunk_Physics]] и [[02_World_Lore/Energy_Concept]] |
| `02_World_Lore/04_Culture_Assimilation.md` | культурная ассимиляция, чужие физики, Протокол Резонанса | Слито в [[02_World_Lore/Culture_Language]] и [[02_World_Lore/Protocol_Resonance]] |
| `09_Project_Management/Action_Plan_Update.md` | рабочие refactor-задачи и стабилизация систем | Свернуто в [[09_Project_Management/TODO]] и актуальные системные файлы |
| `09_Project_Management/Lore_Update.md` | seeds по Ancients, Keepers, True Matrices, Living Circuits | Свернуто в [[Reference Notes New#Cosmogony Overhaul]] |

## Legacy TODO Digest

Старый `TO-DO_List_Legacy` больше не является рабочей доской. Его содержимое разобрано на три категории.

### Уже Интегрировано

| Старый блок | Текущая точка правды |
|:---|:---|
| Loop pacing, 6-часовой сервер, фазовый серфинг | [[01_Core_Vision/02_Core_Loop]], [[08_World_Generation/Generation/07_Server_Lifecycle]], [[08_World_Generation/Generation/08_Gate_Check]] |
| Environment gatekeeping, жесткий фильтр гира | [[08_World_Generation/Generation/08_Gate_Check]], [[05_Combat_Survival/Threat_Thresholds]] |
| Батареи, кантрипы, Reality Burn | [[05_Combat_Survival/Magic_Batteries]], [[06_Economy_Loot/Currency_Rez]], [[04_Player_Entities/Attributes_TOUCH]] |
| Стабилизация `Volatile`-лута | [[06_Economy_Loot/Economy_Core]], [[06_Economy_Loot/Sinks_Insurance]], [[07_Gear_Inventory/Item_Attributes_UI]] |
| Найденыши и капсулы | [[04_Player_Entities/Shell_Foundlings]], [[04_Player_Entities/Lifecycle_Roster]], [[06_Economy_Loot/Auction_House]] |
| Two-Paradox и боевой профиль | [[04_Player_Entities/Two_Paradox_Birth]], [[04_Player_Entities/Combat_Profile_Pipeline]], [[04_Player_Entities/_Matrices/00_Character_Matrix]] |
| Blood Debt tutorial seed | [[03_Factions_Societies/Quest_Engine]], [[03_Factions_Societies/Lore/New_Factions]], [[Reference Notes New#Blood Debt Tutorial]] |

### Перенесено в Reference Notes

- [[Reference Notes New#The Keeper's Breach]]
- [[Reference Notes New#Selection Protocol]]
- [[Reference Notes New#Blood Debt Tutorial]]
- [[Reference Notes New#Stabilized Living Cargo]]
- [[Reference Notes New#Redemption Runs]]

### Закрыто Без Переноса

- Завершенные refactor-пункты больше не дублируются в TODO.
- Проверка пустых старых папок закрыта: в корне проекта они не найдены.
- Ненужные старые цели заменены текущими каноническими файлами.
- Большие сырые вставки из старого диалога больше не считаются задачами; их смысл свернут в reference notes.

## Weak Sides Digest

`Weak Sides.md` больше не является рабочей заметкой. Она была полезна как аудит конфликтов, но после разбора стала дублировать канон, risk register и TODO.

### Уже Закрыто В Каноне

| Конфликт | Текущая точка правды |
|:---|:---|
| Непонятный 10-45 минутный луп против 6-часовой локации | [[01_Core_Vision/02_Core_Loop]], [[08_World_Generation/Generation/07_Server_Lifecycle]] |
| Жесткий фильтр гира и вход в более опасную фазу | [[08_World_Generation/Generation/08_Gate_Check]], [[05_Combat_Survival/Threat_Thresholds]] |
| Дальний бой как магическое оружие, батареи и высокий TTK | [[05_Combat_Survival/Magic_Batteries]], [[05_Combat_Survival/Weapon_Core]], [[05_Combat_Survival/Weapon_Ranged]] |
| Удаление полной деградации предметов | [[07_Gear_Inventory/Item_Attributes_UI]], [[06_Economy_Loot/Economy_Core]] |
| TOUCH, скрытые подхарактеристики и боевой профиль | [[04_Player_Entities/Attributes_TOUCH]], [[04_Player_Entities/Combat_Profile_Pipeline]] |
| Валюта Rez отдельно от святого урона | [[06_Economy_Loot/Currency_Rez#6. Урон Реальностью (Reality Burn)]], [[05_Combat_Survival/Weapon_Core#7. Стихии и импульсы]] |
| Три активные локации с фазовым сдвигом | [[08_World_Generation/Generation/07_Server_Lifecycle]], [[08_World_Generation/Generation/04_Global_Map_Rotation]] |

### Оставлено Как Будущая Задача

- Мертвый игрок, VOIP после смерти и spectator loop вынесены в [[09_Project_Management/TODO]].
- AFK/disconnect и защита от злоупотреблений вынесены в [[09_Project_Management/TODO]].
- Удаленное присутствие в хабе и физический PvP уточняются через [[09_Project_Management/Risk_Register]].
- Guild/Clan, prestige/seasons и pitch one-pager оставлены как поздние задачи, чтобы не раздувать MVP.

## Отброшено

- Старые индексы и устаревшая навигация.
- Повторяющиеся описания контрактов, pins и таймеров квестов.
- Рабочие пояснения "что изменено", не являющиеся каноном.
- Дубли старых формул там, где новая структура уже точнее.

## Текущий Канон После Чистки

- Игровой луп: [[01_Core_Vision/02_Core_Loop]]
- 6-часовая жизнь локации: [[08_World_Generation/Generation/07_Server_Lifecycle]]
- Жесткий gear-filter: [[08_World_Generation/Generation/08_Gate_Check]]
- Резонанс и происхождение предметов: [[07_Gear_Inventory/Resonance_Value]], [[06_Economy_Loot/Loot_Sync_Cycle]]
- Экономика наград: [[06_Economy_Loot/Economy_Core]]
- Квесты и расследования: [[03_Factions_Societies/Quest_Engine]], [[03_Factions_Societies/Quest_Engine_Grammar]]
