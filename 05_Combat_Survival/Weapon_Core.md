---
status: active
system: action_combat
tags:
  - weapons
  - tiers
  - arcaneguns
  - battery_combat
related_files:
  - "[[05_Combat_Survival/Combat_Three_Debts|Combat_Three_Debts]]"
  - "[[05_Combat_Survival/Weapon_Ranged|Weapon_Ranged]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
  - "[[05_Combat_Survival/Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Skill_Build_Philosophy|Skill_Build_Philosophy]]"
  - "[[07_Gear_Inventory/Gear_Progression|Gear_Progression]]"
type: system
index_route: owner
index_group: combat_survival
index_order: 180
index_summary: "Определяет состояния, разрешение и связи: Оружие: идентичность и исполнение."
read_when: "Когда нужен контракт «Оружие: идентичность и исполнение» и его границы с соседними владельцами."
---
# Оружие: идентичность и исполнение

## 1. Главный принцип

Верхнеуровневый контракт боя задан в [[05_Combat_Survival/Combat_Three_Debts|Законе трёх долгов]]. Оружие не отменяет цену действия: оно выбирает, где и когда игрок платит дистанцией, вниманием, подготовкой и Recovery.

Дальний бой в Элдрейне - это **магострельная технология**: катушки, руны, конденсаторы, батареи, перегрев и Диссонанс. Тросовые и процедурные устройства принадлежат навыкам и используют собственный контракт источника.

```text
Дальний бой = давление + контроль + окно добивания
не = непрерывный DPS и низкий TTK
```

Оружие может убивать самостоятельно, если игрок держит дистанцию, контролирует охлаждение, расходует локальный magazine, если конструкция его использует и попадает в слабые места. Но нормальная роль магострела - сбить темп, раскрыть позицию, прожечь защиту или создать окно для `melee / Q / E / команды`.

### Combat Feel

Бой находится на пересечении:

- **Hunt: Showdown:** каждый выстрел является событием, звук раскрывает намерение и позицию, промах имеет цену, попадание читается по реакции цели;
- **Apex Legends:** пространство поддерживает вертикальные углы, быстрый поиск маршрута и мобильные тела;
- **Eldraine:** действие тяжелее и обязательнее, чем в Apex. Свобода движения не отменяет взвод, отдачу, перегрев, восстановление и риск переносимого веса.

> Персонаж движется свободно, но каждое совершенное действие обладает весом.

После входа в `Commitment` Recovery принадлежит действию, а не предмету. Смена оружия, Q/E, блок или взаимодействие не удаляют это окно уязвимости.

## 2. Запрет на современный темп

В каноне MVP нет скоростных магазинных фреймов и непрерывного дальнего DPS. Быстрый повторный огонь заменяется на:

- `charge_time` - подготовка импульса;
- `bloom` - эфирный разброс после движения, паники и повторного выстрела;
- `heat` - перегрев ствола, катушки или перчатки;
- `dissonance` - эфирный след для Аномалии;
- `battery_cycle` — ресурсная процедура по отдельному владельцу.

Full Battery оплачивает одну атомарную транзакцию и становится физической Drained Cell по [[05_Combat_Survival/Magic_Batteries|Magic Batteries]]. Pattern может объявить magazine model; текущий остаток хранит конкретный Weapon ItemID по [[05_Combat_Survival/Weapon_Ranged|Weapon Ranged]]. После reload отдельный выстрел больше не читает батарею.

Если способность временно повышает темп, она должна платить перегревом, Диссонансом, потерей движения или явно объявленной ценой своей операции.

## 3. Frame → Pattern → ItemID

Frame даёт игроку переносимое понимание незнакомого оружия: какую spatial job оно выполняет, какую дистанцию и позицию хочет, как организует тело, какие классы операций допускает, каким Commitment платит и какого ответа боится. Его grammar envelope включает Natural Debt, пределы вариаций и learnability prior. Он не задаёт точный moveset каждой конструкции.

