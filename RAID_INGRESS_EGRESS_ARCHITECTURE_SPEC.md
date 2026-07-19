---
title: Архитектура живого входа, фазовой непрерывности и выхода
aliases:
  - Raid Ingress Egress Architecture Spec
type: architecture_spec
status: proposed
canonical: false
date: 2026-07-19
system: raid_ingress_egress
scope:
  - live_expedition
  - ingress
  - rolling_pool
  - phase_continuity
  - egress
  - recovery
tags:
  - architecture
  - extraction-fps
  - live-session
  - ingress-egress
---

# Архитектура живого входа, фазовой непрерывности и выхода

> [!important] Статус
> Это proposal, а не канон. Живой канон пока противоречит решению; ни один новый термин не становится каноническим до миграции профильных страниц. Документ задаёт implementation-neutral контракт и не утверждает, что каноническая миграция выполнена.

## 1. Вердикт, оценки и ADR

### 1.1. Вердикт

Текущий канон — **CONTRADICTORY**. [[08_World_Generation/Generation/19_Access_Contracts|Access Contracts]] смешивает фазу, маршрут, цену, место и readiness; Tier превращён в билет. Старое описание входа использует Саркофаг, Wake Up и invulnerability; Blackout отбирает управление и переносит Пешку в укрытие. Safe Door Frame/комнаты, универсальная транспортная причинность и [[08_World_Generation/Anomaly/15_Frequency_Tuner|Trace redeploy]] конфликтуют с живой асинхронной сессией.

После hardening целевая архитектура — **COHERENT** и implementation-neutral **REALIZABLE**. Её контракты допускают co-located transaction либо durable coordinator с идемпотентными проекциями, но не зависят от конкретной базы данных, сетевого стека или engine API.

| Оценка | Значение | Что оценивается |
|---|---:|---|
| Current architecture quality | 3/10 | Состояние действующего канона. |
| Architectural coherence of proposal | 8.5/10 | Целостность proposal после hardening. |
| Implementation-contract completeness | Contract-complete proposal | Владельцы, состояния, fences и failure outcomes определены; production readiness не заявляется. |
| Canonical completeness | 1/10 | Решения ещё не перенесены в профильный канон. |
| Empirical confidence | 5/10 | Коридоры времени, нагрузки и читаемости ещё требуют тестов. |

Оценки не усредняются: качество целевой архитектуры, полнота канона и эмпирическая уверенность отвечают на разные вопросы.

### 1.2. ADR: rolling live pool

**Решение:** rolling live pool — **AUTHOR CONSTRAINT**.

**Причина:** closed-round matchmaking уничтожает четыре обещания системы: direct entry в текущую фазу; same-Pawn survival через фазовый сдвиг; public Recovery внутри обычного PvPvE-мира; шестичасовую причинность living world. Сложность rolling pool оправдывается этими авторскими обещаниями, а не сравнением с конкурентами.

**Следствие:** SessionID живёт непрерывно до Final Stabilization; player entry, phase mutation, Recovery и egress подчиняются одному server total order. Нельзя возвращать Access Contract/ticket authority, safe spawn, invulnerability, отдельные комнаты, universal transport prop, relocation, partial manifest или survivor time buff.

## 2. Player promise и фазовая идентичность

Главное обещание: **неизвестный мир — известный себе персонаж**. Точные seed, маршруты, противники, кандидаты входа и Пороги неизвестны. Игрок знает правила, состояние тела и снаряжения, фазовый clock, заявленный route debt, concrete route commitment, возможную потерю и человеческую причину отказа.

Concrete economic commitment принадлежит [[07_Gear_Inventory/Inventory_Architecture|Inventory/Custody]] либо [[03_Factions_Societies/Pledge_Contracts|Pledge]]. Он immutable, lock до deployment confirmation, consume только при Breach `decision=COMMIT`, release/refund exactly once до него. Ownerless access fee/price не существует.

Каждый `SessionID` живёт ровно шесть часов:

| Derived phase band | Время | Игровая идентичность |
|---|---|---|
| Manifestation | 00:00–02:00 | Learn/read/prepare; не tutorial и не easy queue. |
| Memory | 02:00–04:00 | Exploit and contest remembered catastrophe/prepared infrastructure. |
| Reassembly | 04:00–06:00 | Combine/cash out under terminal clock. |
| Final Stabilization | 06:00 | Terminal event; следующей playable phase нет. |

[[08_World_Generation/Generation/07_Server_Lifecycle|Server Lifecycle]] derives phase band from elapsed session clock и владеет monotonic `PhaseRevision` конкретного committed world state. Scheduler не хранит ни phase band, ни PhaseRevision. T1/T2/T3 — derived age/world states, а не buckets, доступ, рейтинг или товар. В 06:00 вся Пешка без завершённого выхода получает KIA; награды «дожил» нет.

Direct entrant имеет полноценную objective→risk→Threshold→aftermath петлю в каждом phase band. Mandatory objective, main reward и exit не требуют previous Knowledge, World mutation, pre-shift item или survived gate.

## 3. Владельцы и запрет параллельной authority

| Owner | Authority |
|---|---|
| ServerLifecycle | SessionID, elapsed clock, PhaseRevision, barriers, Final Stabilization, arbitration key |
| Regional scheduler | service set, hosting, capacity/latency policy, LowPopulationPolicy |
| Session Boundary Graph | hidden IngressOpportunity и public-search ThresholdOpportunity |
| ApproachOfferResolver | target-independent offer terms, OfferTermsHash и StickyTargetScopeID |
| TargetBindingResolver | hidden target, TargetEpoch, disclosure, stickiness и expiry |
| EntryQuoteResolver | immutable target-bound EntryQuote facts |
| TargetAvailabilityResolver | GlobalTargetUnusableCertificate и глобальная unusability target |
| AdministrativeResolutionResolver | finite post-disclosure technical resolution |
| InsertionAdmissionResolver | AdmissionHold facts и admission fence |
| InsertionBreachCoordinator | candidate revalidation, IngressPressureField и один durable BreachTransaction decision |
| StaticRevisionValidator | StaticRevisionVariantCertificate и matching static bundle |
| ExtractionSolvencyValidator | StaticEgressSupplyEnvelopeCertificate, EgressSolvencyBundle и global witness |
| Gate Check | envelope/current environment forecast и phase pulse |
| Dissonance | self Dissonance result и собственный budget |
| Account Lifecycle | `UNIQUE_ACTIVE_RAID_CONTROLLER(AccountID)` через AccountDeploymentLease |
| Pawn Lifecycle/Presence | одна физическая Пешка, Presence epoch и terminal removal |
| ParticipationLedger | one AccountID×SessionID и STANDARD/RECOVERY kind |
| ContinuityRootRegistry | immutable ContinuityBudgetRootID и root owner record |
| ContinuityAxisValidator | authoring proof для semantic root combinations |
| RaidKnowledgeLedger | session-local KnowledgeClaim/SearchEvidence |
| SessionWorldState/entity | public world mutation |
| Inventory/Custody | ItemID/LivingCargo, custody и concrete inventory commitment |
| Mission/Pledge | objective/reward и pledge commitment; не continuity mint |
| Extraction resolver | SyncLease decision и ProtectedManifest transaction |
| Lifecycle/Recovery | RecoveryCase и existing AccountLifecycle.account_last_thread_slot |
| RecoveryResolutionResolver | один durable RecoveryResolutionTransaction decision |
| Operations/anti-cheat | association policy, federation eligibility, residual abuse audit |
| UI projection | human state/reason/deadline/loss/action; backend authority отсутствует |

Один результат имеет одного decision owner. Прочие системы поставляют facts, fences или идемпотентные projections по durable decision reference; они не принимают второе решение.

## 4. Rolling pool и LowPopulationPolicy

### 4.1. Public не означает populated

`public standard session` означает обычный globally joinable standard pool. Это не обещание, что в конкретный момент рядом существует противник. `populated` — наблюдаемое server-side состояние активности, не product promise и не UI-поле.

Минимальный regional service set сохраняет один serviceable SessionID каждого envelope: 0–2, 2–4 и 4–6. Duplicates создаются только по demand/capacity. Suppression, отказ кандидатов или Recovery никогда не создают shard.

```yaml
SessionServiceSnapshot:
  owner: RegionalScheduler
  source: lifecycle_health_capacity_static_bundle_and_dynamic_solvency_views
  snapshot_id: opaque
  session_id: opaque
  activity_state: SEEDING|CONTESTABLE
  admission_state: OPEN|SATURATED|DRAINING|CLOSED
  health_ref: required
  capacity_ref: required
  matching_static_revision_variant_certificate_ref: required
  current_egress_solvency_bundle_ref: required
  can_publish_ingress_ref: derived_output_only
  observed_at: timestamp
  lifecycle: replaced_by_newer_snapshot_until_FinalStabilization_then_CLOSED
```

`activity_state` и `admission_state` orthogonal. `SEEDING` — ordinary standard session, способная принять первого normal player; Recovery её не seed. `CONTESTABLE` означает server-confirmed ordinary activity, но не обещает nearby enemy. Admission state имеет total transitions:

| Trigger | From → To | Rule |
|---|---|---|
| Healthy live lifecycle + capacity + matching publication bundle | CLOSED/SATURATED → OPEN | Только до Final Stabilization и при valid dynamic solvency. |
| Capacity exhausted | OPEN → SATURATED | Existing bodies и clock не меняются. |
| Capacity returns and policy still serves session | SATURATED → OPEN | Новый snapshot; target stickiness rules сохраняются. |
| Low-pop collapse selects duplicate for drain | OPEN/SATURATED → DRAINING | Новые Binding/Quote запрещены. |
| Final Stabilization, terminal failure or service removal with no further intake | any → CLOSED | Existing terminal processing follows ServerLifecycle. |
| Ordinary first activity | SEEDING → CONTESTABLE | Recovery не может вызвать transition. |

```text
BaseAdmissionServiceable(session, composition)
= LifecycleLive(session)
AND HealthOK(session)
AND AdmissionState(session) == OPEN
AND CapacityAllows(session, composition)
AND MatchingStaticPublicationBundleValid(session, candidate_revision, composition)
```

`BaseAdmissionServiceable` не читает `CanPublishIngress`. `CanPublishIngress` ниже добавляет dynamic objective/path/search/time/solvency facts к этой базе; cycle отсутствует. `can_publish_ingress_ref` — только derived output snapshot, не input.

Символические predicates — нормативные interfaces. Их числовые коридоры являются эмпирическими inputs.

### 4.2. Fixed collapse order

При падении population/capacity scheduler применяет порядок без перестановки:

1. Backfill healthy `BaseAdmissionServiceable` already-live SessionID.
2. Stop creating duplicates.
3. Перевести duplicates в `DRAINING`: existing bodies остаются, обычный clock продолжается, новые Binding/Quote не выдаются.
4. Remove event/overflow sessions из нового admission.
5. Reduce sector breadth, сохраняя три envelopes.
6. Использовать latency-compatible federation только для новых unbound requests.
7. Mark конкретный envelope unavailable; never silently substitute другой envelope.

