---
type: tech_spec
status: active
system: ui_hud
tags: [minimap, json, data_stream]
---
# Протокол Данных Мини-карты

## 1. Проблема Динамики
Поскольку карта генерируется процедурно, статические текстуры (PNG) невозможны. UI должен рисовать карту "на лету" по вектору.

## 2. JSON-Структура (Server to Client)
Генератор отдает пакет данных при входе в сектор:

```json
{
  "sector_guid": "SEC-77-ALPHA",
  "sector_phase": "ANOMALY",
  "current_tier": "T2",
  "time_to_phase_shift_sec": 312,
  "time_to_collapse_sec": 7512,
  "fog_of_war_reset": false, // Нужно ли стереть открытую карту игрока
  "map_objects": [
    {
      "id": 1045,
      "position": {"x": 120, "y": -45}, // Вектор вместо гекса
      "type": "BUILDING",
      "tags": ["HEIGHT_HIGH", "BRIDGE_NORTH"], // UI рисует иконку мостика
      "poi_icon": "ICON_TRADER_CELLS",
      "poi_state": "ANOMALY",
      "poi_tier_variant": "T2",
      "visibility_layer": "DIEGETIC"
    },
    {
      "id": 1046,
      "type": "OBSTACLE_RUBBLE", // Гора мусора (непроходимая зона)
      "shape": "CIRCLE",
      "radius": 15
    },
    {
      "id": 1099,
      "type": "SHELTER",
      "status": "LOCKED" // UI рисует замок
    }
  ]
}
```

## 3. Слои Видимости
Чтобы карта и HUD не превратились в таблицу из 13 переменных, каждый параметр получает слой:

| Layer | Что показывает | Пример |
|:---|:---|:---|
| **VISIBLE** | критичные числа, нужные каждую секунду | HP, stamina, заряды активной батареи, таймер Gate Check |
| **DIEGETIC** | читается через мир и приборы | треск фильтра, гул перегрева, цвет тумана, маркеры карты |
| **LATENT** | скрыто до наведения, сканера или Mission Readiness | точный ResonanceLoad, SurvivalScore, шанс охоты, Tier-вариант POI |

Mission Readiness показывает Latent-данные до входа. В рейде HUD держит только VISIBLE, а остальное отдает через звук, маску, карту и короткие предупреждения.
