---
type: mechanic
system: server_clock
tags: [timer, wipe, difficulty_tiers]
---

# Жизненный Цикл Сервера (Server Lifecycle)

## 1. Структура Сессии (6-Hour Cycle)
Один серверный инстанс живет ровно **6 часов**. Это жесткая константа. Внутри этого времени мир проходит 3 фазы эскалации (Tier Shift).
Игрок может зайти и выйти в любой момент, пока инстанс жив.

## 2. Фазы Мира (The Timeline)

| Тайминг (Время сервера) | Фаза (Tier) | Состояние Лута | Сложность Мобво |
| :--- | :--- | :--- | :--- |
| **00:00 - 02:00** | **Tier 1 (Stabilization)** | Базовый (Low Value) | Scavengers / Rats |
| **02:00 - 04:00** | **Tier 2 (Escalation)** | +Quality / +Quantity | Mercenaries / Mutants |
| **04:00 - 06:00** | **Tier 3 (Entropy Storm)** | **High Value / Artifacts** | Bosses / Horrors |
| **06:00** | **THE WIPE (Коллапс)** | Полное уничтожение | Смерть всего живого |

## 3. Коллапс (Wipe)
В 06:00 сервер закрывается. Все игроки, не успевшие эвакуироваться, считаются погибшими (MIA). Инстанс удаляется.