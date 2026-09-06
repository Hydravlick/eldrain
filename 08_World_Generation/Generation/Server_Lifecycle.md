---
status: active
system: server_lifecycle
tags:
  - session_clock
  - phase_revision
  - phase_barrier
  - apex
  - dawn
  - rolling_pool
related_files:
  - "[[08_World_Generation/Generation/Async_Timers|Async Timers]]"
  - "[[08_World_Generation/Generation/Egress_Solvency|Egress Solvency]]"
  - "[[08_World_Generation/Anomaly/Apex_Last_Hour|Apex Last Hour]]"
  - "[[08_World_Generation/Anomaly/Insertion_Logic|Insertion Logic]]"
  - "[[06_Economy_Loot/Return_Manifest_Contract|Return Manifest Contract]]"
  - "[[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]]"
  - "[[08_World_Generation/Hub/Hub_Map_Table|Hub Map Table]]"
  - "[[08_World_Generation/City_State/Civic_Event_Lifecycle|Civic Event Lifecycle]]"
  - "[[08_World_Generation/Generation/Location_Revision_Lifecycle|Location Revision Lifecycle]]"
type: system
index_route: owner
index_group: world_generation
index_order: 190
index_summary: "Определяет состояния, разрешение и связи: Жизненный цикл сервера."
read_when: Когда нужен контракт «Жизненный цикл сервера» и его границы с соседними владельцами.
---
# Жизненный цикл сервера

## 1. Единственный владелец времени и барьеров

`SERVER_LIFECYCLE` — единственный владелец `SessionID`, elapsed session clock, производной phase band, монотонного `PhaseRevision`, phase barriers и полного порядка решений на одном ключе. Один `SessionID` живёт шесть часов; это непрерывная жизнь одной карты, а не длительность личного рейда или отдельная очередь.

При создании `SessionID` Lifecycle читает опубликованную [[08_World_Generation/Generation/Location_Revision_Lifecycle|WorldRevision]] и текущий [[08_World_Generation/City_State/Civic_Event_Lifecycle|CityState]]. Он не выбирает и не меняет ни один из них. Сессии, начатые на одной `location_revision_id`, получают одинаковые геометрию, здания, маршруты и базовые POI; их живые локальные изменения по-прежнему не синхронизируются.

`T1`, `T2`, `T3` и `T4` — только производные состояния возраста мира. Они никогда не являются билетом, уровнем снаряжения, продуктом доступа или matchmaking bucket. Вход, materialization, target binding, egress и per-Presence исходы принадлежат профильным владельцам; Server Lifecycle поставляет им только время, revision и order.

```yaml
SessionClock:
  owner: SERVER_LIFECYCLE
  source: SessionID
  city_state_input: city_state_id + city_revision (read-only)
  world_revision_input: world_revision_id + location_revision_id (read-only)
  elapsed_session_clock: monotonic
  phase_revision: monotonic_committed_session_phase_revision
  lifecycle: created_once_per_session; never_reset_or_merged
```

## 2. Производная фазовая идентичность

| Время session clock | Phase band | Правило lifecycle |
|---|---|---|
| `00:00–02:00` | Manifestation | Живой joinable мир первой возрастной полосы. |
| `02:00–04:00` | Memory | Живой joinable мир второй возрастной полосы. |
| `04:00–05:00` | T3 Reassembly/Choice | Последняя joinable полоса: обычная цель, риск и Threshold ещё могут поместиться до Seal. |
| `04:00` | Apex disclosure point | Server Lifecycle публикует supplied `ApexDirector` family/signature facts; он не выбирает family или content. |
| `04:45` | Apex last foretell | Каждый active player получает обязательный foretell о предстоящем Seal. |
| `05:00–06:00` | sealed T4 Apex | Та же карта и тот же `SessionID` остаются live, но ingress больше не публикуется. |
| `06:00` | Dawn resolving / terminal | Барьер запускает per-Presence settlement у профильных lifecycle owners. |

