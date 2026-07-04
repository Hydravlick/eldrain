---
type: mechanic
status: active
system: player_core
category: attributes
tags: [stats, touch, hidden_substats, arcanegun_combat, formulas, core]
base_attribute: 10
touch_schema:
  - { key: TRQ, label: Тяга }
  - { key: GRP, label: Хват }
  - { key: LYR, label: Слой }
  - { key: GLW, label: Накал }
  - { key: SNS, label: Чутье }
related_files:
  - "[[04_Player_Entities/Combat_Profile_Pipeline|Combat_Profile_Pipeline]]"
  - "[[05_Combat_Survival/Weapon_Core|Weapon_Core]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
  - "[[04_Player_Entities/_Registries/Registry_Races|Registry_Races]]"
  - "[[04_Player_Entities/_Registries/Registry_Specs|Registry_Specs]]"
  - "[[04_Player_Entities/_Registries/Registry_Combos|Registry_Combos]]"
  - "[[04_Player_Entities/_Registries/Registry_Tags|Registry_Tags]]"
---
# Система Атрибутов: T.O.U.C.H.

T.O.U.C.H. - это видимый фасад тела Пешки. Игрок видит пять характеристик, но боевые, лутовые и магострельные правила работают через скрытые производные параметры.

```text
CoreTOUCH(A) = 10 + RaceDelta(A) + SpecDelta(A)

ExternalShift(A) =
  StableTagDelta(A)
  + ActiveBodyInterfaceDelta(A)

OrdinaryFinalTOUCH(A) = clamp(CoreTOUCH(A) + ExternalShift(A), 6, 20)
FinalTOUCH(A) = OrdinaryFinalTOUCH(A) + ExplicitCorruptionException(A)

Hidden Substats = f(Final TOUCH, Combo, Tags, Gear, Frame)
```

