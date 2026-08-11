---
name: eldraine-vault-curator
description: Use when auditing or repairing Eldraine note authority, duplicated rules, owner-page readability, AI-shaped prose, broken navigation, stale proposals, or structural drift in Markdown without changing the intended canon.
---

# Eldraine Vault Curator

## Principle

Audit authority before style. Remove text that hides a decision, but preserve text that carries canon, player experience, or an intentional voice.

## Active Canon Language

Describe the accepted target state affirmatively: name the active entities, rules, scope, and consequences.

Historical context belongs outside active rule statements. When it helps explain provenance or a reference, label it as contextual material and return the adopted model in the canonical result.

## Responsibility Boundary

Own note administration, prose-health findings, and the safety of approved rewrites. Do not decide a disputed game rule, retcon lore, rebalance values, or create a second owner. Route those questions through the matching Eldraine specialist before proposing a repair.

## Detect First

Default to findings only. Rewriting requires **explicit approval** for named files and a bounded edit surface. Never run a corpus-wide rewrite from an audit request.

Start at `00_Index.md`, resolve the subject to its active owner, and read that owner plus direct dependencies. Treat route pages as projections, registries as structured records, and contextual material as provenance rather than active authority.

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

## Protected Invariants

An approved prose rewrite must preserve:

- YAML frontmatter and owner metadata;
- heading structure;
- fenced code, inline code, blockquotes, and tables;
- Obsidian and Markdown link targets;
- rule IDs, registry keys, numeric literals, units, formulas, state transitions, and negative authority boundaries;
- every factual claim from the source.

Never add a fact, name, number, date, quote, citation, or canon claim during cleanup. Preserve information, not paragraph shape. Use the approved voice rather than mechanically regularizing punctuation.

## Two-Pass Review

### Pass 1: structure

Find duplicated conclusions, repeated section openings, equal-length paragraph cadence, forced triplets, contrast formulas such as “не просто X, а Y”, announcement sentences, and abstract atmosphere where an actor, condition, or outcome is required.

### Pass 2: language

After structural repair is proposed, check inflated significance, promotional adjectives, vague attribution, synonym cycling, excessive transitions, manufactured punchlines, and unsupported certainty. Do not flag a word in isolation.

## Deterministic Tools

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

Lead with `CLEAN`, `REPAIRABLE`, `AUTHORITY_BLOCKED`, or `APPROVAL_REQUIRED`. Separate authority findings from prose findings. Rank at most five repairs by impact, then name the first owner-scoped edit worth making. Do not turn a finding list into another essay.
