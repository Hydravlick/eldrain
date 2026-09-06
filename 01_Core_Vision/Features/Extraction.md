---
type: feature
status: active
system: player_experience
feature_id: extraction
feature_order: 7
display_name: Решить, когда уходить
player_promise: Найти обычный выход и завершить ставку либо осознанно отказаться от неё ради живого человека.
expected_dynamics: Жадность конкурирует с уходом, а столкновение у выхода сохраняет читаемую контригру.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[08_World_Generation/Anomaly/Extraction_System]]"
  - "[[08_World_Generation/Generation/Egress_Solvency]]"
  - "[[06_Economy_Loot/Extraction_Stabilization_Loop]]"
  - "[[06_Economy_Loot/Return_Manifest_Contract]]"
  - "[[08_World_Generation/Generation/Server_Lifecycle]]"
  - "[[08_World_Generation/Anomaly/Apex_Last_Hour]]"
ux_surfaces:
  - "[[08_World_Generation/Anomaly/Extraction_System]]"
  - "[[06_Economy_Loot/Extraction_Stabilization_Loop]]"
production_disciplines:
  - level design
  - UX
  - audio
  - VFX
  - QA
validation:
  - "[[01_Core_Vision/Features/Extraction#Проверка гипотезы]]"
data_sources: ["[[08_World_Generation/Registries/Registry_Raid_Interfaces]]", "[[08_World_Generation/Content/Hunt_Frontier_Slice]]"]
---

# Решить, когда уходить

Найти обычный выход и завершить ставку либо осознанно отказаться от неё ради живого человека.

Дать рейду завершение, вокруг которого сходятся время, груз и риск встречи.

## За минуту

Игрок оценивает оставшийся путь и груз, ищет Порог и принимает обязательство Sync. Его исход передаётся возврату. Body-only отказ и запечатанный Apex читаются как другие ставки с собственными владельцами последствий.

## Сценарии и границы

- Дойти до Порога и вернуть допустимый груз.
- Порог недоступен или Sync прерван: прочитать отказ и оставшиеся варианты.
- Союзник выходит отдельно: его решение не разрешает чужой исход.
- Смерть, спор custody или фазовая граница во время обязательства дают один упорядоченный результат.
- Breakline сохраняет живого человека ценой отказа от груза и расчёта контракта.

Не гарантировать безопасный отход и не присваивать выживание по факту наличия manifest.

## Кто исполняет и что видит игрок

Правила и переходы: [[08_World_Generation/Anomaly/Extraction_System]], [[08_World_Generation/Generation/Egress_Solvency]], [[06_Economy_Loot/Extraction_Stabilization_Loop]], [[06_Economy_Loot/Return_Manifest_Contract]], [[08_World_Generation/Generation/Server_Lifecycle]], [[08_World_Generation/Anomaly/Apex_Last_Hour]].

Данные и авторские экземпляры: [[08_World_Generation/Registries/Registry_Raid_Interfaces]].

Игроковые экраны, сигналы и объяснение отказа: [[08_World_Generation/Anomaly/Extraction_System]], [[06_Economy_Loot/Extraction_Stabilization_Loop]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Жадность конкурирует с уходом, а столкновение у выхода сохраняет читаемую контригру.

- **Наблюдаем:** Игрок заранее меняет план выхода и объясняет, чем пожертвовал; проигравший видит доступный ответ.
- **Доказательство и способ наблюдения:** Запись ранних/поздних уходов, засад, split-party, custody-конфликтов и фазовых границ.
- **Опровержение:** Одна засада контролирует и первый удар, и добычу, и отход либо уход превращается в обязательную рутину без решения.
- **Ответ:** Пересмотреть топологию поиска и контригру у выхода, не вводя скрытый таймер наказания.

## MVP и производство

Первый срез: Найти Порог, завершить и прервать Sync, разойтись с группой; отдельно воспроизвести body-only отказ и фазовую границу. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

Населённость и координация групп меняют convergence; тестировать опытные группы, а не только первый рейд.

Level design оставляет читаемый поиск и контригру; audio/VFX показывают рождение шва и reset; UX объясняет вместимость и личный исход; QA проверяет спор за груз.
