---
type: spec
status: active
system: player_entities
id: specialist
display_name: Догмат
english_name: The Scholar
aliases: [Догмат, The Scholar]
sort_order: 50
content_scope: post_mvp
base_vector: aether
weak_to: [shadow, tech, ballistics]
touch_TRQ: 0
touch_GRP: 1
touch_LYR: -1
touch_GLW: 5
touch_SNS: 1
tags: [spec, practice, player_entity]
---
# Догмат (The Scholar)

> Эфирный канал, работа с артефактами и осознанный телесный долг без батареи.

## Системные модификаторы

[substats:: output_power +15, reality_burn_power +12, heat_sink +6]
[condition_bonus:: while_channeling: weakspot_read +8]

## Методология

Догматы — учёные-маги, изучающие батарейный импульс как воспроизводимый телесный процесс. Каждая их активная способность имеет кантрип, малую версию без батареи. Все такие применения делят общий телесный долг: первый импульс создаёт `Strained`, повтор до лечения оставляет постоянный Шрам, дальнейшая перегрузка грозит `Broken`. Другие специализации могут получить лишь отдельный ситуативный кантрип через конкретную комбинацию. Полная мощность, дальность и повторяемость по-прежнему требуют источник.

## Примеры профессий

- **Архивариус (Archivist):** читает заклинания из книг с каст-таймом и опознаёт артефакты на месте.
- **Детектив (Investigator):** видит эхо прошедших событий и подсвечивает уязвимости врагов.
