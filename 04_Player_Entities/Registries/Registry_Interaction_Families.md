---
status: active
system: player_entities_registry
registry_type: interaction_families
tags: [owners, loops, operations, debt, information, validation]
related_files:
  - "[[04_Player_Entities/Skill_Build_Philosophy|Философия навыков и билдостроения]]"
  - "[[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile Pipeline]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic Batteries]]"
  - "[[07_Gear_Inventory/Inventory_Architecture|Архитектура инвентаря]]"
type: "registry"
index_route: "owner"
index_group: "player_entities"
index_order: 20
index_summary: "Хранит схему и записи: Реестр: семейства взаимодействий."
read_when: "Когда нужен контракт «Реестр: семейства взаимодействий» и его границы с соседними владельцами."
---
# Реестр: семейства взаимодействий

> Реестр объединяет параметры, которые принадлежат одному физическому циклу, ручной операции, долгу или линии информации. Его задача — не дать нескольким локальным владельцам превратить честные улучшения в безопасную непрерывность.

## 1. Закрытая грамматика

Новая запись выбирает семейство ниже и публикует только его необходимые поля.

| Семейство | Что объединяет | Допустимая ось пользы | Неснимаемая граница |
|---|---|---|---|
| `thermal_cycle` | один запас Heat, его порог, Vent и Recovery | `capacity` **или** `cadence` **или** `safety` | объявленный Vent, hard Recovery, Bloom, Dissonance и цена энергии |
| `manual_operation` | одно непрерывное решение руками до осмысленной отмены | `cadence` | Exposure и итоговое время всей процедуры |
| `self_backlash` | собственный риск процедуры | `safety` | `hard_debt`, правило сброса и последствие отказа |
| `signal_reading` | существующий сигнал, след или телеграф | `information` | источник, линия доступа и аудитория знания |
| `load_route` | масса груза, переноска и маршрутная обязанность | `capacity` | bulk, доступность, маршрут и физическое обязательство |
| `anchored_hold` | названная опора, удержание или предел процедуры | `capacity` | поза, линия, занятые руки или иной Commitment |

Правило объединения параметров и неизменяемые долги: [[04_Player_Entities/Interaction_Constraints]].

## 2. Проверка активного профиля

См. [[04_Player_Entities/Interaction_Constraints#2. Проверка активного профиля]].

## 3. `thermal_cycle`

См. [[04_Player_Entities/Interaction_Constraints#3. `thermal_cycle`]].

## 4. `manual_operation`

См. [[04_Player_Entities/Interaction_Constraints#4. `manual_operation`]].

## 5. `self_backlash` и hard debt

См. [[04_Player_Entities/Interaction_Constraints#5. `self_backlash` и hard debt]].

## 6. `signal_reading`

См. [[04_Player_Entities/Interaction_Constraints#6. `signal_reading`]].

## 7. `load_route`

См. [[04_Player_Entities/Interaction_Constraints#7. `load_route`]].

## 8. Допуск нового семейства

См. [[04_Player_Entities/Interaction_Constraints#8. Допуск нового семейства]].

