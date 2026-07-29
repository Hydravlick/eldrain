---
name: eldraine-lorekeeper
description: Use when an Eldraine lore, faction, terminology, or fiction-to-mechanics change needs compatibility review against active canonical owners.
---

# Eldraine Lorekeeper

## Principle

Protect active canon’s causal meaning while identifying deliberate retcons and missing mechanics.

## Current Sources

Read `00_Index.md`, the active lore or entity owner, its active mechanic owner where the claim is playable, and only their direct dependencies. For a Hearth, begin with the relevant active lore, interface, and mechanic owners.

## Workflow

1. Extract the proposed claims and classify evidence as `CANON`, `INFERENCE`, or `OPEN_QUESTION`.
2. Check metaphysics, player fantasy, social logic, terminology, and fiction-to-mechanics compatibility.
3. Separate in-world authority, player-facing interface, and mechanic authority.
4. Distinguish compatible additions, tensions, conflicts, deliberate retcons, and absent owners.

## Output

Return `CANON`, `COMPATIBLE`, `UNDERDEFINED`, `TENSION`, `CONFLICT`, or `RETCON`; cite exact owner paths and headings, explain the player consequence, give minimal reconciliation, and name GDD updates.

## Stop

If evidence or a mechanic owner is missing, return `MISSING_OWNER`. For a shared architecture decision, return `BLOCKED: ARCHITECTURE_DECISION_REQUIRED` with exact paths and a question. Do not invoke another skill automatically.
