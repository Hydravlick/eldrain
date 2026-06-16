---
type: architecture
status: active
version: 2.1
tags:
  - structure
  - pipeline
  - vertical_slice
  - roadmap
---

# Архитектура Проекта: Элдрейн (MVP)

> **Статус:** Версия 2.1 (Full Structure Update)
> **Цель:** Создание "Вертикального Среза" (Vertical Slice) — полностью играбельного цикла на базе одного сектора.

---

## 1. Структура Папок (File Tree)

Проект организован по системе **"5 Столпов"**, охватывающих фундамент, переменные, механику, лор и контент.

* **00_Core:** Фундамент и видение.
* **00_Variables:** Реестры данных, матрицы баланса и константы.
* **10_Mechanics:** Техническая документация и правила систем.
* **20_Lore:** Нарративное наполнение.
* **30_Content:** Игровые данные и атлас мира.

```text
LegacyLangRU/
├── 00_Core/                  # [ФУНДАМЕНТ]
│   ├── 00_Index.md
│   ├── GDD_Main.md           # Главный дизайн-документ
│   ├── Glossary.md           # Глоссарий терминов
│   ├── Loop.md               # Геймплейный цикл
│   └── Vision.md             # Видение проекта
│
├── 00_Variables/             # [ПЕРЕМЕННЫЕ И РЕЕСТРЫ]
│   ├── 00_Archetype_Matrix.md
│   ├── 00_Biome_Matrix.md
│   ├── 00_Character_Matrix.md
│   ├── 00_Faction_Reputation.md
│   ├── 00_Synergy_Map.md
│   ├── Registry_Armors.md
│   ├── Registry_Biomes.md
│   ├── Registry_Blueprints.md
│   ├── Registry_Combos.md
│   ├── Registry_Consumables.md
│   ├── Registry_CraftingRecipes.md
│   ├── Registry_Factions.md
│   ├── Registry_Headwear.md
│   ├── Registry_Items.md
│   ├── Registry_Mobs.md
│   ├── Registry_POIs.md
│   ├── Registry_Races.md
│   ├── Registry_Skill_Types.md
│   ├── Registry_Specs.md
│   ├── Registry_StatusEffects.md
│   ├── Registry_Tags.md
│   └── Registry_Weapons.md
│
├── 10_Mechanics/             # [МЕХАНИКИ И ПРАВИЛА]
│   ├── 01_Player_Core/       # Сущность игрока
│   │   ├── 01_Entity_Grimoire.md
│   │   ├── 02_Shell_Specification.md
│   │   ├── 03_Shell_Construction.md
│   │   ├── 04_Attributes_TOUCH.md
│   │   ├── 05_Ability_Synergy.md
│   │   ├── 06_Proficiency_Arsenal.md
│   │   ├── 07_Tags_System.md
│   │   └── 08_Lifecycle_Roster.md
│   │
│   ├── 02_Action_Combat/     # Боевая система
│   │   ├── 01_Movement_Physics.md
│   │   ├── 02_Acoustic_Stealth.md
│   │   ├── 03_Resonance_System.md
│   │   ├── 04_Ballistics_Armor.md
│   │   ├── 05_Ballistics_PvP.md
│   │   ├── 06_Ballistics_PvE.md
│   │   ├── 07_Threat_Thresholds.md
│   │   ├── 08_Weapon_Core.md
│   │   ├── 09_Weapon_Melee.md
│   │   ├── 10_Weapon_Ranged.md
│   │   ├── 11_Combat_Consumables.md
│   │   ├── 12_Magic_Batteries.md
│   │   ├── 13_Masks_Filters.md
│   │   ├── 14_Status_Effects.md
│   │   ├── 15_Field_Crafting.md
│   │   ├── 16_Threat_Thresholds.md
│   │   └── 17_Traversal_Core.md
│   │
│   ├── 03_Economy/           # Экономика
│   │   ├── 00_Economy_Core.md
│   │   ├── 01_Currency_Rez.md
│   │   ├── 02_Premium_Shards.md
│   │   ├── 04_Spawn_Logic.md
│   │   ├── 05_Sinks_Insurance.md
│   │   ├── 06_Barter_System.md
│   │   ├── 07_Vendor_Logic.md
│   │   ├── 08_Blueprints.md
│   │   ├── 09_Craft_Modifiers.md
│   │   ├── 10_Reputation_Rules.md
│   │   ├── 11_Signet_System.md
│   │   ├── 12_Auction_House.md
│   │   ├── 14_Resource_Cycle.md
│   │   ├── 15_P2P_Interaction.md
│   │   ├── 16_Global_Market_Logic.md
│   │   ├── 17_Loot_Distribution.md
│   │   └── 18_Loot_Sync_Cycle.md
│   │
│   ├── 04_Inventory_Gear/    # Инвентарь
│   │   ├── 01_Grid_Architecture.md
│   │   ├── 02_Containers_Slots.md
│   │   ├── 03_Physical_Weight.md
│   │   ├── 04_Resonance_Value.md
│   │   ├── 05_Inventory_QoL.md
│   │   ├── 06_Equipment_PaperDoll.md
│   │   ├── 07_Item_Attributes_UI.md
│   │   ├── 08_Looting_Process.md
│   │   └── 09_Stash_Architecture.md
│   │
│   └── 05_World_Systems/     # Системы мира
│       ├── 01_Hub/
│       │   ├── 00_Hub_Environment.md
│       │   ├── 01_Hub_Map_Table.md
│       │   ├── 02_Hub_Services_Interaction.md
│       │   ├── 03_Hub_Map_Interaction.md
│       │   ├── 04_Time_Atmosphere.md
│       │   └── 05_Party_Syndicate.md
│       ├── 02_Generation/
│       │   ├── 01_World_Concept_Palimpsest.md
│       │   ├── 02_Mechanic_Night_Benches.md
│       │   ├── 03_Dynamic_Weather.md
│       │   ├── 04_Global_Map_Rotation.md
│       │   ├── 05_Difficulty_Slots.md
│       │   ├── 06_Async_Timers.md
│       │   ├── 07_Server_Lifecycle.md
│       │   ├── 08_Gate_Check.md
│       │   ├── 09_Loot_Respawn.md
│       │   ├── 10_World_Topology.md
│       │   ├── 11_Socket_System.md
│       │   ├── 12_Generation_Strategies.md
│       │   ├── 13_Async_Double_Buffer.md
│       │   ├── 14_Sector_Content_Rules.md
│       │   ├── 15_Traversal_Shortcuts.md
│       │   ├── 16_UI_Map_Protocol.md
│       │   ├── 17_Dual_State_POIs.md
│       │   └── 18_POI_Metadata_Registry.md
│       ├── 03_Anomaly/
│       │   ├── 00_Anomaly_Core_Loop.md
│       │   ├── 05_Hazards_Traps.md
│       │   ├── 13_Insertion_Logic.md
│       │   ├── 14_Extraction_System.md
│       │   ├── 15_Frequency_Tuner.md
│       │   └── Anomaly_System.md
│       └── 04_Global_Rules/
│           ├── 01_Quest_Engine.md
│           ├── 02_Communication_Vox.md
│           ├── 03_Persistence_Ledger.md
│           └── 04_Reality_Integrity.md
│
├── 20_Lore/                  # [НАРРАТИВ]
│   ├── 01_World_Foundation/
│   │   ├── Anomaly_Weather_Systems.md
│   │   ├── Energy_Concept.md
│   │   ├── Magipunk_Physics.md
│   │   ├── The_Anchor.md
│   │   ├── The_Collapse.md
│   │   ├── The_Entity.md
│   │   └── The_Entropy.md
│   ├── 02_Societies_Factions/
│   │   ├── Factions_Active/
│   │   │   ├── New_Factions.md
│   │   │   ├── The_Cartographers.md
│   │   │   └── The_Minstrels.md
│   │   ├── Guild_Roles_Concept.md
│   │   ├── Social_Political_Order.md
│   │   ├── The_Cathedral.md
│   │   └── The_Keepers.md
│   ├── 03_Districts_Geography/
│   │   └── Safe_Zone/
│   │       └── City_Center.md
│   ├── 04_Species_Cultures/
│   │   ├── Races/
│   │   │   └── New_Races.md
│   │   ├── Culture_Language.md
│   │   └── Protocol_Resonance.md
│   └── 05_Daily_Life/
│       ├── Currency_Rezs.md
│       └── Fashion_Gear.md
│
└── 30_Content/               # [КОНТЕНТ]
    └── World_Atlas/
        └── Sectors/
            └── Port/
                ├── 00_Port_Manifest.md
                └── Tables/
                    ├── 01_Difficulty.md
                    ├── 02_Difficulty.md
                    └── 03_Difficulty.md
