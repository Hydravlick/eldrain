---
type: interface_registry
status: active
system: raid_interfaces
coverage_status: active_with_explicit_gaps
tags:
  - raid
  - interfaces
  - ownership
  - migration
related_files:
  - "[[04_Player_Entities/Lifecycle_Resolver|Lifecycle Resolver]]"
  - "[[04_Player_Entities/Last_Thread_Recovery|Last Thread Recovery]]"
  - "[[08_World_Generation/Generation/19_Raid_Approach_and_Entry|Raid Approach and Entry]]"
  - "[[08_World_Generation/Generation/20_Egress_Solvency|Egress Solvency]]"
  - "[[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]]"
  - "[[06_Economy_Loot/Return_Manifest_Contract|Return Manifest Contract]]"
  - "[[08_World_Generation/Anomaly/17_Apex_Last_Hour|Apex Last Hour]]"
---
# Registry: Raid Interfaces

> Active registry of directional handoffs between focused raid owners. Rows with `pending_owner` or `missing_owner` remain explicit gaps and grant no authority.

## Owner-ID convention

Owner IDs are uppercase snake case. `PENDING_OWNER:` names a planned, explicitly identified owner page that does not yet exist. `MISSING_OWNER:` names an interface owner not yet assigned to a page. Neither marker is a wikilink.

