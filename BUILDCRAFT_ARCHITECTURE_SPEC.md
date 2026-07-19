---
title: Архитектура тегов и билдостроения — второй проход
aliases:
  - Buildcraft Architecture Spec
  - Архитектурный пакет билдостроения
type: architecture_spec
status: proposed
canonical: false
date: 2026-07-19
scope:
  - buildcraft
  - roster
  - personal_tags
  - thermos
  - lifecycle
  - double_paradox
tags:
  - architecture
  - buildcraft
  - extraction-fps
  - roster
  - lifecycle
  - thermos
  - personal-tags
---

# Архитектура тегов и билдостроения — второй проход

> [!important] Статус документа
> Это не канон и не новый источник истины. Это утверждённый для записи пакет архитектурных решений: что сохранить, что изменить, кому принадлежит каждое правило и какими проверками закрываются эксплойты. До переноса решений в профильные GDD-файлы действующим каноном остаются существующие страницы проекта.

## 0. Назначение и граница работы

Задача этого прохода — не придумать больше контента и не доказывать удовольствие прототипом. Задача — сделать каркас, в котором:

- процедурный мир отнимает у игрока знание карты, но не знание собственного персонажа;
- ширина ростера создаёт намеренную мету контрпиков;
- сборка расширяет способы решения, а не превращает вылазку в проверку скрытого ключа;
- одна и та же цена не списывается дважды разными системами;
- жизненный цикл не позволяет печатать новых людей через управляемую смерть;
- Термос сохраняет глубину полной RPG-системы носимой экипировки;
- Двойной Парадокс остаётся балансировочной абстракцией, но не начинает диктовать runtime-истину;
- добавление новых тегов, модулей, hero-kit и аномалий использует существующие интерфейсы, а не создаёт новые исключения.

Главный дизайн-инвариант:

> **Неизвестный мир — известный себе персонаж.**

Процедурная карта уже отнимает у игрока привычную extraction-FPS-уверенность: знакомую позицию, заранее выученный маршрут, надёжный угол и память о точном расположении опасностей. Поэтому билдостроение не имеет права дополнительно отнимать причинную ясность собственного персонажа.

«Известный себе» означает: все **действующие сейчас** свойства, возможности, долги и ограничения известны. Latent-тег может оставаться неизвестным только пока он `DORMANT`, не влияет на расчёт и не оставляет статистических утечек. Это неизвестное будущее человека, а не скрытый текущий билд.

## 1. Итоговый вердикт и оценки

### 1.1. Вердикт

Основа системы уникальна и совместима с extraction FPS. Основная проблема не в её необычности, а в неполной формализации границ:

- First Return пока причинно выводится из поведения, хотя должен принадлежать личности;
- «active 3 / Reserve» описывает несуществующее ограничение и приглашает будущего автора случайно его реализовать;
- Last Thread и живое завершение пути не входят в lifecycle state machine;
- Термос имеет оправданное число слоёв, но часть полей дублирует владельцев или смешивает definition с instance-state;
- Двойной Парадокс полезен как внутренняя топология, но его словарь и дублированные данные способны превратить гипотезу в ложную игровую истину;
- эффекты разных источников пока не обязаны проходить один общий stack/debt resolver.

Это ремонтируется без превращения Eldraine в стандартную систему «класс + редкость + Power Score».

### 1.2. Архитектурная оценка

Оценки ниже означают уверенность в каркасе, а не доказанное качество конкретного прототипа.

| Критерий | Текущее состояние | После спецификации | Главная причина разницы |
|---|---:|---:|---|
| Совместимость с привычкой extraction-FPS-игрока | 6/10 | 8.5/10 | Игрок получает прогноз до выбора Пешки и сохраняет уверенность в себе при неизвестной карте |
| Уникальность без жанрового разрыва | 8/10 | 9/10 | Ростер-мета, личные теги и физический Термос остаются; исчезают скрытые причинные ловушки |
| Причинная читаемость билда | 5/10 | 8.5/10 | Один владелец параметра, единый resolver эффектов и progressive disclosure |
| Устойчивость к sacrifice/reroll | 3.5/10 | 8.5/10 | Continuity Admission отделён от Recruitment; незакрытая судьба блокирует печать Ward |
| Масштабирование контента | 6/10 | 8.5/10 | Новое содержание подключается через стабильные семейства, owners и lifecycle events |
| Защита от доминирующих стеков | 5/10 | 8/10 | Stack groups, protected debt, floors и запрет self-funding |
| Доказанность UX | 3/10 | 3/10 | Архитектура не заменяет наблюдение за игроком; эмпирические параметры остаются эмпирическими |

### 1.3. Исправления относительно прошлого аудита

| Тема | Предыдущее чтение | Исправленное решение |
|---|---|---|
| Reserve | «Библиотека контрпиков» была названа риском сама по себе | Претензия снята. Библиотека известных специалистов — намеренная account-meta. Риск начинается только там, где специалист становится обязательным ключом или новые люди превращаются в reroll-каталог |
| Термос | Количество разрешений было прочитано как лишняя перегрузка | Глубина оправдана: Термос заменяет броню, перчатки, обувь, обвязку, аксессуары, сенсорику и энергетическую инфраструктуру. Нужно не сокращение, а единое устройство владельцев и поэтапный UI |
| Двойной Парадокс | Возник риск демонтировать или ослабить систему | Система сохраняется как канонический внутренний дизайн-инструмент. Ограничивается только её runtime-власть |
| First Return | Тег выводился из фактов первой вылазки | Это запрещено. Тег фиксируется при создании `PawnID`; вылазка только даёт событие раскрытия. Chronicle отдельно записывает реальные действия |
| First Survival | Был упомянут, но не стандартизирован | Переименован в **Последнюю нить** и полностью включён в lifecycle resolver |
| Retirement | Был назван, но отсутствовал как живой терминальный исход | Переименован в **Закрытие Хроники** с необратимыми живыми исходами и без наследуемой силы |

## 2. Жанровый контракт уверенности

### 2.1. Что игрок обязан знать до `BreachCommitted`

Игроку доступны:

- полный список всех `ReadySelectable` Пешек;
- тело, hero-kit, P/Q/E, Frame и известные ограничения выбранной Пешки;
- все уже проявленные Personal Tags и их локальные последствия;
- фактические экземпляры оружия, Термоса, модулей, батарей и расходников;
- итоговая масса, покрытие, сервисная нагрузка и Диссонанс сборки;
- класс задачи, сектор, Tier, среда, объявленная аномальная фаза, доступ и временной контракт;
- известные цены выбранного подхода и оставшиеся незакрытые риски;
- `ForecastRevisionID`, подтверждающий актуальность прогноза.

### 2.2. Что остаётся неизвестным

Игрок не получает:

- точный seed;
- геометрию улиц и комнат;
- точное расположение выхода, лута, противников и Threshold;
- гарантированный безопасный угол;
- адаптивную подсказку «эта Пешка победит»;
- скрытый Personal Tag кандидата;
- будущий набор тегов человека;
- фактический PvP-matchup, выведенный из Двойного Парадокса.

### 2.3. Компенсация за неизвестную карту

Генератор обязан гарантировать семантику, а не координаты:

```text
валидная точка входа
→ минимум один базовый маршрут к обязательной задаче
→ возможность распознать обязательную affordance
→ минимум один базовый способ пройти без редкого Personal Tag
→ возможность отказаться или выйти до необратимого дедлайна
→ достижимость Normal Threshold до Final Stabilization
```

Специалист может изменить цену, скорость, надёжность или маршрут. Он не может быть единственным правом участвовать.

Генератор не читает выбранный билд для создания персональной контры или персонально удобного seed. Иначе подготовка становится театром, а не обязательством.

## 3. Единая последовательность решения вылазки

```text
1. SortieForecast опубликован
2. Игрок просматривает весь Ready-ростер
3. Фильтрует по известным возможностям, hero-kit и проявленным tags
4. Выбирает SelectedPawnID
5. Выбирает или собирает Doctrine
6. Резервирует реальные ItemID
7. Resolver показывает эффекты, долги, массу, Диссонанс и незакрытые риски
8. Игрок подтверждает текущий ForecastRevisionID
9. BreachCommitted атомарно запечатывает:
   AccountID × PawnID × SessionID × ContractID × ForecastRevisionID × LoadoutSnapshot
10. После commit другая Пешка и другой loadout не могут заменить ставку в этом SessionID
```

До шага 9 выбор свободен. После шага 9 ростер перестаёт существовать для этой вылазки.

Если forecast изменился, подтверждение инвалидируется. Система не может молча отправить Пешку в изменившиеся условия.

## 4. Карта ответственности

| Данные или решение                                | Единственный владелец                                                    | Разрешённые читатели                    | Запрещённое дублирование                                  |
| ------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------- | --------------------------------------------------------- |
| `readiness`, MIA/LOST_CLOSED/KIA/CLOSED, Last Thread, closure; PawnPresenceLease | [[04_Player_Entities/Lifecycle_Roster\|Lifecycle_Roster]]                | Spawn, Access, UI, Chronicle            | Теги, квест или UI не меняют lifecycle напрямую           |
| `ReadySelectable`                                 | derived из Lifecycle                                                     | Sortie Draft                            | Prepared Cases не участвуют                               |
| Membership ростера                                | Lifecycle                                                                | Hub, Spawn                              | active-slot не является membership                        |
| Prepared Cases                                    | Hub/UI preparation                                                       | Sortie Draft                            | Не читаются Access, ReadyCount, reward или recruitment    |
| Latent/active/inactive Personal Tag               | [[04_Player_Entities/Tags_System\|Tags_System]]                          | Combat Profile, UI после reveal         | Chronicle не выбирает TagID                               |
| Факты прожитого                                   | [[04_Player_Entities/Trait_Development\|Trait_Development]] / Chronicle  | Tags reveal, closure grammar, narrative | Факты не переписывают заранее назначенный First Return    |
| Forecast и revision                               | Raid/Contract generation                                                 | Roster UI, Access, player               | Выбранный build не меняет seed                            |
| ParticipationClaim                                | [[08_World_Generation/Generation/19_Access_Contracts\|Access Contracts]] | Lifecycle, extraction, reconnect        | Reserve не заменяет DeployedPawn                          |
| Физический ItemID и manifest                      | Inventory / extraction                                                   | preparation, raid, recovery             | Preset не создаёт второй экземпляр                        |
| Fit и topology Термоса                            | Thermos assembly                                                         | Master UI, resolver                     | Hero-kit не задаёт физическую позицию                     |
| Service capacity                                  | authored hero-kit + derived assembly                                     | Thermos resolver                        | Race/Spec-арифметика не заменяет authored hero-kit        |
| Policy изменяемого параметра                      | единый ParameterContract, утверждённый domain owner                      | Combat Profile resolver                 | Тег и модуль не имеют частных priority/stack/floor-правил |
| Порядок resolution                                | [[04_Player_Entities/Combat_Profile_Pipeline\|Combat Profile Pipeline]]  | runtime consumers                       | Pipeline не копирует domain policies                      |
| Итоговая Диссонанс-реакция                        | [[05_Combat_Survival/Dissonance_System\|Dissonance System]]              | Gate, world response, UI                | Модуль не меняет Gate напрямую                            |
| Топологическая гипотеза                           | Double Paradox registry/tool                                             | design review                           | Не входит в runtime Combat Profile                        |
| Фактический matchup/window                        | authored hero-kit/action                                                 | combat, UI, QA                          | Не выводится автоматически из vector graph                |

