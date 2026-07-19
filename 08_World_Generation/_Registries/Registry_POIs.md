---
type: registry
status: active
system: world_generation_registry
registry_type: map_objects
tags: [ui_map, prefabs, pois, dungeons]
related_systems:
  - "[[08_World_Generation/Anomaly/Anomaly_System|Anomaly_System]]"
  - "[[08_World_Generation/Generation/12_Generation_Strategies|Generation_Strategies]]"
  - "[[08_World_Generation/Hub/01_Hub_Map_Table|Hub_Map_Table]]"
---
# Реестр: Объекты Карты (Map Table Objects)

> **Концепция Карты:** Диегетическая 3D-проекция города на столе.
> **Цикл Фаз (Sector Phases):**
> 1.  **Stable (Стабильность):** мирная проекция. Центральные службы остаются в ядре, а уцелевшие внешние POI становятся адресами-лепестками.
> 2.  **Evacuation (Эвакуация):** Блокировка всех активностей. Подготовка к смене.
> 3.  **Anomaly (Аномалия):** Рейд-зона. Покрыта "Туманом".
>     * **Вход:** Клик по Туману -> Открывает меню **"Mission Readiness"** (Выбор снаряжения, кнопка "Deploy").
>     * **Tier Layer:** внутри Аномалии POI получает вариант T1/T2/T3: состав мобов, опасность среды, лут и доступные комнаты меняются после Phase Shift.

---

## Контракт адресного POI

Реестр хранит стабильные ID и структурированные поля. Универсальные правила принадлежат [[06_Economy_Loot/Barter_System|адресному бартеру]], а технический префабный контракт — [[08_World_Generation/Generation/18_POI_Metadata_Registry|метаданным POI]].

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

# 0. Центральные Пины

### Общие Кладовые
[poi_id:: central_common_stores]
[address_id:: central_common_stores]
[address_class:: central]
[availability:: permanent]
[accepted_families:: fastener|cloth|filter_medium|battery_shell|rez]
[service_roles:: minimum|basic_filter|basic_battery|ration]
[central_fallback:: none]

Постоянный источник recovery-минимума. Не принимает весь `junk` в универсальную топку и не производит редкие результаты.

### Центральный Ремонт
[poi_id:: central_repair_service]
[address_id:: central_repair_service]
[address_class:: central]
[availability:: permanent]
[accepted_families:: fastener|cloth|sealant|conductor]
[service_roles:: repair|exact_dismantle]
[central_fallback:: none]

Показывает точный результат ремонта или разбора до подтверждения. Случайного редкого выхода нет.

### Центральная Медицинская Служба
[poi_id:: central_medical_service]
[address_id:: central_medical_service]
[address_class:: central]
[availability:: permanent]
[accepted_families:: organic|filter_medium|rez]
[service_roles:: treatment|sanitation]
[central_fallback:: none]

Сохраняет базовое лечение и санитарную обработку независимо от внешней ротации.

---

# 1. Категория: Городские Префабы (Civilian Infrastructure)
*Здания двойного назначения. В мирное время — сервис, в Аномалии — источник профильного лута.*

### [PREFAB:: CHEM_LAB_01] — "Аптекарь"
*Угловое здание с зеленой неоновой вывеской.*
[poi_id:: chem_lab_01]
[address_id:: stable_herbalist_service]
[address_class:: stable_external]
[availability:: stable_cycle]
[accepted_families:: organic|filter_medium]
[service_roles:: sanitation|sidegrade]
[central_fallback:: central_medical_service]
* **Map Token:** `icon_medical` (Зеленый крест).
* **Высота:** `Tier 1` (Скрыто туманом в фазе Аномалии).

#### Состояния Объекта:
| Фаза | Визуал на Карте | Взаимодействие (UI) | Геймплейная Роль |
| :--- | :--- | :--- | :--- |
| **Stable** | Внешний лепесток активен, если лаборатория и маршрут сохранились. | Открывает адресную карточку органики и фильтрующих сред. | **Сервис:** санитарная обработка и профильный sidegrade. |
| **Evac** | Маркер серый (Disabled). | "Закрыто. Эвакуация". | Недоступно. |
| **Anomaly** | Скрыто (или контур в тумане). | Показывает инфо: *"Loot: Chemistry / Meds"* | **Loot Spot:** Высокий шанс найти редкие медикаменты внутри рейда. |

