---
type: registry
status: active
index_route: owner
index_group: factions_societies
index_order: 20
index_summary: "Задаёт правила и последствия системы «Реестр игровых интерфейсов фракций»."
read_when: "Читайте при изменении входов, состояний, стоимости или последствий системы «Реестр игровых интерфейсов фракций»."
system: factions
tags:
  - registry
  - faction_interfaces
  - source_of_truth
related_files:
  - "[[09_Project_Management/Architecture_MVP|Архитектура MVP]]"
  - "[[09_Project_Management/Lore_Gameplay_Boundary_Refactor_Plan_2026-07-23|План границы лора и механики]]"
  - "[[03_Factions_Societies/_Registries/Registry_Factions|Реестр фракций]]"
---
# Реестр игровых интерфейсов фракций

> [!important] Ответственность
> Реестр связывает сущность фракции с отдельным игровым взаимодействием. Он не хранит историю института и не разрешает eligibility, стоимость, состояние, награду или failure handling: эти правила принадлежат странице из `mechanic_owner_ref`.

> [!warning] Статус покрытия
> Контракт реестра активен, но мигрированы только явно записанные взаимодействия. Отсутствие строки не означает отсутствия интерфейса; до профильного owner-аудита покрытие считается неполным.

## Гранулярность

- Одна запись соответствует одному самостоятельному взаимодействию.
- Один `faction_id` может иметь любое число записей.
- Одна запись содержит ровно одну роль и один `mechanic_owner_ref`.
- `dependency_refs` перечисляет потребителей или поставщиков фактов, но не создаёт совладельцев.
- Если механический владелец не найден, используется `MISSING_OWNER`.
- Лорная страница не становится временным владельцем правила.

## Допустимые роли

| Роль | Участие сущности | Граница |
|---|---|---|
| `ADDRESS` | Принимает проблему и направляет её к системе или исполнителю. | Не рассчитывает результат. |
| `ISSUER` | Выступает внутриигровой стороной контракта. | Не владеет lifecycle контракта, наградой или системными состояниями. |
| `PROVIDER` | Диегетически предоставляет услугу. | Не определяет eligibility, стоимость или эффект. |
| `WITNESS` | Подтверждает один ограниченный факт. | Не выводит глобальную вину, доступ или итоговое состояние. |
| `PRESENTER` | Показывает уже рассчитанное состояние. | Не создаёт и не изменяет его. |
| `CONSUMER` | Получает системный результат для собственной институциональной процедуры. | Не пересчитывает решение владельца. |

## Контракт записи

Каждая запись использует отдельный заголовок `### <interface_id>` и следующие inline-поля:

```text
[interface_id:: stable.unique.id]
[faction_id:: existing_faction_id]
[interface_status:: planned|active|deprecated]
[role:: ADDRESS|ISSUER|PROVIDER|WITNESS|PRESENTER|CONSUMER]
[input_family:: one_bounded_problem_or_input]
[player_verb:: one_human_readable_action]
[result_family:: one_player_visible_result_family]
[mechanic_owner_ref:: root-relative wikilink|MISSING_OWNER]
[dependency_refs:: zero_or_more_root-relative_wikilinks]
[presentation_ref:: root-relative wikilink|MISSING_PRESENTATION]
[minimum_boundary:: minimum fact or commitment passed across the interface]
[does_not_own:: explicit excluded authority]
```

`interface_id` остаётся стабильным при переименовании отображаемого текста. Поля не содержат формул, resolver-порядка или пересказа исключений владельца.

## Проверка миграции

- Каждый `faction_id` существует в [[03_Factions_Societies/_Registries/Registry_Factions|Registry_Factions]].
- Каждый `interface_id` уникален.
- У каждой `active`-записи существует ровно один `mechanic_owner_ref`, отличный от `MISSING_OWNER`.
- Пара `faction_id + role + player_verb` не продублирована без отдельного результата или границы.
- `does_not_own` не пуст.
- Ссылочная проекция на лорной странице не повторяет правила владельца.
- Удаление игрового раздела из лорной страницы выполняется только после переноса правила к owner и создания соответствующей записи здесь.

## Active interfaces

### first_reception.continuity_admission_presentation

