---
name: eldraine-player-lens
description: Use when evaluating how relevant player profiles will behave around a defined Eldraine mechanic, quest, reward, loss, social feature, or progression contract, including engagement, optimization, frustration, and churn.
---

# Eldraine Player Lens

## Principle

Evaluate behavior, not demographic stereotypes. Ask what each relevant player seeks, learns, repeats, avoids, and values under extraction pressure.

## Local Vault Only

Work only with ordinary files inside the current Eldraine vault. Do not inspect or use Git state, history, diffs, branches, worktrees, staging, commits, remotes, pushes, or pull requests. If another workflow requests a Git step, skip it and continue with local file reads or edits. This changes no authorization boundary: read-only requests stay read-only, and files are edited only when the user explicitly asks.

## Responsibility Boundary

Own behavioural evidence: who adapts, optimizes, avoids, returns, or quits under a defined contract. Do not decide cross-system ownership, uncertainty allocation, genre compatibility, or the final architecture. When those are disputed, use `eldraine-system-architect` first and return the profile consequences of its stated alternatives.

Sparse authored content is not itself a player-behaviour verdict. Evaluate the behaviour taught by the grammar; label instance coverage separately.

Do not repair frustration by adding selection, reroll, replacement, or guaranteed synergy. When the authored fantasy places agency in adapting to an uncontrollable but viable person, evaluate whether the system supplies legibility and meaningful responses after the reveal.

## Profiles

Select only profiles materially affected by the feature:

- **Cautious survivor:** protects continuity and avoids irreversible loss.
- **Optimizer:** seeks best risk-adjusted efficiency and reproducible advantage.
- **PvP hunter:** seeks agency, pursuit, reads, and worthy opposition.
- **World explorer:** seeks discovery, lore, secrets, and environmental meaning.
- **Roster/build collector:** seeks ownership, combinations, growth, and identity.
- **Team player:** seeks roles, rescue, coordination, and shared stories.
- **Solo player:** seeks autonomy, stealth, escape routes, and fair information.
- **Genre newcomer:** needs legible stakes, recoverable learning, and trustworthy feedback.
- **Post-loss player:** is emotionally vulnerable to churn, revenge play, or over-caution.
- **Tired veteran:** needs novelty and low-friction decisions without trivialized mastery.

Add a situational profile only when the feature creates a distinct behavior not represented here.

## Evaluate

For each selected profile identify:

1. **Promise:** what makes them care.
2. **Likely behavior:** what they will actually do repeatedly.
3. **Reward value:** what counts as a satisfying payoff.
4. **Friction:** challenge that supports the fantasy.
5. **Frustration:** cost that feels arbitrary, unreadable, or disrespectful.
6. **Failure response:** retry, adapt, avoid, exploit, blame teammates, or quit.
7. **Return reason:** why they come back next session.

Separate intentional audience exclusion from accidental neglect. A hardcore game need not satisfy every profile equally.

## Answer Contract

Lead with the two or three profiles most decisive for the feature.

Use:

| Profile | Attraction | Actual behavior | Frustration/churn risk | Design adjustment |
|---|---|---|---|---|

Then provide:

- conflicts between profiles;
- behaviors the system rewards unintentionally;
- one change that helps multiple profiles without flattening them;
- one trade-off that should remain;
- playtest cohorts and questions.

Do not mechanically list all profiles. Do not average away the game's identity. Recommend `eldraine-crash-test` when behavior becomes exploitative and `eldraine-player-experience` when the issue is moment-to-moment readability. Do not edit GDD unless asked.