## 5. First Return: личность фиксируется до поведения

### 5.1. Неподвижный контракт

```text
PawnIDCreated
→ сервер атомарно назначает latent_first_tag_id
→ status = LATENT_DORMANT
→ TagID сохраняется до любого raid input
→ первая самостоятельная обычная вылазка завершается валидным возвращением
→ Chronicle записывает реальные факты
→ отдельное lifecycle-событие раскрывает уже существующий TagID
→ status = ACTIVE
```

First Return отвечает на вопрос «что впервые проявилось в этом человеке». Chronicle отвечает на вопрос «что он сделал». Это связанные во времени, но причинно разные записи.

### 5.2. Минимальная модель данных

```yaml
first_return:
  pawn_id: PawnID
  tag_id: PersonalTagID
  assignment_revision: TagPoolRevisionID
  assigned_at: PawnIDCreated
  lifecycle_state: LATENT_DORMANT | REVEAL_PENDING | ACTIVE | INACTIVE
  reveal_event_id: null | LifecycleEventID
  reserved_lifetime_slot_index: 1
```

Обязательные инварианты:

- `tag_id` существует до первой вылазки;
- assignment атомарно резервирует один lifetime-slot, но не увеличивает revealed-count и не завершает formation;
- поле серверное и не меняется от поведения, отмены, disconnect, маршрута или использованных действий;
- до reveal эффект не работает и UI не выдаёт косвенную статистику, по которой его можно вычислить;
- Chronicle facts не являются входом `SelectTag()`;
- reveal и activation совершаются одной транзакцией после валидного возвращения;
- повтор события идемпотентен по `LifecycleEventID`.

### 5.3. Событие раскрытия

`FIRST_ORDINARY_RETURN_COMPLETED` требует одновременно:

- Пешка была `DeployedPawn` в обычной вылазке;
- существовал `BreachCommitted`;
- достигнут обычный `NormalThreshold`;
- Пешка лично пересекла валидный выход живой;
- это не scripted onboarding, Recovery, Breakline-only, carry-only или civic escort;
- исход не был административно восстановлен после серверной ошибки.

Не раскрывают First Return:

- Breakline;
- Последняя нить / Recovery;
- перенос бессознательной Пешки;
- MIA;
- KIA;
- handoff;
- отказ от кандидата;
- наблюдение за чужой вылазкой.

### 5.4. Reveal-run как допустимый риск, а не заранее выдуманный штраф

Игрок может начать водить новых Пешек в самый безопасный обычный контракт ради раскрытия. Это не закрывается усталостью, обязательной сложной миссией или искусственным таймером заранее.

Архитектурные ограничения уже достаточны:

- вылазка обычная и самостоятельная;
- существует ставка жизни и предметов;
- Recovery не раскрывает tag;
- смерть не продвигает recruitment pool;
- First Reception не выдаёт новый механический roll за sacrifice.

Только если наблюдение покажет массовые бессодержательные двухминутные reveal-runs, корректируется минимальная содержательность обычного контракта. Причинность тега не меняется.

## 6. Ростер как намеренная библиотека контрпиков

### 6.1. Термины

| Убрать или переопределить | Целевой термин | Точная семантика |
|---|---|---|
| `Shell Deck` / Колода | `Roster` / Ростер Пешек | Все принятые живые Пешки |
| `3 active slots` | `Prepared Cases` / Линия подготовки | До трёх закреплённых карточек или черновиков сборки для быстрого сравнения |
| `Reserve` как состояние | Удалить | Не выбранная сейчас `READY`-Пешка остаётся обычной `ReadySelectable` |
| `Active Pawn` до входа | `SelectedPawn` | Пешка текущего Sortie Draft |
| `Active Pawn` после входа | `DeployedPawn` | Пешка, запечатанная в ParticipationClaim |
| `Retired` | `CLOSED_*` | Живая, но необратимо недоступная для Deploy Пешка |

`Prepared Cases`:

- не меняют `ReadyCount`;
- не входят в `CanDeploy`;
- не дают пассивный бонус;
- не ограничивают выбор;
- могут хранить `PawnID + DoctrineDraft`;
- разные drafts могут ссылаться на один ItemID, потому что это планы;
- только `CommittedLoadoutSnapshot` создаёт `LoadoutReservation` и запрещает одному физическому ItemID одновременно находиться в двух обязательствах;
- могут расширяться Хабом только как QoL;
- могут быть полностью удалены, если UX не оправдает отдельную сущность.

Нельзя превращать их в усталость, upkeep, задержку переключения или платный доступ к собственной Пешке.

### 6.2. Здоровая account-meta

Разрешено и желательно:

- хранить узкого специалиста ради определённой аномальной фазы;
- выбирать Пешку по известному hero-kit;
- выбирать Пешку по уже проявленному Personal Tag;
- иметь более быстрый, дешёвый или надёжный specialist-route;
- собирать несколько доктрин под разные прогнозы;
- не использовать часть ростера месяцами без искусственного decay.

Запрещено:

- делать Personal Tag единственным ключом обязательного контракта или базовой эвакуации;
- позволять specialist-build удалить всю сцену, tell, риск и counter-action;
- давать невыбранным Пешкам пассивные ресурсы, страховку, Gate, скидки или account-stat;
- показывать `Best Pawn` или Power Score;
- использовать latent tags в фильтре;
- подстраивать seed под выбранного специалиста;
- заменять погибшего человеком со скамейки после commit.

Инвариант горизонтальной ширины:

> Ветеран владеет большим числом хороших ответов. Он не получает универсально более сильного ответа и не обходит ставку после выбора.

### 6.3. Continuity Admission против recruitment-gacha

Текущая цепочка `ReadyCount=0 → новый Ward` эксплуатируема, если следующий Ward получает новый механически значимый roll:

```text
единственный Ward
→ дешёвая смерть или раскрытие неудобного тега
→ ReadyCount = 0
→ новый roll
→ повторить
```

Нельзя одновременно сохранить:

1. мгновенного нового человека при нулевом ростере;
2. новый механический профиль при каждой смерти;
3. управляемую игроком KIA;
4. отсутствие стойкого последствия;
5. отсутствие sacrifice-reroll.

Целевое разделение:

| Канал | Назначение | Расширяет библиотеку | Что создаёт следующий шанс |
|---|---|---:|---|
| `Continuity Admission` | Не дать аккаунту потерять право играть | Нет | Ноль Ready и отсутствие незакрытой судьбы/ожидаемого admission |
| `Recruitment Opportunity` | Получить нового уникального специалиста | Да | Rescue, отношение, контракт, мировой authored-source |
| KIA / отказ / handoff / closure | Судьба существующего человека | Нет | Никогда |

Рекомендуемый жёсткий предохранитель — стабильный continuity-профиль:

```yaml
continuity_profile_id
continuity_hero_kit_id
continuity_race_id
continuity_spec_id
continuity_tag_seed
continuity_epoch_id
continuity_epoch_advance_source_id
```

- создаётся один раз для аварийной линии Первого Приёма;
- определяет baseline `RaceID × SpecID`, hero-kit и latent First Return аварийных Wards внутри текущей epoch;
- `continuity_epoch_id` и `continuity_tag_seed` не меняются от KIA, suicide, handoff, closure, reconnect или Breakline;
- новый Ward может иметь другое имя, внешность, биографию и Chronicle, но сохраняет тот же `RaceID × SpecID` и не даёт новую механическую попытку внутри epoch;
- уникальные новые специалисты приходят только через Recruitment Opportunity;
- каждый фиксированный профиль обязан поддерживать минимум две жизнеспособные baseline-доктрины через обычные gear, Frames и Welfare; это не может обеспечиваться скрытым тегом;
- сменить continuity epoch может только одноразовый внешний milestone с сохранённым `advance_source_id`, который невозможно ускорить уничтожением ростера.

Цена решения сознательная: после раскрытия аварийный профиль внутри epoch предсказуем. Это лучше скрытого recruitment-gacha, потому что First Reception обеспечивает непрерывность игры, а не бесконечную новизну через смерть.

Единственный admission-predicate определён в §10.7 и принадлежит Lifecycle. Он учитывает Ready, все recoverable-судьбы, живых Пешек в Care и pending admissions. Если authored MIA требует второго действующего лица при нулевом ростере, его recovery-entry обязан предоставить operation-local/civic доступ, а не создать постоянного recruitable Ward.

### 6.4. Foundling: commitment до private roll

Целевой порядок:

```text
Encounter
→ Rescue Commitment
→ Normal Threshold
→ safe recovery
→ раскрыть личность, видимое тело, hero-kit и Continuation
→ необратимо выбрать roster / civic / obligation outcome
→ если выбран roster:
     уже зафиксированный Origin остаётся LATENT_DORMANT
     первая самостоятельная обычная вылазка
     reveal + activation Origin
```

Выбирать кандидата по известному hero-kit разрешено: это стабильная роль. Сканировать точный Origin, оставлять удачный roll и гуманно передавать неудобный — запрещённый recruitment-sort.

`OriginTagID` фиксируется сервером при создании `CandidateOccurrenceID`, до действий игрока, и не меняется от rescue outcome. До roster commitment он не раскрывается и не действует. Это закрывает и предварительную сортировку, и reroll через отказ.

`CandidateOccurrenceID` закрывается при любом исходе и никогда не ускоряет следующий occurrence.

## 7. Термос как полная система носимой экипировки

### 7.1. Что сохраняется

Термос остаётся единым носителем:

- брони и физического покрытия;
- перчаток, обуви и обвязки;
- сенсорных и оптических ветвей;
- герметизации и защиты от среды;
- энергетической разводки и батарейной инфраструктуры;
- аксессуарных/utility-функций;
- локальных уязвимостей, массы, Heat и Диссонанса;
- материальной истории вещи: подгонки, передачи, повреждения и потери.

