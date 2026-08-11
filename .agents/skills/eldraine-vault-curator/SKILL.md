---
name: eldraine-vault-curator
description: Use when auditing or repairing Eldraine note authority, duplicated rules, mixed lore/mechanic/system responsibility, owner-page readability, AI-shaped prose, broken navigation, stale proposals, or structural corpus drift without changing accepted canon or game-design decisions.
---

# Eldraine Vault Curator

## Principle

Audit authority before style. Remove text that hides a decision, but preserve text that carries canon, player experience, or an intentional voice.

## Active Canon Language

Describe the accepted target state affirmatively: name the active entities, rules, scope, and consequences.

Historical context belongs outside active rule statements. When it helps explain provenance or a reference, label it as contextual material and return the adopted model in the canonical result.

## Responsibility Boundary

Own note administration, responsibility separation, prose health, and the safety of structural repairs. Relocate established meaning and create a focused owner when placement is the problem and no suitable owner exists. Do not decide a disputed game rule, retcon lore, rebalance values, or choose between incompatible active claims. Route those questions through the matching Eldraine specialist.

## Mode Selection

Use **audit mode** when the user asks to inspect, review, diagnose, or report findings. Default to findings only. Rewriting requires explicit approval for named files and a bounded edit surface. Never infer a corpus-wide rewrite from an audit request.

Use **structural refactor mode** when the user asks to clean, reorganize, separate responsibilities, remove AI-shaped documentation, split lore from mechanics or systems, repair mixed authority, or refactor the active corpus. A request covering a directory, domain, or the active corpus approves the structural edits required inside that scope. Do not request separate approval for each file, heading, move, split, merge, or deletion unless the edit would change a game-design decision or canon fact.

In either mode, start at `00_Index.md`, resolve the subject to its active owner, and read that owner plus only the direct dependencies required for the current judgment. Treat route pages as projections, registries as structured records, and contextual material as provenance rather than active authority.

## Structural Refactor Mode

Structural refactor mode is an edit mode, not an audit-only mode.

Process the corpus **owner by owner**. Complete the current owner's analysis and repair before advancing:

1. Read the owner.
2. Read only its direct dependencies, obvious destination owners, and relevant incoming consumers required to understand misplaced material.
3. State internally what the current file is supposed to own.
4. Divide its content into semantic responsibility blocks.
5. Classify each block as `KEEP`, `MOVE`, `ALREADY_OWNED`, `LINK`, `MERGE`,
   `STALE_SUPERSEDED`, `DELETE_TRUE_DUPLICATE`, or `SPLIT_TO_NEW_OWNER`.
6. Apply destination edits first for every `MOVE` or split.
7. Verify destination semantic coverage.
8. Only then remove, compress, or rewrite the source block.
9. Re-read every changed file and complete the semantic coverage check.
10. Continue to the next owner.

Do not create an audit manifest, migration plan, scanner report, prose-candidate inventory, or temporary rewrite document unless the user explicitly asks for one. Do not perform a corpus-wide audit before editing.

### Semantic Coverage Invariant

Structural refactoring preserves the useful meaning of the corpus even when
file boundaries, headings, and authority placement change.

For every semantic block that is removed, compressed, or replaced, exactly
one disposition must be true:

- `MOVE` — the block contains unique accepted meaning and is integrated into
  an exact destination owner or supporting page before source deletion;
- `ALREADY_OWNED` — an exact destination already preserves the same meaning
  at sufficient detail, so the source may reduce its duplicate statement to
  context plus a link;
- `STALE_SUPERSEDED` — an active owner clearly replaced or contradicted the
  old statement, so retaining it would preserve obsolete meaning rather than
  canon;
- `DELETE_TRUE_DUPLICATE` — the block adds no unique rule, canon,
  explanation, example, player-facing sequence, sensory information,
  design rationale, uncertainty, or intentional voice beyond material that
  remains.

A block may not disappear merely because another page owns a related rule.
Related authority is not equivalent semantic coverage.

For `MOVE` and `ALREADY_OWNED`, identify internally the exact destination
path and section or semantic block that preserves the meaning.

If no destination actually preserves it, use `MOVE`, `KEEP`, or
`SPLIT_TO_NEW_OWNER`; do not delete it.