[interface_id:: first_reception.continuity_admission_presentation]
[faction_id:: first_reception]
[interface_status:: active]
[role:: PROVIDER]
[input_family:: named living candidate after ContinuityAdmissionAllowed]
[player_verb:: accept the offered person]
[result_family:: civic presentation after Spawn Logic creates one Ready Ward]
[mechanic_owner_ref:: [[04_Player_Entities/Spawn_Logic|Spawn Logic]]]
[dependency_refs:: [[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]]]
[presentation_ref:: [[03_Factions_Societies/Lore/The_First_Reception|The First Reception]]]
[minimum_boundary:: a named living candidate, the roster's admission predicate and one already resolved Ready Ward]
[does_not_own:: PawnID creation, continuity epoch, readiness resolution, welfare eligibility, tag assignment or lifecycle settlement]

### first_reception.first_return_presentation

[interface_id:: first_reception.first_return_presentation]
[faction_id:: first_reception]
[interface_status:: active]
[role:: PRESENTER]
[input_family:: already_resolved_manifestation_result]
[player_verb:: learn what the Ward has manifested]
[result_family:: civic acknowledgement of an already revealed personal property]
[mechanic_owner_ref:: [[04_Player_Entities/Tags_System|Personal Tags]]]
[dependency_refs:: [[04_Player_Entities/Trait_Development|Chronicle]]]
[presentation_ref:: [[03_Factions_Societies/Lore/The_First_Reception|The First Reception]]]
[minimum_boundary:: immutable revealed TagID and readable player-facing result]
[does_not_own:: First Return predicate, TagID assignment, Dawn settlement, tag slot accounting or combat resolution]

## Planned interfaces with unresolved owners

Эти строки фиксируют реальные границы будущих систем. `MISSING_OWNER` запрещает считать лорную страницу, Очаг, квестовый lifecycle или реестр временным resolver.

### first_reception.quarantine_assessment

[interface_id:: first_reception.quarantine_assessment]
[faction_id:: first_reception]
[interface_status:: planned]
[role:: WITNESS]
[input_family:: named living subject and observed environmental risk]
[player_verb:: request a bounded sanitary assessment]
[result_family:: timed assessment of a named biological risk]
[mechanic_owner_ref:: MISSING_OWNER]
[dependency_refs:: [[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]]]
[presentation_ref:: [[03_Factions_Societies/Lore/The_First_Reception|The First Reception]]]
[minimum_boundary:: subject identity, observed signs, assessed risk, uncertainty and expiry]
[does_not_own:: personhood, custody, property, permanent access, city-wide quarantine or treatment resolver]

### common_storehouses.emergency_reserve_release

[interface_id:: common_storehouses.emergency_reserve_release]
[faction_id:: common_storehouses]
[interface_status:: planned]
[role:: PROVIDER]
[input_family:: declared local shortage and named protected reserve]
[player_verb:: request emergency opening of a reserve]
[result_family:: bounded release or public refusal with next review]
[mechanic_owner_ref:: MISSING_OWNER]
[dependency_refs:: [[06_Economy_Loot/Economy_Core|Economy Core]]]
[presentation_ref:: [[03_Factions_Societies/Lore/The_Common_Storehouses|The Common Storehouses]]]
[minimum_boundary:: branch, stock family, protected minimum, amount, reason, witnesses and review time]
[does_not_own:: item prices, Welfare predicate, vendor stock generation, stash capacity or debt settlement]

### contour_chamber.evidence_attestation

[interface_id:: contour_chamber.evidence_attestation]
[faction_id:: contour_chamber]
[interface_status:: planned]
[role:: WITNESS]
[input_family:: dated observation, instrument trace and named witnesses]
[player_verb:: submit an observation for attestation]
[result_family:: versioned bounded record with uncertainty]
[mechanic_owner_ref:: MISSING_OWNER]
[dependency_refs:: [[08_World_Generation/Hub/01_Hub_Map_Table|Hub Map Table]]]
[presentation_ref:: [[03_Factions_Societies/Lore/The_Contour_Chamber|The Contour Chamber]]]
[minimum_boundary:: observation, place, time, method, witnesses, uncertainty and version]
[does_not_own:: guilt, ownership, biological status, global truth, route eligibility or fog-of-war resolver]

### weighing_houses.provenance_adjudication

[interface_id:: weighing_houses.provenance_adjudication]
[faction_id:: weighing_houses]
[interface_status:: planned]
[role:: WITNESS]
[input_family:: disputed object and bounded chain of transfer]
[player_verb:: request recognition of a transfer chain]
[result_family:: limited seal, refusal or recorded unresolved conflict]
[mechanic_owner_ref:: MISSING_OWNER]
[dependency_refs:: [[06_Economy_Loot/Loot_Sync_Cycle|Loot Sync Cycle]]]
[presentation_ref:: [[03_Factions_Societies/Lore/The_Weighing_Houses|The Weighing Houses]]]
[minimum_boundary:: object identity, transfer signatures, custody, conflicts of interest, scope and expiry]
[does_not_own:: human guilt, universal property law, item value, barter result, debt collection or physical transfer]

### support_artels.infrastructure_load_order

[interface_id:: support_artels.infrastructure_load_order]
[faction_id:: support_artels]
[interface_status:: planned]
[role:: WITNESS]
[input_family:: named structure, measured load and local use testimony]
[player_verb:: request a bounded load conclusion]
[result_family:: hold, restrict, inspect or release recommendation with expiry]
[mechanic_owner_ref:: MISSING_OWNER]
[dependency_refs:: [[08_World_Generation/Hub/01_Hub_Map_Table|Hub Map Table]]]
[presentation_ref:: [[03_Factions_Societies/Lore/The_Support_Artels|The Support Artels]]]
[minimum_boundary:: structure, observed load, local testimony, holder of calculation and review time]
[does_not_own:: district evacuation, player access, item durability, armor repair, route generation or permanent ownership]

### cathedral.ritual_stress_service

[interface_id:: cathedral.ritual_stress_service]
[faction_id:: cathedral_all_faiths]
[interface_status:: planned]
[role:: PROVIDER]
[input_family:: named participant, consented rite and existing stress state]
[player_verb:: enter a bounded restorative rite]
[result_family:: declared attempt to alter a named stress state]
[mechanic_owner_ref:: MISSING_OWNER]
[dependency_refs:: [[05_Combat_Survival/Status_Effects|Status Effects]]]
[presentation_ref:: [[03_Factions_Societies/Lore/The_Cathedral|The Cathedral]]]
[minimum_boundary:: participant consent, rite, target state, duration, failure and exit]
[does_not_own:: proof of gods, generic combat buff, status resolver, relic effects, contract reward or raid alliance]

### proving_houses.repeatability_attestation

[interface_id:: proving_houses.repeatability_attestation]
[faction_id:: proving_houses]
[interface_status:: planned]
[role:: WITNESS]
[input_family:: recorded trial, sample custody and independent repetitions]
[player_verb:: submit a result for repeatability review]
[result_family:: bounded seal, warning or refusal]
[mechanic_owner_ref:: MISSING_OWNER]
[dependency_refs:: [[07_Gear_Inventory/_Registries/Registry_CraftingRecipes|Registry Crafting Recipes]]]
[presentation_ref:: [[03_Factions_Societies/Lore/The_Proving_Houses|The Proving Houses]]]
[minimum_boundary:: sample owner, conditions, two independent repetitions, failure mode and owner of harm]
[does_not_own:: all research, education, item identification, recipe unlock, crafting result or universal sales ban]

### circle_of_interposition.temporary_pause

[interface_id:: circle_of_interposition.temporary_pause]
[faction_id:: circle_of_interposition]
[interface_status:: planned]
[role:: PROVIDER]
[input_family:: observed continuing harm and named protected person, object or route]
[player_verb:: request a temporary interposition]
[result_family:: timed pause, refusal, extension request or release]
[mechanic_owner_ref:: MISSING_OWNER]
[dependency_refs:: [[03_Factions_Societies/Pledge_Contracts|Pledge Contracts]]]
[presentation_ref:: [[03_Factions_Societies/Lore/The_Circle_of_Interposition|The Circle of Interposition]]]
[minimum_boundary:: protected subject, observed harm, holder of pause, witness, scope, expiry and release condition]
[does_not_own:: guilt, investigation, custody, property, biological status, permanent imprisonment or city-wide law]
