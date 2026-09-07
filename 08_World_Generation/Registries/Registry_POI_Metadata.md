---
status: active
system: generation
tags:
  - metadata
  - prefabs
  - address_pins
related_files:
  - "[[08_World_Generation/Generation/Location_Revision_Lifecycle|Location_Revision_Lifecycle]]"
  - "[[08_World_Generation/Registries/Registry_POIs|Registry_POIs]]"
  - "[[08_World_Generation/Generation/Dual_State_POIs|Dual_State_POIs]]"
  - "[[08_World_Generation/Hub/Hub_Map_Table|Hub_Map_Table]]"
type: registry
index_route: owner
index_group: world_generation
index_order: 200
index_summary: "Хранит схему и записи: Метаданные POI для Рейда и Мирной Проекции."
read_when: Когда нужен контракт «Метаданные POI для Рейда и Мирной Проекции» и его границы с соседними владельцами.
---
# Метаданные POI для Рейда и Мирной Проекции

## 1. Ответственность

Этот документ задаёт технический контракт префаба. Конкретные POI и стабильные ID живут в [[08_World_Generation/Registries/Registry_POIs|Registry_POIs]], правила адресного бартера — в [[06_Economy_Loot/Barter_System|Barter_System]], а карта только отображает результат resolver.

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
- `stable_eligibility`: допустимость участия в `StablePOISelection`; она не выбирает слот и не зависит от локальной рейдовой сессии.

## 3. Resolver

См. [[08_World_Generation/Generation/Dual_State_POIs#4. Resolver]].

## 4. Проверки

- отсутствующий ассет не создаёт пин;
- пустые семейства делают адрес невалидным и показывают диагностическое закрытое состояние;
- внешний пин не получает `permanent`;
- короткая продолжительность и ночное расписание не являются допустимыми полями MVP;
- raid loot profile не копируется в stable assortment;
- закрытый маршрут объясняет недоступность, а не молча удаляет знакомый адрес.
