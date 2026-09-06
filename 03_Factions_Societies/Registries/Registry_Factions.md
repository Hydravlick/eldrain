---
status: active
system: factions_societies_registry
registry_type: factions
tags:
  - database
  - diplomacy
  - world_building
  - contracts
  - crafting
related_files:
  - "[[03_Factions_Societies/Faction_Address_System|Faction_Address_System]]"
  - "[[03_Factions_Societies/Lore/Civic_Ethos_Under_Lamps|Civic_Ethos_Under_Lamps]]"
  - "[[03_Factions_Societies/Lore/The_Circle_of_Interposition|The_Circle_of_Interposition]]"
related_mechanics:
  - "[[03_Factions_Societies/Pledge_Contracts|Pledge_Contracts]]"
  - "[[03_Factions_Societies/Reputation_Rules|Reputation_Rules]]"
  - "[[03_Factions_Societies/Quest_Engine|Quest_Engine]]"
  - "[[06_Economy_Loot/Barter_System|Barter_System]]"
type: registry
index_route: owner
index_group: factions_societies
index_order: 30
index_summary: "Хранит схему и записи: Реестр: городские Очаги и фракционные адреса."
read_when: "Когда нужен контракт «Реестр: городские Очаги и фракционные адреса» и его границы с соседними владельцами."
---
# Реестр: городские Очаги и фракционные адреса

Реестр хранит контракт идентичности и отношений; значения принадлежат страницам сущностей. Игровые интерфейсы перечислены в [[03_Factions_Societies/Registries/Registry_Faction_Interfaces]], правила участия — в [[03_Factions_Societies/Pledge_Contracts]].

Старые черновые фракции **Литейный Синдикат**, **Академия Эфира** и **Теневой Картель** не используются как основные канонические фракции.

- Крафт, исследования и распознавание свойств перешли в **Дома Пробы** и их Столы.
- Тяжёлый ремонт и городская инженерия перешли в **Артели Подпорки**.
- Оценка, спорная собственность и долги перешли в **Весовые Дома**.
- Серые услуги стали явлением **Ночных Поручителей**, а не единой мафией.

## Игровая модель

```text
1. Очаг      -> какое обещание города поддержано
2. Стол      -> какая экспертиза принимает предмет или проблему
3. Мастер    -> кто именно берёт это в руки
4. Адрес     -> чем предмет станет после сдачи
5. Последствие -> доверие, доступ, долг, конфликт или память
```

## Типы действий

Игровые изменения доверия и нарушения договора: [[03_Factions_Societies/Reputation_Rules]].

## Фракции

Канонические данные и отношения хранятся на страницах самих фракций. Этот реестр только собирает семейство в один обзор.

```dataview
TABLE WITHOUT ID
  file.link AS "Фракция",
  faction_role AS "Роль",
  promise AS "Обещание"
WHERE entity_kind = "faction"
SORT sort_order ASC
```

## Контракт отношений

Отношения хранятся в теле фракционной страницы как повторяемые inline Dataview-поля с причиной на той же строке:

```markdown
[rel_union:: common_storehouses] (первичный уход требует еды, тепла и базовых наборов)
```

Правила отношений:

- Допустимые типы: `conflict`, `hunt`, `monitor`, `spy`, `trade`, `union`.
- `target` содержит `faction_id`, а не заголовок, путь или отображаемое имя.
- `target: all` является явным системным указателем на все остальные фракции и допустим только для надфракционной либо скрытой силы.
- Направление и причина принадлежат странице-источнику. Обратная запись создаётся только тогда, когда у второй стороны действительно есть собственная формулировка отношения.
- Одна и та же связь не хранится одновременно в YAML страницы и в `Registry_Factions`.
- Неизвестный target, дублирующий `faction_id`, неизвестный тип и пустая причина должны быть видны как ошибка данных.


## Свойства фракционной сущности

```yaml
type: entity
entity_kind: faction
status: active
system: factions
faction_id: first_reception
display_name: Круг Первого Приёма
faction_role: major
sort_order: 10
promise: никто не остаётся один перед неизвестным состоянием
```

`faction_id` остаётся стабильным. Карта отношений читает `rel_*` на самой сущности: [[03_Factions_Societies/Views/Faction_Relationships]].