### [PREFAB:: MECHANIC_HUB] — "Мастерская"
*Промышленный ангар.*
[poi_id:: mechanic_hub]
[address_id:: stable_mechanic_service]
[address_class:: stable_external]
[availability:: stable_cycle]
[accepted_families:: fastener|conductor|housing]
[service_roles:: repair_sidegrade|assembly]
[central_fallback:: central_repair_service]
* **Map Token:** `icon_craft` (Оранжевый ключ).
* **Высота:** `Tier 1` (Скрыто туманом).

#### Состояния Объекта:
| Фаза | Визуал на Карте | Взаимодействие (UI) | Геймплейная Роль |
| :--- | :--- | :--- | :--- |
| **Stable** | Внешний лепесток активен при уцелевшем оборудовании. | Открывает несколько конкретных RecipeTransaction. | **Сервис:** профильная сборка или ремонтный sidegrade, не общий крафт. |
| **Evac** | Маркер серый. | "Мастер ушел". | Недоступно. |
| **Anomaly** | Скрыто. | Показывает инфо: *"Loot: Scrap / Tech"* | **Loot Spot:** Источник металлолома и чертежей. |

### [PREFAB:: GUILD_HALL] — "Гильдейский Холл"
*Богато украшенное каменное здание.*
[poi_id:: guild_hall]
[address_id:: stable_guild_hall_service]
[address_class:: stable_external]
[availability:: stable_cycle]
[accepted_families:: proof|contract_cargo]
[service_roles:: obligation|route|recognition]
[central_fallback:: none]
* **Map Token:** `icon_flag` (Флаг фракции).
* **Высота:** `Tier 1`.

#### Состояния Объекта:
| Фаза | Визуал на Карте | Взаимодействие (UI) | Геймплейная Роль |
| :--- | :--- | :--- | :--- |
| **Stable** | Маркер активен. | Контракты и награды. | **Quest Hub:** Выдача заданий. |
| **Evac** | Маркер серый. | Блокировано. | Недоступно. |
| **Anomaly** | Скрыто. | Показывает инфо: *"Loot: Intel / Gold"* | **Stronghold:** Укрепленная точка с элитными врагами и сейфом фракции. |
## Ржавый Порт (Port Sector)

### [PREFAB:: PORT_DOOR] — "Дверь" (The Door)
*Сохранившийся приёмный узел Ковчега и древний причал. Отдельная ручная безопасная локация вне рейдовой геометрии.*
[poi_id:: port_door]
[address_id:: none]
[address_class:: none]
[availability:: permanent]
* **Map Token:** `icon_portal_blue` (Синяя Арка).
* **Высота:** `Tier 2` (Арка всегда светится сквозь любой туман).
* **Свойство:** `Handcrafted Safe Frame` (Статичный объект. Никогда не перемещается, не исчезает и не входит в процедурный пул Порта).

#### Канон Двери

Дверь существовала до Коллапса и не является слепком или творением Сущности. Изначально это была гавань прибытия для жителей миров, отобранных Предтечами.

После повреждения Ковчега Дверь:

- утратила способность выбирать миры и прокладывать осознанные маршруты;
- пассивно улавливает существ, уже потерявших связь со своей реальностью;
- доставляет их к причалу вместе с лодками, капсулами или обломками последнего пути;
- сохраняет небольшую область устойчивости даже во время Аномалии.

Физическая Дверь, причал и безопасный карман создаются вручную. Аномалия не проводит через них рейдовые угрозы. Процедурный Порт начинается за контролируемым порогом: генератор использует рейдовую сторону порога как один из корней улиц, но не изменяет саму Дверь.

Первый персонаж игрока прибывает через Дверь как один из таких потерявшихся жителей. Молодой Осколок проявляется внутри него, но Дверь не создаёт Осколок и не выбирает его.

