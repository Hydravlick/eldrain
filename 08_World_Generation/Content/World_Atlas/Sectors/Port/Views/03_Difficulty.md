---
type: view
status: active
system: world_atlas
view_kind: sector_difficulty
difficulty: 3
biome_id: port
sector_ref: "[[08_World_Generation/Content/World_Atlas/Sectors/Port/Port_Manifest]]"
upstream_sources:
  - "[[08_World_Generation/Registries/Registry_Biomes]]"
  - "[[08_World_Generation/Registries/Registry_Mobs]]"
  - "[[07_Gear_Inventory/Registries/Registry_Items]]"
  - "[[07_Gear_Inventory/Registries/Registry_Thermos_Modules]]"
  - "[[07_Gear_Inventory/Registries/Registry_Headwear]]"
  - "[[07_Gear_Inventory/Registries/Registry_Consumables]]"
  - "[[07_Gear_Inventory/Registries/Registry_Blueprints]]"
  - "[[05_Combat_Survival/Registries/Registry_Weapons]]"
  - "[[08_World_Generation/Content/World_Atlas/Sectors/Port/Port_Manifest]]"
items_ref: "[[07_Gear_Inventory/Registries/Registry_Items]]"
modules_ref: "[[07_Gear_Inventory/Registries/Registry_Thermos_Modules]]"
headwear_ref: "[[07_Gear_Inventory/Registries/Registry_Headwear]]"
consumables_ref: "[[07_Gear_Inventory/Registries/Registry_Consumables]]"
blueprints_ref: "[[07_Gear_Inventory/Registries/Registry_Blueprints]]"
biomes_ref: "[[08_World_Generation/Registries/Registry_Biomes]]"
mobs_ref: "[[08_World_Generation/Registries/Registry_Mobs]]"
---

# Ржавый Порт: сложность 3

Производная таблица среды, встреч и связанной добычи. Канон читается из `upstream_sources`; таблица не определяет состав рейда и не гарантирует выпадение предмета. Номер сложности задан в properties.

```dataviewjs
await dv.view("tools/dataview/sector_difficulty", dv.current());
```
