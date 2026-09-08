# Milestone — Weapon Set, Inputs, Aim & Battery Cycle

**Дата:** 2026-09-08  
**Статус:** authoritative pre-canon milestone.

## Boundary guardrails

Target UX не строится на:

- universal lead/support layer;
- modal support как базовой dual-wield grammar;
- внутреннем selected-weapon layer внутри уже активной dual Set;
- `RMB = Aim` как универсальном ranged contract;
- per-shot battery packet accounting.

Эти ограничения защищают единый Set/input contract от возврата нескольких перекрывающихся control layers.

---

# 1. Weapon Set

Weapon Set — подготовленная полная конфигурация двух hand slots.

```
WEAPON SET A
[ hand slot 1 ] [ hand slot 2 ]

WEAPON SET B
[ hand slot 1 ] [ hand slot 2 ]
```

Допустимые конфигурации:

```
1H + empty
1H + 1H
2H occupying both hand slots
```

Примеры:

```
SET A
[ sword ] [ pistol ]

SET B
[──── condenser_2h ────]
```

или:

```
SET A
[ pistol ] [ pistol ]

SET B
[──── reach_line_2h ────]
```

## Why Set is the player-facing unit

Weapon Set — это не «selected main weapon + secondary inventory object». Это **уже подготовленная конфигурация двух рук**.

Если внутри dual-set добавить ещё один selected-weapon layer, появляются две разные операции с похожим смыслом:

```
Switch Set
vs
select another held weapon
```

и одна из двух вещей в руках снова превращается в support/quick-slot.

В целевой модели оба 1H ItemID уже входят в immediate decision-space; выбор делается действием через соответствующий channel.

Set therefore owns configuration, not moveset. Конкретные действия по-прежнему принадлежат Pattern/Action.

---

# 2. Switch Set

`Switch Set` меняет **всю** конфигурацию рук.

Он не означает:

```
inside sword+pistol
→ select pistol instead of sword
```

Пистолет уже является частью активной Set.

Переключение:

```
dual → dual
dual → 2H
2H → dual
single → 2H
2H → single
```

использует один общий physical transition contract.

## Set transition is a physical procedure

Switch не должен быть телепортацией inventory state. Реализация должна иметь причинную последовательность:

```
request new Set
→ wait for / reach allowed release point
→ free required hand claims
→ stow/drop old ItemIDs as authored
→ retrieve new ItemIDs
→ establish required grips/presentation
→ new operations become eligible
```

Разные конфигурации могут иметь разные timings. Но outstanding Action debt, Heat, magazine и condition не исчезают из-за смены Set.

---

# 3. Action channels

Базовые непосредственные weapon inputs:

```
LMB → Action Channel 1
RMB → Action Channel 2
```

Это каналы активной Weapon Set, а не универсальные понятия `attack` и `block`.

## Why two channels

Два канала дают одну устойчивую grammar для трёх конфигураций:

```
single 1H
→ one Pattern may use both

dual 1H
→ each Pattern gets one immediate Primary

2H
→ one Pattern may use both
```

Это позволяет не вводить отдельные combat control schemes для single, dual и 2H. При этом channel сам ничего не знает о `attack`, `block`, `shot` или `tool use`: смысл определяет назначенная операция Pattern.

---

# 4. Single 1H

Если в Set один рабочий 1H Pattern:

```
LMB → Primary
RMB → Alt, если он существует
```

Не каждый Pattern обязан иметь Alt.

Пустой второй channel не требует выдуманного действия.

---

# 5. Dual 1H

Если Set содержит два 1H Pattern:

```
LMB → Primary hand-slot Pattern A
RMB → Primary hand-slot Pattern B
```

Оба предмета действительно входят в непосредственное decision-space.

Базовая dual grammar **не предоставляет автоматически независимые Alt обоих Pattern**.

Это естественный компромисс:

```
single Pattern
→ Primary + possible Alt

dual Pattern A + Pattern B
→ Primary A + Primary B
```

## Price of dual-wield

Dual не нуждается в искусственном `offhand penalty`, потому что у него уже есть структурная цена: player input budget делится между двумя непосредственными Primaries.