Монтаж выполняется у мастера в Хабе и блокируется после Deploy. Сложность допустима, потому что игрок принимает её в выделенном экране подготовки, а не в бою.

### 7.2. Семь вопросов, непересекающиеся authority contracts

| Вопрос | Владелец | Результат |
|---|---|---|
| Можно ли надеть основу на это тело? | Body + Thermos model + instance refit | `fit_state` |
| Куда физически встаёт модуль? | Thermos topology + module mount pattern | занятые nodes и spatial conflicts |
| Способна ли Пешка обслуживать функции? | authored hero-kit + validated support | service capacity legality |
| Что модуль меняет? | domain owner конкретного параметра | resolved effect |
| Сколько это физически весит? | Item instances → Physical Weight | load state и движение |
| Какой аномальный след создаётся? | source emission → Dissonance System | persistent signature / event pulse |
| Сколько это стоит и насколько редко? | Economy/acquisition | получение и замена, не монтажная законность |

`effect_axis` отвечает только за поиск и отчётность. Он не является восьмым разрешением.

Один system может владеть несколькими контрактами, если это естественно. Требование не в искусственном числе систем, а в том, чтобы один результат не имел двух источников истины.

### 7.3. Целевая структура данных

```yaml
ThermosModel:
  model_id: ThermosModelID
  fit_envelope: MorphologyEnvelope
  mount_nodes:
    - node_id
      body_region
      capacity_units
      accepted_mount_classes
  base_service_support_delta: {plate, optic, seal, conduit, rig, weave}
  policy: hub_stitch_only

ModuleDefinition:
  module_def_id: ModuleDefID
  allowed_mount_patterns:
    - pattern_id
      required_claims: [NodeClaim]
  service_load: {plate, optic, seal, conduit, rig, weave}
  effects: [EffectContract]
  physical_mass
  persistent_dissonance_signature
  dissonance_contributor_rules
  body_interface_kind: null | InterfaceKind
  selectable_interface_effect_id: null | EffectID
  ui_search_aliases: []

InstalledModule:
  module_instance_id: ItemID
  module_def_id: ModuleDefID
  thermos_instance_id: ItemID
  selected_pattern_id
  occupied_nodes
  damage_state
  stitched_state

ThermosAssemblyInstance:
  thermos_instance_id: ItemID
  fitted_for_morphology
  fit_revision
  installed_module_ids
  active_body_interface_module_id
```

Definition не хранит фактическое состояние конкретной сборки. `fit_state`, свободный объём, `Used`, `Final`, `Remaining`, итоговое покрытие, масса и Диссонанс являются derived.

Миграция неоднозначных полей:

| Текущее поле | Целевой смысл |
|---|---|
| `slot_count` | Derived сумма `mount_nodes.capacity_units` |
| `slot_size` | `mount_load` выбранного pattern либо сумма его node claims |
| `module_positions` | Разделить на definition `allowed_mount_patterns` и instance `occupied_nodes` |
| `fit_profiles` | `fit_envelope` модели |
| `interface_state` в registry | Удалить из definition; состояние принадлежит assembly instance |
| `field_state:: stitched_locked` в registry | В definition оставить policy; фактический state хранить в instance |
| `module_axes` | Derived `effect_axes` для поиска |

`allowed_mount_patterns` обязаны различать `OR` и `AND`. Например, наруч можно поставить **либо** на левое, **либо** на правое предплечье двумя patterns. Плечевое ярмо, одновременно занимающее два плеча и спину, имеет один pattern с тремя обязательными claims.

### 7.4. Семейства означают обслуживание, а не эффект

Сохраняются шесть семейств:

- `plate`;
- `optic`;
- `seal`;
- `conduit`;
- `rig`;
- `weave`.

Целевая терминология:

| Текущее имя | Целевое имя |
|---|---|
| `HeroKitCapacity` | `BaseServiceCapacity` |
| `ExplicitGearCapacity` | `ServiceSupportDelta` |
| `FinalCapacity` | `FinalServiceCapacity` — только derived |
| `module_cost` | `service_load` / «нагрузка обслуживания» |
| `module_families` | Не хранить отдельно: `service_families = keys(service_load where value > 0)` |

`BaseServiceCapacity` остаётся authored-полем полного hero-kit. Её нельзя арифметически выводить из Race и Spec: это уничтожит authored-пересечение.

Гибридный модуль:

- занимает физическое место один раз по выбранному mount pattern;
- платит `service_load` всем реально работающим семействам;
- не получает второй независимый эффект бесплатно;
- при трёх и более независимых семействах по умолчанию разбивается на assembly/preset;
- остаётся атомарным только если имеет единый механизм, trigger, failure-state и уязвимость.

### 7.5. Support capacity без циклов

```text
Base(family) = BaseServiceCapacity(hero-kit, family)

SupportLoad(family) =
  sum(service_load всех support-module sources по family)

SupportSourcesEligible iff
  SupportLoad(family) <= Base(family)
  для каждого family

FinalServiceCapacity =
  Base
  + ThermosModel.base_service_support_delta
  + sum(ServiceSupportDelta всех eligible support-modules)

UsedServiceCapacity =
  sum(service_load ВСЕХ модулей, включая support-modules)

AssemblyValid iff
  SupportSourcesEligible
  AND UsedServiceCapacity <= FinalServiceCapacity
```

Ни индивидуальная, ни совокупная нагрузка support-модулей не использует ни один `ServiceSupportDelta`. Сначала вся support-группа должна поместиться в authored-базу; только затем её delta участвует в финальной проверке сборки.

Разрешённые support-sources:

- конструктивная черта модели Термоса;
- отдельный физический support-модуль с node, массой и собственной базовой допустимостью.

Запрещённые:

- Personal Tag;
- Chronicle;
- временный рейдовый статус;
- расходник;
- self-funding модуль;
- цепочка взаимно включающих harness-модулей.

### 7.6. Effect contract и stack safety

Каждый эффект Термоса использует общий контракт:

```yaml
effect_id
target_owner
target_parameter
activation_mode
condition
operation
stack_group
intrinsic_debt
debt_lock
tell
failure_state
```

Источник не задаёт priority, global floor/cap или допустимый перенос. Доменный `ParameterContract` задаёт `stack_policy` и порядок:

- `exclusive`;
- `best_only`;
- `additive_to_cap`;
- `sequential` — только для осознанного многостадийного цикла.

Модуль, тег, батарея и P/Q/E не могут по отдельности переписать одну и ту же короткую стадию. Resolver показывает конфликт до монтажа.

Protected debt нельзя стереть соседним модулем или тегом. Смягчение разрешено только если:

- владелец параметра допускает mitigation;
- сохраняется минимальный floor долга;
- новый источник платит собственной ценой в той же сцене.

Опорный контур остаётся один:

- definition хранит `body_interface_kind`;
- только definition с ненулевым `body_interface_kind` и собственным `selectable_interface_effect_id` может быть выбран;
- assembly instance хранит `active_body_interface_module_id`;
- resolver проверяет, что выбранный EffectID принадлежит этому установленному модулю и совместим с телом;
- только `interface_output` выбранного контура активен;
- обычные не-interface функции остальных модулей продолжают работать;
- переключение выполняется только у мастера до Deploy;
- interface-output проходит тот же domain-owner/stack resolver и не имеет частной системы исключений.

### 7.7. Монтажный resolver

```text
1. Definition completeness
2. Fit: compatible / refit_required / incompatible
3. Mount pattern: существующие nodes, свободные units, отсутствие spatial conflict
4. BaseServiceCapacity
5. Aggregate SupportLoad <= Base для шести семейств
6. FinalServiceCapacity и Used всех модулей <= Final
7. Effect-owner и stack/debt validation
8. Assembly lock: stitched_locked
9. Derived sortie profile:
   mass + coverage + Dissonance + environment capabilities + readiness
```

Resolver возвращает все причины отказа одновременно. Игрок не должен исправлять по одной скрытой ошибке за цикл.

### 7.8. Progressive disclosure

**Экран выбора Пешки/вылазки:**

- силуэт покрытия;
- состояние физической нагрузки;
- состояние Диссонанса;
- активный Опорный контур;
- приоритизированное краткое резюме итоговых изменений; точное число определяется UX-тестом;
- критические readiness-предупреждения.

**Экран мастера:**

- nodes и свободные units;
- совместимые placement patterns;
- только затронутые service families;
- точное `до → после` по массе, покрытию, Диссонансу и эффекту;
- долг, stack conflict и все причины несовместимости.

**Раскрытая экспертиза:**

- все шесть capacities и их sources;
- полный owner path;
- stack groups;
- floors/caps;
- альтернативные patterns;
- derived effect axes.

**В рейде:** только фактическое покрытие, повреждённые ветви, active interface, локальные уязвимости, масса и Диссонанс. Монтажные таблицы read-only и по умолчанию скрыты.

### 7.9. Обязательные crash-tests Термоса

| Эксплойт | Предохранитель |
|---|---|
| Hybrid получает slot compression и два полноценных эффекта по цене одного | Каждая независимая функция платит service load и хотя бы одну релевантную same-raid цену: node conflict, mass, exposure, energy, heat, protected debt либо потерю альтернативной функции. Отдельный абстрактный debt не обязателен |
| Support-модуль включает сам себя | Support pass проверяется только против BaseServiceCapacity |
| Два support-модуля включают друг друга | Между support-sources нет рекурсивного финансирования |
| Вес списывается как mass, vulnerability и Recovery одновременно | Physical Weight — единственный источник массы; геометрическое ограничение обязано иметь отдельную причину |
| `effect_axis` становится скрытым allowlist | Ось derived и никогда не участвует в legality/effect resolution |
| Preset клонирует редкий модуль | Preset хранит план; финальный commit резервирует уникальный ItemID |
| Один модуль стирает Recovery/Heat/tell другого | Protected debt + floor + domain-owned stack policy |
| Capacity-support становится обязательным tax | Ни один baseline build не требует support delta; usage отслеживается как balance smell |
| Термос переписывает личность Пешки | Модули не меняют kernel P/Q/E и latent tags |
| Диссонанс становится универсальной второй ценой всего | Каждый emission обязан создавать конкретную сцену/реакцию; декоративная цена удаляется |

### 7.10. Реальные остаточные риски Термоса

