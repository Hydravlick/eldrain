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

## 2. Combo P/Q/E

`Registry_Combos` - главный MVP-источник слияния способностей и разрешенного арсенала. Он не хранит Combat Profile напрямую.

Каждый combo обязан содержать:

```markdown
[req_race:: rat]
[req_spec:: scout]
[type:: blade] | [prof:: 2]
[type:: arcanegun] | [prof:: 1]
```

- **P** - пассивка: расовый талант, искаженный специализацией.
- **Q/E** - активные навыки: классовый шаблон, исполненный через биологию расы.
- **Combat Profile** вычисляется матрицами: `primary = Race.base_vector`, `secondary = Spec.base_vector`, `shared_weakness = Race.weak_to ∩ Spec.weak_to`.
- **Ability Model** выводится автоматически: одинаковые векторы дают `mono_vector_fusion`, разные - `race_spec_fusion`.

## 3. Allowed Arsenal

Для MVP итоговый арсенал берется из combo-блока:

```markdown
[type:: blade] | [prof:: 2]
[type:: arcanegun] | [prof:: 1]
```

Это уже отражает `Allowed = (RaceList union SpecList) - RaceBanned`, но без необходимости прямо сейчас дробить RaceList и SpecList по отдельным файлам.

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

## 5. Proficiency Gates

Оружие не добавляет вектор автоматически.

```text
final_prof = combo_prof + tag_prof_delta + temporary_modifiers
if final_prof >= vector_gate:
    Combat Profile gains weapon_vector
```

Tier 1-2 - это использование оружия. Tier 3+ - это раскрытие скрытого тактического вектора оружия.

## 6. Combat Profile

Итоговый профиль содержит:

- активные векторы;
- вычисленную общую слабость `Race.weak_to ∩ Spec.weak_to`;
- дополнительные слабости от тегов;
- открытые оружейные векторы;
- окна доминации по матрице Двойного Парадокса.

Контра всегда означает **возможность** доминации, а не автоматическую победу.
