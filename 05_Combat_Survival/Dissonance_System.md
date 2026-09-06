---
status: active
system: world_systems
tags:
  - dissonance
  - anomaly
  - magic
  - tags
related_files:
  - "[[05_Combat_Survival/Combat_Three_Debts|Combat_Three_Debts]]"
  - "[[05_Combat_Survival/Hunt_Frontier_Loop|Hunt_Frontier_Loop]]"
  - "[[05_Combat_Survival/Acoustic_Stealth|Acoustic_Stealth]]"
  - "[[07_Gear_Inventory/Dissonance_Value|Dissonance_Value]]"
  - "[[04_Player_Entities/Registries/Registry_Tags|Registry_Tags]]"
  - "[[05_Combat_Survival/Threat_Thresholds|Threat_Thresholds]]"
  - "[[08_World_Generation/Generation/Raid_Approach_and_Entry|Raid_Approach_and_Entry]]"
  - "[[04_Player_Entities/Registries/Registry_Parameter_Contracts|Реестр параметрических контрактов]]"
type: system
index_route: owner
index_group: combat_survival
index_order: 90
index_summary: "Определяет состояния, разрешение и связи: Механика: Диссонанс (Dissonance)."
read_when: "Когда нужен контракт «Механика: Диссонанс (Dissonance)» и его границы с соседними владельцами."
---
# Механика: Диссонанс (Dissonance)

## 1. Концепция

**Диссонанс** - реакция Аномалии на чужеродную материю и активные эфирные действия.

Он не является физическим звуком. Выстрел или каст может одновременно создать [[05_Combat_Survival/Acoustic_Stealth|AcousticEvent]] для ушей и `DissonancePulse` для Аномалии; эти сигналы не складываются в один универсальный шумомер.

**Rez** — стабилизированный материал экономики. Диссонанс — риск быть замеченным или отторгнутым Аномалией из-за боевого эфирного шума.

Он делится на два слоя:

- **DissonanceLoad:** постоянный фон тела, экипировки и переносимых предметов.
- **DissonancePulse:** временный всплеск от выстрела, способности, Reality Burn или другого эфирного действия.

```text
AnomalyPressure = DissonanceLoad + RecentDissonancePulse
```

`DissonanceLoad` проверяется перед входом и задает базовую заметность. `RecentDissonancePulse` существует только внутри рейда, затухает со временем и отвечает за вспышки внимания.

Диссонанс не является анти-кемперским таймером и не регистрирует простое ожидание. Он отвечает только на принесённую чужеродность, состояние тела и описанные эфирные действия. В охоте это эфирный след: он меняет реакцию Аномалии, но не заменяет звук, зрение или право игрока прочитать физическое место.

## 2. DissonanceLoad

```text
DissonanceLoad =
  sum(Item.current_dissonance)
  + sum(BodyTag.dissonance_load)
  + persistent_effects
```

### Предметы

`Item.current_dissonance` рассчитывается через [[07_Gear_Inventory/Dissonance_Value|Dissonance Value]]:

```text
Item.current_dissonance = Item.base_dissonance * sync_multiplier
```

Foreign-предметы создают полный фон. Native-лут синхронизирован с текущей Аномалией и фонит слабее.

### Тело и теги

Тег меняет `DissonanceLoad` только при физическом или эфирном объяснении:

- имплант;
- активная мутация;
- проводящий контур;
- громкая аура;
- адаптация, маскирующая тело от Аномалии.

Профессия, страх, привычка или обычная травма не получают автоматическую цену Диссонанса. Если конкретное свойство имеет механический эффект, его цена остаётся локальной: named slot, физическая несовместимость, конкретный debt или owner-bound effect. Общего `power_weight` не существует.

Числа `dissonance_load` в реестрах являются предварительными до общей калибровки с предметами.

## 3. DissonancePulse

Временный всплеск создают:

- магострельный импульс;
- Q/E и катализаторы;
- перегрев или backlash;
- Reality Burn;
- активация эфирного устройства;
- отдельные погодные и статусные реакции.

Каждый **physical occurrence** создаёт один `DissonanceEvent`; он может добавить не более одного Pulse-вклада. Действие, Backlash или среда публикуют request с физическим источником, а этот resolver принимает его по [[04_Player_Entities/Registries/Registry_Parameter_Contracts#`dissonance_occurrence`|контракту Dissonance occurrence]]. Нельзя добавить отдельный Pulse за батарею, модуль и само действие, если это одна физическая вспышка.

Committed [[07_Gear_Inventory/Thermos_Assembly|Thermos Assembly]] передаёт только список установленных persistent-signature sources и contributor rules конкретных ItemID. `DISSONANCE_SYSTEM` единолично разрешает их итоговый постоянный вклад и occurrence events. Ни Module Definition, ни Assembly не складывают локальный `dissonance_load/pulse`, а итог Диссонанса не возвращается в монтажный resolver как право разрешить или запретить сам модуль.

Оружие хранит профиль occurrence, а не независимый второй долг: `[dissonance_pulse:: N]` описывает вклад его NativeAction после разрешения.

```text
RecentDissonancePulse =
  sum(active_pulses * decay)
```

Pulse:

- не используется как постоянная стоимость билда;
- не блокирует вход до совершения действия;
- может временно перевести игрока из `Тишины` в `Звон` или `Охоту`;
- сообщает Охотникам направление или район, но не обязательно точные координаты;
- постепенно затухает, если игрок перестает фонить.

В [[05_Combat_Survival/Combat_Three_Debts|Законе трёх долгов]] Pulse является отложенным слоем долга внимания и напряжения. Немедленная контригра обеспечивается телеграфом, направлением действия и `Action Recovery`; случайная будущая Охота не балансирует сильное действие в одиночку. `AcousticEvent` остаётся отдельным: один физический жест может породить и звук, и DissonanceEvent, но это два разных домена, не два Pulse.

## 4. Командная Угроза

Для группы:

```text
GroupLoad = DOMAIN_POLICY_AGGREGATE(MemberDissonanceLoad[])
GroupPulse = sum(MemberRecentDissonancePulse)
GroupPressure = GroupLoad + GroupPulse
```

- Самый громкий постоянный билд задает базовый класс внимания.
- Остальные участники повышают плотность угрозы по ещё не откалиброванной non-dominant aggregation policy.
- Одновременный залп группы создает резкий Pulse независимо от стоимости их экипировки.

Единицы, вес остальных участников и числовой corridor — `UNKNOWN` до модели и прототипа; активный контракт фиксирует только структуру агрегации.

## 5. Границы Термина

Не использовать Диссонанс как:

- валюту или синоним Rez;
- общий бюджет силы Personal Tag;
- награду за негативный flaw;
- шкалу рассудка;
- физический шум шагов;
- gear score для матчмейкинга.

Это отдельная верхняя граница риска, проецируемая рядом с [[08_World_Generation/Generation/Raid_Approach_and_Entry|Entry Quote]], но не заменяющая Gate Check, цену подхода или правила группы.
