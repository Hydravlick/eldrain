---
type: feature
status: active
system: player_experience
feature_id: knowledge_investigation
feature_order: 14
display_name: Собрать свидетельства и понять находку
player_promise: Сопоставить чужие объяснения с найденным свидетельством и выбрать дальнейшее расследование.
expected_dynamics: Игрок использует происхождение знания при выборе действия, а после разгадки сохраняется содержательная работа.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[04_Player_Entities/Grimoire_Truth_Triangulation]]"
  - "[[03_Factions_Societies/Quest_Engine]]"
  - "[[03_Factions_Societies/Quest_Engine_Grammar]]"
data_sources:
  - "[[08_World_Generation/Registries/Registry_POIs]]"
  - "[[03_Factions_Societies/Registries/Registry_Faction_Interfaces]]"
ux_surfaces:
  - "[[04_Player_Entities/Grimoire_Truth_Triangulation]]"
  - "[[04_Player_Entities/Entity_Grimoire]]"
  - "[[08_World_Generation/Hub/Hub_Map_Table]]"
production_disciplines:
  - narrative
  - UX
  - level design
  - audio
  - QA
validation:
  - "[[01_Core_Vision/Features/Knowledge_Investigation#Проверка гипотезы]]"
---

# Собрать свидетельства и понять находку

Сопоставить чужие объяснения с найденным свидетельством и выбрать дальнейшее расследование.

Сохранить исследованию смысл после открытия факта, связывая знание с новым действием.

## За минуту

Игрок получает наблюдение, слух или объяснение адреса, видит источник и степень подтверждения в Гримуаре. Несогласие источников даёт повод проверить место в рейде; свидетельство возвращается к контракту и следующему вопросу.

## Сценарии и границы

- Два источника расходятся: сохранить обе версии и их причины.
- Новый след подтверждает часть объяснения, не всё утверждение сразу.
- Факт уже известен сообществу: работа в рейде всё ещё имеет конкретный адрес и последствие.
- Недостаточно свидетельств: показать неопределённость вместо окончательного ответа.

Не объявлять мнение жителя истиной и не обещать неразрешимую сообществом загадку.

## Кто исполняет и что видит игрок

Правила и переходы: [[04_Player_Entities/Grimoire_Truth_Triangulation]], [[03_Factions_Societies/Quest_Engine]], [[03_Factions_Societies/Quest_Engine_Grammar]].

Данные и авторские экземпляры: [[08_World_Generation/Registries/Registry_POIs]], [[03_Factions_Societies/Registries/Registry_Faction_Interfaces]].

Игроковые экраны, сигналы и объяснение отказа: [[04_Player_Entities/Grimoire_Truth_Triangulation]], [[04_Player_Entities/Entity_Grimoire]], [[08_World_Generation/Hub/Hub_Map_Table]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Игрок использует происхождение знания при выборе действия, а после разгадки сохраняется содержательная работа.

- **Наблюдаем:** Игрок различает слух и подтверждённый факт и называет, какое наблюдение изменит его решение.
- **Доказательство и способ наблюдения:** Разбор расследования до и после публичного решения; проверка спорных источников и повторного прохождения.
- **Опровержение:** Гримуар становится обязательным чтением без выбора или расследование после wiki остаётся только execution tax.
- **Ответ:** Пересмотреть связь свидетельства, метода и результата; сократить повторную подачу известного.

## MVP и производство

Первый срез: Один физический след, проверка его происхождения и использование подтверждённого знания в следующем выборе маршрута. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

Сквозной authored пример и ритм поводов ещё требуют production; нельзя объявлять гипотезу validated по схеме.

Content и narrative design создают проверяемое свидетельство; UX показывает известное и неподтверждённое; gameplay и QA сохраняют источник при возврате и повторном просмотре.
