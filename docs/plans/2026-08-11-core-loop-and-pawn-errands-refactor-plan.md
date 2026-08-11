# Core Loop and Pawn Errands Refactor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Eldrain's first playable loop legible as a sequence of player decisions, while defining Pawn errands as one bounded, physical Hub interaction rather than an unowned background-minigame.

**Architecture:** Keep the existing distributed canonical corpus. `02_Core_Loop` becomes the concise player-facing orchestration page; specialist owners retain the rules they already own. Add one narrow canonical owner for an errand lease only after the ownership decision gate. The Hub map renders route and POI state but never becomes the source of Pawn availability, rewards, or contract outcome.

**Tech Stack:** Markdown corpus, internal links/frontmatter, existing Python standard-library contract tests, `tools/build_routes.py`, `tools/vault_guard.py`, and the local vault-curator validators.

## Global Constraints

- Preserve one canonical owner per rule. Do not make `00_Index.md` or route projections authoritative or edit them manually.
- **Management baseline complete:** closed risks and completed active-plan steps have been removed from the working surface. R65 is the active guardrail for Pawn errands; R22 remains a deferred social-Hub boundary and is out of scope.
- Do not perform a corpus-wide prose rewrite. Rewrite only the player-facing summaries and the new errand contract; retain canon/lore unless a migrated rule makes a specific paragraph redundant.
- Separate registers in every changed page: player action and visible feedback first; state, ownership, formulas and edge cases second; diegetic wording only where it is presentation copy.
- `Pawn Errand` is a visualized hand-off in the Hub, not passive income, an idle timer, a second raid, or a replacement for a player-run contract.
- Preserve the existing guarantees: `ReadySelectable` is the only deployment predicate; the map does not assign Pawns; contracts must not create daily-FOMO or safe profit (R65).
- Any unresolved choice must be recorded as `APPROVAL_REQUIRED`, not hidden in prose. In particular, do not invent duration, reward, capacity, or failure values before the design checkpoint.

## Proposed Owner Map

| Concern | Proposed owner | Explicit non-owner |
|---|---|---|
| Seven-step player journey and cross-links | `01_Core_Vision/02_Core_Loop.md` | lore pages and the map UI |
| Pawn roster eligibility, deployment exclusion and return to selectable state | `04_Player_Entities/Lifecycle_Roster.md` | Hub map, Quest Engine |
| Errand instance, payload reservation and state transitions | new `04_Player_Entities/Pawn_Errands.md` | Hub map, faction registry |
| Physical route presentation and POI visibility | `08_World_Generation/Hub/01_Hub_Map_Table.md` and `03_Hub_Map_Interaction.md` | Pawn lifecycle and rewards |
| Service/POI availability and settlement | `08_World_Generation/Hub/02_Hub_Services_Interaction.md` | Pawn selection |
| Contract generation and its consequences | `03_Factions_Societies/Quest_Engine.md` | routine errand traversal |
| Return/extraction transaction | `06_Economy_Loot/Extraction_Stabilization_Loop.md`, `Return_Manifest_Contract.md` | errands |

The new `Pawn_Errands.md` is a proposal, not a decision already made. Task 1 must either confirm it or name another single owner before any rule is written.

## Design Target: First Vertical Slice

The refactored loop must be possible to read without opening lore:

1. At the Hub, the player sees available Pawns, current sector/phase, POIs and a readable objective.
2. The player chooses one `ReadySelectable` Pawn, a target and loadout/approach.
3. The player receives an exact entry quote, reads cost and risk, then confirms entry.
4. In the raid, the player scouts, commits to a route/goal, then chooses whether to extract or take a deeper risk.
5. Extraction or a terminal/recovery path resolves the Pawn and custody through existing owners.
6. Back in the Hub, the player sees what changed and chooses the next meaningful action.

The Pawn-errand slice sits beside step 1, not inside the raid. Recommended bounded interaction:

`READY at HUB -> player selects active Hub POI + permitted errand -> atomic commit -> visible walking route -> arrival/re-resolution -> READY or a visible blocked result`.

It must have no automatic recurring assignment and no reward that bypasses extraction. The physical walk conveys cause and destination; it is not an excuse to simulate a second economy.

## Task 1: Establish the ownership and scope decision

**Files:**

- Modify: `09_Project_Management/TODO.md`
- Modify: `09_Project_Management/Risk_Register.md`
- Read only: `01_Core_Vision/02_Core_Loop.md`, `04_Player_Entities/Lifecycle_Roster.md`, `08_World_Generation/Hub/01_Hub_Map_Table.md`, `08_World_Generation/Hub/02_Hub_Services_Interaction.md`, `08_World_Generation/Hub/03_Hub_Map_Interaction.md`, `03_Factions_Societies/Quest_Engine.md`, `06_Economy_Loot/Extraction_Stabilization_Loop.md`, `06_Economy_Loot/Return_Manifest_Contract.md`

