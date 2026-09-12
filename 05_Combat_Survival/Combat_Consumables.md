---
status: active
system: action_combat
tags:
  - medicine
  - health
  - field_capacity
  - action_commitment
related_files:
  - "[[07_Gear_Inventory/Registries/Registry_Consumables|Registry_Consumables]]"
  - "[[05_Combat_Survival/Registries/Registry_StatusEffects|Registry_StatusEffects]]"
  - "[[04_Player_Entities/Skill_Build_Philosophy|Skill_Build_Philosophy]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
  - "[[08_World_Generation/Hub/Hub_Services_Interaction|Hub_Services_Interaction]]"
type: system
canonical_id: HEALTH
owns:
  - health.values_and_bounds
  - health.damage_and_restoration
  - health.permanent_capacity_resolution
  - health.basic_hub_recovery
index_route: owner
index_group: combat_survival
index_order: 60
index_summary: "Определяет состояния, разрешение и связи: Медицина, здоровье и необходимые расходники."
read_when: Когда нужен контракт «Медицина, здоровье и необходимые расходники» и его границы с соседними владельцами.
---
# Медицина, здоровье и необходимые расходники

> В Элдрейне лекарь может удержать живого в бою, но не отменяет травму, долг сцены или смерть. Предмет покупает телесную процедуру; батарея питает полную версию навыка. Это разные решения, а не две цены за одну кнопку.

## 1. Граница расходников и навыков

Батарея — единственный внешний энергетический расход полного боевого навыка. `Race × Spec` задаёт процедуру, а тело, Frame или устройство исполняют её. Колба, граната, ловушка, барьер, световое поле и сходный боевой результат не требуют отдельного payload-предмета: это временное, не извлекаемое состояние, исполненное батареей через навык.

Обычные расходники остаются только там, где игрок работает с телом или доступом:

- бинты, стимуляторы, шины и профильные медицинские средства;
- ключи и иные одноразовые допуски;
- карты, следы и доказательства как экспедиционные предметы. Они не считаются расходниками, если не уничтожаются своим конкретным применением.

Боевой навык не тратит бинт, зелье или второй предмет ради собственного эффекта. Если действие требует такой вещи, это самостоятельная предметная процедура, а не Q/E.

## 2. Контракт здоровья

Здоровье конкретной Пешки разрешает только этот owner (`HEALTH`); значения хранятся в её BodyID. Игрок видит три значения:

```text
0 <= CurrentHP <= FieldCapacity <= MaxCapacity
```

| Состояние | Игровой смысл | Кто меняет |
|:---|:---|:---|
| `MaxCapacity` | текущий постоянный максимум тела после permanent consequences | Health пересчитывает по определению тела и действующим последствиям с конкретными источниками |
| `FieldCapacity` | доступная в текущей вылазке телесная ёмкость | объявленная тяжёлая травма, среда, Gate Check и профильная полевая медицина |
| `CurrentHP` | немедленная боевая жизнь | обычный урон, лечебные навыки и часть медицины |

Обычный урон уменьшает `CurrentHP`. `FieldCapacity` уменьшается **только** от явно телеграфируемого источника: тяжёлой травмы, названного статусного эффекта, опасной среды, критического последствия либо [[08_World_Generation/Generation/Gate_Check|Gate Check]]. Это не процент от каждого попадания и не скрытый chip-штраф.

Величины damage, capacity-loss и восстановления неотрицательны; недопустимый вход не применяется. Изменение здоровья публикует согласованную тройку атомарно, включая ограничение нижележащих значений после потери максимума.

```text
FieldCapacity' = max(0, FieldCapacity - declared_capacity_loss)
CurrentHP' = min(FieldCapacity', max(0, CurrentHP - hp_loss))
```

При `CurrentHP = 0` Combat передаёт lethal event в [[04_Player_Entities/Lifecycle_Resolver|Lifecycle Resolver]], который определяет исход по существующему контракту; Health не объявляет самостоятельно KIA и не создаёт новый путь спасения. Лечебная аура, поле, кантрип или предмет не являются revive-механикой.

### Постоянные последствия