Existing bodies никогда не перемещаются. Session clocks не reset, не merge и не перепривязываются. Federation не меняет target после durable disclosure и не является способом клиентского shopping. Raw population, state name и collapse step UI не показывает.

Для `DRAINING`: pre-disclosure request получает единственный allowed opaque rebind к equivalent `OPEN` target либо generic failure; disclosed binding остаётся same-target и проходит finite AdministrativeResolution. Collapse не отменяет durable receipt и не retargets client.

```yaml
SessionCohort:
  owner: RegionalScheduler
  source: regional_service_policy
  cohort_id: opaque
  region: required
  started_at: timestamp
  session_ids: [opaque]
  policy_refs: required
  lifecycle: active_until_all_member_sessions_terminal
```

## 5. Target-independent ApproachOffer

Игрок выбирает один из 1–3 текущих **Подходов**. Player-facing backend entity — `ApproachOffer`; она target-independent и не резервирует SessionID, seat, candidate, gear или commitment. Все offers одного `AccountID либо sealed-party + sector + phase-envelope + regional-service-epoch` делят server-owned `StickyTargetScopeID`.

```yaml
StickyTargetScope:
  owner: TargetBindingResolver
  source: account_or_sealed_party_sector_envelope_and_service_epoch
  sticky_target_scope_id: opaque
  original_account_ids: required
  sealed_roster_hash: required_for_party
  sector_id: required
  phase_envelope: required
  regional_service_epoch: required
  bound_target_ref: optional_until_first_disclosure
  state: UNBOUND|TARGET_STICKY|DECLINED_STICKY|CONFLICT|EXPIRED|GLOBAL_RELEASED
  sticky_expires_at: timestamp
  lifecycle: survives_offer_change_client_restart_party_disband_and_reassembly
```

```yaml
ApproachOffer:
  owner: ApproachOfferResolver
  source: sector_envelope_policy_plus_self_and_party_snapshot
  offer_id: opaque
  sticky_target_scope_id: required
  offer_terms_hash: OfferTermsHash
  sector_id: required
  phase_envelope: required
  public_clock_bounds: required
  envelope_forecast_ref: required
  self_dissonance_result_ref: required
  party_composition_ref: required
  approach_profile_ref: required
  declared_route_debt: required
  concrete_route_commitment_ref: optional
  commitment_refund_policy_ref: required
  tell_exposure_class: required
  objective_exclusions: required
  conservative_commit_cutoff: timestamp
  eligible_target_equivalence_class_ref: hidden
  state: OPEN|SELECTED|SUPERSEDED|EXPIRED
  lifecycle: selected_or_expired_without_target_reservation
```

Каждый из 1–3 offers имеет собственные `OfferID` и `OfferTermsHash`, но общий `StickyTargetScopeID`. `OfferTermsHash` MUST быть идентичен для всех eligible targets equivalence class конкретного offer. Изменение любого player-relevant поля создаёт другой hash и требует reconfirm; silent substitution запрещена.

До target stickiness запрещено выдавать exact SessionID/seed/pop/server, exact target clock/environment/geometry/anchor/candidate, target-specific response size/order/reason/timing или любой иной fingerprint. Opaque rebind count, reason, latency и payload ordering не observable. Client получает только final target-bound quote либо generic preflight failure.

Каждый open offer имеет credential-free baseline для каждого supported party size/composition. Credentialed approach несёт минимум одну player-relevant same-raid nonfungible liability. Upfront wealth/rarity и ненужная group capacity не являются tradeoff. Credential не покупает phase, seat, допустимое пересечение, objective, reward или exit. Pareto invariant запрещает approach одновременно превосходить baseline по time, noise, exposure, capacity, commitment/debt и objective proximity.

Mission/Pledge выбирается отдельно и не создаёт route. `late-phase authored mission overlay` не создаёт и не продлевает ingress, seat, quote, Threshold или final deadline.

## 6. Hidden target, disclosure и exact EntryQuote

### 6.1. Total flow

```text
HUB_PLANNING
→ APPROACH_OFFER_SELECTED
→ OPAQUE_TARGET_PREFLIGHT
→ optional exactly-one silent OPAQUE_REBIND before target-tainted output
→ one durable all-or-none multi-account DISCLOSURE_RECEIPT transaction + TARGET_STICKY
→ exact target-bound ENTRY_QUOTE_ISSUED
→ PLAYER_CONFIRMED
→ CONTENT_DISCLOSED/STAGING
→ CLIENT_WORLD_READY
→ ADMISSION_HELD
→ CANDIDATE_ASSIGNED
→ BREACH_PREPARED
→ BREACH_COMMITTED
→ ACTIVE_PARTICIPATION
```

`IngressOpportunity` остаётся hidden, exact SessionID+PhaseRevision bound и не является Подходом.

```yaml
IngressOpportunity:
  owner: SessionBoundaryGraph
  source: published_revision_boundary_set
  ingress_opportunity_id: opaque
  session_id: opaque
  phase_revision: integer
  boundary_family_id: opaque
  availability: OPEN|CLOSING|CLOSED
  valid_until: timestamp
  supported_party_compositions: required
  candidate_cell_set_ref: hidden
  runtime_veto_policy_ref: required
  opportunity_revision: integer
  lifecycle: published_until_close_expiry_or_revision_barrier
```

### 6.2. TargetBinding и DisclosureReceipt

Любой datum, из которого можно реконструировать target, — `TARGET_TAINTED`. TargetBindingResolver атомарно пишет durable receipts для всего sealed roster и делает scope sticky **до** отправки первого target-tainted byte/key/payload. First party disclosure — один multi-account CAS: receipts создаются all-or-none, roster после этого sealed.

```yaml
TargetBinding:
  owner: TargetBindingResolver
  source: opaque_preflight_selection
  binding_id: opaque
  sticky_target_scope_id: required
  offer_terms_hash: required
  sealed_roster_hash: required
  target_epoch: integer
  hidden_session_id: opaque
  state: OPAQUE_PREFLIGHT|TARGET_STICKY|QUOTE_ISSUED|PLAYER_CONFIRMED|COMMITTED|EXPIRED|ADMIN_RESOLUTION|RELEASED
  opaque_rebind_count: 0|1
  sticky_expires_at: timestamp
  disclosure_receipt_refs: required_before_tainted_output
  release_transaction_ref: optional
  lifecycle: one_active_nonterminal_binding_per_AccountID_across_pool

DisclosureReceipt:
  owner: TargetBindingResolver
  source: atomic_target_disclosure_transaction
  receipt_id: opaque
  original_account_id: required
  sealed_roster_hash_at_disclosure: required
  sticky_target_scope_id: required
  binding_id: required
  target_epoch: required
  disclosed_offer_terms_hash: required
  disclosed_at: timestamp
  sticky_expires_at: timestamp
  holds_seat_candidate_gear_or_commitment: false
  state: ACTIVE|EXPIRED|CONSUMED_BY_COMMIT|GLOBAL_RELEASED
  lifecycle: persists_for_original_account_after_party_disband_or_reassembly
```

До target-tainted output допускается exactly-one silent `OPAQUE_REBIND` к equivalent already-live target. Любой internal quote прежнего target superseded и никогда не показывается. Disclosure любого offer binds target для **всех** offers общего scope. Смена approach создаёт новый exact quote того же target, если target совместим; иначе offer помечается unavailable без reroll.

Client restart, party disband/reassembly и смена offer не сбрасывают scope/receipt. Clean members могут присоединиться к уже известному target только если target/offer valid для всего нового sealed roster и receipts для всех members записаны all-or-none **до** tainted output. Conflicting active receipts одного scope, указывающие разные targets, дают `STICKY_TARGET_CONFLICT`: участники ждут expiry либо durable global release; никто не retargets.

Decline exact target terms даёт explicit `TARGET_STICKY_DECLINED`: Binding становится `RELEASED`, seat/candidate/gear/commitment освобождены, но receipts и scope остаются sticky до expiry/global release.

### 6.3. Exact EntryQuote

```yaml
EntryQuote:
  owner: EntryQuoteResolver
  source: final_sticky_target_plus_current_authoritative_snapshots
  entry_quote_id: opaque
  binding_id: required
  target_epoch: required
  session_id: required
  phase_revision: required
  ingress_opportunity_id: required
  opportunity_revision: required
  offer_terms_hash: required
  account_id: required
  pawn_id: required
  squad_snapshot_ref: required
  loadout_snapshot_ref: required
  exact_current_environment_ref: required
  exact_next_environment_ref: required
  dissonance_result_ref: required
  declared_route_debt: required
  concrete_route_commitment_ref: optional
  exact_loss_state: required
  time_to_shift: required
  time_to_final: required
  expires_at: timestamp
  commit_cutoff_at: timestamp
  state: ISSUED|PLAYER_CONFIRMED|CLOSING|CONSUMED_BY_BREACH|EXPIRED|ROLLED_BACK
  immutable: true
  lifecycle: exactly_one_sticky_target_never_survives_rebind
```

Exact target terms показываются до economic/deployment confirmation. Quote относится ровно к одному BindingID+TargetEpoch+IngressOpportunity и никогда не переживает rebind либо Resume. `RESUME_SAME_TARGET` supersedes old Quote и создаёт новый immutable Quote того же BindingID+TargetEpoch. До player confirmation concrete commitment может быть представлен, но не consumed. Если `OfferTermsHash` изменился, возвращается новый ApproachOffer и требуется явный reconfirm.

### 6.4. Total lifecycle table

| Event | TargetBinding | DisclosureReceipt/Scope | EntryQuote | AdministrativeResolution |
|---|---|---|---|---|
| Opaque target selected | OPAQUE_PREFLIGHT | Scope UNBOUND; no receipt | Internal candidate only, never shown | Absent |
| First target-tainted output | TARGET_STICKY | All-or-none receipts ACTIVE; scope TARGET_STICKY | Exact immutable ISSUED | Absent |
| Player confirms | PLAYER_CONFIRMED | Unchanged | PLAYER_CONFIRMED | Absent |
| Player declines | RELEASED | Receipt ACTIVE; scope DECLINED_STICKY | ROLLED_BACK | Absent |
| No valid crossing/technical failure after disclosure | ADMIN_RESOLUTION | Receipt ACTIVE | EXPIRED/ROLLED_BACK | OPEN→RESOLVING |
| Resume same target | TARGET_STICKY | Receipt ACTIVE | Old superseded; new immutable Quote same BindingID+TargetEpoch | RESUME_SAME_TARGET terminal |
| Withdraw/fail-refund | RELEASED | Receipt ACTIVE until sticky expiry/global release | ROLLED_BACK | WITHDRAWN_STICKY/FAIL_REFUND terminal |
| Global target unusable | RELEASED | GLOBAL_RELEASED only by durable certificate transaction | ROLLED_BACK | SYSTEM_TERMINAL_FAILURE + retarget authorization |
| Breach COMMIT | COMMITTED | CONSUMED_BY_COMMIT | CONSUMED_BY_BREACH | Absent/terminal |

