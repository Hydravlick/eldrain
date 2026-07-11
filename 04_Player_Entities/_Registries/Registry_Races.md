---
type: registry
status: active
registry_type: races
system: player_entities_registry
tags: [database, races, dataview]
related_files:
  - "[[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]]"
  - "[[04_Player_Entities/_Registries/Registry_Combos|Registry Combos]]"
---
# Реестр: Расы

> **MVP:** Зафиксированы Ёж, Крыса и Белка. Жаба и Ящерица сохраняются как каноническая карта расширения с атрибутами, векторами и биологической основой, но без готовых MVP-комбинаций.
>
> Биологическая основа не является отдельной расовой пассивкой. Все игровые `P/Q/E` создаются в конкретной ячейке `Race × Spec` по [[04_Player_Entities/MVP_3x3_Design_Contract|контракту матрицы 3×3]].

`Раса` здесь означает антропоморфную звериную телесную линию, а не классический фэнтезийный народ. В Элдрейне нет базовых людей, эльфов, орков или гномов. Все игровые расы сохраняют животный силуэт, физиологию и читаемые биологические свойства. Культура определяется конкретной диаспорой и миром происхождения, а не одним названием животного.

Стабильные поля каждой расы находятся только в YAML её страницы. Этот файл является семейным обзором и не дублирует данные сущностей.

## Статическая навигация

**MVP:** [[04_Player_Entities/Races/Hedgehog|Ёж]] · [[04_Player_Entities/Races/Rat|Крыса]] · [[04_Player_Entities/Races/Squirrel|Белка]].  
**Расширение:** [[04_Player_Entities/Races/Toad|Жаба]] · [[04_Player_Entities/Races/Lizard|Ящерица]].

Таблица ниже — необязательное Dataview-представление этих же YAML-записей. Внешний читатель открывает страницы рас по ссылкам выше.

```dataview
TABLE WITHOUT ID
  file.link AS "Раса",
  content_scope AS "Контур",
  base_vector AS "Вектор",
  join(weak_to, ", ") AS "Слабости",
  culture AS "Культура"
FROM "04_Player_Entities/Races"
WHERE type = "race"
SORT sort_order ASC
```
