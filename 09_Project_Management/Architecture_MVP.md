---
type: architecture
status: active
system: project_management
version: 3.0
tags:
  - structure
  - pipeline
  - vertical_slice
  - roadmap
---
# Архитектура Проекта: Элдрейн (MVP)

> **Статус:** актуальная структура после рефакторинга.
> **Цель:** держать вертикальный срез в 9 смысловых блоках и не возвращаться к старым пространствам имен.

---

## 1. Канонические Блоки

Проект организован вокруг 9 рабочих систем. Любая новая заметка должна попадать в один из этих блоков или в `_Archive`, если это источник для сверки, а не активная механика.

| Блок | Роль | Якорные файлы |
|:---|:---|:---|
| `01_Core_Vision` | Концепция, тон, основной цикл | [[01_Core_Vision/GDD_Main]], [[01_Core_Vision/02_Core_Loop]], [[01_Core_Vision/Glossary]] |
| `02_World_Lore` | Ковчег, Коллапс, Якорь, Сущность, магипанк и культуры | [[02_World_Lore/The_Ark]], [[02_World_Lore/The_Collapse]], [[02_World_Lore/The_Anchor]], [[02_World_Lore/Protocol_Resonance]], [[02_World_Lore/Culture_Language]] |
| `03_Factions_Societies` | Фракции, репутация, поручения, допуски, контракты и становление города | [[03_Factions_Societies/Registry_Factions]], [[03_Factions_Societies/Reputation_Rules]], [[03_Factions_Societies/Pledge_Contracts]], [[03_Factions_Societies/Quest_Engine]], [[03_Factions_Societies/Lore/City_Anatomy]] |
| `04_Player_Entities` | Оболочки, расы, классы, TOUCH, синергии | [[04_Player_Entities/Shell_Specification]], [[04_Player_Entities/MVP_3x3_Design_Contract]], [[04_Player_Entities/_Registries/Registry_Races]], [[04_Player_Entities/_Registries/Registry_Specs]], [[04_Player_Entities/Combat_Profile_Pipeline]] |
| `05_Combat_Survival` | Бой, магострелы, батареи, статусы, выживание | [[05_Combat_Survival/Weapon_Core]], [[05_Combat_Survival/Magic_Batteries]], [[05_Combat_Survival/Status_Effects]], [[05_Combat_Survival/Dissonance_System]] |
| `06_Economy_Loot` | Рез, рынок, бартер, аукцион, стабилизация лута | [[06_Economy_Loot/Economy_Core]], [[06_Economy_Loot/Currency_Rez]], [[06_Economy_Loot/Loot_Distribution]] |
| `07_Gear_Inventory` | Инвентарь, экипировка, предметы, крафт-реестры | [[07_Gear_Inventory/Inventory_Architecture]], [[07_Gear_Inventory/Gear_Progression]], [[07_Gear_Inventory/Equipment_PaperDoll]], [[07_Gear_Inventory/_Registries/Registry_Items]] |
| `08_World_Generation` | Сервер, таймеры, аномалии, вход, выход, атлас | [[08_World_Generation/Generation/07_Server_Lifecycle]], [[08_World_Generation/Generation/08_Gate_Check]], [[08_World_Generation/Generation/19_Access_Contracts]], [[08_World_Generation/Anomaly/Anomaly_System]] |
| `09_Project_Management` | Канбан, риски, планы, техническая кухня | [[09_Project_Management/TODO]], [[09_Project_Management/Risk_Register]], [[09_Project_Management/Architecture_MVP]] |

---

## 2. Правило Ссылок

Все YAML-поля связей должны ссылаться на существующие Obsidian-цели:

```yaml
related_files:
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
related_mechanics:
  - "[[08_World_Generation/Anomaly/Anomaly_System|Anomaly_System]]"
```

Правила:

- Использовать текущий путь от корня vault: `[[08_World_Generation/Anomaly/Anomaly_System]]`.
- Не использовать старые пространства имен `10_Mechanics`, `20_Lore`, `30_Content`, `00_Variables`.
- Если нужен короткий видимый текст, писать алиас: `[[08_World_Generation/Anomaly/14_Extraction_System|Extraction_System]]`.
- Если документ переехал или был смержен, ссылка должна вести в текущий канонический файл, а не в старое имя.
- Для registry-файлов ссылаться на сам реестр или на конкретный заголовок объекта, например [[03_Factions_Societies/Registry_Factions#Хранители (The Keepers)|Keepers]].

---

## 3. MVP Pipeline

Минимальный вертикальный срез должен проходить через одну связную цепочку:

1. Игрок выбирает Оболочку и сборку через [[04_Player_Entities/MVP_3x3_Design_Contract|контракт матрицы 3×3]] и [[04_Player_Entities/Combat_Profile_Pipeline|Combat_Profile_Pipeline]].
2. Карта Хаба показывает доступные T1/T2/T3 локации, цену маршрута и живые слоты через [[08_World_Generation/Hub/01_Hub_Map_Table|Hub_Map_Table]].
3. Перед входом игрок выбирает [[08_World_Generation/Generation/19_Access_Contracts|Access Contract]], а сборка проходит [[08_World_Generation/Generation/08_Gate_Check|Gate_Check]] и проверку Диссонанса через [[05_Combat_Survival/Dissonance_System|Dissonance_System]] / [[05_Combat_Survival/Threat_Thresholds|Threat_Thresholds]].
4. В рейде темп задают [[08_World_Generation/Generation/07_Server_Lifecycle|Server_Lifecycle]], [[08_World_Generation/Anomaly/Anomaly_System|Anomaly_System]] и [[05_Combat_Survival/Magic_Batteries|Magic_Batteries]].
5. После эвакуации лут проходит цикл экономики: [[07_Gear_Inventory/Looting_Process|Looting_Process]] -> [[06_Economy_Loot/Economy_Core|Economy_Core]] -> [[06_Economy_Loot/Barter_System|Barter_System]].

---

## 4. Контроль Долга

Если появляется заметка с неочевидным местом:

- сначала привязать ее к одному из 9 блоков;
- затем добавить `type`, `status`, `system`, `tags`;
- после этого прописать валидные `related_files` или `related_mechanics`;
- если это старый источник, перенести его в `_Archive` и оставить ссылку на канонический файл в [[_Archive/_MERGED_SOURCES|merge-log]].
