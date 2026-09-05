# Editing the local vault

Work in the current Obsidian vault and preserve unrelated user changes. Git is history and recovery; no worktree, branch, commit or remote workflow is required for a document edit. Carry an authorized change through writing, affected consumers and verification. An audit-only request remains a review.

Find the owner, read the relevant contract, apply the accepted decision there, update direct consumers/incoming links, and check the result. Ordinary placement and prose choices are editorial work. Ask only when choosing between materially different game designs is necessary and the user has not already decided.

For an authorized structural refactor, finish one coherent owner and its destinations at a time: read -> classify responsibility -> integrate/move -> rewrite -> remove duplication -> reread. A large preliminary audit or migration manifest is not a substitute for edits. Use [design-architecture.md](design-architecture.md) to classify meaning and [obsidian-workflow.md](obsidian-workflow.md) for file operations.

Destination edits precede source removal. Before removing or substantially compressing a block, account for its unique meaning in an exact destination, establish that it is explicitly superseded, or show that it is a true duplicate. Related ownership alone does not prove equivalent coverage. Preserve rationale, overview, experiential flow, presentation, lore, useful examples and intentional uncertainty. Do not reduce these pages to link hubs.

Read the changed source and destinations together. Preserve accepted rules, IDs, numbers, negations, causal relationships and voice unless their change was authorized. Scripts check mechanics; they do not decide semantic moves or justify deletions. Retire a temporary source only after its useful meaning is integrated and links validate; keep historical evidence when it still has a contextual purpose.

For a proposed design, distinguish reasoning from the adopted rule. For an approved revision, do not reopen the entire design. An actual contradiction or missing runtime responsibility calls for design architecture; straightforward moves and merges do not require another skill.

## Structural naming and placement

Prefer stable semantic filenames for System, Mechanic, Entity, Registry and Feature notes unless a sequence is part of their identity. Numeric prefixes are appropriate for stable domain order, `00_Index` / `00_Routes`, a real lifecycle or pipeline, semantic level/sequence, or required curated reading order. They are not creation timestamps, arbitrary sorting boosts, substitutes for semantic names or obligations inherited from an obsolete GDD. Where metadata/routes express navigation order, do not also encode it in filenames without a semantic reason. Before changing an existing sequence, determine what its numbers mean; never strip them automatically. `01_Difficulty` is reasonable when `01` really means Difficulty 1.

Folders group stable responsibilities or content families, not miscellaneous/archive bins. Domain-first organization remains preferred; do not force `Systems/`, `Mechanics/` and `Content/` into every domain. A subdirectory is useful for an actual family such as Features, Lore, Registries, Views, authored entities/content or tooling support. An underscore prefix grants no authority and must have one explainable structural purpose, not simultaneously mean canonical data, archive, visualization, miscellaneous and special sorting. A later semantic refactor may rename `_Matrices` / `_Registries`; their current names mandate neither retention nor removal.

Exact or near-duplicate structural notes need semantic classification before consolidation. Hash equality is evidence of matching bytes, never deletion permission. Distinguish authored variants, parameterized views, placeholders, template plus instances, accidental copies and superseded duplicates; choose the representation that preserves their actual role. Shared DataviewJS algorithms may become reusable views with thin wrappers, while meaningful parameters and interactive behavior survive.

Design Architect resolves semantic classification, GDD Editor applies accepted naming/placement, and Vault Maintenance performs mechanical migration using the native Obsidian contract in [obsidian-workflow.md](obsidian-workflow.md). Folder shape must not drive gameplay redesign.

Run focused checks after meaningful batches and full relevant validation at the end; see [validation.md](validation.md). Update generated routes from metadata when an authorized move or metadata change affects navigation. Honor an explicit user request to defer regeneration and report the exact pending files; no permanent structural-refactor exception forbids validation.
