---
type: system
status: active
system: combat_profile
tags: [combat_profile, two_paradox, abilities, arsenal, tags]
related_files:
  - "[[04_Player_Entities/Skill_Build_Philosophy|Философия навыков и билдостроения]]"
  - "[[04_Player_Entities/Ability_Synergy]]"
  - "[[04_Player_Entities/Shell_Construction]]"
  - "[[04_Player_Entities/Proficiency_Arsenal]]"
  - "[[04_Player_Entities/Tags_System]]"
  - "[[04_Player_Entities/Two_Paradox_Vector_Matrix]]"
  - "[[04_Player_Entities/_Registries/Registry_Combos]]"
  - "[[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]]"
---
# Combat Profile Pipeline

> Канон расчета Оболочки: `Race + Spec -> Final TOUCH -> прямые потребители тела/Frame/P/Q/E -> Allowed Arsenal -> Tags -> Proficiency Gates -> Combat Profile, Frame Commitment и допустимая сборка Термоса`.

## 1. Race + Spec

Раса и специализация образуют **архетип**: задают базовую биологию, методологию, атрибуты и два стартовых тактических вектора. Это ещё не фактическая роль и не полный профиль вылазки.

- Раса отвечает за физиологическую основу, физику тела и биологические ограничения.
- Практика / специализация отвечает за методологию давления, подготовки и решения задач.
- Их сумма не является готовой способностью. Готовые способности появляются только после слияния в `Registry_Combos`.
- Фактический **Профиль вылазки** возникает только после учёта P/Q/E, арсенала, Термоса, батарей, тегов, контракта, команды и условий операции.
- На этом шаге считается только видимый `Final TOUCH`. Тело, Frame, батарея и P/Q/E затем независимо рассчитывают свои конечные параметры из названного T.O.U.C.H.; общего слоя скрытых рейтингов нет.

```text
Ordinary Final TOUCH = clamp(10 + Race + Spec + Stable Tags + Active Body Interface, 6, 20)
Final TOUCH = Ordinary Final TOUCH + Explicit Corruption Exception
R(N) = 1
R(T) = (1 + r) ^ (T - N)
Action Parameter = OwnerResolve(OwnerBase, R(Final TOUCH) ^ weight)
```

## 2. Combo P/Q/E

`Registry_Combos` - главный MVP-источник слияния способностей и разрешенного арсенала. Он не хранит Combat Profile напрямую.

Игровой MVP использует зафиксированные расы Ёж, Крыса, Белка и практики Авангард, Технократ, Странник. `Registry_Combos` содержит ровно девять проектных слотов этой матрицы. Полная сетка 5x5 сохраняется как внутренняя карта расширения.

Наличие слота не означает готовый контент. Ячейка считается канонически спроектированной только после тройной проверки из [[04_Player_Entities/MVP_3x3_Design_Contract|контракта 3×3]].

Каждый combo обязан содержать:

```markdown
[req_race:: rat]
[req_spec:: scout]
[weapon_frame:: short_cut_1h] | [prof:: 2] | [combat_role:: route_finish]
[weapon_frame:: pulse_tool_1h] | [prof:: 1] | [combat_role:: panic_stop]
```

- **P/Q/E** — смешанные способности конкретной пары `Race × Spec`.
- **Q/E** — самостоятельные ситуативные действия, а не обязательная ротация.
- **Combat Profile** вычисляется матрицами: `primary = Race.base_vector`, `secondary = Spec.base_vector`, `shared_weakness = Race.weak_to ∩ Spec.weak_to`.
- **Ability Model** выводится автоматически: одинаковые векторы дают `mono_vector_fusion`, разные - `race_spec_fusion`.
- **Ability Component Model** читается из P/Q/E: прямые T.O.U.C.H.-компоненты, фиксированный долг, downstream и общий envelope. Combo не хранит второй пакет числовых бонусов поверх Race/Spec.

## 3. Allowed Arsenal

Для MVP итоговый арсенал берется из combo-блока:

```markdown
[weapon_frame:: short_cut_1h] | [prof:: 2] | [combat_role:: route_finish]
[weapon_frame:: pulse_tool_1h] | [prof:: 1] | [combat_role:: panic_stop]
```

Строка арсенала указывает конкретный экземпляр фрейма для MVP-доктрины. Если владение не заявлено, строка не пишется; `prof:: 0` не хранится как данные.

### Доступ к Frame

Обычный Frame не получает числовой атрибутный допуск и не становится закрытым, пока игрок не соберёт нужную характеристику. Доступ проходит три разных проверки:

```text
arsenal capability -> тело физически допускает Frame
proficiency gate  -> открывается его техника мастерства
named TOUCH consumer -> улучшается уже доступный физический результат
```

Первая граница бинарна только для настоящей анатомической несовместимости и живёт в capability/теге. Вторая принадлежит proficiency. Третья может улучшить удержание тяжёлой линии, взвод, Heat-цикл или возврат руки, но не запрещает базовое применение и не выдаёт общий урон.

`arcanegun` в этой системе означает магострельные и механические дальнобойные фреймы: разрядники, конденсаторы, эмиттеры и игольники. Они работают через батарейный цикл, heat, bloom и Dissonance.

