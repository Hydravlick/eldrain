---
type: mechanic
status: active
system: player_core
tags: [tags, traits, mutation, implants]
related_files:
  - "[[04_Player_Entities/_Registries/Registry_Tags|Registry Tags]]"
  - "[[04_Player_Entities/Trait_Development|Trait Development]]"
  - "[[04_Player_Entities/Attributes_TOUCH|T.O.U.C.H.]]"
  - "[[04_Player_Entities/Skill_Build_Philosophy|Философия навыков]]"
---
# Система тегов: системный слой

## 1. Что такое тег

Тег и трейт — один исполняемый объект биографии Пешки. `tag` используется в данных, `трейт` — в игроковом тексте.

Тег может описывать устойчивое изменение тела, опыт, травму, мутацию, имплант, доступ или уязвимость. Он не является вторым деревом навыков и не хранит скрытый пакет числовых бонусов.

## 2. Допустимые изменения

- `attr_delta` — устойчиво меняет видимый T.O.U.C.H. и проходит общий ExternalShift cap;
- `prof_delta` — меняет владение оружейным семейством;
- `module_capacity_delta` — меняет допустимую сложность Термоса без создания физического слота;
- `arsenal_grant` / `arsenal_block` — явно меняют доступ к Frame;
- `capability` — даёт бинарную физическую возможность;
- `vulnerability` — называет постоянно релевантную цену;
- `add_vector` / `block_vector` — меняют вектор только через мутацию, физическую перестройку или редкую Fusion;
- `dissonance_load` — меняет постоянный фон только при физически или эфирно заметной причине;
- `owned_output_mod` — допустим только для одного конечного видимого результата в форме `owner_id.final_parameter delta`.

Запрещены:

- `substats`, `substat_bonus`, `substat_mult`;
- `condition_bonus` и общий `tradeoff`;
- прямое изменение T.O.U.C.H.-компонента P/Q/E;
- создание новой P/Q/E или нового payload;
- скрытый порог, где сумма рейтингов внезапно создаёт capability;
- двойной путь `attr_delta + бонус производному` одного действия.

## 3. Итоговый билд

```text
Race + Spec + P/Q/E
  + Final TOUCH
  + Arsenal / Proficiency
  + Module Capacity
  + Capabilities / Vulnerabilities
  + Frame, Battery, Armor and Material Payload
  = Combat Profile
```

T.O.U.C.H.-скейлинг навыка принадлежит самой P/Q/E. Явный обмен сборки принадлежит физическому модулю или Frame-доктрине и показывает конечные параметры `до → после`.

## 4. Внешний сдвиг T.O.U.C.H.

```text
PositiveExternalShift(A) = StableTags + ActiveBodyInterface
PositiveExternalShift(A) <= +4
GearContribution(A) <= +2
```

Положительный `attr_delta` требует лорной причины устойчивого изменения тела. Редкость, `power_weight` и несовместимость сами по себе не являются ценой; цена читается через слот развития, vulnerability, блокировку функции, Dissonance либо потерю альтернативного пути.

## 5. Типы тегов

1. **Proficiency:** оружие, устройство, процедура и ёмкость.
2. **Mutation:** физически меняет тело, интерфейс или вектор.
3. **Attribute:** устойчиво меняет один или несколько видимых T.O.U.C.H.
4. **Flaw:** даёт блокировку, vulnerability или отрицательный attr delta.
5. **Fusion:** заменяет две биографические линии одной более выразительной возможностью и новой ценой; не уплотняет скрытые бонусы.

## 6. Иерархия конфликтов

1. физиология и устойчивые теги тела;
2. ядро Combo P/Q/E;
3. материальный carrier/supply contract;
4. Proficiency Gate;
5. текущий Frame, модуль и их Commitment;
6. автоматическая matchup-карта.

Capability не создаёт материальный payload. Например, `vent_fit` разрешает физический проход, но не переносит тело через стену; `eligible_contact_surface` разрешает нанесение состава, но не создаёт дозу.

## 7. Контракт тега

```markdown
[id:: template_tag]
[tag:: template_tag]
[tag_kind:: proficiency | mutation | attribute | flaw | fusion]
[tag_polarity:: positive | mixed | negative]
[add_vector:: tech]
[block_vector:: hazard]
[prof_delta:: arcanegun +1]
[module_capacity_delta:: weave +1, plate -1]
[attr_delta:: TRQ +2, SNS -1]
[owned_output_mod:: body.movement_noise +8]
[capability:: none]
[vulnerability:: none]
[deferred_rule:: none]
[override_race_ban:: heavy_weapon]
[arsenal_grant:: breach_impact_2h @1]
[arsenal_block:: none]
[exclusive_with:: incompatible_tag]
[fusion_with:: other_tag -> result_tag]
[fusion_requires:: source_tag_a, source_tag_b]
[trait_pool:: standard | specialist]
[event_family:: rescue, survival]
[dissonance_load:: 0]
[power_weight:: 0]
```

## 8. Проверки

- один источник не оплачивает T.O.U.C.H. и производный результат отдельно;
- тег не меняет коэффициент P/Q/E;
- capability имеет физический интерфейс и не создаёт предмет;
- vulnerability релевантна тем же рейдам, где полезен тег;
- Fusion не создаёт третий engine или свободный слот бесконечного роста;
- Dissonance используется только как доказательство мира, а не универсальный балансный налог.
