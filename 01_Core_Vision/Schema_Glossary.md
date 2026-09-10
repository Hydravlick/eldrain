---
type: core_concept
status: active
system: core_vision
tags: [glossary, definitions]
---
# Внутренние термины GDD

[[01_Core_Vision/Glossary|Все слои словаря]] · [[01_Core_Vision/World_Vocabulary|Слова мира]] · [[01_Core_Vision/Player_Mechanics_Glossary|Понятия игрока]]

Краткие значения межсистемных имён. Формулы, поля записей и разрешение переходов принадлежат связанным владельцам. Включение имени сюда не назначает слово мира или готовую UI-надпись.

## Сессия, ревизии и транзакции

- **SessionID** — идентификатор конкретной живой рейдовой сессии. Участие и повторный вход: [[08_World_Generation/Anomaly/Insertion_Logic|Insertion Logic]].
- **SessionRuntime** — локальное состояние одного SessionID: двери, враги, предметы, следы и действия. Не переписывает общее основание локации. [[08_World_Generation/Generation/Server_Lifecycle|Server Lifecycle]].
- **LocationRevision** — общее прегенерированное основание цикла: геометрия, маршруты, кандидаты контента. [[08_World_Generation/Generation/Location_Revision_Lifecycle|Location Revision Lifecycle]].
- **StableProjection** — low-poly представление LocationRevision на Живой Миниатюре, карта и интерфейс адресов в лобби. Это не прогулочная локация. [[08_World_Generation/Generation/Location_Revision_Lifecycle|Жизненный цикл проекции]].
- **StablePOISelection** — ограниченный выбор активных адресов среди кандидатов ревизии; прочие элементы могут остаться диорамой. [[08_World_Generation/Generation/Dual_State_POIs|Dual-State POIs]].
- **WorldRevision** — опубликованная связка ревизий локаций, проекций и активных адресов для regional shard. [[08_World_Generation/Generation/Location_Revision_Lifecycle|Публикация мира]].
- **SyncLease** — ограниченное обязательство синхронизации конкретного участника у Порога; условия прерывания и завершения ведёт [[08_World_Generation/Anomaly/Extraction_System|Extraction System]].
- **EntryQuote** — неизменяемая котировка для раскрытой цели с привязанными снимками состояния, ценой, потерями и временными границами. [[08_World_Generation/Generation/Raid_Approach_and_Entry|Approach and Entry]].
- **ReturnManifest** — атомарная транзакция подтверждённого возврата переносимого графа предметов. Не выполняет Напоминание или разрешение спора о праве. [[06_Economy_Loot/Return_Manifest_Contract|Return Manifest Contract]].
- **regional shard / reconnect** — региональная сервисная область / восстановление соединения с соблюдением правил участия. Не связаны с метафизическим Осколком. [[08_World_Generation/Generation/Async_Timers|Региональный сервис]], [[08_World_Generation/Anomaly/Insertion_Logic|участие]].

## Метрики и предметные категории

- **DissonanceLoad** — постоянный вклад предметов, тела и объявленных сохраняющихся источников; **DissonancePulse** — вклад конкретного физического действия; **AnomalyPressure** — Load вместе с недавним затухающим Pulse. Один occurrence не учитывается повторно по батарее, модулю и действию. [[05_Combat_Survival/Dissonance_System|Dissonance System]].
- **Reality Buffer: Shell.Reality_Buffer / reality_buffer** — отдельный телесный вклад поглощения фазового импульса. В текущем MVP равен 0; это не вся защита. [[07_Gear_Inventory/Calibration_Contract|Calibration Contract]], [[08_World_Generation/Generation/Gate_Check|Gate Check]].
- **ProtectionScore / Battery.Buffer** — итог отдельных действующих защит и штрафов / самостоятельный батарейный вклад в фазовый расчёт. [[08_World_Generation/Generation/Gate_Check|Gate Check]].
- **ResolvedEnvironmentProtection** — модульный вклад защиты среды с незакрытым MISSING_OWNER; неизвестное значение не считается нулём. [[07_Gear_Inventory/Calibration_Contract|Граница калибровки]].
- **Embedded Legacy / Civic Legacy** — встроенное наследие места / его общественная роль и последствия; GDD-категории, не личная доставка. [[06_Economy_Loot/Extraction_Stabilization_Loop|Цикловое наследие]].
- **Unstabilized Transfer** — передача с неоформленным правом, а не синоним материального Volatile. [[06_Economy_Loot/P2P_Interaction|Передача]].

## Ростер и боевой дизайн

