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
  "time_to_seal_sec": 3912,
  "time_to_dawn_sec": 7512,
  "approach_summary": "PREPARED",
  "entry_quote_summary": {
    "status": "CONFIRMED",
    "shown_phase": "T2",
    "entry_window": "OPEN",
    "environment_forecast": "RISK"
  },
  "environment_forecast": "RISK",
  "dissonance_state": "YELLOW",
  "entry_state": "OPEN",
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
| **VISIBLE** | критичные числа, нужные каждую секунду | HP, stamina, Weapon/Casting ImpulseReserve, выбранный источник Q/E, прогноз цены кантрипа при модификаторе, таймер Gate Check |
| **DIEGETIC** | читается через мир и приборы | треск фильтра, гул перегрева, цвет тумана, маркеры карты |
| **LATENT** | скрыто до наведения, сканера или готовности к рейду | точный DissonanceLoad, SurvivalScore, внутренняя доступность входа, шанс охоты, Tier-вариант POI |

До входа карта показывает готовность, прогноз и понятную карточку подхода/ставки. В рейде HUD держит только VISIBLE, а остальное отдаёт через звук, маску, карту и короткие предупреждения. Он не раскрывает технические очереди, резервации или внутренние идентификаторы входа.