Фазовая смена может менять локальную `PhaseRevision` и authored-правила текущей сессии, но не публикует новую `world_revision` для города и не переносит игроков в комнату, безопасный Саркофаг или иную локацию. Первое доступное body frame и полный контроль после materialization принадлежат [[08_World_Generation/Anomaly/Insertion_Logic|Insertion Logic]], а не этому owner.

## 3. Барьеры и полный порядок

Каждое решение имеет полный `arbitration_key = (server_tick, event_priority, sequence)`. Нет равных ключей. `SERVER_LIFECYCLE` применяет все lower-key решения до барьера; решение с тем же или более поздним ключом следует правилам конкретного барьера.

Обычный phase barrier фиксирует новую `PhaseRevision` после lower-key world/movement решений. Он не создаёт ticket, отдельную сессию или иммунитет. Подготовка и validators других владельцев могут не допустить новую joinable публикацию, но не изменяют clock.

### 3.1 Seal — 05:00

В `05:00` Server Lifecycle безусловно закрывает ingress, Threshold и Breakline. Lower-key операции завершаются по своим owners; same-key и higher-key попытки этих путей abort. Remaining Presence продолжают существовать на той же карте и в том же `SessionID` как sealed Apex cohort: нет relocation, отдельной комнаты, безопасного ожидания или нового admission.

[[08_World_Generation/Generation/Egress_Solvency|Egress Solvency]] получает барьерный факт для retirement pre-Seal bundle; [[08_World_Generation/Anomaly/Apex_Last_Hour|Apex Last Hour]] получает sealed transition/cohort fact. Server Lifecycle не решает solvency, Apex pressure, manifest или Recovery.

### 3.2 Dawn — 06:00

В `06:00` Dawn — barrier и trigger per-Presence settlement, не egress supply, Threshold slot или продление admission. Lethal terminal events с приоритетом на том же ключе разрешаются до settlement trigger.

`PENDING_OWNER:LIFECYCLE_RESOLVER` единолично принимает per-STANDARD `DawnSettlementDecision=STANDARD_RETURN|LETHAL_TERMINAL`. [[04_Player_Entities/Recovery_Lifecycle|RECOVERY_LIFECYCLE]] единолично принимает Recovery outcome. [[06_Economy_Loot/Return_Manifest_Contract|EXTRACTION_RETURN_RESOLVER / Return Manifest]] получает только committed `STANDARD_RETURN` и производно доставляет физический custody; он никогда не владеет survival или settlement decision. Эта страница не выбирает ни одну ветку `UR-001`, `UR-002` или `UR-003`.

## 4. Непрерывность SessionID и общий WorldRevision

Seal и Dawn не создают второй рейдовый инстанс. После terminal settlement Lifecycle фиксирует локальный итог `SessionID`; переносимый предмет не становится личной наградой от итоговой карты.

Публичный `WorldRevision` приходит от [[08_World_Generation/Generation/Location_Revision_Lifecycle|WORLD_REVISION_PUBLISHER]], а не складывается из исхода одной сессии. Он ссылается на одну общую `LocationRevision`, её Stable-проекцию и выбранные внешние адреса. [[08_World_Generation/Hub/Hub_Map_Table|Hub Map Table]] читает опубликованную ревизию как мирную проекцию, а не как свободно посещаемую карту. Следующий `SessionID` читает актуальную опубликованную ревизию; старые clocks не reset, не merge и не перепривязываются.

## 5. Граница с regional service

[[08_World_Generation/Generation/Async_Timers|Async Timers]] / Regional Scheduler владеет service set, hosting, capacity, latency и fixed LowPopulationPolicy. Он может сделать envelope unavailable или draining для нового intake, но не хранит phase band, `PhaseRevision`, Seal/Dawn order или outcome. Состояние public session не обещает фактическое население.

## 6. Remaining downstream drift

Смежные владельцы потребляют только ordered lifecycle facts: [[08_World_Generation/Generation/Raid_Approach_and_Entry|Approach and Entry]], [[08_World_Generation/Anomaly/Insertion_Logic|Insertion]], [[08_World_Generation/Anomaly/Extraction_System|Threshold Extraction]], [[08_World_Generation/Anomaly/Apex_Last_Hour|Apex]] и lifecycle/recovery resolvers. Они не получают clock authority из собственных страниц.
