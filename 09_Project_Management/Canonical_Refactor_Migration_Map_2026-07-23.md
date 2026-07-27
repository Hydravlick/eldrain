---
type: migration_map
status: active
system: project_management
date: 2026-07-23
tags:
  - refactor
  - canon_migration
  - source_ownership
  - four_layers
related_files:
  - "[[09_Project_Management/Worldbuilding_Refactor_Roadmap_2026-07-23|Worldbuilding refactor roadmap]]"
  - "[[RAID_INGRESS_EGRESS_ARCHITECTURE_SPEC|Raid ingress/egress source proposal]]"
  - "[[BUILDCRAFT_ARCHITECTURE_SPEC|Buildcraft source proposal]]"
  - "[[T4_APEX_ENDGAME_LOOP_AND_PRODUCT_MODEL_PROPOSAL|T4 Apex source proposal]]"
  - "[[09_Project_Management/Refactor_Unresolved_Registry_2026-07-23|Unresolved registry]]"
---
# Карта миграции канонического рефактора

> Эта страница владеет только порядком переноса, картой источников и редакторскими ограничениями. Она не владеет runtime-правилами, состояниями, IDs, валидаторами или транзакциями: после миграции их единственными владельцами остаются профильные страницы систем.

## Цель и граница

Перенести принятый материал из дорожной карты миростроения, предложений Buildcraft, Raid ingress/egress, supplement и T4 Apex в активные канонические страницы. Перенос не меняет принятые решения и инварианты, не создаёт новые правила и не устраняет противоречия без явного авторского решения.

После полной и проверенной миграции каждый proposal-источник получает `status: superseded` и перестаёт быть источником истины. Неизменяемая [[10_Reference/Source Note — Переосмысление пяти древнейших народов Eldrain — 2026-07-20|исходная авторская заметка]] сохраняется как provenance; она не становится вторым каноническим владельцем правила.

## Семантические слои и порядок чтения

Слои определяют ответственность текста, а не структуру папок. Универсальная системная страница может последовательно раскрывать player promise, механику и технический контракт, если остаётся единственным владельцем одного предмета. Это исключение не относится к страницам сущностей: фракция, Очаг, народ, место, персонаж или иная сущность не получает runtime-authority только потому, что через неё игрок видит несколько систем.

1. **Lore.** Внутриигровая причинность, сеттинговые образы, история и терминология. Лор объясняет, почему явление существует, но не определяет его правила. Внутри этого слоя **Narrative** остаётся отдельным явно размеченным подразделом: он показывает значение события для мира, жителей, отношений и последствий, но не заменяет игроковую инструкцию и не владеет механикой.
2. **Player Experience / Presentation.** Что игрок видит, слышит, понимает, выбирает и по какой обратной связи узнаёт исход. Здесь допустимы только простые игровые и сеттинговые термины; IDs, owners, транзакции и внутренние состояния запрещены.
3. **Game Mechanics.** Читаемые правила, риски, последствия, условия и обратная связь. Короткая производная проекция нормативного правила допустима в предыдущих слоях, если она явно не создаёт второго owner.
4. **System Contract.** Единственные owners, states, validators, IDs, transactions, arbitration и failure handling. Этот слой живёт на профильных страницах систем, а не в `09_Project_Management`.

Порядок чтения: **Lore (с отдельным Narrative) → Player Experience / Presentation → Game Mechanics → System Contract**. Пользовательское описание не раскрывает backend-лексику, а системный контракт не подменяется метафорой.

## Сущность, интерфейс и системный владелец

Для сложной сущности применяется связка **страница сущности → реестр интерфейсов → владельцы систем**.

1. Страница сущности отвечает, чем объект является в мире: происхождение, обещание, люди, власть, имущество, отношения, быт, конфликт и цена ошибки.
2. Каждое самостоятельное игровое взаимодействие получает одну нормализованную запись интерфейса. Одна строка описывает одну роль сущности, один игроковый глагол или результат, одного `mechanic_owner_ref` и явную границу `does_not_own`.
3. Профильная системная страница остаётся единственным владельцем eligibility, состояния, стоимости, результата, арбитража и failure handling.
4. Страница сущности может показывать короткую ссылочную проекцию интерфейсов, но не повторяет их правила.
5. Отдельная player-experience страница создаётся только для уникальной многошаговой последовательности. Четыре файла на каждую сущность не являются целевой нормой.

Допустимые базовые роли сущности: `ADDRESS`, `ISSUER`, `PROVIDER`, `WITNESS`, `PRESENTER`, `CONSUMER`. Роль описывает участие, а не authority. Один Очаг может иметь любое число интерфейсов; ровно один владелец требуется не Очагу, а каждой активной строке интерфейса. Отсутствующий владелец фиксируется как `MISSING_OWNER`.

