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
5. Classify each block as `KEEP`, `MOVE`, `LINK`, `MERGE`, `DELETE_DUPLICATE`, or `SPLIT_TO_NEW_OWNER`.
6. Apply the source and destination edits immediately.
7. Re-read every changed file and verify ownership manually.
8. Continue to the next owner.

Do not create an audit manifest, migration plan, scanner report, prose-candidate inventory, or temporary rewrite document unless the user explicitly asks for one. Do not perform a corpus-wide audit before editing.

### Manual Review

Perform structural refactoring by reading and reasoning about the Markdown. Do not use prose scanners, candidate counters, Python audit scripts, or heuristic banned-phrase detectors to decide what moves or gets rewritten.

Use search tools only to locate owners, references, duplicated claims, incoming links, and terminology. Validate each owner primarily by:

- re-reading the changed source;
- re-reading every destination modified by the move;
- searching for duplicated normative claims;
- verifying links and ownership boundaries;
- verifying that no factual or canonical claim disappeared.

Run mechanical project validation only when explicitly requested or after the semantic refactor is complete. It does not replace manual editorial judgment.

### Responsibility Model

Every active page has one primary responsibility.

- **LORE** owns world truth and in-world causality: metaphysics, history, culture, social meaning, origins, fictional terminology, beliefs, and diegetic explanation. It may explain why a mechanic fits the world, but it does not resolve gameplay state, costs, eligibility, formulas, rewards, failure handling, or runtime transitions.
- **MECHANIC** owns the player-facing interaction: what the player notices, can do, chooses, receives as feedback, and decides next. Read it as `PLAYER ACTION -> GAME RESPONSE -> FEEDBACK -> NEXT DECISION`. It may summarize system behavior for comprehension, but links to the system owner instead of becoming a second normative specification.
- **SYSTEM** owns authoritative resolution: inputs, source of truth, preconditions, triggers, states, ordered resolution, postconditions, costs, formulas, interfaces, edge cases, failure outcomes, and parameters.
- **ENTITY** owns what a faction, person, species, place, item family, Hearth, institution, or other world object is. Participation in a mechanic does not transfer ownership of that mechanic's rules.
- **CONTENT** owns one realization of an existing grammar: an encounter, sector, anomaly, quest, location, enemy instance, or authored event. Content consumes rules; it does not redefine them.
- **REGISTRY** owns stable structured records and IDs. It does not become a prose owner because many systems consume it.
- **MANAGEMENT** owns project decisions, risks, unresolved work, and process. It never owns a game rule.

### Structural Freedom

Preserve meaning, not document shape. You may rewrite headings, reorder sections, split or merge files, create a focused owner, correct responsibility metadata, move prose and tables, replace duplicated normative prose with a link, update consumers, retire an emptied source, and rewrite AI-shaped prose.

Unless the user explicitly requests a design change, preserve accepted canon facts, actual game rules, numeric values, IDs and registry keys, formulas, explicit negative boundaries, intentional uncertainty, meaningful examples, and authored voice that carries information or atmosphere. Heading structure, paragraph structure, sentence structure, and historical file boundaries are not protected invariants in structural refactor mode.

### Movement Rule

When material belongs elsewhere:

1. Find the existing canonical owner when one exists.
2. Move and integrate the information there.
3. Remove the duplicated normative version from the source.
4. Leave only the minimum contextual sentence and link needed for readability.

Do not copy a rule into both files. Create a new focused owner only when no destination exists and the responsibility is substantial enough to deserve independent reading. Small mechanic explanations may remain in a system page; small lore context may remain as one short non-normative paragraph. Do not create one file for every conceptual layer.

### Decision Boundary

Placement ambiguity is not a blocking design question. If canon is clear but documented poorly, choose the most coherent owner with the responsibility model and continue.

Stop only when active sources contain genuinely incompatible game rules or canon claims and choosing between them would change the design. Do not turn ordinary editorial judgment into `APPROVAL_REQUIRED`.

### AI-Shaped Prose

Do not hunt individual words. While repairing each owner, remove repeated conclusions, abstract announcement paragraphs, fake contrasts, redundant summaries, inflated significance, generic design-language filler, paragraphs about the document rather than the game, and atmosphere with no lore, mechanic, player-experience, or causal function.

Prefer direct statements of actor, condition, action, consequence, and meaning. Preserve useful lore voice, examples, sensory information, and emotional context.

### Completion Condition Per Owner

Continue only after:

- the primary responsibility is obvious from the first screen;
- foreign responsibility has moved or become a contextual link;
- the owner does not duplicate another owner's normative rule;
- every moved claim exists in its destination;
- affected links are valid;
- no accepted meaning was lost.

Then proceed immediately to the next owner.

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

In structural refactor mode, the normal result is changed canonical Markdown. Summarize owners repaired, destinations changed, decisions blocked by genuine source conflict, manual checks performed, and final mechanical validation. Do not substitute a findings report for the edits.