- Шесть service capacities будут восприниматься как произвольный class-lock, если fantasy hero-kit не объясняет их распределение.
- Mount topology требует визуального и сетевого QA на разных морфологиях; схема данных не оплачивает production-cost автоматически.
- Hybrid-модули могут доминировать за счёт slot compression даже при честной service-цене; это отдельный числовой corridor.
- Support-модули легко превращаются в обязательный tax; их pick-rate и долю baseline-сборок нужно отслеживать.
- Одна система всего wearable-gear увеличивает цену восстановления после потери; нужны presets-планы и ясная повторная сборка без клонирования предметов.
- Потерянная сборка сохраняется только как `ghost plan`, а не как предмет: exact rebuild резервирует реальные `ItemID`; nearest substitute допускается лишь как preview с полным `до → после`, явным подтверждением и отдельным BOM/work order.
- Масса, геометрическое ограничение движения и Recovery могут трижды описать одну физическую проблему; QA обязан требовать отдельную причинность каждого долга.
- Progressive disclosure остаётся UX-гипотезой: архитектура определяет слои, но не доказывает удобство экрана мастера.

## 8. Двойной Парадокс как балансировочная абстракция

### 8.1. Статус и власть

```yaml
system_class: internal_design_model
design_authority: topology_and_hypotheses
runtime_authority: none
player_visibility: none
build_legality_dependency: none
matchmaking_dependency: none
automatic_content_generation_authority: none
offline_content_planning_output: allowed
```

Двойной Парадокс остаётся активной частью дизайна. Он детерминированно создаёт гипотезы о давлении, концентрации риска, покрытии и пробелах каталога. Фактическая игровая истина принадлежит authored-действиям, локальным владельцам параметров и проверяемой сцене.

### 8.2. Один источник графа

| Данные | Владелец |
|---|---|
| Vector IDs, labels, semantics, `dominates`, graph version | единый Double Paradox Registry |
| `base_vector` Race | Race definition |
| `base_vector` Spec | Spec definition |
| `WeakTo` | derived inverse графа |
| `ComboVectors`, concentration, pressure, coverage | derived tool output |
| P/Q/E, windows, exposure, actual bad matchup | authored HeroKit |
| Подтверждение/опровержение | review overlay с `graph_version` |

`[[04_Player_Entities/_Matrices/00_Synergy_Map|Synergy Map]]` читает registry, а не хранит собственный `paradoxRules`. `weak_to` на страницах родителей либо удаляется, либо показывается как derived view.

Review overlay принадлежит отдельному целевому файлу `04_Player_Entities/_Matrices/Registry_Double_Paradox_Reviews.md`. Он не записывается в `Registry_Combos` и не экспортируется в runtime.

### 8.3. Два независимых pipeline

```text
Race.base_vector + Spec.base_vector
→ Double Paradox Design Profile
→ hypotheses / review queue / coverage audit
```

```text
HeroKitID
→ P/Q/E + Frame + doctrine + tags + loadout
→ runtime Combat Profile
→ фактические windows и counterplay
```

Они встречаются только в design review:

```text
hypothesis
↔ authored scene
→ confirmed | partial | refuted | intentional_inversion | out_of_scope
```

### 8.4. Допустимые outputs

- topological pressure;
- shared-risk concentration;
- coverage hypothesis;
- mono-vector concentration;
- пустоты и перенасыщение каталога;
- review priority;
- candidate-coordinate для планирования;
- сигнал пересмотреть `base_vector` или graph edge.

Запрещённые outputs:

- урон, HP, точность, Heat, Recovery или шанс;
- P/Q/E, Frame, proficiency или service capacity;
- разрешение loadout, Gate, Access, loot, spawn или matchmaking;
- автоматический tag;
- автоматическое объявление фактической контры или поддержки;
- Power Score;
- требование переписать authored-kit ради соответствия графу;
- обязательство произвести весь Cartesian product `Race × Spec`;
- player-facing tooltip или tier chart.

### 8.5. Переименование опасного словаря

| Сейчас | Целевое имя |
|---|---|
| `NetPressure` | `TopologicalPressureDelta` |
| `Counter` | `PressureHypothesis` |
| `support` | `CoverageHypothesis` |
| `Strong support` | `HighPriorityCoverageHypothesis` |
| `SharedWeakness` | `SharedRiskConcentration` |
| `mono_vector_fusion` | `MonoVectorConcentration` |
| `strength` в инструменте | `signal` или `review_priority` |

### 8.6. Нормализация

Сырой `RawPressure` несопоставим между mono-coordinate и dual-coordinate. Используется:

```text
ComparablePairCount(A,B) =
  count((a,b), где graph содержит a→b или b→a)

ForwardRate(A,B) =
  RawPressure(A,B) / ComparablePairCount(A,B)

ReverseRate(A,B) =
  RawPressure(B,A) / ComparablePairCount(A,B)

TopologicalPressureDelta(A,B) = ForwardRate(A,B) - ReverseRate(A,B)
```

При `ComparablePairCount = 0` pressure отсутствует. Общие векторы не входят в denominator направленного давления и публикуются отдельно.

`ComparablePairCount = 0` и, следовательно, zero useful signal — допустимый результат, а не ошибка, которую следует заполнять искусственной парой.

Отдельно показываются `evaluated_relation_pairs`, `shared_vector_pairs` и `mono_concentration`. Результат не является вероятностью победы или balance coefficient.

Текущий граф создаёт направленную асимметрию для 30 из 36 пар MVP-координат. Это не доказывает ошибку модели, но показывает слабую приоритизацию: если отмечено около 83% пар, глобальный view не помогает выбирать следующую проверку.

### 8.7. Масштабируемый review

Для нового утверждаемого hero-kit обязательны:

1. семантическая проверка родительских `base_vector`;
2. review не более `review_budget_per_kit.incoming` верхних входящих signals;
3. review не более `review_budget_per_kit.outgoing` верхних исходящих signals;
4. review каждого фактического `bad_matchup`/`mitigates`, заявленного самим kit;
5. review `MonoVectorConcentration`, если применимо.

Ранжирование детерминировано: priority → число comparable relations → stable kit ID. Ничьи сверх бюджета остаются вычисленными, но не обязательными к записи.

Полный O(K²) расчёт остаётся автоматическим. O(K²) ручное объяснение не требуется. Для текущего MVP 3×3 допустим один полный pairwise-pass как разовая проверка.

Review-запись хранит `graph_version`. Изменение графа делает старое подтверждение `stale`, но не удаляет его.

Каждый review top-N обязан содержать named scene и evidence. Если почти все пары получают high-priority, priority output признаётся непригодным и приостанавливается до пересмотра vectors/edges; он не получает runtime-статус и не заставляет автора производить ложный обзор.

Минимальная review-запись:

```yaml
review_id
source_hero_kit_id
target_hero_kit_id
graph_version
hypothesis_type
predicted_reason
status: CONFIRMED | PARTIAL | REFUTED | OUT_OF_SCOPE | INTENTIONAL_INVERSION
scene_context
named_window
evidence_ref
decision_note
```

### 8.8. Реальные остаточные риски Двойного Парадокса

- Семь широких векторов могут сжать различия между authored-kit сильнее, чем полезно.
- Регулярный граф визуально похож на RPS-закон и будет подталкивать автора буквально реализовывать каждое ребро.
- Словарь `counter/weakness/strength` способен вернуть runtime-утечку даже после правильной схемы данных.
- Если почти все связи high-priority, инструмент становится красивой картой без функции выбора.
- Классификация каждого предмета, тега и действия по векторам создаст новый TOUCH; vectors принадлежат родительской дизайн-топологии, а не каждому runtime-объекту.
- Если authored window/evidence слой пуст, математическая карта будет казаться доказательнее, чем является.

## 9. Общий resolver параметра, эффекта и долга

Все источники — P/Q/E, Personal Tag, Термос, батарея, weapon attachment и environment modifier — используют один target/stack resolver. Но они не обязаны притворяться активным действием.

`[[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile Pipeline]]` владеет грамматикой resolution и порядком проходов. Политика каждого параметра хранится один раз в целевом registry `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`:

```yaml
ParameterContract:
  parameter_id
  domain_owner
  lifecycle_envelope
  allowed_operations
  stack_policy
  protected_floor
  protected_cap
  allowed_mitigation_owners
  allowed_transfer_targets
  counterplay_deadline
```

Локальные P/Q/E, tags, modules и batteries публикуют только modifier-request и intrinsic debt. Они не копируют domain policy.

Миграция resolver выполняется только как shadow-resolver: old и new параллельно сравниваются, затем переключение идёт по одному `domain_owner`; old resolver удаляется лишь после parity. Dynamic protected-floor tooltip всегда показывает `requested`, `applied`, `floor`, `final`, `reason` и `revision`.

Допустимые lifecycle envelopes:

```text
ACTION:
  Preparation → Commitment → Effect → Recovery → Aftermath

PERSISTENT_STATE:
  Enter → Active → Degraded/Disabled → Exit

REACTIVE_EVENT:
  Trigger → Tell → Resolve → Aftermath
```

`ParameterContract.lifecycle_envelope` определяет допустимую форму. Пластина, герметизация и масса используют `PERSISTENT_STATE`, а не фиктивные Commitment/Recovery.

Modifier-request может:

- заменить одну конкретную стадию;
- сократить или удлинить параметр в пределах owner-policy;
- добавить локальный результат;
- перенести долг в явно названную стадию;
- смягчить долг только до protected floor.

Источник не может:

- объявить собственное правило стека;
- стереть чужой protected debt;
- одновременно сократить Commitment и Recovery без двух отдельных цен;
- менять семантику parameter owner;
- создавать скрытый глобальный бонус «ко всему»;
- превращать Preparation в in-combat RTS-микроменеджмент.

### 9.1. Типы долга

| Тип | Правило |
|---|---|
| `FIXED` | Не смягчается другими слоями |
| `MITIGABLE_WITH_FLOOR` | Смягчается только разрешёнными owners и не ниже floor |
| `TRANSFERABLE` | Может быть перенесён только в разрешённую `ParameterContract` стадию без уменьшения severity и не позже `counterplay_deadline` |
| `CONDITIONAL` | Исчезает только при выполнении authored-condition, а не от общего stat |

Перенос фиксируется до получения пользы. Он не может вынести цену за encounter boundary, extraction или момент, после которого противник уже потерял возможность ответить. Межсценовый долг требует отдельного authored lifecycle-envelope и не разрешается одним флагом `TRANSFERABLE`.

### 9.2. Диссонанс

Разделяются два вида источника:

```yaml
persistent_dissonance_signature:
  source_item_id
  actor_id
  magnitude
  condition

dissonance_emission_event:
  emission_occurrence_id
  action_instance_id
  source_actor_id
  energy_source_id: null | ItemID
  base_emission
  contributors: []
  modifier_requests: []
  final_emission: derived
  tell
```

