---
type: mechanic_contract
status: active
system: pawn_errands
tags: [pawn, hub, poi, roster, delegation]
related_files:
  - "[[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]]"
  - "[[08_World_Generation/Hub/01_Hub_Map_Table|Hub Map Table]]"
  - "[[08_World_Generation/Hub/02_Hub_Services_Interaction|Hub Services Interaction]]"
  - "[[08_World_Generation/Hub/03_Hub_Map_Interaction|Hub Map Interaction]]"
  - "[[03_Factions_Societies/Quest_Engine|Quest Engine]]"
  - "[[09_Project_Management/Risk_Register|Risk Register]]"
read_when: "Читайте при изменении поручения Пешке, её доступности в Хабе, маршрута к POI или результата городской услуги."
---

# Поручения Пешкам

> Активный владелец `PawnErrandLease`: одного видимого поручения Пешки между POI Хаба. Это не фоновая добыча, не второй рейд и не список ежедневных заданий.

## Обещание игроку

Игрок видит, куда и зачем идёт конкретная Пешка. Пока поручение не завершено, её нельзя случайно отправить в рейд; карта показывает маршрут, цель и понятный результат.

## Граница владельца

`PAWN_ERRAND_LEASE` владеет созданием, состоянием и завершением `PawnErrandLease`, резервом входов поручения и причиной результата.

Он не владеет roster membership, финальным `PawnPresenceLease`, геометрией Хаба, POI/service offer, наградой контракта, городским событием, extraction, loot custody или скоростью анимации маршрута.

| Слой | Владелец | Что передаёт или читает |
|---|---|---|
| Доступность Пешки | [[04_Player_Entities/Lifecycle_Roster\|Lifecycle Roster]] | `PawnID`, `Presence = HUB`, readiness и единственный переход в `ERRAND` |
| Поручение | эта страница | `PawnErrandLease` и его переходы |
| POI и услуга | [[08_World_Generation/Hub/02_Hub_Services_Interaction\|Hub Services Interaction]] | актуальный `ServiceOfferID`, допустимые входы и settlement результата |
| Карта | [[08_World_Generation/Hub/01_Hub_Map_Table\|Hub Map Table]] | origin, destination, маршрут и видимый статус без права менять lease |
| Контракт | [[03_Factions_Societies/Quest_Engine\|Quest Engine]] | может указать на услугу, но не создаёт и не завершает routine errand |

## Запись lease

```text
PawnErrandLease {
  ErrandID,
  PawnID,
  OriginPOI,
  DestinationPOI,
  ServiceOfferID,
  payload_reservation_ref?,
  cost_reservation_ref?,
  HubRevisionID,
  state,
  version
}
```

Поля являются техническими именами контракта. Игрок видит название Пешки, цель, назначение, текущий статус и результат, а не внутренние ID.

## Цикл игрока

1. Игрок выбирает `ReadySelectable` Пешку, доступный POI и опубликованную услугу.
2. До подтверждения видит цель, требуемый предмет или цену, что Пешка станет недоступна и какой результат услуга способна вернуть.
3. После подтверждения карта показывает Пешку на маршруте `OriginPOI → DestinationPOI`.
4. При прибытии услуга ещё раз проверяется. Игрок видит завершение или понятную причину блокировки.
5. После settlement Пешка снова доступна в Хабе; результат не появляется как награда за ожидание.

## Состояния и порядок

| Состояние | Предусловие и триггер | Обязательный результат |
|---|---|---|
| `COMMITTED` | Один атомарный commit прошёл readiness, Presence, offer и reservation-проверки | Lease создан; `Lifecycle Roster` проецирует readiness `ERRAND` |
| `WALKING` | Карта получила подтверждённый lease | Карта показывает маршрут; повтор команды не создаёт второй lease |
| `ARRIVED` | Пешка достигла DestinationPOI в видимой проекции | Сервис повторно читает текущий offer и reservation |
| `RESOLVED` | Сервис принял входы и записал свой результат | Reservation settlement завершён; roster возвращает Пешку в `READY` при сохранённом `HUB` Presence |
| `CANCELLED` | Игрок отменил `COMMITTED` до начала `WALKING` | Lease и резервы освобождены без результата; Пешка возвращается в `READY` |
| `BLOCKED` | POI, offer или вход стали недействительны до settlement | Игрок получает причину; сервис разрешает или возвращает резерв; Пешка возвращается в `READY` |

Ни UI, ни карта, ни Quest Engine не могут перепрыгнуть состояние, написать `RESOLVED` или вернуть Пешку в `READY` самостоятельно.

## Атомарный commit

Порядок `COMMITTED` всегда один:

1. Проверить `PawnPresenceLease.state = HUB` и `readiness = READY` у `Lifecycle Roster`.
2. Проверить актуальность `OriginPOI`, `DestinationPOI` и `ServiceOfferID` у владельца услуги.
3. Проверить и зарезервировать payload и цену.
4. Создать единственный versioned `PawnErrandLease`.
5. Только после успешного commit спроецировать readiness `ERRAND` и показать маршрут.

Любой неуспех до шага 4 не меняет Пешку. Неуспех после reservation, но до lease, откатывает reservation. Два одновременных запроса к одной Пешке: выигрывает один commit; второй получает отказ без частичного списания.

## Критические случаи

| Условие | Разрешение | Защищаемый принцип |
|---|---|---|
| Игрок пытается начать рейд Пешкой в `ERRAND` | admission отклоняет выбор по `ReadySelectable` | Одно тело не находится в двух действиях |
| POI исчезает или меняет offer в пути | `BLOCKED`; settlement решает судьбу резерва по service contract | Карта не обещает устаревший результат |
| Игрок перезашёл или карта перерисовалась | тот же `ErrandID` и `version` восстанавливают статус; повторное наблюдение ничего не списывает | Наблюдение не является действием |
| Payload больше невалиден к прибытию | услуга возвращает понятный `BLOCKED` либо применяет свой заранее опубликованный settlement | Предмет не дублируется и не исчезает молча |
| Пешка получает terminal lifecycle outcome | lease прекращается владельцем lifecycle; сервис не создаёт награду или замену | Lifecycle сильнее поручения |
| Игрок ждёт в Хабе | ожидание не генерирует Rez, loot, reputation, progression или новый контракт | Нет safe-profit и daily-FOMO |

## Границы контента

Routine errand обслуживает уже опубликованную городскую услугу или локальную передачу. Он не создаёт новый POI, не меняет фазу мира, не потребляет `EntryQuote`, не даёт доступ к рейду и не заменяет контрактную вылазку. Реальная срочность остаётся свойством наблюдаемого городского/рейдового события, а не таймером routine errand.

## Открытое измерение

Скорость маршрута, длина видимой прогулки и необходимость ожидать завершения — `EMPIRICAL_UNKNOWN`. Прототип должен проверить одно: помогает ли видимый маршрут игроку понимать недоступность Пешки лучше, чем статичный статус, без ощущения idle-таймера.