```yaml
GlobalTargetUnusableCertificate:
  owner: TargetAvailabilityResolver
  source: authoritative_global_target_lifecycle_and_service_failure
  certificate_id: opaque
  session_id: required
  target_epoch: required
  reason: SESSION_TERMINAL|GLOBAL_SERVICE_FAILURE|REVISION_PERMANENTLY_UNUSABLE
  decision_key: arbitration_key
  input_hash: required
  state: ISSUED|CONSUMED_FOR_GLOBAL_RELEASE
  lifecycle: immutable_durable_authorization_for_retarget_only
```

## 7. CanPublishIngress и AdmissionHold

```text
CanPublishIngress(session, composition, now)
= BaseAdmissionServiceable(session, composition)
AND unexhausted baseline objective/reward family exists
AND ordinary reachable route and Threshold search path exist
AND matching StaticRevisionVariantCertificate exists
AND current global EgressSolvencyBundle covers ActiveCommitted + ProspectiveBreachGroup
AND now + p95_offer_binding_commit
        + minimum_field_agency_window
        + minimum_threshold_search_budget
        + required_sync_duration
        + server_margin
    < FinalStabilization
```

Правило вычисляется per selected supported party composition. Все durations — calibrated empirical inputs; само неравенство нормативно. Рядом с 02:00/04:00 offer показывает envelope current+next forecast и conservative cutoff, а exact quote — target current+next Environment и exact cutoff. Вход до boundary допустим, но не создаёт automatic continuity.

```yaml
AdmissionHold:
  owner: InsertionAdmissionResolver
  source: player_confirmed_quote_plus_client_world_ready
  hold_id: opaque
  binding_id: required
  entry_quote_id: required
  session_id: required
  phase_revision: required
  ingress_opportunity_id: required
  account_and_squad_snapshot_ref: required
  expires_at: timestamp
  state: HELD|CONSUMED_BY_BREACH|RELEASED|EXPIRED
  renewable: false
  cardinality: one_outstanding_per_account_across_pool
  lifecycle: short_lived_after_client_ready
```

AdmissionHold не является body, Presence, ParticipationClaim или entitlement. Он резервирует admission capacity только после client ready и освобождается при любом pre-decision abort.

## 8. Finite AdministrativeResolution

После durable disclosure нет бесконечного hold. Technical delay всегда имеет server-owned reason, deadline и finite terminal outcome.

```text
OPEN
→ RESOLVING
→ RESUME_SAME_TARGET
or WITHDRAWN_STICKY / FAIL_REFUND
or SYSTEM_TERMINAL_FAILURE
```

```yaml
AdministrativeResolution:
  owner: AdministrativeResolutionResolver
  source: post_disclosure_target_or_transport_failure
  resolution_id: opaque
  binding_id: required
  disclosure_receipt_refs: required
  reason: NO_VALID_CANDIDATE_AFTER_DISCLOSURE|TRANSIENT_TARGET_FAILURE|TRANSIENT_SERVER_FAILURE|STALE_OPPORTUNITY|LOST_CAPACITY|DISCONNECT
  opened_at: timestamp
  original_resolution_deadline: timestamp
  effective_deadline: min(original_resolution_deadline,sticky_expiry,phase_cutoff,FinalStabilization)
  phase_and_final_cutoff_ref: required
  resource_release_transaction_ref: required
  state: OPEN|RESOLVING|RESUME_SAME_TARGET|WITHDRAWN_STICKY|FAIL_REFUND|SYSTEM_TERMINAL_FAILURE
  global_target_unusable_certificate_ref: optional
  retarget_authorization: NONE|AUTHORIZED_BY_GLOBAL_TARGET_UNUSABLE_CERTIFICATE
  exact_once_refund_ref: required_for_terminal_failure
  lifecycle: finite_before_effective_deadline_which_never_resets
```

При открытии resolution seat/admission/candidate освобождаются немедленно; commitment не consumed. Gear/commitment lock releasable при withdrawal; DisclosureReceipt остаётся ACTIVE. `RESUME_SAME_TARGET` supersedes old Quote и выпускает новый immutable Quote того же BindingID+TargetEpoch. `WITHDRAWN_STICKY/FAIL_REFUND` releases Binding и возвращает игрока в Hub UI, но receipt/scope остаются sticky. `SYSTEM_TERMINAL_FAILURE` exact-once refunds и разрешает retarget только по durable `GlobalTargetUnusableCertificate`.

Effective deadline — минимум original resolution deadline, sticky expiry, phase cutoff и Final Stabilization; он никогда не resets при retry/Resume. Phase/final cutoff всегда побеждает SLA. SLA эмпирический, finite deadline обязательный. Admin failure не является KIA и не consumption ParticipationLedger. Игрок может покинуть modal UI; серверный resolution продолжается независимо от открытого экрана.

## 9. Durable BreachTransaction

### 9.1. Один authoritative decision record

Distributed atomicity реализуется одним durable decision record. Допустимы co-located transaction либо durable coordinator с idempotent projections. Несколько независимых owners не могут каждый решить commit/abort.

```text
PREPARING
→ PREPARED_DURABLE
→ immutable decision COMMIT or ABORT

projection_state:
NONE → APPLYING → MATERIALIZED
or NONE/APPLYING → ROLLED_BACK for decision ABORT
or APPLYING → QUARANTINED → replay toward the same immutable decision
```

```yaml
BreachTransaction:
  owner: InsertionBreachCoordinator
  source: player_confirmed_quote_hold_candidate_and_final_certificates
  breach_transaction_id: deterministic_hash(BindingID,TargetEpoch,sealed_roster_hash)
  binding_id: required
  target_epoch: required
  sealed_roster_hash: required
  entry_quote_refs: required_for_entire_squad
  admission_hold_refs: required_for_entire_squad
  candidate_assignment_ref: required
  static_revision_variant_certificate_ref: required
  final_egress_solvency_bundle_ref: required
  conditional_fence_refs:
    binding_idempotent_consume: required
    account_controller_unique: required_for_each_member
    pawn_presence_unique: required_for_each_member
    participation_unique: required_for_each_member
    commitment_lock: required_for_each_commitment
    seat_admission_candidate: required_for_each_member
  deterministic_body_ids: required
  deterministic_presence_ids: required
  deterministic_participation_claim_ids: required
  deterministic_tell_event_id: required
  deterministic_account_deployment_lease_ids: required
  commit_spatial_footprint_refs: required
  commitment_projection_refs: required
  seat_projection_refs: required
  preparation_state: PREPARING|PREPARED_DURABLE
  decision: UNDECIDED|COMMIT|ABORT
  projection_state: NONE|APPLYING|MATERIALIZED|ROLLED_BACK|QUARANTINED
  logical_effective_at: optional_until_decision
  decision_key: optional_arbitration_key_until_decided
  prepared_watchdog_deadline: required
  reconciliation_deadline: required
  lifecycle: one_transaction_and_one_decision_for_whole_squad
```

До immutable `decision=COMMIT` не существует visible body/hitbox/tell, active Presence/Claim, consumed commitment или logically occupied seat. Prepared tokens — только conditional fences; они не body, active seat, claim или tell. Любой member failure, rejected fence, stale certificate, phase/final cutoff либо client readiness loss до decision делает whole-party `ABORT` и exact-once refund.

`PREPARED_DURABLE` фиксирует deterministic IDs, footprints и valid conditional fence refs, но не делает projections видимыми. `COMMIT` допустим только если все fences принимаются одной authoritative decision transaction. Prepared watchdog не может пересечь commit fence `UNDECIDED`: coordinator пишет `ABORT` до fence либо `COMMIT` меньшим полным arbitration key.

При `decision=COMMIT` logical body, Presence, ParticipationClaim, AccountDeploymentLease, consumed stake, occupied seat и tell существуют в server total order на `logical_effective_at`, даже если projections ещё `APPLYING`. Pending commit footprints входят в phase occupancy snapshot. После COMMIT projections не могут reject или rollback: replay/reconciliation converges к тому же decision.

Replay применяет все later-key phase pulse, KIA и FinalStabilization к logical Presence. После 06:00 ACTIVE materialization запрещена: reconciliation материализует terminal outcome, а не живое тело. Disconnect после COMMIT всё равно materializes vulnerable logical body; reconnect возвращает control к той же Presence, если она не terminal. Первый exposed frame даёт full control. Squad имеет один decision; partial commit и replacement запрещены.

### 9.2. Presence, deployment и participation

```yaml
AccountDeploymentLease:
  owner: AccountLifecycle
  source: BreachTransaction_decision_COMMIT_projection
  account_id: required
  active_presence_ref: required
  acquire_transaction_ref: required
  release_transaction_ref: optional
  state: ACTIVE|RELEASED
  unique_constraint: UNIQUE_ACTIVE_RAID_CONTROLLER(AccountID)
  lifecycle: acquire_on_commit_release_exactly_once_on_terminal_removal

PawnPresenceLease:
  owner: PawnLifecycle
  source: BreachTransaction_decision_COMMIT_projection
  pawn_id: required
  presence_epoch: integer
  session_id: optional
  entity_id: optional
  state: HUB|RAID|CARE|TERMINAL
  unique_constraint: UNIQUE_ACTIVE(PawnID)
  lifecycle: active_until_terminal_removal_or_extraction_transition

ParticipationClaim:
  owner: ParticipationLedger
  source: BreachTransaction_decision_COMMIT_projection
  claim_id: deterministic
  kind: STANDARD|RECOVERY
  session_id: required
  account_id: required
  pawn_id: required
  presence_ref: required
  state: ACTIVE|TERMINAL_SUCCESS|TERMINAL_FAILED
  unique_constraint: one AccountID_x_SessionID
  lifecycle: consumed_once_never_reopened
```

Concurrent second AccountID commit loses before decision and before body/claim/commitment consumption. Normal Extraction, KIA, Breakline terminal exit, Recovery success/failure и иной terminal removal CAS-release AccountDeploymentLease exactly once. Disconnect его не освобождает.

## 10. IngressPressureField и spatial coverage

### 10.1. Identity-blind physical pressure

`IngressPressureField` заменяет identity-like binary grouping. Это continuous, monotone spatial-temporal decay field над фактическими `BreachCommitted` events.

```text
Pressure(x, t) = monotone_sum(over committed breach events e, SpatialKernel(x,e) * TemporalDecay(t,e))
```

Identical physical crossings создают identical combined audible/visual tell, hot-pipe heat и ordinary world/AI perception независимо от declared party, Account association или дружеского поведения. Field не меняет reward, hostility, knowledge, matchmaking, confirmed debt, commitment или character stats. Binary epsilon window отсутствует.

Staggering достаточно далеко разрешено, потому что платит time, separation и traversal. Random solos не получают abstract admission fee; их реальные crossing events физически складываются. Behavioral friendship detector запрещён.

### 10.2. StaticRevisionVariantCertificate

Static certificate создаётся per candidate `PhaseSpatialVariant + topology_hash + supported composition` до публикации. Bounds берутся из versioned `ControlProfileRegistry`, принадлежащего Combat, а не из invented weapon ranges этой системы.

