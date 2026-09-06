---
type: feature
status: active
system: player_experience
feature_id: living_table
feature_order: 10
display_name: Вернуться к живому Столу
player_promise: Понять, что изменилось в городе, и выбрать следующую работу через карту, предметы и голоса.
expected_dynamics: Игрок задерживается ради нового смысла, но освоивший Стол быстро проходит знакомую подготовку.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[08_World_Generation/Hub/Hub_Map_Table]]"
  - "[[08_World_Generation/Hub/Hub_Services_Interaction]]"
  - "[[08_World_Generation/Hub/Hub_Map_Interaction]]"
  - "[[08_World_Generation/City_State/Civic_Event_Lifecycle]]"
  - "[[08_World_Generation/Generation/Dual_State_POIs]]"
  - "[[08_World_Generation/Hub/Party_Syndicate]]"
data_sources:
  - "[[08_World_Generation/Registries/Registry_POIs]]"
  - "[[03_Factions_Societies/Registries/Registry_Faction_Interfaces]]"
ux_surfaces:
  - "[[08_World_Generation/Hub/Hub_Environment]]"
  - "[[08_World_Generation/Hub/Time_Atmosphere]]"
  - "[[04_Player_Entities/Entity_Grimoire]]"
production_disciplines:
  - art
  - audio
  - narrative
  - UX
  - QA
validation:
  - "[[01_Core_Vision/Features/Living_Table#Проверка гипотезы]]"
---

# Вернуться к живому Столу

Понять, что изменилось в городе, и выбрать следующую работу через карту, предметы и голоса.

Сделать паузу между рейдами местом осмысленного выбора и тепла.

## За минуту

Возвращение меняет состав Схрона и видимые поводы на Столе. Игрок замечает адрес, рассматривает его причину, сопоставляет услугу с текущими вещами и закрепляет новую цель; для совместного выхода собирает группу.

## Сценарии и границы

- После потери найти центральный минимум и следующую работу.
- Внешний адрес исчез или изменился с ревизией: увидеть причину и fallback.
- Городское явление показывает публичный исход отдельно от личного вклада.
- Игрок пропускает необязательный разговор и продолжает подготовку.

Не добавлять прогулочное тело Бригадира, обязательный ежедневный обход или worker-dispatch.

## Кто исполняет и что видит игрок

Правила и переходы: [[08_World_Generation/Hub/Hub_Map_Table]], [[08_World_Generation/Hub/Hub_Services_Interaction]], [[08_World_Generation/Hub/Hub_Map_Interaction]], [[08_World_Generation/City_State/Civic_Event_Lifecycle]], [[08_World_Generation/Generation/Dual_State_POIs]], [[08_World_Generation/Hub/Party_Syndicate]].

Данные и авторские экземпляры: [[08_World_Generation/Registries/Registry_POIs]], [[03_Factions_Societies/Registries/Registry_Faction_Interfaces]].

Игроковые экраны, сигналы и объяснение отказа: [[08_World_Generation/Hub/Hub_Environment]], [[08_World_Generation/Hub/Time_Atmosphere]], [[04_Player_Entities/Entity_Grimoire]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Игрок задерживается ради нового смысла, но освоивший Стол быстро проходит знакомую подготовку.

- **Наблюдаем:** После возвращения игрок замечает конкретное последствие и принимает новый выбор без обхода всех пинов.
- **Доказательство и способ наблюдения:** Наблюдение первых и повторных возвратов, после потери и у уставшего опытного игрока.
- **Опровержение:** Тепло требует повторять один разговор либо оптимальный путь превращается в полный обход Стола.
- **Ответ:** Пересмотреть приоритет сигналов, сокращение повторов и связь повода с рейдом.

## MVP и производство

Первый срез: Выбор Пешки, осмотр вернувшегося груза, адрес и переход к следующей вылазке на одном Столе. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

Редкие поводы не должны стать FOMO-расписанием; ритм возвращения остаётся открытой задачей TODO.

UX и art связывают карту, вещи и живых людей; narrative и audio дают короткие реакции на последствия; QA проверяет путь без обязательной прогулки по Хабу.
