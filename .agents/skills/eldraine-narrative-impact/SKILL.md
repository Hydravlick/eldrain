---
name: eldraine-narrative-impact
description: Use when an approved Eldraine narrative or world-state change needs its downstream story and content dependencies traced.
---

# Eldraine Narrative Impact

## Principle

Treat a narrative change as a dependency change with intentional consequences and explicit replacements.

## Current Sources

Read `00_Index.md`, the changed active owner, and direct active owners for named characters, factions, locations, quests, services, reveals, and states.

## Workflow

1. Trace `changed fact → affected state or knowledge → affected content → required response`.
2. Separate established, inferred, and undocumented dependencies.
3. Check immediate play, the current arc, long-term continuity, and player knowledge separately from character knowledge.
4. Classify logic holes, orphaned content, pacing damage, system dependencies, intentional irreversibility, and new opportunities.

## Output

Lead with `LOCAL`, `ARC`, or `FOUNDATIONAL`. Provide a horizon table with evidence and response, then the minimum continuity patch, stronger branch, intentional losses, files to update, and author decisions.

## Stop

If the changed fact or a required owner is absent, return `MISSING_OWNER`. If the change needs a shared architecture decision, return `BLOCKED: ARCHITECTURE_DECISION_REQUIRED` with exact owner paths and one question. Do not invoke another skill automatically.
