# Canonical Corpus Prose Refactor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove AI-shaped structure, duplicated normative prose, stale management residue, and unreadable owner-page openings from Eldrain's active corpus without changing canon, numbers, ownership, links, or intentional lore voice.

**Architecture:** Run two deliberately separate passes. Pass A is an owner-scoped prose-health rewrite across `01_` through `08_`; it removes structural and lexical AI-shaped prose without moving authority. Pass B starts at `03_Factions_Societies` and continues through `08_World_Generation`; it separates entity/lore, playable mechanic, universal system, and interface-registry responsibilities, then migrates only approved normative text to one canonical owner. `02_World_Lore` receives Pass A only. Every batch includes only the route-selected owner, its direct dependencies, and proven incoming consumers, and passes structure-preservation plus project validation before the next batch begins.

**Tech Stack:** Markdown and Obsidian links/frontmatter, Python standard-library tests, `rg`, `tools/build_routes.py`, `tools/vault_guard.py`, and the local `eldraine-vault-curator` audit and rewrite-validation scripts.

**Execution target:** `gpt-5.6-terra` with reasoning effort `high`. Use one fresh Terra context per approved batch when the executor supports handoff; do not load the whole corpus into one editing context.

## Approved Strategy

**Decision: APPROVED WITH OWNER-SCOPED GATES.** Use staged owner batches followed by a distinct responsibility-normalization pass from `03_` onward.

Rejected alternatives:

- **One-shot corpus rewrite:** fastest in prompts, but cannot preserve authority, direct dependencies, and authorial lore voice reliably.
- **Replace only scanner hits:** safe-looking but incomplete. The scanner finds lexical candidates and exact repetition; it does not prove duplicated authority or detect every structural mannerism.
- **Staged prose pass plus responsibility pass:** chosen because style and authority have different evidence, skills, approval gates, and validation requirements.

## Baseline Evidence

- Active canonical surface inspected: 234 Markdown files under `01_` through `09_`.
- Route-selected owners under `01_` through `08_`: 126 total (`3 / 7 / 7 / 14 / 20 / 13 / 22 / 40` by domain).
- Current detect-only scan: 258 candidates — 30 `FORMULAIC_PROSE`, 228 exact repeated sentences.
- Of the exact repeats, 216 are inside `_Registries`. They are candidates for schema/authority review, not evidence of AI-slop by themselves.
- The densest credible prose-review cluster is the culture dependency set under `02_World_Lore`, especially `Lizard_Culture.md`, `Squirrel_Culture.md`, `Toad_Culture.md`, and `Rat_Culture.md`.
- Current skill and corpus checks pass: `test_eldraine_skill_contracts.py`, `test_vault_curator.py`, `test_canonical_guidance.py`, `test_management_hygiene.py`, and `vault_guard.py`.

## Global Constraints

- Start with `00_Index.md`, select the relevant route page, then read the owner and only its direct dependencies.
- Keep the two passes separate. Pass A may rewrite prose but cannot move authority. Pass B may migrate authority only from `03_` through `08_` after an approved responsibility map.
- `02_World_Lore` is explicitly excluded from Pass B. Culture and metaphysics pages may receive lore-preserving prose cleanup, but this plan does not split or redistribute their responsibilities.
- Do not edit `00_Index.md` or generated `00_Routes.md` pages manually. If owner metadata changes, run `python tools/build_routes.py --write` and inspect generated diffs.
- Never rewrite more than three owner pages in one batch. A lore culture page longer than 3,000 words is a batch by itself.
- Before any edit, freeze the exact file list in the audit manifest. An unlisted file is read-only until the manifest is reviewed and updated.
- Preserve YAML frontmatter, heading structure, fenced code, inline code, blockquotes, tables, link targets, rule IDs, registry keys, numeric literals, units, formulas, state transitions, factual claims, and negative authority boundaries.
- Do not add a fact, name, number, date, quote, citation, or canon claim during cleanup.
- Do not regularize lore into system prose. Use `LORE` for culture/history/voice, `MECHANIC` for player action and feedback, `SYSTEM` for states/formulas/outcomes, and `MANAGEMENT` for decisions/risks/evidence.
- A scanner candidate is not a finding. Map it to a supported curator finding only after reading context; otherwise mark it `KEEP`.
- Repeated registry sentences are allowed when they express the same field contract across records. Change them only for `DUPLICATE_RULE`, `MIXED_AUTHORITY`, or an actual schema error.
- Do not require the final scanner count to be zero. Success means every candidate was triaged and every approved rewrite passed protected-invariant review.
- Contextual materials (`10_Reference`, `Истории`, root proposals, and media) are out of scope. They may be read for provenance but need a separate approved plan before editing.
- Do not begin execution from the current dirty worktree. First establish a user-approved baseline commit containing the intended skill and gameplay changes; never discard, reset, or silently absorb unrelated changes.

