---
type: mechanic
system: trade_craft
tags: [crafting, rng, upgrades, orbs]
related_files:
  - "[[Lang_RU/00_Variables/Registry_CraftingRecipes|Registry_CraftingRecipes]]"
---

# Крафт: Декораторы и Аффиксы (RNG System)

## 1. Слоты Декораторов
В окне крафта есть опциональные слоты для **Катализаторов Качества** (например, `Orb of Flux`, `Fire Essence`).

## 2. Логика Модификации
Если слот пуст — создается предмет с `Fixed Stats` (из базы данных).
Если добавлен Декоратор, запускается генератор:

### Сценарии (Examples)
* **Orb of Flux (Rarity Up):**
    * `Chance`: 100%
    * `Effect`: Tier предмета повышается (White -> Green). Генерируется 1 случайный аффикс из пула `Group_Generic`.
* **Essence (Determenistic):**
    * `Input`: `Fire Essence`
    * `Effect`: Гарантированно добавляет аффикс `+Fire Damage`, остальные статы случайны.
* **Entropy Orb (Risk):**
    * `Effect`: Ролл d4 по таблице "Corruption" (Слом / Легендарка / Мутация).

## 3. Генерация Предмета
1.  Создается "болванка" предмета.
2.  Применяются базовые статы.
3.  Применяются аффиксы от декораторов (`Item.AddModifier()`).
4.  Предмет выдается игроку.