## Правило единственного владельца

- Одно нормативное правило имеет одного canonical owner.
- Другие слои могут содержать короткую, понятную и явно производную проекцию правила, если она помогает чтению; они не повторяют условия, исключения или authority.
- При переносе текст перемещается к owner, а не копируется. В прежней точке остаются только производная проекция и ссылка, когда они нужны для понимания.
- Реестры держат стабильные структурированные записи, а не вторую прозу или второй resolver.
- `09_Project_Management` содержит только ADR, migration map, audits и unresolved registry.

## Источники и порядок миграции

| Поток | Исходники | Порядок | Граница переноса |
|---|---|---:|---|
| Raid и Apex | `RAID_INGRESS_EGRESS_ARCHITECTURE_SPEC.md`, supplement, `T4_APEX_ENDGAME_LOOP_AND_PRODUCT_MODEL_PROPOSAL.md` | 1 | Сначала общий lifecycle boundary, затем ingress/egress, Seal/Dawn, Apex, extraction, economy и player projection; спорные нормы не мигрируются |
| Buildcraft | `BUILDCRAFT_ARCHITECTURE_SPEC.md` | 2 | Потребляет уже назначенные Raid/Recovery/Return owners; затем переносит player lifecycle, First Return, roster, tags, Thermos и Double Paradox |
| Миростроение | Исходная заметка, общая дорожная карта и четыре профильных плана | 3 | Source Note остаётся provenance; внутри потока обязательный порядок: Порог → культурная грамматика → пять культур → город и Очаги → граница лора и механики |
| Интеграция | Все затронутые владельцы | 4 | Ссылки, registry coverage, `Architecture_MVP`, navigation и audits без создания новой runtime-authority |

### Общая граница Raid и Buildcraft

Чтобы порядок `Raid/T4 → Buildcraft` не создал циклических владельцев, первый поток начинает с минимального общего контракта:

- `Lifecycle_Roster` владеет состояниями Пешки, Presence, единственным account-slot и производными roster-counts;
- `Last_Thread_Recovery` владеет eligibility личной Последней нити, летальным intercept и идемпотентным `RecoveryRequest`, но не slot или attempt lifecycle;
- `Recovery_Lifecycle` принимает или отклоняет запрос и владеет публичным `RecoveryCase`, поиском, recovery binding-attempts, expiry и resolution;
- Raid ingress владеет target binding, admission и Breach;
- `Return_Manifest_Contract` владеет физическим manifest обычного Threshold и Dawn;
- Server Lifecycle владеет Seal/Dawn total order.

Ни один из двух потоков не повторяет состояния соседнего владельца. Первый этап создаёт и связывает эти boundaries, после чего Raid/T4 переносит public-session contract, а Buildcraft — личную жизнь Пешки и остальные системы.

## Требования к каждому перенесённому фрагменту

1. Найти один канонический owner и прямые потребители.
2. Отметить слой текста и сохранить только лексику, разрешённую этому слою.
3. Перенести правило или определение полностью к owner.
4. Заменить старые копии краткой производной проекцией либо ссылкой.
5. Проверить YAML, root-relative wikilinks, существование owners и отсутствие второго источника истины.
6. Если источник противоречит другому источнику или активному канону, не переносить норму и внести запись в [[09_Project_Management/Refactor_Unresolved_Registry_2026-07-23|unresolved registry]].

## Контракт агентного исполнения

Интеллектуальное решение и механическая запись разделены.

### Архитектор-контроллер

- читает proposal, активный канон и прямые зависимости;
- классифицирует каждый фрагмент как `AUTHOR CONSTRAINT`, `GDD FACT`, `CANON DRIFT`, `EMPIRICAL UNKNOWN`, `CONTENT GAP` или unresolved conflict;
- назначает точного owner, интерфейсы и отрицательные границы;
- определяет порядок authority switch и критерии приёмки;
- не передаёт писателю конкурирующие варианты без статуса.

### Агент-писатель

- получает один bounded brief с точными источниками, целевыми файлами и уже принятыми owner-решениями;
- не проектирует новую механику, не дописывает отсутствующий лор и не выбирает между конфликтующими нормами;
- переносит правило полностью к owner, создаёт ссылки и нормализованные registry rows, затем удаляет старую копию;
- оставляет `EMPIRICAL UNKNOWN`, `MISSING_OWNER` и unresolved decision видимыми;
- не меняет соседний поток «для согласованности», если brief не называет его потребителем.

### Агент-проверяющий

