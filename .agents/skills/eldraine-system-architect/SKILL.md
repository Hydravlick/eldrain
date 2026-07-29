---
name: eldraine-system-architect
description: Use when an Eldraine change spans two or more active canonical owners, has an unresolved ownership conflict, or requires an architectural decision before specialist analysis.
---

# Eldraine System Architect

## Principle

Protect player competence through one owner per rule, legible uncertainty, causal loss, and reusable learning.

## Current Sources

Read `00_Index.md`, `01_Core_Vision/01_Vision.md`, `09_Project_Management/Architecture_MVP.md`, the active owners named by the change, and only their direct active dependencies.

## Workflow

1. State the player promise, deliberate uncertainty, and evidence class: `AUTHOR_CONSTRAINT`, `GDD_FACT`, `STRUCTURAL_INFERENCE`, `EMPIRICAL_UNKNOWN`, or `CONTENT_GAP`.
2. Map only affected states: one owner, source of truth, visibility, decision moment, duration, reversibility, loss, and downstream readers.
3. For every relevant uncertainty, record reveal time, commitment already paid, available response, failure signal, and stable knowledge retained.
4. Test owner duplication, boundary multiplication or cancellation, bypass, timing compression, information stacking, exception growth, and learning reset.
5. Define content-independent invariants, repair directions, and the smallest author decisions required before content work.

## Output

Return `COHERENT`, `FRAGILE`, `CONTRADICTORY`, or `UNSPECIFIED`. Include the player contract, responsibility map, certainty ledger, findings, invariants, cross-layer abuse chains, repair directions, author decisions, and bounded evidence requests.

## Stop

If an owner is absent, return `MISSING_OWNER`; if active owners conflict, return `SOURCE_CONFLICT` with exact paths. Recommend a specialist by name and bounded question only when the user or orchestration workflow explicitly selects it; never invoke it automatically.