- **Pawn** — GDD/ID-обозначение смертного жителя с прошлым, характером и телом, совместно проживающего вылазку с Осколком. Общую волю он воспринимает как собственную. Статус слова в мире и UI — AUTHOR_DECISION. [[04_Player_Entities/Entity_Grimoire|Entity Grimoire]].
- **Ready Pawn / ReadySelectable** — внутренняя категория готового принятого жителя / predicate доступности выбора. Экипировка, Presence и гражданский статус разрешаются отдельно. [[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]].
- **Ward** — внутренний ключ гражданского статуса Подопечного. Может сочетаться с готовностью; не является типом тела или собственностью. [[04_Player_Entities/Spawn_Logic|Spawn Logic]].
- **Welfare** — фиксированная loadout loan с собственной eligibility; не общий гражданский минимум, не награда за смерть или допуск. [[04_Player_Entities/Spawn_Logic|Выдача снаряжения]].
- **Breakline** — внутреннее имя аварийного выхода до окончательной KIA с необратимым Forfeit и отдельными последствиями для тела и груза. World/UI label остаётся AUTHOR_DECISION. [[06_Economy_Loot/Extraction_Stabilization_Loop|Breakline]].
- **Spec / полевой профиль Race × Spec** — слой методологии / отдельная authored-реализация пересечения тела и практики: P/Q/E, decision signature, именованный арсенал, модули, долги и Exposure. Не вычисляется сложением родителей и не получает автоматическую постоянную слабость. [[04_Player_Entities/Skill_Build_Philosophy|Профили]].
- **Schema-only ID** — стабильный ключ реестра. `assault`, `support`, `scout` соответствуют Застрельщику, Ладчику, Страннику в данных, а не именам партийных ролей. [[04_Player_Entities/Skill_Build_Philosophy|Специализации]].
- **Frame / Pattern / ItemID / Action** — переносимый оружейный язык / повторяемая конструкция с moveset / физическая копия со ссылкой на Pattern / конкретное исполнение и принятый долг. Старый weapon `instance_id` обозначал конструкцию и остался только в legacy; target definition ID — `pattern_id`. [[05_Combat_Survival/Weapon_Core|Weapon Core]].
- **Proficiency** — личное отношение `(PawnID, FrameID)`, список `frame_proficiencies` с уровнями 0–3. Профиль задаёт исходные отношения; runtime принадлежит Пешке. При prof >= 1 полный moveset Pattern. Прежняя MasteryContribution-формула superseded. `load_tier` остаётся отдельной нагрузочной осью старой progression-модели. [[04_Player_Entities/Proficiency_Arsenal|Владение]].
- **Cadence Gate** — ограничитель следующего сильного действия: взвод, охлаждение, сброс или иной телесно читаемый цикл. **Emission Profile** — способ доставки воздействия: импульс, линия, веер или механическая игла. **Action debt** — принятый Commitment, телесные claims и Recovery конкретного исполнения; Heat и техническая готовность остаются у ItemID. [[05_Combat_Survival/Weapon_Core|Weapon Core]].

- **Prepared Set layout / actual occupancy / Action claims / custody** — ссылки на подготовленную конфигурацию / фактическое удержание / принятые ограничения конкретного Action / физическое существование, размещение и reservation ItemID. Первые два состояния принадлежат [[07_Gear_Inventory/Equipment_PaperDoll|PaperDoll]], claims — [[05_Combat_Survival/Combat_Three_Debts|Action]], custody — [[07_Gear_Inventory/Inventory_Architecture|Inventory]].
- **weapon_channel_1/2 / aim / switch_weapon_set** — semantic intent IDs [[01_Core_Vision/Input_Contract|Input Contract]]. Set channels адресуют операции Pattern без внутреннего selected-weapon слоя; Aim recipient не переназначает channels. Switch Set меняет всю конфигурацию. Default bindings Switch Set и cantrip остаются TBD.

## Profile service budget

**BaseServiceCapacity** — authored поле полного Field Profile; values хранятся в Registry Combos по [[04_Player_Entities/Skill_Build_Philosophy#BaseServiceCapacity|profile owner]]. Proficiency его не вычисляет. FinalServiceCapacity/UsedServiceCapacity и legality разрешает [[07_Gear_Inventory/Thermos_Assembly|Thermos Assembly]].

## Battery и magazine

- **battery_state** — `Full | Drained` одного физического Battery ItemID; ровно одна атомарная транзакция из Full. [[05_Combat_Survival/Magic_Batteries|Magic Batteries]].
- **magazine_current / magazine_capacity** — текущий ресурс Weapon ItemID / authored ёмкость его Pattern; не общий запас Set и не состояние Battery. [[05_Combat_Survival/Weapon_Ranged|Weapon Ranged]].
- **reload** — отдельное сервисное намерение для одного concrete recipient, с физической source reservation и commit; не автоматическое действие пустого оружия. [[05_Combat_Survival/Magic_Batteries#3. Reload и получатель энергии|Reload contract]].

## Сохранённые старые имена

- **Shell / Оболочка** — прежняя внутренняя метафора человека; deprecated в нейтральном Lore. Пути и ключи сохранены, пустой контейнер ими не утверждается. [[04_Player_Entities/Entity_Grimoire|Личность]].
- **Deck / Колода** — deprecated метафора набора смертных персонажей. Текущий ростер состоит из живых людей с карточками; карточка не означает владения человеком. [[04_Player_Entities/Lifecycle_Roster|Ростер]].
- **Puppeteer / Кукловод; Foreman / Бригадир** — историческая UX-метафора / GDD-роль работы с ростером. Отдельного физического персонажа или управления марионетками не устанавливают. [[04_Player_Entities/Entity_Grimoire|Граница UX и личности]].
- **Reality Charge** — deprecated как отдельный второй расходник. Роль выполняют специальная батарея, overcharge-версия или режим устройства. [[05_Combat_Survival/Magic_Batteries|Батарейный контракт]].
- **Reality Resin** — старая внутренняя расшифровка Реза; не обязательное мировое имя или универсальное вещество. [[06_Economy_Loot/Currency_Rez|Рез]].
- **Frequency Tuner** — старое имя документа о регионе, задержке и доступности сервиса. Буквальная мировая процедура deprecated; название продуктового экрана открыто. [[08_World_Generation/Anomaly/Frequency_Tuner|Регион и качество соединения]].

Открытые авторские и механические решения собраны как задачи в [[09_Project_Management/TODO|TODO]]. Ни старое имя, ни краткая словарная запись не закрывают REVIEW у владельца.
