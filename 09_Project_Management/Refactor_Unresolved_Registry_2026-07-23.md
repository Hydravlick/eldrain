---
type: unresolved_registry
status: active
system: project_management
date: 2026-07-23
tags:
  - refactor
  - unresolved
  - decision_registry
related_files:
  - "[[09_Project_Management/Canonical_Refactor_Migration_Map_2026-07-23|Migration map]]"
  - "[[BUILDCRAFT_ARCHITECTURE_SPEC|Buildcraft source proposal]]"
  - "[[T4_APEX_ENDGAME_LOOP_AND_PRODUCT_MODEL_PROPOSAL|T4 Apex source proposal]]"
---
# Реестр неразрешённых расхождений рефактора

> Реестр фиксирует источники, точные конкурирующие утверждения и затронутых владельцев. Он не выбирает вариант, не создаёт runtime-правило и не заменяет профильную документацию.

## Правило ведения

- Добавлять только фактически обнаруженное расхождение между источниками либо между источником и активным каноном.
- Указывать точные файлы и заголовки, а не пересказ предположения.
- Не переносить спорную норму в active canonical page, пока автор не примет решение.
- После авторского решения переносить его через профильного owner; запись получает статус `resolved / pending migration` и сохраняет историю выбора.

## Открытые решения

| ID | Статус | Конкурирующие утверждения | Затронутые owners | Требуется решение |
|---|---|---|---|---|
| `UR-001` | `unresolved derived decision` | Buildcraft §5.3: First Return раскрывается только после самостоятельного обычного выхода через `NormalThreshold`; T4 Apex §«Смысл за пределами добычи»: `FIRST_FULL_RETURN_COMPLETED` раскрывается через `NORMAL_THRESHOLD` **или** `DAWN`. | Player lifecycle, Tags, Trait Development, Chronicle, player-facing return flow | Должен ли Dawn раскрывать заранее назначенный First Return / TagID, или Dawn считается только return outcome без раскрытия? |
| `UR-002` | `unresolved lifecycle conflict` | Buildcraft §10.2/§10.5: offline pending timer отсутствует, а активный Recovery clock начинается после валидного `BreachCommitted`; Raid §15: `RecoveryCase.expires_at` абсолютен с момента создания Case, действует в `PENDING/SEARCHING/BOUND/IN_RECOVERY` и не паузится. | Last Thread, Lifecycle Roster, Recovery Lifecycle, Raid ingress, UI projection | Истекает ли право Recovery, пока система ищет публичный сектор, либо смертельный clock начинается только после появления физической Recovery Presence? |
| `UR-003` | `unresolved closure trigger` | Buildcraft §11: closure arc разрешается через обычный `NormalThreshold`; T4 Apex §«Смысл за пределами добычи»: authored `LifeClosure` может принять `DAWN_RETURN`. | Life Closure, Pawn lifecycle, Tags, Chronicle, Dawn settlement | Может ли Dawn завершать authored closure arc, либо Closure требует отдельного обычного возвращения? |

## Решения вне реестра

`Dawn full return` имеет статус `APPROVED / PENDING_MIGRATION` в [[09_Project_Management/Canonical_Refactor_Migration_Map_2026-07-23|migration map]]. Это не открытое расхождение и не должно добавляться в данный реестр.

Recovery, которая имеет живую неистёкшую Presence на Dawn, разрешается как `RECOVERED` без cargo, manifest и стандартной награды; KIA, lethal collapse и истечение Case имеют приоритет. Это принятое правило Raid/T4, а не право враждебного игрока или отдельный вариант Buildcraft. Открытым в `UR-002` остаётся только начало и течение самого Case clock.