- проверяет только изменённый bounded scope и его прямых потребителей;
- отдельно выдаёт verdict по owner uniqueness, canonical coverage, player-facing readability и link validity;
- возвращает нарушение писателю; не исправляет его собственной альтернативной архитектурой;
- запрещает `superseded`, пока активный consumer всё ещё читает proposal или старый owner.

## Очередь исполнительных агентов

### Статус исполнения

| Этап | Статус | Проверка |
|---|---|---|
| Raid/T4: proposed focused-owner foundation | `complete` | 6 файлов, 21 направленный интерфейс; independent review `APPROVED`; active authority ещё не переключена |
| Raid/T4: Server Lifecycle и regional service | `complete` | 2 active owner pages; independent review `APPROVED`; legacy claims удалены в bounded scope |
| Raid/T4: topology, solvency, Threshold и return consumers | `pending` | следующий bounded пакет |
| Остальные этапы | `pending` | запуск только после приёмки предыдущего владельца |

### Агент 1 — Raid ingress/egress и T4 Apex

**Источники:** `RAID_INGRESS_EGRESS_ARCHITECTURE_SPEC.md`, `T4_APEX_ENDGAME_LOOP_AND_PRODUCT_MODEL_PROPOSAL.md`.

**Сначала создаёт границы:**

- `Lifecycle_Roster` — Pawn/Presence/account-slot;
- `Last_Thread_Recovery` — lethal intercept и `RecoveryRequest`;
- `Recovery_Lifecycle` — Case/search/binding attempts/expiry/resolution;
- Raid approach/entry — target binding/admission/Breach;
- `Return_Manifest_Contract` — Threshold/Dawn physical return;
- Server Lifecycle — phase clock/Seal/Dawn order.

**Затем переносит:** rolling pool, phase clock, Approach/Quote/Breach, egress solvency, Threshold/Sync, ReturnManifest, Recovery in public sector, Apex last hour, Dawn outcomes, loot/progression/product boundaries.

**Не переносит:** `UR-001`, `UR-002`, `UR-003`, числовые коридоры, buy-to-play гипотезу и будущие Apex families как готовый канон.

**Создаёт focused owners:**

- `08_World_Generation/Generation/19_Raid_Approach_and_Entry.md`;
- `08_World_Generation/Generation/20_Egress_Solvency.md`;
- `04_Player_Entities/Recovery_Lifecycle.md`;
- `06_Economy_Loot/Return_Manifest_Contract.md`;
- `08_World_Generation/Anomaly/17_Apex_Last_Hour.md`.

**Создаёт структурированные источники:**

- `08_World_Generation/_Registries/Registry_Raid_Interfaces.md`;
- `08_World_Generation/_Registries/Registry_Apex_Families.md`;
- `08_World_Generation/_Registries/Registry_Approach_Profiles.md`;
- `08_World_Generation/_Registries/Registry_Threshold_Families.md`;
- `05_Combat_Survival/_Registries/Registry_Control_Profiles.md`.

**Расширяет без смены предмета:** `02_Core_Loop`, `Server_Lifecycle`, `Async_Timers`, `Hub_Map_Table`, `Insertion_Logic`, `Extraction_System`, `World_Topology`, `Sector_Content_Rules`, `Persistence_Ledger`, `Inventory_Architecture`, `Extraction_Stabilization_Loop`, `Loot_Distribution`, `Gear_Progression`, `Pledge_Contracts` и `Party_Syndicate`.

### Агент 2 — Buildcraft

**Источник:** `BUILDCRAFT_ARCHITECTURE_SPEC.md`.

**Потребляет без переопределения:** владельцев Presence, RecoveryCase, Raid ingress, Seal/Dawn и ReturnManifest из этапа 1.

**Переносит:** Known Self / Unknown World, roster lifecycle, Continuity Admission, First Return assignment, tags, Foundlings, Parameter Contracts, Dissonance boundary, Thermos, Double Paradox и Life Closure.

**Не переносит:** спорные Dawn reveal/closure branches и Recovery clock; не создаёт второй Recovery attempt, binding или manifest resolver.

**Создаёт focused owners и registries:**

- `04_Player_Entities/Last_Thread_Recovery.md`;
- `04_Player_Entities/Life_Closure.md`;
- `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`;
- `04_Player_Entities/_Registries/Registry_Double_Paradox_Vectors.md`;
- `04_Player_Entities/_Matrices/Registry_Double_Paradox_Reviews.md`.

**Расширяет без дублирования Raid owners:** `Lifecycle_Roster`, `Spawn_Logic`, `Tags_System`, `Registry_Tags`, `Trait_Development`, `Shell_Foundlings`, `Combat_Profile_Pipeline`, `Dissonance_System`, `Thermos_System`, Thermos registries, `Two_Paradox_Vector_Matrix`, `00_Synergy_Map`, `MVP_3x3_Design_Contract` и player-facing Core Vision pages.

