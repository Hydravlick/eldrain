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
[delivery_form:: self | contact | projectile | thrown | placed | tether | field | channel | procedure]
[carrier_contract:: body | device | environment_node]
[supply_contract:: stamina | biological_reserve | battery_impulse | device_charge | local_material]
[carrier_fate:: retained | deployed]
[effect_persistence:: instant | maintained | attached | anchored]
[target_scope:: self | single | line | cone | area | surface | device | environment_node]
[required_interface:: none | interface_id]
[carrier_ref:: none | registry_id]
[consume_amount:: none]
[consumption_point:: none]
[depletion_rule:: none | rule_id]
[retrieval_rule:: none | destroy_only | rule_id]
[economic_output:: none | nonextractable]
[placement_limit:: none | integer]
[reserve_id:: none | reserve_id]
[reserve_capacity:: none | amount]
[reserve_recovery:: none | rule_id]
[nonextractable:: true | false]
[payload_family:: none]
[status_effect:: none | effect_id]
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
| Combo / kernel | действием, геометрией, окном, телеграфом и Recovery | переносимым товаром и бесконечным payload |
| T.O.U.C.H.-компонент | одной измеримой осью действия | новым статусом или глаголом |
| Passive | одним состоянием с общим trigger и loss rule | несколькими независимыми двигателями |
| Frame | хватом, линией, сектором, пределом, оружейным обязательством и native Frame Window | новым P/Q/E, доставкой Q/E и универсальной защитой от Exposure |
| Медицинский предмет | телесной процедурой, дозой и уязвимым применением | топливом боевого навыка |
| Device | корпусом, зарядом и удержанием сложного эффекта | существованием без слота и отказа |
| Status Registry | buildup, последствием, repeat rule и counter action | источником вещества |
| Culture / technology | причинностью знания и доступностью процедуры | расовой монополией на общий инструмент |

## 3. Закон исполнения

Полный боевой навык исполняется через `body`, `device` или `environment_node` и питается батареей. Он может создать временное поле, tether, якорное состояние, барьер или статус, но результат обязан быть `nonextractable: true` и не становится предметом, веществом либо товаром.

```text
battery_impulse + declared_executor -> temporary_nonextractable_effect
```

| Исполнитель | Обязательные поля | Запрет |
|:---|:---|:---|
| `device` | `carrier_ref`, `placement_limit` при якоре, `retrieval_rule` | существование без слота, отказа и контригры |
| `body` | `reserve_*` для телесной версии, `nonextractable: true` | извлекаемый или передаваемый товар |
| `environment_node` | `carrier_ref`, `required_interface`, `depletion_rule` | перенос или продажа authored-ресурса |

- батарея не создаёт переносимую материю, но исполняет временное записанное состояние;
- медрасходники применяются самостоятельным действием и не входят в контракт Q/E;
- длительный эффект объявляет якорь, предел, прерывание и правило прекращения;
- `device` занимает слот, имеет заряд/предел размещения и отказ;
- Frame не является исполнителем или доставкой P/Q/E; его `skill_interfaces` принадлежат только native оружейным действиям.

## 4. Границы спорных возможностей

| Возможность | Статус | Обязательный контракт |
|:---|:---|:---|
| Наложить состояние через оружие | `FRAME-NATIVE` | физическое последствие конкретного оружейного действия, его попадания и собственной контригры; это не Q/E Combo |
| Создать брошенное состояние | `COMPATIBLE` | батарейный импульс, видимая дуга, не извлекаемое поле и предел якоря; это не колба |
| Поставить ловушку или зону | `COMPATIBLE` | объявленный якорь, время установки, видимость, прерывание и предел размещения; это не расходуемый корпус |
| Лечить | `COMPATIBLE` | `effect_domain: restore`, батарея, живой адресат, телеграф, Recovery; восстанавливает только `CurrentHP` |
| Создать барьер | `COMPATIBLE` | устройство или телесный исполнитель, батарея, поддержание или правило якоря; без исполнителя/энергии поле прекращается |
| Работать с правилом Аномалии | `COMPATIBLE` | конкретный узел, устройство, канал, источник, телеграф, Recovery и исход прерывания |
| Материализовать переносимый яд, колбу, мину или лекарство кнопкой | `CONFLICT` | P/Q/E не создаёт товар; разрешён только временный не извлекаемый эффект |