Он покупает:

- два разных immediate tools;
- более широкий decision-space без Set switch;
- независимые device states.

Он отдаёт:

- мгновенный доступ к optional Alt обоих Pattern;
- специализированную двухручную физическую работу.

Не каждый Pattern обязан быть хорошим dual partner. Если его identity критически зависит от Alt, это содержательное свойство Pattern, а не повод расширять universal input grammar.

---

# 6. 2H

Один 2H ItemID занимает оба hand slots.

Управление:

```
LMB → Primary
RMB → Alt, если Pattern его имеет
```

То есть 2H использует ту же Set-модель, а не отдельную UX-парадигму.

---

# 7. Aim

**Left Alt = Aim.**

Финальное разделение:

```
Aim != Alt
Aim != Primary
Aim != Fire
```

Aim — отдельное стабильное player intent.

## Why Aim is separate from Alt

Aim вынесен в отдельный input не ради добавления ещё одной кнопки, а чтобы сохранить две независимые вещи:

1. **Alternative Application** Pattern остаётся настоящей альтернативной операцией и не обязана быть прицелом.
2. Перестановка предмета внутри mixed dual-set не отнимает у ranged Pattern фундаментальную capability.

Если Aim снова живёт на `RMB`, то:

```
single pistol
→ RMB = Aim

sword + pistol
→ RMB needed for pistol Primary
→ Aim disappears or requires special-case
```

Отдельный `Left Alt` устраняет эту асимметрию.

---

# 8. Aim не универсален

Не всё ranged оружие обязано поддерживать Aim.

Не всё оружие вообще имеет осмысленную Aim operation.

Pattern явно определяет:

```
supports Aim?
what physical preparation does Aim perform?
```

Примеры возможны:

```
pistol → sight / stabilize
rifle → establish precise line
another ranged Pattern → Aim unsupported
```

Не вводить искусственный Aim ради category symmetry.

## Aim is preparation, not a category tax

Aim имеет смысл только там, где конструкция действительно умеет перейти в отдельную подготовленную стрелковую организацию. Поэтому два ranged Pattern могут честно различаться:

```
ranged A
→ supports Aim

ranged B
→ immediate / charge / area / mechanical grammar without Aim
```

Не-Aim ranged не является автоматически «хуже». Он должен покупать другой способ действия, а не просто терять кнопку.

---

# 9. Alt тоже не универсален

Не всё оружие должно иметь Alternative Application.

Разделение окончательное:

```
Primary
optional Alt
optional Aim
```

Это три разные ответственности.

Нельзя считать Aim просто разновидностью Alt ради раскладки кнопок.

---

# 10. Aim не означает Fire Commitment

Для обычного ranged Pattern:

```
hold Left Alt
→ present / sight / stabilize / observe

Primary
→ decide to fire
```

Игрок может:

```
Aim
→ observe
→ track
→ release Aim
```

не принимая обязательство будущего выстрела.

Commitment начинается там, где его определяет конкретный Action.

## Deterministic fire principle

Для обычного aimed ranged weapon подготовка и решение о выпуске разделены:

```
Aim
→ establish / improve line

Primary press
→ explicit decision to fire now
```

Это позволяет наблюдать и сопровождать цель без «зажатого будущего выстрела».

Hold→release остаётся допустимым там, где удержание **физически создаёт подготовленный выпуск**. То есть control grammar должна следовать устройству, а не наоборот.

---

# 11. Compact pistol

Если обычный pistol Pattern поддерживает Aim, то в dual Set:

```
[ sword ] [ pistol ]

LMB → sword Primary
RMB → pistol Primary
Left Alt → pistol Aim
```

`RMB` без Aim может быть быстрым / плохо подготовленным / «шальным» выстрелом согласно физике Pattern.

Это не должно автоматически означать скрытый accuracy dice penalty.

Разница должна читаться через:

- положение оружия;
    
- line preparation;
    
- stabilization;
    
- geometry;
    
- timing.
    

---

# 12. Mixed pair symmetry

