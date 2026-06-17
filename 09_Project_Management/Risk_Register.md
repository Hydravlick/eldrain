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
| R01 | Gate Check и Resonance регулируются отдельно | Ввести `Readiness Corridor`: нижняя граница `SurvivalScore`, верхняя `ResonanceLoad` | fixed | `Gate_Check`, `Threat_Thresholds`, `Hub_Map_Table` |
| R02 | Смерть носильщика найденыша не определена | Найденыш становится `BackSlotObject` с `Rescue Timer`; чужой вынос дает `Unstabilized Captive` | fixed | `Shell_Foundlings`, `Physical_Weight`, `Lifecycle_Roster` |
| R03 | Рез одновременно валюта, стабилизация и урон | Сырой Рез не тратится из кошелька в бою; Reality Burn идет через `Reality Charge`, `Overcharge Cell` или стабилизатор | fixed | `Currency_Rez`, `Magic_Batteries`, `Registry_Consumables` |
| R04 | Игрок может зайти за 5 минут до Phase Shift и умереть без понимания | `Late Entry Protocol`: предупреждение до Deploy, прогноз `OK/Risk/Fail` | fixed | `Gate_Check`, `Hub_Map_Table`, `UI_Map_Protocol` |
| R05 | Репутация может отрезать критичные сервисы | Нейтральный survival-stock всегда доступен; фракции дают лучшие/дешевые/редкие версии | fixed | `Vendor_Logic`, `Reputation_Rules`, `Registry_Factions` |
| R06 | Страховка убивает пермадет | Страховка ограничена слотами, задержкой, отсутствием текущего лута и найденышей | fixed | `Sinks_Insurance`, `Registry_Factions` |
| R07 | 9 комбо из 25 выглядят как неполнота | 9 curated-комбо считаются MVP scope; остальные пары не утверждены | fixed | `Registry_Combos`, `Combat_Profile_Pipeline`, `00_Balance` |
| R08 | Ballistics/Shadow выглядят как "висящие" векторы | Классовые векторы валидны; источник вектора может быть race/spec/tag/weapon gate | fixed | `Two_Paradox_Vector_Matrix` |
| R09 | Dual State POI не покрывает T1/T2/T3 | Добавлен Tier Layer внутри `Anomaly` | fixed | `Dual_State_POIs`, `Registry_POIs`, `UI_Map_Protocol` |
| R10 | Кукловод и пермадет конфликтуют лорно | Кукловод = стабильный оператор/Осколок, Оболочки погибают как ростерные биографии; правда раскрывается постепенно | fixed | `Hub_Environment`, `Glossary` |
| R11 | Благословения Собора конфликтуют с безразличным Наблюдателем | Баффы = ритуалы концентрации, реликтовые якоря и психотехника, а не доброта бога | fixed | `The_Cathedral`, `Registry_Factions` |
| R12 | Хранители слишком похожи на силовую монополию | Хранители контролируют экзистенциальные угрозы и лучшие аварийные решения, но не базовый рынок | fixed | `The_Keepers`, `Registry_Factions` |
| R13 | HUD перегружен 13+ параметрами | Ввести слои `VISIBLE`, `DIEGETIC`, `LATENT` | fixed | `UI_Map_Protocol`, `Item_Attributes_UI` |
| R15 | P2P-дроп обходит аукцион и налог | `Field Transfer` дает `Unstabilized Transfer`; нужен отмыв/стабилизация перед легальным рынком | fixed | `P2P_Interaction`, `Auction_House` |
| R16 | 6-часовой цикл может быть несправедливым по таймзонам | Rolling pool из T1/T2/T3 локаций со сдвигом, опциональный 4-й слот | fixed | `Server_Lifecycle`, `Async_Timers`, `Difficulty_Slots` |
| R21 | Два глоссария расходятся в терминах | Канон терминов держать в `Glossary`; numbered-версию слить или архивировать | fixed | `Glossary`, `Architecture_MVP` |

## Оставить На Потом

| ID | Тема | Почему не сейчас |
|:---|:---|:---|
| R14 | VOIP-смерть и dead-silence | Нужен отдельный дизайн spectator/dead loop, чтобы не сломать хардкорную коммуникацию |
| R17 | AFK/disconnect | Требует сетевого и антиабьюз-дизайна |
| R18 | Guild/Clan система | Не нужна для первого боевого/экономического MVP |
| R19 | Сезонные вайпы / престиж | Макро-прогрессия после стабилизации core loop |
| R20 | Внешний elevator pitch | Отдельный документ для найма/питча после фиксации лупа |
| R22 | Хаб как remote-presence может быть спутан с физическим PvP-пространством | Нужно уточнить модель безопасного Хаба и взаимодействия аватаров до полноценной social layer |