```yaml
IngressCoverageSubproof:
  owner: StaticRevisionValidator
  source: candidate_cell_graph_plus_ControlProfileRegistry
  subproof_id: opaque
  candidate_cell_graph_ref: required
  effective_controller_token_model_ref: required
  control_horizon_ref: required
  min_credible_passive_suppression_cut: derived_first
  validation_result: VALID|INVALID
  lifecycle: immutable_part_of_matching_static_bundle

StaticRevisionVariantCertificate:
  owner: StaticRevisionValidator
  source: prevalidated_variant_topology_composition_bundle
  certificate_id: opaque
  candidate_phase_revision: required
  phase_spatial_variant_id: required
  topology_hash: required
  supported_composition_ref: required
  ingress_candidate_graph_ref: required
  threshold_family_graph_ref: required
  ControlProfileRegistry_version: required
  control_horizon_ref: required
  movement_and_intercept_bounds_ref: required
  persistent_device_and_channel_budget_ref: required
  JIT_activation_policy_ref: required
  ingress_coverage_subproof_ref: required
  static_egress_supply_envelope_certificate_ref: required
  continuity_axis_proof_ref: required
  min_bodies_to_control_all_threshold_families: derived
  controller_admission_cap: frozen_prepublication
  bundle_hash: required
  validation_result: VALID|INVALID
  lifecycle: immutable_for_candidate_revision_variant_and_topology_hash
```

`EffectiveControllerTokens` учитывает hostile body, remote observer, persistent trap/device и maintained control channel в пределах registry-defined control horizon. Account identity и declared party не меняют token count.

Сначала вычисляется suppression cut, затем frozen cap:

```text
controller_admission_cap
= min(engine_population_cap,
      MinCrediblePassiveSuppressionCut - 1,
      static_egress_admission_cap)
```

Population-wide invariant требует `MinCrediblePassiveSuppressionCut > controller_admission_cap`. Если текущие EffectiveControllerTokens превышают cap candidate variant, phase selection выбирает следующий matching fallback; existing bodies никогда не удаляются. Если ни один variant не проходит, применяется valid `NO_SPATIAL_DELTA` bundle либо candidate revision rejected до publication.

Runtime всё равно revalidates nav, hostile LoS/firing line, traps, projectiles, observers, aim/dwell/kill heat, active combat, objective/boss/vault/Foundling/apex skip, capacity и две independent cover-egress. `suppressed` означает aggregate failure хотя бы одного hard veto. Veto не ослабляется. Если все cells suppressed, commit невозможен и shard не создаётся: pre-disclosure допускается один silent equivalent opaque rebind; post-disclosure — finite same-target AdministrativeResolution.

Threshold subproof требует:

```text
MinBodiesToControlAll(ThresholdFamilies) > MaxSupportedSquad
```

Есть минимум две independent search families/routes; single key, edge, observer, device или channel не закрывает все. Минимум одна family сохраняет multiple latent anchors до server-confirmed evidence. Runtime exact anchor назначается durable JIT decision и не enumerable at phase start.

## 11. Phase boundary и geometry realizability

### 11.1. Phase transaction

```text
PHASE_WARNING
→ REVISION_CLOSING
→ COMMIT_FENCE
→ PHASE_BARRIER_DECISION_KEY occupancy snapshot
→ choose matching prevalidated variant bundle + global dynamic solvency
→ atomic PhaseRevision + variant + bundle
→ boundary/search sets → SessionServiceSnapshot → ApproachOffers
```

`PHASE_WARNING` — physical precursor + nonmodal UI forecast. `REVISION_CLOSING` прекращает выдачу quotes/SyncLeases, которые не помещаются до barrier. На fence BreachTransaction принимает decision меньшим key либо ABORT. Snapshot снимается на exact `PHASE_BARRIER_DECISION_KEY` после всех lower-key movement/world events и включает active Presence и COMMIT-but-unprojected spatial footprints.

Arbitration key — `(server_tick,event_priority,sequence)`; равных order нет. При одном server tick FinalStabilization/KIA имеют priority раньше ExtractionCommitted. Extraction succeeds только с меньшим полным key.

### 11.2. PhaseSpatialMutationSet

Каждый переход использует finite preauthored set: primary variant, occupancy-safe fallbacks и mandatory `NO_SPATIAL_DELTA` fallback.

```yaml
PhaseSpatialMutationSet:
  owner: SessionWorldState
  source: authored_sector_phase_content
  mutation_set_id: opaque
  from_phase_revision: required
  target_phase_band: required
  primary_variant_ref: required
  occupancy_safe_fallback_refs: ordered
  no_spatial_delta_fallback_ref: required
  objective_reward_cost_equivalence_proof_refs: topology_uncertainty_LoS_traversal_objectives_rewards_all_cost_axes
  materiality_policy_ref: required
  static_revision_variant_certificate_refs: matching_per_variant
  min_protected_presences_to_force_no_spatial_delta: exceeds_collusion_bound_or_fallback_materially_nonbeneficial
  state: AUTHORED|STATIC_VALIDATED|PUBLISHED|REJECTED
  lifecycle: selected_once_at_phase_barrier

ProtectedVolumeSnapshot:
  owner: ServerLifecycle
  source: authoritative_occupancy_at_PHASE_BARRIER_DECISION_KEY
  snapshot_id: opaque
  occupied_presence_and_COMMIT_pending_footprint_refs: required
  swept_capsule_stance_support_margin_refs: required
  living_cargo_refs: required
  velocity_and_transform_refs: required
  lifecycle: immutable_for_phase_variant_selection
```

Transaction:

1. Prevalidate matching static bundle for every variant/topology hash.
2. Warning/fence.
3. Capture barrier-key occupancy including pending COMMIT footprints.
4. Choose first variant whose exact bundle hash matches occupancy/topology/controller cap.
5. Check one global dynamic EgressSolvencyBundle.
6. In one bounded server decision perform final clearance, collision activation and atomic PhaseRevision+variant+bundle; mismatch chooses next variant/NO_SPATIAL without async gap.
7. Publish boundary/search sets, then SessionServiceSnapshot, then offers.

Valid variant preserves transform and velocity, support surface, ProtectedVolume clearance и минимум одну reachable Threshold search family с remaining-time corridor. Он не создаёт overlap, wall/prop под телом или disconnected occupied component.

Нет player-specific geometry, push, micro-teleport, collision disabling или runtime deformation. Если все spatial variants invalid, `NO_SPATIAL_DELTA` сохраняет geometry, но новая phase hazard/light/rules commits. Equivalence proof покрывает topology uncertainty, LoS, traversal, objectives/rewards и все cost axes по materiality policy; unique shortcut не сохраняется. Если forced fallback может дать material collusion advantage и collusion-bound invariant не выполнен, content invalid.

Player occupancy не задерживает phase и не покупает advantage: ordered fallback выбирается глобально, а не по желанию игрока.

## 12. EgressSolvencyInvariant

Server MUST NOT admit или phase-shift игроков в mathematically insolvent exit envelope.

```yaml
StaticEgressSupplyEnvelopeCertificate:
  owner: ExtractionSolvencyValidator
  source: prevalidated_variant_topology_and_threshold_supply
  certificate_id: opaque
  phase_spatial_variant_id: required
  topology_hash: required
  unique_future_threshold_slot_refs: required
  static_time_expanded_supply_graph_ref: required
  static_supply_lower_bound: derived
  state: VALID|INVALID
  lifecycle: immutable_part_of_StaticRevisionVariantCertificate

EgressSolvencyBundle:
  owner: ExtractionSolvencyValidator
  source: static_envelope_plus_global_dynamic_demand_and_supply_epoch
  bundle_id: opaque
  session_id: required
  candidate_phase_revision: required
  phase_spatial_variant_id: required
  topology_hash: required
  demand_epoch: required
  static_supply_envelope_ref: required
  global_time_expanded_graph_witness_ref: required
  globally_unique_future_threshold_slot_refs: required
  sync_reservation_refs: required
  active_committed_demand_refs: required
  prospective_breach_group_refs: required
  per_component_views: disjoint_projections_of_one_global_witness
  final_stabilization_at: required
  validation_result: SOLVENT|INSOLVENT
  lifecycle: versioned_recompute_on_every_supply_demand_or_time_event

EgressCoverageObligation:
  owner: ExtractionSolvencyValidator
  source: committed_presence_in_global_witness
  obligation_id: opaque
  presence_ref: required
  latest_start_key: required
  state: TIMELY|ALLOCATED_SYNC|REMOVED|WINDOW_FORFEITED_BY_INACTION
  lifecycle: terminal_on_REMOVED_or_WINDOW_FORFEITED_BY_INACTION
```

```text
GlobalConservativeReachableUniqueThresholdThroughputBefore06
>= AllActiveCommittedPresences + ProspectiveBreachGroup
```

Один global time-expanded graph охватывает demands всех component sources; два components не могут посчитать один future slot дважды. Per-component views — только disjoint projections одного witness, не отдельные solvers. Witness не reservation/entitlement.

Bundle проверяется при publication, phase commit, admission и Breach COMMIT. Recompute triggers: latest-start clock, Threshold birth/TTL/fade/reset, Sync reserve/release, topology/components, JIT anchor assignment, SearchGraph, terminal removal и population change. Threshold use/Extraction уменьшает supply и demand на один. World mutation не может ломать solvency: выбирает fallback/equivalent supply либо rejects. Hostile action или inaction могут сделать runtime outcome insolvent.

Own missed latest-start переводит obligation в `WINDOW_FORFEITED_BY_INACTION`, может закрыть intake и не создаёт pity exit. Acceptance проверяет solvency в decision points, не eternal solvency. Bundle не personal reservation, protected route, success guarantee или защита от PvP, greed, interruption и failure to act.

## 13. Threshold, SearchEvidence и manifest

### 13.1. SearchResolutionGraph

```yaml
SearchResolutionGraph:
  owner: RaidKnowledgeLedger
  source: authored_threshold_search_content
  graph_id: opaque
  session_id: required
  phase_revision: required
  threshold_family_id: required
  finite: true
  acyclic: true
  authored_edge_refs: required
  alternate_branch_refs: required
  state: PUBLISHED|CLOSED|EXPIRED
  lifecycle: revision_bound

SearchEvidence:
  owner: RaidKnowledgeLedger
  source: server_confirmed_authored_evidence_action
  evidence_id: opaque
  knower_ref: PawnID_or_PartyKnowledgeRef
  session_id: required
  phase_revision: required
  graph_edge_ref: required
  evidence_class: authored
  confirmed_at: timestamp
  cost_evidence_ref: nonzero_time_exposure_resource_or_opportunity
  state: CONFIRMED|TRANSFORMED|STALE|EXPIRED
  lifecycle: session_local_until_transform_stale_or_session_terminal

SearchEdgeAttempt:
  owner: RaidKnowledgeLedger
  source: authored_search_action_started
  attempt_id: opaque
  edge_ref: required
  presence_ref: required
  state: IN_PROGRESS|CONFIRMED|ABORTED_AT_BARRIER|FAILED|EXPIRED
  deterministic_transform_ref: optional
  lifecycle: total_before_edge_or_phase_deadline
```