## Required Skill Routing

The executor must read each selected `SKILL.md` completely before acting, announce the selection, and add it to the active working plan. Do not run every specialist automatically; use conditional specialists only when their evidence can change the verdict.

| Stage | Required skills | Purpose |
|---|---|---|
| Plan execution and isolation | `superpowers:executing-plans`, then `superpowers:using-git-worktrees` | Execute task-by-task from a clean isolated baseline |
| Audit manifest and every prose batch | `eldraine-vault-curator` | Detect authority/prose findings, bound edits, preserve invariants, validate rewrites |
| Responsibility Pass B (`03_`–`08_`) | `eldraine-system-architect` | Decide entity/interface/mechanic/system boundaries and one source of truth |
| Approved placement and migration | `eldraine-gdd-author` | Extend or create the canonical home, migrate text, update consumers and links |
| Lore and faction meaning | `eldraine-lorekeeper` | Protect canon, terminology, in-world authority, causality, and fiction-to-mechanics compatibility |
| Final completion claim | `superpowers:verification-before-completion` | Re-run complete evidence before reporting success |

Conditional routing:

- `eldraine-player-experience` — required when a mechanic contract exists but its lived player sequence, feedback, or failure comprehension is absent.
- `eldraine-crash-test` — use when a moved boundary exposes safe farming, bypass, dominance, or incentive abuse.
- `eldraine-balance-modeler` — use when the dispute concerns a number, formula, threshold, probability, cost, or reward corridor.
- `eldraine-gear-progression` — use when the boundary concerns equipment, loadouts, replacement, or progression dominance.
- `eldraine-location-designer` — use for topology, sectors, routes, extraction feasibility, sockets, or spatial production guarantees.
- `eldraine-narrative-impact` — use when a migration changes chronology, reveal order, story consequence, or world-state propagation.
- `eldraine-player-lens` — use when the architectural verdict depends on motivation, adaptation, churn, or profile conflict rather than on prose placement.

Every specialist request must use the project handoff contract:

```text
HANDOFF: <skill-name>
Affected owners: <exact active paths>
Question: <one bounded question>
Expected return: <evidence, table, constraint, or verdict>
```

## Responsibility Model for Pass B

Assign every affected heading or paragraph under `03_` through `08_` exactly one primary responsibility before moving text:

| Responsibility | Owns | Must not own |
|---|---|---|
| `LORE / ENTITY` | Identity, history, culture, relationships, in-world authority, resident belief, fiction and emotional meaning | Runtime eligibility, costs, formulas, state transitions, rewards, validators, or failure resolution |
| `MECHANIC` | The bounded player interaction: player action, system response, feedback, next decision, local preconditions and outcomes | Cross-content global state or a second copy of universal formulas and lifecycle rules |
| `SYSTEM` | Reusable rule grammar, authoritative state, lifecycle, inputs/outputs, shared eligibility, costs, formulas by reference, edge cases and failure handling | Entity identity, faction history, or decorative content-instance prose |
| `INTERFACE REGISTRY` | One normalized relation between an entity and a mechanic: entity, player-facing verb/result, role, one mechanic owner, and `does_not_own` boundary | Narrative exposition or resolution logic |
| `CONTENT INSTANCE` | One concrete faction service, sector, anomaly, encounter, item, or other realization of an existing grammar | A new universal rule hidden inside the example |
| `PRESENTATION` | UI, map, sensory tell, diegetic framing, and projection of already-owned state | Authoritative state or settlement logic |

`MECHANIC` and `SYSTEM` are distinct responsibilities, not a requirement to create two files. They may occupy separate headings in one focused owner when the bounded player interaction and its authoritative lifecycle have the same scope. Create or select a separate universal system owner only when several mechanics consume the same state, lifecycle, eligibility rule, or value. Do not create one file per semantic layer merely to satisfy this taxonomy.

For a faction, Hearth, place, NPC, culture, or item family, require the chain:

`entity page -> interface record -> mechanic/system owner`; when shared state exists, add `mechanic owner -> universal system owner`.

The entity may participate as `ADDRESS`, `ISSUER`, `PROVIDER`, `WITNESS`, `PRESENTER`, or `CONSUMER`; that role never grants runtime authority. If no canonical mechanic/system owner exists, record `MISSING_OWNER` and stop migration. Do not solve it by leaving the rule on a lore page or by making the interface registry normative.

---

### Task 0: Establish the execution baseline

**Files:**

