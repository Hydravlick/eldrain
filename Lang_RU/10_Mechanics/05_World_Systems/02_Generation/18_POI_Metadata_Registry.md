---
type: tech_spec
system: generation
tags: [metadata, json, prefabs]
---

# Реестр Метаданных POI

## 1. Структура Данных Префаба
Любой процедурный объект (здание, вагончик, подвал) содержит компонент `WorldMetadata`. При генерации сектора эти данные собираются в единый манифест для UI.

## 2. JSON-Определение
Пример конфигурации для префаба `PREFAB_BUILDING_SMALL_04`:

```json
{
  "guid": "77-ALPHA-GEN-22",
  "world_position": {"x": 1450, "y": 320},
  
  // Визуальные теги для Мини-карты в рейде
  "raid_tags": {
    "icon": "ICON_HOUSE_LOOT",
    "danger_level": "TIER_2",
    "loot_table": "TABLE_HERBS_RARE"
  },

  // Данные для Стола Карты в Хабе
  "hub_service": {
    "enabled": true,
    "service_id": "VENDOR_NPC_HERBALIST", // Какой NPC тут живет
    "ui_label": "Аптека Старика",
    "trade_route_bonus": 1.5 // Бонус к доходу, если отправить сюда караван
  }
}