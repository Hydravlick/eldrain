---
name: eldraine-gear-progression
description: Use when evaluating Eldraine weapon, armor, battery, rarity, tier, Gate Check, loadout cost, replacement, or extraction progression where cheap valid gear, armor stacking, gear score, obsolete loot, or a dominant budget kit may collapse meaningful choice.
---

# Eldraine Gear Progression

## Principle

Evaluate complete loadouts over repeated raids, not isolated item stats. A healthy upgrade must change capability, reliability, or risk-adjusted opportunity without making cheaper gear either universally optimal or completely obsolete.

## Local Vault Only

Work only with ordinary files inside the current Eldraine vault. Do not inspect or use Git state, history, diffs, branches, worktrees, staging, commits, remotes, pushes, or pull requests. If another workflow requests a Git step, skip it and continue with local file reads or edits. This changes no authorization boundary: read-only requests stay read-only, and files are edited only when the user explicitly asks.

## Responsibility Boundary

Own equipment progression and risk-adjusted value of complete loadouts over repeated raids. Tags, hero-kits, roster rules, and maps enter this model only when they change equipment access, capability, loss, logistics, replacement, or dominance.

Do not judge the whole buildcraft architecture, player certainty budget, or tag-system quality by the number of authored builds. Use `eldraine-system-architect` first for cross-system buildcraft, genre compatibility, decision ownership, or scaling. When called by the architect, test only the delegated gear boundary.

`INSUFFICIENT DATA` applies to the specific equipment-dominance or numeric claim, not to structural findings outside it.

## Establish the Model

Read the relevant weapon, armor, battery, Gate Check, Resonance, weight, loot, and replacement-cost files. Label every input:

- `GDD FACT` — explicitly established;
- `DERIVED` — follows from established rules;
- `TEST ASSUMPTION` — invented to expose behavior;
- `UNKNOWN` — required but absent.

Separate these jobs before judging strength:

| Job | Question |
|---|---|
| Access | What permits entry or survival through Gate Check? |
| PvE capability | What enemies, shields, weakpoints, or contracts can it handle? |
| PvP capability | How does it kill, survive, disengage, or reveal position? |
| Logistics | What does weight, battery use, repair, and inventory space cost? |
| Extraction economy | What is lost on death and how many successful raids replace it? |
| Anomaly risk | What `ResonanceLoad` and `ResonancePulse` does it create? |

## Mandatory Loadout Test

Use this comparison when equipment progression or a dominant loadout is the question. It is not an automatic prerequisite for a cross-system architecture review.

Compare at least:

1. **Welfare:** cheapest replaceable complete kit.
2. **Balanced:** intended standard for the target content.
3. **Armor rat:** best affordable armor plus cheapest lethal weapon.
4. **Glass cannon:** strong weapon plus minimal legal protection.
5. **Specialist:** old or low-tier gear optimized for one niche.
6. **Squad carrier:** one member pays the progression cost while allies free-ride.
7. **Overgeared:** maximum practical kit near the Resonance ceiling.

For each loadout record:

| Field | Meaning |
|---|---|
| Entry cost | Replacement value at deployment |
| Loss exposure | Cost actually lost on death |
| Content coverage | Tasks and threats it can solve without a carry |
| Kill pressure | Repeatable ability to create or finish combat windows |
| Survival | Errors or encounters it can survive |
| Tempo | Shots, abilities, cooldown, repair, and battery burden |
| Mobility/carry | Movement cost and remaining loot capacity |
| Resonance | Load before combat and Pulse during execution |
| Recovery | Successful raids or time needed to replace it |

Do not collapse these fields into one gear score.

## Dominance Tests

Attack the model with these questions:

1. **Armor-rat test:** Does expensive armor plus the cheapest lethal weapon outperform the balanced kit after loss rate and replacement cost?
2. **White-weapon test:** Can cheap gear retain nearly all PvP lethality while avoiding the costs that justify weapon progression?
3. **Mandatory-tier test:** Does new content require a number rather than a new preparation or capability?
4. **Obsolescence test:** Does a higher tier erase every niche of the previous tier?
5. **Free-rider test:** Can a squad buy one advanced tool and let everyone else avoid progression cost?
6. **Avoidance test:** Can players farm advanced rewards while systematically skipping the threats that justify advanced gear?
7. **Rich-get-richer test:** Does expensive gear improve survival, loot rate, and replacement speed at the same time?
8. **Boring-optimum test:** Once solved, does the same kit answer most raids, weather, enemies, and contracts?

Flag a strategy as dominant when it wins on risk-adjusted reward across several common objectives, not merely when it is strong in one niche.

## Upgrade Value

Judge an upgrade through marginal value:

```text
Upgrade Value =
  added content coverage
  + added repeatability and tempo
  + added survival or extraction chance
  - added replacement exposure
  - added weight and resource burden
  - added Resonance risk
```

Do not require every upgrade to increase damage. Do require expensive weapons to provide meaningful repeatable opportunity that armor cannot substitute.

Healthy progression usually preserves all three:

- cheap gear can produce an upset through skill or preparation;
- advanced gear earns better consistency, tempo, or content coverage;
- expensive loadouts accept greater loss, logistics, or Resonance exposure.

## Verdict

| Verdict | Meaning |
|---|---|
| `HEALTHY` | Several loadouts have distinct jobs and no broad risk-adjusted winner. |
| `FRAGILE` | Choice exists, but one missing value or exploit may collapse it. |
| `DOMINATED` | One cheap, safe, or scalable loadout invalidates progression. |
| `INSUFFICIENT DATA` | Costs, loss rates, encounter needs, or replacement times are absent. |

## Answer Contract

Lead with the highest-risk dominant strategy. Then provide:

1. **Progression promise** — what upgrading is supposed to unlock.
2. **Loadout comparison** — mandatory loadouts in one table.
3. **Dominance findings** — method, likelihood, impact, and present counterplay.
4. **Player perspectives** — optimizer, cautious survivor, PvP hunter, solo, squad, and collector only when relevant.
5. **Boring optimum** — the repeated kit and behavior rational players learn.
6. **Healthy niches** — strong options that still pay meaningful costs.
7. **Minimal repair** — smallest rule change that restores choice.
8. **Systemic alternative** — only if the minimal repair preserves the root failure.
9. **Prototype measurements** — prices, loss rates, task completion, ammunition/battery use, and loadout frequency needed for numeric or empirical proof.

Do not fix a dominance problem by adding another universal score. Recommend `eldraine-balance-modeler` for numeric corridors, `eldraine-crash-test` for broader abuse chains, and `eldraine-player-experience` when the rule cannot be perceived or understood in play.
