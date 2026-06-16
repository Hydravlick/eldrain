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

