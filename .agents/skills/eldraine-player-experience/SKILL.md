---
name: eldraine-player-experience
description: "Use when translating or evaluating an already bounded Eldraine feature as a lived sequence: onboarding, first-hour flow, combat feel, encounter pacing, readability, feedback, failure comprehension, or hub-to-raid flow."
---

# Eldraine Player Experience

## Principle

Describe the game from outside the system. Every important rule must become something the player can perceive, interpret, decide about, and remember.

## Local Vault Only

Work only with ordinary files inside the current Eldraine vault. Do not inspect or use Git state, history, diffs, branches, worktrees, staging, commits, remotes, pushes, or pull requests. If another workflow requests a Git step, skip it and continue with local file reads or edits. This changes no authorization boundary: read-only requests stay read-only, and files are edited only when the user explicitly asks.

## Responsibility Boundary

Own the chronological evidence of what the player perceives, believes, decides, commits, and learns in a bounded flow. Do not define cross-system ownership, the total certainty budget, the genre contract, or scaling invariants. When the question spans several system layers or asks whether the framework itself is sound, use `eldraine-system-architect` first and answer only its bounded experience question.

Do not convert an architectural uncertainty into a prototype checklist. Prototype questions here may measure perception, timing, feel, or comprehension only after the intended rule and decision are defined.

## Choose a Mode

- **First 15 minutes / first hour:** arrival, first promise, first confusion, first risk, first earned memory.
- **Encounter slice:** approach, detection, commitment, exchange, recovery, outcomes.
- **Combat feel:** anticipation, sound, animation commitment, impact, enemy reaction, recovery cadence.
- **Failure readability:** warning, causal signal, death or loss, lesson, next decision.
- **Hub-to-raid journey:** preparation, readiness judgment, deployment, extraction, aftermath.

Read the relevant mechanics and content. Do not invent feedback as if it already exists; mark additions as proposals.

## Experience Frame

For each beat capture:

1. **Perception:** what is seen, heard, felt, or noticed.
2. **Interpretation:** what the player is likely to believe.
3. **Decision:** meaningful options and information available.
4. **Commitment:** time, exposure, resource, or emotional stake.
5. **Feedback:** immediate response proving what happened.
6. **Consequence:** tactical and emotional result.

Flag beats with no decision, invisible causality, weak feedback, fake choice, excessive cognitive load, or no payoff.

## Answer Contract

Start with the intended emotional arc in one sentence. Then write a chronological slice using concrete seconds or minutes where useful.

After the slice provide:

- **Strong beats**
- **Experience gaps**
- **Misread risks:** what players may wrongly infer
- **Minimum feel pass:** smallest audio, visual, animation, camera, or timing additions
- **Three outcomes:** success, retreat, and failure when relevant
- **Prototype questions:** observations about perception, timing, feel, or comprehension to collect from playtests

Do not solve weak feel by adding UI alone. Do not confuse mechanical complexity with meaningful tension. Recommend `eldraine-player-lens` for audience differences and `eldraine-balance-modeler` for numerical tuning. Do not edit GDD unless asked.
