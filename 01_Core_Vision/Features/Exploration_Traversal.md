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

Пешка входит в знакомый сектор, собранный иначе. Игрок сопоставляет карту с видимыми проходами, шумом, погодой и физическими следами. Нужно найти цель и оставить возможность вернуться с грузом. Знание прежнего маршрута помогает сориентироваться, но не сообщает, кто сейчас занял проход и зачем там оставлен след.

## Проверять путь по мере движения

Неполный след может привести к цели, чужой работе или засаде. Замеченную угрозу можно обойти, переждать либо отказаться от цели. Наблюдение даёт основание для выбора, но не гарантирует знание чужого намерения. Карта и звук не должны выдавать противника сквозь стены.

Если событие изменило проход, игрок ищет читаемую альтернативу: сопоставляет новую геометрию с известными связями и проверяет возможность отхода. Смена сборки должна менять задачу маршрута. Лишний бег по единственной оставшейся дороге сам по себе не делает повторное исследование полезным.

На обратном пути прежнее решение может перестать подходить из-за груза. Игрок сравнивает то, что несёт, с доступным движением и решает, что оставить, чтобы пройти дальше. Путь к цели и путь с находкой проверяются отдельно. Ожидание допустимо; неподвижность не наказывается отдельным таймером.

## Геометрия, следы и карта

[[05_Combat_Survival/Traversal_Core|Traversal]] и [[05_Combat_Survival/Movement_Physics|физика движения]] задают действия тела; [[08_World_Generation/Generation/World_Topology|топология]] и [[08_World_Generation/Generation/Traversal_Shortcuts|короткие пути]] — связи места. [[05_Combat_Survival/Hunt_Frontier_Loop|Поиск и охота]] и [[05_Combat_Survival/Acoustic_Stealth|акустика]] связывают чужую работу с наблюдаемыми следами.

[[08_World_Generation/Generation/UI_Map_Protocol|Карта]] и [[04_Player_Entities/Grimoire_Truth_Triangulation|Гримуар]] различают известное и предположение. Для первого среза [[08_World_Generation/Content/World_Atlas/Sectors/Port/Port_Manifest|Порт]], [[08_World_Generation/Registries/Registry_POIs|POI]] и [[08_World_Generation/Registries/Registry_Environment_States|состояния среды]] должны дать различимые подходы и причины их изменения.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** После освоения карты игрок продолжает читать текущую сцену, а не только повторять маршрут из wiki.

- **Наблюдаем:** Знакомый маршрут меняется по наблюдаемой причине; игрок может объяснить свой обход.
- **Доказательство и способ наблюдения:** Повторные прохождения одной ревизии и нескольких сборок; разбор маршрутов после обмена знаниями.
- **Опровержение:** Есть неизменно лучший путь либо изменения требуют только лишнего бега без нового решения.
- **Ответ:** Пересмотреть размещение следов, связность и альтернативы отхода.

## MVP и производство

Первый срез: Одна сборка Порта с различимыми альтернативами пути, следом и отказом от опасного прохода; повторный заход меняет маршрутную задачу. Сценарий — [[01_Core_Vision/Build_Extraction_Concept_Slice]], работа — [[09_Project_Management/TODO]].

Данные первого знакомства не доказывают долговечность исследования; нужен повтор после общего знания карты.

Level design собирает различающиеся подходы; art, audio и VFX делают причину читаемой; QA проверяет доступность контрхода и отсутствие слепого обязательного прохода.