Evidence никогда не создаётся proximity, per-frame camera или bulk scan. Alternate branch существует заранее и требует отдельного authored action.

```text
CanStartSearchEdge(edge, presence, now)
= EdgePrerequisitesConfirmed(edge, presence)
AND EdgeTTLAllows(edge, now)
AND now + conservative_edge_duration
        + remaining_search_lower_bound
        + required_sync_duration
        + server_margin
    < min(edge_valid_until,
          next_phase_barrier unless edge is authored TRANSFORMABLE,
          FinalStabilization)
```

Player-facing reason ровно различает: **другой путь ещё помещается** или **повтор уже не помещается**.

Barrier завершает `IN_PROGRESS` attempt без evidence, если authored deterministic transform отсутствует. Потраченный physical cost не refunds; uncommitted reservations releases.

### 13.2. Threshold и SyncLease

```text
SEARCH_PATH
→ THRESHOLD_FORETOLD
→ THRESHOLD_OPEN
→ SyncLeaseCreated + SYNCING
→ EXTRACTION_COMMITTED
or INTERRUPTED → RESET/OPEN if TTL and CanStartSync allow
or INTERRUPTED → FADE
```

```yaml
ThresholdAnchorAssignment:
  owner: SessionBoundaryGraph
  source: server_confirmed_search_evidence_plus_world_state
  assignment_id: idempotency_key
  session_id: required
  phase_revision: required
  threshold_family_id: required
  evidence_ref: required
  eligible_anchor_set_hash: required
  selected_anchor_ref: required
  decision_key: arbitration_key
  static_revision_variant_certificate_ref: required
  current_egress_solvency_bundle_ref: required
  state: PREPARING|ASSIGNED|FORETOLD|INVALIDATED
  lifecycle: one_server_decision_no_client_reroll

ThresholdOpportunity:
  owner: SessionBoundaryGraph
  source: published_threshold_family_plus_confirmed_search_evidence
  threshold_opportunity_id: opaque
  session_id: required
  phase_revision: required
  opportunity_revision: required
  valid_until: timestamp
  capacity: integer
  anchor_ref: hidden_until_evidence
  sync_profile_ref: required
  state: FORETOLD|OPEN|FADING|CLOSED
  lifecycle: revision_and_TTL_bound

SyncLease:
  owner: ExtractionResolver
  source: living_body_enters_full_vulnerability_sync
  lease_id: idempotency_key
  threshold_opportunity_id: required
  session_id: required
  phase_revision: required
  pawn_presence_ref: [PawnID, presence_epoch]
  reserved_capacity_slot_id: required
  issued_at: timestamp
  expires_at: timestamp
  nontransferable: true
  nonrenewable: true
  one_active_per_presence: true
  state: SYNCING|ABORTED|COMMITTED|EXPIRED
  lifecycle: continuous_living_body_procedure_only
```

Every eligible anchor проходит static validation. Перед `FORETOLD` assignment проверяет final global coverage+solvency. World/evidence inputs разрешены; hostile positions, identity и personal safety запрещены. JIT assignment не является client reroll.

```text
CanStartSync
= now + required_sync_duration + server_margin
   < min(Threshold.valid_until, next_phase_barrier, FinalStabilization)
```

SyncLease CAS-creates и reserves ровно один slot в тот же момент, когда living body входит в full-vulnerability `SYNCING`. Nonvulnerable capacity hold отсутствует. Interrupt/disconnect releases slot, sync progress becomes zero, TTL continues и same Presence должна закончить local reset перед retry.

Interrupt меняет только SyncLease/Threshold. Он не transfers/erases private evidence, не создаёт reward/claim, не продлевает TTL, не выдаёт new anchor и не rerolls graph. Уже earned evidence остаётся в своём state. `RESET/OPEN` допустим только если TTL и `CanStartSync` ещё позволяют; иначе `FADE`.

### 13.3. ExtractionCommitted и ProtectedManifest

```yaml
ExtractionEligibilityPolicy:
  owner: ExtractionResolver
  source: item_definition_custody_and_operation_scope
  policy_revision: required
  every_custody_graph_node_requires_eligibility: true
  normal_manifest_rejects:
    - operation_local_or_recovery_foreign_ItemID
    - RecoveryKit
    - BodyCustodyClaim
    - active_PawnPresence_or_player_body
  living_cargo_requires: explicit_normal_eligibility_and_no_active_player_presence
  lifecycle: immutable_for_manifest_transaction

ProtectedManifest:
  owner: ExtractionResolver
  source: ExtractionCommitted_decision
  transaction_id: idempotency_key
  participation_claim_ref: required
  presence_ref: required
  sync_lease_ref: required
  eligibility_policy_ref: required
  custody_graph_refs: required
  world_tombstone_refs: required
  logical_extraction_key: arbitration_key
  decision: UNDECIDED|COMMIT|ABORT
  projection_state: NONE|APPLYING|MATERIALIZED|ROLLED_BACK|QUARANTINED
  reconciliation_deadline: required
  lifecycle: one_atomic_manifest_or_no_manifest
```

At immutable manifest `decision=COMMIT`, custody lock, Sync slot consumption, raid Presence removal, terminal claim и lease release становятся logically effective на `logical_extraction_key`; projections replay toward that decision. Final total order всегда применяется: extraction с меньшим полным key succeeds; Final/KIA с тем же или меньшим key делает ABORT/KIA. Crash после COMMIT не отменяет manifest; reconciliation имеет finite deadline.

COMMIT CAS-locks entire carried graph, создаёт один ProtectedManifest, tombstones world copies и удаляет raid body/presence. Затем `RAID→CARE`, если aftermath требует лечения, иначе `RAID→HUB`; states взаимоисключающи. Seat освобождается после logical removal.

Каждый squad member выходит собственной transaction. Partial manifest запрещён. Живая Пешка выходит только своей Presence transaction; чужое тело обрабатывает отдельный lifecycle resolver и никогда не становится manifest cargo.

## 14. Earned Phase Continuity: K/W/C и semantic root

### 14.1. Eligibility и derived view

```text
PhaseContinuityView(ParticipationClaim, FromRevision, ToRevision)
= mapped KnowledgeClaimRefs
+ surviving WorldMutationRefs
+ continuous CustodyRefs
```

Eligibility: тот же SessionID, последовательные revisions, тот же PawnID+presence_epoch, Presence `RAID` строго до и после barrier. Presence, claim и elapsed time не создают value. View не хранит score, meter, buff, currency или player-facing budget.

| Канал | Earn condition | Carry rule |
|---|---|---|
| Knowledge | Server-confirmed authored observation/action с ненулевым time/exposure/opportunity cost | PRESERVE/TRANSFORM/STALE; точная координата не переносится через изменённую geometry без authored mapping. |
| World | Конкретная public world entity mutation | PERSIST/TRANSFORM_WITH_LINK/CONSUME/INVALIDATE; finite per SessionID/Revision, no respawn/reset farm. |
| Custody | Тот же physical ItemID/LivingCargo в continuous custody | Weight/slot/Dissonance/damage сохраняются; dropped item следует world resolver; marker не заменяет custody. |

K/W refs session-local и истекают с SessionID/claim. Extracted ItemID покидает raid только обычным manifest и не превращается в account Continuity buff. Mission может читать K/W/C refs и переносить собственное состояние, но не является четвёртым continuity/access channel.

### 14.2. ContinuityBudgetRootID

```yaml
ContinuityBudgetRoot:
  owner: ContinuityRootRegistry
  source: authored_exactly_one_root_owner
  continuity_budget_root_id: stable
  root_owner_ref: exactly_one(ObjectiveInstanceID|RouteCommitmentID)
  primary_axes: [time, exposure, uncertainty]
  minimum_live_material_debts_after_carryover: 2
  state: AUTHORED|VALIDATED|ACTIVE|TERMINAL
  lifecycle: inherited_without_remint_by_all_descendants

ObjectiveCommitmentContext:
  owner: ContinuityRootRegistry
  source: server_confirmed_contributor_closure_for_semantic_root
  context_id: opaque
  continuity_budget_root_id: required
  contributor_closure: all_actual_parties_Pawns_and_public_mutations_for_root
  KWC_ref_union: required
  reachable_combination_refs: required
  lifecycle: recomputed_on_party_ref_or_scene_change
```

Каждый subscene, world transform, mission handoff и derived K/W/C ref наследует один `ContinuityBudgetRootID`. Root owner immutable; handoff/readers и Mission/Pledge не remint root.

`ContinuityAxisValidator` authoring-time доказывает для всех simultaneously reachable combinations server-confirmed contributor closure across all actual parties/Pawns/public mutations. Friendship inference не используется; coordinated cross-party K/W/C учитываются через semantic root:

- materially retired максимум одна primary axis: time **или** exposure **или** uncertainty;
- secondary spillover остаётся sub-material;
- минимум две material debts остаются live;
- carryover даёт materially different nonexclusive cost vector, который нельзя купить credential/loadout;
- baseline objective/reward/exit остаются доступны fresh entrant.

Runtime никогда не cancels earned physical state ради cap. Invalid content/revision не публикуется. Каждый 0→2 и 2→4 переход предоставляет минимум две spatially/temporally competing continuity opportunities из K/W/C, встроенные в observe/prepare physical object/carry. Checklist отсутствует. 4→6 playable continuity payoff нет: value надо реализовать и выйти до 06:00.

После shift protected incumbent window/priority отсутствует. Новые opportunities публикуются сразу; incumbent сохраняет только natural position, knowledge, prepared public state, custody и оплаченный риск.

## 15. Public Recovery contract

### 15.1. RecoveryCase

```yaml
RecoveryCase:
  owner: LifecycleRecovery
  source: authoritative_source_raid_lifecycle_event
  recovery_case_id: opaque
  account_id: required
  pawn_id: required
  source_session_id: required
  account_last_thread_slot_ref: existing_AccountLifecycle.account_last_thread_slot
  active_recovery_binding_attempt_ref: optional
  created_at: timestamp
  expires_at: absolute_player_visible_timestamp
  state: PENDING|SEARCHING|BOUND|IN_RECOVERY|COLLAPSED|RECOVERED|FAILED|EXPIRED
  terminal_resolution_transaction_ref: optional
  lifecycle: CAS_account_last_thread_slot_EMPTY_to_CaseID_then_release_exactly_once_by_terminal_resolution

RecoveryBindingAttempt:
  owner: LifecycleRecovery
  source: Recovery_target_binding_attempt
  attempt_id: opaque
  recovery_case_id: required
  binding_id: required
  public_activity_certificate_ref: required
  state: PREPARING|BOUND|SUPERSEDED|COMMITTED|FAILED
  terminal_reason: optional
  lifecycle: append_only_never_rewrites_prior_attempt
```

