---
title: "T4 Apex: терминальный endgame-цикл и живая продуктовая модель"
aliases:
  - "Apex / Последний час"
  - "T4 Apex"
type: architecture_proposal
status: proposed
canonical: false
date: 2026-07-23
system: t4_apex_endgame
tags:
  - proposal
  - endgame
  - apex
  - extraction
  - product-model
---

# T4 Apex: терминальный endgame-цикл и живая продуктовая модель

> [!warning] Proposal / noncanonical
> Это предложение, а не миграция канона. Все численные параметры, кроме жёстких часов сессии, требуют прототипа и телеметрической проверки. Канонические страницы не изменены и не считаются мигрированными этой заметкой.

## Решение и обещание игроку

**Apex / Последний час** — терминальный режим уже существующего `SessionID`, а не четвёртый tier снаряжения, не новый account level и не отдельный endgame-шард. Внутреннее сокращение `T4` допустимо только как backend shorthand. Игрок должен понимать простую ставку: если `STANDARD` Presence остаётся после seal, он переживает последний час в той же публичной карте и возвращает Пешку со всем eligible физически удерживаемым грузом только через Dawn. `RECOVERY` Presence тоже может пережить Apex, но его победный исход — `RECOVERED` без cargo, loot и standard reward.

- **AUTHOR CONSTRAINT — текущая граница продукта:** текущая архитектура не вводит playable `T5`, `Frame Class 4/5` или обязательную следующую ступень силы.
- **STRUCTURAL INFERENCE:** `T3` может завершать baseline power, а Apex проверяет мастерство и выдаёт горизонтальную ширину.
- **PRODUCT/EMPIRICAL UNKNOWN:** retention и content cadence без будущей вертикальной ступени ещё не доказаны.

Это не запрет `T5` навсегда. Его возвращение требует отдельного ADR и аудита экономики, builds и matchmaking.

| Оценка | Значение | Что означает |
|---|---:|---|
| Сырая идея без guardrails | 5/10 | Сильная смена режима, но bunker, loot faucet и доминирование Dawn ещё ломают extraction-решение |
| Целевая архитектурная связность | 8.5/10 | Контракт целостен при активном давлении, STANDARD full physical return, RECOVERY-only resolution и конечном reward budget |
| Эмпирическая уверенность | 4/10 | Часовой pacing, solo/squad corridor и реальный `pD` не доказаны |
| Коммерческая уверенность | 3/10 | До budget, CAC, retention и стоимости concurrency существует только продуктовая гипотеза |

Жёсткая временная грамматика одного `SessionID`:

| Время | Фаза | Контракт |
|---|---|---|
| 00:00–02:00 | T1 Manifestation | открытие проблемы и ранняя экспедиция |
| 02:00–04:00 | T2 Memory | развитие карты, памяти и давления |
| 04:00–05:00 | T3 Reassembly / Choice | устойчивый основной extraction-цикл и осознанный выбор |
| 05:00–06:00 | T4 Apex / Последний час | необратимый terminal regime |
| 06:00 | Dawn / Final Stabilization | per-Presence STANDARD return, RECOVERY resolution либо lethal/expired terminal outcome |

В 04:00 семья Apex и её signature уже публично видимы и в секторе, и в Hub: это время для честного планирования билда, пути и риска. В 04:45 выдаётся обязательное последнее физическое предупреждение (`APEX_LAST_FORETELL`). Оно не сообщает о дедлайне впервые; оно подтверждает, что обычный мир ещё раз предупреждает тело перед необратимой границей.

## Карта, ingress и seal

