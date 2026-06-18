---
type: registry
status: active
system: gear_inventory_registry
registry_type: armor
tags:
  - magipunk
  - gear
  - protection
  - active_tanking
---
# Реестр: Броня и Одеяния (Magipunk Armor)

> **Философия Стиля:**
> "Слой за слоем". Персонажи носят свободные, мешковатые одежды, скрывающие контуры тела.
> * **Hard Layer (Пластины):** Зачарованная керамика с гравировкой. Светятся при попадании.
> * **Soft Layer (Ткань):** Стеганый шелк, вываренная кожа, эфирное полотно.
> * **Mobility First:** Никаких цельных кирас. Только сегменты, не сковывающие акробатику.

> **Параметры:**
> `[armor_plates:: ...]` — Зоны абсолютной защиты (Рунные плиты).
> `[armor_axes:: ...]` — игровые специализации брони помимо покрытия.

Броня не дает механические «карманы». Карманы остаются частью визуального языка одежды. Игровые оси:

- `coverage` — зоны и работа пластин;
- `environment` — сопротивление среде;
- `mobility` — инерция, карабканье, восстановление движения;
- `energy` — передача батарей, Heat sink, защита контура;
- `cantrip` — переносимость Backlash и травмы;
- `stealth` — акустический, тепловой и резонансный след;
- `support` — лечение, стабилизация и работа с устройствами;
- `cargo` — перенос Back Slot и тяжелых объектов.

---

## 1. Тяжелые Латы (Heavy Plate)
*Сплав магии земли и металла. Массивные, но разбитые на множество подвижных сегментов.*
*Стиль: "Бронированный Монах". Широкие штаны, массивные поножи и наплечники, торс часто открыт или закрыт тканью.*

### Комплект "Базальт" (Basalt Shell)
[tier:: 2] | [environment_resistance:: 55] | [armor_plates:: chest, arm guards, shoulder pads, shin_guards] | [armor_axes:: coverage, cargo] | [weight:: 22kg] | [armor_type:: heavy_plate]
*Грубые керамические плиты, словно вырезанные из скалы, надетые поверх плотной шерстяной робы.*
* **Pattern (Покрытие):** **Bastion.** Массивные наплечники, позволяющие спрятать голову. Спина закрыта лишь тканью плаща.

### Доспех "Хранитель Очага" (Hearth-Keeper)
[tier:: 3] | [environment_resistance:: 70] | [armor_plates:: l_shoulder, r_shoulder, thighs, chest_center] | [armor_axes:: coverage, environment, energy] | [weight:: 18kg] | [armor_type:: heavy_plate]
*Древние ритуальные плиты, пульсирующие теплом.*
* **Pattern (Покрытие):** **Frontal.** Мощная грудная пластина с руной. Руки ниже локтя открыты для сотворения заклинаний.

---

## 2. Композитные Одеяния (Composite Layers)
*Смесь кожи, цепей и зачарованной ткани. Выбор наемников и путешественников.*
*Стиль: "Бродяга". Много ремней, подсумков, плащи с капюшонами.*

### Сбруя "Наемник" (Mercenary Rig)
[tier:: 2] | [environment_resistance:: 35] | [armor_plates:: upper_chest, stomach, forearms] | [armor_axes:: mobility, support] | [weight:: 12kg] | [armor_type:: composite_rig]
*Кожаный жилет с нашитыми керамическими чешуйками.*
* **Pattern (Покрытие):** **Duelist.** Усиленные наручи с рунами твердости (можно отбивать мечи руками).

### Жилет "Собиратель" (Scavenger Wrap)
[tier:: 1] | [environment_resistance:: 15] | [armor_plates:: chest_heart] | [armor_axes:: mobility, cargo] | [weight:: 6kg] | [armor_type:: composite_rig]
*Мешковатая куртка со множеством скрытых карманов. Единственная пластина защищает сердце.*
* **Pattern (Покрытие):** **Minimal.** Защита символическая, расчет на то, что в свободную одежду сложнее попасть.

---

## 3. Эфирный Шелк (Ether Weave)
*Тончайшие ткани, укрепленные магическим плетением.*
*Стиль: "Тень". Облегающие костюмы, скрытые под развивающимися лохмотьями.*

### Мантия "Проводник" (Conduit Robe)
[tier:: 2] | [environment_resistance:: 40] | [armor_plates:: r_shoulder, back_spine] | [armor_axes:: energy, cantrip] | [weight:: 3kg] | [armor_type:: ether_weave]
*Ткань, которая слегка искрит при касании. В воротник вплетены кристаллы.*
* **Pattern (Покрытие):** **Asymmetric.** Правое плечо закрыто кристаллическим наплечником (гасит отдачу посохов/катализаторов).

### Костюм "Призрак" (Wraith Veils)
[tier:: 1] | [environment_resistance:: 20] | [armor_plates:: none] | [armor_axes:: mobility, stealth] | [weight:: 2kg] | [armor_type:: ether_weave]
*Многослойный балахон из полупрозрачной дымчатой ткани.*
* **Pattern (Покрытие):** **Evasive.** Нет жестких элементов. Ткань колышется, размывая силуэт врагу.
---

## 0. Нулевой пациент: шаблон брони

### Шаблон Брони (Template Armor)
[armor_id:: template_armor]
[armor_type:: light_armor]
[tier:: 1]
[protection_vector:: ballistics]
[armor_axes:: mobility]
[environment_resistance:: 0]
[weight:: 1.0kg]
[value:: 0]
*Короткое описание защитной роли.*
- **Защищает от:** урон, среда или статус.
- **Плата:** вес, шум, перегрев, потеря гибкости.
- **Слои:** где сидит на бумажной кукле.
