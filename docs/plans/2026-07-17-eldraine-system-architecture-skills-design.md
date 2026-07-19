# Eldraine System Architecture Skills Design

**Date:** 2026-07-17  
**Status:** Approved by the author

## Problem

The current Eldraine skills are strong local reviewers, but no skill owns the cross-system contract. In baseline reviews, architecture questions drifted toward sparse content, unknown numbers, mandatory loadout comparisons, and prototype requests. Those are useful downstream checks, but they cannot decide whether the framework itself preserves extraction-player competence, distributes uncertainty fairly, or remains coherent when content scales.

## Design Decision

Create `eldraine-system-architect` as the only owner of cross-system architecture. Adapt every existing Eldraine skill so it owns one local evidence domain and hands cross-system questions to the architect. Do not copy the architect's certainty ledger, responsibility map, genre contract, or invariants into local skills.

## Responsibility Map

| Skill | Owns | Does not own | Handoff |
|---|---|---|---|
| `eldraine-system-architect` | Cross-system promise, responsibility boundaries, uncertainty allocation, genre contract, lifecycle of decisions, scaling invariants, interface failures | Detailed numbers, complete loadout balance, moment-to-moment presentation, deep exploit enumeration, lore authority, document authoring | Delegates one bounded question to the matching specialist |
| `eldraine-player-experience` | Perception → interpretation → decision → feedback in a bounded lived sequence | Cross-system ownership or total uncertainty budget | Returns readability and failure-comprehension evidence |
| `eldraine-player-lens` | Behavior, motivation, churn, adaptation, optimization by relevant player profiles | Final architecture or generic audience averaging | Returns behavioral consequences of a defined contract |
| `eldraine-crash-test` | Incentive abuse, dominant strategies, safe farming, boring optima, population effects | Defining the intended contract or judging content completeness | Attacks explicit invariants and interfaces supplied by the architect |
| `eldraine-gear-progression` | Equipment progression and repeated complete-loadout value | Whole buildcraft architecture or tag-registry completeness | Tests the equipment boundary and progression promise |
| `eldraine-balance-modeler` | Numeric corridors, formulas, thresholds, probabilities and sensitivity | Normative architecture and content volume | Tests only claims whose truth depends on values |
| `eldraine-location-designer` | Spatial decisions, route grammar, procedural production, local map readability | Total game-wide uncertainty allocation | Reports the map's uncertainty contribution and spatial guarantees |
| `eldraine-lorekeeper` | Canon authority, fiction-to-mechanics causality and retcon cost | System viability, balance or audience fit | Reports canon constraints to the architect |
| `eldraine-narrative-impact` | Downstream story and state dependencies | Cross-system gameplay architecture | Reports narrative blast radius of an approved change |
| `eldraine-gdd-author` | Canonical placement and integration of approved decisions | Resolving disputed architecture | Writes only after the architect or author resolves the contract |

## Architectural Workflow

1. Classify evidence as author constraint, architecture fact, structural inference, empirical unknown, or content gap.
2. Map each layer's owner, visibility, decision moment, duration, reversibility, loss, and downstream effects.
3. Build a qualitative certainty ledger across world, encounter, self, rules, and outcome. Evaluate when uncertainty is stacked, not merely how many unknowns exist.
4. State the extraction genre contract as competence guarantees, not competitor imitation.
5. Define content-independent invariants and attack cross-layer interfaces under scale.
6. Separate architecture contradictions from content gaps and numerical unknowns.
7. Delegate bounded local questions. A specialist may not replace the architectural verdict with its own default output contract.
8. Request a prototype only for an empirical unknown that remains after the normative design and state transitions are defined.

## Required Behaviour Change

- Sparse registries must not lower an architecture verdict.
- `INSUFFICIENT DATA` may apply to a numeric or balance claim, not to the whole architecture when structural reasoning is possible.
- A request for architecture must not be converted into a content-authoring checklist or a prototype plan.
- High procedural-map uncertainty does not require every other layer to be deterministic. It requires bounded, attributable uncertainty plus reliable footholds for control, planning, adaptation, and failure learning.
- Local skills must not reproduce the architect's method. They return evidence inside their domain.

## Test Strategy

Reuse the baseline buildcraft scenarios under three pressures: missing authored content, unknown balance values, and the temptation to defer to prototyping. Success requires the agent to produce a responsibility map, certainty ledger, content-independent invariants, cross-layer abuse chains, and architecture-first repair direction without scoring down sparse registries.

Add two counterexamples:

1. A purely numeric battery threshold must route directly to `eldraine-balance-modeler`, not the architect.
2. A bounded combat-readability sequence must route directly to `eldraine-player-experience`, with no unnecessary architecture ceremony.
