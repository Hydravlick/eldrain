---
status: active
system: combat_survival_registry
registry_type: weapon_definitions
type: registry
index_route: owner
index_group: combat_survival
index_order: 20
index_summary: "Хранит схемы и публикацию оружейных Frame и Pattern."
read_when: "Когда нужны поля Frame/Pattern и проверка допуска оружейного контента к публикации."
---
# Реестр оружейных определений

Реестр задаёт схему двух уровней определений и показывает опубликованные записи. Данные каждого Frame и Pattern принадлежат его странице `type: entity`; реестр не хранит вторую копию. Ответственности уровней описаны в [[05_Combat_Survival/Weapon_Core|Weapon Core]], исполнение — в [[05_Combat_Survival/Combat_Three_Debts|Action contract]]. Физические ItemID здесь не регистрируются.

## Публикация

`status` использует общий lifecycle документов vault. Отдельное поле `publication_state` отличает назначение оружейного контента; `canonical_content` — явный boolean, а не вывод из наличия ID.

| Назначение | `status` | `publication_state` | `canonical_content` |
|---|---|---|---|
| Действующее каноническое определение | `active` | `canonical` | `true` |
| Диагностический fixture | `draft` | `diagnostic_fixture` | `false` |
| Неопубликованный проект | `draft` | `unpublished` | `false` |

Активный арсенал включает только записи, удовлетворяющие **всем трём** условиям первой строки. Fixtures выбираются отдельно по второй строке и никогда не попадают в канонический счётчик. Отсутствующее поле не означает разрешение публикации.

Нулевой corpus активных Frames/Patterns допустим. Неопубликованные определения и fixtures не становятся fallback действующего арсенала.

Следующий контентный шаг — diagnostic fixtures после schema gate. Служебные ID имеют префикс `fixture_` (например, `fixture_close_1h`); эта договорённость не создаёт записей. Реальные taxonomy, названия, starting arsenal и Patterns определяются позднее, после проверки fixtures, без предпочтения прежней taxonomy.

## Frame record

Поля находятся во frontmatter страницы с `entity_kind: weapon_frame`.

| Поле | Требование |
|---|---|
| `frame_id` | Уникальный стабильный ID определения |
| `status`, `publication_state`, `canonical_content` | Согласованная строка publication contract |
| `spatial_job` | Какую пространственную задачу покупает язык оружия |
| `positioning_contract` | Характерная дистанция и позиция |
| `bodily_organization` | Переносимая организация тела |
| `operation_classes` | Непустой список допустимых классов операций |
| `commitment_character` | Характер принятого обязательства |
| `natural_debt` | Характерная цена, сохраняемая вариациями |
| `counterplay_contract` | Разумный тип ответа противника |
| `variation_limits` | Допустимое пространство Pattern variation |
| `learnability_prior` | Что игрок заранее знает о незнакомой конструкции |
| `boundary_notes` | Обоснование границы Frame по тесту Weapon Core |

Точное расписание атак, runtime Recovery, Heat и magazine не являются полями Frame record.

## Pattern record

Поля находятся во frontmatter страницы с `entity_kind: weapon_pattern`.

| Поле | Требование |
|---|---|
| `pattern_id` | Уникальный стабильный ID повторяемой конструкции |
| `frame_id` | Ссылка по ID на единственный Frame |
| `status`, `publication_state`, `canonical_content` | Согласованная строка publication contract |
| `hand_requirement` | Объявленное требование конструкции к рукам; не текущая занятость |
| `primary_operation` | Локальный ID основной operation definition |
| `alt_operation` | Необязательный локальный ID Alt operation |
| `supports_focus` | Явный boolean; наличие Focus не подразумевается |
| `focus_operation` | Обязателен при `supports_focus: true`, отсутствует иначе |
| `service_contract_ref` | Необязательная ссылка на определение операции обслуживания |
| `magazine_capacity` | Необязательная положительная целая ёмкость, только для magazine model |
| `shot_consumption` | Вместе с capacity: authored стоимость/правило выпуска, обычно 1 |
| `reload_service_ref` | Вместе с capacity: ссылка на reload definition/контракт; может совпадать с `service_contract_ref` |
| `operation_ids` | Непустой список определённых на этой странице операций |