**Новый Frame нужен, когда знание старого Frame систематически заставляет игрока выбирать неправильную позицию или неправильный тип ответа.** Изменение отдельного ввода или траектории само по себе не создаёт новый Frame.

Pattern — повторяемая физическая конструкция внутри Frame. Он определяет конкретный moveset: Primary, необязательный Alt, необязательную поддержку Aim, траектории, подготовку, порядок операций, сервисные требования, видимые состояния конструкции и поведение выпуска. Aim и Alt не обязательны и не являются одной операцией. Pattern не знает конкретного соседнего Pattern и не публикует pair-specific combo matrix.

ItemID — эта физическая вещь, ссылающаяся на Pattern. Она хранит condition, повреждения, текущий Heat и device state, rarity/affixes, provenance, custody и экономическую судьбу. Magazine, если Pattern использует эту модель, также является runtime state конкретного Weapon ItemID по [[05_Combat_Survival/Weapon_Ranged|ranged contract]]. Обычный случайный экземпляр не получает новый moveset. Две копии одного Pattern используют одни определения операций, но независимо повреждаются, нагреваются и меняют владельца.

### Знакомство с Pattern

Игрок узнаёт возможности и ограничения найденной конструкции по виду, dry-use, анимации, краткой operational information и ограниченному числу проб. Знание Frame даёт осмысленную исходную гипотезу; точную траекторию и продолжения можно восстановить на месте. Скрытые combo counters, история последовательностей, случайное переписывание moveset, неразличимые wind-ups и невидимый каталог procs не являются допустимым способом создавать обычную Pattern identity.

Различие Pattern может менять продолжения после попадания, промаха, блока или изменения дистанции. Оно не должно делать длинную запомненную ротацию всегда правильным решением. Противник получает своевременный tell действия или состояния, если различие меняет его непосредственный ответ; знать каталог моделей для базовой контригры не требуется.

## 4. Публикация и граница gear progression

[[05_Combat_Survival/Registries/Registry_Weapons|Registry Weapons]] задаёт schema и publication contract. Наличие файла не означает действующее оружие. Нулевой активный арсенал допустим; diagnostic fixtures проверяют архитектуру отдельно от последующего Real Frame / Pattern Content Pass.

Frame Class / `load_tier` — унаследованное имя construction/load axis с действующими потребителями в [[07_Gear_Inventory/Gear_Progression|Gear Progression]], ballistics и calibration. Её окончательное владение остаётся отдельным gear-progression вопросом. Она не является обязательным полем Frame или Pattern identity, и Diagnostic Fixtures не должны от неё зависеть.

## 5. Тиры, TTK и броня

Высокий TTK держится не тем, что все выстрелы слабые, а тем, что выстрел редко является бесплатным продолжением мышки.

- Хорошее попадание должно быть ощутимым: stagger, aim punch, трещина щита, открытие weakspot.
- Убийство дальним боем требует серии решений: позиция, заряд, расход батареи, контроль heat, повторный угол.
- Ближний бой и способности остаются важными, потому что магострел чаще **создает окно**, чем закрывает весь бой сам.
- Общего `Efficient Tier` нет. Покров, щиты и особые цели раскрываются через Frame, weakspot, навыки или устройства аномальной процедуры, статусы, тип импульса и достаточное число сильных действий.
- Сильный PvE-контент должен проверять цикл оружия, а не единственный высокий выстрел: снять защиту, пережить ответ, удержать позицию и завершить окно.

### Обязательная Обратная Связь

Для операций каждого Pattern нужно определить:

- звук подготовки и выстрела;
- движение рук, оружия и камеры;
- длительность обязательства до следующего полного действия;
- реакцию мягкой цели, брони, щита и weakspot;
- визуальный и звуковой язык промаха, рикошета, stagger и перегрева.

