---
status: active
system: threshold_extraction
tags:
  - threshold
  - search
  - anchor
  - sync
  - extraction
related_files:
  - "[[08_World_Generation/Generation/Egress_Solvency|Egress Solvency]]"
  - "[[06_Economy_Loot/Return_Manifest_Contract|Return Manifest Contract]]"
  - "[[08_World_Generation/Generation/Server_Lifecycle|Server Lifecycle]]"
  - "[[08_World_Generation/Anomaly/Apex_Last_Hour|Apex Last Hour]]"
  - "[[08_World_Generation/Registries/Registry_Raid_Interfaces|Raid interfaces]]"
type: system
index_route: owner
index_group: world_generation
index_order: 100
index_summary: "Определяет состояния, разрешение и связи: Нестабильные Пороги: обычный выход."
read_when: "Когда нужен контракт «Нестабильные Пороги: обычный выход» и его границы с соседними владельцами."
---
# Нестабильные Пороги: обычный выход

Игрок ищет Порог по признакам среды и локальным предвестникам. Подтверждённая ветвь поиска приводит к физическому шву; его точное место назначается, когда шов должен проявиться. До синхронизации игрок видит вместимость, допустимую массу, ожидаемую длительность и условия прерывания. Во время процедуры тело остаётся уязвимым: урон или уход обнуляет прогресс, а оставшееся время Порога продолжает идти. Успешная синхронизация подтверждает выход для последующей доставки переносимого груза.

## SearchResolutionGraph

Для каждой допустимой обычной вылазки до Seal существуют минимум две материально независимые семьи поиска/маршрута, чтобы один choke, POI или способ чтения не превращался в единственный обязательный ответ. Граф связывает:

- изучаемые признаки среды;
- локальные предвестники;
- возможные ветви маршрута;
- условия открытия следующего наблюдаемого факта;
- набор допустимых anchor-классов.

Граф гарантирует объяснимую возможность искать выход, а не успешную эвакуацию. Игрок может неверно прочитать признаки, задержаться, проиграть бой или отказаться. `SearchEvidence` считается подтверждённым только из authored evidence, совместимого с текущим static revision certificate. Перед переводом возможности в `FORETOLD` проверяются этот certificate, текущая достижимость и действующий solvency fact. Система не имеет права скрыто оставить корректно играющее присутствие без всякой достижимой поисковой семьи, пока normal-egress envelope ещё действует.

Точные координаты и момент появления не публикуются глобально. Один вечный выход, фиксированный край карты и полностью случайная милость не соответствуют контракту.

## ThresholdAnchorAssignment

Конкретный `threshold_anchor` назначается только тогда, когда подтверждённая поисковая ветвь должна материализовать шов. Назначение учитывает текущую топологию, достижимость, matching static revision certificate, phase revision, уже занятые назначения, актуальное давление и current solvency check.

Один физический slot не может быть обещан двум несовместимым lease. Anchor assignment:

- не является резервированием на весь рейд;
- не закрепляет Порог за первым увидевшим;
- не переносит игрока по карте;
- не доказывает успешный выход;
- после durable assignment не меняется по повторному запросу, reconnect, клиентскому отказу или наблюдению результата;
- может быть аннулирован только server-authored несовместимой topology revision или terminal lifecycle fence; это создаёт объяснимый terminal/fade fact, а не новый клиентский reroll.

## SyncLease

Игрок начинает синхронизацию только для собственной `Presence` и физически переносимого custody graph. До начала UI показывает вместимость, ожидаемую длительность, допустимую массу и условия прерывания.

`SyncLease`:

1. создаётся для одного Presence, anchor revision и carried graph snapshot;
2. оставляет тело полностью уязвимым и управляемым в пределах объявленного action contract;
3. прерывается уроном, выходом из процедуры, разрушением anchor или несовместимой сменой мира;
4. при прерывании освобождает slot и обнуляет progress, но не перезапускает непрерывный TTL;
5. после прерывания переходит в `RESET/OPEN` только если остаточный TTL и свежий `CanStartSync` всё ещё валидны; иначе получает читаемый `FADE`;
6. при успехе фиксируется ровно один раз и передаётся `RETURN_MANIFEST` как trigger proof.

Убийца может использовать оставшийся открытым Порог и физически подобрать груз. Чужие тайники, тела и предметы на земле не включаются автоматически.

## Phase boundary

Обычные Пороги доступны только до lifecycle `Seal`. После Seal новые search/assignment/sync операции не создаются, а незавершённые операции завершаются согласно атомарному порядку [[08_World_Generation/Generation/Server_Lifecycle|Server Lifecycle]].

Sealed Apex `05:00–06:00` — другой контракт выживания. Dawn не является Порогом, бесплатным slot или поздним `SyncLease`.

## Handoffs

### Responsibility

Threshold flow разделён между тремя владельцами:

- `RAID_KNOWLEDGE_LEDGER` владеет `SearchResolutionGraph`, подтверждёнными `SearchEvidence` и тем, что конкретная поисковая ветвь стала известна;
- `SESSION_BOUNDARY_GRAPH` владеет `ThresholdOpportunity` и durable `ThresholdAnchorAssignment` внутри committed topology revision;
- `EXTRACTION_RESOLVER` владеет созданием, прерыванием и успешным завершением `SyncLease`.

Ни один из них не владеет достаточностью общего числа выходов, физической доставкой вещей, `ReturnManifest`, Breakline, Seal/Apex/Dawn, судьбой персонажа или Recovery. Knowledge owner не назначает anchor; topology owner не подтверждает знание игрока и не решает Sync; extraction owner не reroll-ит topology или evidence.

- [[08_World_Generation/Generation/Egress_Solvency|Egress Solvency]] доказывает, что joinable pre-Seal envelope покрывает обязательства; он не выбирает anchor и не решает Sync.
- [[06_Economy_Loot/Return_Manifest_Contract|Return Manifest Contract]] получает committed `SyncLease` и атомарно решает физическую доставку carried graph; он не решает успех Sync.
- [[08_World_Generation/Generation/Server_Lifecycle|Server Lifecycle]] задаёт Seal/Dawn order.
- [[08_World_Generation/Anomaly/Apex_Last_Hour|Apex Last Hour]] управляет sealed survival grammar, а не обычными выходами.

## Prototype checks

- каждый валидный поздний вход до Seal получает хотя бы одну объяснимую ветвь поиска;
- игрок до Sync понимает вместимость, carried graph и reset;
- два потребителя не могут получить один и тот же slot;
- прерывание никогда не превращается в невидимое расходование выхода;
- Threshold-camping силён локально, но не универсален из-за нескольких ветвей и JIT assignment;
- Seal не оставляет подвешенных lease или двойной authority.
