---
type: system
status: active
system: combat_profile
tags: [combat_profile, two_paradox, abilities, arsenal, tags]
related_files:
  - "[[04_Player_Entities/Ability_Synergy]]"
  - "[[04_Player_Entities/Shell_Construction]]"
  - "[[04_Player_Entities/Proficiency_Arsenal]]"
  - "[[04_Player_Entities/Tags_System]]"
  - "[[04_Player_Entities/Two_Paradox_Vector_Matrix]]"
  - "[[04_Player_Entities/_Registries/Registry_Combos]]"
  - "[[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]]"
---
# Combat Profile Pipeline

> Канон расчета Оболочки: `Race + Spec -> Combo P/Q/E + Module Capacity -> Allowed Arsenal -> Tags -> Proficiency Gates -> Combat Profile и допустимая сборка Термоса`.

## 1. Race + Spec

Раса и специализация задают базовую биологию, роль, атрибуты и два стартовых тактических вектора.

- Раса отвечает за физиологическую основу, физику тела и биологические ограничения.
- Специализация отвечает за методологию давления, подготовки и решения задач.
- Их сумма не является готовой способностью. Готовые способности появляются только после слияния в `Registry_Combos`.
- На этом шаге считается видимый `Final TOUCH` и первый слой скрытых подстатов: `brace`, `cell_swap_speed`, `heat_sink`, `weakspot_read`, `backlash_resist` и другие.

```text
Final TOUCH = 10 + Race + Spec + Tags + Gear + Temporary Effects
Hidden Substats = f(Final TOUCH, Race.substat_bonus, Spec.substat_bonus)
```

## 2. Combo P/Q/E

`Registry_Combos` - главный MVP-источник слияния способностей и разрешенного арсенала. Он не хранит Combat Profile напрямую.

Игровой MVP использует зафиксированные расы Ёж, Крыса, Белка и классы Авангард, Технократ, Странник. `Registry_Combos` содержит ровно девять проектных слотов этой матрицы. Полная сетка 5x5 сохраняется как внутренняя карта расширения.

Наличие слота не означает готовый контент. Ячейка считается канонически спроектированной только после двойной проверки из [[04_Player_Entities/MVP_3x3_Design_Contract|контракта 3×3]].

Каждый combo обязан содержать:

```markdown
[req_race:: rat]
[req_spec:: scout]
[arsenal_type:: blade] | [prof:: 2]
[arsenal_type:: arcanegun] | [prof:: 1]
```

- **P/Q/E** — смешанные способности конкретной пары `Race × Spec`.
- **Q/E** — самостоятельные ситуативные действия, а не обязательная ротация.
- **Combat Profile** вычисляется матрицами: `primary = Race.base_vector`, `secondary = Spec.base_vector`, `shared_weakness = Race.weak_to ∩ Spec.weak_to`.
- **Ability Model** выводится автоматически: одинаковые векторы дают `mono_vector_fusion`, разные - `race_spec_fusion`.
- **Substat Model** берется из `condition_bonus` и `tradeoff` combo. Combo не должен дублировать Race/Spec атрибуты, он должен задавать условную манеру исполнения.

## 3. Allowed Arsenal

Для MVP итоговый арсенал берется из combo-блока:

```markdown
[arsenal_type:: blade] | [prof:: 2]
[arsenal_type:: arcanegun] | [prof:: 1]
```

Это уже отражает `Allowed = (RaceList union SpecList) - RaceBanned`, но без необходимости прямо сейчас дробить RaceList и SpecList по отдельным файлам.

`arcanegun` в этой системе означает магострельные и механические дальнобойные фреймы: разрядники, конденсаторы, эмиттеры, гарпуны и игольники. Они работают через батарейный цикл, heat, bloom и Dissonance.

## 4. Tags

Теги накладываются поверх combo.

- `add_vector` добавляет активный вектор.
- `block_vector` выключает активный или оружейный вектор.
- `prof_delta` меняет tier владения.
- `override_race_ban` разрешает физиологически спорный арсенал.
- `exclusive_with` запрещает несовместимые теги.
- `fusion_requires` описывает curated Trait Fusion, который появляется из двух тегов и связующего события.
- `power_weight` хранит внутренний балансный вес тега, не являясь характеристикой мира.
- `dissonance_load` меняет постоянный фон только для физически или эфирно заметных тегов.
- `substat_bonus` меняет скрытые параметры T.O.U.C.H.
- `condition_bonus` включает бонус при понятном поведении.
- `tradeoff` фиксирует цену силы.

## 5. Proficiency Gates

Оружие не добавляет вектор автоматически.

```text
final_prof = combo_prof + tag_prof_delta + temporary_modifiers
if final_prof >= vector_gate:
    Combat Profile gains weapon_vector
```

Tier 1-2 - это использование оружия. Tier 3+ - это раскрытие скрытого тактического вектора оружия.

Открытие оружейного вектора не удаляет и не пересчитывает базовую общую слабость `Race × Spec`. Оно добавляет возможность в Combat Profile, сохраняя исходную цену архетипа.

### Параллельный расчёт модулей

Профильные ёмкости Термоса не добавляют вектор автоматически и не используют оружейный `vector_gate`.

```text
final_module_capacity = combo.module_capacity + stable_tags.module_capacity_delta
installed_module_cost <= final_module_capacity
```

Итог определяет допустимость вшитой сборки у мастера. Физические слоты и положения читаются из выбранного Термоса, а не из Combat Profile.

Для `arcanegun` открытый `weapon_vector:: ballistics` читается как **линейное дальнее давление**: stagger, aim punch, контроль линии, создание окна и безопасный добор, а не непрерывный DPS.

Магострельные фреймы читают скрытые substats и отдельные Frame Window. Frame Window описывает создаваемое оружием тактическое окно, а не числовой параметр тела.

| Frame/System | Главные substats | Frame Window |
|:---|:---|:---|
| `handcannon` | `recoil_damp`, `drift_control`, `cell_swap_speed` | `pressure_open` |
| `condenser_longframe` | `brace`, `weakspot_read`, `heat_sink` | `weakspot_open` |
| `scatter_emitter` | `backlash_resist`, `heat_sink` | `melee_setup` |
| `harpoon_driver` | `heavy_ready`, `brace` | `tether_control` |
| `needle_crossbow` | `bolt_wind_speed`, `weakspot_read`, `ambush_resist` | `ambush_open` |
| `catalyst_focus` | `output_power`, `reality_burn_power`, `backlash_resist` | `reality_burn` |
| Batteries | `battery_efficiency`, `heat_sink`, `cell_swap_speed` | — |

## 6. Combat Profile

Итоговый профиль содержит:

- активные векторы;
- вычисленную общую слабость `Race.weak_to ∩ Spec.weak_to`;
- дополнительные слабости от тегов;
- использованную `Growth Capacity`;
- открытые оружейные векторы;
- видимые T.O.U.C.H. значения;
- скрытые substats и активные condition bonuses;
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
