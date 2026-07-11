---
type: registry
status: active
system: player_entities_registry
registry_type: skill_grammar
tags: [database, mechanics, skill_grammar, capability_boundaries]
related_files:
  - "[[04_Player_Entities/Skill_Build_Philosophy|Философия навыков и билдостроения]]"
  - "[[04_Player_Entities/Ability_Synergy|Ability Synergy]]"
  - "[[05_Combat_Survival/_Registries/Registry_StatusEffects|Registry Status Effects]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Consumables|Registry Consumables]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic Batteries]]"
---
# Реестр: грамматика и границы навыков

> Реестр классифицирует уже обоснованное действие. Он не легализует предмет, вещество, биологию или технологию одним названием типа.

## 1. Полный контракт

```markdown
[skill_slot:: P | Q | E]
[kernel:: strike | deploy | alter | guard | traverse | treat | perceive | operate]
[window_function:: create | exploit | mitigate]
[effect_domain:: harm | displacement | state | restore | protection | information | interaction]
[delivery_form:: self | contact | weapon_bound | projectile | thrown | placed | tether | field | channel | procedure]
[carrier_contract:: body | current_frame | consumable | device | environment_node]
[supply_contract:: stamina | biological_reserve | battery_impulse | item_charge | device_charge | local_material]
[carrier_fate:: retained | consumed | deployed]
[effect_persistence:: instant | maintained | attached | anchored]
[target_scope:: self | single | line | cone | area | surface | device | environment_node]
[required_interface:: none | interface_id]
[compatible_frames:: none | any_with_interface | frame_id; frame_id]
[carrier_ref:: none | registry_id | equipped_frame]
[consume_amount:: none | amount_and_unit]
[consumption_point:: none | commitment | release | placement | maintenance]
[depletion_rule:: none | rule_id]
[retrieval_rule:: none | destroy_only | rule_id]
[economic_output:: none | nonextractable]
[placement_limit:: none | integer]
[reserve_id:: none | reserve_id]
[reserve_capacity:: none | amount]
[reserve_recovery:: none | rule_id]
[nonextractable:: true | false]
[payload_family:: none | family_id]
[status_effect:: none | effect_id | from_carrier]
[output_properties:: final_parameter; final_parameter; ...]
[passive_trigger:: none | event_id]
[passive_state:: none | state_or_right_id]
[passive_properties:: none | property_id; property_id; property_id]
[passive_loss_rule:: none | rule_id]
[touch_components:: TOUCH -> final_parameter @weight; ...]
[fixed_terms:: target_rule, geometry, loss_rule]
[fixed_debt:: telegraph, commitment, recovery]
[interrupt_rule:: rule_id]
[counterplay:: response_id]
[downstream_edges:: property -> consumer.parameter; ... | none]
[energy_contract:: body | hybrid | device]
[battery_version:: effect_id | none]
[cantrip_version:: effect_id | none]
[overcharge_version:: effect_id | none]
[impulse_cost:: 0]
[casting_reserve_required:: false]
```

`direct_damage`, `area_damage`, `crowd_control`, `buff_debuff`, `healing`, `mobility`, `defense` и `anomaly_procedure` больше не являются достаточными типами способности. При необходимости они выводятся как отчётные ярлыки из полного контракта.

## 2. Владение

| Слой | Владеет | Не владеет |
|:---|:---|:---|
| Combo / kernel | действием, геометрией, окном, телеграфом и Recovery | материей и бесконечным payload |
| T.O.U.C.H.-компонент | одной измеримой осью действия | новым статусом или глаголом |
| Passive | одним состоянием с общим trigger и loss rule | несколькими независимыми двигателями |
| Frame | хватом, линией, сектором, пределом и оружейным обязательством | реагентом и новой Q/E |
| Consumable / payload | веществом, дозой, весом и экономическим расходом | бесконечным восстановлением по cooldown |
| Device | корпусом, зарядом и удержанием сложного эффекта | существованием без слота и отказа |
| Status Registry | buildup, последствием, repeat rule и counter action | источником вещества |
| Culture / technology | причинностью знания и доступностью процедуры | расовой монополией на общий инструмент |

