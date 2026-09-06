---
status: active
system: life_closure
tags: [lifecycle, permanent_choice, civic_outcome]
related_files:
  - "[[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]]"
type: "system"
index_route: "owner"
index_group: "player_entities"
index_order: 200
index_summary: "Определяет состояния, разрешение и связи: Life Closure."
read_when: "Когда нужен контракт «Life Closure» и его границы с соседними владельцами."
---
# Life Closure

Пешка с завершённой жизненной аркой может навсегда остаться жить в городе. Когда условия выполнены, игрок сразу выбирает этот исход или окончательно сохраняет её полевую жизнь. Уход не приносит снаряжения, усилений или преимуществ следующему человеку.

## Responsibility

`LIFE_CLOSURE` owns closure eligibility, the closure arc instance, the immediate irreversible choice, and its `LifeClosureResolution`. It does **not** write a separate personal-history record, assign or reveal tags, recruit a replacement, transfer gear, grant discounts or services, or project roster membership.

Authored closure conditions may consume their named lifecycle, Quest, body or material facts; they do not decide closure themselves. [[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]] consumes the resulting terminal fact and projects the Pawn as `CLOSED_CIVIC` / `readiness=CLOSED`.

## Eligibility and one decision

The active generic path requires a living READY Pawn in the Hub, a formed life (`3` reserved lifetime manifestation slots and `3` revealed manifestations), and a resolved authored closure arc. Exact content patterns are authored elsewhere; a pattern is fixed to `PawnID` and cannot be rerolled by cancel, failure, Breakline, Recovery, disconnect, or death.

When eligibility becomes true, the system presents one irreversible decision immediately:

```text
CLOSURE_READY
  → CLOSE_CIVIC
  → RETURN_TO_FIELD_FOREVER
```

`CLOSE_CIVIC` creates `LifeClosureResolution=CLOSED_CIVIC`: the person lives in the city, leaves procedural deployment, and cannot be targeted as ordinary cargo, MIA, KIA, or recruitment content. `RETURN_TO_FIELD_FOREVER` preserves the field Pawn but forecloses the generic safe-closure path. It is not a parking state.

## Non-power invariant

Life Closure confers no tags, stats, gear, recipes, services, discounts, recruitment acceleration, candidate reroll, Continuity benefit, or inherited strength. It is a conclusion for a person, never a method for optimizing the roster.

Future fiction-specific closure branches require a separate lore-approved contract and are absent from this state machine.

## Handoff

The only emitted fact is immutable `LifeClosureResolution`. Lifecycle Roster projects it once. `KIA` forecloses an unresolved closure arc; no consumer may transform death into Closure.