- Read: `.agents/skills/eldraine-vault-curator/SKILL.md`
- Read: `.agents/skills/eldraine-system-architect/SKILL.md`
- Read: `.agents/skills/eldraine-gdd-author/SKILL.md`
- Read: `.agents/skills/eldraine-lorekeeper/SKILL.md`
- Read: `AGENTS.md`
- Verify: `tools/test_eldraine_skill_contracts.py`
- Verify: `tools/test_vault_curator.py`
- Verify: `tools/test_canonical_guidance.py`
- Verify: `tools/test_management_hygiene.py`
- Verify: `tools/vault_guard.py`

**Interfaces:**

- Consumes: the committed post-skill-fix repository state.
- Produces: a clean, validated baseline from which prose-only diffs can be reviewed independently.

- [ ] **Step 1: Confirm the worktree is safe to use**

Run: `git status --short`

Expected: no uncommitted changes. If the tree is dirty, stop editing and report the exact paths; do not stash, reset, commit, or move user work without approval.

- [ ] **Step 2: Re-read the active editing contracts**

Read `AGENTS.md`, the full vault-curator skill, and the Render-Safe Tables section referenced by the GDD-author skill.

Expected: the executor can state the owner route, selected register, protected invariants, and exact approval surface before editing.

- [ ] **Step 3: Run the skill contract suite**

Run:

```powershell
python tools/test_eldraine_skill_contracts.py
python tools/test_vault_curator.py
python tools/test_canonical_guidance.py
python tools/test_management_hygiene.py
```

Expected: all tests pass.

- [ ] **Step 4: Run the corpus baseline**

Run: `python tools/vault_guard.py`

Expected: exit code 0 with no output.

- [ ] **Step 5: Create the execution branch**

Use `superpowers:using-git-worktrees` at execution time and create `codex/canonical-prose-refactor` from the approved baseline.

Expected: the refactor is isolated from unrelated work.

### Task 1: Freeze the audit manifest before rewriting

**Files:**

- Create: `docs/audits/2026-08-11-canonical-prose-refactor-manifest.md`
- Read: `00_Index.md`
- Read: `01_Core_Vision/00_Routes.md` through `08_World_Generation/00_Routes.md`
- Read: active owners selected from those route pages and only their direct dependencies.

**Interfaces:**

- Consumes: route ownership, frontmatter dependencies, scanner candidates, and current incoming links.
- Produces: the only approved list of Pass A editable batches for Tasks 3–6 and the source inventory consumed by the Pass B audit in Task 7.

- [ ] **Step 1: Record the manifest header and fixed columns**

Use exactly these short index columns:

```markdown
| Batch | Pass | Register | Owner | Decision | Status |
|---|---|---|---|---|---|
```

For every batch, put direct dependencies, exact evidence, curator finding, smallest repair, preserved meaning, approval, and validation in a titled list below the table. In tables, escape every Obsidian alias separator as `\|`; never put multi-link dependency lists or long paths in table cells.

- [ ] **Step 2: Enumerate route owners deterministically**

Run:

```powershell
rg -l 'index_route:\s*owner' 01_Core_Vision 02_World_Lore 03_Factions_Societies 04_Player_Entities 05_Combat_Survival 06_Economy_Loot 07_Gear_Inventory 08_World_Generation -g '*.md' | Sort-Object
```

Expected: 126 owner paths with domain counts `3, 7, 7, 14, 20, 13, 22, 40`.

- [ ] **Step 3: Run the detect-only scanner by domain**

For each domain, pass its Markdown file list to:

```powershell
python .agents/skills/eldraine-vault-curator/scripts/audit_prose.py --json <bounded paths>
```

Expected baseline: 258 candidates overall. A different count is allowed only when the approved baseline commit changed the corpus; record the new count rather than forcing the old value.

- [ ] **Step 4: Triage every candidate into a supported outcome**

Use only `DUPLICATE_RULE`, `MIXED_AUTHORITY`, `ORPHAN_CONTEXT`, `MISSING_LINK`, `ROUTE_DRIFT`, `FORMULAIC_PROSE`, `OVERLONG_OWNER`, `EMPIRICAL_AS_FACT`, `STALE_PROPOSAL`, or `TOOL_POLICY_DRIFT` as findings.

Map scanner-only `DUPLICATE_SENTENCE` and `OVERLONG_PARAGRAPH` candidates to one of those findings only when context proves it. Otherwise record `KEEP — structured repetition` or `KEEP — intentional voice`.

- [ ] **Step 5: Split the manifest into bounded batches**

Apply these hard limits:

- up to three normal owner pages plus their direct dependencies;
- exactly one culture page when it exceeds 3,000 words;
- no more than 1,500 editable non-table lines per batch;
- one register profile per batch;
- no mixed domain batch unless one page is a direct consumer of the selected owner.

