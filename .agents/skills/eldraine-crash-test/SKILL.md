---
name: eldraine-crash-test
description: Use when attacking a defined Eldraine mechanic, build, economy loop, progression rule, reward, party interaction, or risk contract for exploits, dominant strategies, safe farming, degenerate play, or boring optimal behavior.
---

# Eldraine Crash Test

## Principle

Attack the incentive structure, not the prose. Find what rational players will repeatedly do when rewards, risk, coordination, and time pressure interact.


## Active Canon Language

Describe the accepted target state affirmatively: name the active entities, rules, scope, and consequences.

Historical context belongs outside active rule statements. When it helps explain provenance or a reference, label it as contextual material and return the adopted model in the canonical result.

## Responsibility Boundary

Own adversarial evidence against an explicit decision, cost, reward, invariant, or interface. Do not invent the intended cross-system contract, allocate uncertainty, or judge the architecture by content volume. If ownership, reveal timing, acceptable behaviour, or system boundaries are unresolved, report that dependency and use `eldraine-system-architect` first.

When called by the architect, attack only the supplied boundary or invariant. Do not replace the architecture review with the full default attack-surface checklist.

## Prepare

Read the mechanic and its direct dependencies. Record:

- intended player decision;
- cost, reward, failure state, and repeat rate;
- stated counters and limits;
- missing values or assumptions.

If the intended decision or owner is absent, label it as an architectural dependency instead of silently choosing one.

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

## Lifecycle and Concurrency Edge Cases

For background tasks, hub services, assignments, crafting, recovery, travel, or other multi-step processes, test the relevant cases explicitly:

- **Simultaneous events:** two triggers complete on the same tick or transition.
- **Cancellation mid-process:** the player cancels after cost, reservation, travel, or partial reward.
- **Invalid or lost target:** the target changes, disappears, dies, or stops qualifying during resolution.
- **Unavailable POI:** the destination is blocked, removed, occupied, or invalid for the current hub state.
- **Conflicting reservation:** two tasks reserve the same Pawn, item, slot, currency, or capacity.
- **Save/load:** persistence occurs before departure, during transit, during resolution, or after reward creation.
- **Offline time skip:** elapsed time completes several dependent tasks without intermediate player decisions.
- **Pawn unavailable:** death, injury, deployment, dismissal, or another assignment interrupts the contract.
- **Capacity and overflow:** output inventory, roster, queue, or destination capacity is full.
- **State transition:** raid start, hub phase change, account migration, or world-state change occurs mid-process.

For each case name the current rule, the abuse or deadlock, the exact expected resolution, and whether the player receives enough feedback to understand it.

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
- **Prototype tests:** concrete metrics or scenarios needed to verify an empirical concern after the intended contract is defined.

Do not fabricate numeric certainty. Recommend `eldraine-balance-modeler` when the verdict depends on uncalibrated values. Do not edit GDD unless asked.
