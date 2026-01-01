---
type: mechanic
system: class
tags:
  - character
  - progression
  - core
  - formulas
related_files:
  - "[[Lang_RU/10_Mechanics/Meta/Tags_System]]"
  - "[[Lang_RU/10_Mechanics/Meta/Races_Mechanics]]"
  - "[[Lang_RU/10_Mechanics/Meta/Specs_Mechanics]]"
---

# Спецификация: Конструктор Персонажа

## 1. Формула Генерации
Персонаж (Entity) создается путем сложения двух баз данных.

$$Character = Race\_Data + Spec\_Data + Random\_Traits$$

### Процесс (Step-by-Step)
1.  **Выбор Расы:** Система берет статы из [[Lang_RU/10_Mechanics/Meta/Races_Mechanics]].
    * *Пример:* Лазур (+3 AGI).
2.  **Выбор Спека:** Система выдает предметы и навык из [[Lang_RU/10_Mechanics/Meta/Specs_Mechanics]].
    * *Пример:* Дуэлянт (Рапира, Навык Парирования).
3.  **Расчет Синергии:** Проверка таблицы [[Lang_RU/10_Mechanics/Meta/Progression#Synergy_Matrix]].
    * *Лазур* + *Дуэлянт* = Открывается скрытая пассивка **"Танец Смерти"** (Уклонение повышает крит).

## 2. Расчет Характеристик (Final Stats)
Итоговые цифры, которые видит игрок.

| Параметр | Формула | Описание |
| :--- | :--- | :--- |
| **Max HP** | `Base(100) + (STR * 5) + (END * 10)` | Очки здоровья. |
| **Stamina** | `Base(50) + (END * 2) - (Armor_Weight)` | Выносливость для бега/атак. |
| **Speed** | `Base(100%) + (AGI * 1.5%)` | Скорость передвижения. |
| **Stealth** | `(AGI * 2) - (Inventory_Value / 100)` | Шанс остаться незамеченным. |

## 3. Слоты (Hardpoints)
У каждого персонажа есть фиксированная анатомия для экипировки.
* **Голова:** 1 слот (Шлем/Очки).
* **Тело:** 1 слот (Броня).
* **Спина:** 1 слот (Рюкзак/Плащ).
* **Руки:** 2 слота (Main Hand + Off Hand).
* **Пояс:** `4 + (STR / 3)` слотов под расходники.