- [ ] Use `eldraine-system-architect` to write a compact decision record in the relevant TODO entry: confirm the owner of `PawnErrandLease`, its direct consumers, and the fact that it is not a contract/raid replacement.
- [ ] Add an in-progress risk entry only if existing R65/R22 do not cover a discovered failure mode. The candidate risk is: a visualized errand silently changes `Ready` availability, duplicates a payload, or produces safe value while the player raids.
- [ ] Mark the following product choices `APPROVAL_REQUIRED` for the design checkpoint: maximum simultaneous errands per account; whether cancel is allowed before departure; whether the user must inspect arrival; intended time scale; and whether any reward exists beyond the selected Hub service outcome.

**Acceptance:** a reviewer can identify exactly one owner for every new field and transition before any implementation prose is added.

## Task 2: Add failing contract tests for the player loop and errands

**Files:**

- Create: `tools/test_core_loop_refactor.py`
- Create: `tools/test_pawn_errands_contract.py`
- Modify: `tools/test_canonical_guidance.py` only if the new active owner needs an expected-route assertion

- [ ] Write tests before editing owners. `test_core_loop_refactor.py` must require a concise `First playable vertical slice` table in `02_Core_Loop.md` with player action, visible feedback, irreversible commit/result, and a link to each specialist owner.
- [ ] Require that the loop table links to roster/readiness, Hub map, raid approach and entry, extraction/return, and Quest Engine without copying their state rules into the core-loop page.
- [ ] Make `test_pawn_errands_contract.py` fail until the selected owner contains: a state machine; preconditions; atomic commit fields; direct consumers; non-ownership; and all required edge cases.
- [ ] Test the minimum edge-case list: Pawn ceases to be `READY`; two commands race for one Pawn; POI/service changes before arrival; player starts a raid; cancellation at each permitted boundary; save/reconnect; payload/inventory reservation; terminal Pawn outcome; map route unavailable; and a resolution which does not mint safe profit.

**Acceptance:** both tests fail for missing design contracts, not for wording or lore style.

## Task 3: Refactor the Core Loop into a player-readable orchestration page

**Files:**

- Modify: `01_Core_Vision/02_Core_Loop.md`
- Modify only if its high-level promise becomes inaccurate: `01_Core_Vision/GDD_Main.md`

- [ ] Add a one-screen `First playable vertical slice` at the top of `02_Core_Loop.md`, before broad promise and phase exposition. Use six player-facing beats from the design target, with columns: `player sees`, `player does`, `system commits`, `immediate feedback`, `owner`.
- [ ] Keep the existing seven raid phases as a detailed reference below the new table, but replace duplicated explanations of state ownership with direct links to their owners.
- [ ] Rewrite only abstract opening statements that conceal an action. Convert them to concrete verbs and observable stakes; retain a maximum of one short atmospheric promise per section.
- [ ] Add a `Core-loop exclusions` paragraph: the loop does not own Pawn lifecycle, POI availability, quote validation, return custody, contract generation, or detailed balance numbers.
- [ ] Use `eldraine-player-experience` to walk the table as a first-time player: after every beat they must know their next action, its cost, and how failure appears.

**Acceptance:** the main loop can be summarized from the table alone; specialist rules remain singly owned and linked.

## Task 4: Define the Pawn Errand lease and its critical cases

**Files:**

- Create after Task 1 confirms placement: `04_Player_Entities/Pawn_Errands.md`
- Modify: `04_Player_Entities/Lifecycle_Roster.md`
- Modify: `08_World_Generation/Hub/01_Hub_Map_Table.md`
- Modify: `08_World_Generation/Hub/02_Hub_Services_Interaction.md`
- Modify: `08_World_Generation/Hub/03_Hub_Map_Interaction.md`
- Modify only as a consumer note: `03_Factions_Societies/Quest_Engine.md`

- [ ] Define one identifier and one durable record: `PawnErrandLease` with `ErrandID`, `PawnID`, `OriginPOI`, `DestinationPOI`, `ServiceOfferID`, payload/cost reservation references, `HubRevisionID`, state, version and timestamps. Do not add world-lore aliases to schema fields.
- [ ] Define the state machine, using either the following proposed names or approved replacements: `OFFERED -> COMMITTED -> WALKING -> ARRIVED -> RESOLVED`, plus explicit `CANCELLED`, `BLOCKED`, and `ABORTED` outcomes. Each transition needs precondition, writer, observable feedback, idempotency rule, and postcondition.
- [ ] Extend `Lifecycle_Roster` so a Pawn with an active errand lease is excluded from `ReadySelectable` by one named predicate. Do not use a UI flag or silent timer as an availability rule.
- [ ] Define an atomic commit order: check current Pawn Presence/readiness, current POI/service offer, payload/cost availability, then create the lease and reserve inputs. Specify rollback for every failed check.
- [ ] Define arrival re-resolution: a visual route only proves travel presentation; arrival must recheck the POI/service offer. If invalid, produce a readable `BLOCKED` result and settle reservations by an explicitly owned rule.
- [ ] Add physical map presentation: origin, route, destination and current step are visible; changing a map pin must not teleport, duplicate, kill, or silently complete a Pawn.
- [ ] State explicit boundaries: errand does not enter a raid, change world phase, generate a contract, consume an `EntryQuote`, create a replacement Pawn, create passive reward, or bypass extraction.
- [ ] Use `eldraine-crash-test` to challenge duplicated commands, disconnects, concurrent raid deployment, map revision changes, cancellation, and payload custody.

