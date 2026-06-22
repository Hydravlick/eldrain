---
type: registry
status: active
registry_type: specs
system: dnd_hybrid
tags: [database]
---
# Реестр: Классы (Blocks)

> **MVP:** Зафиксированы Авангард, Технократ и Странник. Страж и Догмат остаются направлениями расширения с атрибутами, векторами и профессиональной основой, но без готовых MVP-комбинаций.
>
> Специализация задаёт методологию, а не готовые `Q/E` и не обязательную партийную роль. Все игровые `P/Q/E` создаются в ячейке `Race × Spec` по [[04_Player_Entities/MVP_3x3_Design_Contract|контракту матрицы 3×3]].

## Шаблон класса

### Шаблон Класса (Template Spec)
[id:: template_spec]
[base_vector:: ballistics]
[weak_to:: hazard, kinetics, tech]
**Атрибуты:** [TRQ:: +0] | [GRP:: +0] | [LYR:: +0] | [GLW:: +0] | [SNS:: +0]
[substat_bonus:: brace +0, cell_swap_speed +0, heat_sink +0, weakspot_read +0]
[condition_bonus:: none]
[tradeoff:: none]
*Роль: краткое назначение в рейде.*
#### Описание:
Методология класса: как он наносит давление, защищается и создает ценность для группы.
#### Примеры:
- _Профессия:_ оружие, утилита, уникальный риск.

---

## Страж (Guardian)
[id:: guard]
*Роль: Танк / Контроль.*
**Атрибуты:** [TRQ:: +3] | [GRP:: -2] | [LYR:: +4]| [GLW:: +2]| [SNS:: -1]
**Вектор:** [base_vector:: kinetics]
[weak_to:: hazard, shadow, aether]
[substat_bonus:: brace +15, armor_sync +10, backlash_resist +5]
[condition_bonus:: while_blocking: trauma_resist +10]
[tradeoff:: cell_swap_speed -5]
#### Описание:
	Физическая сила, работа с тяжелыми весами и материалами. Это те, кто держит город на своих плечах — буквально.
#### Примеры:
- _Кузнец (Forgeman):_ Использует кузнечный молот и носит фартук из асбеста. Ставит временные пластины, усиливает укрытия и стабилизирует снаряжение союзников в бою.
- _Забойщик (Miner):_ Носит тяжелый бур или гвоздомет. Ломает стены, открывая новые проходы (Destruction).
---
## Авангард (The Vanguard)
[id:: assault]
*Роль: магострельное давление, дуэли 1 на 1, создание окна для добивания.*
**Атрибуты:** [TRQ:: +2] | [GRP:: +2] | [LYR:: +1]| [GLW:: +2]| [SNS:: -2]
**Вектор:** [base_vector:: ballistics]
[weak_to:: hazard, kinetics, tech]
[substat_bonus:: drift_control +10, cell_swap_speed +8, recoil_damp +8]
[condition_bonus:: after_stagger: weapon_swap_speed +10]
[tradeoff:: resonance_load +2]
#### Описание:
	Силовое решение конфликтов. Это не обязательно солдаты, это все, кто умеет держать линию импульса, заставлять цель ошибаться и переводить дистанцию в окно для добивания.
#### Примеры:
- _Городской Дозорный (Watchman):_ Использует дубинку-шокер и щит. Бонусы против гуманоидов (арест).
- _Ликвидатор (Liquidator):_ Охотник на монстров с огнеметом. Специалист по зачистке гнезд в канализации.
---
## Технократ (The Technocrat)
[id:: support] *Роль: подготовка пространства, обслуживание устройств и изменение условий боя.*
**Атрибуты:** [TRQ:: -1] | [GRP:: +1] | [LYR:: 0]| [GLW:: +3]| [SNS:: +3]
**Вектор:** [base_vector:: tech]
[weak_to:: shadow, kinetics, detection]
[substat_bonus:: field_craft_speed +12, battery_efficiency +8, heat_warning +8]
[condition_bonus:: near_workstation: cell_swap_speed +8]
[tradeoff:: direct_pressure -5]
#### Описание:
	Прикладная наука, химия, инженерия. Те, кто стабилизирует людей, механизмы и маршруты. Методология полезна и в группе, и соло, но не является обязательным партийным слотом.
#### Примеры:
- _Уличный Хирург (Alchemist):_ Метает колбы с кислотой или лечебным паром.
- _Механик (Grease Monkey):_ Ставит турели, чинит лифты для эвакуации, взламывает двери.
---
## Странник (The Drifter)
[id:: scout] *Роль: маршрутизация, изменение позиции, сбор информации и выбор момента.*
**Атрибуты:** [TRQ:: 0] | [GRP:: +4] | [LYR:: -1]| [GLW:: +2]| [SNS:: +1]
**Вектор:** [base_vector:: shadow]
[weak_to:: hazard, ballistics, detection]
[substat_bonus:: loot_speed +12, bolt_wind_speed +8, weapon_swap_speed +8, ambush_resist +6]
[condition_bonus:: from_cover: drift_control +8]
[tradeoff:: brace -5]
#### Описание:
	Знание географии, ловкость, доступ в закрытые зоны. Те, кто живет между слоями города.
#### Примеры:
- _Фонарщик (Lamplighter):_ Прыгает по крышам, зажигает свет (дебафф тьмы на врагов), слепит вспышками.
- _Курьер Теневого Рынка (Runner):_ Переносит слоты инвентаря быстрее, вскрывает замки, видит ловушки.
---
## Догмат (The Scholar)
[id:: specialist] *Роль: "Стеклянная пушка", использование свитков, решение головоломок, обнаружение магических следов.*
**Атрибуты:** [TRQ:: 0] | [GRP:: +1] | [LYR:: -1]| [GLW:: +5]| [SNS:: +1]
**Вектор:** [base_vector:: aether]
[weak_to:: shadow, tech, ballistics]
[substat_bonus:: output_power +15, reality_burn_power +12, heat_sink +6]
[condition_bonus:: while_channeling: weakspot_read +8]
[tradeoff:: backlash_risk +5]
#### Описание:
	Интеллектуальная элита. Работа с чистой информацией, историей и древними артефактами. Магия здесь — это наука.
#### Примеры:
- _Архивариус (Archivist):_ Читает заклинания из книг (каст-тайм), опознает артефакты на месте (экономия слотов).
- _Детектив (Investigator):_ Видит "Эхо" прошедших событий, подсвечивает уязвимости врагов.
---