## 3. Закон материальности

Если после способности остаётся вещество или объект, он должен быть физически оплачен. `carrier_fate` описывает судьбу носителя, а `effect_persistence` — длительность доставленного эффекта; эти оси не заменяют друг друга.

```text
persistent_or_transferable_output <= consumed_or_depleted_or_committed_physical_input
```

`committed` означает физический корпус, перенесённый из инвентаря в мир и занятый до честного снятия, разрушения или потери. `carrier_ref`, количество и точка списания позволяют проверить не только художественную правдоподобность, но и экономику вылазки. Локальный материал не переносится Пешкой: он существует в authored-узле и исчерпывается по `depletion_rule`.

| Carrier tuple | Обязательные поля | Запрет |
|:---|:---|:---|
| `consumable + item_charge + consumed` | `carrier_ref`, `consume_amount`, `consumption_point`, `payload_family` | бесплатное восстановление по cooldown |
| `current_frame + retained` | `carrier_ref`, `required_interface != none`, `compatible_frames` | интерфейс, которого нет у Frame |
| `environment_node + local_material` | `carrier_ref`, `required_interface`, `depletion_rule` | перенос или продажа добытого кнопкой материала |
| `body + biological_reserve` | `reserve_id`, `reserve_capacity`, `reserve_recovery`, `consume_amount`, `consumption_point`, `nonextractable: true` | извлекаемый или передаваемый товар |
| `device + deployed` | `carrier_ref`, `placement_limit`, `depletion_rule`, `retrieval_rule` | бесконечные размещённые корпуса или бесплатное снятие |

- `consumable` расходуется в объявленной точке Commitment/Release;
- `device` занимает слот, имеет заряд, предел размещения и отказ;
- `current_frame` предоставляет только заявленный интерфейс;
- `body` может дать подтверждённый биологический носитель, но не создаёт извлекаемый товар;
- `environment_node` существует только в конкретной сцене;
- батарея питает эффект, но не создаёт материю.

## 4. Границы спорных возможностей

| Возможность | Статус | Обязательный контракт |
|:---|:---|:---|
| Покрыть оружие ядом или коррозионным составом | `COMPATIBLE` | подготовленная доза или резервуар; совместимая поверхность; занятые руки; расход; статус проходит через рану, дыхание или интерфейс |
| Бросить колбу с состоянием | `COMPATIBLE` | физическая колба или заряд аппарата; видимая дуга; расход; payload из узкой семьи; статус из реестра |
| Поставить ловушку | `COMPATIBLE` | корпус или локальный объект; время установки; видимость; разрушение; лимит размещения; невозвращаемый расход либо честное снятие |
| Создать химическую зону | `COMPATIBLE` | объём происходит из количества вещества; зона не производит реагент и прекращается по материальному правилу |
| Лечить или восстанавливать структуру | `UNDERDEFINED` | стабилизация возможна телом/практикой; восстановление требует лекарства, материала либо специализированного устройства; полноценный батарейный медицинский контракт ещё не утверждён |
| Создать физический или энергетический барьер | `COMPATIBLE` | панель/щит/локальный материал либо `current_frame`/`device` с интерфейсом фокуса + батарея + поддержание; без носителя поле прекращается |
| Работать с правилом Аномалии | `COMPATIBLE` | конкретный узел, устройство, канал, источник, телеграф, Recovery и исход прерывания |
| Материализовать яд, колбу, мину или лекарство кнопкой | `CONFLICT` | cooldown не является материей; действие запрещено без физического носителя |

Эти строки являются границами возможностей, а не готовыми P/Q/E или предметами.

## 5. Движение

Способность не переносит тело через пространство и не выбирает маршрут за игрока. Она может изменить одну цену, форму или доступ к физически читаемому движению.