Operation definitions в теле Pattern описывают moveset, траектории, подготовку, порядок действий, видимые состояния конструкции и поведение выпуска. Каждое определение имеет inline-поле `operation_id`; список `operation_ids` перечисляет эти ID. Primary/Alt/Focus ссылаются на них. Сервисное требование может ссылаться на отдельного владельца; оно не записывает текущий расход ресурса или Action debt. Magazine-тройка объявляется целиком либо отсутствует целиком. Числовая стоимость положительна и не превышает capacity; именованное правило требует definition. `magazine_current` не является полем Pattern. Runtime и списание принадлежат [[05_Combat_Survival/Weapon_Ranged|Weapon Ranged]], полная Battery transaction — [[05_Combat_Survival/Magic_Batteries|Magic Batteries]]. Ни одной реальной magazine-конфигурации эта схема не публикует.

Канонический Pattern ссылается только на канонический Frame. Fixture может ссылаться на канонический либо diagnostic Frame. Draft может ссылаться на draft, fixture или canonical Frame; deprecated-материал не становится его действующей зависимостью. Незаполненный draft можно хранить, но нельзя публиковать или выдавать за готовый fixture.

## Контракт доступа

[[04_Player_Entities/Proficiency_Arsenal#Контракт доступа|Proficiency]] хранится как `Pawn ↔ Frame`. При `prof >= 1` все Patterns этого Frame предоставляют полный собственный moveset. Ни Pattern, ни ItemID не получают своего уровня prof. Mastery, его unlocks/steps/expressions и prof-specific branches не являются требованиями валидности оружейного определения.

## Definition и physical identity

Повторяемая конструкция имеет `pattern_id`; конкретная физическая вещь — ItemID со ссылкой на Pattern. Поле `instance_id` не используется в definition schema. Обычный ItemID не создаёт новый moveset.

Frame Class / `load_tier` остаётся отдельным нерешённым gear-progression axis по [[05_Combat_Survival/Weapon_Core#4. Публикация и граница gear progression|границе Weapon Core]], не обязательным полем Frame/Pattern и не prerequisite Diagnostic Fixtures.

## Активные Frames

```dataview
TABLE frame_id AS "Frame", spatial_job AS "Пространственная работа", natural_debt AS "Цена"
WHERE type = "entity" AND entity_kind = "weapon_frame" AND status = "active" AND publication_state = "canonical" AND canonical_content = true
SORT frame_id ASC
```

## Активные Patterns

```dataview
TABLE pattern_id AS "Pattern", frame_id AS "Frame", hand_requirement AS "Руки", supports_focus AS "Focus"
WHERE type = "entity" AND entity_kind = "weapon_pattern" AND status = "active" AND publication_state = "canonical" AND canonical_content = true
SORT pattern_id ASC
```

Обе пустые таблицы означают отсутствие опубликованного контента, а не ошибку схемы. Лут-проекции читают только опубликованные Patterns; правила распределения остаются у [[06_Economy_Loot/Loot_Distribution|Loot Distribution]].

## Проверка

`tools/check_overhaul_contracts.py` проверяет publication tuple, уникальность ID, Frame references, ссылки на локальные операции, отсутствие legacy `instance_id` и Mastery/prof-полей в публикуемых определениях. При нулевом контенте проверка проходит. Переносимость Frame и learnability Pattern требуют проверки поведения; структурный тест не доказывает их качество.

Focus definition использует общую [[05_Combat_Survival/Combat_Three_Debts#Targeting и одна Preparation|Targeting / Preparation grammar]]. Наличие `supports_focus` у Pattern не отменяет single-owner Set restriction из [[05_Combat_Survival/Weapon_Core#Weapon Focus|Weapon Core]]. Ни runtime Preparation, ни target selection не хранятся в Pattern.
