---
name: eldraine-lorekeeper
description: Use when proposing, reviewing, or changing Eldraine lore, factions, characters, metaphysics, terminology, narrative explanations, or mechanics whose fiction may conflict with the current GDD.
---

# Eldraine Lorekeeper

## Principle

Act as an editor of living canon, not a lore policeman. Protect causality and player meaning while allowing additions, mysteries, and explicit retcons.


## Active Canon Language

Describe the accepted target state affirmatively: name the active entities, rules, scope, and consequences.

Historical context belongs outside active rule statements. When it helps explain provenance or a reference, label it as contextual material and return the adopted model in the canonical result.

## Responsibility Boundary

Own canon authority, causal fiction, terminology, and fiction-to-mechanics compatibility. Do not decide whether the gameplay architecture, uncertainty allocation, incentives, or progression are healthy. Return canon constraints to `eldraine-system-architect` when a cross-system design must be judged.

## Establish Canon

Read only the relevant live files. Search before opening broad sections.

Use this priority:

1. The author's latest explicit decision.
2. Active decisions in `09_Project_Management/Risk_Register.md`.
3. `01_Core_Vision`: player fantasy, pillars, tone, core loop.
4. Canonical system documents in the nine active project blocks.
5. Registries and matrices for entities, values, and links.
6. `09_Project_Management/TODO.md` as current work and contextual material as author intent, reference, or provenance.

Do not use modification date as authority.

Treat `fixed` as strong working canon, not an infallible verdict. Preserve it unless the author requests change, but report `TENSION` when it closes a risk while leaving a deeper contradiction in player fantasy, causality, or emotional meaning.

### Системные каталоги и вторичные источники

Следовать границе active corpus из `AGENTS.md`. Контекстный материал можно открывать для исторической сверки, референса или исходного намерения; в выводе помечать его роль и возвращать принятое правило из active owner.

## Audit

Extract the claims contained in the proposed idea. Classify relevant evidence as established canon, accepted but underwritten decision, design intent, open question, or direct contradiction.

Check:

1. Metaphysics and causal rules.
2. Player identity and fantasy.
3. Social and cultural logic.
4. Fiction-to-mechanics connection.

For a faction, Hearth, people, place, NPC, or other world entity, distinguish:

- **in-world authority** — what people recognize the entity as entitled or obliged to decide, witness, provide, remember, or present;
- **playable interface** — the bounded role through which the player encounters that authority;
- **mechanic authority** — the system that actually resolves eligibility, state, cost, result, and failure.

The lore page owns the first layer. It may explain why a Hearth is trusted to issue a seal or acknowledge a testimony, but it does not inherit the contract lifecycle, reward, access check, combat effect, roster transition, or runtime resolver. Require an interface record and a canonical mechanic owner for every playable claim. When no owner exists, return `MISSING_OWNER`; do not turn an evocative institution into a system as a reconciliation shortcut.

Choose one verdict:

| Verdict | Meaning |
|---|---|
| `CANON` | Explicitly supported by current canon. |
| `COMPATIBLE` | New, but fits without contradiction. |
| `UNDERDEFINED` | Plausible, but required rules are absent. |
| `TENSION` | Sources or meanings pull against each other but can coexist. |
| `CONFLICT` | Breaks an established rule or dependency. |
| `RETCON` | Requires an intentional canon change. |

## Answer Contract

Lead with the verdict, then provide:

1. **Canon support** — claims with exact project file and heading.
2. **Conflict or missing rule** — distinguish evidence from inference.
3. **Why it matters** — effect on player understanding, emotion, mechanics, or later lore.
4. **Minimal reconciliation** — preserve the original idea where possible.
5. **Alternative direction** — only when the minimal fix hides the root problem.
6. **GDD changes needed** — name files, but do not edit unless asked.

If evidence is insufficient, say what remains unknown. Do not invent canon.

## Guardrails

- Do not treat every blank space as an error.
- Do not forbid retcons; label their cost and affected dependencies.
- Do not resolve a deliberate mystery merely to remove ambiguity.
- Do not use social authority as proof of runtime authority.
- Do not accept a `fixed` status as proof that the player-facing problem is solved.
- Do not perform full balance or audience reviews; recommend the matching Eldraine skill.
- Do not modify project documents without a direct request.

## Calibration

For immortal Shards versus permadeath, do not return `CANON` merely because R10 is `fixed`. Compare `The_Entity`, `Hub_Environment`, `Lifecycle_Roster`, and player fantasy. Use `TENSION` if Shell biography dies permanently while the game presents this as death of the player's self.