Обратная конфигурация:

```
[ pistol ] [ knife ]

LMB → pistol Primary
RMB → knife Primary
Left Alt → pistol Aim
```

Таким образом:

```
knife+pistol
pistol+knife
```

различаются каналом/физическим положением предмета, но не искусственной потерей Aim.

Нет universal `main/offhand effectiveness penalty`.

---

# 13. Dual ranged

Для:

```
[ pistol A ] [ pistol B ]
```

базово:

```
LMB → Primary A
RMB → Primary B
Left Alt → Aim/preparation для поддерживающих её ranged operations
```

Два устройства:

- имеют независимые magazines;
    
- независимый Heat;
    
- независимое technical recovery;
    
- независимое condition.
    

Но Action-owned bodily Recovery остаётся общим ограничением Пешки.

## One body, one current aiming organization

Dual ranged не означает две независимые камеры/две независимо сопровождаемые цели. Aim выражает текущую стрелковую организацию Пешки, а конкретный channel выбирает, какой поддерживающий Aim Pattern выполняет Primary.

Каждый ItemID всё равно проверяет собственную:

- muzzle/geometry;
- readiness;
- magazine;
- Heat/device state;
- eligibility.

Это сохраняет симметрию двух пистолетов, не превращая dual в два независимых shooter agents.

---

# 14. Shields / combat accessories

Если позже появляются:

- shield;
    
- buckler;
    
- combat tool;
    
- focus;
    
- иной hand-slot боевой аксессуар,
    

он не получает отдельный universal input layer.

В dual Set:

```
[ sword ] [ shield ]

LMB → sword Primary
RMB → shield Primary
```

Что именно делает shield Primary — ответственность его Pattern/operation.

---

# 15. Hold → release weapons

Контракт:

```
hold Primary
→ prepare
release
→ effect
```

не является общей pistol grammar.

Он допустим, если реальная конструкция включает:

- charge;
    
- cocking;
    
- tension;
    
- accumulation;
    
- controlled release.
    

Input следует физике оружия.

Физика оружия не придумывается ради экономии кнопки Aim.

---

# 16. Final combat input vocabulary

Базовый contract:

```
LMB       → Action Channel 1
RMB       → Action Channel 2
Left Alt  → Aim
R         → Reload / weapon-energy service intent
Switch Set→ сменить Weapon Set целиком
Q / E     → Profile actions
```

Точная клавиша `Switch Set` не является частью архитектуры этого milestone.

## Q/E and hand claims

Q/E имеют отдельные player inputs, но не являются универсально «бесплатными поверх оружия». Каждая конкретная Profile Action объявляет собственные operation requirements и должна уважать outstanding Action claims.

То есть архитектура не вводит общих правил:

```
Q always requires free hand
E always ignores weapon commitment
Q/E always executable during Recovery
```

Конкретная способность может требовать руку, позу, источник, presentation или наоборот не требовать их — это принадлежит её Action contract.

## Input intent binding

> **Уже начатый input и буферизованное намерение относятся к конкретной операции и конкретному получателю. Изменение Weapon Set, состояния предмета или назначения channel не переинтерпретирует старый input как новую атаку, выстрел, Aim или Reload. Удерживаемая кнопка не запускает автоматически операцию предмета новой Set.**

Точные buffering windows остаются prototype-bound.

Недопустимое поведение:

```
press/hold LMB on Set A
→ switch to Set B
→ old input fires Set B weapon
```

## Input semantics acceptance test

Смена контекста может сделать исходное намерение невозможным, но не должна делать его **другим намерением**. Это относится к:

- Set switch;
- depletion;
- loss of Aim support;
- hand reorganization;
- temporary inability during Recovery.

Если действие не может выполниться, система должна дать понятный cancel/failure/no-op outcome согласно operation contract, а не отложенно запускать уже другое действие после изменения контекста.

---

# 17. Battery model

Для ranged weapon батарея **не является магазином**.

У weapon ItemID есть собственный внутренний magazine.

Батарея является физическим источником его зарядки, а не отдельным ресурсом `Battery Charge`.

