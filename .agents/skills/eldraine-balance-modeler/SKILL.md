---
name: eldraine-balance-modeler
description: Use when an active Eldraine claim depends on explicit numbers, formulas, thresholds, probabilities, costs, rewards, or breakpoints.
---

# Eldraine Balance Modeler

## Principle

Turn an active claim into the smallest falsifiable model. Distinguish canon from derived results and test assumptions.

## Current Sources

Read `00_Index.md`, the active canonical owner of the claim, and only its direct active dependencies or registries that define its inputs.

## Workflow

1. State the decision the number must support.
2. Label each input `GDD_FACT`, `DERIVED`, `TEST_ASSUMPTION`, or `UNKNOWN`, with units.
3. Define the smallest formula and model weak, baseline, and extreme cases.
4. Identify breakpoints, sensitivity, dead zones, cliffs, or reward-to-risk loops.

## Output

Return the question, inputs with sources, formula, scenario table, breakpoints, verdict, and prototype measurements. Use `SUPPORTED`, `FRAGILE`, `NO_CORRIDOR`, or `INSUFFICIENT_DATA`. Test assumptions are never recommendations.

## Stop

If the owner or intended decision is missing, return `MISSING_OWNER`. If a shared ownership decision is required, return `BLOCKED: ARCHITECTURE_DECISION_REQUIRED` with exact affected owner paths and the decision required. Recommend a specialist only when explicitly selected by the user or orchestration workflow.
