---
status: active
system: raid_ingress
tags:
  - ingress
  - admission
  - breach
  - spawn_safety
  - participation
related_files:
  - "[[08_World_Generation/Generation/Raid_Approach_and_Entry|Raid Approach and Entry]]"
  - "[[08_World_Generation/Generation/Egress_Solvency|Egress Solvency]]"
  - "[[08_World_Generation/Generation/Server_Lifecycle|Server Lifecycle]]"
  - "[[04_Player_Entities/Spawn_Logic|Spawn Logic]]"
  - "[[08_World_Generation/Registries/Registry_Raid_Interfaces|Raid interfaces]]"
type: system
index_route: owner
index_group: world_generation
index_order: 90
index_summary: "Определяет состояния, разрешение и связи: Insertion Logic."
read_when: Когда нужен контракт «Insertion Logic» и его границы с соседними владельцами.
---
# Insertion Logic

> Физический вход — не поездка и не безопасная комната. Это атомарный перевод подтверждённого намерения в уязвимое присутствие внутри уже живого сектора.

## Responsibility

`INSERTION_ADMISSION_RESOLVER` владеет `AdmissionHold`, проверкой текущей допустимости кандидата и освобождением временных ресурсов.

`INSERTION_BREACH_COORDINATOR` владеет:

- финальным выбором и повторной проверкой физической точки;
- единственным durable-решением `BreachTransaction=COMMIT|ABORT`;
- атомарным созданием `ParticipationClaim` и runtime `PhysicalRaidEntity` при `COMMIT`;
- первым доступным body frame после входа.

Эти владельцы не выбирают скрытую цель, не меняют `EntryQuote`, не определяют цену подхода, не считают обеспеченность выхода, не решают судьбу на Dawn и не создают специальные Recovery-инстансы. `PhysicalRaidEntity` — симулируемое тело мира; отдельный `PawnPresenceLease` является проекцией [[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]].

## AdmissionHold

Подтверждённый `EntryQuote` может открыть один ограниченный по времени `AdmissionHold`. Hold связывает Account, Pawn, sealed party roster, loadout snapshot, target epoch и quote revision. Он временно удерживает только ресурсы подготовки входа.

`AdmissionHold`:

- не является местом игрока в мире;
- не создаёт `Presence` или `ParticipationClaim`;
- не расходует право участия;
- не обещает конкретную точку;
- не переживает Seal, invalidated quote или terminal target revision.

Перед передачей в Breach Coordinator Admission Resolver повторно проверяет readiness, неизменность подтверждённых фактов, допустимость участия, актуальный lifecycle fence и наличие solvent pre-Seal envelope. Любое расхождение освобождает Hold либо возвращает поток в конечный administrative resolution; оно не переносит игрока на другую цель молча.

## Candidate selection and veto

Кандидаты создаются только в подготовленной физической геометрии сектора. Ранжирование применяется после hard veto и никогда его не отменяет.

Точка запрещена, если на момент проверки:

1. hostile actor, observer, trap, projectile или firing line контролирует появление либо первый обычный маршрут;
2. рядом идёт активный бой или прогнозируемое немедленное столкновение;
3. недавний kill/aim/dwell heat показывает подготовленную засаду;
4. точка обходит обязательную процедуру сектора или даёт прямой доступ к ключевой награде;
5. нет как минимум двух материально разных достижимых направлений к укрытию или маршруту;
6. геометрия, navmesh, collision, streaming readiness или target revision не подтверждены;
7. до Seal не остаётся времени для полного commit path.

Для группы используется согласованный кластер; veto одного обязательного участника отменяет весь кластер. RecoveryBindingAttempt проходит те же правила и не получает частной или более безопасной геометрии.

## Ingress pressure and legibility

Каждый durable `BreachTransaction=COMMIT` добавляет физический след в пространственно-временное поле входного давления. Одинаковые crossings дают одинаковый слышимый, видимый и доступный обычному world/AI след независимо от `AccountID`, объявленной группы или дружеского поведения.

