---
type: mechanic
system: player_core
tags:
  - tags
  - attributes
  - logic
related_files:
  - "[[Character_Specification]]"
  - "[[Skills_Archetypes]]"
---

# Система Тегов: ДНК Персонажа

## 1. Философия
Тег — это минимальная единица смысла. В игре нет "древ навыков", есть набор тегов, определяющий возможности сущности.

## 2. Категории Тегов
* **Source Tags:** Раса (`[Race: Lazur]`), Специализация (`[Class: Duelist]`).
* **Perks (Перки):** Бонусы (`[Master: Blade]`, `[Trait: Night_Vision]`).
* **Flaws (Изъяны):** Штрафы (`[Flaw: Limp]` - хромота, `[Flaw: Asthma]` - штраф к стамине).
* **State Tags:** Временные состояния (`[Status: Burning]`, `[Status: Hidden]`).

## 3. Влияние на Атрибуты
Теги являются модификаторами для базовых атрибутов (см. [[Character_Specification]]):
* `[Strong]` -> +STR.
* `[Agile]` -> +AGI.
* `[Tough]` -> +CON/END.

## 4. Эволюция Тегов (Tag Synergy)
Если персонаж обладает двумя синергирующими тегами, они могут **слиться** в один "Золотой Тег" (Golden Tag), освобождая слот памяти и давая мощный эффект.
* *Пример:* `[Effect: Burn]` + `[Master: Fire]` = Эволюция в `[Pyromancer]` (Иммунитет к огню + Усиление урона огнем).