---
status: active
system: city_state
tags:
  - city_state
  - civic_events
  - shared_world
  - city_revision
  - public_contribution
related_files:
  - "[[08_World_Generation/Generation/Location_Revision_Lifecycle|Location_Revision_Lifecycle]]"
  - "[[08_World_Generation/Generation/Server_Lifecycle|Server_Lifecycle]]"
  - "[[08_World_Generation/Hub/Hub_Map_Table|Hub_Map_Table]]"
  - "[[03_Factions_Societies/Quest_Engine|Quest_Engine]]"
  - "[[03_Factions_Societies/Lore/City_District_Social_Grammar|City_District_Social_Grammar]]"
  - "[[06_Economy_Loot/Barter_System|Barter_System]]"
  - "[[08_World_Generation/Registries/Registry_POIs|Registry_POIs]]"
type: system
index_route: owner
index_group: world_generation
index_order: 205
index_summary: "Определяет состояния, разрешение и связи: CityState и жизненный цикл городских явлений."
read_when: Читайте при изменении общего состояния города, публичных событий, CityRevision или вклада аккаунта в исход явления.
---
# CityState и жизненный цикл городских явлений

## 1. Обещание

Город живёт независимо от того, взял ли конкретный игрок контракт: магазин меняет публичную витрину, диорама показывает странность, а жители спорят о её цене. При этом игрок видит, какой личный поступок стал вкладом в общий исход, и не может один переписать город для остальных.

## 2. Единственный владелец общего города

`CIVIC_EVENT_LIFECYCLE` владеет одним `CityState` на региональный shard. Он единолично публикует упорядоченные `CityRevision`, публичный каталог торговцев и состояние городских явлений. Общую ревизию локации создаёт отдельный [[08_World_Generation/Generation/Location_Revision_Lifecycle|WORLD_REVISION_PUBLISHER]].

```text
CityState
  city_state_id: regional shard
  city_revision: monotonic ordered revision
  merchant_catalog_revision: public catalogue and availability
  civic_events[]: public event records
```

`CityState` не принадлежит Хабу, карте, аккаунту или рейдовому `SessionID`. Карта его отображает, Quest Engine читает его давления, а торговец использует только его публичный каталог.

### Граница рейдовой сессии

При создании `SessionID` [[08_World_Generation/Generation/Server_Lifecycle|Server Lifecycle]] читает опубликованную [[08_World_Generation/Generation/Location_Revision_Lifecycle|WorldRevision]] вместе с текущим `CityState`. Поэтому параллельные рейдовые сессии одного shard, начатые на одной ревизии, получают одинаковые размещение POI, базовые правила сектора и доступные типы содержимого.

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

Завершённый контракт сначала разрешается по обычным правилам Quest Engine: field-контракт — за физически вынесенное доказательство, наблюдаемый вред или custody-цепочку, а Hub-only — за объявленную цель и метод. Если контракт относится к активному `CivicEvent`, Quest Engine передаёт проверяемое основание в Lifecycle.

Lifecycle проверяет актуальность `event_id`, допустимый канал и основание, затем единолично записывает `ContributionReceipt`. Аккаунт видит свою квитанцию и личное последствие; общий город читает только агрегированный канал вклада. Требует ли исход многих вкладов или одной уникальной операции, задаёт `resolution_policy_ref`; публичный исход обязан показать, какой тип действия стал его причиной.

### Идемпотентный `ContributionReceipt`

```text
ContributionReceipt
  receipt_id
  event_id
  contract_id
  account_id_hash
  contribution_channel
  evidence_ref
  accepted_city_revision
  aggregation_status: accepted_pending_barrier | aggregated | rejected_duplicate | rejected_late | rejected_invalid
```

Личный результат контракта и публичное принятие вклада — разные переходы. Quest Engine сначала разрешает личную награду по своему контракту; только затем Lifecycle принимает либо отвергает общественную квитанцию.

- Для пары `event_id + contract_id` допускается не более одной принятой квитанции.
- Повтор `receipt_id` возвращает прежний результат и не увеличивает вклад; повторная доставка после reconnect не создаёт новый receipt.
- Квитанция принимается только в открытую `accepted_city_revision`. Барьер агрегирует все принятые к нему квитанции и закрывает ревизию.
- Поздняя доставка не пересчитывает закрытую ревизию. Если событие всё ещё активно в новой открытой ревизии, новый валидный контракт может создать новую квитанцию уже для неё; иначе receipt получает `rejected_late`.
- `resolution_policy_ref` определяет, агрегирует ли барьер множество обычных квитанций либо ждёт одну заранее объявленную уникальную операцию.

### Остаток и право пропустить момент

`residue_type` и `persistence` не дают полю остатка стать контейнером для всего. После исхода город может оставить изменённую диораму, правило, адрес, организм, условие маршрута, социальную память или будущую проблему.

Пропуск события меняет момент и контекст, но не отнимает у аккаунта фундаментальную возможность играть. Карта должна оставить хотя бы один из следов: остаток, свидетельство, слух или ретроспективный контракт.

## 4. Общий магазин и account custody

`merchant_catalog_revision` задаёт, что в этом городе публично доступно и почему это видно в Порту. [[06_Economy_Loot/Barter_System|Barter System]] владеет account custody, покупкой и инвентарём; [[03_Factions_Societies/Quest_Engine|Quest Engine]] владеет контрактным reward budget. Два игрока видят один магазин и одну причину его ассортимента, но не конкурируют за одну последнюю единицу товара.

## 5. Границы

- Lifecycle не создаёт контракт, не выбирает Пешку, не выдаёт личную награду и не определяет репутацию.
- Lifecycle не создаёт `LocationRevision`, Stable-проекцию, веса адресов или `WorldRevision`.
- Quest Engine не меняет `CityState`; он передаёт только проверяемое основание вклада.
- Hub Map Table не хранит `CivicEvent` и не становится вторым источником каталога торговца.
- Публичный вклад не создаёт личную геометрию POI и не синхронизирует локальные действия рейда.
- Конкретная длительность CityRevision, частота событий и числовой вес каналов остаются предметом отдельного прототипа, а не скрытой нормой этого контракта.
