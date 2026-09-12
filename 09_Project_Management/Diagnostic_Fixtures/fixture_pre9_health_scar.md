---
type: diagnostic
system: project_management
status: draft
publication_state: diagnostic_fixture
canonical_content: false
fixture_id: fixture_pre9_health_scar
---
# Pre-9 — Health & Scar: итог интеграции

Принятое решение находится в действующих owners, перечисленных ниже. Этот отчёт фиксирует проверку и не становится дополнительным health/Scar resolver. **Verdict: PRE-9 COMPLETE.** Полный Life Cycle / Closure не перерабатывался; commit/push/PR не выполнялись.

## Owners и затронутые потребители

- [[05_Combat_Survival/Combat_Consumables]] — единственный HEALTH; три значения, постоянные потери, обычная/полевая медицина, бесплатный Hub recovery и UI причин.
- [[04_Player_Entities/Tags_System]] — Scar identity, embodied consequence, eligibility/resolve и сохранение lifetime history после лечения.
- [[04_Player_Entities/Body_Morphology_Contract]] — граница последствий Scar с Morphology revision; Health туда не переносится.
- [[06_Economy_Loot/Barter_System]] — адресованный результат лечения в существующей RecipeTransaction, реальные ресурсы и атомарность.
- [[08_World_Generation/Hub/Hub_Services_Interaction]] — доступ, выбор пациента/Scar и точный preview; Facility не пишет Health.
- [[07_Gear_Inventory/Registries/Registry_CraftingRecipes]] — schema адресованного treatment outcome без production-рецептов.
- [[05_Combat_Survival/Magic_Batteries]], [[05_Combat_Survival/Status_Effects]], [[05_Combat_Survival/Registries/Registry_StatusEffects]] — различение acute cantrip debt и permanent Scar, eligibility перед Scar-producing Commit.
- [[01_Core_Vision/Features/Living_Table]], [[01_Core_Vision/Player_Mechanics_Glossary]], [[01_Core_Vision/Schema_Glossary]] — согласованное объяснение игроку и terminology.
- `tools/test_health_scar_contracts.py` — 7 новых проверок деклараций/ownership с отрицательными случаями.

Изменены 12 существующих страниц и добавлены тесты/этот отчёт. Локальные изменения Batch 7/8, существовавшие до Pre-9, сохранены.

## Контрольные переходы

Порядок чисел ниже: **MaxCapacity / FieldCapacity / CurrentHP**. Это иллюстративные входы для разбора принятого контракта, не production balance.

| Исходное состояние | Принятое событие | Итог и следующий выбор |
|---|---|---|
| 100 / 100 / 100 | Обычный damage 20 | 100 / 100 / 80; обычное лечение ограничено FieldCapacity |
| 100 / 100 / 80 | Объявленная recoverable capacity-loss 30 | 100 / 70 / 70; обычное лечение не вернёт потерянную ёмкость |
| 100 / 70 / 70 | Полевая медицина возвращает 15 ёмкости | 100 / 85 / 70; здоровье не заполнилось само |
| 100 / 100 / 95 | Один конкретный Scar с permanent_capacity_loss 10 | 90 / 90 / 90; причина остаётся в этом Scar |
| 90 / 70 / 40, этот Scar active | Успешное возвращение живой Пешки, бесплатная медицина | 90 / 90 / 90; Scar active и его потеря максимума сохраняются |
| 90 / 90 / 90, этот Scar active | Eligible адресное лечение с реальными ресурсами и confirm | После прекращения этого последствия Health даёт 100 / 90 / 90 при отсутствии иных permanent modifiers; последующий Hub recovery — 100 / 100 / 100 |
| 100 / 100 / 100, functional Scar active | То же адресное лечение подходящим service | Прекращается объявленное функциональное последствие; искусственного HP-loss/HP-бонуса нет |
| Два активных Scar с разными причинами | Лечится только один | Второй остаётся; максимум/функции пересчитываются по оставшимся источникам |
| Не хватает inputs либо Scar/revision уже изменены | Confirm устаревшего preview | До commit ресурсы и Scar не меняются; другой пациент не подставляется |
| Та же успешная transaction повторена | Retry | Прежний result, без повторного расхода/удаления потерь |
| Подтверждённый смертельный исход | Запрос базовой медицины/treatment | Отказ как revive; прежний lifecycle outcome не меняется |

