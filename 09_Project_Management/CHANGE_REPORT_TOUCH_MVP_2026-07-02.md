---
type: report
status: active
system: project_management
tags: [touch, thermos, substats, mvp, change_report]
related_files:
  - "[[04_Player_Entities/Attributes_TOUCH|Attributes_TOUCH]]"
  - "[[07_Gear_Inventory/Thermos_System|Thermos_System]]"
  - "[[04_Player_Entities/Tags_System|Tags_System]]"
---
# TOUCH MVP — отчёт об изменениях 2026-07-02

## Изменено

- T.O.U.C.H. разделён на `Core`, ограниченный `ExternalShift`, обычный итог и отдельное Corruption-исключение.
- Добавлен **Опорный контур**: свойство существующего модуля Термоса, а не новое семейство или гибрид.
- Зафиксирован один активный контур, Gear `+2`, Tags + Gear `+4`, обычный диапазон `6–20` и показ overflow.
- В реестр добавлены десять `blocked_calibration` prototype-контуров — по два обмена на каждый атрибут.
- Substats отделены от capabilities, output modifiers, vulnerabilities и Frame Window; процентные значения нормализованы через `/100`.
- `spark_gain` связан с пассивной основой `squirrel_assault` «Инерционный заряд».
- `gate_resist` поглощён телесным `entropy_buffer`, отдельным от `ThermosModuleProtection`.
- `vent_fit` стал бинарной capability; `movement_noise` и `move_speed` перенесены в output modifiers.
- Обычным Affix запрещены первичные T.O.U.C.H. и изменение `touch_shift`.
- Character Matrix читает `TRQ/GRP/LYR/GLW/SNS` и базу `10` из структурированных данных; старые fallback удалены.

## Осознанно удалено из первичного T.O.U.C.H.

- `Temporary Effects`: в MVP они меняют substats, conditions и output modifiers.

## Отложено после MVP

- `downed_time` — до появления полного состояния Downed.
- `toxin_filter`, `dry_heat_penalty`, `stillness_camo`, `cold_start_speed` — вместе с Жабой и Ящерицей.
- `shock_output`, `natural_recharge`, `wet_backlash` — до появления исполняемых правил.
- `direct_pressure`, `backlash_risk`, `relocation_speed` — удалены как свободные числовые слова; смысл сохранён в описаниях или vulnerability notes.

## Проверено

- слабый, базовый и экстремальный клэмп: `11/14/20`, overflow экстремума `3`;
- Cell Swap после нормализации: `1.087 / 1.000 / 0.680` от базового времени;
- все активные `attr_delta` используют только пять ключей T.O.U.C.H.;
- все используемые `substat_bonus` находятся в каноническом каталоге;
- на каждый атрибут существуют два разных prototype-контура.

## Требует прототипа

- эквивалентность `+1 T.O.U.C.H.` весу, Heat, Pulse и другим уязвимостям;
- `module_cost`, позиции и точные цены prototype-контуров;
- полные Welfare, Balanced, Armor Rat, Glass Cannon, Specialist, Squad Carrier и Overgeared-тесты;
- формула `spark_gain` и пороги meaningful movement impulse.
