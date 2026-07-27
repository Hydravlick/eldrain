---
type: system_contract
status: active
system: player_recovery
tags:
  - recovery
  - last_thread
  - lifecycle
  - public_raid
  - migration_foundation
related_files:
  - "[[04_Player_Entities/Last_Thread_Recovery|Last Thread Recovery]]"
  - "[[04_Player_Entities/Lifecycle_Resolver|Lifecycle Resolver]]"
  - "[[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]]"
  - "[[08_World_Generation/Generation/19_Raid_Approach_and_Entry|Raid Approach and Entry]]"
  - "[[08_World_Generation/Generation/20_Egress_Solvency|Egress Solvency]]"
  - "[[08_World_Generation/Anomaly/17_Apex_Last_Hour|Apex Last Hour]]"
  - "[[08_World_Generation/_Registries/Registry_Raid_Interfaces|Raid interfaces]]"
---
# Recovery Lifecycle

> Active focused owner of RecoveryCase lifecycle. This page establishes no new account slot and does not choose the unresolved Recovery clock semantics.

## Responsibility

`RECOVERY_LIFECYCLE` owns the public `RecoveryCase`, target search, append-only recovery binding attempts, expiry handling, and exactly-once recovery resolution.

[[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]] owns Pawn/Presence state, the account-level Last Thread slot, and derived roster counts. [[04_Player_Entities/Last_Thread_Recovery|Last Thread Recovery]] owns the personal lethal intercept and idempotent `RecoveryRequest`. Generic raid ingress owns target admission and `Breach`; Recovery does not create a private shard, room, queue, or special physical-target rule.

Recovery does **not** own `ReturnManifest`, cargo, loot delivery, standard rewards, normal-egress success, Breakline, Seal/Dawn order, or the account slot itself.

## Case and binding attempts

A `RecoveryRequest` may be rejected without creating a `RecoveryCase` or changing the account slot. This owner derives one deterministic `CaseID` for the intercept transaction and prepares the Case, but acceptance becomes visible only in the final atomic commit where [[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]] succeeds with `CAS(EMPTY → CaseID)` and all source-handoff participants commit. A failed CAS or failed participant aborts every leg. The Case records its source Pawn/session, account-slot reference, visible deadline field, state and terminal-resolution reference. This page never reserves or creates an account slot.

`RecoveryBindingAttempt` is append-only and binds a Case to a normal public target only through the ordinary target/breach path. Binding requires independently observed ordinary STANDARD activity and a serviceable public target; Recovery cannot seed a session. A stale target attempt can resume only through the finite same-target administrative path. A globally terminal target needs the durable global-unusable authorization before a new unbound search is allowed.

## Resolution boundary

`RECOVERY_LIFECYCLE` writes one immutable terminal record:

```yaml
RecoveryResolution:
  result: RECOVERED | FAILED | EXPIRED
  terminal_pawn_outcome: CARE | KIA | LOST_CLOSED
  cause_ref: WorldResolutionRef
```

`RECOVERED` requires `terminal_pawn_outcome=CARE`. `FAILED` and `EXPIRED` consume authoritative [[04_Player_Entities/Lifecycle_Resolver|lifecycle]] or world cause and must already choose `KIA` or `LOST_CLOSED`; they cannot leave this choice to the roster. [[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]] only projects the supplied Pawn/roster Presence outcome and releases its own matching `CaseID` slot exactly once. ParticipationClaim and any system lease are closed through their own owners, never through the roster. A successful Recovery never creates a `ReturnManifest`, cargo return, loot delivery, or STANDARD reward.

If a Recovery Presence exists when the session enters Apex, it remains an ordinary vulnerable Presence under the public raid's phase handling. The recovery resolution path, not a parallel Dawn settlement, resolves its final Recovery outcome. Lethal precedence and any adopted expiry rule must be applied through the authoritative server order.

## Explicit unresolved branch — UR-002

`UR-002` remains unresolved: whether Recovery expiry is an absolute Case deadline from Case creation, including search and binding, or whether the active clock starts only after a valid committed Recovery entry/physical Presence. This active contract records both branches but selects neither.

Until an author decision is made, `expires_at`, clock start, pause behavior, and expiry-versus-entry arbitration are **PENDING_DECISION: UR-002**. No implementation or consumer may infer clock semantics from this page. The accepted boundaries above remain valid under either branch.

## Consumer handoff

[[04_Player_Entities/Last_Thread_Recovery|Last Thread Recovery]] supplies `RecoveryRequest`; the public ingress path consumes a validated binding attempt; the solvency owner reads the immutable terminal-resolution reference only to close its Apex-bound obligation. None of these consumers may redefine a Case, attempt history, expiry, or recovery result.