Поле не меняет награду, hostility, knowledge, commitment, характеристики или matchmaking. Нельзя заменять его бинарной группировкой, детектором дружбы либо абстрактной надбавкой за solo-вход. Разнесённые во времени входы могут уменьшить общий след только ценой настоящего времени, разделения и маршрута.

## Breach transaction

Перед необратимостью кандидат повторно валидируется по свежему world snapshot.

```text
AdmissionHold
  -> candidate selected
  -> final veto + lifecycle + participation + solvency fences
      -> ABORT: release resources; no PhysicalRaidEntity; no participation consumed
      -> COMMIT: materialize Breach + ParticipationClaim + PhysicalRaidEntity atomically
```

`COMMIT` — единственная граница участия:

- для `AccountID × SessionID` создаётся ровно один lifetime `ParticipationClaim`;
- claim, `PhysicalRaidEntity` и физический Breach получают общий transaction key;
- до durable decision и при `ABORT` ни одна из трёх сущностей не существует;
- после durable `COMMIT` любой частичный технический результат идемпотентно достраивается до тех же `ParticipationClaim`, `PhysicalRaidEntity` и физического Breach с тем же transaction key; откат к их отсутствию запрещён;
- после `COMMIT` ledger остаётся consumed до завершения SessionID независимо от выхода, KIA или reconnect;
- освободившуюся вместимость может занять другой допустимый AccountID, но не повторное тело уже участвовавшего аккаунта.

`ABORT` не расходует участие и не создаёт наблюдаемого следа игрока в мире. Причина фиксируется, Hold освобождается, а дальнейший исход следует точной административной ветке.

## Economic commitment handoff

Ingress не владеет ценой, долгом, ключом или заложенной вещью. Он публикует immutable `BreachDecisionRef` объявленным commitment owners:

- durable `COMMIT` разрешает каждому владельцу exactly-once consume только собственной зарезервированной обязанности;
- `ABORT` требует release/refund по исходному commitment contract;
- повторная доставка того же decision ref не может списать ценность второй раз;
- сбой projection не меняет уже принятое Breach decision и восстанавливается владельцем обязательства.

Item custody и физические locks принадлежат [[07_Gear_Inventory/Inventory_Architecture|Inventory Architecture]], денежная проводка — [[06_Economy_Loot/Currency_Rez|Currency Rez]], а pledge/debt obligation — [[03_Factions_Societies/Pledge_Contracts|Pledge Contracts]].

## First-frame control contract

Первое клиенту доступное состояние существует только после durable `COMMIT`. В первом отрисованном и симулируемом body frame игрок:

- уже является обычной уязвимой `Presence`;
- имеет полный стандартный контроль движения, обзора, оружия и отменяемых действий;
- получает синхронизированный HUD и collision state;
- может быть замечен и атакован по тем же правилам, что другие присутствия.

Нет транспортной капсулы, фазы пробуждения, временной неуязвимости, блокировки управления или безопасной комнаты. Если система не может одновременно дать валидную геометрию, уязвимость и полный контроль, она обязана `ABORT` до материализации.

## Failure and reconnect

Разрыв клиента до `COMMIT` приводит к освобождению Hold или конечной same-target administrative resolution. Разрыв после `COMMIT` не отменяет Presence и не возвращает участие: стандартный reconnect присоединяет клиента к уже существующему телу, не создавая новый Breach.

## Non-ownership

- Approach/Binding/Quote: [[08_World_Generation/Generation/Raid_Approach_and_Entry|Raid Approach and Entry]].
- Normal-egress solvency: [[08_World_Generation/Generation/Egress_Solvency|Egress Solvency]].
- Phase order, Seal and Dawn: [[08_World_Generation/Generation/Server_Lifecycle|Server Lifecycle]].
- Pawn readiness and roster state: [[04_Player_Entities/Spawn_Logic|Spawn Logic]] and lifecycle owners.