Do not use brevity, DRY, one-rule-one-owner, an `overview` label, or the
existence of links as sufficient justification for deletion.

### Per-Owner Semantic Ledger

Before changing the current owner, maintain a compact internal ledger for
every block that may be moved, compressed, rewritten substantially, or
deleted:

SOURCE BLOCK: <heading or recognizable fragment>
PRIMARY FUNCTION: <LORE | MECHANIC | SYSTEM | ENTITY | CONTENT | REGISTRY |
  OVERVIEW | DESIGN_RATIONALE | PRESENTATION | PLAYER_EXPERIENCE | MANAGEMENT>
UNIQUE MEANING: <claims, causal explanation, example, sequence, feedback,
  uncertainty, voice, or boundary that would be lost>
DISPOSITION: <KEEP | MOVE | ALREADY_OWNED | LINK | MERGE |
  STALE_SUPERSEDED | DELETE_TRUE_DUPLICATE | SPLIT_TO_NEW_OWNER>
DESTINATION: <exact path + section, or NONE when KEEP>
COVERAGE PROOF: <what in the post-edit corpus preserves the useful meaning>

Do not write this ledger into the vault unless the user explicitly requests
it. It is an internal per-owner reasoning aid.

If `UNIQUE MEANING` is non-empty, `DELETE_TRUE_DUPLICATE` is invalid.

### Manual Review

Perform structural refactoring by reading and reasoning about the Markdown. Do not use prose scanners, candidate counters, Python audit scripts, or heuristic banned-phrase detectors to decide what moves or gets rewritten.

Use search tools only to locate owners, references, duplicated claims, incoming links, and terminology. Validate each owner primarily by:

- re-reading the changed source;
- re-reading every destination modified by the move;
- searching for duplicated normative claims;
- verifying links and ownership boundaries;
- verifying that no factual or canonical claim disappeared.

For structural refactor mode, semantic validation is manual. Do not run Python scanners, validators, route builders, or `vault_guard` during owner-by-owner work or use their output to decide what content moves, survives, splits, or is deleted. After the full named scope is complete, run `vault_guard` once as a mechanical integrity check. Its output is not semantic evidence and must not override manual editorial judgment.

When generated projections become stale, record them for regeneration after the semantic refactor. Do not interrupt owner-by-owner structural work to regenerate them.

### Structured Duplication Check

When the current owner contains a structured list, table, registry-like
summary, or repeated set of named IDs, search those exact IDs in the active
corpus before deciding that the block is unique or safely duplicated.

If the same structured set occurs in multiple active pages, identify which
page owns:

- the normative records;
- the player-facing explanation;
- any legitimate overview.

Resolve the duplication while processing the current owner and its direct
destinations. Do not defer it to a later domain-wide cleanup pass.

### Responsibility Model

Every active page has one primary responsibility.

- **LORE** owns world truth and in-world causality: metaphysics, history, culture, social meaning, origins, fictional terminology, beliefs, and diegetic explanation. It may explain why a mechanic fits the world, but it does not resolve gameplay state, costs, eligibility, formulas, rewards, failure handling, or runtime transitions.
- **MECHANIC** owns the player-facing interaction: what the player notices, can do, chooses, receives as feedback, and decides next. Read it as `PLAYER ACTION -> GAME RESPONSE -> FEEDBACK -> NEXT DECISION`. It may summarize system behavior for comprehension, but links to the system owner instead of becoming a second normative specification.
- **SYSTEM** owns authoritative resolution: inputs, source of truth, preconditions, triggers, states, ordered resolution, postconditions, costs, formulas, interfaces, edge cases, failure outcomes, and parameters.
- **ENTITY** owns what a faction, person, species, place, item family, Hearth, institution, or other world object is. Participation in a mechanic does not transfer ownership of that mechanic's rules.
- **CONTENT** owns one realization of an existing grammar: an encounter, sector, anomaly, quest, location, enemy instance, or authored event. Content consumes rules; it does not redefine them.
- **REGISTRY** owns stable structured records and IDs. It does not become a prose owner because many systems consume it.
- **MANAGEMENT** owns project decisions, risks, unresolved work, and process. It never owns a game rule.
- **OVERVIEW** owns useful synthesis for orientation. It may connect several
  owners, explain the reader-facing model, sequence, trade-offs, or
  conceptual map, but does not become a second normative specification.
