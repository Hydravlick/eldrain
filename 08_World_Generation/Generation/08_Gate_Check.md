---
type: mechanic
status: active
index_route: owner
index_group: world_generation
index_order: 200
index_summary: "Задаёт правила и последствия системы «Гейт-проверка»."
read_when: "Читайте при изменении входов, состояний, стоимости или последствий системы «Гейт-проверка»."
system: phase_pulse_survival
tags:
  - damage_event
  - environment
  - phase_shift
  - survival
related_files:
  - "[[08_World_Generation/Generation/07_Server_Lifecycle|Server Lifecycle]]"
  - "[[05_Combat_Survival/Threat_Thresholds|Threat Thresholds]]"
  - "[[05_Combat_Survival/Masks_Filters|Masks and Filters]]"
  - "[[07_Gear_Inventory/Item_Calibration_Matrix|Item Calibration Matrix]]"
  - "[[07_Gear_Inventory/Thermos_System|Thermos System]]"
---
# Гейт-проверка

> Gate Check — исключительно физический результат фазового импульса для уже присутствующего тела. Это не допуск, матчмейкинг, цена входа или право на место.

## Responsibility

`PHASE_PULSE_RESOLVER` получает server-authored pulse fact и текущий физический snapshot `Presence`, рассчитывает поглощение и фиксирует один локальный результат:

- `ABSORBED`;
- `OVERFLOW_INJURY`;
- `LETHAL_OVERFLOW`.

Resolver не выбирает сектор, не блокирует вход заранее, не проверяет экономику или население, не перемещает тело и не создаёт безопасную фазу.

## Protection model

```text
ThermosModuleProtection =
  sum(working_installed_module.environment_resistance)

ProtectionScore =
  ThermosModuleProtection
  + Headwear.Filter_Rating
  + Battery.Buffer
  + Stabilizer_Bonus
  + Shell.Reality_Buffer
  - Open_Wounds_Penalty
  - Overload_Penalty

PulseOverflow = EntropyPulseDamage - ProtectionScore
```

В расчёт входят только физически установленные и работающие компоненты. `UNKNOWN`, `blocked_calibration`, отключённый или уничтоженный модуль даёт только подтверждённый фактический вклад.

`Frame Class`, цена оружия, Chronicle, происхождение, civic status и источник loadout не участвуют. Тело не заменяет обязательный средовой контур: Reality Buffer лишь ограниченно поглощает остаток.

## Outcomes

| Условие | Результат |
|---|---|
| `PulseOverflow <= 0` | импульс поглощён; возможен объявленный расход ресурса защиты |
| `0 < PulseOverflow < Current_HP` | немедленный урон и связанные физические последствия |
| `PulseOverflow >= Current_HP` или отсутствует обязательный контур | lethal outcome по владельцу жизненного цикла |

Числовые коридоры принадлежат balance-калибровке и считаются неподтверждёнными, пока Item Calibration Matrix не содержит репрезентативные T1/T2/T3 комплекты.

## World continuity

Фазовый переход меняет мир вокруг существующего тела. `PresenceID`, координаты и player control сохраняются. Среда может разрушиться или открыть новые маршруты по собственным правилам topology mutation, но сам Gate Check:

- не телепортирует игрока;
- не ищет укрытие;
- не гасит экран как обязательное правило;
- не блокирует управление;
- не выдаёт неуязвимость;
- не лечит и не компенсирует опасную позицию.

Если новая геометрия несовместима с occupied space, это обязанность topology owner обеспечить непрерывную допустимую трансформацию; Gate Check не является fallback relocation.

## Warning and feedback

Предвестник импульса появляется заранее и проецирует только средовую готовность: `OK`, `RISK` или `FAIL` против ожидаемого pulse envelope. Это прогноз, а не admission veto.

В момент события причина читается через физические каналы: фильтр, маска, батарея, стабилизатор, ранения и overload показывают поглощённую и прошедшую часть удара. Игрок должен отличать недостаток защиты от обычного входного решения, Dissonance и сетевой ошибки.

## Non-ownership

- время и порядок фаз: [[08_World_Generation/Generation/07_Server_Lifecycle|Server Lifecycle]];
- конкретные предметные параметры: [[07_Gear_Inventory/Item_Calibration_Matrix|Item Calibration Matrix]];
- средовые модули: [[07_Gear_Inventory/Thermos_System|Thermos System]];
- Dissonance и raid approach являются отдельными системами и не вычисляются здесь.
