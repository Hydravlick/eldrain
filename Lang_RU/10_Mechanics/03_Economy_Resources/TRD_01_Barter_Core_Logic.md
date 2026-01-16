---
type: mechanic
system: trade_craft
tags: [barter, crafting, core]
related_files:
  - "[[Lang_RU/00_Variables/Registry_CraftingRecipes|Registry_CraftingRecipes]]"
---

# Торговля: Ядро Бартера (Barter Core)

## 1. Единая Система
В коде нет различий между "Крафтом на верстаке" и "Покупкой у Торговца". Оба действия используют класс `RecipeTransaction`.

## 2. Структура Сделки (The Recipe)
Любая операция описывается формулой:
$$[Input\_List] + [Blueprint] + [Catalyst\_Rez] \xrightarrow{Time} [Output\_Item]$$

### Компоненты:
1.  **Inputs:** Список предметов-ингредиентов (Array).
2.  **Blueprint:** (Optional) Требуемый предмет знания (см. `TRD_02`).
3.  **Catalyst:** Валюта (Рез), оплачивающая работу/энергию.
4.  **Decorators:** (Optional) Дополнительные слоты для повышения качества (см. `TRD_03`).

## 3. Валидация (Check Process)
Перед активацией кнопки "Craft/Buy":
1.  **Check Currency:** Хватает ли Реза (Inv + Stash)?
2.  **Check Items:** Хватает ли ингредиентов?
3.  **Check Space:** Есть ли свободное место в инвентаре для `Output_Item`? (Важно: учитываем размеры сетки).

## 4. Результат
При успехе:
* Ингредиенты и Валюта удаляются (`Destroy`).
* Создается `New Item Instance`.
* Если использовались Декораторы, запускается `Affix Generator`.