Эти строки являются границами возможностей, а не готовыми P/Q/E или предметами.

## 5. Движение

Способность не переносит тело через пространство и не выбирает маршрут за игрока. Она может изменить одну цену, форму или доступ к физически читаемому движению.

Без способности тот же маршрут остаётся доступен обычному телу, если только authored-среда не предоставляет отдельный физический интерфейс. Мгновенный dash, teleport, отмена коллизии, автоматическая неуязвимость и escape без остаточного Recovery не являются базовым разрешением `traverse`.

## 6. Оружейный контур

Frame может предоставить внутренний интерфейс оружейного действия:

```text
edge | point | impact_surface | contact_surface | brace | conduit | projectile | reach | free_hand
```

Эти интерфейсы принадлежат native Frame Window, а не полному контракту P/Q/E. При смене Frame меняется оружейное давление и его обязательство; уже выбранные Q/E сохраняют свою форму, цель, источник, телеграф и контригру без изменений.

## 7. Иллюстративные контракты

Ниже показана только грамматика; записи не утверждают контент.

### Направленное терминальное состояние

```text
kernel: alter
effect_domain: state
delivery_form: tether
carrier_contract: device
supply_contract: battery_impulse
carrier_fate: retained
effect_persistence: attached
target_scope: single
required_interface: utility_focus
carrier_ref: example_utility_focus
economic_output: nonextractable
nonextractable: true
status_effect: terminal_condition
```

Способность владеет процедурой направленного состояния и выпускает её через собственный фокус. Оружие может создать для неё окно, но не доставляет её до цели; батарея оплачивает полный импульс. Никакая ампула или переносимый реагент не создаётся.

### Бросок якорного состояния

```text
kernel: deploy
effect_domain: state
delivery_form: thrown
carrier_contract: device
supply_contract: battery_impulse
carrier_fate: deployed
effect_persistence: anchored
target_scope: area
carrier_ref: equipped_focus
placement_limit: 1
economic_output: nonextractable
nonextractable: true
status_effect: anchored_condition
```

Навык не создаёт колбу и не выбирает любой статус из реестра. Он выпускает одну заранее объявленную временную запись через фокус; поле прекращается по правилу якоря или прерывания.

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

Тело даёт действие; Frame может создать отдельное оружейное окно, но не меняет эту утилиту в лечение, яд или дальний контроль.

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
- батарея является единственным внешним расходом полной энергетической версии; Q/E не требует второго payload-предмета;
- кантрип не производит предмет, лекарство, батарею или извлекаемую ценность.

Для Догмата каждая активная способность имеет `cantrip_version`. У других практик отдельная Combo может получить ситуативный кантрип или оставить `[cantrip_version:: none]`.

## 9. Проверки

- исполнитель и батарейный источник объявлены до Commitment;
- временный эффект не превращается в предмет, товар или второй расход;
- длительный статус имеет обычный не-скилловый ответ;
- Frame не исполняет и не доставляет Q/E; он создаёт только собственное оружейное окно;
- в графе Passive/Q/E/weapon/status нет положительного замкнутого цикла;
- способность не создаёт извлекаемый или перерабатываемый предмет;
- культура объясняет процедуру, но не запрещает другим народам изучить общий инструмент.

## 10. Поддержка, восстановление и импульсы

`restore`, `aura`, `area` и `buff` являются формами вывода из контракта, а не готовыми классами. Направленный импульс, tether, аура, якорная область и бафф имеют разные геометрию, батарейную цену и контригру.

- лечебный навык восстанавливает только `CurrentHP` по [[05_Combat_Survival/Combat_Consumables|контракту здоровья]];
- АоЕ и аура делят один общий `restore`-бюджет между целями;
- на цели действует общий `restore_saturation`, который не обходится сменой лекаря;
- `healing_suppression` уменьшает входящее восстановление, а `restoration_fracture` откладывает его части; оба имеют обычную контрмеру;
- T.O.U.C.H. может менять `pulse_count` по формуле `floor`, но тот же компонент не увеличивает одновременно общий restore, радиус, длительность и безопасность.