Числа урона не заменяют ощущение. Игрок должен понимать результат по телу врага, звуку материала и изменению боевого окна.

## 6. Локальное владение параметрами оружия

| Владелец | Что определяет или хранит | Чего не присваивает |
|---|---|---|
| Frame | Переносимая grammar envelope, пространственная работа, Natural Debt и контригра | Exact Pattern moveset, runtime state, magazine, Heat, текущий Action debt |
| Pattern / Skill definition | Определение операции; у оружия — конкретная конструкция и moveset | Pawn proficiency, текущая condition/provenance и исполнение Action |
| ItemID | Ссылка на Pattern и независимое физическое runtime state вещи | Новый случайный moveset или телесный Recovery Пешки |
| Action | Текущая фаза, принятый Commitment, bodily claims, interruption, Effect occurrence, Recovery и release points | Идентичность конструкции или постоянный уровень владения |
| Pawn ↔ Frame | Отношение Proficiency по [[04_Player_Entities/Proficiency_Arsenal\|владельцу доступа]] | Pattern-level и ItemID-level prof, Mastery unlocks, prof-specific movesets |
| Body | Физическая capability/vulnerability, morphology и текущая травма | Универсальный множитель урона или скорости оружия |
| Inventory | Custody, вес, доступность ItemID и Ready Access | Определения атак и принятый долг |

Pattern задаёт ожидаемые требования и цены операции; конкретный Action принимает их по [[05_Combat_Survival/Combat_Three_Debts|общему контракту исполнения]]. Рука, занятая вещью, и claim исполняемого действия — разные факты. Технический цикл ItemID и телесное восстановление Action остаются раздельными; смена предмета или Q/E не стирает принятое обязательство.

`Frame.NativeAction` как совмещённый владелец exact moveset и исполнения, а также universal Mastery в weapon identity — superseded. При `prof >= 1` доступен полный moveset Pattern. Уровни и handling semantics задаёт [[04_Player_Entities/Proficiency_Arsenal|Proficiency owner]]: prof влияет на качество возвращения контролируемой готовности через объявленное исполнение, не на identity Pattern или текущие claims. Mastery не преобразуется автоматически в Trait.

Связи с другими системами используют узкие содержательные interfaces. Они не передают владение исходному Trait/Q/E и не собираются в универсальный Power Score или общий weapon-tags resolver. Реализуемое действие должно сохранять встречную цену и читаемый результат. Точные параметры и исключения проверяются у владельца операции, а не создают второй engine внутри Frame.

Локальный `downstream_edge` по-прежнему называет `source.property → owner.parameter`, один наблюдаемый результат и встречную цену в той же сцене: Heat, Commitment, занятые руки, Pulse, потерю угла или Recovery. Одно ребро не улучшает одновременно результат, частоту и безопасность. Этот принцип не переносит definition или исполнение к источнику запроса.

## Weapon requests из Set

[[07_Gear_Inventory/Equipment_PaperDoll|Weapon Set]] читает Primary/optional Alt у Pattern и создаёт operation request по semantic channels из [[01_Core_Vision/Input_Contract|Input Contract]]. Set не хранит второй moveset и не гарантирует готовность действия. Общая eligibility учитывает требования операции, actual occupancy, outstanding claims, состояние ItemID и среды по [[05_Combat_Survival/Combat_Three_Debts|Action contract]].

`hand_requirement` Pattern описывает требуемую организацию. `free_hand` как требование операции означает фактически доступную руку, а не `empty` в prepared layout. Рука, занятая временным объектом или Action claim, не становится свободной от пустого Set slot.

### Weapon Focus

Weapon Focus — precision stance одного weapon owner. Игрок получает выделенную точную подготовку, когда активная Set содержит ровно один независимый weapon ItemID и его Pattern поддерживает Focus. Один 2H ItemID, занимающий обе позиции, считается одним owner. У двух независимых оружий dedicated Focus недоступен, даже если только одно из них умеет Focus. Перестановка ItemIDs между hand slots ничего не меняет.

