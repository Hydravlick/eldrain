---
type: mechanic
system: player_core
tags:
  - tags
  - attributes
  - logic
related_files:
  - "[[Lang_RU/10_Mechanics/01_Player_Core/Specs_Mechanics|Specs_Mechanics]]"
  - "[[Lang_RU/10_Mechanics/01_Player_Core/Tags_System|Tags_System]]"
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
Теги являются модификаторами для базовых атрибутов (см. [[Lang_RU/10_Mechanics/01_Player_Core/Character_Specification]]):
* `[Strong]` -> +STR.
* `[Agile]` -> +AGI.
* `[Tough]` -> +CON/END.

## 4. Эволюция Тегов (Tag Synergy)
Если персонаж обладает двумя синергирующими тегами, они могут **слиться** в один "Золотой Тег" (Golden Tag), освобождая слот памяти и давая мощный эффект.
* *Пример:* `[Effect: Burn]` + `[Master: Fire]` = Эволюция в `[Pyromancer]` (Иммунитет к огню + Усиление урона огнем).

## 5. Характеристики (Attributes) TBD
Теги напрямую влияют на 5 основных атрибутов:
1.  **Сила (STR):** Грузоподъемность, урон ближнего боя.
2.  **Ловкость (DEX):** Скорость, крит, обращение с легким оружием.
3.  **Телосложение (CON):** HP, сопротивление травмам.
4.  **Интеллект (INT):** Эффективность техники, крафт.
5.  **Мудрость/Эфир (WIS):** Cила заклинаний.
