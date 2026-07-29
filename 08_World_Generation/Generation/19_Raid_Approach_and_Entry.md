---
type: system_contract
status: active
index_route: owner
index_group: world_generation
index_order: 290
index_summary: "Задаёт правила и последствия системы «Raid Approach and Entry»."
read_when: "Читайте при изменении входов, состояний, стоимости или последствий системы «Raid Approach and Entry»."
system: raid_ingress
tags:
  - raid
  - ingress
  - approach
  - target_binding
  - entry_quote
  - migration_foundation
related_files:
  - "[[08_World_Generation/Generation/07_Server_Lifecycle|Server Lifecycle]]"
  - "[[08_World_Generation/Anomaly/13_Insertion_Logic|Insertion Logic]]"
  - "[[08_World_Generation/Generation/20_Egress_Solvency|Egress Solvency]]"
  - "[[08_World_Generation/_Registries/Registry_Raid_Interfaces|Raid interfaces]]"
---
# Raid Approach and Entry

> Active focused owner for approach, target disclosure, target-bound quote and finite administrative resolution.

## Responsibility

`APPROACH_OFFER_RESOLVER` owns target-independent `ApproachOffer`; `TARGET_BINDING_RESOLVER` owns `StickyTargetScope`, `TargetBinding`, and `DisclosureReceipt`; `ENTRY_QUOTE_RESOLVER` owns immutable target-bound `EntryQuote`; `ADMINISTRATIVE_RESOLUTION_RESOLVER` owns the finite post-disclosure technical outcome.

It does **not** own hidden ingress opportunities, admission holds, candidates, physical target admission, `BreachTransaction`, body/Presence creation, commitments, capacity, Seal/Dawn order, or normal-egress solvency. Physical admission and the durable `COMMIT|ABORT` decision remain `INSERTION_BREACH_COORDINATOR` work in the generic raid-ingress path.

## Approach and disclosure boundary

An `ApproachOffer` is selected before a target is known. It carries the approach terms, phase-envelope forecast, declared route debt, applicable commitment reference and conservative cutoff, but never reserves a session, seat, candidate, gear, or commitment.

All offers in one account-or-sealed-party sector/envelope/service scope share one `StickyTargetScopeID`. Before target disclosure, client-visible output cannot reveal a target fingerprint. One equivalent opaque rebind is permitted before any target-tainted output; it is never player-visible.

The first target-tainted output atomically writes a `DisclosureReceipt` for every sealed-roster member and makes the scope target-sticky before that output is sent. Changing approach, restarting the client, or disbanding/re-forming the party does not clear the receipt. A declined quote releases admission-related resources but leaves target stickiness until expiry or a durable global release.

## Target-bound quote

`EntryQuote` is created only for the disclosed sticky target. It is immutable and binds the current session/revision/opportunity, Pawn and squad snapshots, loadout snapshot, current and next environment, exact loss state, time bounds, and commit cutoff.

Any player-relevant term change supersedes the quote and requires reconfirmation. A resume may issue a new quote only for the same binding and target epoch. The quote is information and consent; it is not a physical admission or a Breach decision.

## Finite administrative resolution

After disclosure, a technical or post-disclosure candidate failure opens `AdministrativeResolution`. It has a server-owned reason, an effective deadline bounded by the original deadline, stickiness expiry, phase cutoff, and Seal, and exactly one terminal outcome:

- `RESUME_SAME_TARGET`;
- `WITHDRAWN_STICKY` or `FAIL_REFUND`;
- `SYSTEM_TERMINAL_FAILURE`.

Opening the resolution releases seat, candidate, and admission resources; an unconsumed commitment remains releasable. Retargeting is forbidden except after the durable global-target-unusable authorization. Retrying or resuming never resets the deadline.

## Consumer handoff

After player confirmation, the target-bound quote is consumed by the admission/breach path. That path must separately validate current availability, solvency, candidate assignment, and all commit fences before it may create a durable Breach decision.

## Non-ownership

This contract preserves the accepted distinction between intent/disclosure and physical entry. Future specialized UI projection is `MISSING_OWNER:UI_PROJECTION`; it may present these facts but cannot decide them.