[[04_Player_Entities/Tags_System#Scar и адресное лечение|Scar owner]] хранит конкретный Scar и объявленное embodied consequence. Health читает только действующие capacity-consequences; сам факт наличия Scar не снижает HP. `MaxCapacity` уже учитывает их: отдельного `ScarredCapacity` или `ScarredHP` нет, предыдущее имя максимума не сохраняется вторым параметром.

Для Scar с `permanent_capacity_loss` величина потери неотрицательна и принадлежит этому Scar. Health пересчитывает максимум из определения тела и всех ещё действующих постоянных последствий, затем сохраняет границы:

```text
MaxCapacity' = resolve(body_definition, active_permanent_consequences)
FieldCapacity' = min(FieldCapacity, MaxCapacity')
CurrentHP' = min(CurrentHP, FieldCapacity')
```

Resolver не выдаёт отрицательный максимум. Повтор одного source event не применяет Scar дважды. Источники и их вклад сохраняются раздельно; сумма capacity-loss не становится переносимой валютой или безличным pool. При удалении одного Scar пересчитывается его вклад, остальные Scar и постоянные последствия остаются. Повышение MaxCapacity само не заполняет FieldCapacity/CurrentHP; для этого нужна разрешённая медицина.

Например, при здоровом максимуме 100 конкретный Scar с потерей 10 даёт `MaxCapacity = 90`. При прежних `FieldCapacity = 100, CurrentHP = 95` значения ограничиваются до 90/90. После обычного возвращения максимум остаётся 90. Адресное лечение этого Scar может вернуть максимум к 100, если других постоянных причин потери нет; последующая медицина Хаба заполняет два остальных значения.

```yaml
health_contract:
  owner: HEALTH
  runtime_record: BodyID
  player_values: [MaxCapacity, FieldCapacity, CurrentHP]
  invariant: "0 <= CurrentHP <= FieldCapacity <= MaxCapacity"
  maximum_basis: body_definition_and_active_permanent_consequences
  permanent_loss_source: concrete_scar
  permanent_capacity_loss_target: MaxCapacity
  resolved_scar_capacity_effect: remove_only_source_loss_then_recalculate
  maximum_recalculation: source_scoped_idempotent
  after_maximum_change: [clamp_field_to_maximum, clamp_current_to_field]
  health_snapshot_update: atomic
  maximum_increase_fills_health: false
  ordinary_damage_target: CurrentHP
  ordinary_heal_ceiling: FieldCapacity
  field_medicine_ceiling: MaxCapacity
  lethal_resolution_owner: LIFECYCLE_RESOLVER
  hub_recovery_cost: free
  hub_recovery_requires: living_pawn_and_confirmed_hub_recovery_context
  hub_recovery_result: fill_field_and_current_to_current_maximum
  hub_recovery_removes_scar: false
  hub_recovery_restores_permanent_loss: false
  resurrection: false
```

## 3. Что именно восстанавливает помощь

```text
лечебный навык:  CurrentHP' = min(FieldCapacity, CurrentHP + restore)
полевая медицина: FieldCapacity' = min(MaxCapacity, FieldCapacity + restore_capacity)
```

Полевая медицина не заполняет `CurrentHP` автоматически. Поэтому даже удачная хирургическая процедура не стирает бой одним действием: союзнику всё ещё нужен навык, стимулятор, время или безопасный выход.

| Слой помощи | Результат | Типичная цена |
|:---|:---|:---|
| Стабилизация | прекращает bleed или иной объявленный медицинский drain | руки, время, уязвимость |
| Терапия | восстанавливает `CurrentHP` или стамину | предмет, короткое окно, уязвимость применения |
| Полевая медицина | ограниченно возвращает `FieldCapacity` и/или обслуживает тяжёлую травму | долгий Commitment, неподвижность, редкий предмет |
| Лечебная Q/E | восстанавливает только `CurrentHP` | батарея, Heat, Pulse, телеграф, Recovery |

## 4. Лечебные навыки и контригра

Лечебная Q/E, аура или область подчиняются тому же циклу `Condition -> Preparation -> Reveal -> Effect -> Recovery`, что и атака.

- нужен живой адресат, близость, линия либо удержание объявленной зоны;
- батарейный эффект создаёт Heat, Recovery и читаемый Pulse;
- проводник, линия, якорь или построение могут быть сорваны обычным боевым действием;
- лекарь не ведёт одновременно полный уронный цикл;
- лечение не снимает bleed, cripple, яд, Heat, Dissonance, чужой Recovery или уже разрешившуюся потерю `FieldCapacity`.

АоЕ и ауры имеют **один общий бюджет восстановления** на импульс, который делится между подходящими целями. На цели действует единый `restore_saturation`: повторный батарейный restore в коротком окне ослабляется либо даёт только заранее объявленную стабилизацию. Смена лекаря не обходит это правило.

Антилечение не обязано быть запретом «лечиться нельзя». Оно может уменьшать восстановление (`healing_suppression`) или дробить его на отложенные части (`restoration_fracture`). У каждого такого статуса есть телеграф, обычная контрмера и правило повторов в реестре статусов.

## 5. Локальный контракт помощи и расходника

Лечение не масштабируется универсальным RPG-атрибутом. Каждый параметр имеет одного конкретного владельца:

| Владелец | `owned_parameters` | Не владеет |
|:---|:---|:---|
| `HEALTH` / запись `BodyID` | разрешением `MaxCapacity / FieldCapacity / CurrentHP` по телесным источникам | величиной чужого лечения, Scar identity или ресурсной транзакцией Facility |
| Scar / Body по [[04_Player_Entities/Tags_System\|Tags System]] | конкретным Scar, его состоянием и embodied consequence | вторым расчётом здоровья или списанием входов услуги |
| `HeroKitID.ActionID` | authored-результатом `Race × Spec`: `restore_budget`, `pulse_count`, геометрия, Commitment, Pulse и Recovery | медицинским предметом, базовой стрельбой или чужой ёмкостью тела |
| `ConsumableID.Procedure` | дозой, `restore / restore_capacity`, временем применения, consume point и остатком | батарейным импульсом Q/E или постоянным бонусом владельца |
| `InventoryOwner` | размером стека, слотом, Ready Access и физической доступностью предмета | результатом процедуры после её начала |

Запись действия или предмета публикует значения в `owned_parameters`. Связь между ними допустима только как `source.property -> owner.parameter` в `downstream_edges`: один источник меняет один наблюдаемый результат, не получает владение им и платит одну цену в той же сцене. Увеличенный `pulse_count`, например, распределяет один общий `restore_budget` между импульсами либо прямо повышает объявленный батарейный расход/Exposure; он не увеличивает одновременно общий restore, радиус, длительность и безопасность.

`counterplay_now` называет немедленный ответ на сцене: прервать занятые руки, разорвать линию, вытолкнуть цель из области, сломать видимый якорь или дождаться объявленного насыщения. Ответ, существующий только после полного восстановления, контригрой не считается.

## 6. Восстановление в Хабе

После успешного возвращения живой Пешки базовая медицина и санитарная обработка бесплатны и автоматичны. Health применяет их к текущему максимуму тела:

```text
FieldCapacity = MaxCapacity
CurrentHP = MaxCapacity
```

Она снимает обычный полевой damage и recoverable trauma по их владельцам. Постоянные Scar, связанные потери MaxCapacity и иные permanent consequences сохраняются. Острое cantrip-состояние снимается по [[05_Combat_Survival/Magic_Batteries#5. Кантрипы|своему контракту]]; это не удаление Scar. Исход `Broken` и смерть не отменяются базовой медициной.

[[08_World_Generation/Hub/Hub_Services_Interaction#Адресное лечение Scar|Facility]] может предложить отдельное лечение подходящего Scar за объявленные реальные ресурсы. [[06_Economy_Loot/Barter_System#Адресная транзакция лечения Scar|RecipeTransaction]] подтверждает расход и результат; Scar/Body прекращает адресованное последствие, Health пересчитывает максимум. После успешной процедуры в Хабе обычный recovery может заполнить здоровье до нового MaxCapacity. Ни процедура, ни заполнение не меняют terminal outcome, Presence, readiness или Closure: их разрешают прежние lifecycle owners.

### UI здоровья

Карточка показывает `MaxCapacity`, `FieldCapacity`, `CurrentHP`, причины потерь и доступную контрмеру. Например: `Max Health: 90`, под ним `Burned Lung: -10 Max Health`. Это пояснение вклада конкретного Scar, не четвёртый постоянный stat. Functional Scar показывает своё функциональное последствие; UI не подставляет ему HP-loss. До платного лечения preview показывает, какой Scar и какой его вклад будут сняты; итоговые числа получает от Health.

## 7. Проверки прототипа

- один обычный размен не делает продолжение рейда математически неверным;
- тяжёлая травма остаётся читаемой причиной решить: рискнуть полевой медициной или эвакуироваться;
- один лекарь спасает окно, но не удерживает фокус-цель бесконечно;
- несколько лекарей не умножают одну батарею на весь сквад и не обходят saturation ротацией;
- соло может стабилизировать себя предметом, но не получает бесплатный групповой цикл;
- UI показывает три значения здоровья и конкретную причину потери, не добавляя отдельный Scar pool.

Точные объёмы восстановления, длительности, токсичность, радиусы и пороги остаются `prototype` до проверки слабого, обычного и оптимизированного сценариев.

## 4. Запреты

- колбы, гранаты, ловушки, химические зоны, световые шары и барьеры не существуют как обычные боевые расходники;
- боевой навык не требует медицинский предмет как второй платёж;
- расходник не создаёт новый P/Q/E или бесконечное восстановление по cooldown;
- доступ, карта и след не заменяют [[08_World_Generation/Generation/Gate_Check|Gate Check]], бой или обязательную экстракцию.
