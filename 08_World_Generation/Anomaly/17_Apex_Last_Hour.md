---
type: system_contract
status: active
index_route: owner
index_group: world_generation
index_order: 120
index_summary: "Задаёт правила и последствия системы «Apex Last Hour»."
read_when: "Читайте при изменении входов, состояний, стоимости или последствий системы «Apex Last Hour»."
system: apex_runtime
tags:
  - apex
  - raid
  - survival
  - conditional_cooperation
  - migration_foundation
related_files:
  - "[[08_World_Generation/Generation/07_Server_Lifecycle|Server Lifecycle]]"
  - "[[08_World_Generation/Generation/20_Egress_Solvency|Egress Solvency]]"
  - "[[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]]"
  - "[[08_World_Generation/_Registries/Registry_Raid_Interfaces|Raid interfaces]]"
---
# Apex Last Hour

> Active focused owner of the sealed-Apex survival grammar. It does not own the Anomaly clock or lifecycle decisions.

## Responsibility

`APEX_DIRECTOR` owns the selected Apex family, its pressure contract, survival-route requirements, authored world-rule changes, and public-action semantics for the sealed cohort.

It does **not** own the Seal clock or its total order, ingress closure, normal-egress bundle retirement, `ReturnManifest`, custody, loot delivery, RecoveryCase, Recovery resolution, or lethal/Dawn settlement decisions. Those are consumed as external facts from their focused owners and `SERVER_LIFECYCLE`.

## Sealed survival contract

At the server-provided Apex transition, no new direct ingress is created. The Director runs a pressure contract for the cohort present at that transition. Pressure is fixed from that cohort under the authored contract and does not scale down in real time after deaths.

Each valid Apex realization provides at least two materially independent survival-route families. A solo player has a complete route; cooperation can improve coverage or execution but must use diminishing returns rather than multiplying invulnerability. Static shelter is not a complete answer: routes require continued survival play under changing pressure.

The MVP family is the authored **Siege/Wall** grammar: global fronts and waves, exhausted positions, movement, service, redirection, and breach. It is not a DPS quota. No future family, family registry, compatibility matrix, numerical pressure corridor, or balance value is created by this page.

## Conditional cooperation

Public actions may help every survivor and have no last-hit owner. PvP and friendly-fire risk remain possible. Removing another player can create positional or custody advantage, but it never lowers the world's pressure budget or produces a shared fail-switch. No player can unilaterally end the event for everyone.

## Basic victory boundary

`APEX_DIRECTOR` supplies one authored `BasicDawnVictoryPredicate`: basic victory is survival to the server's Dawn resolution, not score, contribution, winner slots, or a squad ranking. Lifecycle owners alone evaluate that predicate against each Presence's authoritative facts and resolve the resulting STANDARD, RECOVERY, lethal, or expiry outcome.

The Director has no per-Presence survival-eligibility field, manifest-delivery decision, or Recovery-fate authority. `MISSING_OWNER:UI_PROJECTION` may present the authored predicate and its player-facing state, but cannot evaluate or resolve it.
