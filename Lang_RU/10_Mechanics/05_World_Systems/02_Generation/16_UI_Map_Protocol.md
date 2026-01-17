---
type: tech_spec
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
  "fog_of_war_reset": false, // Нужно ли стереть открытую карту игрока
  "map_objects": [
    {
      "id": 1045,
      "position": {"x": 120, "y": -45}, // Вектор вместо гекса
      "type": "BUILDING",
      "tags": ["HEIGHT_HIGH", "BRIDGE_NORTH"], // UI рисует иконку мостика
      "poi_icon": "ICON_TRADER_AMMO"
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