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
  - "[[08_World_Generation/_Registries/Registry_Environment_States|Registry Environment States]]"
  - "[[09_Project_Management/Risk_Register|Risk Register]]"
---
# Реестр: грамматика и границы навыков

> Реестр классифицирует уже обоснованное действие. Он не легализует предмет, вещество, биологию или технологию одним названием типа.

## 1. Общий контракт и условные продолжения

```markdown
## Общая часть каждой P/Q/E
[skill_slot:: P | Q | E]
[kernel:: strike | deploy | alter | guard | traverse | treat | perceive | operate]
[window_function:: create | exploit | mitigate]
[effect_domain:: harm | displacement | state | restore | protection | information | interaction]
[delivery_form:: self | contact | projectile | thrown | placed | tether | field | channel | procedure]
[carrier_contract:: body | device | environment_node]
[supply_contract:: stamina | biological_reserve | battery_impulse | device_charge | local_material]
[effect_persistence:: instant | maintained | attached | anchored]
[target_scope:: self | single | line | cone | area | surface | device | environment_node]
[owned_parameters:: owner.parameter = value; ...]
[fixed_terms:: target_rule, geometry, loss_rule]
[fixed_debt:: telegraph, commitment, recovery]
[interrupt_rule:: none | interruptible | rule_id]
[counterplay_now:: response_id; ...]

## Только если это нужно типу
P: [passive_trigger:: event_id] [passive_state:: state_or_right_id]
   [passive_properties:: property_id; ...] [passive_loss_rule:: rule_id]
state/restore: [status_effect:: effect_id]
terminal/anchor/node: [carrier_fate:: retained | deployed] [carrier_ref:: registry_id]
   [required_interface:: interface_id] [placement_limit:: integer]
   [terminal_integrity:: declared] [uptime_contract:: battery | battery_and_terminal_health | channel_commitment]
   [reserve_id:: reserve_id] [reserve_capacity:: amount] [reserve_recovery:: rule_id]
   [depletion_rule:: rule_id] [retrieval_rule:: destroy_only | rule_id]
support: [support_family:: seal | signal | access | maintenance | expose]
   [support_polarity:: allied_buff | hostile_expose] [benefit_axis:: ingress | information | permission | sustain]
   [status_interaction:: named_effect_or_ingress_path] [stack_group:: family_id]
   [baseline_path:: named_non_support_option] [attribute_mutation:: forbidden]
downstream: [downstream_edges:: property -> consumer.parameter; ...]
energy variant: [energy_contract:: body | hybrid | device] [battery_version:: effect_id]
   [cantrip_version:: effect_id | none] [overcharge_version:: effect_id | none]
   [impulse_cost:: 0] [casting_reserve_required:: false]
```

`direct_damage`, `area_damage`, `crowd_control`, `buff_debuff`, `healing`, `mobility`, `defense` и `anomaly_procedure` больше не являются достаточными типами способности. При необходимости они выводятся как отчётные ярлыки из полного контракта.

## 2. Владение

| Слой | Владеет | Не владеет |
|:---|:---|:---|
| Combo / kernel | действием, геометрией, окном, телеграфом и Recovery | переносимым товаром и бесконечным payload |
| Локальный параметр | одним измеримым результатом своего доменного владельца | общим рейтингом человека, новым статусом или глаголом |
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

`restore`, `aura`, `area` и `buff` являются формами вывода из одного контракта, а не готовыми классами. Для поддержки обязательны `support_family`, `benefit_axis`, `baseline_path`, `uptime_contract`, `stack_group` и обычные поля источника, цели, доставки, долга и контригры.

- лечебный навык восстанавливает только `CurrentHP` по [[05_Combat_Survival/Combat_Consumables|контракту здоровья]];
- АоЕ и аура делят один общий `restore`-бюджет между целями;
- на цели действует общий `restore_saturation`, который не обходится сменой лекаря;
- `healing_suppression` уменьшает входящее восстановление, а `restoration_fracture` откладывает его части; оба имеют обычную контрмеру;
- способность может публиковать дискретный `pulse_count`, но то же свойство не увеличивает одновременно общий restore, радиус, длительность и безопасность;
- `attribute_mutation` всегда `forbidden`; поддержка не усиливает Frame и не превращает доступ к сцене в обязательный гейт;
- аура — пространственный терминал: для поставленного поля нужны батарея, граница, здоровье тотема, правило разрушения и `baseline_path`;
- `maintenance` удерживает только один объявленный собственный терминал; `expose` раскрывает активный механизм врага, не саму цель;
- владелец читает фазу и направление внешнего источника на минимальном личном HUD; противник читает источник, границу, фазу и ближайшую контригру без HUD владельца.

## 11. Боевой результат

`effect_domain: harm` не получает дополнительную билдовую ветку и не выбирается через модуль в Хабе. Запись способности объявляет собственные конечные параметры через `owned_parameters`; остальные определяющие параметры живут в `fixed_terms`.

- direct harm фиксирует геометрию, число целей, импульсы, частоту, помощь попаданию, контроль, антихил и батарейную эффективность;
- поле может иметь один изменяемый параметр границы **или** времени, но не одновременно усиливать direct harm на цель;
- длительный эффект может иметь один изменяемый параметр длительности, интервала либо заранее видимого числа импульсов, но не одновременно burst-harm и геометрию;
- одна причинная цепь не разрешает одновременно полный harm, охват, частоту, контроль, антихил и батарейную эффективность;
- параметры harm/radius и пороги TTK являются прототипными, пока не закрыт [[09_Project_Management/Risk_Register|R61]].
