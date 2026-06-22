---
type: mechanic
status: active
system: world_systems
tags:
  - resonance
  - anomaly
  - magic
  - tags
related_files:
  - "[[07_Gear_Inventory/Resonance_Value|Resonance_Value]]"
  - "[[04_Player_Entities/_Registries/Registry_Tags|Registry_Tags]]"
  - "[[05_Combat_Survival/Threat_Thresholds|Threat_Thresholds]]"
---
# Механика: Резонанс (Эфирный Шум)

## 1. Концепция

Резонанс — реакция Аномалии на чужеродную материю и активные эфирные импульсы.

Он делится на два слоя:

- **ResonanceLoad:** постоянный фон тела, экипировки и переносимых предметов.
- **ResonancePulse:** временный всплеск от выстрела, способности, Reality Burn или другого действия.

```text
CurrentThreat = ResonanceLoad + RecentPulse
```

`ResonanceLoad` определяет готовность входа и базовую заметность. `RecentPulse` влияет только внутри рейда и затухает со временем.

## 2. ResonanceLoad

```text
ResonanceLoad =
  sum(Item.CurrentResonance)
  + sum(BodyTag.ResonanceLoad)
  + persistent_effects
```

### Предметы

`Item.CurrentResonance` рассчитывается через [[07_Gear_Inventory/Resonance_Value|Resonance Value]]:

```text
Item.CurrentResonance = Item.BaseResonance * SyncMultiplier
```

Foreign-предметы создают полный фон, Native-лут синхронизирован с текущей Аномалией и фонит слабее.

### Тело и теги

Тег меняет `ResonanceLoad` только при физическом или эфирном объяснении:

- имплант;
- активная мутация;
- проводящий контур;
- громкая аура;
- адаптация, маскирующая тело от Аномалии.

Профессия, страх, привычка или обычная травма не получают автоматическую цену Резонанса. Их сила учитывается через `power_weight`, слот, несовместимость и игровые ограничения.

Числа `resonance_load` в реестрах являются предварительными до общей калибровки с предметами.

## 3. ResonancePulse

Временный всплеск создают:

- магострельный импульс;
- Q/E и катализаторы;
- перегрев или backlash;
- Reality Burn;
- активация эфирного устройства;
- отдельные погодные и статусные реакции.

Оружие хранит поле `[resonance_pulse:: N]`.

```text
RecentPulse =
  sum(active_pulses * decay)
```

Pulse:

- не используется как постоянная стоимость билда;
- не блокирует вход до совершения действия;
- может временно перевести игрока из Green в Yellow/Red;
- сообщает Охотникам направление или район, но не обязательно точные координаты;
- постепенно затухает, если игрок перестает фонить.

## 4. Командная Угроза

Для группы:

```text
GroupLoad = Max(MemberLoad) + sum(OtherMemberLoad * 0.2)
GroupPulse = sum(MemberRecentPulse)
GroupThreat = GroupLoad + GroupPulse
```

- Самый громкий постоянный билд задает базовый класс внимания.
- Остальные участники повышают плотность угрозы.
- Одновременный залп группы создает резкий Pulse независимо от стоимости их экипировки.

Точные коэффициенты подлежат калибровке.

## 5. Границы Термина

Не использовать Резонанс как:

- общий бюджет силы трейта;
- награду за негативный flaw;
- шкалу рассудка;
- физический шум шагов;
- синоним валюты Рез.

Это отдельные системы с собственными причинами и обратной связью.
