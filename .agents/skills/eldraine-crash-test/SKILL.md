---
name: eldraine-crash-test
description: Use when a defined active Eldraine rule, reward, economy loop, progression boundary, or interface needs adversarial testing for exploits or dominant play.
---

# Eldraine Crash Test

## Principle

Test the incentives created by an active rule: rational play, not ideal play.

## Current Sources

Read `00_Index.md`, the active canonical owner of the rule, and its direct active dependencies for cost, reward, failure, repetition, and counterplay.

## Workflow

1. Record the intended player decision and label evidence `GDD_FACT`, `INFERENCE`, or `TEST_ASSUMPTION`.
2. Attack relevant combat, economy, risk, progression, party, population, and boredom surfaces.
3. Test optimizer, solo, coordinated-party, newcomer, and veteran behavior only where it can change the result.
4. Separate strong strategies with healthy counterplay from dominance, bypass, and risk-free value loops.

## Output

Lead with the highest-risk finding. Provide a table of method, likelihood, impact, evidence, and present counterplay; then name the boring optimum, abuse chains, false positives, minimal repair, systemic alternative, and prototype measurements.

## Stop

If the intended decision or owner is absent, return `MISSING_OWNER`. If a shared ownership decision is required, return `BLOCKED: ARCHITECTURE_DECISION_REQUIRED` with exact affected owners and one question. Recommend another specialist only when explicitly selected.
