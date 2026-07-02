---
type: mechanic
status: active
system: world_systems
tags:
  - dissonance
  - anomaly
  - magic
  - tags
related_files:
  - "[[07_Gear_Inventory/Dissonance_Value|Dissonance_Value]]"
  - "[[04_Player_Entities/_Registries/Registry_Tags|Registry_Tags]]"
  - "[[05_Combat_Survival/Threat_Thresholds|Threat_Thresholds]]"
  - "[[08_World_Generation/Generation/19_Access_Contracts|Access_Contracts]]"
---
# Механика: Диссонанс (Dissonance)

## 1. Концепция

**Диссонанс** - реакция Аномалии на чужеродную материю и активные эфирные действия.

Термин заменяет прежнее название боевого эфирного шума, чтобы не конфликтовать с валютой **Rez**. Рез - стабилизированный материал экономики. Диссонанс - риск быть замеченным или отторгнутым Аномалией.

Он делится на два слоя:

- **DissonanceLoad:** постоянный фон тела, экипировки и переносимых предметов.
- **DissonancePulse:** временный всплеск от выстрела, способности, Reality Burn или другого эфирного действия.

```text
AnomalyPressure = DissonanceLoad + RecentDissonancePulse
```

`DissonanceLoad` проверяется перед входом и задает базовую заметность. `RecentDissonancePulse` существует только внутри рейда, затухает со временем и отвечает за вспышки внимания.

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

Профессия, страх, привычка или обычная травма не получают автоматическую цену Диссонанса. Их сила учитывается через `power_weight`, слот, несовместимость и игровые ограничения.

Числа `dissonance_load` в реестрах являются предварительными до общей калибровки с предметами.

## 3. DissonancePulse

Временный всплеск создают:

- магострельный импульс;
- Q/E и катализаторы;
- перегрев или backlash;
- Reality Burn;
- активация эфирного устройства;
- отдельные погодные и статусные реакции.

Оружие хранит поле `[dissonance_pulse:: N]`.

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

## 4. Командная Угроза

Для группы:

```text
GroupLoad = Max(MemberDissonanceLoad) + sum(OtherMemberDissonanceLoad * 0.2)
GroupPulse = sum(MemberRecentDissonancePulse)
GroupPressure = GroupLoad + GroupPulse
```

- Самый громкий постоянный билд задает базовый класс внимания.
- Остальные участники повышают плотность угрозы.
- Одновременный залп группы создает резкий Pulse независимо от стоимости их экипировки.

Точные коэффициенты подлежат калибровке.

## 5. Границы Термина

Не использовать Диссонанс как:

- валюту или синоним Rez;
- общий бюджет силы трейта;
- награду за негативный flaw;
- шкалу рассудка;
- физический шум шагов;
- gear score для матчмейкинга.

Это отдельная верхняя граница риска, связанная с [[08_World_Generation/Generation/19_Access_Contracts|Access Contracts]], но не заменяющая Gate Check, цену входа или размер группы.
