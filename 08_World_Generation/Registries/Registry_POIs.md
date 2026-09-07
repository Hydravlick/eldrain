---
status: active
system: world_generation_registry
registry_type: map_objects
tags:
  - ui_map
  - prefabs
  - pois
  - dungeons
related_systems:
  - "[[08_World_Generation/Anomaly/Anomaly_System|Anomaly_System]]"
  - "[[08_World_Generation/City_State/Civic_Event_Lifecycle|Civic_Event_Lifecycle]]"
  - "[[08_World_Generation/Generation/Location_Revision_Lifecycle|Location_Revision_Lifecycle]]"
  - "[[08_World_Generation/Generation/Generation_Strategies|Generation_Strategies]]"
  - "[[08_World_Generation/Hub/Hub_Map_Table|Hub_Map_Table]]"
type: registry
index_route: owner
index_group: world_generation
index_order: 50
index_summary: "Хранит схему и записи: Реестр: Объекты Карты (Map Table Objects)."
read_when: "Когда нужен контракт «Реестр: Объекты Карты (Map Table Objects)» и его границы с соседними владельцами."
---
# Реестр объектов карты

Реестр хранит стабильные ID подтверждённых POI и минимальные данные, которыми пользуются карта, адреса и генерация. Представление фаз, выбор цели и переход к подготовке принадлежат [[08_World_Generation/Hub/Hub_Map_Table]] и [[08_World_Generation/Generation/Raid_Approach_and_Entry]]. Тут не разрешаются очереди, награды, боевые волны, tutorial lifecycle или account progression.

## Active contract

### Адресный POI

Реестр хранит стабильные ID и структурированные поля. Универсальные правила принадлежат [[06_Economy_Loot/Barter_System|адресному бартеру]], а технический префабный контракт — [[08_World_Generation/Registries/Registry_POI_Metadata|метаданным POI]].

```text
poi_id
address_id: stable key for address pins | none
address_class: central | stable_external | none
availability: permanent | stable_cycle | raid_only
accepted_families
service_roles
central_fallback
```

`stable_external` не означает «лучше центра». Он обозначает услугу, существующую благодаря текущей Stable-конфигурации сектора.

### Общий POI и отношение аккаунта

Состояние и разграничение общей ревизии и знания аккаунта: [[08_World_Generation/Generation/Location_Revision_Lifecycle#Общий POI и отношение аккаунта]].

### Рейдовый Реквием

Поля наложения исполняются по [[08_World_Generation/Anomaly/Anomaly_System#Рейдовый Реквием]].

```text
poi_role: requiem_overlay
availability: raid_only
constant_ref: canonical Constantine record
relic_trace_family_ref: canonical Constantine trace family
manifestation_anchor: existing POI element
manifestation_form: creature | object | route | scene | localized_weather
manifestation_extent: bounded POI subspace
entry_tell: observable boundary signal
exit_condition: declared completion or withdrawal condition
refusal_path: visible bypass or cost
precedent: short disputed civic rule
human_cost: whom the rule protects, burdens, or excludes
counterplay: readable response to the rule
evidence_payload: extractable proof | none
```

Смысл полей и обязательные сигналы: [[08_World_Generation/Anomaly/Anomaly_System#Рейдовый Реквием]].

## Confirmed records

### Общие Кладовые

[poi_id:: central_common_stores]
[address_id:: central_common_stores]
[address_class:: central]
[availability:: permanent]
[accepted_families:: fastener|cloth|filter_medium|battery_shell|rez]
[service_roles:: minimum|basic_filter|basic_battery|ration]
[central_fallback:: none]

Постоянный адрес городского минимума, подтверждённый [[03_Factions_Societies/Lore/The_Common_Storehouses|Общими Кладовыми]] и [[06_Economy_Loot/Vendor_Logic|контрактом адресов]]. Не принимает весь `junk` в универсальную топку и не производит редкие результаты.

### Центральный Ремонт
[poi_id:: central_repair_service]
[address_id:: central_repair_service]
[address_class:: central]
[availability:: permanent]
[accepted_families:: fastener|cloth|sealant|conductor]
[service_roles:: repair|exact_dismantle]
[central_fallback:: none]

Постоянный базовый ремонт и точный разбор по [[06_Economy_Loot/Vendor_Logic|контракту адресов]]. Показывает результат до подтверждения; случайного редкого выхода нет.

### Центральная Медицинская Служба
[poi_id:: central_medical_service]
[address_id:: central_medical_service]
[address_class:: central]
[availability:: permanent]
[accepted_families:: organic|filter_medium|rez]
[service_roles:: treatment|sanitation]
[central_fallback:: none]

Сохраняет базовое лечение и санитарную обработку независимо от внешней ротации; роль подтверждена [[06_Economy_Loot/Vendor_Logic|контрактом адресов]] и практикой [[03_Factions_Societies/Lore/The_First_Reception|Первого Приёма]].

### Дверь

[poi_id:: port_door]
[address_id:: none]
[address_class:: none]
[availability:: permanent]
[map_token:: icon_portal_blue]
[height_tier:: 2]
[procedural_pool:: excluded]
[safe_frame:: handcrafted]

Сохранившийся приёмный узел Ковчега и древний причал. Дверь постоянна, не входит в процедурный пул Порта и отделена от рейдовой геометрии безопасным карманом. Канон места, его граница с генерацией и Отпечаток Перехода принадлежат [[08_World_Generation/Content/World_Atlas/Sectors/Port/Port_Manifest#Граница Двери|манифесту Порта]].

## Adding a record

```text
poi_id
address_id: stable key for address pins | none
address_class: central | stable_external | none
availability: permanent | stable_cycle | raid_only
accepted_families
service_roles
central_fallback
metadata_ref
content_owner_ref
```

Для рейдового POI добавляются только поля, реально потребляемые [[08_World_Generation/Registries/Registry_POI_Metadata|метаданными POI]] или профильным владельцем. Сюжетное описание, lifecycle взаимодействия, награды и боевые правила остаются у своих владельцев.
