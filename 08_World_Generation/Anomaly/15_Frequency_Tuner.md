---
type: player_facing_projection
status: active
system: service_region_ui
tags:
  - region
  - ping
  - service
  - ui
related_files:
  - "[[08_World_Generation/Generation/19_Raid_Approach_and_Entry|Raid Approach and Entry]]"
---
# Настройка частоты

## Responsibility

Тюнер — только player-facing представление региона, качества соединения и доступности сервиса. Он не выбирает конкретный raid target, не открывает повторный вход и не владеет matchmaking-решением.

Игрок видит:

- регион обслуживания;
- измеренную задержку и стабильность соединения;
- предупреждение о качестве сети;
- общую доступность сервиса для начала нового Approach.

Список именованных серверов не показывается. После выбора региона поток передаётся [[08_World_Generation/Generation/19_Raid_Approach_and_Entry|Raid Approach and Entry]], который создаёт target-independent предложение и отдельно управляет раскрытием цели.

## Boundaries

- смерть не выдаёт идентификатор для возвращения в ту же сессию;
- reconnect может восстановить управление только уже существующей Presence по владельцу ingress/session continuity;
- новый Approach никогда не является способом подобрать собственное тело из прежнего SessionID;
- Recovery использует обычный публичный target search по своему lifecycle-контракту, а не этот UI.