### Агент 3 — Конвергентный технологический порог

**Источники:** неизменяемая Source Note как provenance и `Convergent_Technological_Threshold_Refactor_Plan_2026-07-23.md`.

**Переносит:** росток против инструкции, пять классов операций, шесть общественных признаков порога, материальную взаимопонятность и границы тайны Предтеч.

**Не выбирает:** цель Предтеч, критерий отбора, общие единицы, универсальность порога или распространение на будущие народы.

**Изменяет:** `The_Ark`, `Energy_Concept`, `Magipunk_Physics`, затем общий contract в `People_Design_Framework` и `Culture_Revision_Audit`. `Magic_Batteries` и `Art_Direction_Material_Grammar` только проверяет на границу владельцев.

### Агент 4 — Пять древнейших народов

**Источники:** неизменяемая Source Note, выполненный этап Порога и `Five_Ancient_Peoples_Refactor_Plan_2026-07-23.md`.

**Переносит:** cultural framework, четыре эпохи, социальный низ, преступление конца, новое право и связь с authored world content.

**Не дописывает:** оборванную жабью фразу и отсутствующие исторические решения Ящериц, Белок и Ежей. Такие места остаются `UNDERDEFINED` до авторского решения.

**Изменяет после снятия соответствующих ворот:** `Rat_Culture`, `Toad_Culture`, `Lizard_Culture`, `Squirrel_Culture`, `Hedgehog_Culture`, затем проверяет пять `04_Player_Entities/Races/*.md`, `Culture_Language` и `City_Genesis`.

### Агент 5 — Город, Очаги и граница механики

**Источники:** выполненные культурные страницы, `Civic_World_and_Hearths_Refactor_Plan_2026-07-23.md`, затем `Lore_Gameplay_Boundary_Refactor_Plan_2026-07-23.md`.

**Порядок:** `City_Genesis` → `Civic_Order` → `Hearth_Anatomy` → институциональный проход восьми Очагов → перенос системных правил к owners → `Registry_Faction_Interfaces` → удаление дубликатов из Lore.

**Не делает:** один `primary_system` на Очаг, центральное правительство, систему образования, новые награды или owner из лорной метафоры.

**Создаёт:** `03_Factions_Societies/Lore/Civic_Order.md`, `03_Factions_Societies/Lore/Hearth_Anatomy.md`, системный `03_Factions_Societies/Faction_Address_System.md` и нормализованные записи в уже созданном `Registry_Faction_Interfaces`.

**Изменяет:** восемь главных страниц Очагов, малые сети, `Civic_Ethos_Under_Lamps`, `City_Genesis`, `Registry_Factions` и только те профильные mechanic owners, которые прямо названы интерфейсным аудитом.

### Агент 6 — Интеграционный проверяющий

Проверяет:

- один owner на правило и одну активную interface row;
- отсутствие активных ссылок на deprecated/superseded sources;
- отсутствие runtime-лексики на entity pages;
- отсутствие lore-причинности в system contracts;
- существование root-relative wikilinks и headings;
- видимость `MISSING_OWNER`, unresolved decisions и пустого registry coverage;
- два маршрута чтения: человек понимает сущность без backend, исполнитель реализует механику без толкования лора.

## Принятое решение, ожидающее миграции

| Решение | Статус | Будущие профильные owners | Граница |
|---|---|---|---|
| Dawn full return для живого `STANDARD` Presence | `APPROVED / PENDING_MIGRATION` | Pawn lifecycle / LifecycleResolver; Extraction/Return; Inventory/Custody; player-facing extraction flow | На Dawn стандартная Пешка возвращается с полным eligible физически удерживаемым custody через единственный ReturnManifest. `RECOVERY` получает только `RECOVERED`, без cargo, лута и стандартной награды. |

Это решение не является конфликтом. Его player-facing проекция объясняет переживание рассвета и итог возвращения простыми словами; точные owners, доказательства, порядок арбитража и failure handling живут только у профильных систем.

## Условия завершения

- Каждый принятый фрагмент из источников живёт ровно у одного канонического owner.
- Порядок чтения и терминологические границы выдержаны во всех затронутых страницах.
- Proposal-источники имеют `status: superseded` только после проверки их карты переноса.
- Неизменяемая авторская заметка сохранена как provenance.
- Все найденные противоречия перечислены отдельно и не замаскированы редактурой.
- Навигация и ссылки ведут в действующий канон, а не в superseded proposal.
