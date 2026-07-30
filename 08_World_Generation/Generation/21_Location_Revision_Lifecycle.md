---
type: system_contract
status: active
index_route: owner
index_group: world_generation
index_order: 175
index_summary: "Задаёт общую прегенерацию локации, Stable-постгенерацию и публикацию WorldRevision."
read_when: "Читайте при изменении общей геометрии локации, экземпляров рейда, Stable-проекции или выбора внешних POI."
system: location_revision_lifecycle
tags: [location_revision, session_runtime, stable_projection, stable_poi_selection, world_revision]
related_files:
  - "[[08_World_Generation/Generation/04_Global_Map_Rotation|Global_Map_Rotation]]"
  - "[[08_World_Generation/Generation/07_Server_Lifecycle|Server_Lifecycle]]"
  - "[[08_World_Generation/Generation/17_Dual_State_POIs|Dual_State_POIs]]"
  - "[[08_World_Generation/Generation/18_POI_Metadata_Registry|POI_Metadata]]"
  - "[[08_World_Generation/City_State/Civic_Event_Lifecycle|Civic_Event_Lifecycle]]"
  - "[[08_World_Generation/Hub/01_Hub_Map_Table|Hub_Map_Table]]"
  - "[[08_World_Generation/_Registries/Registry_POIs|Registry_POIs]]"
---
# Жизненный цикл ревизии локации

## 1. Обещание

Игрок изучает общую локацию, а не удачную версию чужого рейда. Все рейдовые сессии начинают на одинаковых зданиях, маршрутах и базовых POI; после Stable город показывает общую low-poly проекцию этой же локации и выбирает из реально присутствующих функций только ограниченный набор адресов.

## 2. Четыре разных состояния

```text
LocationRevision
  -> many SessionRuntime instances
  -> StableProjection + StablePOISelection
  -> published WorldRevision
```

### `LocationRevision`

Одна общая прегенерированная конфигурация на общий цикл локации. Она неизменяема после публикации и содержит:

```text
location_revision_id
common_cycle_id
source_generation
seed
placed_assets[]
geometry_ref
route_links[]
poi_candidates[]
asset_tags[]
```

Она определяет, какие здания, маршруты, POI-кандидаты и теги существуют для всех рейдов. Она не хранит открытые двери, смерти врагов, оставленные предметы или знание аккаунта.

### `SessionRuntime`

Отдельный живой экземпляр рейда, читающий ровно одну `location_revision_id`:

```text
session_id
location_revision_id
phase_revision
door_states[]
enemy_states[]
ground_items[]
player_actions[]
presence_outcomes[]
```

Эти поля принадлежат `SessionID`. Они не создают вторую геометрию, не меняют `LocationRevision` и не становятся входом в Stable-постгенерацию. Из рейда наружу уходят только личные extraction/contract/evidence результаты по своим владельцам.

### `StableProjection` и `StablePOISelection`

После общего Stable-барьера постгенератор читает исходную `LocationRevision`, а не одну выбранную сессию и не агрегат её разрушений.

```text
StableProjection
  source_location_revision_id
  low_poly_assets[]
  low_poly_routes[]

StablePOISelection
  source_location_revision_id
  eligible_poi_candidates[]
  selected_address_pins[]: exactly N authored slots
  available_poi_types[]
  authored_city_constraints[]
  absence_history_inputs[]
  rejected_local_mutations[]
```

`eligible_poi_candidates[]` составляют только реально присутствующие ассеты с допустимыми metadata. `N`, базовые веса, допустимые конкуренции и обязательные сервисные границы — authored-ограничения, а не скрытая случайность. Для выбора адресов тип, который давно не был активен, получает повышенный вес; это не отменяет требования к ассету и не делает невыбранный адрес сломанным. Невыбранный объект остаётся видимой частью low-poly диорамы, но не получает активный сервисный пин.

Для каждого eligible-кандидата publisher фиксирует объяснимый `selection_reason`: `base_weight`, применённый `absence_history` и авторское ограничение, которое пропустило либо отклонило кандидат. Точные числа и длина истории — эмпирический прототипный вопрос; сам порядок причин не скрыт и не зависит от того, что произошло в одной сессии.

`rejected_local_mutations[]` явно исключает состояние дверей, врагов, предметов, урон окружению и действия игроков из построения проекции и выбора пинов. `eligible_session_facts[]` для геометрии и адресов пуст: проверяемые результаты рейда идут только в extraction, контракт или `ContributionReceipt`, а не в постгенератор карты.

### `WorldRevision`

```text
world_revision_id
regional_shard_id
published_against_city_revision
location_bundles[]
  location_revision_ref
  stable_projection_ref
  stable_poi_selection_ref
  available_poi_types[]
```

`WorldRevision` — опубликованный общий набор, а не снимок конкретного `SessionID`. Он может включать несколько `LocationRevision`, но каждый конкретный рейд читает ровно одну из них. `available_poi_types[]` означает типы, доступные в этой общей ревизии; `discovered_poi_types[]` принадлежит только аккаунту.

## 3. Единственный publisher

`WORLD_REVISION_PUBLISHER` владеет прегенерацией `LocationRevision`, построением `WorldRevisionCandidate`, Stable-постгенерацией и публикацией `WorldRevision`.

```text
author generation inputs
  -> LocationRevision
  -> all SessionID clone its base
  -> common Stable barrier
  -> WorldRevisionCandidate
  -> publisher validation
  -> WorldRevision
```

```text
WorldRevisionCandidate
  source_generation: location_revision_id
  eligible_session_facts[]: none for topology or POI selection
  authored_city_constraints[]
  preserved_assets[]
  rejected_local_mutations[]
  publication_reason: initial_generation | stable_post_generation
```

Publisher проверяет, что каждый выбранный адрес существует в `LocationRevision`, проходит metadata и не превышает authored `N`. Он не выбирает репрезентативную сессию, не суммирует локальные разрушения и не меняет личные результаты игроков.

`CIVIC_EVENT_LIFECYCLE` остаётся владельцем `CityState`, `CityRevision`, городских явлений и общего торгового каталога. Он читает опубликованную `WorldRevision` как общий контекст и не создаёт её содержимое. Оба сервиса синхронизируются по `published_against_city_revision`, но не владеют полями друг друга.

## 4. Границы

- `SERVER_LIFECYCLE` владеет временем и runtime отдельной сессии, но не `LocationRevision`, `StableProjection`, выбором адресов или публикацией мира.
- `CIVIC_EVENT_LIFECYCLE` не выбирает ассеты, веса адресов или геометрию.
- Hub Map отображает `WorldRevision`, но не собирает её и не вычисляет веса.
- POI metadata описывает допустимость кандидата; она не выбирает `N` и не создаёт пин сама.
- Аккаунт хранит `discovered_poi_types[]`, принятые контракты, награду и социальный след. Ни одно из этих полей не записывается в `WorldRevision`.