Mark every `02_World_Lore` row `Pass A only`. Mark every approved `03_` through `08_` owner row `Pass A + Pass B`; this means style is reviewed first and responsibility is reviewed only after the prose batch closes.

- [ ] **Step 6: Review the manifest before edits**

Expected: every `REWRITE` row names exact paths, evidence with heading or line, smallest safe repair, preserved meaning, approval requirement, and validation commands. Rows without that evidence remain `KEEP` or `APPROVAL_REQUIRED`.

- [ ] **Step 7: Commit the audit-only artifact**

```powershell
git add docs/audits/2026-08-11-canonical-prose-refactor-manifest.md
git commit -m "docs: scope canonical prose refactor"
```

Expected: no canonical file is changed in this commit.

### Task 2: Finish management hygiene before canon prose work

**Files:**

- Execute: `docs/plans/2026-08-11-management-corpus-cleanup-plan.md`
- Modify only as specified there: `09_Project_Management/Risk_Register.md`
- Modify only as specified there: `09_Project_Management/Worldbuilding_Refactor_Roadmap_2026-07-23.md`
- Verify: `tools/test_management_hygiene.py`

**Interfaces:**

- Consumes: the existing evidence-backed cleanup plan.
- Produces: an active management surface containing only unfinished work and active/deferred risks.

- [ ] **Step 1: Execute Tasks 1–4 of the management cleanup plan exactly**

Do not broaden deletion beyond the 40 `fixed` risk rows and two completed roadmap checkboxes already named by that plan.

- [ ] **Step 2: Prove retained management documents still contain live work**

Run the candidate-evidence search from Task 4 of the management cleanup plan.

Expected: all four named documents remain `KEEP`; no whole document is deleted.

- [ ] **Step 3: Run targeted hygiene verification**

Run: `python tools/test_management_hygiene.py`

Expected: PASS.

- [ ] **Step 4: Commit the bounded management cleanup**

```powershell
git add 09_Project_Management/Risk_Register.md 09_Project_Management/Worldbuilding_Refactor_Roadmap_2026-07-23.md tools/test_management_hygiene.py
git commit -m "docs: remove completed management residue"
```

### Task 3: Pass A — refactor core promise and economy owners

**Files:**

- Modify only manifest-approved batches under `01_Core_Vision` and `06_Economy_Loot`.
- Primary route owners: the 3 owners in `01_Core_Vision/00_Routes.md` and 13 owners in `06_Economy_Loot/00_Routes.md`.
- Snapshot before files under a validated temporary directory outside the repository.

**Interfaces:**

- Consumes: approved `SYSTEM` or `MECHANIC` manifest rows.
- Produces: owner openings that state the adopted rule, player action, and consequence without duplicating detailed rules from dependencies.

- [ ] **Step 1: Select one approved batch from the manifest**

Read its route owner, direct dependencies, and incoming links only. State the exact editable paths before changing them.

- [ ] **Step 2: Snapshot every editable file**

Create a task-specific directory with `New-Item -ItemType Directory`, resolve its absolute path, then copy each editable file with `Copy-Item -LiteralPath`.

Expected: one immutable before-file per editable file.

- [ ] **Step 3: Perform structure pass**

Remove duplicated conclusions, announcement paragraphs, forced contrast, repeated section openings, and abstract explanation that hides actor/condition/outcome. Move the adopted rule and observable consequence into the first screen. Do not change headings in this pass.

- [ ] **Step 4: Perform language pass**

Remove inflated significance, vague attribution, synonym cycling, excess transitions, and manufactured punchlines only where they obscure or repeat a concrete claim.

- [ ] **Step 5: Validate every rewritten file**

Run:

```powershell
python .agents/skills/eldraine-vault-curator/scripts/validate_rewrite.py --json <before-file> <after-file>
python .agents/skills/eldraine-vault-curator/scripts/audit_prose.py --json <after-file>
```

Expected: `validate_rewrite.py` reports `valid: true`. Remaining audit candidates are recorded as `KEEP` or returned to the manifest; they are not auto-fixed.

- [ ] **Step 6: Review the bounded diff and commit**

Run `git diff --check` and `git diff -- <exact batch paths>`.

Expected: only approved prose and proven duplicate-consumer removal changed. Commit as `docs: clarify <owner subject>`.

- [ ] **Step 7: Repeat Steps 1–6 until all approved `01_` and `06_` batches are closed**

Each repetition is a separate review and commit. Do not combine batches for speed.

### Task 4: Pass A — refactor player, combat, and gear owners

**Files:**

- Modify only manifest-approved batches under `04_Player_Entities`, `05_Combat_Survival`, and `07_Gear_Inventory`.
- Primary route owners: 14 in `04_`, 20 in `05_`, and 22 in `07_`.
- Registries under each `_Registries` directory are schema-first and read-only unless the manifest proves an authority or schema defect.