Case creation CASes existing `AccountLifecycle.account_last_thread_slot` from `EMPTY→CaseID`; новый owner/slot не создаётся. Slot занят во всех unresolved PENDING/SEARCHING/BOUND/IN_RECOVERY/COLLAPSED states. Пока он занят, lethal outcome другой Пешки получает `BLOCKED_BY_ACCOUNT_CUSTODY`. Только authoritative terminal RecoveryResolution/expiry releases slot exactly once. Ingress не invents fate. `expires_at` видим игроку, действует и в `IN_RECOVERY` и не pauses последним entry/technical retry.

### 15.2. PublicActivityCertificate

`PublicActivityCertificate` создаётся из ordinary standard activity независимо и **до** Recovery binding.

```yaml
PublicActivityCertificate:
  owner: RegionalScheduler
  source: independently_observed_ordinary_standard_activity
  certificate_id: opaque
  session_id: required
  phase_revision: required
  service_snapshot_id: required
  observed_at: timestamp
  issued_at: timestamp
  issued_before_recovery_binding: true
  independent_standard_activity_set_ref: required
  admission_state: OPEN
  static_revision_variant_certificate_ref: required
  recovery_egress_solvency_bundle_ref: required
  input_hash: required
  independence_threshold_policy_ref: required
  target_selection_entropy_policy_ref: required
  valid_until: timestamp
  state: VALID|STALE|REVOKED|SESSION_TERMINAL
  lifecycle: server_owned_never_minted_by_recovery_request
```

Recovery binding требует:

- target != source;
- target activity `CONTESTABLE`, admission `OPEN` и ordinary intake остаётся open;
- certificate создан до binding независимо от Recovery;
- на Recovery BreachCommitted присутствует минимум один active unaffiliated STANDARD AccountID;
- matching static bundle, recovery-specific global solvency и time corridor;
- Recovery AccountID имеет Participation `NeverParticipated` в target.

Recovery Breach PREPARED/COMMIT требует Case `BOUND`, unexpired case key, matching attempt/certificate/phase/service/static/global-solvency refs и active unaffiliated STANDARD at decision key. COMMIT atomically transitions `BOUND→IN_RECOVERY`. После COMMIT natural depopulation не отменяет попытку. Association policy остаётся residual operations layer; certificate снижает alt-seeding risk, но не объявляет его абсолютно решённым.

Insufficient independence/entropy либо no certificate оставляет Case `SEARCHING`; Recovery не seed session, shard/room или special queue. `SEEDING` принимает первого normal standard player, не Recovery.

Stale activity/certificate запускает same-target AdministrativeResolution; Resume требует новый independently minted same-target certificate. Если target globally unusable, durable GlobalTargetUnusableCertificate разрешает new unbound search до case expiry. Exact SessionID хранится только TargetBinding, не RecoveryCase.

Recovery entry использует standard seat, обычный BreachTransaction и `ParticipationClaim.kind=RECOVERY`. Recovery exit — только `RecoveryThresholdSync/BodyRecoverySync→CARE`, без ProtectedManifest. Operation-local/Recovery items не проходят normal extractor. Breakline остаётся отдельным body-only emergency flow.

### 15.3. RecoveryResolutionTransaction

```yaml
RecoveryResolutionTransaction:
  owner: RecoveryResolutionResolver
  source: recovery_success_failure_case_expiry_or_world_terminal_event
  transaction_id: idempotency_key
  recovery_case_id: required
  presence_ref: optional_for_pending_searching_bound_expiry
  participation_claim_ref: optional
  account_deployment_lease_ref: optional
  account_last_thread_slot_ref: required
  logical_resolution_key: arbitration_key
  decision: UNDECIDED|RECOVERED|FAILED|EXPIRED
  projection_state: NONE|APPLYING|MATERIALIZED|QUARANTINED
  reconciliation_deadline: required
  protected_manifest_ref: forbidden
  lifecycle: one_immutable_decision_and_exactly_once_CARE_or_terminal_projections
```

Case expiry participates even `IN_RECOVERY`. При одном tick world/case expiry имеет priority раньше Recovery success; success succeeds только с меньшим полным key. Pending/SEARCHING/BOUND expiry resolves без body; active expiry terminally removes recovery body. Transaction atomically resolves Case, Presence, Claim, AccountDeploymentLease и account_last_thread_slot в CARE либо terminal state; ProtectedManifest никогда не создаётся.

## 16. Player projection и lived failure flows

Backend IDs, certificate states, population, opaque rebind, coordinator state и policy codes игроку не показываются.

```yaml
IngressPlayerProjection:
  owner: UIProjection
  source: authoritative_offer_binding_admin_breach_state
  projection_id: opaque
  account_and_party_scope_ref: required
  state: SELECTING_APPROACH|PREPARING_CROSSING|ENTRY_WINDOW_CLOSING|SECTOR_DELAYED|ENTERING|ENTRY_CANCELLED|ACTIVE_IN_SECTOR
  headline: exactly_one_human_phrase
  human_reason: exactly_one
  optional_deadline: zero_or_one
  exact_loss_state: required
  allowed_action: exactly_one_primary_action
  member_blocker: optional_who_and_what_only
  backend_ids_or_raw_population: forbidden
  lifecycle: replaced_on_authoritative_state_change
```

Human reasons: terms changed; window closed; party/loadout/commitment blocker; no valid crossing; connection; technical delay; system refunded. Party видит shared operation; member blocker раскрывает только who/what, не hidden target internals. UI имеет одну headline, одну human reason, optional одну deadline, exact loss state и одну primary allowed action.

### 16.1. Normal direct ingress

| Frame | Player experience |
|---|---|
| Perception | Sector, envelope, public clock bounds, envelope forecast, self Dissonance, 1–3 approaches, debt/commitment. |
| Interpretation | Direct entry — полноценная петля, но без private exact-seed memory/custody authorship. |
| Decision | Выбрать ApproachOffer; после sticky target изучить exact quote и подтвердить либо отказаться без reroll scope. |
| Commitment | Gear/commitment lock после confirmation; deployment stake только при Breach decision=COMMIT. |
| Feedback | `PREPARING_CROSSING`→`ENTERING`, local physical tell, первый exposed frame с full control. |
| Consequence | Fresh Presence участвует в public world; no automatic continuity. |

### 16.2. No candidate before disclosure

`OPAQUE_TARGET_PREFLIGHT` может сделать one silent equivalent rebind. Player не видит attempt count, latency oracle или target fingerprint; получает final quote либо generic `ENTRY_CANCELLED: no valid crossing`, без loss и без sticky target-tainted detail.

### 16.3. No candidate after disclosure / finite resolution

Projection: `SECTOR_DELAYED`; одна human reason «нет допустимого места пересечения» или «техническая задержка», finite deadline и action «вернуться в Хаб». Seat/candidate released, commitment не consumed, receipt sticky. Outcome: resume same target; withdrawn sticky/refund; либо system terminal failure/refund с server-authorized retarget только при globally unusable target.

### 16.4. Low-pop Recovery wait

Projection показывает `RecoveryCase.SEARCHING`, absolute case expiry и reason «ищется обычная живая экспедиция». Он не обещает врага, не показывает raw population и не создаёт impression специальной Recovery queue. No certificate означает wait/search; expiry даёт lifecycle outcome, не ingress penalty.

### 16.5. Phase warning и fallback

Nonmodal first layer показывает максимум три приоритетных human-verb changes; unchanged скрыты, полный список доступен в map/log. Player не выбирает geometry fallback и не должен подтверждать warning в бою. Physical precursor→pulse→visible changed state. Если выбран `NO_SPATIAL_DELTA`, hazard/light/rules visibly change, а geometry остаётся; UI не обещает closure, которого не произошло.

### 16.6. Late Threshold interrupt

Interrupt даёт читаемые physical interruption, slot release и sync reset. Затем ровно один reason: «другой путь ещё помещается» либо «повтор уже не помещается». Earned evidence остаётся; new anchor и pity progress не выдаются. Late denial может завершиться KIA и остаётся healthy PvP consequence.

### 16.7. Minimum feel pass

- local ingress tell и first-frame full control;
- physical phase precursor/pulse и visible spatial/non-spatial fallback result;
- visible world transform либо stale evidence reason;
- Threshold birth/reset/fade и interrupt feedback;
- distinct human reasons для offer changed, window closed, no valid crossing, connection, technical delay и system refund;
- three outcomes: success, deliberate retreat/withdrawal, failure/KIA.

## 17. Enforcement taxonomy

### 17.1. Runtime-enforced

Owners: ServerLifecycle, TargetBindingResolver, EntryQuoteResolver, InsertionAdmissionResolver, InsertionBreachCoordinator, ExtractionResolver, RecoveryResolutionResolver.

- six-hour clock, PhaseRevision, fences и arbitration;
- one nonterminal binding/account, DisclosureReceipt-before-tainted-output;
- immutable exact quote и no rebind after disclosure;
- one durable squad Breach `decision=COMMIT|ABORT`, conditional fences и exactly-once projections/refunds;
- unique Account controller/Pawn Presence/Participation;
- hard candidate veto, pressure physics, finite AdministrativeResolution;
- SyncLease/manifest/finality/Recovery-no-manifest rules.

### 17.2. Load-bearing authoring and validator obligations

Owners: StaticRevisionValidator, ExtractionSolvencyValidator, ContinuityRootRegistry/ContinuityAxisValidator и authored content owners.

- matching StaticRevisionVariantCertificate/IngressCoverageSubproof, StaticEgressSupplyEnvelopeCertificate, PhaseSpatialMutationSet и continuity proofs;
- threshold-family independence and latent anchors;
- `NO_SPATIAL_DELTA` plus objective/reward/cost equivalence;
- ContinuityBudgetRoot inheritance and ContinuityAxisValidator;
- finite acyclic SearchResolutionGraph;
- baseline objective/path/search/reward for every supported composition.
- predicate dependency graph acyclic: static facts → BaseAdmissionServiceable → dynamic EgressSolvencyBundle → CanPublishIngress.

Конкретные sector instances остаются content work, но архитектура уже задаёт owner, certificate и acceptance test.

### 17.3. Operations policy

Owner: regional operations/anti-cheat.

- health/capacity/latency and low-pop collapse execution;
- federation compatibility только для unbound requests;
- association policy и false-positive audit;
- incident resolution reason/SLA operations;
- observability, abuse response и certificate failure alerting.

### 17.4. Empirical corridors and residual risks

- p95 offer/binding/commit, agency/search/sync margins;
- AdministrativeResolution SLA;
- practical controller bounds from Combat registry;
- false-positive/false-negative association behavior;
- residual probabilistic same-instance co-binding in low population;
- player comprehension of reasons, phase fallback и late denial;
- acceptable sparse standard PvPvE feel.

Ни одно эмпирическое значение не подменяет runtime invariant.

## 18. Crash tests

