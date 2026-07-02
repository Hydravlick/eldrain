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
| `active_body_interface` | ID активного Опорного контура либо `none` |
| `requested_touch_shift` | заявленный сдвиг активного контура |
| `applied_touch_shift` | часть сдвига после внешнего и итогового клэмпа |
| `touch_overflow` | неприменённая часть сдвига |
| `interface_vulnerability` | наблюдаемая цена контура |

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

В `InstalledModuleEnvironment` входят только установленные работающие модули с `install_state:: installable`. `Shell.Entropy_Buffer` читает явный телесный substat `entropy_buffer`; пока ни одна MVP-запись не выдаёт его, значение остаётся `0`. Он не входит в модульную защиту и не заменяет Environment Seal.

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

### Проверка Опорного контура

Prototype-модули `body_interface` остаются `blocked_calibration`, пока семь полных комплектов не пройдут этот срез. `unmeasured` означает отсутствие цены, тайминга или вероятности, а не положительный результат.

| Комплект | Что должен доказать контур | Главный риск | Статус |
|:---|:---|:---|:---|
| Welfare | базовая летальность и T1 остаются доступны без контура | обязательный слот прогрессии | `unmeasured` |
| Balanced | один контур создаёт специализацию, не закрывая все задачи | универсальный безопасный обмен | `unmeasured` |
| Armor Rat | `+LYR/+TRQ` оплачены мобильностью, лутом или темпом | дешёвая летальность плюс слишком много права на ошибку | `unmeasured` |
| Glass Cannon | `+GLW/+GRP` не отменяют Heat, Recovery и батарейный риск | непрерывный DPS | `unmeasured` |
| T1 Specialist | дешёвый старый контур сохраняет узкую нишу | обязательная замена на Tier выше | `unmeasured` |
| Squad Carrier | контур усиливает только носителя | бесплатный групповой проход | `unmeasured` |
| Overgeared | один активный контур и клэмпы не позволяют поднять всё тело | богатая сборка без уязвимости | `unmeasured` |

### Проверка Боевого Долга

Каждый полный комплект дополнительно проходит один и тот же срез:

| Комплект | Импульсы | Окна | Recovery | Телесная Экономика |
|:---|:---|:---|:---|:---|
| Welfare | батарея не обязательна для базовой летальности | может создать или использовать одно честное окно | не отменяется бесплатной сменой канала | жизнь выгоднее штатной жертвы |
| Balanced | Weapon/Casting Reserve требуют явного выбора | два канала не закрывают все функции | переход сохраняет долг предыдущего действия | кантрип остаётся аварийным решением |
| Glass Cannon | сильный импульс не становится непрерывным DPS | быстро использует подготовленное окно | ошибка оставляет взыскиваемый Recovery | низкий HP не усиливает кантрип |
| T1 Specialist | дешёвый Frame сохраняет узкую роль | primary window читается и контрится | ниша не удаляет commitment | не производит передаваемую ценность телом |
| Squad Carrier | один резерв не питает группу бесплатно | команда ускоряет реализацию, не создаёт функцию впервые | прикрытие не отменяет Recovery носителя | жертвуемый Welfare не повышает чистую прибыль |
| Overgeared | аффиксы переносят долг, но не удаляют остаток | нет универсального create/exploit/mitigate | лучший цикл остаётся прерываемым | дорогая устойчивость не требует дешёвого смертника |

Для сравнения фиксировать распределение импульсов между Weapon/Casting Reserve, долю неразрешённых отмен Recovery, максимальную цепочку hard control и риск-скорректированную прибыль живого и жертвуемого Welfare.

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
