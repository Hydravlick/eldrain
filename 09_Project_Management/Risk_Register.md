---
type: project_management
status: active
system: project_management
tags: [risk_register, decisions, mvp]
related_files:
  - "[[_Archive/_MERGED_SOURCES#Weak Sides Digest|Weak Sides Digest]]"
  - "[[08_World_Generation/Generation/08_Gate_Check]]"
  - "[[06_Economy_Loot/Currency_Rez]]"
  - "[[04_Player_Entities/_Registries/Registry_Combos]]"
---
# Risk Register: MVP Decisions

## Решения MVP

| ID | Риск | Решение | Статус | Владелец |
|:---|:---|:---|:---|:---|
| R01 | Gate Check и Диссонанс регулируются отдельно | Ввести `Access Readiness`: Environment Seal, Dissonance Budget, Access Price и Population Seat | fixed | `Gate_Check`, `Dissonance_System`, `Access_Contracts`, `Hub_Map_Table` |
| R02 | Смерть носильщика найденыша не определена | Найденыш становится `BackSlotObject` с `Rescue Timer`; чужой вынос дает `Unstabilized Captive` | fixed | `Shell_Foundlings`, `Physical_Weight`, `Lifecycle_Roster` |
| R03 | Рез одновременно валюта, стабилизация и урон | Сырой Рез не тратится из кошелька в бою; Reality Burn идет через `Reality Charge`, `Overcharge Cell` или стабилизатор | fixed | `Currency_Rez`, `Magic_Batteries`, `Registry_Consumables` |
| R04 | Игрок может зайти за 5 минут до Phase Shift и умереть без понимания | `Late Entry Protocol`: предупреждение до Deploy, прогноз `OK/Risk/Fail` | fixed | `Gate_Check`, `Hub_Map_Table`, `UI_Map_Protocol` |
| R05 | Репутация может отрезать критичные сервисы | Нейтральный survival-stock всегда доступен; фракции дают лучшие/дешевые/редкие версии | fixed | `Vendor_Logic`, `Reputation_Rules`, `Registry_Factions` |
| R06 | Страховка убивает пермадет | Страховка ограничена слотами, задержкой, отсутствием текущего лута и найденышей | fixed | `Sinks_Insurance`, `Registry_Factions` |
| R07 | 9 комбо из 25 выглядят как неполнота | Состав зафиксирован: Ёж/Крыса/Белка × Авангард/Технократ/Странник. Реестр содержит все 9 проектных слотов; Жаба, Ящерица, Страж и Догмат остаются видимой картой расширения. Риск остаётся открытым до проектирования и проверки всех ячеек по общему контракту | in_progress | `MVP_3x3_Design_Contract`, `Registry_Combos`, `Combat_Profile_Pipeline`, `00_Balance` |
| R08 | Ballistics/Shadow выглядят как "висящие" векторы | Классовые векторы валидны; источник вектора может быть race/spec/tag/weapon gate | fixed | `Two_Paradox_Vector_Matrix` |
| R09 | Dual State POI не покрывает T1/T2/T3 | Добавлен Tier Layer внутри `Anomaly` | fixed | `Dual_State_POIs`, `Registry_POIs`, `UI_Map_Protocol` |
| R10 | Кукловод и пермадет конфликтуют лорно | Все Пешки — смертные жители. Осколок объясняет непрерывность игрока, но сохраняет только совместно прожитый опыт, а не личность погибшего. «Кукловод/Бригадир» остается рабочей UX-ролью | fixed | `The_Entity`, `Entity_Grimoire`, `Lifecycle_Roster`, `Hub_Environment`, `Glossary` |
| R11 | Благословения Собора могут ошибочно доказать существование доброго бога или единого Наблюдателя | Баффы = ритуалы концентрации, реликтовые якоря и психотехника. Общий механизм установлен, но природа богов остаётся недоказанной | fixed | `The_Cathedral`, `Registry_Factions` |
| R12 | Хранители слишком похожи на силовую монополию | Хранители контролируют экзистенциальные угрозы и лучшие аварийные решения, но не базовый рынок | fixed | `The_Keepers`, `Registry_Factions` |
| R13 | HUD перегружен 13+ параметрами | Ввести слои `VISIBLE`, `DIEGETIC`, `LATENT` | fixed | `UI_Map_Protocol`, `Item_Attributes_UI` |
| R15 | P2P-дроп обходит аукцион и налог | `Field Transfer` дает `Unstabilized Transfer`; нужен отмыв/стабилизация перед легальным рынком | fixed | `P2P_Interaction`, `Auction_House` |
| R16 | 6-часовой цикл может быть несправедливым по таймзонам или оставлять T3 пустым | Rolling pool из T1/T2/T3 локаций со сдвигом, прямые T2/T3 Access Contracts, drop-in/drop-out и опциональный 4-й слот | fixed | `Server_Lifecycle`, `Async_Timers`, `Difficulty_Slots`, `Access_Contracts` |
| R21 | Два глоссария расходятся в терминах | Канон терминов держать в `Glossary`; numbered-версию слить или архивировать | fixed | `Glossary`, `Architecture_MVP` |
| R23 | Биография и теги могут превратиться в скрытый рецепт или полный рандом | Использовать общий каталог категории, событийную группу кандидатов, биографические веса и `exclusive_with`; игрок выбирает испытание, но не точный результат | fixed | `Trait_Development`, `Tags_System`, `Registry_Tags` |
| R24 | Диссонанс может снова стать ценой билда, шумом оружия и бюджетом трейта одновременно | Разделить постоянный `DissonanceLoad`, временный `DissonancePulse`, экономическую цену `value_rez` и внутренний `power_weight`; не использовать Диссонанс как gear score | fixed | `Dissonance_System`, `Registry_Tags`, `Threat_Thresholds`, `Access_Contracts` |
| R25 | Sanity существует фрагментарно без полноценного цикла | Убрать постоянную шкалу Sanity из MVP; оставить ситуационный статус Stress, конкретные источники, спад и лечение | fixed | `Registry_StatusEffects`, `The_Cathedral`, `Magic_Batteries` |
| R26 | ET, Tier, Rarity и Quality создают дублирующие вертикальные шкалы | Удалить общий ET и отдельный Quality; Tier оружия задает допустимую нагрузку, Rarity - аффиксы, батарея - силу импульса, броня - среду и зоны защиты | fixed | `Gear_Progression`, `Weapon_Core`, `Magic_Batteries`, `Item_Attributes_UI` |
| R27 | Сильная броня плюс дешевое летальное оружие становится вечным оптимумом | Разрешить Armor Rat как PvP-нишу, но глубокую награду привязать к повторяемому рабочему циклу, расходу и покрытию задач; проверять полные комплекты по стоимости замены | in_progress | `Gear_Progression`, `Item_Calibration_Matrix`, `TODO` |
| R28 | Один дорогой Frame позволяет всей бюджетной группе обойти оружейную прогрессию | Производящий T2/T3-награду контент должен требовать параллельных задач, длительного давления или нескольких дорогих циклов | in_progress | `Gear_Progression`, `Magic_Batteries`, encounter registries |
| R29 | Пустой Casting Reserve случайно превращает привычное Q/E в самоповреждение | Полная версия использует обычное нажатие; кантрип требует отдельный модификатор и предпросмотр цены. Автоматического расхода HP нет | fixed | `Magic_Batteries`, `Ability_Synergy`, `UI_Map_Protocol` |
| R30 | Игрок бесплатно перекладывает одну батарею между оружием и Q/E | Явная маршрутизация немедленно создаёт Drained Cell и передаёт все импульсы только в Weapon либо Casting Reserve; перенос и смешивание непустого резерва запрещены | fixed | `Magic_Batteries`, `Weapon_Ranged`, `Ability_Synergy`, `Gear_Progression` |
| R31 | Аффиксы повторяют Dark and Darker как набор универсальных положительных чисел | Обычные Affix настраивают исходный цикл по семействам; Defect, Legendary и Corruption разделены; специализацию узко меняет только Legendary/Artifact | fixed | `Affix_Grammar`, `Craft_Modifiers`, `Gear_Progression` |
| R32 | Один сильный трейт полностью определяет билд и обесценивает комбинации | Обычный стиль выводится из суммы proficiency, substats, условий, экипировки и подготовки; отдельное новое правило дают только мутации, Fusion и пороги | fixed | `Tags_System`, `Combat_Profile_Pipeline`, `Registry_Tags` |
| R33 | Происхождение батарей, Аномалий, Сущности, Осколков и Двери описано разными несовместимыми причинами | Зафиксирован Ковчег Предтеч: батареи являются маяками и записью с побочной энергией; Сущность наследует утраченную волю притяжения и пересобирает слепки; Осколки возникают из попыток понять смертных изнутри; Дверь остаётся пассивным приёмным узлом | fixed | `The_Ark`, `The_Collapse`, `The_Entity`, `Energy_Concept`, `Server_Lifecycle`, `Registry_POIs` |
| R34 | Многозонный легаси-пакет может закрыть несколько частей тела ценой одного неизвестного слота | Все неатомизированные пакеты получают `install_state:: blocked_calibration`, не показываются мастером и не входят в расчёт сборки. Допуск возвращается только после назначения физической позиции, `slot_size` и раздельного `module_cost` | in_progress | `Thermos_System`, `Registry_Thermos_Modules`, `Item_Calibration_Matrix`, `TODO` |
| R35 | Capacitor Cell даёт оружию несколько действий, но исчезает после одного Q/E | Оружие и способности расходуют `impulse_cost` из раздельных резервов; батарея передаёт все `Battery.ChargeCount` выбранному контуру | fixed | `Magic_Batteries`, `Weapon_Ranged`, `Ability_Synergy` |
| R36 | Смена оружия, блок или Q/E удаляют Recovery предыдущего действия | `Action Recovery` принадлежит действию и переживает смену канала; полная готовность возвращается только через общий state machine | fixed | `Combat_Three_Debts`, `Movement_Physics`, `Weapon_Core` |
| R37 | Tether, реакция среды и Stun складываются в бесконечную потерю управления | Все hard control используют общую `control_family` и `repeat_rule:: diminishing`; повтор сокращается до interrupt без полной потери управления | fixed | `Status_Effects`, `Registry_StatusEffects`, `MVP_3x3_Design_Contract` |
| R38 | Отсутствие боевого акустического следа делает тихий мили-сквад универсальным оптимумом | Мили создаёт низкие повторяющиеся AcousticEvent; серия ударов, блоков и разрушений уточняет область контакта, оставаясь тише магострельного пика | fixed | `Acoustic_Stealth`, `Weapon_Melee`, `Combat_Three_Debts` |
| R39 | Кастер готовит полный эффект за стеной и показывает себя только в момент результата | Сильный каст обязан иметь exposure-фазу через линию, уязвимый проводник или читаемый телеграф; удержание копит Heat/Strain | fixed | `Combat_Three_Debts`, `Ability_Synergy`, `Status_Effects` |
| R40 | Доступная Пешка становится оптимальным штатным смертником для прибыли группы | Кантрип слабее и локальнее батарейной версии, не усиливается от низкого HP, не производит передаваемую ценность и прекращает незакреплённый эффект при смерти | in_progress | `Magic_Batteries`, `Gear_Progression`, `Lifecycle_Roster`, `Shell_Projections`, `Item_Calibration_Matrix` |

## Оставить На Потом

| ID | Тема | Почему не сейчас |
|:---|:---|:---|
| R14 | VOIP-смерть и dead-silence | Нужен отдельный дизайн spectator/dead loop, чтобы не сломать хардкорную коммуникацию |
| R17 | AFK/disconnect | Требует сетевого и антиабьюз-дизайна |
| R18 | Guild/Clan система | Не нужна для первого боевого/экономического MVP |
| R19 | Сезонные вайпы / престиж | Макро-прогрессия после стабилизации core loop |
| R20 | Внешний elevator pitch | Отдельный документ для найма/питча после фиксации лупа |
| R22 | Хаб как remote-presence может быть спутан с физическим PvP-пространством | Нужно уточнить модель безопасного Хаба и взаимодействия аватаров до полноценной social layer |
