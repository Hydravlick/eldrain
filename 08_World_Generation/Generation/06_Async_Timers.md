---
type: system_contract
status: active
index_route: owner
index_group: world_generation
index_order: 180
index_summary: "Задаёт правила и последствия системы «Асинхронные таймеры и regional service»."
read_when: "Читайте при изменении входов, состояний, стоимости или последствий системы «Асинхронные таймеры и regional service»."
system: regional_service
tags: [regional_scheduler, rolling_pool, capacity, low_population, service_availability]
related_files:
  - "[[08_World_Generation/Generation/07_Server_Lifecycle|Server Lifecycle]]"
  - "[[08_World_Generation/Generation/19_Raid_Approach_and_Entry|Raid Approach and Entry]]"
  - "[[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]]"
  - "[[08_World_Generation/Hub/01_Hub_Map_Table|Hub Map Table]]"
---
# Асинхронные таймеры и regional service

## 1. Ответственность
`REGIONAL_SCHEDULER` владеет regional service set, hosting, capacity, latency policy и fixed `LowPopulationPolicy`. Он обслуживает новый request только через already-live `SessionID`, но не владеет session clock, phase band, `PhaseRevision`, Seal/Dawn barrier или player outcome: это authority [[08_World_Generation/Generation/07_Server_Lifecycle|Server Lifecycle]].

Scheduler не создаёт отдельную T4 queue, личную Recovery карту, первый population для Recovery или новый shard как ответ на suppression/отказ кандидата. Recovery никогда не создаёт shard, first population или RECOVERY-only queue. Duplicates допустимы только из demand/capacity policy.

Минимальный regional service set сохраняет три live age envelopes: `0–2`, `2–4` и `4–6` часов возраста SessionID. Поздний envelope joinable только в `04:00–05:00` как T3 Reassembly/Choice; в `05:00–06:00` тот же instance остаётся live как sealed Apex и не принимает новый ingress.

Это не обещает одновременно joinable T1, T2, T3 и T4 или всегда доступный joinable T3. High-end window может отсутствовать, пока поздний envelope sealed; [[08_World_Generation/Hub/01_Hub_Map_Table|Hub Map Table]] показывает forecast следующего staging вместо скрытого обещания очереди. Public session означает обычный service pool, а не гарантированно populated PvP-сцену.

## 2. Сервисное обещание
Scheduler создаёт динамическую доступность, но не appointment FOMO и не hidden population oracle:
* **Forecast, не обещание:** Hub показывает доступность envelope и прогноз следующего staging без UTC-обязательства, raw population или collapse-step.
* **Ротация целей:** service set не делает один сектор вечным фармом; unavailable envelope показывается честно, а не тихо заменяется другим Tier.
* **Защита от таймзон:** rolling service не привязан к одному глобальному часу, но late joinable window может отсутствовать, пока поздний SessionID sealed.

## 3. Проекция service state
Hub показывает только доступность envelope и forecast следующего staging; полный ingress quote и body-frame feedback принадлежат другим owners.
* Service projection не обещает populated PvP, nearby opponents или безопасную среду.
* Внутренние activity state, raw population, collapse-step и reason code не показываются игроку и не являются player-visible oracle.
* Нет `RECOVERY ONLY`: Recovery использует ordinary public service path либо остаётся в search state у [[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]].
* `SEEDING` принимает только первого ordinary STANDARD participant; Recovery не создаёт first population или RECOVERY-only intake.

## 4. Fixed LowPopulationPolicy

При падении population/capacity Regional Scheduler применяет только этот порядок:

1. Backfill healthy `BaseAdmissionServiceable` already-live `SessionID`.
2. Stop creating duplicates.
3. Перевести duplicates в `DRAINING`: existing bodies и их clock остаются; новые Binding/Quote не выдаются.
4. Remove event/overflow sessions из нового admission.
5. Reduce sector breadth, сохраняя три age envelopes.
6. Использовать latency-compatible federation только для новых unbound requests.
7. Mark конкретный envelope unavailable; never silently substitute другой envelope.

Existing bodies никогда не перемещаются; Session clocks не reset, не merge и не перепривязываются. Federation не меняет target после durable disclosure. `DRAINING` прекращает новый Binding/Quote, но не отменяет durable disclosure: disclosed request использует тот же target и finite administrative resolution.

## 5. Negative boundaries and downstream drift

Scheduler публикует serviceability facts для ordinary admission — health, capacity, latency compatibility, runtime availability и forecast — но не phase или outcome. Target binding, exact quote, physical admission and `Breach` остаются у [[08_World_Generation/Generation/19_Raid_Approach_and_Entry|Raid Approach and Entry]] и generic ingress owners; Scheduler не решает RecoveryCase, expiry, manifest или Dawn result.

Региональный планировщик публикует только пригодные service envelopes. [[08_World_Generation/Generation/19_Raid_Approach_and_Entry|Raid Approach and Entry]] потребляет их без передачи target, quote или admission authority планировщику.
