---
type: reference
status: draft
system: project_management
canonical_content: false
---

# Batch 9B — Canonize Life Closure: результат

Выполнено локально на main 2026-09-13, без commit/push/PR. Это отчёт об интеграции принятых решений, не gameplay owner. Правила разрешает [[04_Player_Entities/Life_Closure|Life Closure]] и его named consumers.

## Итоговый переход

~~~text
authored facts + authored terminal opportunity → OFFER_AVAILABLE
accept + confirm при валидных условиях → LifeClosureResolution → terminal projection
decline → окончательный отказ от этого offer, дальнейшая field life сохраняется
defer → тот же offer, пока сохраняются его реальные условия
~~~

Ordinary CLOSE_CIVIC сохраняет человека живым в городе и навсегда исключает ordinary deployment, recruitment/Spawn и cargo. Account reward не обязателен; другая Пешка также может получить собственное authored civic ending. Причинно независимая история может дать иной offer; отказ не является пожизненным отказом от всех окончаний.

## Удалённые правила

- Универсальный допуск по трём reserved и трём revealed manifestations; предел Personal Traits остаётся у Tags без изменений.
- Глобальный RETURN_TO_FIELD_FOREVER и обязательное немедленное решение при открытии Hub.
- Абсолютный запрет причинных downstream последствий. Заменён требованием нового terminal факта, named owner и конкретного unresolved дела.
- Положительные seeds про level-based Recognition и выращивание пригодных тел: их историческая предпосылка помечена отклонённой, текущий TODO направлен к принятой границе.

Новых общих life/maturity/biography scores, счётчиков развития или replacement rewards не введено.

## Death и Closure

При Death personal/embodied теряется, unfinished work переоценивается, completed results продолжают существовать под своими owners. Death не создаёт Closure.

При Closure embodied больше недоступно для deployment, unfinished work переоценивается, completed results не меняются самим окончанием. Только новый добровольный terminal поступок может дать одно специально authored внешнее следствие. Готовый ItemID, recipe за работу, источник, доказанный факт и выполненное обязательство получают результат при completion, без повторной выплаты при retirement.

## Ownership и anti-farming

- Life Closure: eligibility, arc/offer, confirmation, immutable LifeClosureResolution.
- Lifecycle Roster: terminal projection, Presence/deployability, отсутствие повторного deployment.
- Quest/work owners: собственные факты истории, unfinished работа и completion.
- Reputation/Pledge: своё отношение и право; личная связь не наследуется.
- Гримуар: источник и проверка знания.
- Recipe/Vendor/Service: собственный технический, экономический результат или интерфейс; не resolver судьбы.

У результата есть конкретная причина дела. Потребитель отдельно защищает повторную доставку события и повтор той же причины другим PawnID. Другой человек не создаёт второе уже разрешённое право. Нет generic payout, account XP, reputation bounty или reward value от stats/Scars/Proficiency/возраста/рейдов/числа CLOSED. Сохранённый результат не требует retired человека как работника, service condition или account modifier.

## Keeper boundary и намеренно открытое

Account Recognition по последствиям нескольких жизней не является Closure/death/retired counter и не создаёт Pawn-specific terminal offer.

Конкретная Keeper-ветка, физическая судьба человека, его информированное согласие, terminal необходимость и receiving owner остаются предметом будущего решения. Ни передача, ни смерть, ни потеря памяти, ни CLOSED_CIVIC для такой ветки, ни Archive/recipe/service reward не утверждены. UR-003 о Dawn также не решён побочно.

Research 9A сохранён без изменений как draft reference/non-canon. Его speculative истории и модели не импортированы. Полная account progression, permanent recipes, vendor ladder, новые tiers, Workbench и executable prototype не создавались.

## Файлы этого батча

Изменены 17 существующих файлов; добавлены contract guards и этот отчёт. Предыдущие подготовленные изменения других батчей сохранены.

- [[01_Core_Vision/Features/Pawn_Lifecycle]]
- [[02_World_Lore/The_Anchor]]
- [[03_Factions_Societies/Lore/The_Keepers]]
- [[03_Factions_Societies/Pledge_Contracts]]
- [[03_Factions_Societies/Quest_Engine]]
- [[03_Factions_Societies/Reputation_Rules]]
- [[04_Player_Entities/Entity_Grimoire]]
- [[04_Player_Entities/Grimoire_Truth_Triangulation]]
- [[04_Player_Entities/Life_Closure]]
- [[04_Player_Entities/Lifecycle_Roster]]
- [[04_Player_Entities/Shell_Construction]]
- [[04_Player_Entities/Tags_System]]
- [[06_Economy_Loot/Barter_System]]
- [[06_Economy_Loot/Vendor_Logic]]
- [[08_World_Generation/Hub/Hub_Services_Interaction]]
- [[09_Project_Management/TODO]]
- [[10_Reference/Reference Notes New]]
- tools/test_life_closure_contracts.py
- [[09_Project_Management/Batch9B_Life_Closure_Report|Этот отчёт]]

## Verification

- Полный unittest discover: **182 tests, OK**, включая 11 новых contract guards и прежние 171.
- Новые guards проверяют offer/refusal/defer, отсутствие универсального gate, terminal projection, Death/work boundary, named consequence и causal fact, dedup между PawnID, запрет passive CLOSED condition и незаданный Keeper reward. Негативные мутации отклоняют возврат gate, глобального отказа, reroll, unowned consequence и per-Pawn payout.
- Existing overhaul guards: **PASS, 0 violations**; canonical Frames = 0, Patterns = 0.
- Routes --check: **PASS**, пересборка не нужна: metadata маршрутов не менялась.
- Harness: **8 skills, 0 violations**.
- Vault guard и полный strict guard: **5 прежних MISSING_LINK_TARGET**, новых нет. Все пять находятся в [[10_Reference/Reference Note Экономика подготовки — материалы, находки и трансформации]]: Weapon_Core:64 (дважды), Magic_Batteries:182, Spawn_Logic:91, Calibration_Contract:78.
- Strict owner/consumer links и anchors в новых guards: **PASS**. Git diff --check: без ошибок.
- Проверки деклараций не являются runtime/UX-прототипом и не доказывают качество будущего контента или экономики.

**BATCH 9B COMPLETE**

Следующий отдельный шаг — выбрать конкретную authored terminal opportunity и проверить её причинность. Для Keeper-варианта сначала определить судьбу человека и основание неизбежного окончания; награды заранее не назначать.