Ни FieldCapacity, ни CurrentHP не превышают постоянный максимум; четвёртого числа здоровья и общего ScarredHP pool нет. Новый UI пример — `Max Health: 90` с причиной `Burned Lung: -10 Max Health`, а не отдельная постоянная шкала.

## Audit и исправленные коллизии

1. `BaseCapacity` заменён на `MaxCapacity` в действующем Health и Hub consumer; в активных страницах доменов `01_`–`08_` прежнего имени не осталось. Изначальное значение тела до последствий не сохранено как второй health stat.
2. Формулировки «лечение не удаляет Scar» уточнены до **обычной бесплатной медицины**; отдельное платное разрешение конкретного Scar теперь имеет owner, eligibility и ресурсную транзакцию. Бесплатная медицина больше не содержит оговорки, допускающей неявное удаление permanent consequences.
3. `SOURCE_CONFLICT` исправлен в [[05_Combat_Survival/Combat_Consumables]]: прежнее прямое объявление смерти при нуле HP обходило [[04_Player_Entities/Lifecycle_Resolver]]. Теперь Health передаёт lethal event; resolver/Last Thread/Closure не перерабатываются и новых revive paths нет.
4. Коллизия обязательного permanent Scar из Cantrip с ограничением lifetime slots в [[04_Player_Entities/Tags_System]] закрыта проверкой Scar eligibility до Commit в [[05_Combat_Survival/Magic_Batteries]]. При невозможности законно записать последствие выбранный Cantrip отклоняется до эффекта/расхода; постоянная цена не подменяется временным надрывом. Лечение не освобождает занятое lifetime-место и не стирает reveal history.
5. `RecipeTransaction` допускает узкий адресованный body outcome лечения. Facility не отправляет пациента/его последствие в общий инвентарь и не становится владельцем телесных чисел.

Проверены [[04_Player_Entities/Lifecycle_Roster]], [[04_Player_Entities/Lifecycle_Resolver]], [[04_Player_Entities/Last_Thread_Recovery]], [[04_Player_Entities/Recovery_Lifecycle]] и [[04_Player_Entities/Life_Closure]]. Их состояния, условия исхода, CARE/READY и closure eligibility не менялись. Недостающего health owner не выявлено; его прежняя страница теперь явно объявляет `canonical_id: HEALTH` и узкие health ownership keys.

## Verification и Batch 9

Полный suite: **171 tests, OK**, включая 7 новых. Overhaul/Pre-7 guards — **PASS, 0 violations**, canonical Frames/Patterns — 0/0. Routes check проходит без регенерации; harness — 8 skills, 0 violations. Новые тесты проверяют одну health authority, source-scoped capacity loss, отсутствие бесплатного Scar removal/четвёртого stat, направленность Facility transaction и законность cantrip Scar handoff. Это проверки GDD declarations, не заявление о существующем игровом health engine.

Общий `vault_guard` сохраняет 5 прежних `MISSING_LINK_TARGET` в reference-заметке, уже зафиксированных Batch 7/8; они не относятся к Pre-9. Исправление этих unrelated-ссылок в объём работы не включалось.

Для **Batch 9: Life Cycle / Closure + Representative Content** остаются конкретные Scar definitions, eligibility и реальные inputs отдельных services, а также их применение к различным lifecycle outcomes в рамках существующих owners. История resolved Scar/lifetime slots не должна превращаться в reroll или обнуляться при Closure. Цена лечения и каталог Facility пока не заданы; это content/calibration, не пробел общего treatment contract. Таймеры, daily cooldown, случайное исчезновение Scar, универсальная Scar currency и новое воскрешение не введены.
