---
status: active
system: project_management
date: 2026-07-23
tags:
  - refactor
  - unresolved
  - decision_registry
related_files:
  - "[[09_Project_Management/Architecture_MVP]]"
type: "project_management"
---
# Открытые продуктовые решения

> Реестр фиксирует источники, точные конкурирующие утверждения и затронутых владельцев. Он не выбирает вариант, не создаёт runtime-правило и не заменяет профильную документацию.

## Правило ведения

- Добавлять только фактически обнаруженное расхождение между источниками либо между источником и активным каноном.
- Указывать точные файлы и заголовки, а не пересказ предположения.
- Не переносить спорную норму в active canonical page, пока автор не примет решение.
- После авторского решения переносить его через профильного owner; запись получает статус `resolved / pending migration` и сохраняет историю выбора.

## Открытые решения

| ID | Статус | Конкурирующие утверждения | Затронутые owners | Требуется решение |
|---|---|---|---|---|
| `UR-001` | `unresolved derived decision` | First Return раскрывается только после самостоятельного обычного выхода через `NormalThreshold`; альтернативная T4-гипотеза допускала `DAWN`. | [[04_Player_Entities/Lifecycle_Roster]], [[04_Player_Entities/Tags_System]], [[04_Player_Entities/Lifecycle_Resolver]] | Должен ли Dawn раскрывать заранее назначенный First Return / TagID, или Dawn считается только return outcome без раскрытия? |
| `UR-002` | `unresolved lifecycle conflict` | Одна retired personal-lifecycle proposal не запускала offline pending timer до валидного `BreachCommitted`; другая retired raid proposal делала `RecoveryCase.expires_at` абсолютным с момента создания Case, включая `PENDING/SEARCHING/BOUND/IN_RECOVERY`. | [[04_Player_Entities/Last_Thread_Recovery]], [[04_Player_Entities/Lifecycle_Roster]], [[04_Player_Entities/Recovery_Lifecycle]], [[08_World_Generation/Generation/Raid_Approach_and_Entry]] | Истекает ли право Recovery, пока система ищет публичный сектор, либо смертельный clock начинается только после появления физической Recovery Presence? |
| `UR-003` | `unresolved closure trigger` | Одна гипотеза разрешала closure arc только через обычный `NormalThreshold`; другая допускала `DAWN_RETURN`. | [[04_Player_Entities/Life_Closure]], [[04_Player_Entities/Lifecycle_Resolver]], [[04_Player_Entities/Tags_System]] | Может ли Dawn завершать authored closure arc, либо Closure требует отдельного обычного возвращения? |

## Решения вне реестра

`Dawn full return` уже живёт у [[04_Player_Entities/Lifecycle_Resolver|Lifecycle Resolver]] и [[06_Economy_Loot/Return_Manifest_Contract|Return Manifest Contract]]. Это не открытое расхождение и не должно добавляться в данный реестр.

Принятый исход Recovery на Dawn находится у [[04_Player_Entities/Recovery_Lifecycle]]. В `UR-002` остаётся открытым только начало и течение Case clock.