- Action Resolver владеет базовым импульсом действия;
- одно физическое emission occurrence создаёт ровно один `DissonanceEmissionEvent` с уникальным `emission_occurrence_id`;
- батарея указывается как `energy_source_id`/contributor, а не создаёт второй event;
- модуль может публиковать постоянную сигнатуру или contributor/modifier;
- модуль создаёт отдельный event только для отдельного module-originated `ActionInstance` с другим временем и `emission_occurrence_id`;
- Tags не меняют Gate напрямую;
- Dissonance System агрегирует источники, применяет floors/caps и создаёт реакцию мира;
- `final_emission` является derived и записывается только после Dissonance resolution;
- итог Gate/Readiness читает результат Dissonance System, а не сумму частных штрафов.

### 9.3. Батарейный перенос

Текущий ход `active cell → drained → impulse reserve` может остаться, если это физический перенос, а не бесплатное виртуальное хранилище.

Обязательный `ImpulsePacket`:

```yaml
packet_id
source_battery_id
source_cell_revision
circuit_id
created_by_action_instance_id
initial_impulse_count
remaining_impulse_count
energy_class
consumption_window
state: ARMED | DEPLETED | EXPIRED
```

Инварианты:

- один `source_cell_revision` не создаёт два параллельных packets;
- каждый `ImpulseSpendEvent` атомарно уменьшает `remaining_impulse_count`;
- `DEPLETED` наступает только при нуле;
- `EXPIRED` безвозвратно рассеивает остаток, а не возвращает его в ячейку;
- пакеты разных батарей не смешиваются в общий банк;
- перенос между circuits атомарно закрывает старую reservation до создания новой и требует нового Commitment;
- raid UI не превращается в меню ручной маршрутизации во время боя;
- Anchor/Pareto-ветвь платит ценой в той же вылазке — Load, arming, tell, heat или exposure, а не только редкостью и ценой до рейда.

## 10. Последняя нить (`LastThreadRecovery`)

`First Survival` переименовывается в **Последнюю нить**. Это не воскресение, не rollback и не player-owned KIA: первый eligible `FIELD_RECOVERABLE` lethal при доступной Нити атомарно выводит ту же Пешку из проигранной исходной вылазки в отдельную recovery-судьбу.

### 10.1. Player-facing словарь

| Сущность | Название |
|---|---|
| Состояние карты | Затерян |
| Действие | Удержать нить |
| Личная Нить | Готова / Удерживаем нить / Потрачена |
| Terminal unknown fate | Пропал навсегда |
| Успех | Вернулся живым |
| KIA | Погиб |

Основной UI не засоряется техническими состояниями: «Готов / Затерян / Удерживаем нить / На лечении / Погиб». `LOST_CLOSED/MIA_FORECLOSED` доступен только в detail/Chronicle как «Пропал навсегда», а не как ложное «Погиб».

### 10.2. Authoritative fields

```yaml
readiness: READY | IN_RAID | MIA | CARE | CLOSED | KIA | LOST_CLOSED
last_thread_state: AVAILABLE | CONSUMED_PENDING | SPENT
recovery_life_state:
  - null
  - OPERATIONAL
  - COLLAPSED_RESCUABLE

PawnPresenceLease:
  pawn_id
  state: HUB | RAID | RECOVERY_TRANSIT | CARE | TERMINAL
  session_id: null | SessionID
  entity_id: null | EntityID
  presence_epoch
  invariant: UNIQUE_ACTIVE(PawnID)

derived_last_thread_operational_status:
  READY_TO_INTERCEPT | BLOCKED_BY_ACCOUNT_CUSTODY | RECOVERY_PENDING | RECOVERY_ACTIVE | SPENT

AccountLifecycle:
  account_last_thread_slot: EMPTY | RecoveryID

RecoveryContract:
  recovery_id
  pawn_id
  source_raid_session_id
  target_session_id
  state: PENDING_CHOICE | MATCH_COMMITTED | ACTIVE | ADMINISTRATIVE_HOLD | CLOSED_RECOVERED | CLOSED_KIA | LOST_CLOSED
  attempt_count: 0 | 1
  squad_snapshot
  rescue_deadline_at: null | Timestamp
  target_final_stabilization_at
```

Один account-wide `account_last_thread_slot` обязателен для pending, committed, active и collapsed Recovery. Другие Ready-Пешки остаются доступны, но их Нить до commit явно показывает `BLOCKED_BY_ACCOUNT_CUSTODY`; она не может перехватить lethal, пока custody занята. Offline pending-timer отсутствует.

### 10.3. Летальный resolver и исходная вылазка

Оружие и lethal source публикуют только `LethalEvent` и его факты. Единственный Lifecycle/World disposition resolver классифицирует `ResolutionContext` по приоритету: `ADMINISTRATIVE_HOLD`; `FINAL_STABILIZATION/TERMINAL_OVERRIDE`; `WORLD_CONFIRMED_FATAL`; `AUTHORED_MIA`; `FIELD_RECOVERABLE`. `WORLD_CONFIRMED_FATAL` публикует только World/Session disposition по закрытому registry. Damage type, headshot, overdamage, дополнительный урон, corpse destruction, distance и attribution не могут публиковать terminal class или напрямую записывать KIA.

```text
FIELD_RECOVERABLE + AVAILABLE + custody EMPTY
→ last_thread_state = CONSUMED_PENDING
→ source ParticipationClaim = CLOSED_FAILED
→ ledger = Consumed
→ gear/Cargo = ContestableWreck в source
→ readiness = MIA
→ PawnPresenceLease: RAID(source) → RECOVERY_TRANSIT
→ account_last_thread_slot = RecoveryID
→ создать RecoveryContract PENDING_CHOICE
```

`ContestableWreck` не является person-entity. Живого тела в source не остаётся; тот же `PawnID` не может повторно войти в `source_raid_session_id`. Исходная ставка, награды, Cargo и прогресс вылазки окончательно проиграны. Attacker получает source victory, loot/cargo и credit «вынудил уйти на Нить», но никогда не ownership KIA.

Только `WORLD_CONFIRMED_FATAL` и terminal world resolver могут записать KIA по своим явным контрактам. `ADMINISTRATIVE_HOLD` останавливает reconciliation: не KIA, не reseed и не free attempt. Если `FinalStabilizationBarrier` уже commit либо находится в том же resolver order, finality выигрывает. После завершённого Presence transfer в `RECOVERY_TRANSIT` Пешки уже нет в source, и более поздняя source Stabilization её не убивает.

### 10.4. COMMON-POOL RECOVERY OVERLAY

Recovery проходит в другом уже живом обычном публичном PvPvE `target_session_id`: это **COMMON-POOL RECOVERY OVERLAY**, не same-session, не отдельный recovery-instance и не recovery-очередь. Target SessionID не создаётся Recovery; при `BreachCommitted` в нём присутствует хотя бы один unaffiliated standard `AccountID`. Recovery Pawn занимает обычный physical seat, а `RecoverySeatCap < PlayerSeatCap`. Последующее падение населения попытку не отменяет.

До commit UI показывает только envelope: доступный класс среды, риск, rescue condition и наличие escort-option. Точный seed, target SessionID, opponents и anchors скрыты. Player `RecoveryCommitted` ставит `attempt_count = 1`, запечатывает squad snapshot и переводит contract в `MATCH_COMMITTED`; live presence и ParticipationClaim ещё не созданы, exact target нельзя reroll.

После server binding точный target нельзя заменить после раскрытия. Только валидный target `BreachCommitted` атомарно создаёт ParticipationClaim, переносит PawnPresenceLease `RECOVERY_TRANSIT → RAID(target, new epoch)`, устанавливает `readiness = IN_RAID`, `recovery_life_state = OPERATIONAL`, `RecoveryContract = ACTIVE` и запускает active clock.

Recovery-owner управляет тем же `PawnID`, а не второй Пешкой. Optional escorts допустимы только precommitted до `RecoveryCommitted`: другие AccountID, каждый со своей Ready Pawn, обычным `CanDeploy`, собственной ценой/stake/seat/claim и `NeverParticipated` в target. Late join, replacement и вторая Pawn recovery-owner запрещены. Organic public players остаются независимыми участниками; victim browser и охотничья очередь отсутствуют.

### 10.5. Валидатор, kit и активный clock

Baseline Recovery solo-viable: escorts повышают надёжность, но не право начать. Валидатор требует минимум две действительно независимые rescue route/threshold candidates без общего choke и unique destructible key, с обычными публичными пересечениями, без дешёвого apex-POI shortcut и с достаточным временем до Final Stabilization.

Recovery Pawn получает operation-local nonextractable kit. Он не создаёт Protected Manifest, не возвращает original stake, не выдаёт normal loot/reward/tags/First Return; чужие `ItemID` остаются в target. Enemy может стрелять, зонить, мешать процедуре, убить carrier и брать обычный loot, но не может применить завершающее действие, переносить target, писать KIA, менять deadline или reset progress.

Active/event clock стартует только после валидного `BreachCommitted`, не в pending/matchmaking. Технический сбой после commit переводит контракт в `ADMINISTRATIVE_HOLD` и восстанавливает тот же контракт без reseed/free attempt.

### 10.6. Collapse, custody и успех

```text
OPERATIONAL
→ collapse
→ COLLAPSED_RESCUABLE
→ один раз установить rescue_deadline_at

effective_deadline =
  min(rescue_deadline_at, target_final_stabilization_at)
```

`rescue_deadline_at` никогда не паузится и не сбрасывается revive, recollapse, carry, reconnect или phase shift. При равенстве deadline/finality выигрывает deadline/finality. Только precommitted squad может stabilize/revive/carry по `BodyCustodyClaim` и `BodyRecoverySync`; organic ally не может. Carry занимает Back Slot и массу, имеет tell и ограничения; carrier после sync остаётся в рейде.

Успех: `SELF RecoveryThresholdSync` либо `SQUAD BodyRecoverySync` до effective deadline. В одной транзакции `last_thread_state: CONSUMED_PENDING → SPENT`, PawnPresenceLease переходит `RAID(target) → CARE`, Recovery становится `CLOSED_RECOVERED` и account custody освобождается; после Care discharge PawnPresenceLease переходит `CARE → HUB` одновременно с `readiness = READY`. Gear/Cargo/reward/tags не возвращаются и не выдаются.