Это сознательный обмен: single-owner Set покупает precision preparation, dual — две немедленно выбираемые независимые Primary operations. Ни selected weapon, ни last-fired recipient, ни hidden scoring здесь нет. Неоружейный предмет сам по себе не становится weapon owner; физические требования Focus всё равно проверяются Action. Combat accessory со своей независимой weapon operation считается вторым owner.

Pattern объявляет `supports_focus` и локальную `focus_operation`. Поддержка не выводится из ranged/melee категории. Weapon Core потребляет `weapon_focus` из [[01_Core_Vision/Input_Contract|Input Contract]], проверяет единственного owner и разрешает его operation request. Actual occupancy и подготовленная Set приходят из [[07_Gear_Inventory/Equipment_PaperDoll|PaperDoll]], исполнение — из [[05_Combat_Survival/Combat_Three_Debts#Targeting и одна Preparation|Action contract]]. Неподдерживаемый Focus даёт понятную недоступность без fallback.

```yaml
weapon_focus_contract:
  intent: weapon_focus
  owner_count: distinct_weapon_itemids
  required_owner_count: 1
  support_field: supports_focus
  operation_field: focus_operation
  dual_available: false
  slot_order_independent: true
  changes_channels: false
  runtime_owner: ACTION_EXECUTION
  release_fires: false
  resume: same_intent_same_context_after_legal_recovery
```

LMB/RMB сохраняют Primary/optional Alt в single/2H и Primary A/Primary B в dual. Focus не превращает RMB в zoom, Aim или специальный выстрел. Если Alt использует подготовленное target solution, это объявляет сама Alt definition. Runtime claims определяют возможность исполнения уже выбранной операции, а не смысл кнопки. Primary/Alt может принять подготовленное решение того же weapon owner по своей definition; это переход единственной Preparation к выбранному Commit, не запуск второй параллельной подготовки и не новый moveset.

Focus позволяет наблюдать и готовить линию без принятия будущего выстрела. Primary или Alt принимает собственный Commit. Пока Focus удерживается в том же контексте, после законного Recovery возможна повторная Preparation. Отпускание Focus завершает active/pending uncommitted Preparation и не стреляет. Q/E, Reload и Switch Set прекращают это намерение Focus: для возврата требуется новое намерение, а не сохранённый raw hold. Уже committed Action продолжает отвечать за свой долг.

Focus обязан покупать другой control envelope за authored settle/acquisition, ограничение движения или facing, читаемый tell, exposure либо cancellation cost. Unprepared execution сохраняет причину применения. Длительности, камера, ограничения и tell задаются Pattern и проверяются прототипом; один бесплатный бонус точности не является достаточной grammar.

Dual может иметь точный thrust, braced discharge, narrow line или charged strike как собственную Primary operation. Запрет dedicated Focus не запрещает точные операции. Hold/release также допустим только по физике конкретной операции, не как универсальная экономия кнопки.

## 7. Стихии и импульсы

Для MVP стихия - это не отдельная RPS-игра поверх оружия и не список школ магии для билдов. Это свойство импульса, батарейного канала, биома или статусного эффекта:

- `thermal` - нагрев конкретного материала, света или участка среды;
- `shock` - объявленный источником interrupt для `interruptible` действия либо перегруз конкретной техники; глобальных цепных реакций нет;
- `acid` - состояние конкретной брони, крепления или укрытия, а не общий debuff тела;
- `aether` - щиты, Reality Burn, аномальные тела;
- `kinetic` - stagger, aim punch, пролом.

Биом может усиливать или глушить импульсы, но базовый бой строится на Frame, конкретной батарее, позиции и окне добивания. Если стихии останутся только в лоре, эти поля все равно работают как описания статусов и окружения, не как обязательная отдельная прогрессия.