| Risk | Severity | Failure chain | Required break | Healthy false positive |
|---|---|---|---|---|
| Fingerprint tuple | Critical | response size/order/timing→target identity | Offer equivalence, generic preflight response, tainted-output receipt fence | Exact quote after sticky disclosure. |
| Rebind timing oracle | Critical | first target slow→silent rebind observable | bounded indistinguishable preflight projection; metrics | Generic preflight failure. |
| Multiple bindings | Critical | parallel offers→multiple targets | one nonterminal binding/account CAS | New binding after terminal expiry. |
| Cross-offer scope reroll | Critical | another OfferID→another target | shared StickyTargetScopeID across all offers | Different terms, same sticky target. |
| Receipt conflict | Critical | reshaped party has conflicting targets | all-or-none receipts; STICKY_TARGET_CONFLICT until expiry/global release | Clean member joins known compatible target. |
| Party reshuffle | Critical | disband→receipt reset→reroll | per-original-account durable receipt | New offer scope after expiry. |
| Finite resolution grief | High | delayed target→endless block | deadline, resource release, finite outcomes | Short same-target resume. |
| Crash before PREPARED | Critical | partial locks | decision ABORT/refund projections | Retry same transaction ID. |
| Prepared fence reject | Critical | one uniqueness/capacity fence fails | whole roster ABORT before logical effects | Durable preparation itself. |
| Crash after PREPARED | Critical | UNDECIDED crosses fence | watchdog writes ABORT or lower-key COMMIT | Prepared token itself. |
| COMMIT pending across phase/final | Critical | logical body not projected | pending footprint in occupancy; replay pulse/KIA/Final; no ACTIVE after 06:00 | Brief reconcile latency. |
| Crash during materialization | Critical | duplicate body/claim/tell | deterministic IDs/idempotent projections | Replayed projection. |
| Population-wide ingress suppression | Critical | controllers cover all cells | suppression-cut certificate/cap reduction/reject revision | One camped ingress region. |
| Pressure epsilon exploit | High | micro-delay exits binary window | continuous monotone decay field | Paid staggering far enough. |
| Pressure shadowing | High | declared party/identity changes tell | identity-blind committed-event field | Organic teaming later. |
| Continuity subscene laundering | Critical | split mission→remint three axes | inherited semantic root/union validator | Alternative refs within same retired axis. |
| Recovery alt-seeding | Critical | alt creates population certificate | independently prior ordinary activity certificate | Sparse genuine standard PvPvE. |
| Recovery special shard | Critical | no target→new instance | SEARCHING/wait; suppression/Recovery never creates | Standard SEEDING accepts normal player. |
| Egress insolvency | Critical | admit demand>reachable unique global supply | EgressSolvencyBundle at publish/phase/admit/Breach | PvP later denies exit. |
| Two components share future slot | Critical | per-component double count | one global unique-slot witness; disjoint views | Separate truly unique slots. |
| JIT anchor harms global flow | Critical | assignment consumes critical supply | durable assignment checks current global bundle before FORETOLD | One camped Threshold. |
| Phase occupancy manipulation | High | body blocks closure for shortcut | ordered global fallback/equivalence/no advantage | No-spatial fallback commits hazards. |
| Barrier occupancy race | Critical | movement/COMMIT footprint omitted | exact barrier-key snapshot includes both | Lower-key movement counts. |
| Forced fallback collusion | High | bodies force profitable NO_SPATIAL | collusion bound or materially nonbeneficial proof | Legitimate fallback. |
| Variant/hash mismatch | Critical | geometry uses wrong static bundle | bounded decision chooses matching bundle or next fallback | Valid next variant. |
| Threshold family lock | Critical | squad controls all exits | family coverage certificate/JIT latent anchors | One camped Threshold. |
| Late evidence pity | High | interrupt→free anchor/progress | evidence unchanged, sync zero, TTL continues | Late interrupt can be lethal. |
| SyncLease cycling | High | reserve/abort stalls TTL | vulnerable create, immediate release, TTL never extends | Legitimate retry after reset. |
| Manifest laundering | Critical | Recovery/body/item enters normal manifest | node eligibility/CAS/no Recovery manifest | Eligible LivingCargo. |
| Manifest crash before/after COMMIT | Critical | custody/slot/removal diverge | immutable manifest decision + replay by logical key | Earlier extraction key succeeds. |
| Recovery multiple-Pawn custody | Critical | two unresolved cases/account | existing account_last_thread_slot CAS | One active case. |
| Recovery certificate mule/entropy | High | alt manufactures activity confidence | independent activity+entropy policy; residual measured | Sparse genuine public session. |
| Recovery commit/expiry/success race | Critical | last-second entry pauses fate | absolute expiry; full-key RecoveryResolution decision | Earlier success wins. |
| Time-forfeit | High | missed latest-start demands pity supply | WINDOW_FORFEITED_BY_INACTION; close intake if needed | Late denial/no pity exit. |
| Final race | Critical | extraction and KIA at 06:00 | full arbitration key; Final/KIA priority same tick | Extraction with smaller full key. |
| Low-pop collapse | High | silent phase substitute/moved bodies | fixed collapse order, unavailable state | Sparse standard public session. |

Deterministic exploit chain «alt fingerprints target→party reshuffles→waits T3→blocks all ingress/egress→farms empty world» не работает: tainted-output receipt, durable per-account scope, suppression-cut/Threshold certificates, no idle value, fresh baseline и solvency checks разрывают её. Probabilistic co-binding low-pop остаётся residual operations risk и измеряется, а не объявляется закрытым.

## 19. Failure matrix

| Event | Authoritative outcome | Player projection |
|---|---|---|
| OfferTermsHash changed | Old offer superseded; no target substitution | SELECTING_APPROACH: terms changed |
| Opaque preflight finds no target | One silent equivalent rebind; otherwise generic fail | ENTRY_CANCELLED: no crossing available |
| Target-tainted payload ready | Receipt+stickiness atomically precede send | PREPARING_CROSSING |
| Exact quote declined | Receipt remains sticky; locks released | ENTRY_CANCELLED with exact loss zero |
| Other offer in same scope selected | Same target; compatible new quote or unavailable | PREPARING_CROSSING / approach unavailable |
| Conflicting active receipts | STICKY_TARGET_CONFLICT; no retarget | incompatible party target; wait/re-form |
| No candidate after disclosure | AdministrativeResolution; no new target | SECTOR_DELAYED with deadline |
| Target terminal globally | SYSTEM_TERMINAL_FAILURE/refund; retarget authorization | ENTRY_CANCELLED: system refunded |
| Stale opportunity/capacity lost | Finite resolution or fail/refund | technical delay/window closed |
| Disconnect before decision | Whole party abort/refund | ENTRY_CANCELLED: connection |
| Member failure before decision | Whole party abort/refund | party blocker who/what |
| Crash before PREPARED_DURABLE | decision ABORT; projections ROLLED_BACK | technical delay then refund |
| Crash after PREPARED before decision | Watchdog decides abort before fence | technical delay/window closed |
| Conditional fence rejected | Whole roster decision ABORT | blocker/refund |
| Crash after decision COMMIT | Reconcile toward same logical effects | ENTERING; logical body remains vulnerable |
| COMMIT projection crosses barrier/final | Pending footprint receives later-key pulse/KIA/Final; no ACTIVE after 06:00 | ACTIVE or terminal result by total order |
| Crash during materialization | Idempotent deterministic replay | ENTERING then ACTIVE_IN_SECTOR |
| All ingress cells suppressed before disclosure | One allowed opaque rebind or generic fail | ENTRY_CANCELLED |
| All ingress cells suppressed after disclosure | Same-target finite resolution | SECTOR_DELAYED |
| Phase fence before breach decision | Whole transaction abort/refund | ENTRY_WINDOW_CLOSING→ENTRY_CANCELLED |
| Phase barrier after breach decision | Body materializes and receives pulse | ACTIVE_IN_SECTOR |
| No valid phase spatial variant | Commit NO_SPATIAL_DELTA plus new hazards/rules | phase changed, geometry unchanged |
| Variant/bundle hash mismatch | Try next matching variant/NO_SPATIAL in same bounded decision | phase fallback result |
| Egress solvency invalid before admission | No publish/commit | no crossing available |
| Global future slot collision | Bundle INSOLVENT; no double-count | no crossing available |
| Egress latest-start missed | Obligation WINDOW_FORFEITED_BY_INACTION; no pity supply | retry no longer fits |
| JIT anchor fails global bundle | Assignment not FORETOLD; no reroll | another path fits / unavailable |
| Sync interrupted | Slot released, sync zero, TTL continues, evidence unchanged | retry fits / no longer fits |
| Barrier during sync | Abort; slot release; new revision set | Threshold fades/resets |
| Duplicate ItemID | Manifest abort/reconcile; no duplicate projection | extraction failed, item state unchanged |
| Manifest crash after COMMIT | Replay custody/slot/removal by same logical key | extraction resolving then settled |
| KIA and Extraction same tick | Event priority puts KIA first | failure/KIA |
| Recovery certificate absent | Case SEARCHING, no shard | waiting for public expedition |
| Account last-thread slot occupied | New Case blocked; existing Case unchanged | BLOCKED_BY_ACCOUNT_CUSTODY |
| Recovery target terminal before case expiry | Server authorizes unbound search if globally unusable | searching; same absolute deadline |
| RecoveryCase expiry | RecoveryResolution decision EXPIRED; slot/Presence/Claim/lease resolve once | EXPIRED/terminal fate reason |
| Recovery success and expiry same tick | Expiry wins; earlier full-key success wins | CARE or terminal outcome |
| Final Stabilization | All remaining raid bodies KIA | failure; no survivor reward |

## 20. Metrics and empirical unknowns

Collect without invented corridors:

- approach select/decline/reconfirm by envelope and composition;
- shared-scope cross-offer reuse, receipt conflict and all-or-none disclosure failures;
- Offer fingerprint anonymity: response size/order/timing leakage and classifier success;
- opaque preflight generic failures, silent-rebind aggregate rate and timing distributions available only to secure operations telemetry;
- AdministrativeResolution reason/outcome/time, withdrawal and refund latency;
- conditional fence rejection, Breach reconcile latency, QUARANTINED projections, duplicate logical effects and crash edge distribution;
- ingress suppression veto reasons, min suppression cut and coverage certificate failures;
- IngressPressureField density, paid staggering, random-solo comprehension;
- pool activity SEEDING/CONTESTABLE, admission OPEN/SATURATED/DRAINING/CLOSED and each collapse step;
- envelope availability, backfill, federation and latency;
- Recovery wait/absolute deadline outcomes, account-slot blocks, certificate independence/entropy rejection, expiry-success arbitration and association false positives;
- global unique-slot Egress supply/demand margin at publication/phase/admission/Breach, time-forfeit and JIT assignment rejection;
- phase fallback selected, barrier-key occupancy/pending-footprint conflicts, variant/hash mismatch, forced-fallback attempts and no-spatial frequency;
- continuity root combinations, validator rejection and carryover use by axis;
- SearchEvidence CONFIRMED/TRANSFORMED/STALE/EXPIRED outcomes;
- Threshold camp/interruption/reset/fade/success and late KIA;
- manifest decision/reconcile latency, duplicate projections and KIA–Extraction–Stabilization arbitration;
- player comprehension of one-line reason, exact loss, allowed action and deadline;
- stay/direct/exit rates, fresh entrant objective/extraction success, deaths/damage after breach, AFK dwell and private-knowledge PvP effect.

