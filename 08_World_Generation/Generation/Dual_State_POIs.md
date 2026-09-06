---
status: active
system: world_simulation
tags:
  - poi
  - dual_state
  - persistence
  - address_pins
related_files:
  - "[[08_World_Generation/Generation/Location_Revision_Lifecycle|Location_Revision_Lifecycle]]"
  - "[[08_World_Generation/Generation/Server_Lifecycle|Server_Lifecycle]]"
  - "[[08_World_Generation/Registries/Registry_POI_Metadata|POI_Metadata]]"
  - "[[08_World_Generation/Hub/Hub_Map_Table|Hub_Map_Table]]"
  - "[[06_Economy_Loot/Extraction_Stabilization_Loop|Extraction_Stabilization_Loop]]"
type: system
index_route: owner
index_group: world_generation
index_order: 200
index_summary: "Определяет состояния, разрешение и связи: Двойное Состояние POI."
read_when: Когда нужен контракт «Двойное Состояние POI» и его границы с соседними владельцами.
---
# Двойное Состояние POI

## 1. Обещание

Место, через которое игрок рисковал в Аномалии, может вернуться на Стол как узнаваемая мирная функция — но только если общий `LocationRevision` действительно содержит его ассет, маршрут и допустимую службу.

## 2. Рабочий цикл

```text
LocationRevision POI candidate
  -> many local Raid POI runtimes
  -> common Stable post-generation
  -> StableProjection + StablePOISelection
  -> service / obligation / quarantine / closed trace
```

В Аномалии игрок посещает POI физически. В Stable-состоянии он взаимодействует только с пином и диорамой Живой Миниатюры.

## 3. Правила состояний

| Состояние | Роль POI | Физическое взаимодействие | Представление на Столе |
|:---|:---|:---|:---|
| **Active T1–T3** | локальная runtime-версия POI: лут, маршрут, угроза, встроенный узел, Ночной Верстак | обыск, бой, опасная authored-процедура | разведданные и Mission Readiness |
| **Stable** | общая проекция POI: выбранный внешний адрес, общественное наследие, контракт, карантин или закрытая руина | свободный вход отсутствует | пин-лепесток или объяснённое закрытое состояние |
| **Replacement** | конфигурация замещается новым циклом | нет | старый лепесток исчезает без расхода preview |

Tier внутри Active-состояния меняет комнаты, маршруты, опасность, `heat_state` и доступ к источникам. T1 учит читать опасный слепок в доступной экосреде; T2 делает среду, существ, игроков и маршруты совместной угрозой; T3 проверяет полный набор подготовленных механик и лучших билдов. Stable-сервис не является четвёртым Tier награды.

## 4. Условия внешнего адреса

POI создаёт `stable_external` пин, только если:

1. его ассет присутствует в `LocationRevision` опубликованной `WorldRevision`;
2. metadata допускает мирную сервисную функцию;
3. postgenerator подтвердил маршрут или доставку к центральному ядру;
4. `StablePOISelection` выбрал его в один из authored `N` адресных слотов;
5. metadata указывает `address_id`, семейства и роль результата.

Иначе POI становится закрытой диорамой, контрактом восстановления, карантином или просто частью пейзажа.

### Пример: лавка травника

- **Raid:** разграбленное здание даёт профильные источники и маршрутный риск.
- **Stable:** присутствующая в общей ревизии сушильня и подтверждённый путь становятся кандидатом; адрес появляется, только если его выбрал общий `StablePOISelection`.
- **Результат:** мастер предлагает конкретный sidegrade или санитарную услугу; он не продаёт «лучшие зелья» из абстрактного процента целостности.
- **Следующий цикл:** адрес исчезает при замещении, но тип POI остаётся изученным.

## 5. Сохранение контекста

- оставленный переносимый лут не появляется на полках Stable-сервиса;
- массовые материалы могут стать общественным запасом, но не личным инвентарём;
- встроенная реликвия остаётся POI и требует отдельной опасной процедуры;
- authored состояние ассета, карантин и маршрутные ограничения меняют тип доступного пина, а не только цену;
- полезная инфраструктура может принести обязательство или карантин вместо торговли.

## 6. Исключения и риски

- внешний адрес живёт весь Stable-цикл, без почасового FOMO;
- временность не даёт автоматический бонус курса;
- один POI не публикует все семейства материалов;
- Stable-проекция не обещает прогулочный Хаб;
- Ночной Верстак в Active-состоянии не превращается автоматически в обычную Stable-мастерскую: для мирного адреса нужна отдельная metadata-функция уцелевшего POI.

## 7. Схема перехода

```text
resolveStablePOI(location_asset, routes, metadata, stable_selection)
  -> stable_external_address
  | civic_legacy
  | quarantine_or_contract
  | closed_projection
```

## 4. Resolver

```text
if asset is absent from LocationRevision:
  no projection pin
else if projection_role == address
     and route_state is confirmed:
  submit eligible candidate to StablePOISelection
else:
  publish declared closed / quarantine / civic state
```

Только `StablePOISelection` выбирает `N` активных адресов из eligible-кандидатов. Не выбранный кандидат остаётся диорамой без активного пина; локальное `SessionRuntime` не является входом resolver.

Metadata не содержит торговый коэффициент, глобальный бонус дохода или случайный ассортимент. `recipe_ids` разрешаются адресным слоем из канонического реестра сделок.

`heat_state` не переносится в Stable-проекцию как бонус торговли. У Hot POI обязательны минимум две записи `approach_contract` с различными `approach_id` и `entry_anchor`, разными `route_layer` либо доказанно разными пространственными связями, и один читаемый `refusal_path`; отсутствие любого поля делает рейдовую процедуру недоступной, а не молча безопасной.
