---
type: feature
status: active
system: player_experience
feature_id: living_world
feature_order: 12
display_name: Выбрать момент в меняющемся мире
player_promise: Читать возраст сектора, переживать его изменение и видеть, что город унаследовал после него.
expected_dynamics: Игрок выбирает фазовый риск, а изменение мира добавляет решения после освоения сектора.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[08_World_Generation/Generation/Server_Lifecycle]]"
  - "[[08_World_Generation/Generation/Global_Map_Rotation]]"
  - "[[08_World_Generation/Generation/Location_Revision_Lifecycle]]"
  - "[[08_World_Generation/Anomaly/Anomaly_System]]"
  - "[[08_World_Generation/Anomaly/Anomaly_Mutation_Lines]]"
  - "[[08_World_Generation/Generation/Dynamic_Weather]]"
  - "[[08_World_Generation/Generation/Gate_Check]]"
  - "[[08_World_Generation/Anomaly/Apex_Last_Hour]]"
data_sources:
  - "[[08_World_Generation/Registries/Registry_Biomes]]"
  - "[[08_World_Generation/Registries/Registry_Anomaly_Mutations]]"
  - "[[08_World_Generation/Registries/Registry_Environment_States]]"
  - "[[08_World_Generation/Content/World_Atlas/Sectors/Port/Port_Manifest]]"
ux_surfaces:
  - "[[08_World_Generation/Generation/Difficulty_Slots]]"
  - "[[08_World_Generation/Anomaly/Anomaly_Core_Loop]]"
  - "[[08_World_Generation/Hub/Hub_Map_Table]]"
production_disciplines:
  - level design
  - art
  - audio
  - VFX
  - UX
  - QA
validation:
  - "[[01_Core_Vision/Features/Living_World#Проверка гипотезы]]"
---

# Выбрать момент в меняющемся мире

Читать возраст сектора, переживать его изменение и видеть, что город унаследовал после него.

Соединить короткую вылазку с более долгой жизнью места без подмены личного исхода общим событием.

## За минуту

На Столе виден возраст доступного сектора. В рейде фаза, местные следы и погода предупреждают об изменении; игрок уходит, углубляется или принимает запечатанный последний час. После завершения публикуется новая мирная ревизия по своему lifecycle.

## Сценарии и границы

- Короткая работа в ранней фазе.
- Остаться на фазовый переход и увидеть последствия подготовки.
- Поздний сектор ещё жив, но новые входы закрыты.
- Несколько сессий одной ревизии сохраняют локальные изменения раздельно.
- Dawn завершает сессию, но личные судьбы решаются отдельно.

Не считать Tier рейтингом человека, не подменять WorldRevision локальными событиями рейда.

## Кто исполняет и что видит игрок

Правила и переходы: [[08_World_Generation/Generation/Server_Lifecycle]], [[08_World_Generation/Generation/Global_Map_Rotation]], [[08_World_Generation/Generation/Location_Revision_Lifecycle]], [[08_World_Generation/Anomaly/Anomaly_System]], [[08_World_Generation/Anomaly/Anomaly_Mutation_Lines]], [[08_World_Generation/Generation/Dynamic_Weather]], [[08_World_Generation/Generation/Gate_Check]], [[08_World_Generation/Anomaly/Apex_Last_Hour]].

Данные и авторские экземпляры: [[08_World_Generation/Registries/Registry_Biomes]], [[08_World_Generation/Registries/Registry_Anomaly_Mutations]], [[08_World_Generation/Registries/Registry_Environment_States]], [[08_World_Generation/Content/World_Atlas/Sectors/Port/Port_Manifest]].

Игроковые экраны, сигналы и объяснение отказа: [[08_World_Generation/Generation/Difficulty_Slots]], [[08_World_Generation/Anomaly/Anomaly_Core_Loop]], [[08_World_Generation/Hub/Hub_Map_Table]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Игрок выбирает фазовый риск, а изменение мира добавляет решения после освоения сектора.

- **Наблюдаем:** Игрок различает время своего рейда и возраст мира, узнаёт предупреждение и меняет план до барьера.
- **Доказательство и способ наблюдения:** Повторные рейды через фазовые границы, наблюдение Apex и перехода к Stable-проекции.
- **Опровержение:** Переход читается как случайная казнь или после освоения остаётся только обязательный набор защиты.
- **Ответ:** Пересмотреть сигналы, условия среды и ценность позднего выбора без изменения времени исподтишка.

## MVP и производство

Первый срез: Один сектор проходит наблюдаемое изменение локального POI и завершение ревизии; account-знание показывается отдельно от общей топологии. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

Плотность игроков, совместное знание и стоимость авторства разных фаз могут изменить ожидаемую динамику.

World и level design авторствуют смену сцены; audio/VFX показывают её заранее; gameplay и QA проверяют переход при разных Presence и повторном входе.