T.O.U.C.H. остаётся телом Пешки. Теги описывают устойчивое изменение тела, а экипировка может сдвинуть первичный атрибут только через один активный [[07_Gear_Inventory/Thermos_System#Опорный контур|Опорный контур]].

`Temporary Effects` намеренно удалены из первичной формулы MVP. Временные эффекты меняют substats, conditions и output modifiers, но не переписывают пять чисел тела.

## 1. Три слоя системы

### Слой A: Видимые атрибуты

Пять чисел на карточке персонажа:

| Атрибут | Смысл |
|:---|:---|
| `TRQ` | масса, тяга, удержание позиции |
| `GRP` | хват, пальцы, взаимодействия |
| `LYR` | слои тела, травмостойкость, живучесть |
| `GLW` | накал, батареи, heat, перегруз |
| `SNS` | чутье, следы, weakspot, предупреждения |

### Слой B: Скрытые подхарактеристики

Скрытые параметры нужны для билдостроения и баланса, но игрок не обязан видеть все числа. UI должен показывать короткие readable labels: `Устойчивая стойка`, `Быстрые руки`, `Чистый контур`, `Чует перегрев`, `Тихий лутер`.

### Слой C: Источники модификаторов

- **Race** дает биологию, капы и врожденные скрытые бонусы.
- **Spec** дает профессиональный метод и боевые привычки.
- **Combo** дает манеру исполнения: условия, окна, tradeoff.
- **Tags** ломают правила, добавляют мутации, flaws и proficiency gates.
- **Gear** дает внешние бонусы через предметы, фреймы и батареи.

---

## 2. TRQ - Тяга

*Инерция, масса, перенос груза и способность не быть сдвинутым миром.*

> "Тяжесть - это надежно. Тяжесть не сдует ветром Пустоты."

| Substat | Что делает | Единица | Статус MVP | Потребитель |
|:---|:---|:---|:---|:---|
| `carry_load` | лимит веса и запас до перегруза | `kg` | `formula` | Carry Load |
| `recoil_damp` | гашение отдачи магострельного импульса | rating | `consumer` | Handcannon и тяжёлые Frame |
| `brace` | удержание осадной стойки, щита, двери, гарпуна | rating | `consumer` | Longframe, Harpoon, shield |
| `melee_force` | таран, stagger и пролом; не универсальный `+Damage` | rating | `prototype` | Weapon Melee impact/stagger |
| `heavy_ready` | подготовка тяжелого фрейма к выстрелу | rating | `consumer` | Harpoon и тяжёлые Frame |
| `reality_buffer` | ограниченный телесный вклад в фазовый удар | points | `consumer` | Gate Check `Shell.Reality_Buffer` |

`gate_resist` поглощён `reality_buffer` и больше не является отдельным substat. Средовая защита модулей считается отдельно и не заменяется телом.

**В бою:** высокий `TRQ` не делает стрелка точнее сам по себе. Он позволяет держать тяжелый фрейм, не терять стойку после импульса и меньше получать aim punch от чужого попадания.

---

## 3. GRP - Хват

*Мелкая моторика, руки, инструменты, батареи, болты и карманы.*

> "Мир шершавый. Чтобы выжить, нужно уметь хватать, крутить и не отпускать."

| Substat | Что делает | Единица | Статус MVP | Потребитель |
|:---|:---|:---|:---|:---|
| `loot_speed` | скорость обыска контейнеров | `%` | `prototype` | Looting Process |
| `cell_swap_speed` | замена батареи в магостреле или катализаторе | `%` | `formula` | Battery swap |
| `bolt_wind_speed` | взвод механического фрейма | `%` | `consumer` | Needle Crossbow |
| `weapon_swap_speed` | смена оружия и быстрых предметов | `%` | `prototype` | Weapon handling |
| `lockwork` | взлом, отмычки, тонкая механика | rating | `prototype` | locks/devices |
| `drift_control` | контроль дрейфа импульса руками | `%` | `formula` | Bloom Control |
| `field_craft_speed` | сборка болтов, тросов, стабилизаторов в рейде | `%` | `prototype` | field crafting |

**В бою:** высокий `GRP` ускоряет батарейный цикл и делает дальний бой менее беспомощным после выстрела, но не превращает магострел в скоростной DPS.

---

## 4. LYR - Слой

*Целостность тела, броневые слои, одежда, удача и способность не рассыпаться.*

> "Зашей рану, намотай скотч, надень еще один свитер. Ты не сломаешься, пока держишься вместе."

| Substat | Что делает | Единица | Статус MVP | Потребитель |
|:---|:---|:---|:---|:---|
| `structure_hp` | базовое здоровье | `HP` | `formula` | MaxHP |
| `trauma_resist` | сопротивление переломам и stagger | rating | `prototype` | Status Effects |
| `bleed_resist` | порог получения открытой раны, не общий резист урону | rating | `prototype` | Bleed application |
| `stamina_recovery` | восстановление после рывков и тяжести | `%` | `prototype` | Stamina |
| `armor_sync` | насколько тело принимает броню и пластины | rating | `prototype` | armor interaction |
| `backlash_resist` | сопротивление ожогам, отдаче батареи и кантрипам | points | `formula` | Backlash |
| `downed_time` | окно до смерти после падения | seconds | `deferred` | отсутствующий в MVP Downed cycle |

`downed_time` остаётся только как отложенный термин. Он не используется в активных формулах до появления полного цикла падения, спасения и смерти.

**В бою:** высокий `LYR` дает шанс пережить ошибку, импульс в пластину, backlash или неудачный кантрип. Это не броня вместо экипировки, а запас целостности.

---

## 5. GLW - Накал

*Внутренний жар, батареи, охлаждение, маготехника и перегруз.*

> "Батарея греет бок. Главное - не дай ей прожечь тебя насквозь."

| Substat | Что делает | Единица | Статус MVP | Потребитель |
|:---|:---|:---|:---|:---|
| `heat_sink` | скорость остывания оружия, катушки, перчатки | `%` | `formula` | Heat cycle |
| `battery_efficiency` | шанс снизить лишний heat/dissonance от импульса | `%` | `consumer` | Batteries |
| `output_power` | сила эфирных навыков и катализаторов | points | `consumer` | Catalyst/abilities |
| `overload_limit` | сколько перегруза тело выдерживает до backlash | points | `prototype` | Overcharge |
| `spark_gain` | скорость наполнения ограниченного биоэлектрического заряда от значимых импульсов | rating | `consumer` | `squirrel_assault` «Инерционный заряд» |
| `reality_burn_power` | сила Reality Burn и стабилизирующего урона | points | `consumer` | Catalyst Focus |

`spark_gain` имеет высший приоритет интеграции среди ещё не откалиброванных рейтингов. Расовое `+20` Белки не является готовыми `+20%`: оно должно войти в формулу порога значимого движения, убывающей отдачи и ёмкости накопленного импульса.

**В бою:** высокий `GLW` делает магострельный темп стабильнее: меньше перегрев, лучше переносимость Overcharge Cell, сильнее Q/E и Reality Burn. Но высокий `GLW` также может повышать заметность, если билд не гасит Dissonance.

---

## 6. SNS - Чутье

*Сенсорика, следы, слабые места, дрейф реальности и раннее предупреждение.*

> "Если волоски на шее встали дыбом - беги. Даже если глаза ничего не видят."

| Substat | Что делает | Единица | Статус MVP | Потребитель |
|:---|:---|:---|:---|:---|
| `danger_sense` | неполное предупреждение ловушек и засад | rating | `prototype` | trap/ambush warning |
| `trace_read` | расследования, следы, эхо событий | rating | `prototype` | Echo/investigation content |
| `shiny_detection` | ощущение потенциальной ценности без точной цены и содержимого | rating | `prototype` | «Экономика Плюшкина» |
| `ambush_resist` | защита от внезапных входов | points | `consumer` | Needle Crossbow/ambush |
| `entropy_warning` | предупреждение о фазовом давлении и Gate Check | rating | `prototype` | Gate warning |
| `weakspot_read` | чтение уязвимых зон | points | `formula` | Weakspot Read |
| `heat_warning` | предупреждение о перегреве, дрейфе и нестабильной батарее | rating | `prototype` | Heat warning |

**В бою:** высокий `SNS` не делает персонажа танком. Он помогает раньше понять, где цель раскроется, когда импульс сорвется и куда лучше вложить дорогой заряд.

---

## 7. Базовые параметры

| Параметр | Значение | Описание |
|:---|:---|:---|
| `base_attribute` | 10 | стартовое значение всех T.O.U.C.H. |
| `base_hp` | 80 | здоровье до LYR и gear |
| `base_stamina` | 100 | запас выносливости |
| `base_speed` | 5.0 m/s | базовая скорость бега |
| `base_carry_load` | 20 kg | переносимый вес до TRQ |
| `base_action_speed` | 1.0 | базовая скорость взаимодействий |
| `base_heat_sink` | 1.0 | базовая скорость охлаждения |
| `base_cell_swap` | 1.0 | базовая скорость замены батареи |

Обычная шкала итоговых атрибутов:

| Диапазон | Чтение |
|:---|:---|
| `6-9` | слабая сторона |
| `10-13` | норма |
| `14-16` | сильная специализация |
| `17-20` | экстремальная сборка |
| `21+` | аномальные значения через теги, артефакты или редкие combo |

### Внешний сдвиг и клэмп MVP

- один активный Опорный контур даёт Gear-вклад не выше `+2` к одному атрибуту;
- сумма положительных `Tags + Gear` не выше `+4` к одному атрибуту;
- заявленный бонус выше `20` не конвертируется в другую силу;
- UI показывает применённую часть и overflow до установки;
- Corruption может явно сдвинуть один предел на `1` за собственную постоянно релевантную цену.

```text
Слабый случай:    Core 7  + External 4 = 11, Applied +4, Overflow 0
Базовый случай:   Core 10 + External 4 = 14, Applied +4, Overflow 0
Белка-Догмат GLW: Core 19 + External 4 = 20, Applied +1, Overflow 3
```

Экстремальное тело получает меньше пользы от усиления уже сильной стороны. Переполненный `touch_shift` можно носить ради других функций модуля, но лишние очки T.O.U.C.H. не работают.

---

## 8. Формулы MVP

### Structure / HP

```text
MaxHP = base_hp + (LYR * 4) + race_hp_bonus + gear_hp_bonus
```

### Carry Load

```text
CarryLoad = base_carry_load + (TRQ * 2.5kg) + substat_bonus(carry_load)
```

### Cell Swap

```text
CellSwapTime = base_cell_swap / (1 + ((GRP - 10) * 0.035) + (substat_bonus(cell_swap_speed) / 100))
```

### Heat Sink

```text
HeatSink = base_heat_sink * (1 + ((GLW - 10) * 0.03) + (substat_bonus(heat_sink) / 100))
```

### Bloom Control

```text
BloomGain = frame_bloom
  + movement_penalty
  + panic_penalty
  + heat_penalty
  - (TRQ * 0.01)
  - (GRP * 0.012)
  - (substat_bonus(drift_control) / 100)
```

### Weakspot Read

```text
WeakspotRead = SNS + substat_bonus(weakspot_read) + frame_scope_bonus
```

### Backlash Resist

```text
BacklashResist = LYR + GLW + substat_bonus(backlash_resist)
```

Эти формулы являются рабочими якорями для баланса, а не финальными числами. Главное правило: ни один атрибут не должен в одиночку превращать магострел в непрерывный DPS.

---

## 9. Dataview-контракт скрытых бонусов

Race, Spec, Combo, Tags и Gear могут добавлять скрытые бонусы через однотипные поля.

```markdown
[substat_bonus:: heat_sink +10, cell_swap_speed +8]
[substat_mult:: recoil_damp x1.10]
[condition_bonus:: while_stationary: brace +20, recoil_damp +15]
[cap_mod:: max_carry +5kg]
[tradeoff:: relocation_speed -10, dissonance_load +4]
```

- `substat_bonus` - плоский бонус к скрытой подхарактеристике.
- `substat_mult` - множитель, использовать редко.
- `condition_bonus` - лучший формат для combo: сила включается при понятном поведении.
- `cap_mod` - меняет пределы тела или экипировки.
- `tradeoff` - цена, которая удерживает билд в балансе.

### Единицы и readable labels

`substat_bonus` не является общей безразмерной валютой. Единица закреплена в каталоге выше: процентные рейтинги входят в дробную формулу через `value / 100`, points складываются как очки, `kg` — как масса, а Capability хранится отдельным бинарным полем.

Readable label строится по реализованному изменению действия, а не по сырому рейтингу:

- менее `5%` — отдельная подпись не выводится;
- `5–14%` — обычная короткая подпись;
- `15%+` — усиленная подпись;
- prototype без откалиброванного потребителя показывает конкретное поле без оценочного label.

| Substat | `5–14%` | `15%+` |
|:---|:---|:---|
| `brace` | `Устойчивая стойка` | `Несдвигаемый` |
| `cell_swap_speed` | `Быстрые руки` | `Батарея на лету` |
| `heat_sink` | `Чистый контур` | `Холодный контур` |
| `heat_warning` | `Чует перегрев` | `Слышит срыв` |
| `loot_speed` | `Быстрые карманы` | `Обыск на ходу` |

## 10. Правило для combo

Combo не должно дублировать профиль Race/Spec. Оно не хранит "Профиль" и не должно просто давать `+3 TRQ`.

Хороший combo-бонус:

```markdown
[condition_bonus:: while_stationary: brace +20, recoil_damp +15]
[tradeoff:: relocation_speed -10, dissonance_load +3]
```

Плохой combo-бонус:

```markdown
[TRQ:: +3]
[profile:: tank_ranged]
```

Combo отвечает за **манеру исполнения**: стоять и давить, проходить вентиляцию, сжигать батарею в одном залпе, читать weakspot, держать химическую зону.
