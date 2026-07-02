# Eldraine: handoff «Race × Spec → оружие → мастерство → Термос»

Этот архив — сфокусированный срез активного GDD Eldraine для независимого третьего ревью. Он содержит только цепочку персонажа и снаряжения, а не весь мир, экономику или Аномалии.

## Статус после первого ревью

- старые многозонные пакеты модулей помечены `install_state:: blocked_calibration` и не могут устанавливаться до атомизации;
- Gate Check суммирует `environment_resistance` работающих установленных модулей вместо старого поля единой `Armor`;
- `Shell.Entropy_Buffer` в текущем MVP явно равен `0` и остаётся зарезервированной точкой расширения;
- базовое ближнее оружие получило утверждённые `weapon_vector`, `vector_gate`, нулевые `heat` и `dissonance_pulse`;
- разница `45/75` между Handcannon и Longframe не исправлялась вслепую: она вынесена в проверку полного цикла с HP, пластинами, точностью, Heat, Pulse и стоимостью потери.

## Что требуется проверить

1. Понятна ли игроку разница между оружейным proficiency, профильной ёмкостью Пешки, физическими слотами Термоса и `module_cost`.
2. Создаёт ли `Race × Spec` несколько жизнеспособных сборок вместо одной обязательной.
3. Не возникает ли доминирующий Armor Rat, бесплатное сжатие функций гибридами или обесценивание старых модулей.
4. Достаточно ли прозрачен путь `Хаб → мастер → stitched_locked → рейд → возврат`.
5. Где документы противоречат друг другу или требуют отсутствующего правила.

Не предлагай числа как канон без отдельной модели. Сначала отделяй подтверждённые правила от `UNKNOWN` и тестовых примеров.

## Короткая модель

```text
Race × Spec
  -> P/Q/E и оружейное владение
  -> базовые module_capacity

Постоянные теги
  -> prof_delta оружия
  -> module_capacity_delta Термоса

Модель Термоса
  -> fit_profile
  -> slot_count
  -> физические позиции

Модуль
  -> module_families
  -> раздельный module_cost
  -> slot_size и module_positions
  -> игровые оси и фактический эффект
```

Сборка допустима, если одновременно подходят посадка, физические слоты, позиции и профильные ёмкости. Гибрид занимает физические слоты один раз, но оплачивается по каждому семейству отдельно. Tier, Rarity, module_cost, вес, Диссонанс и рыночная цена являются разными осями.

Модули устанавливаются и снимаются только у профессионала в Хабе. После подтверждения они получают `stitched_locked`; найденный в Аномалии модуль остаётся Cargo до возвращения.

Термос — сменная вещь общей неокультуры Элдрейна, а не пожизненное продолжение тела. Личная память и многолетний ремонт возможны, но не обязательны.

## Рекомендуемый порядок чтения

### 1. Контекст игры

1. `01_Core_Vision/01_Vision.md`
2. `01_Core_Vision/02_Core_Loop.md`
3. `01_Core_Vision/Glossary.md`
4. `02_World_Lore/Culture_Language.md`

### 2. Персонаж и комбинация

1. `04_Player_Entities/MVP_3x3_Design_Contract.md`
2. `04_Player_Entities/_Registries/Registry_Races.md`
3. `04_Player_Entities/_Registries/Registry_Specs.md`
4. `04_Player_Entities/_Registries/Registry_Combos.md`
5. `04_Player_Entities/Ability_Synergy.md`

### 3. Мастерство и теги

1. `04_Player_Entities/Proficiency_Arsenal.md`
2. `04_Player_Entities/Tags_System.md`
3. `04_Player_Entities/_Registries/Registry_Tags.md`
4. `04_Player_Entities/Combat_Profile_Pipeline.md`
5. `04_Player_Entities/_Matrices/00_Character_Matrix.md`

### 4. Оружие

1. `05_Combat_Survival/Weapon_Core.md`
2. `05_Combat_Survival/Registry_Weapons.md`
3. `05_Combat_Survival/Weapon_Ranged.md`
4. `05_Combat_Survival/Weapon_Melee.md`
5. `05_Combat_Survival/Magic_Batteries.md`

### 5. Термос, одежда и модули

1. `07_Gear_Inventory/Thermos_System.md`
2. `07_Gear_Inventory/Equipment_PaperDoll.md`
3. `07_Gear_Inventory/_Registries/Registry_Thermoses.md`
4. `07_Gear_Inventory/_Registries/Registry_Thermos_Modules.md`
5. `07_Gear_Inventory/Fashion_Gear.md`
6. `07_Gear_Inventory/Civic_Attire.md`
7. `07_Gear_Inventory/_Registries/Registry_Attire.md`

### 6. Прогрессия, интерфейс и подготовка

1. `07_Gear_Inventory/Gear_Progression.md`
2. `07_Gear_Inventory/Affix_Grammar.md`
3. `07_Gear_Inventory/Item_Attributes_UI.md`
4. `07_Gear_Inventory/Physical_Weight.md`
5. `07_Gear_Inventory/Item_Calibration_Matrix.md`
6. `08_World_Generation/Generation/08_Gate_Check.md`
7. `08_World_Generation/Hub/02_Hub_Services_Interaction.md`

## Что ещё не определено

- базовые `module_capacity` девяти MVP-комбинаций;
- реальные `slot_count` и топология моделей Термосов;
- `slot_size` и `module_cost` существующих модульных пакетов;
- стоимость и длительность работы мастера;
- числовой коридор веса, защиты, Диссонанса и замены после смерти;
- финальный набор оптических, герметизирующих и утилитарных модулей.

`UNKNOWN` является честным отсутствием калибровки, а не нулём.

## Границы архива

- Obsidian-ссылки на отсутствующие файлы могут вести в системы вне этого handoff.
- Реестры и DataviewJS сохранены с исходной структурой папок.
- Архив не содержит Git, `_Archive`, исходные референсы или внутренние инструкции Codex.
- При конфликте внутри архива приоритет имеет `Thermos_System.md`, затем `MVP_3x3_Design_Contract.md`, `Proficiency_Arsenal.md` и структурированные реестры.

## Удобный запрос для третьего ревью

> Проведи независимый системный аудит приложенного среза GDD. Сначала восстанови фактическую модель `Race × Spec → оружейное владение/module_capacity → Термос и модули`. Отдельно перечисли противоречия, неясные игроку причины отказа, доминирующие сборки, мёртвые ветки прогрессии и отсутствующие значения. Не назначай балансные числа без явной тестовой модели и не переписывай атмосферу вместо анализа механики.
