---
type: spec
status: active
system: player_entities
id: scout
display_name: Странник
english_name: The Drifter
aliases: [Странник, The Drifter]
sort_order: 40
content_scope: mvp
base_vector: shadow
weak_to: [hazard, ballistics, detection]
touch_TRQ: 0
touch_GRP: 4
touch_LYR: -1
touch_GLW: 2
touch_SNS: 1
tags: [spec, practice, player_entity]
---
# Странник (The Drifter)

> Маршрут, изменение позиции, сбор информации и выбор момента.

## Системные модификаторы

[substats:: loot_speed +12, bolt_wind_speed +8, weapon_swap_speed +8, ambush_resist +6]
[condition_bonus:: from_cover: drift_control +8]
[tradeoff:: brace -5]

## Методология

Знание географии, ловкость и доступ в закрытые зоны. Это те, кто живёт между слоями города.

## Примеры профессий

- **Фонарщик (Lamplighter):** прыгает по крышам, зажигает свет, ослабляет тьму и слепит вспышками.
- **Курьер Теневого Рынка (Runner):** быстрее переносит груз, вскрывает замки и замечает ловушки.
