---
status: active
system: project_management
tags:
  - risk_register
  - decisions
  - mvp
related_files:
  - "[[08_World_Generation/Generation/Gate_Check]]"
  - "[[06_Economy_Loot/Currency_Rez]]"
  - "[[04_Player_Entities/Registries/Registry_Combos]]"
  - "[[06_Economy_Loot/Barter_System]]"
  - "[[03_Factions_Societies/Lore/The_Circle_of_Interposition]]"
type: project_management
---
# Risk Register: MVP Decisions

Описанные правила читаются по ссылкам на владельцев. Все строки ниже остаются открытыми; реестр не свидетельствует о проведённых испытаниях.

## Риски MVP

| ID | Риск | Что нужно проверить или решить | Статус | Владелец |
|:---|:---|:---|:---|:---|
| R06 | Будущее страховое решение может подорвать ставку пермадета | Сначала принять отдельное страховое решение; затем проверить его влияние на ставку пермадета. | in_progress | [[06_Economy_Loot/Sinks_Insurance]] |
| R07 | 9 комбо из 25 выглядят как неполнота | Спроектировать и испытать девять ячеек; различимость и полноту оценивать по общему контракту, а не по наличию строк. | in_progress | [[04_Player_Entities/MVP_3x3_Design_Contract]], [[04_Player_Entities/Registries/Registry_Combos]], [[04_Player_Entities/Combat_Profile_Pipeline]], [[04_Player_Entities/Views/Synergy_Map]] |
| R23 | First Return и Origin могут превратиться в скрытый рецепт, полный рандом или элитный каталог людей | Пройти тихую первую вылазку и попытки suicide-reroll; проверить объяснение Origin без каталога скрытой силы. | in_progress | [[04_Player_Entities/Lifecycle_Roster]], [[04_Player_Entities/Tags_System]], [[04_Player_Entities/Registries/Registry_Tags]], [[04_Player_Entities/Shell_Foundlings]] |
| R27 | Сильная броня плюс дешевое летальное оружие становится вечным оптимумом | Сравнить полную стоимость замены и повторяемую добычу Armor Rat с альтернативными комплектами. | in_progress | [[07_Gear_Inventory/Gear_Progression]], [[07_Gear_Inventory/Views/Item_Calibration_Matrix]], [[09_Project_Management/TODO]] |
| R28 | Один дорогой Frame позволяет всей бюджетной группе обойти оружейную прогрессию | Испытать группу с одним дорогим Frame на параллельной работе, длительном давлении и повторных дорогих циклах. | in_progress | [[07_Gear_Inventory/Gear_Progression]], [[05_Combat_Survival/Magic_Batteries]], encounter registries |
| R32 | Один сильный Personal Tag полностью определяет билд либо возвращает скрытый TOUCH | Проверить широкий набор задач и контрмер: личный тег не должен вытеснить профиль без наблюдаемой цены. | in_progress | [[04_Player_Entities/Tags_System]], [[04_Player_Entities/Registries/Registry_Tags]], [[04_Player_Entities/Proficiency_Arsenal]], [[04_Player_Entities/Combat_Profile_Pipeline]], [[04_Player_Entities/MVP_3x3_Design_Contract]], [[04_Player_Entities/Views/Synergy_Map]] |
| R34 | Многозонный легаси-пакет может закрыть несколько частей тела одним неоднозначным pattern | Для каждого заблокированного пакета получить topology, pattern-bound coverage и atomicity proof либо split; отсутствие данных оставляет публикацию заблокированной. | in_progress | [[07_Gear_Inventory/Thermos_System]], [[07_Gear_Inventory/Thermos_Assembly]], [[07_Gear_Inventory/Registries/Registry_Thermos_Modules]], [[07_Gear_Inventory/Views/Item_Calibration_Matrix]], [[09_Project_Management/TODO]] |
| R40 | Ward с Welfare становится оптимальным штатным смертником и одноразовым источником командной ценности | Сравнить прибыль и командную полезность сохранённой Ready-Пешки с регулярно жертвуемым Ward. | in_progress | [[05_Combat_Survival/Magic_Batteries]], [[07_Gear_Inventory/Gear_Progression]], [[04_Player_Entities/Lifecycle_Roster]], [[04_Player_Entities/Spawn_Logic]], [[07_Gear_Inventory/Views/Item_Calibration_Matrix]] |
| R47 | No-purgatory создаёт gearless-softlock либо позволяет смертью подкреплять ту же сессию | Пройти gearless, нулевой Ready-ростер, CARE и повторную попытку входа в ту же сессию после потери. | in_progress | [[04_Player_Entities/Lifecycle_Roster]], [[04_Player_Entities/Spawn_Logic]], [[03_Factions_Societies/Lore/The_First_Reception]], [[03_Factions_Societies/Lore/The_Common_Storehouses]], [[08_World_Generation/Generation/Raid_Approach_and_Entry]], [[08_World_Generation/Anomaly/Insertion_Logic]], [[08_World_Generation/Anomaly/Extraction_System]] |
| R48 | Перехваченного Foundling можно отмыть через custody-цепочку в собственность, рынок или гача-ролл происхождения | Проверить враждебный вынос и цепочки передачи Foundling; согласие и происхождение должны оставаться прослеживаемыми. | in_progress | [[04_Player_Entities/Shell_Foundlings]], [[04_Player_Entities/Lifecycle_Roster]], [[06_Economy_Loot/Extraction_Stabilization_Loop]], [[06_Economy_Loot/P2P_Interaction]], [[03_Factions_Societies/Quest_Engine_Grammar]] |
| R57 | Редкий выход превращается в лотерею либо в один вечный лагерь | Проверить поиск выхода поздним solo-входом и группами, знающими карту; измерить устойчивость постоянного лагеря. | in_progress | [[08_World_Generation/Anomaly/Extraction_System]], [[08_World_Generation/Generation/Server_Lifecycle]], sector manifests |
| R58 | Перехват у выхода бесплатно присваивает ценность без риска | Воспроизвести прерванный Sync, убийство носителя и гонку за грузом; сопоставить наблюдаемую вместимость с custody. | in_progress | [[08_World_Generation/Anomaly/Extraction_System]], [[06_Economy_Loot/Extraction_Stabilization_Loop]] |
| R59 | «Hitbox Porn» даёт ложную геометрию либо стойку неуязвимости | Проверить движущиеся, приседающие и разворачивающиеся тела с Projectile/Sweep; проигравший объясняет пластину, шов и доступный контрход. | in_progress | [[05_Combat_Survival/Ballistics_Armor]], [[07_Gear_Inventory/Thermos_System]], [[07_Gear_Inventory/Item_Attributes_UI]] |
| R61 | Последний прирост локального harm, границы поля или удержания превращает один боевой terminal в доминирующий | Измерить marginal leverage каждого terminal в дуэли, маршруте и группе: TTK, батарея, контакт, число целей, Exposure и извлечение. | in_progress | [[04_Player_Entities/Skill_Build_Philosophy]], [[04_Player_Entities/Combat_Profile_Pipeline]], [[04_Player_Entities/Registries/Registry_Skill_Types]], prototype combat slice |
| R62 | Breakline становится кнопкой loot denial: wreck прячут в геометрии, уничтожают своим squad или возвращают через посредника в будущей сессии | Атаковать доступность wreck и ForfeitBeneficiarySet через геометрию, squad, посредников и последующие сессии. | in_progress | [[06_Economy_Loot/Extraction_Stabilization_Loop]], [[06_Economy_Loot/P2P_Interaction]] |
| R63 | Поздняя/Recovery-вставка расходует единственное участие в spawn-camp либо при отсутствии валидной точки | Воспроизвести hard-veto, отсутствие точки, ABORT и сбой на границе Breach; сверить единственность участия и тела. | in_progress | [[08_World_Generation/Anomaly/Insertion_Logic]], [[08_World_Generation/Generation/Raid_Approach_and_Entry]], [[04_Player_Entities/Recovery_Lifecycle]], [[04_Player_Entities/Lifecycle_Roster]] |
| R64 | Именованный модуль превращается в обязательную редкую часть полевого профиля либо один Best-in-Slot закрывает все доктрины | Сравнить минимум две доктрины полного профиля и пройти account-loop модуля до допуска installable. | in_progress | [[07_Gear_Inventory/Thermos_System]], [[07_Gear_Inventory/Registries/Registry_Thermos_Modules]], [[04_Player_Entities/MVP_3x3_Design_Contract]] |
| R65 | Квесты становятся параллельным списком chores, daily-FOMO или абстрактным `убей/принеси N`, не связанным с extraction loop | Наблюдать изменение обычных решений вылазки с контрактом и валидный raid без контракта; проверить давление chores и FOMO. | in_progress | [[03_Factions_Societies/Quest_Engine]], [[03_Factions_Societies/Quest_Engine_Grammar]], [[08_World_Generation/Hub/Hub_Services_Interaction]] |
| R68 | Личный обычный лут, `ERRAND` или Facility-owned Quest незаметно вернутся через UI либо потребителя | Провести обычный ItemID через общий Stash и материальную сделку рядом с Hub-only Quest; проверить независимость readiness. | in_progress | [[06_Economy_Loot/Return_Manifest_Contract]], [[07_Gear_Inventory/Inventory_Architecture]], [[04_Player_Entities/Lifecycle_Roster]], [[03_Factions_Societies/Quest_Engine]], [[08_World_Generation/Hub/Hub_Services_Interaction]] |

## Оставить На Потом

| ID | Тема | Почему не сейчас |
|:---|:---|:---|
| R14 | VOIP-смерть и dead-silence | Нужен отдельный дизайн spectator/dead loop, чтобы не сломать хардкорную коммуникацию |
| R17 | AFK/disconnect | Требует сетевого и антиабьюз-дизайна |
| R18 | Guild/Clan система | Не нужна для первого боевого/экономического MVP |
| R19 | Сезонные вайпы / престиж | Макро-прогрессия после стабилизации core loop |
| R20 | Внешний elevator pitch | Отдельный документ для найма/питча после фиксации лупа |
| R22 | Хаб как remote-presence может быть спутан с физическим PvP-пространством | Нужно уточнить модель безопасного Хаба и взаимодействия аватаров до полноценной social layer |
| R49 | Премиальная валюта и торговая площадка | Отложены до определения реального косметического каталога, визуальной читаемости, anti-RMT и границы pay-to-win |
