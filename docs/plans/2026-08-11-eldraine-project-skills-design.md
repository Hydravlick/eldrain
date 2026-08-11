# Eldrain Project Skills Design

**Date:** 2026-08-11

**Status:** approved direction, pending implementation plan
**Scope:** project-local decision grilling and vault curation

## Goal

Add two project-local skills that reduce blind spots and AI-shaped documentation debt without creating a second canon or bulk-rewriting active rules:

1. `eldraine-project-grill` interrogates a bounded decision until its owner, value, dependencies, failure states, alternatives, and evidence are resolved.
2. `eldraine-vault-curator` audits note structure, authority, duplication, prose bloat, link health, and canon lifecycle, then proposes owner-scoped repairs.

The skills live under `.agents/skills/`, follow `AGENTS.md`, and are deployed one at a time. The upstream `grill-me`, `llm-wiki`, and `caveman` skills are not installed as independent runtime skills because their generic triggers and storage models conflict with Eldrain's owner-first corpus.

## Considered Approaches

### 1. Install the upstream repository or its generic note skills unchanged

Rejected. Hundreds of overlapping skill descriptions would increase trigger collisions. Generic `llm-wiki` introduces a parallel `raw/wiki` authority model, and upstream `grill-me` detects mostly English planning phrases and writes session state outside the project.

### 2. Install upstream `grill-me` and layer Eldrain instructions around it

Rejected. Two skills would compete for the same trigger, while the underlying extractor would still lack Russian markers, owner routes, risk IDs, and Eldrain verdicts.

### 3. Create two Eldrain-native skills using selected upstream principles

Selected. Preserve the useful discipline—explore first, one forcing question at a time, recommended answer, depth-first decisions, persistent sessions—inside project-specific ownership and validation rules.

## Skill 1: `eldraine-project-grill`

### Trigger and boundary

Use for a proposal, unresolved TODO/risk, cross-owner change, critical mechanic, or explicit request to grill/stress-test an Eldrain decision. It does not edit canon. It produces evidence and locked decisions for later integration by `eldraine-gdd-author`.

### Inputs

- a named subject, proposal path, TODO item, or Risk Register ID;
- optional success criterion or author constraint;
- project navigation starting at `00_Index.md`.

If no subject can be resolved, return `MISSING_OWNER` or ask one bounded question. Do not manufacture a project-wide scope.

### Read path

1. Resolve the subject through `00_Index.md` and its route page.
2. Open the active owner and direct dependencies only.
3. Read matching TODO and Risk Register entries.
4. Search the canonical corpus only for dependency and consistency checks.
5. Label contextual sources separately from adopted active rules.

### Triage pass

Before questioning the author, classify each candidate blind spot:

- `MISSING_OWNER`;
- `SOURCE_CONFLICT`;
- `CANON_DRIFT`;
- `EMPIRICAL_UNKNOWN`;
- `CONTENT_GAP`;
- duplicate responsibility;
- missing player decision;
- incomplete lifecycle or failure transition;
- cost bypass, exploit, or boring optimum;
- removable complexity;
- approval-dependent value choice.

The first rollout scans the urgent TODO section and 18 `in_progress` risks. It does not grill all owner pages indiscriminately.

### Interview contract

- Ask one question per turn.
- Explore the corpus before asking anything resolvable from files.
- Walk dependencies depth-first.
- Include a recommended answer with evidence paths and one-sentence rationale.
- Record the answer before opening the next branch.
- Never hide an author choice behind a genre convention or invented player research.

Question shape:

```text
Q[i/total]: <one forcing question>
Recommended: <current best answer and why>
Evidence: <active owner paths or explicit absence>
Decision unlocked: <which dependent branch this resolves>
```

### Branch outcomes

Every resolved branch ends in exactly one outcome:

- `KEEP`
- `CLARIFY`
- `SIMPLIFY`
- `MERGE`
- `SPLIT`
- `DEFER`
- `PROTOTYPE`
- `REMOVE`
- `AUTHOR_DECISION`

`REMOVE`, `MERGE`, and `SPLIT` are recommendations until explicitly approved. No automatic deletion or canonical edit occurs during grilling.

### Specialist routing

The skill owns the interview and final decision packet, not every specialist verdict. It may request one bounded handoff at a time using the existing `AGENTS.md` contract. The expected evidence must be capable of changing the active branch outcome.

### Persistence

Transient session state stays inside the workspace under `.agents/state/grill-sessions/` and is ignored by Git. Session names are normalized to lowercase letters, digits, and hyphens; resolved paths must remain inside the session directory.

Final approved results are written only on explicit request as decision records under `09_Project_Management/Decision_Records/`. A record describes the decision and placement; it does not become a second owner of a game rule.

### Decision packet

At completion, report:

- subject and player/system value;
- locked decisions and rejected alternatives;
- canonical owner;
- direct consumers and incoming links;
- branch outcome per issue;
- closed and remaining risks;
- empirical tests;
- approved edit surface;
- unresolved `MISSING_OWNER`, `SOURCE_CONFLICT`, or `APPROVAL_REQUIRED` conditions.