В стартовой сцене Дверь выбрасывает к причалу небольшое судно или обломок лодки с первым персонажем. Поэтому игрок буквально приплывает в Порт, даже если вода за порогом не принадлежит никакому сохранившемуся морю.

#### Особая Механика: Отпечаток Перехода (Training Instance)

Первое прибытие происходит только один раз. Дверь сохраняет запись того, как Ковчег принял человека, и способна развернуть изолированный учебный отпечаток.

Это не путешествие назад, не копия личности и не воскрешение стартовой Пешки.

Префаб существует одновременно в двух слоях:
1.  **Safe Frame:** Физическая ручная локация на границе Порта.
2.  **Transition Imprint:** Изолированный инстанс записи перехода.
* **Функция:** В меню взаимодействия **ВСЕГДА** доступна кнопка `[Replay Tutorial]`. Игрок может в любой момент вернуться в "песочницу" для тестов механик.

#### Состояния Объекта (Always Active):
| Фаза    | Визуал на Карте | Взаимодействие (UI)    |
| :------ | :-------------- | :--------------------- |
| **Any** | Маркер Активен. | 1. **Replay Tutorial** |

### [PREFAB:: PORT_ARENA] — "Перекресток Судеб"
*Круглая площадка на сваях посреди воды, окруженная лодками-трибунами.*
[poi_id:: port_arena]
[address_id:: none]
[address_class:: none]
[availability:: stable_cycle]
* **Map Token:** `icon_swords` (Скрещенные мечи).
* **Высота:** `Tier 1` (Плоская, скрыта туманом).

#### Состояния Объекта:
| Фаза | Визуал на Карте | Взаимодействие (UI) | Геймплейная Роль |
| :--- | :--- | :--- | :--- |
| **Stable** | Маркер активен. | Меню: **"PvP Queue / Wagers"**. | **Event Zone:** Дуэли игроков, ставки на бои NPC. |
| **Evac** | Маркер серый. | "Бои отменены". | Недоступно. |
| **Anomaly** | Скрыто. | Показывает инфо: *"Threat: Gladiator Waves"* | **Combat Challenge:** Арена захвачена элитными мобами. Награда за зачистку волн. |

### [PREFAB:: BLACK_MARKET] — "Сердце"
*Скрытые торговые ряды в полузатопленных подвалах.*
[poi_id:: port_heart_grey_service]
[address_id:: stable_grey_service]
[address_class:: stable_external]
[availability:: stable_cycle]
[accepted_families:: disputed_proof|contraband_trace]
[service_roles:: grey_guarantee|rumor]
[central_fallback:: none]
* **Map Token:** `icon_skull_coin` (Череп с монетой).
* **Высота:** `Tier 0` (Под землей/водой).

#### Состояния Объекта:
| Фаза | Визуал на Карте | Взаимодействие (UI) | Геймплейная Роль |
| :--- | :--- | :--- | :--- |
| **Stable** | Маркер виден после открытия и только если подвалы сохранились. | Адресная карточка спорного права и слухов. | **Серая услуга:** поручительство или информация с явным последствием, без почасового окна. |
| **Evac** | Маркер исчезает. | Нет. | Торговцы скрываются первыми. |
| **Anomaly** | Скрыто. | Показывает инфо: *"Loot: Smuggled Goods"* | **Loot Spot:** Склады контрабандистов. Высокий шанс найти нелегальные предметы. |

# 2. Категория: Подземелья (Dungeons)
*Крупные структуры-ориентиры. В Аномалии их силуэты служат маяками для навигации.*

### [DUNGEON:: FACTORY_CHIMNEYS] — "Трубы Литейной"
*Группа дымящих труб.*
* **Map Token:** `NONE`.
* **Высота:** `Tier 2` (Едва видны).

#### Состояния Объекта:
| Фаза | Визуал на Карте | Логика |
| :--- | :--- | :--- |
| **Stable** | Декорация промзоны. | Часть пейзажа. |
| **Anomaly** | **Силуэт.** Виден красный свет и дым из труб над туманом. | **Raid Objective:** Локация с боссом-механоидом. |

