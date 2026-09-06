# Eldrain

Eldrain is a PvPvE extraction game developed in this local Obsidian vault. The vault is the working surface; Git is history and recovery. Work in the current checkout, preserve unrelated edits, and do not create worktrees, branches or GitHub workflows for ordinary documentation work.

## Find the source

Start at `00_Index.md`, select the relevant `00_Routes.md`, then read the owner and dependencies needed for the question. Expand through incoming links and targeted search when useful. Harness/tooling tasks can start in their own files.

Active owners under `01_` through `08_` establish game canon. `09_Project_Management` contains current work, risks and placement decisions: `TODO.md`, `Risk_Register.md`, `Architecture_MVP.md`. It does not resolve gameplay. `10_Reference`, fiction, proposals and harness material provide context. Cite current rules to their owners; distinguish context and inference.

Routes and the root index are generated projections. Change source metadata, then run the route builder when navigation is affected. Never edit generated route text manually.

## Choose the thinking needed

Skills live in [.agents/skills](.agents/skills); select the smallest useful set. A skill is a workflow, not a separate agent or a mandatory pipeline. Routine edits do not require a plan document, specialist handoff or repeated approval.

| Need | Skill |
|---|---|
| Explain behavior, genre forces, causality or transfer from other games | `eldraine-design-researcher` |
| Decide feature/system decomposition, ownership or interfaces | `eldraine-design-architect` |
| Write an accepted decision or improve GDD prose | `eldraine-gdd-editor` |
| Understand lived flow, feedback, failure and player lenses | `eldraine-player-experience` |
| Check quantities, breakpoints, tuning or sensitivity | `eldraine-balance-modeler` |
| Check fiction truth, culture, voice or narrative consequence | `eldraine-lorekeeper` |
| Attack a defined proposal for exploits and degenerate play | `eldraine-crash-test` |
| Move/rename notes, repair links/properties/routes or derived views | `eldraine-vault-maintenance` |

A Feature is a complete player-facing capability assembled from systems, UX and content. A System owns a coherent state/rule model; a Mechanic is a local rule or action; Content configures existing rules. Entity, Registry, Lore and full distinctions are in [design vocabulary](.agents/policies/design-architecture.md). Read the [Feature contract](.agents/policies/feature-contract.md) when needed. Feature descriptions live in `01_Core_Vision/Features`; their map is `01_Core_Vision/Feature_Map.md`.

Research distinguishes observed outcomes, implementation, claimed causes and working conditions. Use internal evidence and project references first; obtain external evidence when required. Read [causal research](.agents/policies/design-research.md) for evidence grading, transfer and first-/second-order effects.

## Preserve and finish

One rule/data field has one owner. Features, lore, indexes and derived views must not become competing universal-rule sources. Preserve Glossary names and stable IDs. Report incompatible owners as `SOURCE_CONFLICT` and missing ownership as `MISSING_OWNER`, with exact paths. The latest explicit user decision authorizes its integration.

Carry requested edits through the vault and affected consumers. Ask only for a necessary unresolved product decision; ordinary placement, wording and mechanical repair are within scope. For refactoring, integrate unique meaning before source deletion and finish each owner with its destinations. Preserve rationale, examples, experience and lore synthesis. See [editing](.agents/policies/editing.md) and [canon ownership](.agents/policies/canon-ownership.md).

Use a design-correctness pass before the [editorial pass](.agents/policies/editorial-quality.md). Human prose is a shared standard. [Obsidian workflow](.agents/policies/obsidian-workflow.md) covers filesystem moves, properties/wikilinks and user-installed format skills. Bases/Canvas/Dataview stay derived; use the official CLI only if actually available.

## Check the result

With Python 3.10+ and dependencies from `tools/requirements.txt`:

```powershell
python tools/vault_guard.py
python tools/build_routes.py --check
python tools/check_harness.py
python -m unittest discover -s tools -p "test_*.py"
```

Use focused checks after meaningful batches and the relevant full suite before finishing. `python tools/build_routes.py --write` regenerates projections; honor explicit deferral and report pending files. [Validation policy](.agents/policies/validation.md) defines the status model, scope and mechanical limits. Tests do not decide whether prose is good or meaning survived.
