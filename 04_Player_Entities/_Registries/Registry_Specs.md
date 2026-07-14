---
type: registry
status: active
registry_type: specs
system: player_entities_registry
tags: [database, specs, practices, dataview]
related_files:
  - "[[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]]"
  - "[[04_Player_Entities/_Registries/Registry_Combos|Registry Combos]]"
---
# Реестр: Практики / специализации

> **MVP:** Зафиксированы Авангард, Технократ и Странник. Страж и Догмат остаются направлениями расширения с профессиональной методологией, но без готовых MVP-комбинаций.
>
> Практика / специализация задаёт методологию, а не готовые `Q/E` и не обязательную партийную роль. `Race × Spec` образует архетип, а экипировка, теги и условия операции создают итоговый профиль вылазки. Все игровые `P/Q/E` принадлежат конкретной ячейке `Race × Spec`.

Исторические ID `assault`, `support`, `scout` остаются стабильными ключами схемы. Они не являются игроко-видимыми названиями и не описывают партийные роли.

Стабильные поля каждой практики находятся только в YAML её страницы. Этот файл является семейным обзором и не дублирует данные сущностей.

## Статическая навигация

**MVP:** [[04_Player_Entities/Specs/Vanguard|Авангард]] · [[04_Player_Entities/Specs/Technocrat|Технократ]] · [[04_Player_Entities/Specs/Drifter|Странник]].  
**Расширение:** [[04_Player_Entities/Specs/Guardian|Страж]] · [[04_Player_Entities/Specs/Dogmat|Догмат]].

Таблица ниже — необязательное Dataview-представление этих же YAML-записей. Внешний читатель открывает страницы практик по ссылкам выше.

```dataview
TABLE WITHOUT ID
  file.link AS "Практика",
  content_scope AS "Контур"
FROM "04_Player_Entities/Specs"
WHERE type = "spec"
SORT sort_order ASC
```