## Why battery and magazine are separate

Они работают на разных масштабах решения:

```
Full Battery ItemID
→ coarse expedition / preparation resource

Weapon magazine
→ fine-grained local combat resource
```

Разрядка батареи переводит одну физическую единицу подготовленного энергетического ресурса в полный operational reserve конкретного recipient. После транзакции отдельные выстрелы принадлежат grammar оружия и его magazine, а не батарейной бухгалтерии.

Это намеренно исключает:

- per-shot battery routing;
- shared hidden ammo pool;
- partial energy refund;
- leftover impulse accounting;
- weapon-switch arbitrage над общей энергией.

## Canonical battery lifecycle

```
Full Battery ItemID
→ atomic discharge
→ Drained Cell ItemID
```

**Одна Full Battery допускает ровно одну энергетическую транзакцию.** После неё тот же физический ItemID является Drained Cell. Частичной разрядки и внутреннего счётчика charges нет.

Для ranged weapon:

```
Full Battery ItemID
→ reload transaction
→ Drained Cell ItemID
+
recipient weapon magazine = Capacity
```

При capacity = 8:

```
0/8 → 8/8
3/8 → 8/8
7/8 → 8/8
```

Во всех случаях расходуется одна целая Full Battery ItemID: она становится Drained Cell, а magazine ровно одного получателя пополняется до Capacity.

---

# 18. Остаток магазина

Остаток:

- не возвращается в батарею;
    
- не снижает цену зарядки;
    
- не создаёт residual charge или partial battery refund;
    
- не переносится в другой consumer.
    

Дозарядка сознательно может быть неэффективной:

```
7/8
→ fully drain one Full Battery ItemID
→ 8/8
```

Это решение игрока.

## Reload economy

Полное пополнение независимо от остатка создаёт простой риск/цену решения:

```
reload early
→ buy immediate readiness
→ waste remaining magazine value

wait
→ preserve battery efficiency
→ accept lower current reserve
```

Эта цена должна быть читаема без дробной энергетической арифметики. Батарея остаётся дискретным ItemID, magazine — дискретным локальным запасом оружия.

---

# 19. Weapon firing

После зарядки энергия находится в operational magazine конкретного ItemID.

Обычный выстрел:

```
1 shot
→ 1 magazine round
```

если конкретная Pattern emission grammar явно не определяет другой authored расход.

Weapon magazine является runtime состоянием конкретного ItemID.

---

# 20. Reload transaction

Общий battery invariant действует и для weapon reload, и для battery-powered Q/E.

До commit:

```
Battery = Full
recipient/result unchanged
```

После commit:

```
Battery = Drained Cell
result applied atomically
```

Для weapon reload результат:

```
magazine = Capacity
```

Для battery-powered Q/E:

```
ability activation receives required energy
```

Не вводить промежуточные half-drained battery, partial charge, leftover impulse, stranded remainder или packet queue. Батарея не уничтожается: после commit остаётся физический Drained Cell ItemID.

---

# 21. Q/E battery consumption

Если конкретная Q/E является battery-powered:

```
Full Battery ItemID
→ ability activation
→ Drained Cell ItemID
```

> **Q/E fully drains exactly one physical Full Battery ItemID согласно ability contract.**

Она не:

- стреляет патроном weapon magazine;
    
- забирает часть магазина оружия;
    
- превращает оружейный reload в ability payment.

Она также не использует абстрактный `Battery Charge`, не оставляет частично заряженную батарею и не уничтожает ItemID. После операции остаётся физический Drained Cell ItemID.
    

Weapon magazine и battery-powered Profile Action — разные consumers.

## Why Q/E fully drains the physical battery

Battery-powered Profile Action не должна незаметно использовать тот же мелкозернистый weapon-ammo accounting. Её authored contract принимает **целую Full Battery ItemID** как цену активации и после commit оставляет Drained Cell.

Это сохраняет одну физическую модель батареи:

```
Full
→ one atomic energy transaction
→ Drained
```

при разных получателях результата.

---

# 22. Dual ranged reload

Для:

