---
type: feature
status: active
system: player_experience
feature_id: personal_development
feature_order: 13
display_name: Прожить собственную историю Пешки
player_promise: Узнавать приобретённые свойства человека и строить дальнейшие решения вокруг его опыта.
expected_dynamics: Игрок приспосабливается к человеку, вместо выбраковки всех профилей вне решённой меты.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[04_Player_Entities/Tags_System]]"
  - "[[04_Player_Entities/Combat_Profile_Pipeline]]"
  - "[[04_Player_Entities/Proficiency_Arsenal]]"
  - "[[04_Player_Entities/Shell_Foundlings]]"
  - "[[04_Player_Entities/Life_Closure]]"
data_sources:
  - "[[04_Player_Entities/Registries/Registry_Tags]]"
  - "[[04_Player_Entities/Registries/Registry_Combos]]"
ux_surfaces:
  - "[[04_Player_Entities/Entity_Grimoire]]"
  - "[[07_Gear_Inventory/Item_Attributes_UI]]"
production_disciplines:
  - narrative
  - UX
  - VFX
  - gameplay
  - QA
validation:
  - "[[01_Core_Vision/Features/Personal_Development#Проверка гипотезы]]"
---

# Прожить собственную историю Пешки

Узнавать приобретённые свойства человека и строить дальнейшие решения вокруг его опыта.

Сделать развитие продолжением жизни, которое не заменяет полевой профиль и не переносится на нового человека.

## За минуту

Событие жизни назначает или раскрывает свойство по правилу владельца. Игрок читает условие, локальный эффект и долг, проверяет его в составе профиля и меняет привычку следующей вылазки. Завершение жизни сохраняет смысл человека без передачи его механической силы.

## Сценарии и границы

- Раскрыть заранее назначенное свойство после соответствующего события.
- Условный тег неактивен: понять условие, не получить новое свободное место.
- Origin найденыша учитывается в том же личном контракте.
- Новая Пешка после утраты не наследует теги погибшей.

Не вводить дерево, tag-shopping, повторный roll или account-множитель.

## Кто исполняет и что видит игрок

Правила и переходы: [[04_Player_Entities/Tags_System]], [[04_Player_Entities/Combat_Profile_Pipeline]], [[04_Player_Entities/Proficiency_Arsenal]], [[04_Player_Entities/Shell_Foundlings]], [[04_Player_Entities/Life_Closure]].

Данные и авторские экземпляры: [[04_Player_Entities/Registries/Registry_Tags]], [[04_Player_Entities/Registries/Registry_Combos]].

Игроковые экраны, сигналы и объяснение отказа: [[04_Player_Entities/Entity_Grimoire]], [[07_Gear_Inventory/Item_Attributes_UI]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Игрок приспосабливается к человеку, вместо выбраковки всех профилей вне решённой меты.

- **Наблюдаем:** В повторной вылазке игрок использует конкретное личное свойство и называет его ограничение.
- **Доказательство и способ наблюдения:** Продольное наблюдение нескольких жизней, редких конфигураций и решений после знакомства с метой.
- **Опровержение:** Рациональный путь — массово заменять людей ради желаемого тега либо свойство остаётся незаметным.
- **Ответ:** Пересмотреть источники, видимость и локальные пересечения; не выдавать силу за ценность личности.

## MVP и производство

Первый срез: Известный профиль и заранее назначенный First Return при обычном возвращении; один личный тег имеет видимые действие и цену. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

UR-001: раскрытие First Return при STANDARD Dawn. Feature не выбирает эту ветвь.

Narrative связывает проявление с человеком; UX отличает раскрытие от выдачи случайной силы; combat design и QA проверяют локальность эффекта и отсутствие reroll-оптимума.