## Skill 2: `eldraine-vault-curator`

### Trigger and boundary

Use for note administration, structural cleanup, AI-slop review, owner-page readability, broken navigation, duplicated rules, or a request to organize the vault. It audits first and never performs a corpus-wide rewrite by default.

### Audit model

Inspect four separate layers:

1. **Authority:** one rule, one active owner; indexes and registries do not become competing prose owners.
2. **Lifecycle:** intake/context -> decision -> approved owner migration -> consumer update -> validation -> temporary-source cleanup.
3. **Readability:** the first screen states the adopted rule; machine fields and edge cases remain implementable without burying the verdict.
4. **Prose health:** distinguish intentional system-contract structure from formulaic expansion, repeated contrast rhetoric, oversized paragraphs, unjustified certainty, and duplicated explanations.

### Finding classes

- `DUPLICATE_RULE`
- `MIXED_AUTHORITY`
- `ORPHAN_CONTEXT`
- `MISSING_LINK`
- `ROUTE_DRIFT`
- `FORMULAIC_PROSE`
- `OVERLONG_OWNER`
- `EMPIRICAL_AS_FACT`
- `STALE_PROPOSAL`
- `TOOL_POLICY_DRIFT`

Registries are evaluated as structured records, not penalized merely for length. Prose pages are split only when they contain multiple responsibilities, not because they cross an arbitrary line count.

### Repair contract

For each finding, produce:

- exact path and evidence;
- authority impact;
- smallest safe repair;
- semantic invariants that must survive rewriting;
- whether approval or a specialist verdict is required;
- validation commands.

Rewriting proceeds owner by owner. Preserve rule meaning, IDs, state transitions, negative authority boundaries, and direct dependencies. Contextual history remains labeled and does not enter active rule statements.

## Deterministic Tools

Implementation will include these standard-library Python tools:

- a project grill scanner for Russian/English decision markers, TODO entries, risk IDs, owner metadata, and direct links;
- a workspace-bound session tracker with path validation;
- a vault prose/structure audit that reports metrics and finding candidates without rewriting files.

Scripts perform no network calls and no writes outside declared project state or explicitly approved output paths.

## Integration Changes

After each skill passes its own tests:

- add it to `.agents/skills/<skill-name>/` with `SKILL.md` and `agents/openai.yaml`;
- update the `AGENTS.md` orchestration table with a non-overlapping trigger;
- add deterministic script tests under `tools/` or the skill's own `scripts/tests/`;
- extend `.gitignore` for transient grill session state;
- update `vault_guard.py` only when a finding is mechanically enforceable and agrees with the current contextual-material policy.

## Error Handling

- Missing subject or owner -> `MISSING_OWNER`.
- Conflicting active owners -> `SOURCE_CONFLICT` with exact paths.
- Requested deletion or canonical rewrite without approval -> `APPROVAL_REQUIRED`.
- A question answer invalidates downstream branches -> rebuild only the affected subtree.
- Corpus changes during a session -> mark affected evidence stale and re-read before continuing.
- Validation failure -> keep proposed changes uncommitted and report exact findings.

## Testing Strategy

Skills are deployed sequentially and follow RED-GREEN-REFACTOR.

### `eldraine-project-grill` baseline scenarios

1. Return cadence: detect whether regular rewards duplicate `CityState` or create FOMO.
2. Welfare/Foundling: identify lifecycle, abuse, and ownership branches without flattening the authored fantasy.
3. Cross-owner proposal under time pressure: resist broad reading, bundled questions, and premature canonical edits.

Success requires owner-first evidence, one question, a recommendation, a named unlocked dependency, and no mutation.

### `eldraine-vault-curator` baseline scenarios

1. Distinguish an intentionally long registry from a bloated mixed-responsibility prose owner.
2. Detect formulaic prose without treating the required readability contract as an error.
3. Find a stale contextual proposal and propose migration without letting it override active canon.

Success requires exact paths, authority impact, smallest safe repair, preserved invariants, and no bulk rewrite.

## Acceptance Criteria

- No third-party skill is bulk-installed.
- Adapted upstream `grill-me` ideas and code retain MIT attribution in the skill body or bundled reference.
- Both skills are project-local and have non-overlapping triggers.
- Each skill is tested and deployed before work begins on the next.
- The grill reads owners before asking and asks one question per turn.
- The curator separates structural findings from style preferences.
- Neither skill edits active canon without explicit approval.
- Scripts are workspace-bound, stdlib-only, and tested.
- Existing route checks and tool tests remain green.
- `vault_guard` findings are not increased; known policy drift is reported explicitly.

## Rollout

1. Build, baseline-test, implement, and validate `eldraine-project-grill`.
2. Run it on the urgent TODO and one `in_progress` risk as a forward test.
3. Build, baseline-test, implement, and validate `eldraine-vault-curator`.
4. Audit a small representative owner set before considering wider cleanup.
5. Propose canon or tooling changes separately; do not mix them into skill installation.