- **DESIGN_RATIONALE** owns why an accepted design constraint exists, which
  failure mode it prevents, and which trade-off it protects. It does not
  resolve runtime state unless it is also the explicit system owner.
- **PRESENTATION** owns how accepted facts or mechanics are communicated
  through UI, camera, animation, sound, material state, spatial staging, or
  world feedback. It may consume mechanics without owning their resolution.
- **PLAYER_EXPERIENCE** owns the intended lived sequence, comprehension,
  tension, learning order, failure readability, and emotional consequence
  across accepted rules. It synthesizes owners without redefining them.

Only a genuine route, index, or generated navigation page should have pure
navigation as its primary responsibility.

Do not turn an `OVERVIEW`, `DESIGN_RATIONALE`, `PRESENTATION`,
`PLAYER_EXPERIENCE`, `LORE`, or `MECHANIC` page into a bare list of owner
links as a substitute for structural refactoring.

### Normative Leakage

In `LORE`, `ENTITY`, `OVERVIEW`, `PRESENTATION`, and
`PLAYER_EXPERIENCE` pages, treat exact runtime resolution as mixed authority
unless the page is the explicit `SYSTEM` owner.

Strong signals include:

- exact eligibility predicates;
- boolean conditions;
- formulas and numeric thresholds;
- ordered state transitions;
- exact costs;
- exact reward or failure resolution;
- authoritative parameter values.

A non-system page may name or summarize such a rule for comprehension, but
must not reproduce enough of the resolver contract to become an alternative
authority.

A disclaimer elsewhere in the file does not legalize normative leakage in a
different semantic block.

### Structural Freedom

Preserve meaning, not document shape. You may rewrite headings, reorder sections, split or merge files, create a focused owner, correct responsibility metadata, move prose and tables, replace duplicated normative prose with a link, update consumers, retire an emptied source, and rewrite AI-shaped prose.

Unless the user explicitly requests a design change, preserve accepted canon facts, actual game rules, numeric values, IDs and registry keys, formulas, explicit negative boundaries, intentional uncertainty, meaningful examples, and authored voice that carries information or atmosphere. Heading structure, paragraph structure, sentence structure, and historical file boundaries are not protected invariants in structural refactor mode.

### Movement Rule

When material belongs elsewhere:

1. Find the existing canonical owner when one exists.
2. Compare the source block with the exact destination; do not assume a
   related page already covers it.
3. If the source contains unique accepted meaning, move and integrate that
   meaning into the destination before source deletion.
4. Re-read the destination and verify that the moved meaning survived
   integration without ownership drift.
5. Remove the duplicated normative version from the source only after
   coverage is proven.
6. Leave the amount of contextual explanation needed for the source page to
   fulfill its own primary responsibility, plus links to normative owners.

Do not copy a normative rule into both files.

Do not remove non-normative synthesis merely because the normative rule
lives elsewhere.

If a mixed page contains several substantial unique responsibilities,
migrate or split those unique blocks first. Shrink or retire the source only
after each block has a proven destination or is proven stale/duplicated.

Create a new focused owner only when no destination exists and the
responsibility is substantial enough to deserve independent reading. Small
mechanic explanations may remain in a system page; small lore context may
remain as one short non-normative paragraph. Do not create one file for every
conceptual layer.

### Split Trigger

Treat a semantic block as a `SPLIT_TO_NEW_OWNER` candidate when all are true:

1. it has a different primary semantic responsibility from the current
   page's primary responsibility;
2. it contains substantial unique meaning;
3. it forms a coherent independently readable unit;
4. keeping it in place would leave the page with mixed authority or mixed
   reader purpose;
5. no existing owner can absorb it without losing that function.

A self-contained mechanic with its own steps, states, decision loop, or
resolution contract is a strong split candidate even when it is thematically
related to the surrounding page.

Frontmatter `type` is evidence only. Do not infer responsibility mechanically
from metadata.

### Ownership-Safe Summaries

A contextual summary may simplify detail but must preserve ownership
semantics and concept boundaries.

Before writing a summary of another owner, verify the destination's actual
contract. Do not fuse two adjacent responsibilities into one convenient
sentence.

