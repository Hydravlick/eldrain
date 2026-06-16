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
---
# Combat Profile Pipeline

> Канон расчета Оболочки: `Race + Spec -> Combo P/Q/E -> Allowed Arsenal -> Tags -> Proficiency Gates -> Combat Profile`.

## 1. Race + Spec

Раса и специализация задают базовую биологию, роль, атрибуты и два стартовых тактических вектора.

- Раса отвечает за врожденный талант, физику тела и биологический способ выживания.
- Специализация отвечает за шаблон действия, дистанцию, роль и метод доставки.
- Их сумма не является готовой способностью. Готовые способности появляются только после слияния в `Registry_Combos`.
- На этом шаге считается видимый `Final TOUCH` и первый слой скрытых подстатов: `brace`, `cell_swap_speed`, `heat_sink`, `weakspot_read`, `backlash_resist` и другие.

```text
Final TOUCH = 10 + Race + Spec + Tags + Gear + Temporary Effects
Hidden Substats = f(Final TOUCH, Race.substat_bonus, Spec.substat_bonus)
```

## 2. Combo P/Q/E

`Registry_Combos` - главный MVP-источник слияния способностей и разрешенного арсенала. Он не хранит Combat Profile напрямую.

MVP использует 9 curated-комбо как сбалансированный стартовый набор. Полная сетка 5x5 может быть добавлена позже, но текущие матрицы должны читать отсутствие пары как "не утверждено для MVP", а не как сломанную механику.

Каждый combo обязан содержать:

```markdown
[req_race:: rat]
[req_spec:: scout]
[arsenal_type:: blade] | [prof:: 2]
[arsenal_type:: arcanegun] | [prof:: 1]
```

- **P** - пассивка: расовый талант, искаженный специализацией.
- **Q/E** - активные навыки: классовый шаблон, исполненный через биологию расы.
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

`arcanegun` в этой системе означает магострельные и механические дальнобойные фреймы: разрядники, конденсаторы, эмиттеры, гарпуны и игольники. Они работают через батарейный цикл, heat, bloom и resonance.

## 4. Tags

Теги накладываются поверх combo.

- `add_vector` добавляет активный вектор.
- `block_vector` выключает активный или оружейный вектор.
- `prof_delta` меняет tier владения.
- `override_race_ban` разрешает физиологически спорный арсенал.
- `exclusive_with` запрещает несовместимые теги.
- `fusion_requires` описывает тег, который появляется при слиянии двух малых тегов.
- `resonance_credit` компенсирует штрафные flaw-теги без превращения их в бесплатную силу.
- `resonance_cost` удерживает сильные сборки в экономике риска.
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

Для `arcanegun` открытый `weapon_vector:: ballistics` читается как **линейное дальнее давление**: stagger, aim punch, контроль линии, создание окна и безопасный добор, а не непрерывный DPS.

Магострельные фреймы также читают скрытые подстаты:

| Frame/System | Главные substats |
|:---|:---|
| `handcannon` | `recoil_damp`, `drift_control`, `cell_swap_speed` |
| `condenser_longframe` | `brace`, `weakspot_read`, `heat_sink` |
| `scatter_emitter` | `backlash_resist`, `heat_sink`, `melee_setup` |
| `harpoon_driver` | `heavy_ready`, `brace`, `tether_control` |
| `needle_crossbow` | `bolt_wind_speed`, `weakspot_read`, `ambush_resist` |
| `catalyst_focus` | `output_power`, `reality_burn_power`, `backlash_resist` |
| Batteries | `battery_efficiency`, `heat_sink`, `cell_swap_speed` |

## 6. Combat Profile

Итоговый профиль содержит:

- активные векторы;
- вычисленную общую слабость `Race.weak_to ∩ Spec.weak_to`;
- дополнительные слабости от тегов;
- открытые оружейные векторы;
- видимые T.O.U.C.H. значения;
- скрытые substats и активные condition bonuses;
- окна доминации по матрице Двойного Парадокса.

Контра всегда означает **возможность** доминации, а не автоматическую победу.
