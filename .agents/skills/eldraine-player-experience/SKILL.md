---
name: eldraine-player-experience
description: Use when a bounded active Eldraine player sequence needs review of perception, decision, feedback, and failure comprehension.
---

# Eldraine Player Experience

## Principle

Every important rule must become something the player perceives, interprets, decides about, and remembers.

## Current Sources

Read `00_Index.md`, the active owner of the bounded sequence, and its direct active dependencies for player state, feedback, commitment, and outcomes.

## Workflow

1. Select the bounded mode: onboarding, encounter, combat, failure, or hub-to-raid.
2. State the intended emotional arc.
3. For each beat, record perception, interpretation, decision, commitment, feedback, and consequence.
4. Flag invisible causality, unsupported interpretation, fake choice, excessive load, and feedback gaps.

## Output

Return the chronological slice, strong beats, experience gaps, misread risks, minimum feel pass, success/retreat/failure outcomes, and playtest observations about perception, timing, feel, or comprehension.

## Stop

If the underlying rule or owner is absent, return `MISSING_OWNER`. If the sequence requires a shared architecture decision, return `BLOCKED: ARCHITECTURE_DECISION_REQUIRED` with exact paths and one question. Do not invoke another skill automatically.