| interface_id | producer_owner_ref | consumer_owner_ref | fact_or_decision_ref | trigger | authority_boundary | status |
|---|---|---|---|---|---|---|
| `RAID_IF_001` | `APPROACH_OFFER_RESOLVER` | `TARGET_BINDING_RESOLVER` | `ApproachOffer` | offer selected | Consumer may bind a hidden target; producer never chooses one. | `active` |
| `RAID_IF_002` | `TARGET_BINDING_RESOLVER` | `ENTRY_QUOTE_RESOLVER` | `TargetBinding` and all-or-none `DisclosureReceipt` | first target-tainted disclosure | Quote is impossible before durable receipt; consumer cannot alter stickiness. | `active` |
| `RAID_IF_003` | `ENTRY_QUOTE_RESOLVER` | `INSERTION_ADMISSION_RESOLVER` | confirmed immutable `EntryQuote` | player confirmation and client readiness | Admission may hold capacity only; it cannot change quote facts. | `active` |
| `RAID_IF_004` | `INSERTION_ADMISSION_RESOLVER` | `INSERTION_BREACH_COORDINATOR` | `AdmissionHold` | final breach preparation | Hold is not a body, Presence, claim, or Breach decision. | `active` |
| `RAID_IF_005` | `ADMINISTRATIVE_RESOLUTION_RESOLVER` | `TARGET_BINDING_RESOLVER` | finite same-target or global-release outcome | post-disclosure failure | Resolution cannot retarget without global-unusable authorization. | `active` |
| `RAID_IF_006` | `INSERTION_BREACH_COORDINATOR` | `EXTRACTION_SOLVENCY_VALIDATOR` | prospective `ProspectiveBreachGroup` facts | admission and pre-commit Breach fence | Validator calculates a solvency fence; producer has created neither a Presence nor an obligation. | `active` |
| `RAID_IF_007` | `EXTRACTION_SOLVENCY_VALIDATOR` | `INSERTION_BREACH_COORDINATOR` | solvent `EgressSolvencyBundle` | admission and final Breach fence | Solvency permits an envelope; it is not an entry decision. | `active` |
| `RAID_IF_019` | `INSERTION_BREACH_COORDINATOR` | `EXTRACTION_SOLVENCY_VALIDATOR` | immutable `BreachTransaction=COMMIT` and committed `PhysicalRaidEntity` fact | post-COMMIT | Validator creates the `EgressCoverageObligation`; coordinator remains the only physical-commit owner. | `active` |
| `RAID_IF_008` | `SERVER_LIFECYCLE` | `EXTRACTION_SOLVENCY_VALIDATOR` | Seal/Dawn ordered barrier facts | lifecycle barrier | Validator retires its bundle and projects obligations; it does not set the clock. | `active` |
| `RAID_IF_009` | `EXTRACTION_RESOLVER` | `EXTRACTION_RETURN_RESOLVER` | committed `SyncLease` | Normal Threshold extraction | Manifest owns item return, not Sync success. | `active` |
| `RAID_IF_020` | `EXTRACTION_RETURN_RESOLVER` | `LIFECYCLE_RESOLVER` | `PREPARED_DURABLE ReturnManifestRef` | complete STANDARD Dawn manifest preparation | Lifecycle may decide `STANDARD_RETURN` only after this durable handoff; manifest has made no Dawn transfer decision. | `active` |
| `RAID_IF_010` | `LIFECYCLE_RESOLVER` | `EXTRACTION_RETURN_RESOLVER` | `DawnSettlementDecision=STANDARD_RETURN` | Dawn settlement | Manifest commit is derived; it cannot decide survival. | `active` |
| `RAID_IF_011` | `LAST_THREAD_RECOVERY` | `RECOVERY_LIFECYCLE` | idempotent `RecoveryRequest` | eligible lethal intercept | Recovery accepts/rejects Cases; Last Thread does not run Case lifecycle. | `active` |
| `RAID_IF_012` | `LIFECYCLE_ROSTER` | `RECOVERY_LIFECYCLE` | versioned `account_last_thread_slot=EMPTY` fact and final `CAS(EMPTY → CaseID)` result | atomic RecoveryCase acceptance | No pre-acceptance reservation exists; Roster alone mutates the slot in the same commit that accepts the Case. | `active` |
| `RAID_IF_021` | `RECOVERY_LIFECYCLE` | `LIFECYCLE_ROSTER` | immutable terminal `RecoveryResolution(result, terminal_pawn_outcome, cause_ref)` | Recovery terminal resolution | Roster projects the supplied Pawn outcome and releases its own slot exactly once; it cannot choose or redefine the recovery result. | `active` |
| `RAID_IF_022` | `LAST_THREAD_RECOVERY` | `LIFECYCLE_ROSTER` | prepared intercept, deterministic `CaseID` and source-handoff proofs | final atomic acceptance | Roster owns `CAS(EMPTY → CaseID)` and Pawn Presence projection; coordinator owns neither slot nor terminal projection. | `active` |
| `RAID_IF_023` | `RECOVERY_LIFECYCLE` | `LIFECYCLE_ROSTER` | prepared deterministic `CaseID` and final acceptance fact | atomic RecoveryCase acceptance | `PawnPresenceLease=RECOVERY_TRANSIT`, slot CAS and Case acceptance become visible in the same commit; Roster owns only its lease and slot projections. | `active` |
| `RAID_IF_024` | `LAST_THREAD_RECOVERY` | `INSERTION_BREACH_COORDINATOR` | `PreparedRecoveryInterceptRef` | atomic source handoff preparation | Participation owner prepares terminalization while keeping its lifetime claim consumed; Last Thread cannot mutate the claim. | `active` |
| `RAID_IF_025` | `INSERTION_BREACH_COORDINATOR` | `LAST_THREAD_RECOVERY` | `PREPARED_DURABLE SourceParticipationTerminalization` | source participation preparation | Prepared record changes no visible state; coordinator cannot author or reinterpret it. | `active` |
| `RAID_IF_026` | `LAST_THREAD_RECOVERY` | `INVENTORY_CUSTODY` | `PreparedRecoveryInterceptRef` and source custody graph | atomic source handoff preparation | Custody owner prepares contestable world placement; Last Thread owns no body, gear, cargo or wreck. | `active` |
| `RAID_IF_027` | `INVENTORY_CUSTODY` | `LAST_THREAD_RECOVERY` | `PREPARED_DURABLE SourceWreckCustodyTransition` | source custody preparation | Prepared record changes no visible state; coordinator cannot change item eligibility, placement or custody. | `active` |
| `RAID_IF_029` | `LAST_THREAD_RECOVERY` | `INSERTION_BREACH_COORDINATOR` | `AtomicRecoveryInterceptCommitRef` | final atomic intercept commit | Participation and `PhysicalRaidEntity` terminalization become visible with Case acceptance; Last Thread cannot author their contents. | `active` |
| `RAID_IF_033` | `LAST_THREAD_RECOVERY` | `INVENTORY_CUSTODY` | `AtomicRecoveryInterceptCommitRef` | final atomic intercept commit | Prepared world custody becomes visible with Case acceptance; Last Thread cannot change the prepared custody graph. | `active` |
| `RAID_IF_028` | `RECOVERY_LIFECYCLE` | `INSERTION_BREACH_COORDINATOR` | immutable terminal `RecoveryResolution` | Recovery raid-body terminal resolution | Insertion owner terminal-removes `PhysicalRaidEntity` and keeps the lifetime ParticipationClaim consumed; Recovery cannot mutate either. | `active` |
| `RAID_IF_030` | `LIFECYCLE_RESOLVER` | `LAST_THREAD_RECOVERY` | immutable `LethalDisposition=FIELD_RECOVERABLE` | eligible lethal classification | Only this disposition permits an intercept; Last Thread cannot classify the lethal event. | `active` |
| `RAID_IF_031` | `LIFECYCLE_RESOLVER` | `LIFECYCLE_ROSTER` | immutable terminal lethal or STANDARD Dawn Pawn outcome | lifecycle terminal decision | Roster projects the supplied outcome; it cannot choose survival, KIA or LOST_CLOSED. | `active` |
| `RAID_IF_032` | `SERVER_LIFECYCLE` | `LIFECYCLE_RESOLVER` | ordered Dawn barrier and authoritative Presence facts | Dawn barrier committed | Resolver decides per-Presence STANDARD outcome; server owner keeps clock and total-order authority. | `active` |
| `RAID_IF_013` | `REGIONAL_SCHEDULER` | `RECOVERY_LIFECYCLE` | independently minted `PublicActivityCertificate` | target search/binding | Recovery cannot seed or certify a public target. | `active` |
| `RAID_IF_014` | `RECOVERY_LIFECYCLE` | `INSERTION_BREACH_COORDINATOR` | validated `RecoveryBindingAttempt` | Recovery breach preparation | Generic ingress owns target admission and `Breach`; Recovery owns no private ingress. | `active` |
| `RAID_IF_015` | `RECOVERY_LIFECYCLE` | `EXTRACTION_SOLVENCY_VALIDATOR` | immutable `RecoveryResolution` | Dawn or terminal recovery resolution | Validator closes an Apex-bound obligation; it cannot choose Recovery fate or clock semantics. | `active` |
| `RAID_IF_016` | `SERVER_LIFECYCLE` | `APEX_DIRECTOR` | sealed-Apex transition and cohort fact | Seal barrier committed | Director consumes the transition; it does not own the Seal clock or ingress close. | `active` |
| `RAID_IF_017` | `APEX_DIRECTOR` | `MISSING_OWNER:UI_PROJECTION` | family/pressure and survival-route presentation facts | Apex foretell and sealed play | Presentation may explain the state but cannot select family or pressure. | `missing_owner` |
| `RAID_IF_018` | `APEX_DIRECTOR` | `LIFECYCLE_RESOLVER` | authored `BasicDawnVictoryPredicate` | server Dawn barrier | Lifecycle evaluates each Presence against its own facts; Apex owns neither survival eligibility nor an outcome. | `active` |

## Registry constraints

Every row names one producer and one consumer. This registry stores neither a duplicate state machine nor a fallback owner. `UR-001`, `UR-002`, and `UR-003` remain unresolved in [[09_Project_Management/Refactor_Unresolved_Registry_2026-07-23|the unresolved registry]] and are not resolved by an interface row.
