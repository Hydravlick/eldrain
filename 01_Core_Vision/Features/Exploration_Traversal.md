---
type: feature
status: active
system: player_experience
feature_id: exploration_traversal
feature_order: 4
display_name: Прочитать место и проложить маршрут
player_promise: Находить путь, читать следы и менять план в незнакомой сборке знакомого сектора.
expected_dynamics: После освоения карты игрок продолжает читать текущую сцену, а не только повторять маршрут из wiki.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[05_Combat_Survival/Traversal_Core]]"
  - "[[05_Combat_Survival/Movement_Physics]]"
  - "[[05_Combat_Survival/Hunt_Frontier_Loop]]"
  - "[[05_Combat_Survival/Acoustic_Stealth]]"
  - "[[08_World_Generation/Generation/World_Topology]]"
  - "[[08_World_Generation/Generation/Traversal_Shortcuts]]"
  - "[[08_World_Generation/Generation/UI_Map_Protocol]]"
ux_surfaces:
  - "[[08_World_Generation/Generation/UI_Map_Protocol]]"
  - "[[04_Player_Entities/Grimoire_Truth_Triangulation]]"
production_disciplines:
  - level design
  - audio
  - art
  - UX
  - QA
validation:
  - "[[01_Core_Vision/Features/Exploration_Traversal#Проверка гипотезы]]"
data_sources: ["[[08_World_Generation/Content/World_Atlas/Sectors/Port/Port_Manifest]]", "[[08_World_Generation/Registries/Registry_POIs]]", "[[08_World_Generation/Registries/Registry_Environment_States]]", "[[08_World_Generation/Content/Hunt_Frontier_Slice]]"]
---

# Прочитать место и проложить маршрут

Находить путь, читать следы и менять план в незнакомой сборке знакомого сектора.

Дать знанию пространства ценность, сохранив решения после освоения карты.

## За минуту

Игрок сопоставляет карту, геометрию, шум и физические следы, выбирает путь к цели и держит в уме отход. Изменившаяся сцена заставляет уточнить маршрут; наблюдение не гарантирует знание о чужом намерении.

## Сценарии и границы

- Найти цель по неполному следу и выйти другим путём.
- Замечена засада: обойти, ждать или отказаться от цели.
- Проход изменился после события: найти читаемую альтернативу.
- Груз мешает прежнему маршруту: решить, что нести дальше.

Не выдавать wallhack и не наказывать неподвижность отдельным таймером.

## Кто исполняет и что видит игрок

Правила и переходы: [[05_Combat_Survival/Traversal_Core]], [[05_Combat_Survival/Movement_Physics]], [[05_Combat_Survival/Hunt_Frontier_Loop]], [[05_Combat_Survival/Acoustic_Stealth]], [[08_World_Generation/Generation/World_Topology]], [[08_World_Generation/Generation/Traversal_Shortcuts]], [[08_World_Generation/Generation/UI_Map_Protocol]].

Данные и авторские экземпляры: [[08_World_Generation/Content/World_Atlas/Sectors/Port/Port_Manifest]], [[08_World_Generation/Registries/Registry_POIs]], [[08_World_Generation/Registries/Registry_Environment_States]].

Игроковые экраны, сигналы и объяснение отказа: [[08_World_Generation/Generation/UI_Map_Protocol]], [[04_Player_Entities/Grimoire_Truth_Triangulation]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** После освоения карты игрок продолжает читать текущую сцену, а не только повторять маршрут из wiki.

- **Наблюдаем:** Знакомый маршрут меняется по наблюдаемой причине; игрок может объяснить свой обход.
- **Доказательство и способ наблюдения:** Повторные прохождения одной ревизии и нескольких сборок; разбор маршрутов после обмена знаниями.
- **Опровержение:** Есть неизменно лучший путь либо изменения требуют только лишнего бега без нового решения.
- **Ответ:** Пересмотреть размещение следов, связность и альтернативы отхода.

## MVP и производство

Первый срез: Одна сборка Порта с различимыми альтернативами пути, следом и отказом от опасного прохода; повторный заход меняет маршрутную задачу. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

Данные первого знакомства не доказывают долговечность исследования; нужен повтор после общего знания карты.

Level design собирает различающиеся подходы; art, audio и VFX делают причину читаемой; QA проверяет доступность контрхода и отсутствие слепого обязательного прохода.
