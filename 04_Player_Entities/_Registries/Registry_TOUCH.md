---
type: registry
status: active
system: player_entities_registry
registry_type: touch_body_consumers
tags: [database, touch, body, attributes, player_readability]
related_files:
  - "[[04_Player_Entities/Attributes_TOUCH|Система атрибутов T.O.U.C.H.]]"
  - "[[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile Pipeline]]"
  - "[[05_Combat_Survival/Weapon_Core|Weapon Core]]"
---
# Реестр: T.O.U.C.H. — обещание тела

> Каждое очко T.O.U.C.H. сначала меняет тело Пешки. Навык, Frame или батарея могут назвать дополнительный consumer, но не подменяют это базовое обещание и не получают общий бонус «ко всему».

## 1. Общая форма

Все пять строк используют единую нормализованную кривую из [[04_Player_Entities/Attributes_TOUCH|T.O.U.C.H.]]:

```text
R(N) = 1
R(T) = (1 + r) ^ (T - N)
FinalParameter = OwnerResolve(OwnerBase, R(FinalTOUCH) ^ weight)
```

Точные `N`, `r`, базовые значения и `weight` — `UNKNOWN` до прототипа. На карточке игрок всегда видит итоговое `было → станет`; формула остаётся подробностью.

| ID | Что +1 обещает телу | Игроковая единица | Направление |
|:---|:---|:---|:---|
| `TRQ` | переносимый вес | кг | больше — лучше |
| `GRP` | интервал ручной операции | сек. | меньше — лучше |
| `LYR` | текущий предел HP | HP | больше — лучше |
| `GLW` | безопасный предел перегруза | Heat / порог | больше — лучше |
| `SNS` | время раннего сигнала | мс | больше — лучше |

## 2. Тяга — `TRQ`

```text
[attribute_id:: TRQ]
[core_body_output:: CarryLoad]
[player_unit:: kg]
[resolve_direction:: increase]
[balance_state:: prototype]
```

Тяга определяет, какую массу тело способно нести и удерживать. Frame может отдельно назвать `TRQ` для удержания своей нагрузки или силового предела процедуры, но это не создаёт универсальный физический урон.

**Не даёт:** общий damage, бесплатный пробой брони, право держать недоступный Frame.

## 3. Хват — `GRP`

```text
[attribute_id:: GRP]
[core_body_output:: ManipulationInterval]
[player_unit:: seconds]
[resolve_direction:: decrease]
[balance_state:: prototype]
```

Хват сокращает время осмысленной ручной операции: взять, закрепить, заменить, взвести, вернуть руку. Конкретный Frame или батарея могут объявить свой `GRP`-consumer, например время замены ячейки.

**Не даёт:** aim assist, скрытую точность, автоматическое парирование или темп всех атак.

## 4. Слой — `LYR`

```text
[attribute_id:: LYR]
[core_body_output:: MaxHP]
[player_unit:: HP]
[resolve_direction:: increase]
[balance_state:: prototype]
```

Слой определяет текущий предел HP тела. Названная телесная процедура может дополнительно читать `LYR` для тяжести собственного Backlash, но не превращает здоровье в скрытую броню.

**Не даёт:** общий physical/ether resist, лечение травмы, иммунитет к статусам или защиту всех зон силуэта.

## 5. Накал — `GLW`

```text
[attribute_id:: GLW]
[core_body_output:: OverloadThreshold]
[player_unit:: heat_threshold]
[resolve_direction:: increase]
[balance_state:: prototype]
```

Накал определяет, сколько собственной проводящей нагрузки тело и его интерфейс выдерживают до Overload. Батарея, Frame или терминал могут отдельно читать `GLW` для своего Heat-цикла.

**Не даёт:** магический resist, защиту от любого эфирного воздействия, бесплатную батарейную энергию или снятие Heat без цены.

## 6. Чутьё — `SNS`

```text
[attribute_id:: SNS]
[core_body_output:: CueLead]
[player_unit:: milliseconds]
[resolve_direction:: increase]
[balance_state:: prototype]
```

Чутьё определяет, насколько раньше тело замечает уже существующий предупреждающий признак. Конкретный источник может дополнительно назвать `SNS` для ясности следа, weakspot или собственного информационного терминала.

**Не даёт:** wallhack, чтение чужих формул, магический resist, гарантированное попадание или раскрытие врага сквозь сцену.

## 7. Границы реестра

- броня и сопротивление физическому урону принадлежат зоне, материалу, позе и укрытию;
- защита от среды принадлежит фильтру, герметизации, маршруту и конкретной контригре;
- Frame доступен через arsenal capability и proficiency, а не через числовой порог T.O.U.C.H.;
- P/Q/E может назвать дополнительный consumer, но не переписывает пять строк этого реестра;
- временный бафф не меняет T.O.U.C.H. и не создаёт новый базовый итог тела.
