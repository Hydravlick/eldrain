---
type: tech_spec
status: active
system: generation
tags: [metadata, prefabs, address_pins]
related_files:
  - "[[08_World_Generation/_Registries/Registry_POIs|Registry_POIs]]"
  - "[[08_World_Generation/Generation/17_Dual_State_POIs|Dual_State_POIs]]"
  - "[[08_World_Generation/Hub/01_Hub_Map_Table|Hub_Map_Table]]"
---
# Метаданные POI для Рейда и Мирной Проекции

## 1. Ответственность

Этот документ задаёт технический контракт префаба. Конкретные POI и стабильные ID живут в [[08_World_Generation/_Registries/Registry_POIs|Registry_POIs]], правила адресного бартера — в [[06_Economy_Loot/Barter_System|Barter_System]], а карта только отображает результат resolver.

## 2. Обязательные группы полей

```text
WorldMetadata
  prefab_id
  world_position
  raid_state
  stable_projection
  discovery
```

### `raid_state`

- иконка или силуэт;
- профиль источников, а не гарантированный предмет;
- допустимые Tier-состояния;
- тип опасной операции POI, если она существует.
- `heat_state`: `cold | warm | hot` для текущего рейдового инстанса;
- `heat_signal`: физический или поведенческий признак Heat;
- `heat_work`: контракт, способ, Embedded-узел, спасение, ключ маршрута или иной предмет работы;
- `approach_contract`: повторяемые записи `approach_id | entry_anchor | route_layer | world_cue | approach_cost | refusal_path`. `entry_anchor` и `route_layer` обязаны отличать реальные пространственные входы, а не две цены у одной двери.

### `stable_projection`

- `projection_role`: `address | civic_legacy | quarantine | closed`;
- `address_id` для внешнего сервиса;
- принимаемые семейства;
- роли результата;
- требования к уцелевшему ассету и маршруту;
- central fallback;
- доступность `stable_cycle`, без короткого таймера.

## 3. Пример

```json
{
  "prefab_id": "HERBALIST_SHOP_04",
  "world_position": {"x": 1450, "y": 320},
  "raid_state": {
    "map_token": "icon_herbalist_silhouette",
    "source_tags": ["organic", "filter_medium"],
    "tier_states": ["T1", "T2", "T3"],
    "field_operation_id": null,
    "heat_state": "warm",
    "heat_signal": "вентиляция работает рывками, а свет в стекле идёт против дождя",
    "heat_work": "sanitation_contract",
    "approach_contract": [
      {"approach_id": "service_door", "entry_anchor": "canal_service_door", "route_layer": "wet_low", "world_cue": "запах пара у служебной двери", "approach_cost": "шумный короткий вход", "refusal_path": "вернуться во двор"},
      {"approach_id": "roof_pipe", "entry_anchor": "roof_condensate_pipe", "route_layer": "dry_crown", "world_cue": "след конденсата на внешней трубе", "approach_cost": "вертикаль и стамина", "refusal_path": "остаться на крыше"}
    ]
  },
  "stable_projection": {
    "projection_role": "address",
    "address_id": "stable_herbalist_service",
    "accepted_families": ["organic", "filter_medium"],
    "service_roles": ["sidegrade", "sanitation"],
    "requires_asset_state": "serviceable",
    "requires_route_state": "confirmed_delivery",
    "central_fallback_id": "central_medical_service",
    "availability": "stable_cycle"
  },
  "discovery": {
    "poi_type_persists": true,
    "current_instance_persists": false
  }
}
```

## 4. Resolver

```text
if asset is absent:
  no projection pin
else if projection_role == address
     and asset_state is serviceable
     and route_state is confirmed:
  publish stable_external address pin
else:
  publish declared closed / quarantine / civic state
```

Metadata не содержит торговый коэффициент, глобальный бонус дохода или случайный ассортимент. `recipe_ids` разрешаются адресным слоем из канонического реестра сделок.

`heat_state` не переносится в Stable-проекцию как бонус торговли. У Hot POI обязательны минимум две записи `approach_contract` с различными `approach_id` и `entry_anchor`, разными `route_layer` либо доказанно разными пространственными связями, и один читаемый `refusal_path`; отсутствие любого поля делает рейдовую процедуру недоступной, а не молча безопасной.

## 5. Проверки

- отсутствующий ассет не создаёт пин;
- пустые семейства делают адрес невалидным и показывают диагностическое закрытое состояние;
- внешний пин не получает `permanent`;
- короткая продолжительность и ночное расписание не являются допустимыми полями MVP;
- raid loot profile не копируется в stable assortment;
- закрытый маршрут объясняет недоступность, а не молча удаляет знакомый адрес.
