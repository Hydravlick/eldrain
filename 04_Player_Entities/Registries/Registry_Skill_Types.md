---
status: active
system: player_entities_registry
registry_type: skill_grammar
tags:
  - database
  - mechanics
  - skill_grammar
  - capability_boundaries
related_files:
  - "[[04_Player_Entities/Skill_Build_Philosophy|Философия навыков и билдостроения]]"
  - "[[04_Player_Entities/Ability_Synergy|Ability Synergy]]"
  - "[[05_Combat_Survival/Registries/Registry_StatusEffects|Registry Status Effects]]"
  - "[[07_Gear_Inventory/Registries/Registry_Consumables|Registry Consumables]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic Batteries]]"
  - "[[08_World_Generation/Registries/Registry_Environment_States|Registry Environment States]]"
  - "[[09_Project_Management/Risk_Register|Risk Register]]"
type: registry
index_route: owner
index_group: player_entities
index_order: 50
index_summary: "Хранит схему и записи: Реестр: грамматика и границы навыков."
read_when: "Когда нужен контракт «Реестр: грамматика и границы навыков» и его границы с соседними владельцами."
---
# Реестр: грамматика и границы навыков

> Реестр классифицирует уже обоснованное действие. Он не легализует предмет, вещество, биологию или технологию одним названием типа.

## 1. Общий контракт и условные продолжения

Этот шаблон описывает только active Profile Actions Q/E. P использует [[04_Player_Entities/Tags_System#Общая semantic grammar P и Personal Trait|общую Trait rule grammar]] с deterministic Field Profile provenance; поля Action definition для неё не обязательны.

```markdown
## Общая часть активной Q/E
[skill_slot:: Q | E]
[kernel:: strike | deploy | alter | guard | traverse | treat | perceive | operate]
[window_function:: create | exploit | mitigate]
[effect_domain:: harm | displacement | state | restore | protection | information | interaction]
[delivery_form:: self | contact | projectile | thrown | placed | tether | field | channel | procedure]
[carrier_contract:: body | device | environment_node]
[supply_contract:: stamina | biological_reserve | full_battery | device_charge | local_material]
[effect_persistence:: instant | maintained | attached | anchored]
[target_scope:: self | single | line | cone | area | surface | device | environment_node]
[owned_parameters:: owner.parameter = value; ...]
[fixed_terms:: target_rule, geometry, loss_rule]
[fixed_debt:: telegraph, commitment, recovery]
[interrupt_rule:: none | interruptible | rule_id]
[counterplay_now:: response_id; ...]

## Только если это нужно типу
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
   [battery_source_required:: false | true] [battery_service_ref:: service_contract_id when true]
```

`full_battery` требует `battery_source_required: true` и ссылку на физическую процедуру. `reserve_*` описывают только явно объявленный телесный/терминальный ресурс, не Casting Reserve, не Battery и не общий weapon ammo. Полная battery-powered активация разряжает ровно один physical ItemID по [[05_Combat_Survival/Magic_Batteries|battery transaction]].

`direct_damage`, `area_damage`, `crowd_control`, `buff_debuff`, `healing`, `mobility`, `defense` и `anomaly_procedure` больше не являются достаточными типами способности. При необходимости они выводятся как отчётные ярлыки из полного контракта.

## 2. Владение

См. [[04_Player_Entities/Skill_Execution#2. Владение]].

## 3. Закон исполнения

См. [[04_Player_Entities/Skill_Execution#3. Закон исполнения]].

## 4. Границы спорных возможностей

См. [[04_Player_Entities/Skill_Execution#4. Границы спорных возможностей]].

## 5. Движение

См. [[04_Player_Entities/Skill_Execution#5. Движение]].

## 6. Оружейный контур

См. [[04_Player_Entities/Skill_Execution#6. Оружейный контур]].

## 7. Иллюстративные контракты

Ниже показана только грамматика; записи не утверждают контент.

### Направленное терминальное состояние

```text
kernel: alter
effect_domain: state
delivery_form: tether
carrier_contract: device
supply_contract: full_battery
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
supply_contract: full_battery
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
supply_contract: full_battery
carrier_fate: retained
effect_persistence: maintained
target_scope: environment_node
required_interface: anomaly_rule_id
carrier_ref: example_anomaly_procedure_device
energy_contract: device
battery_source_required: true
battery_service_ref: declared_service_contract
```

Универсального «редактирования реальности» нет. Каждая процедура публикует конкретное правило узла. ID с префиксом `example_` показывает форму, но не проходит в `approved`: реальная запись обязана ссылаться на зарегистрированное устройство.

## 8. Энергетический контракт

См. [[04_Player_Entities/Skill_Execution#8. Энергетический контракт]].

## 9. Проверки

См. [[04_Player_Entities/Skill_Execution#9. Проверки]].

## 10. Поддержка, восстановление и импульсы

См. [[04_Player_Entities/Skill_Execution#10. Поддержка, восстановление и импульсы]].

## 11. Боевой результат

См. [[04_Player_Entities/Skill_Execution#11. Боевой результат]].

