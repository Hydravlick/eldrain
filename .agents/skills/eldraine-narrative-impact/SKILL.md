---
name: eldraine-narrative-impact
description: Use when changing an Eldraine plot event, reveal, character fate, faction state, player choice, quest outcome, secret, or chronology and downstream narrative or systemic dependencies may break.
---

# Eldraine Narrative Impact

## Principle

Treat story changes as dependency changes. Preserve intentional consequences while exposing accidental dead ends and contradictions.

## Local Vault Only

Work only with ordinary files inside the current Eldraine vault. Do not inspect or use Git state, history, diffs, branches, worktrees, staging, commits, remotes, pushes, or pull requests. If another workflow requests a Git step, skip it and continue with local file reads or edits. This changes no authorization boundary: read-only requests stay read-only, and files are edited only when the user explicitly asks.

## Responsibility Boundary

Own the downstream narrative and world-state dependency graph of a changed premise. Do not decide the cross-system gameplay contract or use narrative cost as proof that an architecture is healthy. When a gameplay architecture change drives the story change, `eldraine-system-architect` decides the system boundary and this skill reports its narrative blast radius.

## Trace the Change

Read the changed premise and search for every directly named character, faction, location, quest, service, reveal, and term. Build a compact dependency chain:

`changed fact -> affected knowledge/state -> affected content -> required replacement`

Separate:

- established dependency;
- inferred dependency;
- missing documentation.

## Time Horizons

Check:

1. **Immediate:** current scene, tutorial, reward, access, dialogue, party state.
2. **Current arc:** active quests, faction relationships, pacing, available services.
3. **Long term:** later reveals, endings, recurring characters, world-state logic.

Also check player knowledge versus character knowledge. Early truth can break suspense even when world causality remains valid.

## Classify Damage

Use:

- `LOGIC HOLE` — content assumes a fact that is no longer true.
- `ORPHANED CONTENT` — quest or asset loses its trigger or purpose.
- `PACING DAMAGE` — reveal, escalation, or emotional beat arrives at the wrong time.
- `SYSTEM DEPENDENCY` — access, economy, tutorial, or progression relied on the narrative state.
- `INTENTIONAL IRREVERSIBILITY` — meaningful consequence that should remain.
- `NEW OPPORTUNITY` — branch or theme unlocked by the change.

## Answer Contract

Lead with the overall blast radius: `LOCAL`, `ARC`, or `FOUNDATIONAL`.

Then provide:

| Horizon | Broken or changed dependency | Evidence | Required response |
|---|---|---|---|

Finish with:

- minimum continuity patch;
- stronger branch that embraces the consequence;
- content that should remain lost because the choice needs weight;
- files that require updates;
- unresolved author decisions.

Do not restore all lost content automatically. Do not confuse expensive consequences with narrative errors. Use `eldraine-lorekeeper` when the problem is canon authority rather than downstream structure. Do not edit files unless asked.
