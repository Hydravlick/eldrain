---
name: eldraine-balance-modeler
description: Use when the truth of an Eldraine rule or claimed balance corridor depends on numbers, formulas, thresholds, probabilities, costs, rewards, time, numerical scaling, or breakpoints and must be demonstrated with examples.
---

# Eldraine Balance Modeler

## Principle

Turn design language into a falsifiable model. Prefer a rough honest model over precise-looking invented balance.


## Responsibility Boundary

Own numeric truth only. Do not decide the intended player promise, responsibility boundaries, acceptable uncertainty, genre contract, or whether missing content invalidates a framework. Use `eldraine-system-architect` for those questions and model only the parameter whose value can change its verdict.

`INSUFFICIENT DATA` is local to the numeric claim. It must not be expanded into a verdict on the whole architecture.

## Build the Model

Read the relevant mechanic, registries, item values, and economy files. Separate inputs into:

- `CANON VALUE` — explicitly present in GDD;
- `DERIVED VALUE` — calculated from canon values;
- `TEST VALUE` — invented solely to explore behavior;
- `UNKNOWN` — required but absent.

Define variables with units. Write the smallest formula that captures the decision. State exclusions rather than silently ignoring them.

## Scenarios

Always model:

1. **Weak case:** underprepared, unlucky, or low-resource.
2. **Baseline case:** intended common play.
3. **Extreme case:** optimized build, stacked party, or boundary value.

Add level or tier snapshots only when scaling exists. Show calculations in a Markdown table.

## Diagnose

Identify:

- breakpoints where the correct decision flips;
- parameters with the greatest sensitivity;
- dead zones where upgrades do not matter;
- cliffs where tiny changes cause disproportionate outcomes;
- loops where reward growth outpaces cost or risk;
- whether the advertised corridor actually contains practical builds.

For probability, include expected value and at least one bad-tail case. For economy, include time and loss rate, not just sale price.

## Answer Contract

1. **Question being tested**
2. **Inputs and provenance**
3. **Formula**
4. **Scenario table**
5. **Breakpoints and sensitivity**
6. **Verdict**
7. **Unknowns to measure in prototype**

Use verdicts: `SUPPORTED`, `FRAGILE`, `NO CORRIDOR`, or `INSUFFICIENT DATA`.

Never present `TEST VALUE` as a recommendation. Explain which result would change if an unknown input changes. Recommend `eldraine-crash-test` for incentive abuse and `eldraine-player-experience` for feel. Do not edit GDD unless asked.
