# Eldraine Skill Contracts and Vault Curator Design

**Date:** 2026-08-11
**Status:** approved in comparative skill audit and authorized for local implementation

## Goal

Make Eldraine mechanics readable and implementable without flattening intentional atmosphere. Extend the existing specialist skills with precise rule, formula, edge-case, player-experience, lore-delivery, and narrative-impact contracts. Add one project-local `eldraine-vault-curator` for owner-first prose audits and safe, explicitly approved rewrites.

## Boundaries

- Do not install upstream skill repositories.
- Do not create a second GDD, world bible, or authority tree.
- Do not edit active canon as part of skill installation.
- Keep every existing specialist's responsibility boundary intact.
- Default prose work to detection and findings; rewriting requires explicit approval.
- Treat Russian Eldraine prose as the target corpus. Do not translate English banned-word lists mechanically.

## Contract Additions

### System specification

A bounded executable mechanic must expose its player promise, player loop, rule state machine, interfaces, edge cases, and validation hypothesis. Formal rules use `PRECONDITION -> TRIGGER -> RESOLUTION -> POSTCONDITION`. Dependency review flags orphan rules, cycles, deep chains, and bottlenecks.

### Formula specification

Each formula names its owner and evidence status, expression, variables, units, valid ranges, normal output, extreme behavior, worked examples, tuning knobs, dependencies, and breakpoints.

### Player experience

Each beat records perception, interpretation, decision, commitment, feedback, and consequence. Feel review separately checks responsiveness, impact, rhythm, clarity, and payoff. Prototype questions measure observable comprehension and timing rather than imagined retention.

### Lore and narrative

Speaking characters receive voice pillars. Lore delivery distinguishes `SURFACE`, `ENGAGED`, and `DEEP`; causal rules needed for play remain on `SURFACE`. Narrative changes map story beat, world-state change, gameplay surface, observation point, player interpretation, feeling, visibility delay, and canonical owner.

### Vault curation

The curator audits authority, lifecycle, readability, and prose health. It reports exact evidence and the smallest safe repair. A deterministic detector emits candidates without rewriting. A rewrite validator preserves frontmatter, headings, code, tables, link targets, inline code, rule IDs, numbers, and formulas.

## Verification

- Contract tests assert the required sections exist in the affected skills.
- Curator tool tests cover protected Markdown regions and Russian formulaic prose.
- Skill metadata receives structural validation.
- Existing project tests and `tools/vault_guard.py` run after implementation; unrelated pre-existing failures are reported separately.

