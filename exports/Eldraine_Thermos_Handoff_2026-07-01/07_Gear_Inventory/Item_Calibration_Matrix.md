---
type: matrix
status: active
system: gear_balance
tags: [items, weight, value, dissonance, survival_score, calibration]
related_files:
  - "[[07_Gear_Inventory/_Registries/Registry_Items|Registry_Items]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Thermoses|Registry_Thermoses]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Thermos_Modules|Registry_Thermos_Modules]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Consumables|Registry_Consumables]]"
  - "[[05_Combat_Survival/Registry_Weapons|Registry_Weapons]]"
  - "[[08_World_Generation/Generation/08_Gate_Check|Gate_Check]]"
  - "[[08_World_Generation/Generation/19_Access_Contracts|Access_Contracts]]"
  - "[[05_Combat_Survival/Dissonance_System|Dissonance_System]]"
  - "[[05_Combat_Survival/Threat_Thresholds|Threat_Thresholds]]"
  - "[[07_Gear_Inventory/Gear_Progression|Gear_Progression]]"
---
# Матрица Калибровки Предметов

## 1. Цель

Эта матрица является обязательным промежуточным слоем между реестрами предметов и балансными порогами.

До заполнения таблицы значения `T1 -> T2 = 140`, `T2 -> T3 = 260`, лимиты Диссонанса и доходность `5-8% стоимости полного комплекта` считаются **тестовыми якорями**, а не доказанным балансом.

## 2. Обязательные Поля

Каждый предмет, влияющий на вход в рейд или его экономику, должен иметь:

| Поле | Смысл |
|---|---|
| `item_id` | стабильный ключ предмета |
| `category` | оружие, Термос, модуль, маска, батарея, расходник, контейнер, лут |
| `tier` | класс конструкции и допустимой нагрузки; не общий Power Score |
| `rarity` | число и сложность аффиксов, без прямого Power Score |
| `weight_kg` | физический вес одной единицы |
| `value_rez` | базовая стоимость |
| `base_dissonance` | диссонанс до `sync_multiplier` |
| `environment_resistance` | вклад брони в `SurvivalScore` |
| `filter_rating` | вклад маски |
| `battery_buffer` | вклад батареи или стабилизатора |
| `stabilizer_bonus` | одноразовый или постоянный бонус |
| `availability` | welfare, vendor, craft, quest, raid-only |
| `loss_replace_cost` | реальная цена замены после смерти |
| `load_class` | допустимая энергетическая нагрузка оружейного Frame |
| `strong_cycle` | число усиленных действий до критического Recovery |
| `battery_compatibility` | базовая, усиленная и Overcharge-совместимость |
| `slot_count` | физические узлы модели Термоса либо `none` |
| `slot_size` | число узлов, занимаемых модулем, либо `none` |
| `module_positions` | допустимые позиции модуля либо `none` |
| `module_cost` | раздельная стоимость по семействам либо `none` |

Если поле не применимо, ставится `0` или `none`. Если значение ещё не определено, оно маркируется `UNKNOWN`, а не заменяется догадкой.

## 3. Текущие Известные Значения Стартового Набора

| Предмет | Tier | Вес | Цена | Environment | Filter | Battery Buffer | Статус |
|---|---:|---:|---:|---:|---:|---:|---|
| `Scavenger Wrap` | 1 | 6.0 кг | `UNKNOWN` | 15 | 0 | 0 | `slot_size` и `module_cost` не определены |
| `Cracked Cell` | 1 | 0.3 кг | 250 | 0 | 0 | `UNKNOWN` | buffer не определен |
| T1 оружие Бомжа | 1 | `UNKNOWN` | `UNKNOWN` | 0 | 0 | 0 | конкретный предмет не закреплен |
| Базовая маска | 1 | `UNKNOWN` | `UNKNOWN` | 0 | `UNKNOWN` | 0 | стартовая модель не закреплена |
| Базовая Пешка | — | — | — | `Current_HP UNKNOWN` | 0 | 0 | `Entropy_Buffer = 0` в текущем MVP |

## 4. Проверка Access Readiness

Для каждого тестового комплекта считать:

```text
InstalledModuleEnvironment =
  sum(InstalledThermosModule.environment_resistance)

SurvivalScore =
  Current_HP
  + InstalledModuleEnvironment
  + Filter_Rating
  + Battery_Buffer
  + Stabilizer_Bonus
  + Shell.Entropy_Buffer
  - Open_Wounds_Penalty
  - Overload_Penalty

DissonanceLoad =
  sum(Item.base_dissonance * sync_multiplier)
  + sum(BodyTag.dissonance_load)
  + persistent_effects

AnomalyPressure =
  DissonanceLoad
  + RecentDissonancePulse
```

В `InstalledModuleEnvironment` входят только установленные работающие модули с `install_state:: installable`. `Shell.Entropy_Buffer = 0` для всех Пешек текущего MVP и остаётся зарезервированной точкой расширения до появления явного канонического источника.

Обязательные комплекты для первой калибровки:

1. **Welfare:** бесплатный Бомж без найденного усиления.
2. **Prepared T1:** разумно собранный комплект перед входом.
3. **Field Upgraded:** стартовый комплект плюс найденная в рейде подготовка к T2.
4. **Overgeared:** дорогой комплект, переживающий среду, но приближающийся к Yellow/Red Dissonance.
5. **Foundling Standard:** типичный комплект ценной Пешки, потеря которого должна быть экономически болезненной.
6. **Armor Rat:** сильная броня плюс самое дешевое летальное оружие.
7. **Glass Cannon:** сильное оружие плюс минимальная допустимая защита.
8. **T1 Specialist:** редкий низкотировый предмет в своей лучшей нише.
9. **Squad Carrier:** один продвинутый Frame на группу с бюджетными союзниками.
10. **Recovery Drop:** бедный поздний вход в T2/T3 без главного прогресса контрактов.

## 5. Экономический Срез

Для каждого комплекта фиксировать:

| Метрика | Формула |
|---|---|
| Стоимость входа | сумма replacement cost экипировки и расходников |
| Цена Access Contract | Rez, допуск, ключ, долг или услуга за выбранное окно |
| Вес входа | сумма веса всего снаряжения |
| Свободная грузоподъемность | carry limit минус вес входа |
| Средняя добыча | медиана успешного рейда по Tier |
| Обязательные расходы | лечение, батареи, фильтры, стабилизация, комиссия |
| Ожидаемая потеря | стоимость входа × вероятность смерти |
| Чистая доходность | добыча минус расходы и ожидаемая потеря |

## 6. Порядок Работы

1. Нормализовать поля в реестрах оружия, Термосов, модулей, масок, батарей и расходников.
2. Закрепить конкретный Welfare Kit.
3. Рассчитать пять обязательных комплектов.
4. Проверить, существует ли практический коридор между Environment Gate и Dissonance Threshold.
5. Только после этого менять пороги `140/260` и процент доходности полного комплекта.
6. Сравнить риск-скорректированную доходность `Balanced`, `Armor Rat`, `Glass Cannon` и `Squad Carrier`.
7. Проверить, что глубокая награда требует повторяемого рабочего цикла, но не запрещает T1 совершить PvP-переворот.
8. Проверить, что `Deep T3` и `Recovery Drop` поддерживают плотность поздней фазы, но не превращают T3 в бесплатный scav-фарм.