**Interfaces:**

- Consumes: stable promise/economy vocabulary from Task 3 and approved `SYSTEM`/`MECHANIC` batches.
- Produces: player-readable action, feedback, state, and failure text without changing formulas, thresholds, loadout rules, or registry keys.

- [ ] **Step 1: Execute each non-registry batch with the snapshot, two-pass rewrite, validation, diff, and commit cycle from Task 3**

Expected: the first screen answers what the player does, what the system checks, and what visible consequence follows.

- [ ] **Step 2: Audit registry candidates separately**

For every exact repeated sentence in a registry, compare the surrounding record keys and owner metadata.

Expected: repeated field-contract text is marked `KEEP — structured repetition`; only duplicate normative rules or malformed records receive a rewrite decision.

- [ ] **Step 3: Route balance or progression uncertainty instead of editing it**

If prose cleanup reveals a disputed formula, threshold, probability, reward, equipment dominance, or lifecycle outcome, stop that row as `APPROVAL_REQUIRED` and issue the bounded Eldrain handoff required by `AGENTS.md`. The prose refactor does not decide the rule.

- [ ] **Step 4: Run domain-relevant tests after every batch**

At minimum run `python tools/test_canonical_guidance.py` plus any test file that names the changed owner.

Expected: all relevant tests pass before commit.

### Task 5: Pass A — refactor world-generation owners without changing topology

**Files:**

- Modify only manifest-approved batches under `08_World_Generation`.
- Primary route owners: 40 in `08_World_Generation/00_Routes.md`.
- Treat generated route pages and registry records as read-only under the Global Constraints.

**Interfaces:**

- Consumes: stabilized player/combat/gear vocabulary from Task 4.
- Produces: readable world-state, route, entry, exit, Hub, and persistence contracts while preserving topology and production constraints.

- [ ] **Step 1: Order the batches by data flow**

Use this sequence: persistence/reality state → server lifecycle → topology/sector generation → raid approach and entry → extraction/egress → Hub presentation.

- [ ] **Step 2: Execute each batch with the Task 3 snapshot and validation cycle**

Do not rewrite downstream consumers before the selected upstream owner is accepted.

- [ ] **Step 3: Protect map and table rendering**

For every affected table, count declared columns, inspect every wiki-link alias for escaped `\|`, and move long paths or multi-owner lists below the table.

- [ ] **Step 4: Route feasibility uncertainty**

If cleanup exposes a disputed route, socket, sector, extraction, or production-feasibility rule, mark it `APPROVAL_REQUIRED` and request one bounded `eldraine-location-designer` handoff. Do not resolve it as a copy edit.

- [ ] **Step 5: Validate and commit one world-generation batch at a time**

Run changed-owner tests, `git diff --check`, and the exact batch diff before each commit.

### Task 6: Pass A — refactor world-lore and faction pages with register protection

**Files:**

- Modify only manifest-approved `LORE` batches under `02_World_Lore`.
- Modify manifest-approved `LORE`, `MECHANIC`, and `SYSTEM` batches under `03_Factions_Societies`; keep its registries schema-first.
- Start with owner: `02_World_Lore/Culture_Language.md`.
- Direct culture dependencies, one batch each: `02_World_Lore/Rat_Culture.md`, `02_World_Lore/Toad_Culture.md`, `02_World_Lore/Squirrel_Culture.md`, `02_World_Lore/Lizard_Culture.md`, and `02_World_Lore/Hedgehog_Culture.md` when approved by the manifest.
- Update faction consumers only when an exact duplicated or stale statement is proven.

**Interfaces:**

- Consumes: active culture owner, its direct culture dependencies, faction/entity pages, faction mechanic owners, interface registries, and proven consumers.
- Produces: distinctive lore voice and readable faction mechanics with less repeated scaffolding, while preserving chronology, institutions, metaphysics, cultural tensions, runtime rules, quotes, and every canon claim. Mixed responsibility is recorded for Pass B, not migrated here.

- [ ] **Step 1: Invoke the required lore review skills**

Use `eldraine-vault-curator` for every prose surface. Use `eldraine-lorekeeper` for `02_World_Lore` and every faction/entity/narrative page. Select `LORE`, `MECHANIC`, or `SYSTEM` per page before judging a candidate; do not apply lore cadence to mechanic/system owners.

- [ ] **Step 2: Review `Culture_Language.md` as the cluster owner**

Record which statements are cluster-wide rules and which details remain owned by each culture dependency. Do not move details merely to shorten a page.

- [ ] **Step 3: Rewrite one culture page per batch**

