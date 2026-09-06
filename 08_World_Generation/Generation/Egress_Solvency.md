---
status: active
system: egress_solvency
tags:
  - raid
  - egress
  - solvency
  - threshold
  - obligations
related_files:
  - "[[08_World_Generation/Generation/Server_Lifecycle|Server Lifecycle]]"
  - "[[08_World_Generation/Anomaly/Extraction_System|Extraction System]]"
  - "[[08_World_Generation/Generation/Raid_Approach_and_Entry|Raid Approach and Entry]]"
  - "[[06_Economy_Loot/Return_Manifest_Contract|Return Manifest Contract]]"
  - "[[08_World_Generation/Registries/Registry_Raid_Interfaces|Raid interfaces]]"
type: system
index_route: owner
index_group: world_generation
index_order: 300
index_summary: "Определяет состояния, разрешение и связи: Egress Solvency."
read_when: Когда нужен контракт «Egress Solvency» и его границы с соседними владельцами.
---
# Egress Solvency

> Active focused owner of the normal-egress solvency envelope. It does not redefine extraction success.

## Responsibility

`EXTRACTION_SOLVENCY_VALIDATOR` owns the pre-Seal egress supply envelope, its global solvency bundle, and each committed Presence's egress coverage obligation. Its only decision is whether the normal-egress envelope is solvent for publication, admission, and a prospective pre-Seal Breach.

It does **not** own Threshold search, anchor assignment, SyncLease creation, extraction success, `ReturnManifest`, item custody, Breakline resolution, physical removal, lethal fate, or Dawn settlement. `SERVER_LIFECYCLE` alone owns Seal/Dawn order; `RETURN_MANIFEST` remains the return transaction owner.

## Supply envelope and bundle

`StaticEgressSupplyEnvelopeCertificate` is the prevalidated, topology-bound lower supply proof for a joinable extraction revision. `EgressSolvencyBundle` combines that envelope with one global, time-expanded witness of live supply and covered demand.

The witness is global: component views are disjoint projections, not independent solvers, and a future Threshold slot cannot be counted twice. The bundle is revalidated when supply, covered demand, time, topology, search/anchor state, Sync reservation, or terminal removal changes. A joinable ingress may be published or committed only when the prospective breach group is covered by the current solvent bundle.

## Obligation lifecycle

Each pre-Seal Breach `COMMIT` creates an `EgressCoverageObligation`. The obligation remains in the normal-egress ledger until `RETURNED_THRESHOLD`, `TERMINAL_REMOVED`, or the Seal transition. Staying in the raid, receiving a quote, or receiving foretell does not erase it.

- `TIMELY` and `ALLOCATED_SYNC` are covered demand and consume witness capacity.
- A server-proven missed latest-start changes the ledger state to `BEST_EFFORT_AFTER_LATEST_START`; it may use surplus only and creates neither reserved capacity nor a pity exit.
- At Seal, lower-key exits and terminal outcomes settle first. The bundle retires, same-or-higher-key ingress/Threshold/Breakline work cannot proceed, and every remaining living Presence becomes `APEX_BOUND` for this ledger.
- Dawn consumes an immutable lifecycle or recovery terminal-resolution reference and projects `APEX_BOUND` to `DAWN_RESOLVED` or `TERMINAL_REMOVED`. Dawn is never supply, a Threshold slot, or an admission remedy.

## Invariants

1. A normal pre-Seal admission cannot be mathematically insolvent.
2. `BEST_EFFORT_AFTER_LATEST_START` is visible in the ledger but excluded from covered capacity.
3. The bundle retires only at Seal; it cannot provide capacity for sealed Apex.
4. Solvency authorizes an admissible envelope, not a successful extraction or a returned item.

## Consumer handoff

The generic raid-ingress path consumes the solvent bundle as a pre-commit fence. The Threshold/extraction path consumes the ordinary supply facts under its own authority. The return contract consumes an extraction or lifecycle trigger proof, never this validator's permission as proof of success.