For example, if Chronicle records lived facts while `Tags_System` owns
Personal Tags, a summary may say:

"Chronicle records lived facts; Tags System owns Personal Tags."

It must not compress this into:

"Chronicle stores lived experience and personal tags."

A summary that changes who owns a state, rule, tag, result, or lifecycle
decision is a semantic regression even when every individual noun already
exists elsewhere in the corpus.

### Decision Boundary

Placement ambiguity is not a blocking design question. If canon is clear but documented poorly, choose the most coherent owner with the responsibility model and continue.

Stop only when active sources contain genuinely incompatible game rules or canon claims and choosing between them would change the design. Do not turn ordinary editorial judgment into `APPROVAL_REQUIRED`.

### AI-Shaped Prose

Do not hunt individual words. While repairing each owner, remove repeated conclusions, abstract announcement paragraphs, fake contrasts, redundant summaries, inflated significance, generic design-language filler, paragraphs about the document rather than the game, and atmosphere with no lore, mechanic, player-experience, presentation, design-rationale, or causal function.

Prefer direct statements of actor, condition, action, consequence, and meaning. Preserve useful lore voice, examples, sensory information, and emotional context.

### Post-Edit Semantic Coverage Check

Before leaving the current owner, compare the pre-edit meaning against the
changed source and destinations.

Answer internally:

1. What unique information, explanation, example, sequence, feedback,
   uncertainty, or voice existed before this edit?
2. Where does each valuable element exist now?
3. Did any useful block disappear only because another page owns a related
   rule?
4. Did any summary change an ownership boundary, causal relationship, or
   distinction between concepts?
5. Does the source still perform its own primary responsibility, or was it
   accidentally reduced to navigation?
6. If the source became much shorter, can every removed block be justified
   by `ALREADY_OWNED`, `STALE_SUPERSEDED`, `DELETE_TRUE_DUPLICATE`, or a
   completed `MOVE`?

If any answer is uncertain, restore the material or move it properly before
advancing.

Do not defer semantic-loss repair to a later corpus pass.

### Completion Condition Per Owner

Continue only after:

- the primary responsibility is obvious from the first screen;
- foreign normative responsibility has moved or become a contextual link;
- the owner does not duplicate another owner's normative rule;
- every `MOVE` is already integrated into its destination;
- every removed or substantially compressed block has a valid semantic-ledger disposition;
- every `ALREADY_OWNED` and `STALE_SUPERSEDED` entry names an exact active destination;
- every non-empty `UNIQUE MEANING` still exists in the post-edit corpus;
- overview, rationale, presentation, player-experience, lore voice, examples and sensory feedback survive when they perform a distinct function;
- contextual summaries preserve the actual ownership boundaries of their source owners;
- the source still performs its own primary responsibility instead of becoming accidental navigation;
- affected links are valid;
- no accepted or otherwise valuable meaning was lost.

Then proceed immediately to the next owner.

### Early Refactor Calibration

After the first three owners that receive substantial structural changes,
compare their pre-edit versions against the resulting source and
destinations.

This is not a user-approval checkpoint and does not stop the corpus pass when
clean.

Specifically test whether:

- unique semantic blocks survived;
- `ALREADY_OWNED` destinations actually preserve equivalent meaning;
- overview/presentation/rationale pages still perform their reader function;
- no summary changed ownership semantics.

If semantic loss is found, repair those owners and correct the working
interpretation before continuing through the remaining corpus.

## Audit Mode

Audit four layers separately:

1. **Authority:** one rule, one active owner; no duplicated normative prose.
2. **Lifecycle:** context becomes a decision, migrates to the owner, updates consumers, validates, then retires its temporary source.
3. **Readability:** the first screen states the adopted rule, player action, and consequence.
4. **Prose health:** structure and repetition first; lexical mannerisms second.

## Render-Safe Tables

Treat an Obsidian table as a narrow reading surface. Keep it to short, scannable cells and no more columns than the decision needs.

### Required Markdown contract

1. Treat every unescaped `|` as a column separator. This includes an Obsidian link's alias separator.
2. A table cell may contain one short Obsidian link only when its alias separator is written as `\|`. The visible label must be sufficient without the path.
3. Put root-relative paths, raw URLs, multi-item owner lists, and Markdown line breaks outside the table. If a cell needs more than one link, use a titled owner/reference list immediately below it.
4. Escape every literal pipe in a table cell as `\|`. Never use unescaped `|` inside a cell.
5. Before handoff, verify the affected table has its declared number of columns in rendered view; inspect every table wiki-link for the `\|` alias separator.

