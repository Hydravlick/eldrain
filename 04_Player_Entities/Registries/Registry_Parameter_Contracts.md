---
status: active
system: parameter_contracts
tags:
  - parameter_contracts
  - buildcraft
  - ownership
  - modifiers
  - debt
related_files:
  - "[[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile Pipeline]]"
  - "[[04_Player_Entities/Skill_Build_Philosophy|Философия навыков и билдостроения]]"
  - "[[05_Combat_Survival/Magic_Batteries|Магия и батареи]]"
  - "[[05_Combat_Survival/Dissonance_System|Диссонанс]]"
  - "[[07_Gear_Inventory/Thermos_Assembly|Thermos Assembly]]"
  - "[[07_Gear_Inventory/Registries/Registry_Thermos_Interfaces|Thermos Interfaces]]"
type: registry
index_route: owner
index_group: player_entities
index_order: 30
index_summary: "Хранит схему и записи: Реестр параметрических контрактов."
read_when: Когда нужен контракт «Реестр параметрических контрактов» и его границы с соседними владельцами.
---
# Реестр параметрических контрактов

> Реестр нормализует **право менять результат**, а не хранит значения всех предметов, навыков и тел. Он не вводит общий stat-sheet и не становится вторым TOUCH: конкретное значение по-прежнему живёт у своего тела, Frame, действия, батареи, модуля или состояния.

## Контракт записи

```markdown
[parameter_contract_id:: stable_id]
[parameter_domain:: named_result_domain]
[domain_owner:: canonical_resolver | MISSING_OWNER]
[base_source:: body | frame_action | hero_kit_action | gear | state]
[authorized_requesters:: source_family; ...]
[resolution_order:: identity_base -> gear -> state -> authorized_modifier_contracts]
[allowed_operations:: add | replace_by_declared_rule | clamp_by_domain_policy]
[intrinsic_debt_required:: yes]
[does_not_own:: source values | unrelated parameter domains | global rating]
[status:: active | pending]
```

`trait_rule` обозначает одну semantic grammar P/Personal Trait; provenance указывает Field Profile или конкретную Пешку. Авторизация остаётся узкой: происхождение не расширяет разрешённые targets. Порядок разрешения в записи исполняет только названный доменный owner; Combat Profile читает результат.

