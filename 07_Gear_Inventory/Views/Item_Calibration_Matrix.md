---
type: view
status: active
system: gear_balance
view_kind: item_calibration
upstream_sources:
  - "[[07_Gear_Inventory/Calibration_Contract]]"
  - "[[07_Gear_Inventory/Registries/Registry_Items]]"
  - "[[07_Gear_Inventory/Registries/Registry_Thermoses]]"
  - "[[07_Gear_Inventory/Registries/Registry_Thermos_Modules]]"
  - "[[05_Combat_Survival/Registries/Registry_Weapons]]"
  - "[[07_Gear_Inventory/Registries/Registry_Consumables]]"
  - "[[07_Gear_Inventory/Registries/Registry_Headwear]]"
---

# Калибровка: источники и пробелы

Производная карта готовности предметных источников. Состав тестовых комплектов, поля отчёта и критерии проверки принадлежат [[07_Gear_Inventory/Calibration_Contract]]. Значения читаются по ссылкам ниже: копия стартового набора здесь не хранится. `UNKNOWN` и `blocked_calibration` не означают нулевую цену или нулевой вклад.

```dataview
TABLE WITHOUT ID file.link AS "Источник", registry_type AS "Семейство", status AS "Канон"
WHERE type = "registry" AND (registry_type = "thermos_models" OR registry_type = "thermos_modules" OR registry_type = "weapon_frames" OR registry_type = "items" OR registry_type = "necessary_consumables" OR registry_type = "headwear")
```

[[07_Gear_Inventory/Registries/Registry_Headwear]]; [[07_Gear_Inventory/Registries/Registry_Items]]; [[07_Gear_Inventory/Registries/Registry_Consumables]].