```
A magazine
B magazine
```

`R` является отдельным reload intent.

Базовая working policy:

> **R выбирает наиболее истощённый eligible ranged weapon активной Set.**

Пример:

```
A heavily depleted
B partially depleted

R
→ choose most depleted eligible ranged recipient in active Set
→ perform its reload
→ Full Battery becomes Drained Cell
→ A magazine becomes Full
```

После завершения:

```
A full
B partially depleted

R
→ reload B
```

Повторное `R` заново вычисляет recipient по текущему состоянию. Если второй ствол ещё неполный, он обычно становится следующей целью.

Каждое успешное пополнение:

```
one Full Battery ItemID
→ Drained Cell ItemID
+
one recipient magazine = Capacity
```

## Why reload selects one recipient per press

`R` выражает одно намерение обслуживания, а не команду «восстановить весь loadout». Поэтому dual ranged сохраняет два независимых weapon reserves и две реальные транзакции.

Первый `R` выбирает одного recipient по детерминированной политике. После завершения второй `R` заново оценивает состояние.

Не буферизовать случайный double-tap как обязательство сжечь две батареи подряд без нового подтверждённого reload intent. Точные input-buffer правила prototype-bound, но дорогое второе потребление не должно возникать из неясной очереди.

---

# 23. Что значит «наиболее истощённый»

Точный comparator остаётся prototype-bound:

- remaining fraction;
    
- missing fraction;
    
- иной простой deterministic comparator.
    

Не превращать это в скрытую AI-оптимизацию.

Policy должна быть:

- deterministic;
    
- понятной;
    
- стабильной;
    
- видимой игроку.
    

Tie-break также prototype-bound, но фиксированный.

## Selection policy acceptance test

Игрок должен быть способен предсказать цель `R` **до** расхода батареи по видимому состоянию. Если policy требует помнить историю последних выстрелов или скрытые приоритеты rarity/slot, она слишком умна для базового reload intent.

При необходимости будущий UI может дать явный способ адресного обслуживания, но это не должно быть обязательным условием нормальной dual reload grammar.

---

# 24. Full feedback

Если оба eligible magazines полны:

```
R
→ FULL
```

Никакая батарея не расходуется.

Если один полный, другой нет — целью является неполный.

---

# 25. Depletion не переназначает controls

Если:

```
A empty
B loaded
```

то:

```
A channel → empty feedback
B channel → B Primary
```

Игра не должна:

- автоматически стрелять B вместо A;
    
- автоматически менять Weapon Set;
    
- превращать attack input в Reload;
    
- перераспределять channel.
    

---

# 26. Reload / service physics

Не канонизировать универсально:

```
reload always requires exactly two hands
```

Конкретная reload/service operation должна объявлять:

```
recipient
battery source
required manipulation
hand claims
equipment/interface requirements
Commitment / Recovery
transaction commit point
```

Обычная ручная процедура может требовать освободить вторую руку.

Но это следствие конкретной физической процедуры, а не абстрактное правило `dual ranged reload penalty`.

## Service is not Action Recovery or device recovery

Не смешивать:

```
Action Recovery
→ долг уже совершённого combat action

Device technical cycle
→ cooling / mechanism / vent

Magazine depletion
→ локальный запас recipient

Reload/service
→ новая физическая операция над recipient + source
```

Одна из этих систем не должна автоматически обнулять другую. Это особенно важно для dual ranged, где разные device cycles существуют параллельно, но reload остаётся отдельным обязательством.

## Service readability

Игрок должен понимать:

- какой recipient обслуживается;
- какая Full Battery будет разряжена;
- в какой момент транзакция стала необратимой;
- какие руки/поза заняты;
- почему операция сейчас невозможна или прервана.

Противнику не обязательно видеть inventory accounting, но существенное vulnerability window процедуры должно иметь физический tell.

---

# 27. Thermos / equipment interaction

Thermos или другое оборудование может изменить reload/service procedure только если реально предоставляет:

- physical mount;
    
- feed;
    
- routing interface;
    
- stabilization;
    
- удержание recipient;
    
