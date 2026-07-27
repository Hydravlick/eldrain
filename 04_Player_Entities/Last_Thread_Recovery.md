---
type: system_contract
status: active
system: last_thread_recovery
tags: [lifecycle, recovery, permadeath, lethal_intercept]
related_files:
  - "[[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]]"
  - "[[04_Player_Entities/Lifecycle_Resolver|Lifecycle Resolver]]"
  - "[[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]]"
  - "[[08_World_Generation/Anomaly/13_Insertion_Logic|Insertion Logic]]"
  - "[[07_Gear_Inventory/Inventory_Architecture|Inventory Architecture]]"
  - "[[08_World_Generation/_Registries/Registry_Raid_Interfaces|Raid Interfaces]]"
---
# Last Thread Recovery

> Active coordinator of the one eligible lethal intercept. Last Thread prevents no loss: it moves the Pawn from a lost source raid into one public Recovery fate, if the atomic handoff can be completed.

## Responsibility

`LAST_THREAD_RECOVERY` owns lethal-intercept eligibility, idempotent `RecoveryRequest`, and coordination of the cross-owner source transaction. It does **not** own `RecoveryCase`, target search or binding, clock semantics, Recovery result, roster counts, the account slot, physical entry, loot, cargo, or a player's KIA decision.

## Eligibility and authority

Combat and attackers publish `LethalEvent` facts only. [[04_Player_Entities/Lifecycle_Resolver|Lifecycle Resolver]] alone publishes immutable `LethalDisposition`. A hostile, friendly, self-inflicted, headshot, overdamage, corpse interaction, distance, or attribution may never directly write `KIA` or force an intercept.

Last Thread may submit one request only when all are true:

- authoritative `LethalDisposition.outcome` is `FIELD_RECOVERABLE`;
- the Pawn has a source raid Presence and no terminal source result;
- the account slot observed from `LIFECYCLE_ROSTER` is `EMPTY`;

The request is idempotent by `LethalEventID × PawnID`. It has no player-facing action that lets another player "confirm death". A rejected request leaves the source disposition to its owner and creates neither Case nor slot claim.

## Atomic intercept handoff

```text
eligible LethalEvent
→ observe versioned EMPTY account slot; no reservation is written
→ INSERTION_BREACH_COORDINATOR prepares source ParticipationClaim terminalization and PhysicalRaidEntity removal
→ INVENTORY_CUSTODY prepares source body, gear and cargo transition to contestable world custody
→ RECOVERY_LIFECYCLE prepares deterministic CaseID and Case record
→ validate final CAS precondition
→ one AtomicRecoveryInterceptCommitRef makes Participation/custody/PhysicalRaidEntity projections, CAS EMPTY → CaseID, Case acceptance and PawnPresenceLease=RECOVERY_TRANSIT visible together
```

All legs are one transaction coordinated by Last Thread but decided by their existing owners. `LAST_THREAD_RECOVERY` cannot reserve the account slot, mutate a ParticipationClaim, remove a `PhysicalRaidEntity`, change `PawnPresenceLease` or assign item custody. It consumes `PREPARED_DURABLE SourceParticipationTerminalization` and `PREPARED_DURABLE SourceWreckCustodyTransition`; neither prepared record changes visible state. One `AtomicRecoveryInterceptCommitRef` makes every projection visible together.

Before completion, the source Pawn/Presence remains unresolved in its source raid and no accepted Case exists. A technical interruption creates no partial accepted Case and may resume only the same idempotent transaction toward its one committed or rejected result; it never mints a second request, free attempt, loot protection, source-reroll or second Presence.

After commit, the same Pawn may never re-enter the source SessionID. The attacker keeps the source victory and contestable physical custody, but no right to declare the Pawn dead.

## Boundaries

- One unresolved account slot means other READY Pawns remain selectable, but their own Last Thread intercept is unavailable and visible before commitment.
- Last Thread is not resurrection, an extra life, Breakline, a private room, a Recovery queue, or a reward route.
- Recovery itself has no normal loot, cargo, tag reveal, First Return, or STANDARD return.
- `UR-002` clock semantics belong exclusively to [[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]] and remain unresolved.

## Handoff

The coordinator emits a validated, idempotent `RecoveryRequest` and the same `PreparedRecoveryInterceptRef` to the participation/physical-entity, roster-lease and custody owners. It waits for their prepared durable records but cannot author them. After every participant is prepared and the slot CAS is still valid, it emits one `AtomicRecoveryInterceptCommitRef`. [[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]] alone accepts or rejects the Case and later writes its terminal outcome.
