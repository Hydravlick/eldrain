---
type: system_contract
status: active
index_route: owner
index_group: economy_loot
index_order: 110
index_summary: "Задаёт правила и последствия системы «Return Manifest Contract»."
read_when: "Читайте при изменении входов, состояний, стоимости или последствий системы «Return Manifest Contract»."
system: extraction_return
tags:
  - extraction
  - return_manifest
  - custody
  - dawn
  - threshold
related_files:
  - "[[04_Player_Entities/Lifecycle_Resolver|Lifecycle Resolver]]"
  - "[[04_Player_Entities/Last_Thread_Recovery|Last Thread Recovery]]"
  - "[[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]]"
  - "[[06_Economy_Loot/Extraction_Stabilization_Loop|Extraction Stabilization Loop]]"
  - "[[07_Gear_Inventory/Inventory_Architecture|Inventory Architecture]]"
  - "[[08_World_Generation/Generation/20_Egress_Solvency|Egress Solvency]]"
  - "[[08_World_Generation/Anomaly/14_Extraction_System|Extraction System]]"
  - "[[08_World_Generation/_Registries/Registry_Raid_Interfaces|Raid interfaces]]"
---
# Return Manifest Contract

> Active focused owner. `RETURN_MANIFEST` is the sole owner of the physical item-return transaction for Normal Threshold and STANDARD Dawn.

## Responsibility

`EXTRACTION_RETURN_RESOLVER` owns one `ReturnManifest` over the full eligible carried custody graph, including durable preparation, the item-transfer decision/projection, world tombstones, and reconciliation.

It does **not** decide whether a Pawn survives, whether a Threshold is reached, whether a Sync is successful, which items are eligible in the global custody graph, Seal/Dawn order, recovery resolution, personal contract settlement, or loot generation. It consumes those facts from their owners.

## Eligibility and atomicity

Every node of the carried graph must pass the immutable eligibility policy. The transaction has one STANDARD ParticipationClaim and one Presence, one trigger proof, the complete eligible graph, custody locks, and deterministic world-tombstone/projection facts. It commits the graph atomically: partial manifests, protected slots, and duplicate transfer projections are forbidden.

`RECOVERY` is hard-fenced out. It never creates a manifest, cargo return, loot delivery, or standard Dawn reward.

## Normal Threshold

For `NORMAL_THRESHOLD`, the resolver consumes exactly one committed `SyncLease` proof and owns the single `COMMIT|ABORT` item decision. A commit makes the custody transfer and tombstones logically effective together under the resolver's transaction key. This is physical return only; personal contracts remain a separate consumer of their declared trigger policy.

## STANDARD Dawn

For `DAWN`, the resolver first creates a complete `PREPARED_DURABLE` manifest with no logical item transfer and hands its durable reference to [[04_Player_Entities/Lifecycle_Resolver|Lifecycle Resolver]]. That owner may then write its one `DawnSettlementDecision=STANDARD_RETURN` only when the prepared manifest exists.

After that decision, the manifest may only project `COMMIT_DERIVED_FROM_STANDARD_RETURN`; it has no independent Dawn `COMMIT|ABORT` authority. A lethal winning decision discards the prepared record without transfer. Once `STANDARD_RETURN` is committed, technical failure can delay reconciliation but cannot turn the return into loss.

## Boundaries

- Normal Threshold and STANDARD Dawn are the only triggers of `ReturnManifest`.
- Egress solvency admits a pre-Seal envelope; it is not manifest proof.
- Recovery resolution and Apex victory are distinct lifecycle outcomes and cannot deliver items.
- [[04_Player_Entities/Lifecycle_Resolver|Lifecycle Resolver]] owns the survival/settlement decision; this contract owns only its derived physical delivery.