Use this shape:

```markdown
| Слой | Владелец | Передаёт |
|---|---|---|
| Доступность | [[04_Player_Entities/Lifecycle_Roster\|Lifecycle Roster]] | readiness |

### Владельцы

- Несколько владельцев или длинное объяснение — вынести из таблицы в этот список.
```

If a row still wraps enough to stop a player from scanning it, replace the table with headings or a list and inspect the rendered note before handoff.

## Register Profiles

Choose one profile before judging prose:

| Register | Required voice | Keep atmosphere when |
|---|---|---|
| `SYSTEM` | Terms, states, conditions, formulas, exact outcomes | It identifies a player-visible signal or consequence |
| `MECHANIC` | Player action, response, decision, feedback, example | It clarifies the intended feeling or decision |
| `LORE` | Approved in-world or authorial voice | It carries canon, inference, mystery, or character identity |
| `MANAGEMENT` | Decision, owner, risk, evidence, next action | Rarely; only when recording an explicit creative constraint |

Do not apply an English banned-word list to Russian text. A marker is evidence only when it obscures or repeats a concrete claim. An approved author sample outranks general punctuation or cadence preferences.

## Finding Classes

Use only supported findings:

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

For every finding report:

| Field | Required content |
|---|---|
| Evidence | Exact path, heading or line, and quoted fragment |
| Authority impact | Which owner or consumer becomes ambiguous |
| Repair | The **smallest safe repair** |
| Preserved meaning | Rules, IDs, values, dependencies, voice, and negative boundaries that must survive |
| Approval | Whether author or specialist approval is required |
| Validation | Exact commands or owner checks |

## Audit Rewrite Invariants

An audit-mode prose rewrite must preserve unless the approved edit explicitly includes a structural change:

- YAML frontmatter and owner metadata;
- heading structure;
- fenced code, inline code, blockquotes, and tables;
- Obsidian and Markdown link targets;
- rule IDs, registry keys, numeric literals, units, formulas, state transitions, and negative authority boundaries;
- every factual claim from the source.

Never add a fact, name, number, date, quote, citation, or canon claim during cleanup. In structural refactor mode, preserve the semantic invariants under **Structural Freedom** instead of the original heading or file shape. Use the approved voice rather than mechanically regularizing punctuation.

## Two-Pass Review

### Pass 1: structure

Find duplicated conclusions, repeated section openings, equal-length paragraph cadence, forced triplets, contrast formulas such as “не просто X, а Y”, announcement sentences, and abstract atmosphere where an actor, condition, or outcome is required.

### Pass 2: language

After structural repair is proposed, check inflated significance, promotional adjectives, vague attribution, synonym cycling, excessive transitions, manufactured punchlines, and unsupported certainty. Do not flag a word in isolation.

## Deterministic Tools

These tools belong to audit mode. Do not use them to make semantic decisions in structural refactor mode.

Run the detect-only scanner on bounded Markdown paths:

```powershell
python .agents/skills/eldraine-vault-curator/scripts/audit_prose.py --json <path.md>
```

The scanner emits candidates; it does not establish canon and does not rewrite files.

After an approved rewrite, validate protected structure:

```powershell
python .agents/skills/eldraine-vault-curator/scripts/validate_rewrite.py --json <before.md> <after.md>
```

A validator failure blocks the rewrite until the protected difference is explicitly approved as a design change and routed through its owner.

## Answer Contract

In audit mode, lead with `CLEAN`, `REPAIRABLE`, `AUTHORITY_BLOCKED`, or `APPROVAL_REQUIRED`. Separate authority findings from prose findings. Rank at most five repairs by impact, then name the first owner-scoped edit worth making. Do not turn a finding list into another essay.

In structural refactor mode, the normal result is changed canonical Markdown. Summarize owners repaired, destinations changed, decisions blocked by genuine source conflict, manual checks performed, and generated projections pending regeneration. Mention mechanical validation only when the user explicitly requested it. Do not substitute a findings report for the edits.