Провал записывает только world/system resolver: rescue deadline, Final Stabilization, закрытый `WORLD_CONFIRMED_FATAL` registry или irreversible player abandonment during ACTIVE, если конкретный контракт объявляет его сознательным отказом. Terminal KIA transaction устанавливает `last_thread_state = SPENT`, PawnPresenceLease = TERMINAL, `readiness = KIA`, закрывает claim/contract и освобождает custody. Pending-выход не пишет KIA: отдельный необратимый `LOST_CLOSED/MIA_FORECLOSED` делает Pawn permanently nondeployable/nonrecoverable; его transaction также устанавливает `last_thread_state = SPENT`, PawnPresenceLease = TERMINAL, `readiness = LOST_CLOSED`, закрывает contract и освобождает custody, сохраняя честную неизвестную судьбу.

### 10.7. Situation Card и Continuity Admission

Situation Card ясно показывает: что потеряно; кто возвращается; состояние личной Нити и account custody; запущен ли мировой таймер; rescue condition; precommitted escorts; terminal causes; отсутствие rewards.

```text
ContinuityAdmissionAllowed =
  ReadyCount == 0
  AND RecoverablePawnCount == 0
  AND LivingCareCount == 0
  AND PendingAdmissionCount == 0
```

`RecoverablePawnCount` включает весь lifecycle unresolved Last Thread. Создание Ward не происходит внутри transition `RECOVERY_TRANSIT → CARE → READY`.

## 11. Закрытие Хроники (`LifeClosure`)

`Retirement` переименовывается в **Закрытие Хроники**. Это необратимый живой исход после сформированной механической жизни, без передачи силы, скидок, сервисов, recruitment, gear, tags или Continuity acceleration.

### 11.1. Состояния и единственный выбор

```yaml
formation_state: FORMING | FORMED
closure_arc_state: LOCKED | OPEN | COMMITTED | RESOLVED | FORECLOSED
closure_state: LOCKED | CLOSURE_READY | CLOSED_CIVIC
```

```text
reserved_lifetime_slot_count = 3
AND revealed_manifestation_count = 3
→ FORMED + closure_arc_state OPEN

closure_arc_state = RESOLVED through ordinary Normal Threshold
→ CLOSURE_READY
→ Pawn временно nondeployable
→ один необратимый выбор:
   CLOSED_CIVIC сейчас
   OR RETURN_TO_FIELD
```

`CLOSURE_READY` не является парковкой. `RETURN_TO_FIELD` возвращает Пешку в поле и навсегда закрывает generic safe closure; повторно доступна только отдельная future fiction-specific ветвь после lore-approved контракта. Сторонняя closure-ветвь не входит в активные enum, transition или acceptance.

### 11.2. Closure grammar

Для каждого `PawnID` создаётся один `closure_arc_instance_id`: hero-kit, три manifest sources и ключевые Chronicle facts выбирают один authored `ClosurePatternID`, фиксируют instance и не допускают reroll. Pattern меняет обычное решение, имеет видимый Commitment и terminal Chronicle consequence, но не выдаёт четвёртый tag, stat, наследуемый perk или recruitment roll.

```text
cancel before commit → OPEN; тот же PatternID
ordinary failure while Pawn alive → OPEN или RESOLVED с объявленным residue
Breakline / Last Thread Recovery → OPEN; тот же instance
Normal Threshold + terminal choice → RESOLVED
KIA → FORECLOSED
```

### 11.3. Civic closure

```text
CLOSURE_READY
→ CLOSED_CIVIC
→ readiness = CLOSED
→ deployable = false
→ person_state = ALIVE_CLOSED
→ procedural_targetable = false
→ recruitment_targetable = false
→ Chronicle preserved
```

Это обязательный базовый положительный исход. Человек остаётся жив в Хабе, отношениях и эпилоге, но не возвращается в roster и не становится обычной целью procedural Cargo/MIA/KIA. Fiction-specific branches отложены до отдельного lore-approved контракта и не являются активной ветвью этой state machine.

### 11.4. ReadyCount и смена поколений

`CLOSED_CIVIC` не входит в `ReadyCount`. После атомарного closure пересчитывается `ContinuityAdmissionAllowed`; closure не обновляет Foundling pools, не ускоряет faction candidates, не передаёт tags и не усиливает нового Ward.

## 12. Общий жизненный цикл Пешки

```text
ADMITTED
→ READY / FORMING / LastThread AVAILABLE

READY
→ SELECTED
→ BREACH_COMMITTED
→ IN_RAID

IN_RAID
├─ ordinary return ───────────────→ READY или CARE
├─ Breakline success ─────────────→ CARE/READY, body only
├─ AUTHORED_MIA ──────────────────→ MIA_AUTHORED + MIAContract
├─ eligible FIELD_RECOVERABLE ────→ source CLOSED_FAILED + RECOVERY_TRANSIT
├─ WORLD_CONFIRMED_FATAL ─────────→ KIA
└─ terminal override ─────────────→ KIA

RECOVERY_TRANSIT
└─ RecoveryContract PENDING_CHOICE
   ├─ RecoveryCommitted ──────────→ MATCH_COMMITTED; attempt/squad sealed
   ├─ pending terminal unknown fate → LOST_CLOSED/MIA_FORECLOSED; SPENT + TERMINAL
   └─ ADMINISTRATIVE_HOLD ────────→ reconcile same contract

MATCH_COMMITTED
└─ valid target BreachCommitted ──→ ACTIVE in COMMON-POOL overlay; claim/presence/clock атомарны

ACTIVE
├─ SELF RecoveryThresholdSync ────→ RAID(target) → CARE → HUB/READY; LastThread SPENT
├─ SQUAD BodyRecoverySync ────────→ RAID(target) → CARE → HUB/READY; LastThread SPENT
├─ collapse ──────────────────────→ COLLAPSED_RESCUABLE
└─ terminal world/system resolver → KIA; SPENT + TERMINAL

recovery_life_state = COLLAPSED_RESCUABLE
├─ valid BodyRecoverySync ────────→ CARE → READY
└─ deadline / Final Stabilization / WORLD_CONFIRMED_FATAL → KIA

MIA_AUTHORED
├─ recovery success ──────────────→ CARE/READY
└─ failure/expiry/abandon ────────→ KIA

FORMING
→ 3 reserved + 3 revealed manifestations
→ FORMED / closure arc OPEN
→ closure arc RESOLVED
→ CLOSURE_READY
├─ RETURN_TO_FIELD ───────────────→ READY; generic safe closure FORECLOSED
├─ civic closure ─────────────────→ CLOSED_CIVIC
└─ иных активных closure branches нет

KIA, LOST_CLOSED и CLOSED_CIVIC — необратимые terminal operational states.
```

## 13. Теги: cap, inactive, Scar и mastery

### 13.1. Lifetime cap

```yaml
tag_lifecycle_state:
  LATENT_DORMANT
  REVEAL_PENDING
  ACTIVE
  INACTIVE

reserved_lifetime_slot_count: 0..3
revealed_manifestation_count: 0..3
active_effect_count: 0..3
```

Правила:

- `reserved_lifetime_slot_count` считает `LATENT_DORMANT`, `REVEAL_PENDING`, `ACTIVE` и `INACTIVE`;
- `revealed_manifestation_count` считает только `ACTIVE` и `INACTIVE`;
- оба счётчика `<= 3` всегда;
- новый source и Scar проверяют reserved-count, поэтому два pending-события не переполняют cap;
- `INACTIVE` отключает эффект, но не освобождает lifetime-slot;
- удаление, несовместимость или сюжетное угасание тега не создаёт четвёртый roll;
- источник тега фиксируется отдельно: `FIRST_RETURN`, `ORIGIN`, `SCAR`, `AUTHORED`;
- один lifecycle event не создаёт два manifestations;
- повторная активация старого тега не увеличивает ни один count;
- formation/closure начинается только при `reserved = 3 AND revealed = 3`, а не при трёх одновременно активных эффектах и не при скрытом третьем слоте.

### 13.2. Положительный tag

Положительный tag разрешён без симметричного штрафа, если он:

- локален;
- читаем в сцене;
- не универсален;
- меняет решение, а не просто повышает все числа;
- не переписывает PvP-правило или обязательную стадию действия.

Если tag широко сокращает Commitment/Recovery, отменяет tell, меняет PvP-доступ или работает почти в каждой сцене, ему требуется явный debt с protected floor.

### 13.3. Scar при заполненном cap

Если действие обязано создать постоянный Scar, а три lifetime-slots уже зарезервированы, нельзя:

- молча создать четвёртый tag;
- удалить старый;
- превратить Scar в бесплатный временный статус;
- разрешить действие без обещанной цены.

Целевая ветвь по умолчанию:

```text
Action preview
→ permanent Scar required
→ reserved_lifetime_slot_count = 3
→ действие не разрешается
→ payload не возникает
→ HUD: permanent carrier debt cannot manifest
```

Если отдельно нужен last-stand, это другой явный контракт: `BROKEN_LAST_STAND → terminal KIA`. Он не создаёт persistent modifier, не допускает Breakline/MIA/Last Thread и не возвращает deployable Пешку. Пока такой terminal action не канонизирован полностью, он недоступен.

### 13.4. Mastery

Mastery не хранится как повторяемый рецепт «сделай действие N раз». Источник обязан быть прожитым контекстом и не должен позволять безопасно фармить прогресс в Хабе или Recovery.

Off-class остаётся off-class:

- tag может локально открыть процедуру или изменить цену;
- tag не переписывает hero-kit kernel;
- tag не выдаёт полную чужую proficiency;
- повторение одного безопасного действия не превращает любую Пешку в универсального специалиста.

Один Mastery-tag даёт ровно **одно** механическое выражение:

- либо один разрешённый шаг proficiency и открывающийся из него authored moveset;
- либо одну named technique без повышения proficiency.

Одновременно выдавать `+1 proficiency` и отдельную `mastery_expression` запрещено: это двойная награда за один lifetime-slot.

### 13.5. Источники последующих тегов

Personal Tags не являются меню улучшений и не выводятся из повторяемого поведения. Игрок не выбирает TagID после события. Его выбор начинается после проявления: кого выводить, какой loadout собирать, какую роль принять и стоит ли дальше рисковать человеком.

Разрешённые классы источников:

| Source class | Когда фиксируется TagID | Что делает игрок | Когда активируется |
|---|---|---|---|
| `LATENT_IDENTITY` | При создании Pawn/Candidate occurrence | Возвращает человека живым | После первого самостоятельного ordinary return |
| `AUTHORED_OCCURRENCE` | При создании уникального occurrence, до пользовательского outcome | Входит в событие либо отказывается от него | После необратимого Commitment и Normal Threshold |
| `PHYSICAL_CONSEQUENCE` | В момент уникальной травмы/воздействия | Решает продолжать, спасать тело или выходить | После Normal Threshold; до него работает только временное состояние |
| `PROCEDURE_COMMITMENT` | До принятия процедуры | Соглашается на известный класс необратимой процедуры, но не выбирает roll | После завершения процедуры и её threshold |