Apex — продолжение той же публичной карты, того же `SessionID` и того же Presence. Он не создаёт очередь, shard, комнату, лифт, саркофаг, телепорт или перенос тела. Нет T4-билета, `Access Contract` или покупки права на участие. Обычный `ApproachOffer`/`EntryQuote` допускается только до индивидуального pre-Seal cutoff. Любой Breach `COMMIT` до seal остаётся в normal-egress obligation ledger и допустим только если RAID-owned conservative corridor до 05:00 покрывает его. Capacity formula считает `TIMELY|ALLOCATED_SYNC`; server-proven missed latest-start переводит obligation в surplus-only `BEST_EFFORT_AFTER_LATEST_START`, но stay/quote/foretell сами этого не делают. Каждый ещё допустимый late quote показывает точные seal/cutoff/signature; если corridor не помещается, ingress закрывается раньше. 04:45 — обязательный foretell уже находящимся внутри, а не обещание, что вход открыт до 04:45. `APEX_BOUND` возникает только общим seal, а не намерением игрока. В 05:00 ingress закрыт всегда.

До 05:00 `Normal Threshold` и существующий **STANDARD-only** `Breakline` могут завершаться лишь full arbitration key, строго меньшим ключа seal. `ParticipationClaim.kind=RECOVERY` не может вызвать Breakline и разрешается только через RecoveryResolution, Dawn либо terminal fate. На том же tick побеждает `APEX_SEAL`; никакой гонки «я почти вошёл в threshold» не существует. После seal не существует Threshold, Breakline или ingress. Незавершённый sync abort; remaining/unresolved тела и custody graph остаются в поле. Каждый remaining living Presence становится необратимо `APEX_ACTIVE`. Disconnect не является выходом: логическое и физическое тело остаётся уязвимым в мире и подчиняется той же Dawn-арбитрации.

