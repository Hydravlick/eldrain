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

На Столе игрок видит возраст доступного сектора и выбирает, когда войти. Можно выполнить короткую работу в ранней фазе или принять поздний риск ради более глубокой цели. Собственная вылазка занимает часть жизни места: пока Пешка движется, мир продолжает меняться, даже если личная работа ещё не закончена.

## Уйти до изменения или остаться внутри

В рейде фаза, погода и местные следы предупреждают о смене условий. Игрок сопоставляет их с подготовкой Пешки и решает, уходить, углубляться или оставаться на переход. После изменения проверяется конкретная подготовка и маршрут: что осталось проходимым, где нужна другая защита и какую цель ещё можно успеть выполнить.

Поздний сектор может оставаться живым, когда новые входы уже закрыты. Печать переводит находящихся внутри в последний час Apex: обычный выход больше недоступен, нужно пережить отдельный режим до Рассвета. Возраст мира не является таймером личного рейда, а Tier не оценивает силу человека.

## Что останется после Рассвета

Рассвет завершает сессию, но судьба каждой Пешки определяется отдельно. Общий финал не обещает всем одинакового возвращения. Стол показывает новую мирную ревизию только после её отдельной публикации; локальное событие рейда само по себе не заменяет карту города.

Несколько сессий одной ревизии хранят местные изменения раздельно. Игрок должен различать то, что узнал сам, происходящее в текущем рейде и уже опубликованное изменение города. Тогда знакомство с сектором помогает выбирать момент следующей вылазки, не стирая необходимости читать текущие условия.

## Переходы мира и их показ

[[08_World_Generation/Generation/Server_Lifecycle|Жизнь сессии]], [[08_World_Generation/Generation/Global_Map_Rotation|ротация]] и [[08_World_Generation/Generation/Location_Revision_Lifecycle|ревизия места]] разделяют время рейда и публикацию мирного состояния. [[08_World_Generation/Anomaly/Anomaly_System|Аномалия]], [[08_World_Generation/Anomaly/Anomaly_Mutation_Lines|линии мутаций]] и [[08_World_Generation/Generation/Dynamic_Weather|погода]] меняют среду; [[08_World_Generation/Generation/Gate_Check|Gate Check]] и [[08_World_Generation/Anomaly/Apex_Last_Hour|Apex]] задают фазовые последствия.

[[08_World_Generation/Generation/Difficulty_Slots|Живые слоты]], [[08_World_Generation/Anomaly/Anomaly_Core_Loop|фазовые сигналы]] и [[08_World_Generation/Hub/Hub_Map_Table|Стол]] должны согласованно показывать возраст, доступность и изменение. Биомы, мутации, состояния среды и Порт перечислены в источниках данных страницы.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Игрок выбирает фазовый риск, а изменение мира добавляет решения после освоения сектора.

- **Наблюдаем:** Игрок различает время своего рейда и возраст мира, узнаёт предупреждение и меняет план до барьера.
- **Доказательство и способ наблюдения:** Повторные рейды через фазовые границы, наблюдение Apex и перехода к Stable-проекции.
- **Опровержение:** Переход читается как случайная казнь или после освоения остаётся только обязательный набор защиты.
- **Ответ:** Пересмотреть сигналы, условия среды и ценность позднего выбора без изменения времени исподтишка.

## MVP и производство

Первый срез: Один сектор проходит наблюдаемое изменение локального POI и завершение ревизии; account-знание показывается отдельно от общей топологии. Сценарий — [[01_Core_Vision/Build_Extraction_Concept_Slice]], работа — [[09_Project_Management/TODO]].

Плотность игроков, совместное знание и стоимость авторства разных фаз могут изменить ожидаемую динамику.

World и level design авторствуют смену сцены; audio/VFX показывают её заранее; gameplay и QA проверяют переход при разных Presence и повторном входе.