Durations, capacity/controller bounds and UX corridors require balance/load/play tests. Finality, ownership, no partial manifest, no time buff, no special Recovery shard and separation K/W/C are normative, not empirical.

## 21. MVP decomposition

| MVP | Included | Validates | Explicit non-claim |
|---|---|---|---|
| A. Boundary Kernel | NON-PUBLIC/NON-SHIPPABLE static harness; one sector/revision; Offer→shared Scope/Receipt→Quote→Breach; minimal valid static coverage+global egress; **two** Threshold families; manifest/finality; no live shift | Privacy boundary, conditional fences, durable Breach/manifest decisions and unique-slot witness | Does not validate rolling pool or continuity vision. |
| B. Living Pool vertical slice | Three envelopes; LowPopulationPolicy; real 0→2 and 2→4; variants/barrier-key occupancy; static bundles/global solvency; minimum valid competing K/W/C roots/axis proofs | Living clocks, collapse, realizable phase shifts, egress and first continuity invariant | Not broad build/continuity comprehension. |
| C. Continuity and build breadth | Additional authored K/W/C, route/build choices and comprehension pass over already-valid roots | Choice breadth, readability and resistance to cross-party/subscene laundering | Does not establish the first continuity invariant. |
| D. Public Recovery Overlay | RecoveryCase; prior public-health certificate; standard target/seat; no special shard/manifest | Public population dependency, deadline/fate, normal-world recovery | Does not replace ordinary extraction or settlement. |

Federation, events и complex search graphs deferred. Every exercised transition retains total states, matching certificates, deadlines, reconciliation and Final Stabilization.

## 22. Migration map

Authority переносится одновременно; старый Access Contract не остаётся параллельным owner. Эти страницы сейчас не редактируются.

| Canonical page | Required migration after approval |
|---|---|
| [[08_World_Generation/Generation/07_Server_Lifecycle|Server Lifecycle]] | Clock, PhaseRevision, barriers, arbitration, ProtectedVolume snapshot. |
| [[08_World_Generation/Generation/06_Async_Timers|Async Timers]] | Rolling service set, Final Stabilization, deadlines. |
| [[08_World_Generation/Generation/05_Difficulty_Slots|Difficulty Slots]] | Remove matchmaking/access authority; keep only derived world-age semantics where needed. |
| [[08_World_Generation/Generation/19_Access_Contracts|Access Contracts]] | Deprecate/replace with focused Offer, Binding and Ingress opportunity owners. |
| [[08_World_Generation/Anomaly/13_Insertion_Logic|Insertion Logic]] | Conditional fences, durable Breach decision/projections, candidate veto and pressure field. |
| [[08_World_Generation/Anomaly/14_Extraction_System|Extraction System]] | Static supply envelope, global EgressSolvencyBundle, JIT assignment, SyncLease and durable ProtectedManifest. |
| [[08_World_Generation/Generation/08_Gate_Check|Gate Check]] | Envelope/exact forecast and phase pulse; no offer/binding ownership. |
| [[08_World_Generation/Generation/10_World_Topology|World Topology]] | Static variant bundles, barrier-key occupancy, PhaseSpatialMutationSet and global supply graph. |
| [[08_World_Generation/Anomaly/15_Frequency_Tuner|Frequency Tuner]] | Remove Trace rejoin/redeploy path. |
| [[06_Economy_Loot/Extraction_Stabilization_Loop|Extraction Stabilization Loop]] | Manifest settlement and exact 06:00 finality. |
| [[08_World_Generation/Hub/01_Hub_Map_Table|Hub Map Table]] | ApproachOffer and IngressPlayerProjection. |
| [[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]] | Account/Pawn leases, existing account_last_thread_slot, RecoveryCase/Resolution and terminal fate. |
| [[08_World_Generation/Persistence_Ledger|Persistence Ledger]] | Participation, K/W refs, SearchEvidence and durable decisions. |
| [[07_Gear_Inventory/Inventory_Architecture|Inventory Architecture]] | Commitment/custody projections and manifest eligibility. |
| [[03_Factions_Societies/Pledge_Contracts|Pledge Contracts]] | Pledge commitment and no continuity remint. |
| [[05_Combat_Survival/Dissonance_System|Dissonance System]] | Self result only; no hidden admission punishment. |
| [[08_World_Generation/Generation/14_Sector_Content_Rules|Sector Content Rules]] | Coverage/geometry/egress/continuity authoring certificates. |
| [[08_World_Generation/Generation/13_Async_Double_Buffer|Async Double Buffer]] | Prepared variants infrastructure, not decision ownership. |
| [[08_World_Generation/Hub/05_Party_Syndicate|Party Syndicate]] | Shared operation projection and durable per-account receipt semantics. |
| [[09_Project_Management/Architecture_MVP|Architecture MVP]] | Four MVPs and their non-claims. |
| [[01_Core_Vision/02_Core_Loop|Core Loop]] / [[01_Core_Vision/01_Vision|Vision]] | Direct phase entry, same-Pawn phase survival, public Recovery and living-world promise. |

Shadow migration logs old/new decision parity, switches authority atomically, then removes old ticket/sarcophagus/blackout/trace paths. No canonical page is changed by this proposal itself.

## 23. Acceptance

### 23.1. Schema and state completeness

- [ ] Every schema has one owner, one source and total lifecycle including terminal states.
- [ ] Owner registry uses exact resolvers; facts/fences/projections never become second decision owners.
- [ ] Predicate dependency graph is acyclic; `BaseAdmissionServiceable` never reads `CanPublishIngress`.
- [ ] Every state machine defines success, withdrawal, expiry, failure and crash reconciliation where applicable.
- [ ] Target-independent ApproachOffer fields and target-bound EntryQuote/IngressOpportunity fields never overlap semantically.
- [ ] Target-tainted output cannot precede durable DisclosureReceipt and stickiness.
- [ ] All offers in one StickyTargetScope share one target; first-party receipts are all-or-none, roster-sealed and conflicts cannot retarget anyone.
- [ ] One AccountID cannot hold multiple nonterminal bindings or active raid controllers.
- [ ] BreachTransaction has immutable squad decision and separate projection state; all conditional fences pass before COMMIT.

### 23.2. Runtime acceptance

- [ ] Exact 06:00 KIA/finality and arbitration are preserved.
- [ ] No logical body, claim, commitment consumption, tell or occupied seat exists before Breach decision COMMIT.
- [ ] COMMIT-but-unprojected footprints participate in barrier occupancy and later-key phase/Final events; no ACTIVE materialization occurs after 06:00.
- [ ] Every pre-decision party failure aborts/refunds all; every post-decision retry converges on the same materialization.
- [ ] SyncLease begins only with vulnerable SYNCING, and interrupt never pauses TTL or changes evidence.
- [ ] ProtectedManifest is atomic, eligibility-checked and never partial.
- [ ] ProtectedManifest uses immutable decision, separate projection state and full-key Final arbitration.
- [ ] Recovery never creates ProtectedManifest, special shard, room or first standard population.
- [ ] Finite AdministrativeResolution always has deadline, released resources and terminal outcome.

### 23.3. Load-bearing authoring acceptance

- [ ] Every generated variant/revision has matching topology-hash StaticRevisionVariantCertificate, IngressCoverageSubproof, StaticEgressSupplyEnvelopeCertificate, PhaseSpatialMutation and ContinuityAxis proof.
- [ ] Ingress suppression cut exceeds max admissible hostile controllers; runtime veto is never weakened.
- [ ] Thresholds have two independent families/routes, no universal key/observer and at least one family with latent JIT anchors.
- [ ] Every PhaseSpatialMutationSet has equivalent occupancy-safe fallbacks and mandatory NO_SPATIAL_DELTA.
- [ ] One global unique-slot EgressSolvencyBundle covers all component-source demand at publication, phase decision, admission and Breach; component views are disjoint projections.
- [ ] Egress obligations support TIMELY→ALLOCATED_SYNC→REMOVED or WINDOW_FORFEITED_BY_INACTION without pity exit.
- [ ] Every 0→2 and 2→4 transition has at least two competing K/W/C opportunities and a fresh-entry baseline without checklist.
- [ ] Every semantic root retires at most one primary axis and leaves two material debts for all reachable party-ref combinations.
- [ ] Every SearchResolutionGraph is finite, acyclic and uses costly authored evidence actions.
- [ ] ThresholdAnchorAssignment is durable, no-reroll and checks matching static bundle plus current global solvency before FORETOLD.
- [ ] Barrier occupancy snapshot is taken at exact decision key and includes lower-key movement plus pending COMMIT footprints.
- [ ] Forced fallback equivalence covers topology uncertainty, LoS, traversal, objective/reward and all material cost axes.

### 23.4. Low-population and Recovery acceptance

- [ ] Minimal regional service set preserves all three envelopes or explicitly marks one unavailable after fixed collapse order.
- [ ] Existing bodies never move; clocks never reset or merge.
- [ ] SEEDING accepts only first normal standard participation, never Recovery seeding.
- [ ] Recovery certificate is independently prior to binding, target remains ordinary-intake open and active unaffiliated STANDARD participation exists at commit.
- [ ] One existing account_last_thread_slot permits only one unresolved RecoveryCase; no duplicate Recovery owner exists.
- [ ] Recovery certificate includes independence/entropy, matching static bundle and recovery global solvency; sparse activity is not claimed immune to alts.
- [ ] RecoveryCase absolute expiry participates in PREPARED/COMMIT/success arbitration and RecoveryResolution releases Case/Presence/Claim/lease/slot exactly once without manifest.
- [ ] Globally terminal target requires GlobalTargetUnusableCertificate before server-authorized unbound search.

### 23.5. Player-facing acceptance

- [ ] Projection contains one headline, one human reason, optional one deadline, exact loss and one primary action.
- [ ] No backend ID/code, raw population, rebind count/reason/timing or certificate state leaks.
- [ ] Party blocker reveals only who/what.
- [ ] Players distinguish terms changed, window closed, no valid crossing, connection, technical delay and system refund.
- [ ] Phase no-spatial fallback, Threshold reset/fade and late lethal denial remain causally readable.

### 23.6. Legacy removal acceptance

- [ ] No Access Contract/ticket type remains authority.
- [ ] No sarcophagus/coffin/lift/safe room/Wake Up/invulnerability/Blackout/relocation/Trace rejoin remains in active flow.
- [ ] No separate entry/exit instance room, protected crossing, survivor time buff, partial manifest or repeat AccountID participation exists.

## 24. Итоговое решение

Eldraine raid — rolling public living pool, чей target service set стремится сохранять три одновременно serviceable phase envelopes; degraded region явно помечает envelope unavailable и никогда не подменяет его. Игрок выбирает target-independent Подход, получает shared-scope sticky target и затем подтверждает immutable quote. Один durable Breach decision, matching static variant bundle и global unique-slot solvency witness связывают вход, phase и egress. Phase survival сохраняет только earned K/W/C; Recovery использует existing account slot и ordinary public session без собственного мира. Final Stabilization в 06:00 остаётся абсолютным terminal event.