Normal-egress solvency и переход `EgressCoverageObligation → APEX_BOUND` принадлежат только [[RAID_INGRESS_EGRESS_ARCHITECTURE_SPEC#12. EgressSolvencyInvariant|RAID §12]]; эта заметка не создаёт validator и не считает Dawn Threshold-supply. После seal `APEX_ACTIVE` исключается из throughput только RAID-owned transition.

Минимальный порядок ключей должен быть тотальным, но Session state нельзя смешивать с per-Presence outcome:

```text
Session: T3_OPEN → APEX_FORETOLD → APEX_SEALED → DAWN_RESOLVING → TERMINAL
Presence: ACTIVE → APEX_ACTIVE → CARE/HUB projection | terminal removal
STANDARD DawnSettlementDecision: UNDECIDED → STANDARD_RETURN | LETHAL_TERMINAL
RECOVERY Case/Resolution: IN_RECOVERY → RECOVERED | FAILED | EXPIRED
EgressCoverageObligation: TIMELY | ALLOCATED_SYNC | BEST_EFFORT_AFTER_LATEST_START → APEX_BOUND → DAWN_RESOLVED | TERMINAL_REMOVED
```

Внутри финального tick порядок такой: более ранний полный key выигрывает; `KIA` или unresolved lethal-collapse на том же Dawn key имеет приоритет над «жив», а для Recovery также раньше выигрывает absolute Case expiry. `Last Thread` остаётся отдельной Recovery-судьбой: active unexpired Recovery survivor получает только `RECOVERED`, а потерявший тело либо Case до Dawn не survivor и не получает Dawn manifest/reward. Чужой Finisher не получает authority записывать другому Presence `KIA`; он лишь может стать причиной проверяемого combat/lifecycle-события.

## Dawn как полный return, а не разрешение на награду

В 06:00 каждый реально живой STANDARD Presence и каждый живой **unexpired** RECOVERY Presence получает success outcome, определённый его `ParticipationClaim.kind`, независимо от squad; это не означает одинаковый economic settlement. KIA/unresolved lethal-collapse, а для Recovery также выигравший absolute Case expiry, получают свой terminal outcome.

- `STANDARD`: один immutable `DawnSettlementDecision` фиксирует `STANDARD_RETURN`. LifecycleResolver переводит Пешку в `CARE/HUB`, а Return resolver создаёт full manifest всего eligible carried custody graph, включая физический loot, найденный в T4.
- `RECOVERY`: `RecoveryResolutionTransaction=RECOVERED`; ReturnManifest, cargo, loot и standard Dawn reward запрещены. На одинаковом key KIA/lethal collapse и absolute Case expiry имеют приоритет.

Для STANDARD не допускаются partial manifest, «только исходный loadout», protected slot, сортировка по rarity, отдельный T4-контейнер и абстрактный `DawnClaim`. Ground loot и чужие предметы, которых нет физически в custody на Dawn key, не подбираются автоматически.

Это не второй параллельный resolver. [[RAID_INGRESS_EGRESS_ARCHITECTURE_SPEC#13.3. ExtractionCommitted и ReturnManifest|RAID §13.3]] задаёт единственный `ReturnManifest`; T4 только потребляет его интерфейс:

```text
trigger_kind = NORMAL_THRESHOLD | DAWN
trigger_proof = exactly one of { SyncLeaseRef, DawnSettlementDecisionRef }
```

Для Dawn ReturnManifest сначала становится `PREPARED_DURABLE`; только после этого LifecycleResolver может решить `STANDARD_RETURN`. Manifest COMMIT является derived projection этого решения и не имеет собственного Dawn ABORT. Поэтому допустимого состояния «Dawn уже объявил победу, manifest затем отказал» нет.

`DawnSettlementDecision` принадлежит LifecycleResolver, читает immutable Dawn key от ServerLifecycle, принимает только `ParticipationClaim.kind=STANDARD` и не хранит предметы. Один owner manifest — Extraction/Return resolver. Inventory/Custody вычисляет eligibility каждого `ItemID`; ServerLifecycle выпускает только Seal/Dawn keys; Pawn Lifecycle/Presence владеет физическим body и terminal event; LifecycleResolver потребляет его lethal witness и решает STANDARD settlement; RecoveryResolutionResolver решает Recovery fate; ApexDirector задаёт pressure/world rules; legacy resolver производит Stable outcome; Chronicle записывает факты. `ReturnManifest` не принимает world reward policy, не оценивает вклад, не переводит Пешку, не рассчитывает personal contract и не решает, кто заслужил победу. Он применяет уже доказанное физическое состояние и один доказанный trigger.

Для STANDARD Dawn — второй полный способ возвращения: Return resolver commits eligible carried delivery facts. Mission/Pledge отдельно читает `trigger_kind=DAWN` и свою заранее объявленную policy; personal contracts settle так же, как при обычном return, кроме условий, явно маркированных `BEFORE_SEAL` или `NORMAL_THRESHOLD_ONLY`. Скрытый провал контракта из-за того, что игрок честно пережил Dawn, запрещён. RECOVERY branch не получает такого settlement.

Два независимых аудита предлагали «никакого cargo, только Chronicle/DawnClaim». Это решение сознательно отвергается: без cargo T4-предмет физически нереализуем либо требует отдельного DawnClaim-конвертера, обходящего custody и создающего вторую reward authority; рациональным становится minimal expendable loadout, а обещание ценного лута — ложным. Partial return отвергается отдельно из-за laundering/protected-slot packaging: он разрушает полный custody graph и стимулирует упаковку ценности в защищённый слот. Full manifest допустим только при доказанной активной угрозе. Если её можно пересидеть, вся конструкция — не рискованный endgame, а бесплатный сейф.

## Решение остаться: измеримая, а не декоративная дилемма

Игрок сравнивает не «правильный режим» и «побочную активность», а две разные полезности:

```text
U_exit = pE × (V_pawn + V_carry + V_contract) − C_exit
U_apex = pD × (V_pawn + V_carry + E[V_apex] + V_mastery) − C_hour − C_resources
```

Здоровая зона — выбор меняется от ценности груза, подготовки, текущей Пешки и желания пройти мастерство. Высокая carried stake часто уходит через Threshold; подготовленный игрок с иной целью иногда остаётся. Если один вариант почти всегда доминирует, сломана калибровка или сам режим. Формула не задаёт ставки: `pE`, `pD`, ценности и costs — прототипные наблюдаемые, не обещанные числа.

## APEX GAMEPLAY CONTRACT

На `SessionID` существует один читаемый `PrimaryApexFamily`. Для MVP нет стека случайных модификаторов: игрок должен понять закон мира, а не распутывать набор affix. Apex не является HP sponge и не требует часа непрерывной стрельбы. Его общая грамматика:

- Seal необратим, а давление активно меняет мир.
- Есть минимум две materially different survival verbs/routes.
- Static bunker не переживает весь час; короткие окна восстановления — не safe rooms.
- PvP и friendly fire остаются действующими.
- Basic victory — только действительно пережить Dawn: STANDARD получает return, RECOVERY — `RECOVERED`; нет score/contribution gate, winner slots или места для «победителя отряда».

Кооперация условна. Публичные действия помогают всем и не принадлежат last hit. `pressure budget` фиксируется от `cohort_at_seal` с минимальным floor и не уменьшается после смертей:

```text
B_apex = max(B_floor, B_world + f(N_seal))
```

`f` — сублинейна; realtime scale-down запрещён. Убийство сохраняет PvP-лут и позиционное преимущество, но убирает полезные руки и не облегчает мир. Один игрок не имеет общего fail-switch; должны существовать минимум две независимые survival route families. Solo получает complete route, совместная игра полезна с diminishing returns, а не с мультипликативной неуязвимостью.

MVP-family — **«Осада/Стена»**: глобальные фронты и волны, истощаемые позиции, движение, обслуживание, перенаправление и прорыв. Это не DPS quota. Из «Роркха» берётся только ощущение предсказуемой глобальной смены закона мира и коллективной ночи, не буквальная стена HP. Будущая ширина: `Migration` — движущаяся жизнеспособная геометрия; `Hunt` — системные преследователи, trace и decoys. Их нельзя комбинировать до отдельной валидации: random combinatorial soup скрывает проблему читаемости и баланса.

## Лут, экономика и предел вертикальной силы

T4 valuable loot — не global rarity multiplier и не `Frame Class 4`. Common layer остаётся. Ценность исходит из конечных authored sources/procedures: Apex catalysts и unstable components; горизонтальные Patterns и legendary-rule blueprints; редкая provenance/Trace; Embedded/Civic Legacy actions. Базовый build/sustain не запирается за T4 или weekly. Лучшее снаряжение покупает repeatability и coverage задач, но не право входа, иммунитет или универсальный DPS.

Reward budget конечен на `SessionID`/`Revision`, источники exactly-once. Бесконечные волны не печатают валюту и ценный per-kill loot. Transfer player gear не является новой эмиссией, но уменьшает sink и потому измеряется отдельно. T4-находки несут weight, custody, Dissonance и stabilization cost: это большая ценность на decision/slot, а не бесплатный рост каждого билда. Welfare/cheap gear может победить, но не должен стабильно добывать глубокий outcome. T3 остаётся полным устойчивым основным циклом; Apex доброволен и никогда не обязателен для baseline power.

## Смысл за пределами добычи

| Слой | Доставляемый смысл | Ограничитель |
|---|---|---|
| A. Physical stake | STANDARD: full Dawn return Пешки и custody; RECOVERY: только recovered Pawn | только физически удерживаемое STANDARD на Dawn; Recovery cargo не возвращается |
| B. Mastery proof | доказательство Apex-family без stat/streak buff | не вертикальная сила |
| C. Identity | Chronicle fact `DAWN_SURVIVED` | не четвёртый tag и не inherited power |
| D. World authorship | committed actions меняют Stable snapshot/address/problem | один игрок не может проиграть всем |
| E. Social story | условная кооперация, предательство, помощь | нет last-hit ownership |
| F. Horizontal breadth | новые Patterns, Trace, legacy-пути | не обязательный baseline |

`First Return` следует обобщить в `FIRST_FULL_RETURN_COMPLETED`: `NORMAL_THRESHOLD` или `DAWN` раскрывает заранее фиксированный `TagID`; поведение T4 не выбирает tag. Recovery/Breakline ничего не раскрывают. `LifeClosure` может принять authored `DAWN_RETURN`, после чего действует тот же необратимый выбор `CLOSED_CIVIC` или `RETURN_TO_FIELD`, без наследуемой силы. `Last Thread` не переименовывается и не смешивается с Dawn.

## Продуктовая модель при закрытой текущей power ladder

Четыре связанных loop:

1. **Session loop:** исследовать, нести, решить выйти или пережить Apex; STANDARD возвращается физически с custody, RECOVERY завершает отдельную судьбу без cargo.
2. **Pawn/Chronicle loop:** сохранять Пешку, фиксировать факты, осваивать family без бесконечного вертикального роста.
3. **World/Stable loop:** совершать committed actions, видеть следующий Stable snapshot и новые адреса проблем.
4. **Long-term/season loop:** возвращаться за breadth, mastery и разворачивающимися историями, не за обязательной ежедневной силой.

Content flywheel состоит из новых Apex families, совместимых sector/mutation compositions, Stable legacy outcomes и Chronicle/closure patterns. Один общий runtime и curated compatibility matrix важнее случайной комбинаторики. Старые главы и режимы остаются доступными или возвращаемыми; daily, streak и FOMO не являются удерживающим контрактом. Личная Archive chapter может прогрессировать в общем T4 и не создаёт отдельную очередь.

> [!note] PRODUCT HYPOTHESIS
> Рекомендуемая гипотеза: buy-to-play, бесплатные shared gameplay/Apex updates, постоянные optional cosmetic/supporter/archive-presentation packs. Крупные сюжетно-визуальные дополнения допустимы только если базовый Apex runtime и matchmaking не paywall. Коммерческая модель независима от gameplay ADR; нужны budget, CAC и retention данные, и это не финансовое решение.

Запрещено продавать T4 entry, ticket, Dawn insurance, extra Last Thread/life, loot multiplier, gear/stat, progression skip, camouflage или audio advantage, paid priority, mandatory battle pass и expiring power. Premium stash capacity конфликтует с extraction economy/P2W и должна быть удалена либо отдельно переоценена; вопрос премиальной валюты и площадки остаётся TBD в [[06_Economy_Loot/Economy_Core|Economy Core]]. Допустимы лишь readability-safe cosmetics: Chronicle covers/seals, profile/banner, Hub Table presentation, finishes оружия и gear при сохранённом silhouette. Это примеры класса, не обещание каталога.

## Population и сервисная реальность

При текущем 2-hour rolling cadence T3 staging и sealed T4 чередуются; joinable high-end window может отсутствовать до часа. Нельзя молча обещать одновременно joinable T1/T2/T3 и sealed T4 в прежних трёх service envelopes. T4 не становится отдельной queue: Hub показывает следующий Apex/staging; scheduler funnel-ит entrants в minimum late cohorts и дублирует только по capacity/demand. Always-on joinable T3 потребует дополнительной concurrency и может размыть PvPvE — это PRODUCT/OPS UNKNOWN, который надо измерить до SLA. Нет UTC appointment: rolling forecast и no daily bonus. Непостоянная T4-доступность терпима только потому, что Apex не производит baseline power.

## Отклонённые альтернативы и эксплуатационные риски

| Альтернатива / vector | Guardrail | Residual risk |
|---|---|---|
| Passive bunker + full manifest | мир разрушает static shelter, маршруты и позиции истощаются | bunker-геометрия потребует плейтестов |
| No manifest / DawnClaim | атомарный full return custody | риск высокий лишь пока T4 неопасен |
| Partial return / one slot | запрещён partial и protected slot | попытки laundering через custody graph |
| Per-kill wave loot | finite exactly-once authored budget | неверная source-разметка |
| Realtime threat scaling после смертей | budget фиксирован на cohort_at_seal | off-peak баланс |
| Direct T4 queue / скрытая late entry | та же карта; ordinary quote показывает seal/cutoff; каждый commit остаётся obligation, covered demand — только TIMELY/ALLOCATED; если corridor не помещается — ingress close | confusion и фактическое принуждение при слишком позднем crossing |
| AoE+sustain mono-meta | две route families, movement/service/breach | один build может стать слишком широким |
| Long-session phase-surfer monopoly | cadence, finite budget, no baseline lock | population concentration |
| Squad multiplicative safety | solo complete route, diminishing returns | voice coordination всё ещё сильна |
| Alt/mule | custody, weight, Dissonance, no free auto-pickup | transfer/sink метрики |
| Last-hit claim | публичные действия не owned, нет winner slots | attribution UX |
| Exit camping / forced hour | точный seal, 04:45 warning, две egress families | реальный риск rage-quit |
| Disconnect shelter | тело остаётся в поле | техническая устойчивость сессии |
| T4→T4 snowball | нет entry-right/иммунитета, finite budget | mastery может усилить повторяемость |
| Appointment FOMO | rolling forecast, no daily/streak | социальное давление расписаний |

Exit camping/forced hour не объявляется закрытой проблемой. Если тесты покажут rage-quit, увеличивать forecast или last-egress window, а не добавлять безопасную кнопку после 05:00.

## Реализация, владельцы и drift канона

| Owner | Единственная ответственность |
|---|---|
| Extraction/Return resolver | `ReturnManifest`, exactly-one proof и committed delivery facts; не personal contract settlement |
| ExtractionSolvencyValidator | pre-seal Threshold witness и transition obligation; authoritative contract — RAID §12 |
| Inventory/Custody | ItemID eligibility и полный custody graph |
| ServerLifecycle | total order Seal/Dawn keys, ingress close |
| Pawn Lifecycle/Presence | physical Presence, body state и lethal terminal event |
| LifecycleResolver | per-STANDARD-Presence `DawnSettlementDecision` и CARE/HUB projection |
| RecoveryResolutionResolver | RECOVERY `RECOVERED|FAILED|EXPIRED`, включая Dawn; manifest authority отсутствует |
| Mission/Pledge | personal contract settlement по declared trigger policy; не item delivery |
| ApexDirector | family, pressure, routes, world rules |
| Legacy resolver | Stable outcome |
| Chronicle | факты `DAWN_SURVIVED`, First Return, closure |

Ожидаемый canon drift, который эта proposal **не мигрирует**: [[01_Core_Vision/02_Core_Loop|Core Loop]], [[08_World_Generation/Generation/07_Server_Lifecycle|Server Lifecycle]], [[08_World_Generation/Generation/06_Async_Timers|Async Timers]], [[08_World_Generation/Generation/08_Gate_Check|Gate Check]], [[08_World_Generation/Anomaly/14_Extraction_System|Extraction System]], [[06_Economy_Loot/Extraction_Stabilization_Loop|Extraction Stabilization Loop]], [[06_Economy_Loot/Loot_Distribution|Loot Distribution]], [[07_Gear_Inventory/Gear_Progression|Gear Progression]], [[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]], [[RAID_INGRESS_EGRESS_ARCHITECTURE_SPEC|Raid Ingress/Egress Architecture]], [[BUILDCRAFT_ARCHITECTURE_SPEC|Buildcraft Architecture]] и [[07_Gear_Inventory/Stash_Architecture|Stash Architecture]] (monetization conflict).

## MVP, телеметрия и stop/go

MVP: один sector/revision, одна Apex Siege family, fixed finite loot budget, STANDARD full Dawn return и RECOVERY no-manifest branch, solo+trio tests; без season/meta monetization implementation. Exact rates и внутренние таймеры часа — **INSUFFICIENT DATA**.

Телеметрия: stay/exit по carried value; `pD` solo/duo/trio; bunker dwell/movement; meaningful-decision gaps; AoE dependency; 60-minute quit/disconnect; economic injection/destruction на player-hour; Threshold vs Dawn EV; phase-surfer/direct entrant; cooperation/betrayal; comprehension; off-peak cohort; server concurrency cost; корректность First Return/closure/Last Thread.

Stop/go: static shelter не переживает час; один build не решает режим; T3 остаётся рационален; full manifest не доминирует выбор; существует >0 solo path; нет infinite farm; UI понятен до seal.

## Исследовательские ориентиры

Это аналогии, а не доказательство и не шаблоны для копирования в Eldraine. [Deep Rock Galactic Deep Dives](https://store.steampowered.com/news/posts/?appids=548430&enddate=1570623404&feed=steam_community_announcements) указывает на reuse/mastery без T5; [DRG Season Selection](https://store.steampowered.com/news/posts/?appids=548430&enddate=1718363790&feed=steam_community_announcements) — на возвращаемые старые сезоны без обязательного queue split. [Warframe Steel Path](https://www.warframe.com/en/news/the-steel-path) полезен как аналог добровольного повышенного вызова, но не как модель power escalation. [Helldivers 2](https://www.playstation.com/en-us/games/helldivers-2/) — ориентир для ощущения shared world impact. [ARC Raiders Expedition Project](https://arcraiders.com/news/expedition-project) и [feedback update](https://arcraiders.com/news/a-triumphant-exit) — материал для наблюдения за voluntary closure и extraction-ставкой без наследуемой силы. [Sea of Thieves Pirate Emporium](https://www.seaofthieves.com/news/pirate-emporium) — ориентир для cosmetics-not-power. Применимый вывод ограничен: мастерство, общий мир, доступность старого контента, добровольное закрытие и косметика без силы могут сосуществовать; конкретные модели нельзя переносить целиком.

## Раздельные решения

### ADR-G1 — Gameplay

**ADOPT:** тот же `SessionID`, seal 05:00, active Apex, Dawn 06:00, STANDARD full physical return и RECOVERY-only resolution.

**REJECT:** queue/ticket, no-cargo, partial return, per-kill emission, death scale-down и safe disconnect.

### ADR-P1 — Progression boundary

**CURRENT AUTHOR CONSTRAINT + structural proposal:** `T3` завершает current baseline power, Apex не является gear tier или power gate. Отсутствие будущего `T5` — product empirical bet, а не вечный факт.

### ADR-C1 — Commercial hypothesis

**PRODUCT HYPOTHESIS:** buy-to-play/free shared gameplay/cosmetics. Её отклонение не отменяет G1/P1. Независимые invariants: нельзя продавать Apex access, power, Dawn insurance или делить matchmaking paywall.

### Open empirical unknowns

- Какая форма `f(N_seal)` сохраняет solo path без ослабления мира после смертей.
- Какие route families читаются за foretell и не сводятся к AoE+sustain.
- Какой forecast/egress window снижает forced-hour rage-quit без safe exit после seal.
- Каковы off-peak cohort, concurrency cost и допустимая частота staging.
- Каковы реальные `pE`, `pD`, sink и economic injection при STANDARD full Dawn manifest.
- Каковы retention и content cadence без `T5`.

### Acceptance checklist

- [ ] В 04:00 UI показывает family/signature; в 04:45 — обязательный foretell.
- [ ] До seal каждый Breach `COMMIT` остаётся в normal-egress obligation ledger; stay/quote/foretell не меняют state, а только server-proven missed latest-start снимает formula coverage и переводит obligation в surplus-only BEST_EFFORT.
- [ ] Bundle retires only at seal: lower-key exits succeed; same/higher-key Threshold/Breakline/ingress abort; только remaining/unresolved тела и custody остаются в поле.
- [ ] Dawn никогда не считается supply.
- [ ] STANDARD Dawn сначала имеет PREPARED_DURABLE manifest, затем один DawnSettlementDecision и derived manifest COMMIT с одним trigger proof; RECOVERY Dawn никогда не создаёт manifest/cargo/standard reward.
- [ ] Breakline доступен только STANDARD до seal; RECOVERY не может оставить Case без Presence через body-only exit.
- [ ] KIA/collapse на одинаковом key побеждает Dawn survival; для Recovery также побеждает absolute Case expiry, а success пишет один `RecoveryResolution=RECOVERED`.
- [ ] Solo и trio имеют жизнеспособные, но не одинаково безопасные пути.
- [ ] Нет статичного убежища, бесконечной эмиссии и обязательной T4-силы.
- [ ] Контракты явно различают `BEFORE_SEAL`, `NORMAL_THRESHOLD_ONLY` и Dawn-eligible.
- [ ] Сервисный UI не обещает постоянный T4 и не создаёт UTC/FOMO appointment.
