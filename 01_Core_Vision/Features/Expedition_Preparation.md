---
type: feature
status: active
system: player_experience
feature_id: expedition_preparation
feature_order: 2
display_name: Снарядиться под вылазку
player_promise: "Подготовить известную Пешку к выбранной работе: увидеть возможности, недостающее покрытие и цену снаряжения."
expected_dynamics: Игрок меняет подготовку под задачу, сохраняя осмысленный бюджетный вариант.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[07_Gear_Inventory/Calibration_Contract]]"
  - "[[04_Player_Entities/Combat_Profile_Pipeline]]"
  - "[[07_Gear_Inventory/Thermos_System]]"
  - "[[07_Gear_Inventory/Thermos_Assembly]]"
  - "[[07_Gear_Inventory/Equipment_PaperDoll]]"
  - "[[07_Gear_Inventory/Gear_Progression]]"
  - "[[05_Combat_Survival/Magic_Batteries]]"
data_sources:
  - "[[04_Player_Entities/Registries/Registry_Combos]]"
  - "[[07_Gear_Inventory/Registries/Registry_Thermoses]]"
  - "[[07_Gear_Inventory/Registries/Registry_Thermos_Modules]]"
  - "[[05_Combat_Survival/Registries/Registry_Weapons]]"
ux_surfaces:
  - "[[07_Gear_Inventory/Item_Attributes_UI]]"
  - "[[07_Gear_Inventory/Equipment_PaperDoll]]"
production_disciplines:
  - UX
  - art
  - animation
  - gameplay
  - QA
validation:
  - "[[01_Core_Vision/Features/Expedition_Preparation#Проверка гипотезы]]"
---

# Снарядиться под вылазку

Подготовить известную Пешку к выбранной работе: увидеть возможности, недостающее покрытие и цену снаряжения.

Сделать подготовку ответом на среду и задачу, который заметен в рейде.

## За минуту

Игрок выбирает цель, рассматривает тело и полевой профиль, собирает Термос и подбирает оружие с источником энергии. Предпросмотр показывает итог сборки и причины отказа; подтверждённая конфигурация идёт во входной контракт.

## Сценарии и границы

- Собрать допустимый комплект из доступных вещей.
- Модуль не помещается или не обслуживается: увидеть конкретное нарушение до Deploy.
- Один ItemID оказался в двух черновиках: подтвердить только допустимую сборку.
- Дорогой комплект даёт другой ответ, но не обещает безопасный исход.

Не выбирать Q/E сменой оружия; не создавать общий power score и не решать вход за ingress.

## Кто исполняет и что видит игрок

Правила и переходы: [[07_Gear_Inventory/Calibration_Contract]], [[04_Player_Entities/Combat_Profile_Pipeline]], [[07_Gear_Inventory/Thermos_System]], [[07_Gear_Inventory/Thermos_Assembly]], [[07_Gear_Inventory/Equipment_PaperDoll]], [[07_Gear_Inventory/Gear_Progression]], [[05_Combat_Survival/Magic_Batteries]].

Данные и авторские экземпляры: [[04_Player_Entities/Registries/Registry_Combos]], [[07_Gear_Inventory/Registries/Registry_Thermoses]], [[07_Gear_Inventory/Registries/Registry_Thermos_Modules]], [[05_Combat_Survival/Registries/Registry_Weapons]].

Игроковые экраны, сигналы и объяснение отказа: [[07_Gear_Inventory/Item_Attributes_UI]], [[07_Gear_Inventory/Equipment_PaperDoll]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Игрок меняет подготовку под задачу, сохраняя осмысленный бюджетный вариант.

- **Наблюдаем:** Перед повторной вылазкой игрок меняет конкретный инструмент и может назвать ожидаемый выигрыш и долг.
- **Доказательство и способ наблюдения:** Сопоставление выбранной работы, preview и фактического применения снаряжения в рейде.
- **Опровержение:** Один комплект вытесняет альтернативы независимо от среды либо игрок узнаёт собственные ограничения только после Deploy.
- **Ответ:** Пересмотреть читаемость preview и предметные компромиссы у их владельцев.

## MVP и производство

Первый срез: Один полностью заданный комплект с работающим preview и один недопустимый вариант установки; неопубликованные topology не подменяются условными числами. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

Калибровка сборок и данных Термоса не доказана; сначала один полный playable комплект.

Art и animation показывают место установки и телесные ограничения; UX называет причину отказа; gameplay и QA сопоставляют preview с рейдовой конфигурацией.
