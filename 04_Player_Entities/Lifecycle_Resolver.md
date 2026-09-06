---
status: active
system: lifecycle_resolution
tags:
  - lifecycle
  - lethal_disposition
  - dawn
  - permadeath
related_files:
  - "[[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]]"
  - "[[04_Player_Entities/Last_Thread_Recovery|Last Thread Recovery]]"
  - "[[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]]"
  - "[[06_Economy_Loot/Return_Manifest_Contract|Return Manifest Contract]]"
  - "[[08_World_Generation/Generation/Server_Lifecycle|Server Lifecycle]]"
  - "[[08_World_Generation/Registries/Registry_Raid_Interfaces|Raid Interfaces]]"
type: system
index_route: owner
index_group: player_entities
index_order: 200
index_summary: "Определяет состояния, разрешение и связи: Lifecycle Resolver."
read_when: Когда нужен контракт «Lifecycle Resolver» и его границы с соседними владельцами.
---
# Lifecycle Resolver

> Единственный владелец личного lifecycle-решения. Мир и бой поставляют факты; другой игрок не получает права записать чужой terminal state.

## Responsibility

`LIFECYCLE_RESOLVER` владеет:

- классификацией `LethalEvent` в один immutable `LethalDisposition`;
- личным `DawnSettlementDecision` для STANDARD Presence;
- precedence между уже committed world/lifecycle facts.

Он не владеет боевым уроном, source custody, RecoveryCase, Recovery clock/result, roster projection, ReturnManifest, Seal/Dawn clock, First Return tag reveal или Life Closure.

## Lethal disposition

```yaml
LethalDisposition:
  lethal_event_id: LethalEventID
  pawn_id: PawnID
  outcome: FIELD_RECOVERABLE | TERMINAL_KIA | TERMINAL_LOST_CLOSED
  cause_ref: WorldResolutionRef
```

Combat, attacker, Finisher, corpse interaction and UI may publish evidence but cannot choose `outcome`. Exactly one disposition wins under the server's ordered world facts.

- `FIELD_RECOVERABLE` is the only input that permits [[04_Player_Entities/Last_Thread_Recovery|Last Thread]] to attempt an intercept.
- `TERMINAL_KIA` and `TERMINAL_LOST_CLOSED` bypass Last Thread and are projected by the roster without reinterpretation.

## STANDARD Dawn decision

For each STANDARD Presence at the committed Dawn barrier, the resolver consumes the authored Apex predicate, lethal precedence and, for a physical item return, a durable prepared manifest reference. It writes one immutable `DawnSettlementDecision`.

The decision belongs to the Presence, not to a winner slot, another player or `APEX_DIRECTOR`. [[06_Economy_Loot/Return_Manifest_Contract|Return Manifest]] only projects physical custody after `STANDARD_RETURN`; it does not decide survival.

Recovery Presence is excluded. Its final outcome belongs to [[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]].

## Explicit unresolved boundaries

- `UR-001` remains unresolved: this owner does not decide whether STANDARD Dawn reveals a preassigned First Return.
- `UR-003` remains unresolved: this owner does not decide whether Dawn completes Life Closure.

Neither branch may be inferred from `DawnSettlementDecision`.

## Handoffs

- [[08_World_Generation/Generation/Server_Lifecycle|Server Lifecycle]] supplies ordered barriers, never personal outcomes.
- [[04_Player_Entities/Last_Thread_Recovery|Last Thread Recovery]] consumes only `FIELD_RECOVERABLE`.
- [[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]] projects supplied terminal outcomes and cannot reclassify them.
- [[04_Player_Entities/Recovery_Lifecycle|Recovery Lifecycle]] may consume `cause_ref` for its own terminal record but remains its sole Recovery-result owner.

## Объяснение личного исхода

После потери игрок получает читаемую реконструкцию `предупреждение → обязательство → причина → следующий контрход`, а не только надпись KIA и таблицу урона. Экран объясняет уже принятое решение resolver и доступный следующий шаг; он не меняет судьбу человека.