Run structure first: remove repeated thesis restatement, same-shaped cultural section openings, mechanical triplets, and redundant cross-culture comparisons. Then run language review while retaining approved epigraphs, in-world terms, mystery, and characterful cadence.

- [ ] **Step 4: Rewrite `03_Factions_Societies` by register without moving responsibility**

For entity/lore pages, preserve identity, in-world authority, relationships, history, and resident belief. For mechanic/system owners, expose player action, response, state, cost, result, feedback, and failure. For registries, retain repeated field-contract language unless it is a proven authority or schema defect. Record mixed placement for Task 7 instead of relocating text during Pass A.

- [ ] **Step 5: Keep `02_World_Lore` outside responsibility migration**

Do not split, relocate, or reclassify `02_World_Lore` content during this plan. If a runtime-looking statement is discovered there, record it as a finding for author review but leave its placement unchanged. Responsibility Pass B begins at `03_Factions_Societies`.

- [ ] **Step 6: Require lorekeeper verdict for meaning-sensitive cuts**

If a proposed deletion changes chronology, faction motive, metaphysical implication, terminology, or fiction-to-mechanics compatibility, do not edit it. Use the exact `HANDOFF` contract from `AGENTS.md` with `eldraine-lorekeeper` and keep final ownership with the curator batch.

- [ ] **Step 7: Validate protected content and factual parity**

Run `validate_rewrite.py`, then compare every paragraph-level deletion against the manifest's `Preserved meaning` field. Validator success alone is insufficient because the tool cannot prove semantic parity.

- [ ] **Step 8: Check direct consumers after each accepted lore or faction batch**

Search for the exact culture path across `01_` through `09_`. Update a consumer only when it repeats the changed owner statement or points to a removed heading. Otherwise leave it unchanged.

- [ ] **Step 9: Commit each lore/faction page and its proven consumers separately**

Use `docs: refine <subject> prose` and include only the named batch paths.

### Task 7: Pass B — build the responsibility migration map for `03_` through `08_`

**Files:**

- Create: `docs/audits/2026-08-11-responsibility-migration-map.md`
- Read: `01_Core_Vision/01_Vision.md`
- Read: `01_Core_Vision/02_Core_Loop.md`
- Read: `09_Project_Management/Architecture_MVP.md`
- Read: `03_Factions_Societies/00_Routes.md` through `08_World_Generation/00_Routes.md`
- Read first for faction boundaries: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `03_Factions_Societies/_Registries/Registry_Factions.md`, `03_Factions_Societies/Pledge_Contracts.md`, `03_Factions_Societies/Reputation_Rules.md`, and the selected faction/entity page.

**Interfaces:**

- Consumes: closed Pass A prose batches, active architecture constraints, route owners, direct dependencies, interface registries, and incoming consumers.
- Produces: an audit-only migration map assigning each mixed or duplicated responsibility to one exact owner without editing canon.

- [ ] **Step 1: Invoke the architecture skills**

Use `eldraine-system-architect` as the mandatory lead and `eldraine-vault-curator` for evidence and lifecycle safety. Use `eldraine-lorekeeper` whenever the selected source is a faction, Hearth, character, institution, place, culture, or narrative explanation.

- [ ] **Step 2: Extract the architectural evidence classes**

For each selected owner cluster, label relevant statements as `AUTHOR CONSTRAINT`, `GDD FACT`, `STRUCTURAL INFERENCE`, `EMPIRICAL UNKNOWN`, or `CONTENT GAP`. A style impression is not sufficient evidence for migration.

- [ ] **Step 3: Classify each affected heading or paragraph**

Assign exactly one primary responsibility from `LORE / ENTITY`, `MECHANIC`, `SYSTEM`, `INTERFACE REGISTRY`, `CONTENT INSTANCE`, or `PRESENTATION`. Also record whether the current placement is `KEEP`, `DUPLICATE_RULE`, `MIXED_AUTHORITY`, `ORPHAN_CONTEXT`, or `MISSING_OWNER`.

- [ ] **Step 4: Use a render-safe migration index**

Use exactly these short columns:

```markdown
| Migration | Source | Current role | Decision | Status |
|---|---|---|---|---|
```

Below each row, record exact source heading/line, target owner, entity role, mechanic owner, universal system owner when applicable, `does_not_own` boundary, direct consumers, preserved meaning, required skill/handoff, approval, and validation. Do not place multi-link lists in the table.

- [ ] **Step 5: Audit `03_Factions_Societies` first**

For each faction or institution, require this resolution:

1. entity/lore page owns identity, relationships, in-world authority, belief, and history;
2. `Registry_Faction_Interfaces.md` owns normalized participation records only;
3. one mechanic/system owner resolves the player interaction, eligibility, state, cost, result, feedback, and failure;
4. a separate universal system owner exists only for shared lifecycle, state, or values used by multiple mechanics;
5. every source and interface record states what it does not own.

