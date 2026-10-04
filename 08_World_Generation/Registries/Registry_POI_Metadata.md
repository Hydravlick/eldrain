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

### Авторские данные обитаемой встречи

Когда выбран обитаемый POI, metadata связывает его с content definition: роль и цель местного, физическая зависимость от места, условия помощи/отказа, отдельное Routine/Urgent событие при наличии и заданная Stable-форма. Именованное продолжение явно указывает личный либо общий narrative scope по [[08_World_Generation/Generation/Location_Revision_Lifecycle#Общий район и личный финал|Location Revision Lifecycle]]. Metadata не создаёт личность, custody, Origin или общий NPC outcome.

Общая `projection_role` может сохранить карантин или закрытое состояние опасного корпуса. Обитаемая карточка показывает продолжающуюся жизнь местных без их добавления в ростер. Потеря доступа при замещении объясняется отдельно от смерти владельца. Поля локальной сессии не определяют общую форму. Для [[08_World_Generation/Content/World_Atlas/Sectors/Port/Accreting_Tissue_Clinic_Pilot|concept лечебного пилота]] исходная авторская форма — quarantine, при отсутствии допустимого пути — closed; действующий сервис и адрес ещё не заданы.

## 3. Resolver

В [[08_World_Generation/Content/World_Atlas/Sectors/Lens/Lens_Manifest#Возвращение и городское соседство|concept Линз]] белый двор имеет ограниченную `closed`-проекцию с видимой причиной закрытия печного проёма. Это authored общий вариант, не экспорт частной закупки или гибели голема из SessionRuntime. Реальных prefab/address definitions и допуска в selection пока нет; изображение места не создаёт активный сервис.

См. [[08_World_Generation/Generation/Dual_State_POIs#4. Resolver]].

## 4. Проверки

- отсутствующий ассет не создаёт пин;
- пустые семейства делают адрес невалидным и показывают диагностическое закрытое состояние;
- внешний пин не получает `permanent`;
- короткая продолжительность и ночное расписание не являются допустимыми полями MVP;
- raid loot profile не копируется в stable assortment;
- закрытый маршрут объясняет недоступность, а не молча удаляет знакомый адрес.