---

## Подземелья Порта (Port Dungeons)
*Визуальные ориентиры в тумане Аномалии.*

### [DUNGEON:: CREMATORIUM] — "Старый Крематорий"
*Мрачное кирпичное здание с высокими трубами.*
* **Map Token:** `NONE`.
* **Высота:** `Tier 3` (Трубы возвышаются над туманом).

#### Состояния Объекта:
| Фаза | Визуал на Карте | Логика |
| :--- | :--- | :--- |
| **Stable** | Старая промзона, закрытая забором. | Декорация. |
| **Anomaly** | **Силуэт Труб.** Из них валит густой черный дым, смешиваясь с туманом. | **Raid (Horror):** Дебафф "Удушье". Цель: Урны с прахом и артефакты некромантов. |

### [DUNGEON:: THEATRE_PARADOX] — "Мистический Театр"
*Полузатопленное здание оперы с огромным куполом.*
* **Map Token:** `NONE`.
* **Высота:** `Tier 2` (Купол виден над "водой").

#### Состояния Объекта:
| Фаза | Визуал на Карте | Логика |
| :--- | :--- | :--- |
| **Stable** | Заброшенный театр, двери заколочены. | Можно услышать музыку, если подойти камерой близко. |
| **Anomaly** | **Светящийся Купол.** Сквозь проломы в крыше бьет неестественный сценический свет. | **Raid (Wave Defense):** Режим "Спектакль". Отражение 5 волн врагов. Лут: Маски, реквизит. |
# 3. UX Взаимодействие (Map Table Logic)

### Процедура Запуска (Deployment Sequence)
Когда сектор находится в фазе `Anomaly`:
1.  **Visual:** Весь сектор покрыт шейдером тумана/искажений.
2.  **Action:** Игрок кликает в любую точку тумана (или на конкретный силуэт данжа).
3.  **UI Response:** Открывается окно **Deployment Menu**:
    * *Squad Check:* Статус готовности сопартийцев.
    * *Loadout:* Возможность сменить расходники.
    * *Entry Point:* Выбор точки высадки (если доступно несколько).
    * **BUTTON:** [DEPLOY TO ANOMALY]

### Информационный слой (Intel Layer)
При наведении курсора на скрытые зоны в Аномалии (где предположительно стоят Префабы)(Изменить: главный командующий что сидит за столом не умеет того же что и его подопечные *пешки*):
* Если у игрока есть перк `Cartographer` или куплена информация:
    * Всплывает подсказка: *«Сигнал: Высокое содержание медикаментов»* (указывает на Аптеку).
* Без информации:
    * Подсказка: *«Сигнал: Неизвестная структура»*.
---

## 0. Нулевой пациент: шаблон POI

### Шаблон POI (Template POI)
[poi_id:: template_poi]
[address_id:: address_id|none]
[poi_role:: extraction_risk]
[address_class:: central|stable_external|none]
[availability:: permanent|stable_cycle|raid_only]
[accepted_families:: family_id|none]
[service_roles:: role_id|none]
[central_fallback:: poi_id|none]
[tier:: 1]
[anomaly_tiers:: T1, T2, T3]
[dominant_vector:: tech]
[dual_state:: stable/evac/anomaly]
[heat_state:: cold|warm|hot]
[heat_signal:: world-readable cue]
[heat_work:: contract|method|embedded_node|rescue|route_key]
[approach_contract:: approach_id | entry_anchor | route_layer | world_cue | approach_cost | refusal_path]
*Короткое описание точки интереса.*
- **В спокойной фазе:** что игрок получает.
- **В фазе эвакуации:** что блокируется перед сменой.
- **В Аномалии T1:** базовая рейдовая версия.
- **В Аномалии T2:** какие комнаты, мобы или риски раскрываются после первого Phase Shift.
- **В Аномалии T3:** ставка Пересборки, составной босс, закрытие выходов, Embedded-узел или редкий переносимый лут.
- **Связи:** фракция, биом, таблица лута, эвакуация.