- другой причинный способ выполнить операцию.
    

Не существует абстрактной «третьей руки».

Не использовать общий `reload speed +X%` как замену физической причинности, если эффект должен менять саму процедуру.

---

# 28. Device cycles

Reload не сбрасывает автоматически:

- Heat;
    
- technical Recovery;
    
- Vent;
    
- damage;
    
- Action-owned bodily Recovery.
    

Два ranged ItemID могут честно перекрывать локальные technical cycles.

Например:

```
A fired
→ Pawn bodily Recovery ends
→ A still cooling
→ B technically ready
→ B may act
```

Это нормальная ценность dual ranged.

---

# 29. Switch Set state preservation

`Switch Set` не является Reload.

При Set transition сохраняются ItemID states:

```
magazine
Heat
condition
device state
```

Recovery предыдущего Action также не стирается.

## Set-switch exploit tests

Switch Set не должен позволять:

- скрыть empty magazine через автоматическое переназначение channel;
- сбросить Heat/technical debt;
- отменить protected bodily Recovery;
- получить бесплатный reload;
- сохранить старый buffered attack и выполнить его новым ItemID.

При этом Switch не должен быть искусственно запрещён дольше, чем требуют реальные Action claims и физическая перестройка.

---

# 30. Weapon Set trade-off

Главная UX-асимметрия:

```
single / 2H Pattern
→ immediate Primary + optional Alt

dual 1H
→ immediate Primary A + Primary B
```

Aim существует независимо и только у Pattern, которые его поддерживают.

Это даёт dual-wield содержательную цену без:

- universal damage penalty;
    
- hidden offhand stat;
    
- pair catalogue;
    
- removal of Aim.

## Representative UX acceptance cases

Перед массовой миграцией проверить минимум:

### Single 1H melee

```
LMB → Primary
RMB → Alt if authored
Left Alt → no effect unless Pattern supports Aim for a real reason
```

### Sword + pistol

```
LMB → sword Primary
RMB → pistol Primary
Left Alt → pistol Aim if supported
```

### Pistol + knife

```
LMB → pistol Primary
RMB → knife Primary
Left Alt → pistol Aim if supported
```

Две mixed конфигурации должны быть симметричны по фундаментальным capabilities Pattern.

### Pistol + pistol

```
LMB → pistol A
RMB → pistol B
Left Alt → shared aiming organization for supported ranged operations
R → one deterministic reload recipient
```

Пустой A не переназначает LMB на B.

### 2H ranged

```
LMB → Primary
RMB → authored Alt if present
Left Alt → Aim only if Pattern supports it
```

2H не должен терять свой Alt только потому, что ranged category существует.

### Shield / combat accessory

```
[sword][shield]
→ two immediate Primaries through the same channel grammar
```

Не требуется отдельная shield control subsystem.

### Hold→release Pattern

Работает только если preparation/release физически является частью конструкции; early release/cancel не должен оставлять скрытый future-fire intent.

## Milestone falsification

Milestone требует пересмотра, если implementation вынуждает:

- выбирать «активное оружие» внутри уже активной dual Set;
- отнимать Aim у Pattern из-за того, что он находится во втором hand slot;
- использовать RMB одновременно как universal Aim и второй weapon channel;
- автоматически выдавать Alt каждому Pattern ради заполнения кнопки;
- автоматически reload-ить оба dual weapons одной батареей;
- возвращать partial battery value при непустом magazine;
- использовать shared hidden ammo pool между ItemID;
- обходить Action debt через другой channel или Set switch.

---

# Milestone principle

> **Weapon Set — это целая подготовленная конфигурация двух рук. LMB/RMB являются двумя action channels этой конфигурации: один Pattern может использовать их как Primary/Alt, а два 1H Pattern — как Primary/Primary. Left Alt является отдельным Aim intent и не смешивается с Alt. Одна Full Battery ItemID полностью разряжается в Drained Cell и пополняет magazine одного ranged ItemID до Capacity; dual reload последовательно обслуживает конкретные истощённые recipients, не меняя weapon channels и не обходя физическую процедуру.**
