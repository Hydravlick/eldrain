---
name: eldraine-gear-progression
description: Use when an active Eldraine equipment or loadout progression boundary needs testing for meaningful upgrades and dominant loadouts.
---

# Eldraine Gear Progression

## Principle

Judge complete replaceable loadouts across repeated runs, not isolated item statistics.

## Current Sources

Read `00_Index.md`, the active equipment owner, and direct active dependencies that define access, capability, logistics, loss, extraction, and recovery.

## Workflow

1. Label inputs `GDD_FACT`, `DERIVED`, `TEST_ASSUMPTION`, or `UNKNOWN`.
2. Compare welfare, balanced, armor-first, glass-cannon, specialist, party-carrier, and maximum practical loadouts when relevant.
3. Check substitution, mandatory tiers, obsolescence, free-riding, avoidance, snowballing, and repetitive optimal kits.
4. Assess marginal capability, consistency, loss exposure, logistics, and recovery rather than one score.

## Output

Return the progression promise, loadout table, dominance findings, healthy niches, smallest repair, systemic alternative, and measurements. Use `HEALTHY`, `FRAGILE`, `DOMINATED`, or `INSUFFICIENT_DATA`.

## Stop

If equipment’s owner or its decision boundary is absent, return `MISSING_OWNER`. For a shared ownership decision, return `BLOCKED: ARCHITECTURE_DECISION_REQUIRED` with exact owner paths and a single decision question. Do not invoke specialists automatically.