Без способности тот же маршрут остаётся доступен обычному телу, если только authored-среда не предоставляет отдельный физический интерфейс. Мгновенный dash, teleport, отмена коллизии, автоматическая неуязвимость и escape без остаточного Recovery не являются базовым разрешением `traverse`.

## 6. Frame-context

Frame может предоставить публичный интерфейс:

```text
edge | point | impact_surface | contact_surface | brace | conduit | projectile | reach | free_hand
```

При смене Frame сохраняются:

- ядро и семейство результата;
- primary window function;
- правило цели;
- источник payload;
- базовая контр-игра.

Если игроку нужно заново учить, что делает Q/E, это не Frame-context, а скрытая альтернативная способность.

## 7. Иллюстративные контракты

Ниже показана только грамматика; записи не утверждают контент.

### Нанесение подготовленного состава

```text
kernel: alter
effect_domain: state
delivery_form: weapon_bound
carrier_contract: consumable
supply_contract: item_charge
carrier_fate: consumed
effect_persistence: attached
target_scope: surface
required_interface: contact_surface
compatible_frames: any_with_interface
carrier_ref: prepared_contact_dose
consume_amount: 1 dose
consumption_point: commitment
economic_output: none
payload_family: contact_toxin
status_effect: from_carrier
```

Способность владеет процедурой нанесения. Ампула владеет веществом. Frame владеет способом доставить покрытую поверхность до цели.

### Бросок подготовленной колбы

```text
kernel: deploy
effect_domain: state
delivery_form: thrown
carrier_contract: consumable
supply_contract: item_charge
carrier_fate: consumed
effect_persistence: anchored
target_scope: area
carrier_ref: prepared_condition_flask
consume_amount: 1 flask
consumption_point: release
economic_output: none
payload_family: thrown_condition_medium
status_effect: from_carrier
```

Навык не создаёт колбу и не выбирает любой статус из реестра. Носители принадлежат одной заранее объявленной семье результата.

### Телесный перехват

```text
kernel: guard
effect_domain: protection
delivery_form: contact
carrier_contract: body
supply_contract: stamina
carrier_fate: retained
effect_persistence: instant
target_scope: self
```

Тело даёт действие; текущий Frame может предоставить `brace` или `impact_surface`, но не меняет его в лечение, яд или дальний контроль.

### Аномальная процедура

```text
kernel: operate
effect_domain: interaction
delivery_form: procedure
carrier_contract: device
supply_contract: battery_impulse
carrier_fate: retained
effect_persistence: maintained
target_scope: environment_node
required_interface: anomaly_rule_id
carrier_ref: example_anomaly_procedure_device
energy_contract: device
impulse_cost: 1
casting_reserve_required: true
```

Универсального «редактирования реальности» нет. Каждая процедура публикует конкретное правило узла. ID с префиксом `example_` показывает форму, но не проходит в `approved`: реальная запись обязана ссылаться на зарегистрированное устройство.

## 8. Энергетический контракт

- `body` работает от тела, стамины или подтверждённого биологического резерва;
- `hybrid` использует батарею по умолчанию и допускает кантрип только при прямой записи;
- `device` требует физический аппарат и источник;
- `impulse_cost` списывается из подготовленного Casting Reserve;
- кантрип не производит предмет, лекарство, батарею или извлекаемую ценность.

Для Догмата каждая активная способность имеет `cantrip_version`. У других практик отдельная Combo может получить ситуативный кантрип или оставить `[cantrip_version:: none]`.

## 9. Проверки

- payload физически существует до Commitment;
- источник, доставка и эффект не принадлежат одной бесплатной кнопке;
- длительный статус имеет обычный не-скилловый ответ;
- Frame не меняет семейство результата или payload;
- в графе Passive/Q/E/weapon/status нет положительного замкнутого цикла;
- способность не создаёт извлекаемый или перерабатываемый предмет;
- культура объясняет процедуру, но не запрещает другим народам изучить общий инструмент.
