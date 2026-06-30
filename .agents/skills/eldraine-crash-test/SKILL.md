---
name: eldraine-crash-test
description: Use when reviewing an Eldraine mechanic, build, economy loop, progression rule, reward, party interaction, or risk system for exploits, dominant strategies, safe farming, degenerate play, or boring optimal behavior.
---

# Eldraine Crash Test

## Principle

Attack the incentive structure, not the prose. Find what rational players will repeatedly do when rewards, risk, coordination, and time pressure interact.

## Local Vault Only

Work only with ordinary files inside the current Eldraine vault. Do not inspect or use Git state, history, diffs, branches, worktrees, staging, commits, remotes, pushes, or pull requests. If another workflow requests a Git step, skip it and continue with local file reads or edits. This changes no authorization boundary: read-only requests stay read-only, and files are edited only when the user explicitly asks.

## Prepare

Read the mechanic and its direct dependencies. Record:

- intended player decision;
- cost, reward, failure state, and repeat rate;
- stated counters and limits;
- missing values or assumptions.

Mark claims as `GDD FACT`, `INFERENCE`, or `TEST ASSUMPTION`.

## Attack Surfaces

Test at least the relevant surfaces:

1. **Combat:** invulnerability, permanent control, range safety, animation or resource bypass.
2. **Economy:** infinite value loops, laundering, risk-free profit, alt-account transfer, price manipulation.
3. **Risk:** extracting value without accepting the intended loss condition.
4. **Progression:** snowballing, catch-up abuse, optimal stagnation, disposable-character farming.
5. **Party:** multiplicative stacking, role cycling, sacrifice abuse, information advantage.
6. **Population:** what happens when many players copy the strategy.
7. **Boredom:** whether optimal play removes decisions, movement, tension, or variety.

Use adversarial personas when useful: optimizer, coordinated squad, solo rat, wealthy veteran, fresh account, griefer.

## Distinguish Strength from Exploit

A strategy is not broken merely because it is strong. Flag it when one or more apply:

- it has no meaningful counter within the intended rules;
- its reward dominates alternatives after risk and time are included;
- it bypasses the fantasy or cost the system exists to create;
- broad adoption collapses variety or economy;
- counterplay requires foreknowledge unavailable to the victim.

## Answer Contract

Lead with the highest-risk finding. Use a table:

| Finding | Method | Likelihood | Impact | Evidence | Counterplay today |
|---|---|---:|---:|---|---|

Then provide:

- **Boring optimum:** the safest repetitive behavior the system teaches.
- **Abuse chains:** combinations of otherwise valid systems.
- **False positives:** powerful strategies that still have healthy counterplay.
- **Fix options:** one surgical constraint, one systemic fix, and the cost of each.
- **Prototype tests:** concrete metrics or scenarios needed to verify the concern.

Do not fabricate numeric certainty. Recommend `eldraine-balance-modeler` when the verdict depends on uncalibrated values. Do not edit GDD unless asked.
