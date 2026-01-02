---
type: variable_registry
category: attributes
system: dnd_hybrid
tags: [stats, formulas, core]
---

# Система Атрибутов (S.A.V.I.T.)
*Адаптированная D&D система под Magipunk.*

Вместо плоских значений (HP = 100), все показатели персонажа являются **Производными (Derived Stats)** от пяти основных атрибутов.
Базовое значение атрибута для "Нулевого пациента": **10**.

## 1. СИЛА (PHY - Physique)
*Отвечает за физическую мощь, вес и грубую силу.*
> **Философия:** "Броня ничего не весит, если ты достаточно силен."

* **Влияет на:**
	* `Physical Power`: +1% Физ. урона за единицу > 10.
	* `Carry Weight`: +2 кг лимита веса за очко.

## 2. ЛОВКОСТЬ (AGI - Agility)
*Отвечает за координацию, скорость рук и ног.*
> **Философия:** "Скорость убивает. Медленный — значит мертвый."

* **Влияет на:**
	* `Move Speed`: +0.5% к Скорости передвижения.
	* `Action Speed`: Скорость открытия сундуков, установки мин, перезарядки (+1% за очко).
	* `Stealth Rating`: Снижает общий шум.

## 3. СТОЙКОСТЬ (VIG - Vigor)
*Отвечает за здоровье, иммунитет и сопротивление травмам.*
> **Философия:** "Главное не как сильно ты бьешь, а как держишь удар."

* **Влияет на:**
	* `Max HP`: +3 HP за каждое очко.
	* `Trauma Resist`: Шанс проигнорировать кровотечение/перелом.
	* `Recovery`: Скорость восстановления стамины.

## 4. ТЕХНО-ЗНАНИЕ (TEC - Tech/Intellect)
*Замена Интеллекту. Способность обращаться со сложными механизмами и магией.*
> **Философия:** "Магия — это просто сложная инженерия. Не перегревайся."

* **Влияет на:**
	* `Не знаю`

## 5. РЕЗОНАНС (RES - Resonance/Will)
*Замена Мудрости/Воле. Сопротивление Энтропии и ментальная связь.*
> **Философия:** "Бездна смотрит на тебя. Не моргай."

* **Влияет на:**
	* `Magic Resist`: Сопротивление урону от заклинаний.
	* `Entropy Buffer`: Замедляет накопление порчи в "грязных" зонах.
	* `Detection`: Радиус обнаружения ловушек и невидимых врагов.

---

# Формулы Расчета (Formulas)

### 1. Здоровье (Hit Points)
$$MaxHP = stat\_hp\_start + (VIG \times 3) + (Race\_Bonus)$$

* **База (из конфига):** `$= dv.page("00_Variables/Registry_Stats.md").stat_hp_base` HP.
* *Пример расчета (для VIG=15):*
    `$= dv.page("00_Variables/Registry_Stats.md").stat_hp_base` + (15 * 3) = **`$= dv.page("Lang_RU/00_Variables/Registry_Stats.md").stat_hp_base + 45` HP**.

### 2. Переносимый Вес (Loadout)
$$MaxWeight = stat\_carry\_weight\_base + (PHY \times 2)$$

* **База (из конфига):** `$= dv.page("00_Variables/Registry_Stats.md").stat_carry_weight_base` кг.
* *Пример расчета (для PHY=20):*
    `$= dv.page("00_Variables/Registry_Stats.md").stat_carry_weight_base` + (20 * 2) = **`$= dv.page("00_Variables/Registry_Stats.md").stat_carry_weight_base + 40` кг**.

### 3. Скорость Действий (Action Speed)
$$ActSpd = stat\_action\_speed\_base + ((AGI - 10) \times 0.02)$$

* **База (из конфига):** `$= dv.page("00_Variables/Registry_Stats.md").stat_action_speed_base` (100%).
* Влияет на анимации: *Лечение, Лутание, Перезарядка*.

### 4. Скорость Передвижения (Move Speed)
$$MoveSpd = stat\_speed\_base \times (1 + (AGI \times 0.005))$$

* **База (из конфига):** `$= dv.page("00_Variables/Registry_Stats.md").stat_speed_base` м/с.