**Acceptance:** one designer can write a deterministic test trace for every state transition; one player can tell why their Pawn is unavailable and what will make it selectable again.

## Task 5: Keep errands subordinate to the extraction loop and contract model

**Files:**

- Modify: `03_Factions_Societies/Quest_Engine.md`
- Modify only if a service settlement needs it: `08_World_Generation/Hub/02_Hub_Services_Interaction.md`
- Modify only if exact item custody is affected: `06_Economy_Loot/Return_Manifest_Contract.md`
- Modify: `09_Project_Management/Risk_Register.md`

- [ ] Add only a consumer boundary in Quest Engine: a contract may point to a Hub service, but it cannot turn routine errands into a parallel daily queue or resolve a Pawn lease itself.
- [ ] Compare the final errand result against R65. It must alter a visible local Hub/service state or complete an already-costed service exchange; it must not award generic currency, loot, reputation, or progression just for elapsed time.
- [ ] Add a short no-FOMO rule: a normal errand has no real-time expiry; actual emergency content remains authored and visible under the existing contract rules.
- [ ] If a payload reaches a service, name the custody handoff precisely; otherwise state that errands transport no extraction custody and leave `ReturnManifest` untouched.

**Acceptance:** an errand cannot be optimized as an unattended farm and cannot block access to the normal raid loop.

## Task 6: Apply the prose boundary and migrate only proven duplication

**Files:**

- Modify: the exact owner pages changed in Tasks 3–5
- Create only if needed for decisions that have no owner: `09_Project_Management/<approved-decision-file>.md`

- [ ] Run `audit_prose.py` on changed owner pages. Treat findings as review prompts, not automatic edits; retain intentional diegetic copy in presentation examples.
- [ ] For every removed paragraph, either show that it duplicated a new owner contract or retain it as lore/presentation. Never delete a rule solely because it is verbose.
- [ ] Run `validate_rewrite.py` against each old/new rewritten section before accepting the simplification.
- [ ] Verify the glossary: add terms only if `PawnErrandLease` or its player-facing name appears outside its owner. Do not add new lore names until the mechanic is settled.

**Acceptance:** changed system text is terse because it is testable, not because it has lost necessary behaviour or atmosphere.

## Task 7: Verify corpus integrity and conduct two walkthroughs

**Files:**

- Verify all files changed above

- [ ] Run `python tools/test_core_loop_refactor.py` and `python tools/test_pawn_errands_contract.py`.
- [ ] Run the existing local contract suite: `python tools/test_eldraine_skill_contracts.py`, `python tools/test_vault_curator.py`, and `python tools/test_canonical_guidance.py`.
- [ ] Run `python tools/build_routes.py --write`, then inspect only generated diffs caused by canonical metadata changes.
- [ ] Run `python tools/vault_guard.py`; distinguish newly introduced violations from the known pre-existing baseline and resolve every new violation.
- [ ] Run two written walkthroughs: (a) a 10–15 minute first raid from Hub selection to post-return consequence; (b) a Pawn errand whose POI changes during travel. Each walkthrough must cite exact owner headings and end in a visible player outcome.

**Acceptance:** all new tests pass, no new vault-guard violation exists, and both walkthroughs can be followed without consulting lore pages.

## Review Checkpoints

1. **After Task 1:** confirm the new owner and approve unresolved product values before the errand contract is made canonical.
2. **After Task 3:** review the top loop table as a player, not as a lore document. If the next decision is unclear, do not proceed to errands.
3. **After Task 5:** reject the feature if it creates a background-farm incentive, hidden real-time pressure, or a second route to core rewards.
4. **After Task 7:** inspect the diff for duplicate ownership and generated-file churn before any commit.

## Deferred Work

- No Godot implementation, pathfinding, animation, network transport, UI production, numerical tuning, or live timers are included in this documentation refactor.
- No full social/remote-presence Hub layer is included; it remains deferred under R22.
- No general lore cleanup is included. It must be requested as a separate, voice-led pass after the player/system contracts stabilise.
