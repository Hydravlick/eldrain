---
type: feature
status: active
system: player_experience
feature_id: pawn_lifecycle
feature_order: 1
display_name: Живые Пешки и цена возвращения
player_promise: Выбрать конкретного человека для вылазки и понять его судьбу после успеха, потери или спасения.
expected_dynamics: Привязанность к людям сосуществует с готовностью снова выйти после потери.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[04_Player_Entities/Lifecycle_Roster]]"
  - "[[04_Player_Entities/Lifecycle_Resolver]]"
  - "[[04_Player_Entities/Last_Thread_Recovery]]"
  - "[[04_Player_Entities/Recovery_Lifecycle]]"
  - "[[04_Player_Entities/Life_Closure]]"
  - "[[04_Player_Entities/Spawn_Logic]]"
  - "[[04_Player_Entities/Shell_Foundlings]]"
data_sources:
  - "[[04_Player_Entities/Registries/Registry_Races]]"
  - "[[04_Player_Entities/Registries/Registry_Specs]]"
ux_surfaces:
  - "[[04_Player_Entities/Entity_Grimoire]]"
production_disciplines:
  - UX
  - narrative
  - gameplay
  - QA
validation:
  - "[[01_Core_Vision/Features/Pawn_Lifecycle#Проверка гипотезы]]"
---

# Живые Пешки и цена возвращения

Выбрать конкретного человека для вылазки и понять его судьбу после успеха, потери или спасения.

Связать ставку рейда с жизнью Пешки, сохранив понятный путь обратно к игре после потери.

## За минуту

На Столе игрок выбирает готовую Пешку. После рейда ростер показывает результат её личного lifecycle; незавершённое спасение остаётся отдельным делом. При утрате доступного состава Первый Приём проверяет право на нового Ward.

## Сценарии и границы

- Готовая Пешка возвращается и становится кандидатом следующей вылазки.
- Смертельное событие получает одно решение; Last Thread проверяется только по переданному исходу.
- Нет готовых Пешек, но есть CARE или незавершённая Recovery: интерфейс показывает решение Continuity Admission и следующий доступный шаг.
- Найдёныш спасён, но это ещё не автоматическое присоединение к ростеру.

Не выбирать судьбу за Lifecycle Resolver и не превращать ростер в оценку стоимости людей.

## Кто исполняет и что видит игрок

Правила и переходы: [[04_Player_Entities/Lifecycle_Roster]], [[04_Player_Entities/Lifecycle_Resolver]], [[04_Player_Entities/Last_Thread_Recovery]], [[04_Player_Entities/Recovery_Lifecycle]], [[04_Player_Entities/Life_Closure]], [[04_Player_Entities/Spawn_Logic]], [[04_Player_Entities/Shell_Foundlings]].

Данные и авторские экземпляры: [[04_Player_Entities/Registries/Registry_Races]], [[04_Player_Entities/Registries/Registry_Specs]].

Игроковые экраны, сигналы и объяснение отказа: [[04_Player_Entities/Entity_Grimoire]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Привязанность к людям сосуществует с готовностью снова выйти после потери.

- **Наблюдаем:** После потери игрок объясняет судьбу Пешки и самостоятельно находит следующий доступный шаг.
- **Доказательство и способ наблюдения:** Наблюдение первых потерь и повторных вылазок; интервью после CARE, смерти и спасения.
- **Опровержение:** Игрок воспринимает новый Ward как продолжение погибшего или не понимает, почему не может выйти.
- **Ответ:** Пересмотреть объяснение состояний и доступность следующего шага; не вводить скрытую защиту от последствий.

## MVP и производство

Первый срез: Одна выбранная Пешка, успешное возвращение, потеря и следующий доступный вход; отдельный тест показывает незавершённую Recovery без ложного обещания срока. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

UR-002: полный fail/retry-контракт Recovery; UR-003: Dawn и Life Closure. Эти ветви остаются открытыми у владельцев.

UX связывает ростер с объяснением исхода; narrative сохраняет имя и причину привязанности; gameplay и QA воспроизводят потерю и повторный вход.