## 4. Tags

Теги накладываются поверх combo.

- `add_vector` добавляет активный архетипный вектор только через тело, мутацию или редкую Fusion.
- `block_vector` выключает активный архетипный вектор.
- `prof_delta` меняет tier владения.
- `override_race_ban` разрешает физиологически спорный арсенал.
- `exclusive_with` запрещает несовместимые теги.
- `fusion_requires` описывает curated Trait Fusion, который появляется из двух тегов и связующего события.
- `power_weight` хранит внутренний балансный вес тега, не являясь характеристикой мира.
- `dissonance_load` меняет постоянный фон только для физически или эфирно заметных тегов.
- `attr_delta` меняет видимый Final TOUCH только для устойчивого изменения тела и проходит общий предел внешнего сдвига.
- `capability`, `vulnerability`, `arsenal_grant/block`, proficiency и module capacity являются допустимыми явными изменениями.
- Тег не добавляет коэффициент P/Q/E, скрытый рейтинг или второй источник уже оплаченного результата.

## 5. Proficiency Gates и Frame Commitment

Оружие не добавляет новый активный вектор в Combat Profile.

```text
final_prof = combo_prof + tag_prof_delta + temporary_modifiers
if final_prof >= mastery_gate:
    current frame unlocks mastery_unlock
```

Tier 1-2 - это использование оружия. Tier 3+ - это раскрытие мастерства фрейма: стабильность, техника, cancel, снижение экспозиции или дополнительное окно исполнения.

Фрейм имеет `frame_vector`, но этот вектор имеет `vector_scope:: commitment`. Он активен только когда игрок берёт обязательство действием: замах, aim hold, charge, shot, block или recovery. `frame_vector` не пересчитывает `Race.weak_to ∩ Spec.weak_to` и не входит в базовую карту Двойного Парадокса.

### Параллельный расчёт модулей

Профильные ёмкости Термоса не добавляют вектор автоматически и не используют оружейный `mastery_gate`.

```text
final_module_capacity = combo.module_capacity + stable_tags.module_capacity_delta
installed_module_cost <= final_module_capacity
```

Итог определяет допустимость вшитой сборки у мастера. Физические слоты и положения читаются из выбранного Термоса, а не из Combat Profile.

Для `arcanegun` `frame_vector:: ballistics` читается как временное обязательство линейного дальнего давления: stagger, aim punch, контроль линии, создание окна и безопасный добор, а не непрерывный DPS и не новый архетипный вектор.

Фреймы читают Final TOUCH напрямую и имеют отдельные Frame Window. Frame Window описывает создаваемое оружием тактическое окно, а не числовой параметр тела и не способ доставки P/Q/E.

| Frame/System | Прямые T.O.U.C.H.-входы | Frame Window |
|:---|:---|:---|
| `pulse_tool_1h` | `TRQ` держит импульс; `GRP` возвращает руку; `GLW` обслуживает Heat | `stagger_entry` |
| `condenser_rig_2h` | `TRQ` держит стойку; `SNS` читает линию; `GLW` обслуживает заряд | `weakspot_open` |
| `scatter_valve_2h` | `TRQ` держит конус; `LYR/GLW` разрешают исход перегруза | `entry_denied` |
| `needle_thrower_2h` | `GRP` обслуживает взвод; `SNS` читает открытую точку | `quiet_puncture` |
| Batteries | `GRP` обслуживает замену; `GLW` разрешает Heat/Overload | — |

### Current Commitment

Текущий фрейм добавляет не слабость архетипа, а моментную экспозицию:

```text
Current Commitment =
  equipped frame
  + active action phase
  + frame_vector
  + exposure_channels
  + commitment_time / recovery_time
```

Оружие в рюкзаке не создаёт экспозицию. Второй quick-slot может быть показан как готовая альтернатива, но не участвует в расчёте, пока игрок не достал фрейм и не начал действие.

Для компактной статистики используются:

```text
Frame Power =
  creates_window
  + exploits_window
  + mitigates_window
  + range_control
  + reliability

Frame Exposure =
  exposure_weight
  + commitment_time
  + recovery_time
  + heat
  + dissonance_pulse
  + weight / carry_tax
```

Численные веса являются прототипными и не заменяют playtest.

## 6. Combat Profile

Итоговый профиль содержит:

- активные векторы;
- вычисленную общую слабость `Race.weak_to ∩ Spec.weak_to`;
- дополнительные слабости от тегов;
- использованную `Growth Capacity`;
- текущий `Frame Commitment`, если Пешка находится в действии или recovery;
- видимые T.O.U.C.H. значения;
- конечные параметры прямых потребителей и активные doctrine exchanges;
- окна доминации по матрице Двойного Парадокса.

Контра всегда означает **возможность** доминации, а не автоматическую победу.

### Читаемое Резюме Билда

Combat Profile должен выводить из суммы систем, а не из одного тега/трейта:

1. основную возможность;
2. цену или обязательство;
3. главное окно уязвимости.

Пример формата:

> `Короткий штурм`: быстро передает батареи и стабилен вблизи; теряет ценность в затяжном бою; слаб к открытому дальнему давлению.

Алгоритм ярлыков и набор формулировок остаются задачей наполнения.