If any link in the chain is absent, record `MISSING_OWNER` and do not invent a target.

- [ ] **Step 6: Audit `04_` through `08_` by domain order**

Use this order: player lifecycle/entities → combat/survival → economy/loot → gear/inventory → world generation. Keep each migration stream within one owner plus direct dependencies; split circular streams around the smallest shared foundation owner.

- [ ] **Step 7: Route bounded specialist questions**

Use only the matching conditional skill from Required Skill Routing. Record its verdict or evidence in the migration entry; the specialist does not take ownership of the architecture verdict.

- [ ] **Step 8: Stop for approval before migration**

Expected: every actionable row names exact source and target paths and has status `APPROVED_FOR_MIGRATION`. `MISSING_OWNER`, `SOURCE_CONFLICT`, `CANON DRIFT`, or disputed design rows remain unedited.

- [ ] **Step 9: Commit the audit-only migration map**

```powershell
git add docs/audits/2026-08-11-responsibility-migration-map.md
git commit -m "docs: map canonical responsibility migrations"
```

Expected: no canonical page changes in this commit.

### Task 8: Pass B — migrate approved responsibilities

**Files:**

- Modify: only exact source, target owner, interface registry, and direct consumer paths in an `APPROVED_FOR_MIGRATION` entry from `docs/audits/2026-08-11-responsibility-migration-map.md`.
- Never modify: `02_World_Lore/**` during this task.

**Interfaces:**

- Consumes: one approved migration entry with a complete responsibility chain.
- Produces: one canonical owner for each rule, a bounded interface relation, a concise negative-authority boundary at the source, and updated direct consumers.

- [ ] **Step 1: Invoke the mandatory migration skills**

Use `eldraine-system-architect` to confirm the approved boundary, `eldraine-gdd-author` for canonical placement and integration, and `eldraine-vault-curator` for the smallest safe repair. Also use `eldraine-lorekeeper` when the source or target contains lore/entity meaning.

- [ ] **Step 2: Report the edit contract before writing**

Name the proposed canonical location, `extend` versus `create` decision, unresolved assumptions, exact affected files, source responsibility, target responsibility, and `does_not_own` boundary.

- [ ] **Step 3: Snapshot every source and target file**

Create a task-specific absolute temporary directory with `New-Item -ItemType Directory` and copy each file with `Copy-Item -LiteralPath` before editing.

- [ ] **Step 4: Move, link, and retire in one bounded migration**

Place the normative rule in the approved mechanic/system owner. Replace the source copy with the smallest entity-facing, mechanic-facing, or presentation-facing statement plus a direct link and negative-authority boundary. Add or update one interface record when an entity participates in the mechanic. Do not leave two normative copies.

- [ ] **Step 5: Preserve the full executable contract**

When the target owns a mechanic, preserve or establish player promise, player loop, state machine, interfaces, edge cases, feedback, and acceptance criteria. Link numeric owners instead of copying values. Do not create missing values during migration.

- [ ] **Step 6: Update direct consumers and incoming links**

Search for the source heading and migrated rule only after owner selection. Update consumers to the new owner; retain entity links where the consumer needs identity or in-world authority rather than runtime resolution.

- [ ] **Step 7: Validate source, target, interface, and consumers**

Run `validate_rewrite.py` for prose-rewritten files, domain-relevant tests, `python tools/test_canonical_guidance.py`, `git diff --check`, and an exact-path diff. A protected difference caused by the approved migration must be named explicitly in the migration entry; unrelated differences block the batch.

- [ ] **Step 8: Commit one migration stream**

Commit as `docs: separate <entity/mechanic/system responsibility>` with only the exact approved paths.

- [ ] **Step 9: Repeat from Step 1 for the next approved entry**

Do not combine unrelated migrations and do not reopen Pass A style cleanup unless the moved text becomes unreadable in its new register.

### Task 9: Repair direct consumers and navigation drift

**Files:**

- Modify: only direct consumers named by accepted manifest findings.
- Generate when metadata changed: `00_Index.md` and affected `00_Routes.md` pages via `tools/build_routes.py`.

**Interfaces:**

- Consumes: accepted Pass A rewrites from Tasks 3–6 and Pass B migrations from Task 8.
- Produces: no stale heading links, no duplicate normative summaries, and generated routes consistent with owner metadata.

- [ ] **Step 1: Search incoming links only after selecting the accepted owner**

Run `rg -n '<owner stem>|<removed heading text>' 00_Index.md 01_Core_Vision 02_World_Lore 03_Factions_Societies 04_Player_Entities 05_Combat_Survival 06_Economy_Loot 07_Gear_Inventory 08_World_Generation 09_Project_Management -g '*.md'`.

