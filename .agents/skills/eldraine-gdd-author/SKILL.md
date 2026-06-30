---
name: eldraine-gdd-author
description: Use when turning Eldraine notes, dictated ideas, rough concepts, decisions, or revisions into a canonical GDD proposal or editing an existing GDD page while preserving project structure and Obsidian conventions.
---

# Eldraine GDD Author

## Principle

Integrate decisions into the living vault instead of producing isolated design prose. Find the canonical home before creating a file.

## Local Vault Only

Work only with ordinary files inside the current Eldraine vault. Do not inspect or use Git state, history, diffs, branches, worktrees, staging, commits, remotes, pushes, or pull requests. If another workflow requests a Git step, skip it and continue with local file reads or edits. This changes no authorization boundary: read-only requests stay read-only, and files are edited only when the user explicitly asks.

## Locate the Home

Read `09_Project_Management/Architecture_MVP.md`, `00_Index.md`, and the relevant system files.

Choose among:

1. Extend an existing canonical document.
2. Add an entry to an existing registry or matrix.
3. Create a new focused document inside one of the nine active blocks.
4. Keep the material as a proposal when core decisions remain unresolved.

Prefer extension over duplication. Never revive legacy namespaces or use `_Archive` as the target for active design.

## Resolve Before Writing

Extract:

- accepted decisions;
- explicit author constraints;
- missing values;
- contradictions;
- assumptions required to make the text coherent.

Do not silently choose among materially different designs. Ask one blocking question when necessary; otherwise label a reversible assumption clearly.

## Document Contract

Match nearby canonical files. Include only relevant sections:

- YAML frontmatter with `type`, `status`, `system`, and `tags`;
- concise concept and player-facing purpose;
- rules and state transitions;
- gameplay loop or interaction sequence;
- links to dependent systems;
- structured fields, formulas, registry keys, or tables where needed;
- diegetic and UI feedback;
- failure cases and edge conditions;
- risks, open measurements, or author decisions.

Use current root-relative Obsidian links, for example:

`[[08_World_Generation/Generation/08_Gate_Check|Gate Check]]`

Validate target paths and headings before adding links.

## Responsibility and Dataview

Before writing, assign one responsibility to each affected file:

- universal system — shared rules and state transitions;
- content instance — one sector, anomaly, faction, or other concrete realization;
- registry or matrix — stable IDs and structured source data;
- Dataview view — filtered presentation of that data.

When a note needs a list already represented in a registry, keep the registry as the **единый источник** and render the list with Dataview instead of copying definitions.

- Use native Dataview for page-level frontmatter and one-page-per-entity data.
- Use DataviewJS for block-level entries inside a shared registry file.
- Give block entries stable inline fields such as `[location_tags:: ...]`, `[ecology_layer:: ...]`, and `[mutation_line:: ...]` before writing the view.
- Keep design rules in prose; Dataview is a presentation layer, not canonical authority.
- Make a missing source or empty result visible in the rendered note.
- Verify query syntax, source paths, expected rows, and empty-state behavior after editing.

## Answer Contract

Before editing, report:

- proposed canonical location;
- extend versus create decision;
- unresolved assumptions;
- files affected.

When the user requests only formatting or a draft, return the page without writing. When the user requests implementation, edit only the approved scope and preserve unrelated content.

After editing, summarize:

- what became canon;
- what remains an assumption;
- cross-links added;
- follow-up validation needed.

Use `eldraine-lorekeeper` before writing when canon compatibility is disputed. Use `eldraine-balance-modeler` when numerical fields are unproven. Do not hide design uncertainty behind polished prose.