Не являются источниками:

- счётчик повторений действия;
- число убийств;
- количество лечений под огнём;
- использование одного Frame N раз;
- безопасная практика в Хабе;
- Last Thread Recovery;
- Breakline;
- намеренный self/squad damage;
- UI-выбор из двух perks после экстракции.

### 13.6. `ManifestationOpportunity`

```yaml
ManifestationOpportunity:
  occurrence_id
  pawn_id
  source_class
  source_definition_id
  assigned_tag_id
  assignment_revision
  assignment_event_id
  commitment_state: OFFERED | COMMITTED | REFUSED | CLOSED
  activation_gate
  terminal_outcome_id
```

Инварианты:

- `assigned_tag_id` фиксируется до необратимого пользовательского outcome;
- повторное открытие экрана, reconnect или отказ не меняют assignment;
- `occurrence_id` закрывается при принятии, отказе, потере custody, MIA или KIA;
- один occurrence не создаёт следующий occurrence;
- tag pool не обновляется через KIA, closure или handoff;
- до Normal Threshold рейд может хранить temporary condition, но не постоянный tag effect;
- assignment идемпотентно увеличивает reserved-count ровно один раз, а reveal — revealed-count ровно один раз.

### 13.7. Viability filter, а не synergy filter

Перед assignment исключаются только технически мёртвые теги. Tag viable, если:

- его `target_owner` и parameter существуют у этой Пешки;
- тело способно выполнить требуемое действие либо получить совместимый физический инструмент;
- в игре существует хотя бы одна достижимая сцена, где effect меняет решение;
- tag имеет наблюдаемый tell/result;
- он не требует несуществующей proficiency или анатомически невозможного предмета.

Фильтр не имеет права учитывать:

- текущую мету;
- текущий loadout;
- «хорошую синергию» с hero-kit;
- широту эффекта;
- предпочтения игрока;
- то, есть ли в ростере более сильная Пешка.

Странный, узкий и неудобный tag допустим. Физически невозможный или никогда не меняющий решения — нет.

### 13.8. Редкость, сила и combat cap

- `rarity != power`;
- редкость описывает частоту источника/события, а не универсальную величину бонуса;
- каждый tag обязан создавать хотя бы один реальный новый способ использовать Пешку;
- максимально два из трёх reserved lifetime-slots могут принадлежать combat tags;
- если два combat tags уже заняты, третий manifestation обязан быть noncombat; grammar обязана гарантировать достижимую noncombat opportunity;
- чистый положительный tag допустим по правилам §13.2;
- несовместимость с привычным hero-kit допустима и создаёт билд-задачу;
- объективно мёртвый roll запрещён viability filter;
- после `reserved_lifetime_slot_count = 3` pool больше не читается, даже если один эффект inactive или один tag ещё latent.

Свободной замены, fusion или respec после заполнения cap нет. Лечение может изменить физическое условие работы существующего TagID или вернуть его из `INACTIVE`, но не создаёт новый roll и не откладывает завершённость формирования.

## 14. Реестр эксплойтов и обязательных закрытий

| Abuse chain | Архитектурное закрытие |
|---|---|
| KIA единственного Ward → новый mechanical roll | Stable ContinuityProfileID; смерть не продвигает Recruitment Opportunity |
| Раскрыть неудобный First Return → убить → reroll | First Reception выдаёт тот же continuity profile; KIA не меняет candidate source |
| Спасти Foundling → увидеть Origin → оставить только удачных | Origin latent до необратимого roster commitment |
| ReadyCount=0 при recoverable MIA/CARE → получить Ward → вернуть старого | Общий admission-predicate требует `RecoverablePawnCount=0` и `LivingCareCount=0` |
| Накопить много unresolved Last Thread Pawns | Один `account_last_thread_slot`; остальные Ready могут ходить, но без Last Thread-защиты, пока slot занят |
| Suicide-scout → Recovery → вернуться в изученный seed | Исходный `source_raid_session_id` закрыт; COMMON-POOL target скрыт до commit и не может быть reroll |
| Breakline → провал → Last Thread | `BREAKLINE_FAILURE` terminal override |
| Last Thread внутри Recovery | Второй перехват невозможен: account custody остаётся занята до terminal outcome |
| Teamkill ради контролируемой Recovery | Self/friendly FIELD_RECOVERABLE перехватывается так же, как hostile; прямого KIA нет |
| Logout ради нового recovery seed | После commit тот же target binding и squad snapshot; технический сбой даёт ADMINISTRATIVE_HOLD, не reseed/free attempt |
| Recovery farm тегов/награды/предметы | Нет Normal Threshold, tag reveal, standard loot, reward или extractable local kit |
| Reserve даёт пассивную силу | Unselected Ready не имеет отдельного state и ничего не производит |
| Exact specialist превращается в обязательный ключ | У каждой обязательной задачи есть baseline route; specialist меняет цену/темп/маршрут |
| Генератор видит build и создаёт «честную» контру | Build не входит в seed/generation inputs |
| Saved doctrine клонирует ItemID | Draft — план; финальная reservation атомарно проверяет физические экземпляры |
| Hybrid Термоса сжимает несколько билдов в один предмет | Независимые функции платят service load и релевантную same-raid цену; без atomicity proof сложный пакет дробится |
| Support capacity финансирует сама себя | Совокупный SupportLoad всей support-группы обязан помещаться в Base до применения любого delta |
| Тег + модуль + батарея обнуляют Recovery | Один parameter owner, stack group и protected floor |
| Двойной Парадокс автоматически создаёт контру | `runtime_authority: none`; только review hypothesis |
| Инактивировать тег → освободить слот → получить четвёртый | Inactive продолжает занимать lifetime manifestation slot |
| Scar при заполненном reserved-cap превращается в бесплатный эффект | Действие и payload запрещены; отдельный last-stand возможен только как terminal KIA без Last Thread |
| Closure слабой Пешки ради нового specialist-roll | Нужны 3 reserved + 3 revealed manifestations и closure arc; admission profile стабилен; candidate pool не меняется |
| Closure-ветвь превращается в рынок тел | Активна только CLOSED_CIVIC; fiction-specific branches deferred до отдельного lore-approved контракта |

## 15. Масштабирование без новых дубликатов

### 15.1. Новый Personal Tag

Обязан указать:

- source;
- lifecycle state transitions;
- target owner/parameter;
- stack group;
- locality;
- tell;
- debt и floor, если меняет широкую стадию;
- условия inactive;
- подтверждение, что reservation/reveal не меняют соответствующий счётчик повторно.

Не может создавать новый глобальный resolver.

### 15.2. Новый hero-kit

Обязан указать:

- authored P/Q/E и фактические windows;
- одну `BaseServiceCapacity` по шести стабильным семействам;
- known role для roster-meta;
- baseline gaps;
- review приоритетных Double Paradox hypotheses.

Не получает bespoke allowlist модулей и не обязан реализовать каждое ребро графа.

### 15.3. Новый модуль Термоса

Обязан использовать:

- существующий mount-topology interface; fit остаётся отношением `Body ↔ Thermos`;
- все и только реально работающие service families;
- существующего domain owner;
- EffectContract;
- physical mass;
- конкретный Dissonance source, если он существует;
- один mechanism/failure-state для атомарного предмета.

Три и более service families требуют `atomicity_proof`: общий mechanism, trigger/lifecycle, failure-state и vulnerability. Без доказательства предмет оформляется как assembly/preset. Исключительный body-coupled модуль объявляет `body_interface_requirement`, но не получает собственного `fit_profile`.

Новое service family — миграция всей системы, а не обычное добавление контента.

### 15.4. Новая аномалия или контракт

Обязаны публиковать:

- forecast semantics до выбора Пешки;
- baseline route без редкого личного ключа;
- specialist advantages;
- lethal resolution classes;
- semantic generation validation;
- точный terminal override, если обычный Last Thread не допустим.

## 16. Порядок переноса в канон

Модель-писатель не принимает новых дизайн-решений. Она переносит этот пакет по владельцам и после каждого шага проверяет отсутствие второй копии.

1. **[[04_Player_Entities/Lifecycle_Roster|Lifecycle_Roster]]**
   - заменить Deck/active/Reserve на Roster + Prepared Cases;
   - добавить authoritative fields Last Thread и Life Closure;
   - включить полную state machine;
   - определить `RECOVERY_TRANSIT`, `COLLAPSED_RESCUABLE`, `LOST_CLOSED/MIA_FORECLOSED`, `account_last_thread_slot: EMPTY | RecoveryID` и `CLOSED_CIVIC`;
   - зафиксировать атомарный FIELD_RECOVERABLE intercept без player-owned KIA и world/system-only terminal resolver.

2. **[[04_Player_Entities/Spawn_Logic|Spawn Logic]]** и **[[03_Factions_Societies/Lore/The_First_Reception|The First Reception]]**
   - развести Continuity Admission и Recruitment Opportunity;
   - добавить полный continuity profile/epoch contract;
   - использовать единый `ContinuityAdmissionAllowed` с Recoverable/LivingCare/Pending counts;
   - удалить возможность продвигать механический профиль смертью.

3. **[[08_World_Generation/Generation/19_Access_Contracts|Access Contracts]]**
   - оставить выбор любой `ReadySelectable` Пешки;
   - не читать Prepared Cases;
   - добавить `ForecastRevisionID` и атомарный LoadoutSnapshot;
   - закрыть исходный `source_raid_session_id` при атомарном Last Thread intercept;
   - реализовать COMMON-POOL Recovery overlay, target binding и atomic presence/claim transfer без отдельной recovery-сессии.

4. **[[04_Player_Entities/Tags_System|Tags System]]**, **[[04_Player_Entities/_Registries/Registry_Tags|Registry Tags]]** и **[[04_Player_Entities/Proficiency_Arsenal|Proficiency Arsenal]]**
   - добавить lifecycle states, reserved lifetime slots и revealed manifestation count;
   - зафиксировать First Return при `PawnIDCreated`;
   - задать reveal event;
   - определить inactive и Scar-at-cap;
   - запретить tag reveal в Recovery/Breakline;
   - удалить repeat-action recipes;
   - каждый Mastery-tag даёт proficiency-step **либо** named technique, но не оба результата.