Общая авторизация запроса: [[04_Player_Entities/Skill_Build_Philosophy#Авторизация запроса параметра]]. Записи указывают доменного владельца и его bounded policy.

## Активные домены

### `frame_native_action`
Стабильный ключ сохранён для совместимости ссылок. После weapon identity cutover он обозначает параметр операции Pattern; он не возвращает `Frame.NativeAction` как владельца moveset или текущего Recovery.

[parameter_contract_id:: frame_native_action]
[parameter_domain:: один конечный параметр операции конкретного оружейного Pattern]
[domain_owner:: [[05_Combat_Survival/Weapon_Core|Weapon Core]]]
[base_source:: pattern_operation_definition]
[authorized_requesters:: installed_module; trait_rule; declared_state]
[resolution_order:: identity_base -> gear -> state -> authorized_modifier_contracts]
[allowed_operations:: add | replace_by_declared_rule | clamp_by_domain_policy]
[intrinsic_debt_required:: yes]
[does_not_own:: P/Q/E result | global damage | all-frame gunfeel]
[status:: active]

### `hero_kit_action`
[parameter_contract_id:: hero_kit_action]
[parameter_domain:: один конечный параметр конкретного активного Q/E действия]
[domain_owner:: [[04_Player_Entities/Skill_Build_Philosophy|Философия навыков и билдостроения]]]
[base_source:: hero_kit_action]
[authorized_requesters:: installed_module; trait_rule; declared_state]
[resolution_order:: identity_base -> gear -> state -> authorized_modifier_contracts]
[allowed_operations:: add | replace_by_declared_rule | clamp_by_domain_policy]
[intrinsic_debt_required:: yes]
[does_not_own:: weapon Pattern operations | status policy | generic substat]
[status:: active]

### `dissonance_occurrence`
[parameter_contract_id:: dissonance_occurrence]
[parameter_domain:: один physical Dissonance occurrence и его вклад в RecentDissonancePulse]
[domain_owner:: [[05_Combat_Survival/Dissonance_System|Диссонанс]]]
[base_source:: declared_physical_action_or_state]
[authorized_requesters:: frame_action; hero_kit_action; device; backlash; declared_environment_or_status]
[resolution_order:: identity_base -> gear -> state -> authorized_modifier_contracts]
[allowed_operations:: replace_by_declared_rule | clamp_by_domain_policy]
[intrinsic_debt_required:: yes]
[does_not_own:: acoustic event | second pulse for battery quality | action damage]
[status:: active]

### `status_application_policy`
[parameter_contract_id:: status_application_policy]
[parameter_domain:: application, repeat and conflict policy конкретного status effect]
[domain_owner:: MISSING_OWNER]
[base_source:: declared_status_effect]
[authorized_requesters:: declared_delivery_source]
[resolution_order:: identity_base -> gear -> state -> authorized_modifier_contracts]
[allowed_operations:: replace_by_declared_rule | clamp_by_domain_policy]
[intrinsic_debt_required:: yes]
[does_not_own:: status values of every effect | action result | environmental instance]
[status:: pending]

> [!warning] MISSING_OWNER
> [[05_Combat_Survival/Registries/Registry_StatusEffects|Реестр статус-эффектов]] хранит записи эффектов и их повторяемость, но не объявлен универсальным runtime-resolver. До появления отдельного владельца новые источники не получают право локально изобретать priority, floor или cap для статусов.

### `ballistic_coverage_binding`
[parameter_contract_id:: ballistic_coverage_binding]
[parameter_domain:: pattern-bound collider coverage, seam and soft-layer binding установленного защитного модуля]
[domain_owner:: [[05_Combat_Survival/Ballistics_Armor|Ballistics Armor]]]
[base_source:: body_surface]
[authorized_requesters:: installed_plate_pattern]
[resolution_order:: body surface -> committed assembly coverage bindings -> current module condition]
[allowed_operations:: replace_by_declared_rule | clamp_by_domain_policy]
[intrinsic_debt_required:: yes]
[does_not_own:: mount legality | ItemID custody | general damage reduction | Thermos service capacity]
[status:: active]

### `physical_carry_envelope`
[parameter_contract_id:: physical_carry_envelope]
[parameter_domain:: локальный SustainedCarryLimit конкретного тела]
[domain_owner:: [[07_Gear_Inventory/Physical_Weight|Physical Weight]]]
[base_source:: body]
[authorized_requesters:: selected_installed_body_interface; personal_tag; declared_injury_state]
[resolution_order:: body base -> selected gear interface -> injury/state -> authorized modifier contracts]
[allowed_operations:: add | replace_by_declared_rule | clamp_by_domain_policy]
[intrinsic_debt_required:: yes]
[does_not_own:: Item mass | Ready Access slots | Back Slot | assembly legality]
[status:: active]

### Resource state boundary

`battery_state` принадлежит [[05_Combat_Survival/Magic_Batteries|Magic Batteries]], `magazine_current` — [[05_Combat_Survival/Weapon_Ranged|Weapon Ranged]] конкретного ItemID. Capacity и consumption определяет Pattern. Это ресурсные состояния/definition fields, а не новые разрешения произвольных modifiers. Battery transaction не является requester параметров каждого выстрела.

Superseded `prepared_battery_queue_capacity` снят с активной публикации без замещающего бонуса. Ни модуль, ни аффикс не получают право вернуть очередь или внутренний счётчик батареи.

## Thermos-домены без владельца

До появления отдельного ParameterContract следующие concept outputs остаются `MISSING_OWNER` и не могут перевести модуль в `installable`:

- точность powered-tool и удержание heavy-tool;
- post-impact stability и soft-layer impact tolerance;
- перенос Heat между телом и Термосом;
- раннее чтение локального сигнала среды;
- сокращение device-interaction time;
- изменение overload threshold и тяжести cantrip backlash;
- injury threshold и false-positive heat warnings.
- итоговая средовая защита установленной сборки и её связь с Gate/Survival resolution.

Thermos Assembly не создаёт временный локальный resolver для этих пробелов.

## Инварианты

Каждая policy применяется единственным доменным владельцем. [[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile]] читает результат и причины отказа; он не применяет этот порядок повторно и не становится resolver сборки.
