---
type: architecture
status: active
version: 2
tags:
  - structure
  - pipeline
  - vertical_slice
  - roadmap
---

# Архитектура Проекта: Элдрейн (MVP)

> **Статус:** Версия 2.0 (Cluster System)
> **Цель:** Создание "Вертикального Среза" (Vertical Slice) — полностью играбельного цикла на базе одного сектора.

---

## 1. Структура Папок (File Tree)

Проект организован по системе **"4 Столпа"**, что позволяет легко масштабировать контент, не ломая логику.

* **00_Core:** Фундамент и видение (Для геймдизайнеров).
* **10_Mechanics:** Правила игры (Для программистов).
* **20_Lore:** Литературное наполнение (Для нарративщиков и художников).
* **30_Content:** Игровые данные (Таблицы лута, статы мобов, уровни).

```text
Lang_RU/
├── 00_Core/                  # [ФУНДАМЕНТ]
│   ├── GDD_Main.md           # Главный дизайн-документ
│   ├── Vision.md             # Атмосфера и Столпы
│   └── Loop.md               # Геймплейный Цикл (Core & Meta)
│
├── 10_Mechanics/             # [ПРАВИЛА]
│   ├── City/                 # Городской слой
│   │   ├── City_Structure.md
│   │   ├── City_Structure_Generation.md
│   │   ├── Hub_UI.md
│   │   └── Facilities_Services.md
│   ├── Combat/               # Боевая система
│   │   ├── Damage_System.md  # HP, Раны, Смерть
│   │   ├── Skills_Archetypes.md
│   │   └── Status_Effects.md
│   ├── Economy/              # Экономика
│   │   ├── Economy_City.md
│   │   ├── Currency_Entropy.md # Инфляция и Распад
│   │   └── Economy_Monetization.md
│   ├── Inventory/            # Предметы
│   │   ├── Inventory_Core.md
│   │   ├── Equipment_Entropy.md # Износ и Починка
│   │   └── Consumables_Rules.md
│   ├── Magic/                # Магия
│   │   ├── Magic_System.md
│   │   └── Energy_System.md  # Батареи
│   ├── Meta/                 # Прогрессия аккаунта
│   │   ├── Character_Deck.md # Ростер персонажей
│   │   ├── Tags_System.md    # Теги и Билды
│   │   ├── Reputation_System.md
│   │   └── Races_Mechanics.md
│   └── World/                # Правила мира
│       ├── Anomaly_System.md
│       ├── Extraction_Rules.md
│       └── Quest_Engine.md
│
├── 20_Lore/                  # [НАРРАТИВ]
│   ├── 01_World_Foundation/  # Физика мира (Якорь, Сущность)
│   ├── 02_Societies_Factions/# Фракции (Собор, Синдикат, Хранители)
│   ├── 03_Districts_Geography/# Описание районов (Лор)
│   ├── 04_Species_Cultures/  # Расы
│   └── 05_Daily_Life/        # Быт (Валюта, Мода, Еда)
│
└── 30_Content/               # [КОНТЕНТ MVP]
    ├── Items/                # База предметов (JSON/Tables)
    └── World_Atlas/          # Кластерная карта
        ├── _Sector_Template.md
        ├── 00_Safe_Zone_Hub/ # Хаб: Центральный Банк
        └── 01_Core_Sectors/
            └── Sector_01_Port/ # Ржавый Порт (Starter Zone)
                ├── 00_Description.md
                ├── 01_Bestiary.md
                ├── 02_Dungeons.md
                └── 03_Loot_Table.md