5. **[[04_Player_Entities/Trait_Development|Trait Development]]**
   - удалить вывод First Return из поведения;
   - оставить Chronicle фактам вылазки;
   - добавить ClosurePattern/instance grammar;
   - отделить formation от closure readiness.

6. **[[04_Player_Entities/Shell_Foundlings|Shell Foundlings]]**
   - перенести Origin reveal после roster commitment и первой самостоятельной ordinary return;
   - фиксировать Origin TagID до rescue input;
   - гарантировать terminal CandidateOccurrenceID при любом исходе.

7. **[[01_Core_Vision/Build_Extraction_Concept_Slice|Build Extraction Concept Slice]]**
   - закрепить `Known Self / Unknown World`;
   - убрать старую active-deck причинность;
   - заменить event-derived First Return на latent reveal;
   - не дублировать подробные state machines из authoritative pages.

8. **[[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile Pipeline]]** и целевой `Registry_Parameter_Contracts.md`
   - закрепить три lifecycle envelopes: ACTION, PERSISTENT_STATE, REACTIVE_EVENT;
   - Pipeline владеет порядком resolution, ParameterContract — domain policy;
   - запретить локальным источникам собственные stack priority/floor/cap;
   - определить counterplay deadline для переносимых долгов.

9. **[[05_Combat_Survival/Dissonance_System|Dissonance System]]**
   - развести persistent signature и один event на physical occurrence;
   - батарею/модуль записывать contributors, а не вторыми событиями;
   - закрепить единственную агрегацию и Gate-output;
   - удалить прямые Gate modifiers из тегов и модулей.

10. **[[07_Gear_Inventory/Thermos_System|Thermos System]]** и registries
   - закрепить Термос как всю wearable-equipment system;
   - разделить model definition, module definition и assembly instance;
   - заменить неоднозначные positions на mount patterns/nodes;
   - переименовать capacity в service semantics;
   - сделать итоговые поля derived;
   - добавить assembly resolver как consumer ParameterContracts и Dissonance ownership;
   - добавить progressive disclosure.

11. **[[04_Player_Entities/Two_Paradox_Vector_Matrix|Two Paradox Vector Matrix]]**, **[[04_Player_Entities/_Matrices/00_Synergy_Map|Synergy Map]]**, **[[04_Player_Entities/MVP_3x3_Design_Contract|MVP 3x3 Contract]]**
    - назначить единый graph registry;
    - убрать authored-дубли `weak_to/paradoxRules`;
    - переименовать outputs в hypotheses/signals;
    - нормализовать mono/dual pressure;
    - заменить вечный pairwise-writing на приоритетный review;
    - создать отдельный `04_Player_Entities/_Matrices/Registry_Double_Paradox_Reviews.md`; `Registry_Combos` не получает из него runtime-полей.

12. **[[09_Project_Management/Risk_Register|Risk Register]]**
    - `R08`: уточнить границу `design hypothesis → authored runtime`, а не считать матрицу фактической контрой;
    - `R23`: заменить event-derived First Return на creation-fixed latent tag;
    - `R30`: проверить source-bound ImpulsePacket и same-raid Pareto debt;
    - `R32`: добавить lifetime cap, inactive и mastery guard;
    - `R47`: zero-roster admission использует Ready/Recoverable/LivingCare/Pending predicate;
    - `R48`: Foundling Origin раскрывается после roster commitment.

13. После переноса обновить индекс и удалить устаревшие формулировки, а не оставлять их как «исторические варианты» внутри активного канона.

## 17. Критерии приёмки архитектуры

### 17.1. Уверенность игрока

- [ ] До commit игрок видит все известные свойства выбранной Пешки и итоговые долги сборки.
- [ ] Ни один latent tag не влияет на raid до reveal.
- [ ] Forecast появляется до выбора Пешки и имеет revision.
- [ ] Генератор не читает build.
- [ ] У каждой обязательной задачи есть baseline route без редкого Personal Tag.

### 17.2. Ростер и recruitment

- [ ] Любая ReadySelectable Пешка доступна независимо от Prepared Cases.
- [ ] Unselected Ready не даёт пассивной ценности.
- [ ] Смерть, handoff, closure и отказ не продвигают Recruitment Opportunity.
- [ ] Continuity Admission не печатает новый механический roll.
- [ ] Foundling Origin TagID существует до rescue input и admission его не меняет.
- [ ] Origin остаётся dormant в первой собственной вылазке и раскрывается только после eligible ordinary return.
- [ ] `ContinuityAdmissionAllowed` требует ноль Ready, recoverable Pawns, living Care и pending admissions.

### 17.3. First Return и tags

- [ ] First Return TagID существует до первого raid input.
- [ ] Chronicle не является входом выбора TagID.
- [ ] Breakline/Recovery/MIA не раскрывают tag.
- [ ] Inactive tag продолжает занимать lifetime slot.
- [ ] Невозможно получить четвёртый manifestation через Scar, reset или повтор activation.
- [ ] При двух combat tags третий manifestation обязан быть noncombat, а grammar гарантирует достижимую noncombat opportunity.

### 17.4. Термос

- [ ] Fit, topology, service, effect, mass, Dissonance и economy имеют непересекающиеся authority contracts; один system может владеть несколькими, но один результат не имеет двух источников истины.
- [ ] Definition-state не смешан с instance-state.
- [ ] Совокупный SupportLoad всей support-группы помещается в Base до применения любого ServiceSupportDelta.
- [ ] Effect axes derived и не участвуют в legality.
- [ ] Preset не резервирует один ItemID дважды.
- [ ] Все несовместимости показываются одним resolver-pass.
- [ ] Raid UI не требует решать монтажную задачу заново.
- [ ] Каждый modifier читает один ParameterContract; source не задаёт priority/floor/cap.
- [ ] Shadow-resolver мигрирует по одному domain owner и удаляет old resolver только после parity.
- [ ] Protected-floor tooltip показывает requested/applied/floor/final/reason/revision.

### 17.5. Двойной Парадокс

- [ ] Один источник `dominates` и graph version.
- [ ] Ни один runtime-export или player-facing consumer не содержит и не читает hypothesis outputs, включая combat, AI, spawn, loot, generation, matchmaking, Gate, Access, loadout и UI.
- [ ] Фактические matchup-утверждения имеют authored scene/evidence.
- [ ] Mono/dual outputs нормализованы.
- [ ] Новый candidate-coordinate не создаёт обязательный production-slot.

### 17.6. Last Thread и closure

- [ ] Первый eligible FIELD_RECOVERABLE, включая self/friendly, атомарно перехватывается при доступной Нити; противник не владеет причиной KIA.
- [ ] Source ParticipationClaim становится CLOSED_FAILED, ledger Consumed, а gear/Cargo остаются ContestableWreck; живого PawnID в source нет.
- [ ] Recovery использует другой уже живой public PvPvE SessionID, обычный physical seat и COMMON-POOL overlay без отдельной очереди.
- [ ] RecoveryCommitted запечатывает attempt_count=1 и squad snapshot, но не создаёт live presence или ParticipationClaim.
- [ ] Valid target BreachCommitted атомарно фиксирует target, ParticipationClaim, presence transfer и active clock.
- [ ] Solo baseline достаточен; escort допускается только precommitted со своей Ready Pawn, stake/seat/claim и NeverParticipated target.
- [ ] Collapse создаёт один непаузаемый rescue_deadline_at; effective deadline учитывает Final Stabilization.
- [ ] Успех возможен только через SELF RecoveryThresholdSync или SQUAD BodyRecoverySync; чужие ItemID и награды не переходят.
- [ ] Pending выход ведёт в LOST_CLOSED/MIA_FORECLOSED, а не KIA.
- [ ] Исходная ставка и `source_raid_session_id` не возвращаются.
- [ ] Pending Last Thread занимает единственный account-slot и подавляет Continuity Admission, но не доступ к другим Ready-Пешкам.
- [ ] Пока slot занят, временная недоступность Last Thread у других Пешек видна до их commit.
- [ ] `MIA_AUTHORED` имеет success, failure и zero-ready fallback.
- [ ] CARE/Recovery outcome не открывает промежуточное окно для создания Ward.
- [ ] Recovery не выдаёт loot, tags, First Return или account reward.
- [ ] Closure требует три reserved и три revealed manifestations и доступен только Ready-Пешке в Хабе.
- [ ] Cancel, failure, Breakline и Last Thread не рероллят ClosurePatternID.
- [ ] Scar overflow не может вызвать Last Thread или создать четвёртый persistent modifier.
- [ ] Civic closure всегда существует и оставляет человека живым.
- [ ] `CLOSED_CIVIC` не возвращается в procedural lifecycle.
- [ ] CLOSURE_READY требует немедленный необратимый выбор CLOSED_CIVIC либо RETURN_TO_FIELD; сторонняя closure-ветвь отсутствует в active state machine.
- [ ] Ни одна closure-ветвь не наследует build power.

## 18. Что остаётся эмпирическим

После утверждения архитектуры тестами калибруются только:

- насколько подробным должен быть SortieForecast;
- насколько specialist лучше baseline по времени, цене и надёжности;
- время и объяснимость выбора при 3, 12 и 30 Ready-Пешках;
- сравнение baseline/specialist/perfect-counter на одном forecast: последний может сильно менять цену или маршрут, но не становится hard-key и не удаляет всю сцену;
- действительно ли T1 превращается в reveal-конвейер;
- сколько итогов одновременно выдерживает экран подготовки;
- NearDeath penalties, recovery kit, длина маршрута и `RecoveryThresholdSync`;
- насколько solo-viable Recovery и precommitted escorts воспринимаются как справедливое продолжение проигрыша;
- частота ClosurePattern и производственная стоимость их вариаций;
- читаемость шести service families и topology Термоса;
- полезность Double Paradox review priority и числовой `review_budget_per_kit`.

Не являются эмпирически открытыми:

- причинность First Return;
- право выбрать любую Ready-Пешку;
- отсутствие build-adaptive seed;
- отсутствие скрытой четвёртой tag-ячейки;
- один владелец каждого параметра;
- одна попытка Last Thread;
- потеря исходной ставки;
- отсутствие account-power от closure;
- отсутствие runtime-власти Двойного Парадокса.

## 19. Короткая формула целевой системы

```text
неизвестный мир
+ полностью известная себе Пешка
+ известный до выбора forecast
+ широкая библиотека проявленных специалистов
+ физически собранный и потеряемый Термос
+ один общий resolver эффектов и долгов
+ одна последняя незакрытая судьба
+ добровольное живое завершение без наследуемой силы
= уникальный extraction buildcraft без TOUCH-перегруза и без жанрового обмана
```
