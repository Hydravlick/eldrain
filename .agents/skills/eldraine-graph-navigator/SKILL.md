---
name: eldraine-graph-navigator
description: Use when an Eldraine task needs cross-document dependency discovery, backlinks, blast-radius checks, broken-link checks, Obsidian wikilink resolution, or fast navigation across GDD canon, systems, lore, economy, gear, factions, quests, and project notes.
---

# Eldraine Graph Navigator

## Principle

Use the vault graph as a map, not as canon. It identifies likely neighbors and missing links; the linked documents still decide authority.

## Quick Start

Run from `C:\eldrain` before broad edits or dependency reviews:

```powershell
python .agents\skills\eldraine-graph-navigator\scripts\build_vault_graph.py . --out .agents\graph --cache .agents\graph\vault-graph-cache.json
```

For automatic refresh while editing notes, run:

```powershell
python .agents\skills\eldraine-graph-navigator\scripts\watch_vault_graph.py . --out .agents\graph --interval 2
```

Read:

- `.agents/graph/vault-graph-report.md` for summary, high-degree notes, broken links, and orphans.
- `.agents/graph/vault-graph.json` for exact `outgoing` and `backlinks` per note.
- `.agents/graph/vault-graph.dot` when a visual graph renderer is useful.

Use `--include-archive` only when tracing idea history. Active canon checks should normally exclude `_Archive`.

The cache is incremental: unchanged notes are reused, changed/new notes are parsed, deleted notes are removed, and backlinks are rebuilt from the refreshed link set. The watcher uses the same cache and polls Markdown file signatures, so new notes are picked up on the next interval.

## Workflow

1. Build the graph when the task spans more than one document, changes a shared rule, or asks for downstream effects.
2. Start from explicitly named notes, terms, systems, factions, characters, mechanics, or registry entries.
3. Inspect immediate `outgoing` and `backlinks`; then expand one hop at a time only when the connection affects the task.
4. Prefer live canonical blocks `01_` through `10_` over archives and scratch notes.
5. Report graph evidence separately from inference. A backlink suggests relevance; it does not prove dependency.

## Use With Other Eldraine Skills

- Use before `eldraine-lorekeeper` when canon authority or fictional causality may depend on neighboring notes.
- Use before `eldraine-narrative-impact` when a changed event, state, faction, or reveal may break downstream content.
- Use before `eldraine-gdd-author` when choosing whether to extend an existing page or create a new canonical page.
- Use before balance, gear, economy, player-lens, or crash-test reviews when a system has hidden dependencies in adjacent documents.

## Output Contract

When graph context mattered, include:

- the graph build date or that it was freshly generated;
- the seed notes or terms used;
- the directly relevant backlinks/outgoing notes;
- broken links or orphan notes that affect confidence;
- files opened after graph triage.

Do not open every high-degree note just because it is central. Use the graph to narrow reading, not to widen it without reason.
