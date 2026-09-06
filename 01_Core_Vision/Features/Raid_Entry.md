---
type: feature
status: active
system: player_experience
feature_id: raid_entry
feature_order: 3
display_name: Выбрать подход и войти в рейд
player_promise: Принять понятную ставку входа в живой сектор одному или с группой.
expected_dynamics: Игрок принимает поздний риск осознанно, а отказ не воспринимает как произвольную потерю ставки.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[08_World_Generation/Generation/Raid_Approach_and_Entry]]"
  - "[[08_World_Generation/Anomaly/Insertion_Logic]]"
  - "[[08_World_Generation/Generation/Egress_Solvency]]"
  - "[[08_World_Generation/Generation/Async_Timers]]"
  - "[[08_World_Generation/Hub/Party_Syndicate]]"
data_sources:
  - "[[08_World_Generation/Registries/Registry_Raid_Interfaces]]"
ux_surfaces:
  - "[[08_World_Generation/Hub/Hub_Map_Table]]"
  - "[[08_World_Generation/Generation/Difficulty_Slots]]"
production_disciplines:
  - UX
  - level design
  - gameplay
  - QA
validation:
  - "[[01_Core_Vision/Features/Raid_Entry#Проверка гипотезы]]"
---

# Выбрать подход и войти в рейд

Принять понятную ставку входа в живой сектор одному или с группой.

Связать подготовку и намерение с конкретной сессией без ложного обещания безопасной точки.

## За минуту

На Столе игрок выбирает сектор и подход. EntryQuote раскрывает точную ставку; участники подтверждают её независимо. Insertion проверяет кандидата и материализует группу только после общего результата Breach.

## Сценарии и границы

- Подтверждённый подход приводит к обычному входу.
- Quote устарела или окно недоступно: получить конечный отказ и новый выбор.
- Один участник не готов: группа не получает частично исполненное обещание.
- Соединение оборвалось на границе commit: восстановить уже принятое решение без второго тела.

Не обещать безопасный spawn; не разделять очередь по силе экипировки.

## Кто исполняет и что видит игрок

Правила и переходы: [[08_World_Generation/Generation/Raid_Approach_and_Entry]], [[08_World_Generation/Anomaly/Insertion_Logic]], [[08_World_Generation/Generation/Egress_Solvency]], [[08_World_Generation/Generation/Async_Timers]], [[08_World_Generation/Hub/Party_Syndicate]].

Данные и авторские экземпляры: [[08_World_Generation/Registries/Registry_Raid_Interfaces]].

Игроковые экраны, сигналы и объяснение отказа: [[08_World_Generation/Hub/Hub_Map_Table]], [[08_World_Generation/Generation/Difficulty_Slots]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Игрок принимает поздний риск осознанно, а отказ не воспринимает как произвольную потерю ставки.

- **Наблюдаем:** До подтверждения игрок различает цену подхода, фазу мира и неизвестность первого контакта.
- **Доказательство и способ наблюдения:** Наблюдение solo/party входов, устаревших quote, низкой населённости и reconnect.
- **Опровержение:** Игрок путает фазу с допуском по gear либо не может объяснить списание или отказ.
- **Ответ:** Пересмотреть раскрытие quote и административный отказ; исследовать ingress pressure отдельно от обещания безопасности.

## MVP и производство

Первый срез: Один сектор, solo и party подтверждение, устаревшая quote и отказ до Breach; региональное масштабирование проверяется отдельно. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

Региональный service и плотность населения требуют прототипа; поздняя полоса может быть недоступна.

UX показывает цену и конечный результат подтверждения; level design обеспечивает валидных кандидатов; gameplay и QA проверяют commit и восстановление соединения.
