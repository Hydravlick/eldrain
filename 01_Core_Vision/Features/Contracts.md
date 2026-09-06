---
type: feature
status: active
system: player_experience
feature_id: contracts
feature_order: 9
display_name: Выполнить работу и принять её цену
player_promise: Выбрать городскую просьбу, способ выполнения и последствия для людей и адресов.
expected_dynamics: Метод выполнения меняет следующий выбор, а игрок различает работу и повторяемый список наград.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[03_Factions_Societies/Quest_Engine]]"
  - "[[03_Factions_Societies/Quest_Engine_Grammar]]"
  - "[[03_Factions_Societies/Pledge_Contracts]]"
  - "[[03_Factions_Societies/Reputation_Rules]]"
data_sources:
  - "[[03_Factions_Societies/Registries/Registry_Faction_Interfaces]]"
  - "[[08_World_Generation/Registries/Registry_POIs]]"
ux_surfaces:
  - "[[03_Factions_Societies/Quest_Engine_Grammar]]"
  - "[[08_World_Generation/Hub/Hub_Services_Interaction]]"
production_disciplines:
  - narrative
  - UX
  - level design
  - QA
validation:
  - "[[01_Core_Vision/Features/Contracts#Проверка гипотезы]]"
---

# Выполнить работу и принять её цену

Выбрать городскую просьбу, способ выполнения и последствия для людей и адресов.

Связать мотив вылазки с изменением следующего выбора в городе.

## За минуту

Игрок читает просьбу на Столе, выбирает намерение и выполняет работу в рейде. Свидетельство и объявленный trigger передаются Quest Engine; результат меняет доступный разговор, адрес или обязательство.

## Сценарии и границы

- Выполнить условие и вернуться через объявленный trigger.
- Принести вещь без нужного свидетельства: увидеть незавершённую часть.
- Отказаться от поручения или выбрать спорный метод.
- Вернуться body-only: не получить расчёт обычной успешной доставки.

Не превращать фракционную биографию в resolver и не вводить безопасную ферму поручений Пешек.

## Кто исполняет и что видит игрок

Правила и переходы: [[03_Factions_Societies/Quest_Engine]], [[03_Factions_Societies/Quest_Engine_Grammar]], [[03_Factions_Societies/Pledge_Contracts]], [[03_Factions_Societies/Reputation_Rules]].

Данные и авторские экземпляры: [[03_Factions_Societies/Registries/Registry_Faction_Interfaces]], [[08_World_Generation/Registries/Registry_POIs]].

Игроковые экраны, сигналы и объяснение отказа: [[03_Factions_Societies/Quest_Engine_Grammar]], [[08_World_Generation/Hub/Hub_Services_Interaction]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Метод выполнения меняет следующий выбор, а игрок различает работу и повторяемый список наград.

- **Наблюдаем:** Игрок объясняет, кому и почему помог, и замечает последствие в следующем обращении к Столу.
- **Доказательство и способ наблюдения:** Сквозной контракт с normal/negative исходами и повтор после знакомства с выгодными методами.
- **Опровержение:** Все методы отличаются только временем до одинаковой награды или фракция остаётся невидимой шкалой.
- **Ответ:** Пересмотреть причинную связь результата, адреса и видимого последствия.

## MVP и производство

Первый срез: Один field-контракт меняет маршрут и момент выхода, один Hub-only контракт находится рядом с материальной сделкой; отказ от обоих оставляет обычную вылазку. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

Авторские контракты и фракционные голоса требуют контента; схема сама не доказывает переживание долга.

Quest design задаёт конкретную процедуру и стороны; UX различает сделку и цель; narrative сохраняет мотив заказчика; QA проверяет провал, отказ и повтор награды.
