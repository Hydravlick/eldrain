---
type: mechanic
system: player_core
tags:
  - tags
  - traits
  - mutation
  - implants
related_files:
  - "[[04_Player_Entities/_Registries/Registry_Tags|Registry_Tags]]"
---

# Система Тегов: Мутации и Черты

## 1. Что такое Тег?
**Тег (Tag)** — это модификатор, закрепленный за Оболочкой. Это может быть мутация, маго-имплант, болезнь или особенность характера. Все теги двойные: одновременно имеют положительный и негативный эффект.

В новой системе теги являются не только цифрами, а **векторными переключателями** и модификаторами скрытых подхарактеристик T.O.U.C.H. Они могут добавлять тактический вектор, блокировать вектор, менять proficiency tier, усиливать батарейный цикл или обходить запрет арсенала. Любое усиление обязано иметь цену: атрибут, резонанс, слабость, шум, токсичность, heat или ограничение веса.

## 2. Типы Тегов

### За эффектом:
1.  **Теги Мастерства (Proficiency Tags):** 
	- Повышают Tier владения оружием. 
	- *Пример:* `[Trench Reflex]` (+Arcanegun, +Blade, -Catalyst).
	- В Dataview: `[prof_delta:: arcanegun +1, catalyst -1]`.
2.  **Теги Мутации (Mutation Tags):**
	- Меняют правила игры или тип урона. 
	- *Пример:* `[Voltaic Blood]` (Конвертирует физ. урон в электрический).
	- В Dataview: `[add_vector:: aether]` и/или `[block_vector:: hazard]`.
3.  **Теги Атрибутов (Attribute Tags):** 
	- Линейно меняют статы или скрытые substats. 
	- *Пример:* `[Piston Arm]` (+TRQ, -SNS).
	- В Dataview: `[attr_delta:: TRQ +2, SNS -1]` и `[substat_bonus:: heavy_ready +15]`.
4.  **Негативные Трейты (Flaw Tags):**
	- Дают штраф, блокируют вектор или сужают арсенал.
	- *Пример:* `[Brittle Nerves]` (-GLW, блок Aether).
	- В Dataview: `[tag_kind:: flaw]` и `[resonance_credit:: 2]`.
5.  **Теги Слияния (Fusion Tags):**
	- Заменяют два малых тега одним мощным тегом с более высокой ценой.
	- *Пример:* `[Street Breacher]` = `[street_rat] + [trench_veteran]`.
	- В Dataview: `[fusion_requires:: street_rat, trench_veteran]`.

### За происхождением:
1.  **Врожденные (Origin Tags):**
    * Даются при создании/генерации Оболочки.
    * *Пример:* `[Born in Gutter]` (+Стелс, -Харизма).
2.  **Приобретенные (Acquired Tags):**
    * Получаются в рейдах (Травмы, Мутации от Аномалий).
    * *Пример:* `[Greyscale Infection]` (+Броня, -Скорость).

## 3. Влияние на Резонанс
Каждый Тег имеет "Цену" в Резонансе.
* **Техно-теги:** Повышают заметность для Аномалии (Шум).
* **Био-теги:** Могут снижать заметность (Маскировка), но влиять на Рассудок.

## 4. Иерархия конфликтов

Если несколько систем спорят, используется такой порядок:

1. **Физиология и теги тела** - самая сильная надстройка. Тег может открыть запрещенный арсенал или заблокировать потенциал оружия, но обязан дать цену.
2. **Combo P/Q/E** - основной источник способностей. Способности читаются из `Registry_Combos`, где раса и класс уже смешаны.
3. **Proficiency Gate** - решает, насколько полно персонаж раскрывает оружие.
4. **Оружие и броня** - добавляют скрытые векторы только при открытом гейте или явном теге.
5. **Автоматические matchup-матрицы** - `00_Balance` и `00_Synergy_Map` считают связи из реестров, а не из ручных notes.

## 5. Контракт тега для автоматизации

```markdown
### Шаблон Тега (Template Tag)
[id:: template_tag]
[tag:: template_tag]
[tag_kind:: proficiency | mutation | attribute | flaw | fusion]
[tag_polarity:: positive | mixed | negative]
[add_vector:: tech]
[block_vector:: hazard]
[prof_delta:: arcanegun +1, catalyst -1]
[attr_delta:: TRQ +2, SNS -1]
[substat_bonus:: heat_sink +10, cell_swap_speed +8]
[condition_bonus:: while_stationary: brace +20]
[tradeoff:: resonance +4, movement_noise +8]
[override_race_ban:: heavy_weapon]
[exclusive_with:: incompatible_tag]
[fusion_with:: other_tag -> result_tag]
[fusion_requires:: source_tag_a, source_tag_b]
[resonance_cost:: 10]
[resonance_credit:: 0]
```

- `add_vector` добавляет активный вектор к Combat Profile.
- `block_vector` выключает активный вектор или скрытый вектор оружия.
- `prof_delta` меняет итоговый tier владения.
- `substat_bonus` меняет скрытые параметры T.O.U.C.H. вроде `heat_sink`, `cell_swap_speed`, `drift_control`.
- `condition_bonus` включает бонус только при понятном поведении.
- `tradeoff` фиксирует цену бонуса: resonance, heat, шум, слабость или потерю темпа.
- `override_race_ban` разрешает оружие, которое физиология обычно запрещает.
- `exclusive_with` фиксирует несовместимые теги.
- `fusion_with` показывает возможное слияние у исходного тега.
- `fusion_requires` у fusion-тега фиксирует пару источников.
- `resonance_cost` делает сильные теги заметными для Аномалии и экономики.
- `resonance_credit` возвращает часть бюджета за flaw-тег, но не отменяет его штраф.
