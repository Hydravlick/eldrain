---
type: system_contract
status: active
index_route: owner
index_group: world_generation
index_order: 205
index_summary: "Задаёт правила и последствия системы «CityState и жизненный цикл городских явлений»"
read_when: "Читайте при изменении общего состояния города, публичных событий, общей генерационной ревизии или вклада аккаунта в исход явления."
system: city_state
tags: [city_state, civic_events, shared_world, world_revision, public_contribution]
related_files:
  - "[[08_World_Generation/Generation/07_Server_Lifecycle|Server_Lifecycle]]"
  - "[[08_World_Generation/Hub/01_Hub_Map_Table|Hub_Map_Table]]"
  - "[[03_Factions_Societies/Quest_Engine|Quest_Engine]]"
  - "[[03_Factions_Societies/Lore/City_District_Social_Grammar|City_District_Social_Grammar]]"
  - "[[06_Economy_Loot/Barter_System|Barter_System]]"
  - "[[08_World_Generation/_Registries/Registry_POIs|Registry_POIs]]"
---
# CityState и жизненный цикл городских явлений

## 1. Обещание

Город живёт независимо от того, взял ли конкретный игрок контракт: магазин меняет публичную витрину, диорама показывает странность, а жители спорят о её цене. При этом игрок видит, какой личный поступок стал вкладом в общий исход, и не может один переписать город для остальных.

## 2. Единственный владелец общего города

`CIVIC_EVENT_LIFECYCLE` владеет одним `CityState` на региональный shard. Он единолично публикует упорядоченные `CityRevision`, общую генерационную ревизию, публичный каталог торговцев и состояние городских явлений.

```text
CityState
  city_state_id: regional shard
  city_revision: monotonic ordered revision
  world_revision: published shared generation snapshot
  merchant_catalog_revision: public catalogue and availability
  civic_events[]: public event records
```

`CityState` не принадлежит Хабу, карте, аккаунту или рейдовому `SessionID`. Карта его отображает, Quest Engine читает его давления, а торговец использует только его публичный каталог.

### Граница рейдовой сессии

При создании `SessionID` [[08_World_Generation/Generation/07_Server_Lifecycle|Server Lifecycle]] читает уже опубликованный `world_revision`. Поэтому параллельные рейдовые сессии одного shard, начатые на одной ревизии, получают одинаковые размещение POI, базовые правила сектора и доступные типы содержимого.

Внутри конкретной сессии дверь может быть открыта, существо убито, а груз оставлен иначе, чем в другой сессии. Это локальная живая история рейда: она не переписывает `CityState` и не меняет геометрию либо правило POI для остальных. Аккаунт отдельно хранит открытие POI, контрактную связь, личную награду и социальный след.

## 3. CivicEvent

`CivicEvent` — общее видимое явление города, а не квест, пин или личный инстанс.

```text
event_id
city_state_id
city_revision
scope_authority: regional_shard
state: emerging | visible | escalated | resolved | residue
visual_tell
impossible_rule
human_dependency
public_dispute
affected_parties[]
public_pressures[]
contribution_channels: rescue | containment | study | destruction | adoption | public_testimony
resolution_policy_ref
residue_type: visual | civic_rule | address | organism | route_condition | social_memory | future_pressure
residue_ref
persistence: one_cycle | until_superseded | permanent_history
```

Видимое явление всегда называет невозможное правило, человеческую зависимость и публичный спор о цене. Оно может не породить ни одного контракта; Quest Engine сам решает, какие давления становятся слухом, просьбой, спором или доступным заданием.

### Переходы и исход

Только `CIVIC_EVENT_LIFECYCLE` переводит событие между состояниями. На упорядоченной границе `CityRevision` он применяет authored `resolution_policy_ref`, которая читает опубликованные давления и свод публичных вкладов:

```text
emerging
  -> visible                 (явление получает публичный признак)
  -> escalated | resolved    (policy на CityRevision)
  -> residue                 (исход оставляет типизированный след)
```

Политика не является скрытым общим броском. Публичная карточка сообщает, какие каналы вклада — например, containment или public_testimony — повлияли на исход. Авторская политика может допустить эскалацию без игрока, но не лишает игрока базового доступа, обязательного power или единственного способа понять центральную историю.

### Личный результат и публичный вклад

Завершённый контракт сначала разрешается по обычным правилам Quest Engine и extraction: аккаунт получает личный результат только за физически вынесенное доказательство, наблюдаемый вред или custody-цепочку. Если контракт относится к активному `CivicEvent`, Quest Engine передаёт проверяемое основание в Lifecycle.

Lifecycle проверяет актуальность `event_id`, допустимый канал и основание, затем единолично записывает `ContributionReceipt`. Аккаунт видит свою квитанцию и личное последствие; общий город читает только агрегированный канал вклада. Один receipt не завершает явление в одиночку, но публичный исход обязан показать, что такой тип действия стал его причиной.

### Остаток и право пропустить момент

`residue_type` и `persistence` не дают полю остатка стать контейнером для всего. После исхода город может оставить изменённую диораму, правило, адрес, организм, условие маршрута, социальную память или будущую проблему.

Пропуск события меняет момент и контекст, но не отнимает у аккаунта фундаментальную возможность играть. Карта должна оставить хотя бы один из следов: остаток, свидетельство, слух или ретроспективный контракт.

## 4. Общий магазин и личный запас

`merchant_catalog_revision` задаёт, что в этом городе публично доступно и почему это видно в Порту. [[06_Economy_Loot/Barter_System|Barter System]] владеет личным запасом, покупкой, custody и инвентарём аккаунта. Два игрока видят один магазин и одну причину его ассортимента, но не конкурируют за одну последнюю личную единицу товара.

## 5. Границы

- Lifecycle не создаёт контракт, не выбирает Пешку, не выдаёт личную награду и не определяет репутацию.
- Quest Engine не меняет `CityState`; он передаёт только проверяемое основание вклада.
- Hub Map Table не хранит `CivicEvent` и не становится вторым источником каталога торговца.
- Публичный вклад не создаёт личную геометрию POI и не синхронизирует локальные действия рейда.
- Конкретная длительность CityRevision, частота событий и числовой вес каналов остаются предметом отдельного прототипа, а не скрытой нормой этого контракта.
