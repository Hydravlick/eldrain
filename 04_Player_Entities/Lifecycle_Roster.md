---
type: system_contract
status: active
system: player_lifecycle_roster
tags: [roster, permadeath, readiness, presence, recovery, life_closure]
related_files:
  - "[[04_Player_Entities/Last_Thread_Recovery|Last Thread Recovery]]"
  - "[[04_Player_Entities/Lifecycle_Resolver|Lifecycle Resolver]]"
  - "[[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]]"
  - "[[04_Player_Entities/Life_Closure|Life Closure]]"
  - "[[04_Player_Entities/Spawn_Logic|Spawn Logic]]"
  - "[[08_World_Generation/Generation/19_Raid_Approach_and_Entry|Raid Approach and Entry]]"
  - "[[08_World_Generation/Anomaly/13_Insertion_Logic|Insertion Logic]]"
---
# Lifecycle Roster

> Active owner of roster membership, readiness, Pawn Presence, terminal projection, and the one account-level Last Thread slot. A roster is a population of named people, not an active deck.

## Responsibility

`LIFECYCLE_ROSTER` owns roster membership and derived counts; `readiness`, deployability and the authoritative `PawnPresenceLease` projection; the account's single `account_last_thread_slot` and its exactly-once release after a terminal Recovery result; and projection of terminal `KIA`, `LOST_CLOSED`, and living `CLOSED_CIVIC` states from their owning resolvers.

It does **not** classify a lethal event, accept a Recovery request, create or resolve a `RecoveryCase`, bind Recovery to a raid, set its clock, own `LifeClosure` readiness or write a separate personal-history record. It also does not impose active slots, a Shell Deck, or a Reserve state.

## Pawn record and Presence

Each Pawn keeps independent identity axes: origin, civic status, field profile, personal tags, lifecycle state, and physical loadout preparation. None is a value rating or a right to deploy.

```yaml
PawnLifecycle:
  pawn_id: PawnID
  account_id: AccountID
  readiness: READY | IN_RAID | MIA | CARE | CLOSED | KIA | LOST_CLOSED
  presence_lease:
    state: HUB | RAID | RECOVERY_TRANSIT | CARE | TERMINAL
    session_id: null | SessionID
    entity_id: null | EntityID
    presence_epoch: PresenceEpoch
  terminal_projection: null | KIA | LOST_CLOSED | CLOSED_CIVIC

AccountLifecycle:
  account_id: AccountID
  account_last_thread_slot: EMPTY | CaseID
```

`UNIQUE_ACTIVE(PawnID)` is mandatory: one Pawn can have no more than one non-terminal Presence. `RECOVERY_TRANSIT` is not a raid body and is not a completed or accepted Recovery Case; it is only the roster projection after the atomic source-raidside handoff has finished.

## Readiness and derived counts

```text
ReadySelectable(AccountID) = all roster Pawns where
  readiness = READY
  AND Presence.state = HUB
  AND terminal_projection = null

ReadyCount = count(ReadySelectable)
RecoverablePawnCount = count(Pawns referenced by an unresolved Case)
LivingCareCount = count(Pawns where readiness = CARE)
```

`ReadySelectable` covers the full roster. A player may deliberately maintain a broad library of known specialists; no hidden three-slot cap or UI grouping can turn living members into non-members. A prepared loadout or unavailable item does not change roster membership; ordinary Hub settlement does not change readiness. The occupied account Last Thread slot merely makes Last Thread unavailable for another Pawn until its Case resolves.

## State projection

```text
ADMITTED → READY ↔ IN_RAID
IN_RAID → CARE | MIA | KIA | RECOVERY_TRANSIT
RECOVERY_TRANSIT → IN_RAID (only after ordinary Breach COMMIT) | CARE | KIA | LOST_CLOSED
CARE → READY
READY → CLOSED (only after Life Closure result)
KIA | LOST_CLOSED | CLOSED are terminal roster states
```

`MIA` denotes an authored unresolved fate outside Last Thread and does not by itself create a Case. `CLOSED` is a living civic outcome, never a death alias. A terminal state is projected only from the owner that resolves it; UI, tags, quests and equipment cannot write it directly.

## Account Last Thread slot

The account owns exactly one slot, initially `EMPTY`. An eligibility check or prepared intercept does not reserve it. During final atomic Case acceptance, this owner alone performs versioned `CAS(EMPTY → CaseID)` in the same commit that removes the source Presence and creates the Case. A failed CAS aborts the whole intercept; there is no intermediate `RESERVED` state to strand.

On immutable `RecoveryResolution(result, terminal_pawn_outcome, cause_ref)`, this owner releases the same `CaseID` exactly once and projects the supplied Pawn outcome without choosing between `CARE`, `KIA` or `LOST_CLOSED`.

No accepted Case exists while the source `PawnPresenceLease` remains `RAID`. Participation/custody/physical-entity/Case changes are first prepared without visible effects; after the final slot precondition succeeds, one atomic commit simultaneously projects the lease to `RECOVERY_TRANSIT`, CASes `EMPTY → CaseID`, accepts the Case and exposes every prepared source projection. Any failed leg aborts the whole handoff and leaves the source raid authoritative.

## Continuity admission boundary

Recruitment remains a separate owner. It may read only the derived predicate:

```text
ContinuityAdmissionAllowed =
  ReadyCount == 0
  AND RecoverablePawnCount == 0
  AND LivingCareCount == 0
  AND PendingAdmissionCount == 0
```

It cannot use deliberate death, Closure, a Recovery transition, or temporary presentation state to mint a replacement. A new Ward is another person and inherits neither identity, tags, gear nor unresolved obligations.

## Direct handoffs

- [[04_Player_Entities/Lifecycle_Resolver|Lifecycle Resolver]] supplies authoritative lethal and STANDARD Dawn outcomes; this owner only projects them.
- [[04_Player_Entities/Last_Thread_Recovery|Last Thread Recovery]] supplies a prepared intercept and source-handoff proofs; it cannot reserve or mutate the slot.
- [[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]] supplies deterministic `CaseID` for the final atomic CAS and emits one immutable terminal result; it never owns the slot.
- [[04_Player_Entities/Life_Closure|Life Closure]] emits an irreversible living closure result; it never writes roster membership or a separate personal-history record.
- [[08_World_Generation/Anomaly/13_Insertion_Logic|Insertion Logic]] owns `PhysicalRaidEntity` materialization and publishes ordinary Breach `COMMIT`. `LIFECYCLE_ROSTER` consumes that fact and alone projects the corresponding `PawnPresenceLease`. These are distinct records. [[08_World_Generation/Generation/19_Raid_Approach_and_Entry|Raid Approach and Entry]] owns only Approach/Binding/Quote and cannot create either.
