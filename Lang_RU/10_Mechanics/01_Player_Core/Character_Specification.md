---
type: mechanic
system: player_core
tags:
  - character
  - progression
  - formulas
related_files:
  - "[[10_Mechanics/01_Player_Core/Races_Mechanics|Races_Mechanics]]"
  - "[[10_Mechanics/01_Player_Core/Specs_Mechanics|Specs_Mechanics]]"
  - "[[Lang_RU/10_Mechanics/01_Player_Core/Character_Specification|Character_Specification]]"
  - "[[Lang_RU/10_Mechanics/01_Player_Core/Character_Specification|Character_Specification]]"
---

# Спецификация: Конструктор Персонажа

## 1. Формула Генерации
Персонаж (Entity) создается путем сложения двух основных баз данных и случайных элементов.

$$Character = Race\_Data + Spec\_Data + Random\_Traits$$

### Процесс сборки
1.  **Выбор Расы:** Система применяет базовые статы и модификаторы из [[Lang_RU/10_Mechanics/01_Player_Core/Races_Mechanics]].
    * *Пример:* Лазур (+3 AGI).
2.  **Выбор Специализации:** Система выдает стартовый комплект (Kit) и активный навык из [[Lang_RU/10_Mechanics/01_Player_Core/Specs_Mechanics]].
    * *Пример:* Дуэлянт (Рапира, Навык Парирования).
3.  **Расчет Синергии:** Проверка таблицы [[Lang_RU/10_Mechanics/01_Player_Core/Progression#Synergy_Matrix]].
    * *Лазур* + *Дуэлянт* = Открывается скрытая пассивка **"Танец Смерти"** (Уклонение повышает крит).

## 2. Расчет Характеристик (Final Stats)
Итоговые цифры, которые определяют эффективность персонажа.

| Параметр | Формула | Описание |
| :--- | :--- | :--- |
| **Max HP** | `Base(100) + (STR * 5) + (END * 10)` | Очки здоровья. База берется из глобальной переменной `stat_hp_start`. |
| **Stamina** | `Base(50) + (END * 2) - (Armor_Weight)` | Выносливость для спринта и спецатак. |
| **Speed** | `Base(100%) + (AGI * 1.5%)` | Скорость передвижения (м/с). |
| **Stealth** | `(AGI * 2) - (Inventory_Value / 100)` | Шанс остаться незамеченным. Зависит от загруженности инвентаря. |

## 3. Слоты Экипировки (Hardpoints)
Анатомия слотов, доступная для установки предметов (см. [[Lang_RU/10_Mechanics/04_Inventory_Gear/Inventory_Core]]).
* **Голова:** 1 слот (Шлем/Очки/Маска).
* **Тело:** 1 слот (Броня/Разгрузка).
* **Спина:** 1 слот (Рюкзак/Плащ/Баллоны).
* **Руки:** 2 слота (Main Hand + Off Hand) или 1 слот (Two-Handed).
* **Пояс:** `4 + (STR / 3)` слотов быстрого доступа (Quick Slots) под расходники.