- [ ] **Step 2: Apply the smallest consumer repair**

Prefer updating a link or deleting a duplicated normative sentence. Do not rewrite a consumer section merely to harmonize style.

- [ ] **Step 3: Regenerate navigation only when metadata changed**

Run: `python tools/build_routes.py --write`

Expected: generated diffs correspond only to approved metadata changes. If no metadata changed, generated files remain untouched.

- [ ] **Step 4: Commit consumer/navigation repairs separately**

Run `git diff --check`, inspect exact paths, and commit as `docs: align prose consumers`.

### Task 10: Prove corpus integrity and close both manifests

**Files:**

- Modify: `docs/audits/2026-08-11-canonical-prose-refactor-manifest.md`
- Modify: `docs/audits/2026-08-11-responsibility-migration-map.md`
- Verify: every canonical file changed by Tasks 2–9.

**Interfaces:**

- Consumes: all accepted batch commits.
- Produces: a closed audit trail where every prose candidate is `KEEP`, `REWRITE COMPLETE`, `ROUTED`, or `APPROVAL_REQUIRED`, and every responsibility row is `KEEP`, `MIGRATED`, `MISSING_OWNER`, `SOURCE_CONFLICT`, `CANON DRIFT`, or `APPROVAL_REQUIRED`.

- [ ] **Step 1: Re-run all contract tests**

```powershell
python tools/test_eldraine_skill_contracts.py
python tools/test_vault_curator.py
python tools/test_canonical_guidance.py
python tools/test_management_hygiene.py
```

Expected: all tests pass.

- [ ] **Step 2: Run project validation**

Run: `python tools/vault_guard.py`

Expected: exit code 0 with no output.

- [ ] **Step 3: Run final prose scan by domain**

Record remaining candidates in the manifest. Do not edit intentional lore or structured records to reduce the count.

- [ ] **Step 4: Verify repository hygiene**

Run:

```powershell
git diff --check
git status --short
git log --oneline --decorate -12
```

Expected: no unstaged refactor changes, no generated-file drift, and one reviewable commit per batch.

- [ ] **Step 5: Perform the final curator and architecture review**

For each changed owner, confirm:

- authority is singular and explicit;
- the first screen states the adopted rule/action/consequence appropriate to its register;
- removed text carried no unique fact or intentional voice;
- direct consumers and incoming links remain valid;
- every `APPROVAL_REQUIRED` row is still unedited.
- no responsibility migration occurred inside `02_World_Lore`;
- every migrated `03_` through `08_` rule has one entity/lore placement, at most one interface record per distinct interaction, one mechanic/system owner, and a separate universal system owner only when shared state requires it;
- every interface role has an explicit `does_not_own` boundary.

- [ ] **Step 6: Commit the closed manifest**

```powershell
git add docs/audits/2026-08-11-canonical-prose-refactor-manifest.md docs/audits/2026-08-11-responsibility-migration-map.md
git commit -m "docs: close prose and responsibility refactor audits"
```

## Review Checkpoints

1. **After Task 1:** approve the manifest and exact first batches. No prose edit starts before this gate.
2. **After Task 3:** review Core Vision and Economy as the vocabulary baseline for all downstream work.
3. **After Task 5:** inspect topology and table diffs in rendered Obsidian view.
4. **After every culture batch in Task 6:** review voice and semantic parity; validator output is supporting evidence, not the verdict. Confirm that `02_World_Lore` placement did not change.
5. **After Task 7:** approve the exact responsibility migration map. No Pass B canonical edit starts before this gate.
6. **After every Task 8 migration:** review entity/interface/mechanic/system ownership and the negative-authority boundary.
7. **After Task 10:** approve unresolved rows as separate design work; do not hide them in cleanup commits.

## Definition of Done

- Every edited path was named in an approved manifest batch.
- No owner, rule, number, formula, link target, heading, table contract, or negative boundary changed without explicit design approval.
- All supported findings are resolved, routed, or explicitly retained with evidence.
- Registry repetition is preserved where it encodes stable schema.
- `02_World_Lore` received prose cleanup only and no responsibility redistribution.
- Every approved mixed-responsibility finding from `03_` through `08_` was either migrated to one canonical owner or left visibly blocked as `MISSING_OWNER`, `SOURCE_CONFLICT`, `CANON DRIFT`, or `APPROVAL_REQUIRED`.
- Entity/lore pages, interface records, mechanic responsibilities, and shared system responsibilities have explicit non-overlapping boundaries even when mechanic and system headings share one focused owner page.
- All tests and `vault_guard.py` pass.
- The final history is reviewable one owner batch at a time.
- Contextual materials remain untouched and are not silently treated as canon.
