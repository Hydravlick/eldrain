# Milestone — Pawn Causality & Build Ecology

**Дата:** 2026-09-08  
**Статус:** authoritative pre-canon milestone.

## Boundary guardrails

Target architecture не вводит `Chassis` как mega-owner, отдельную универсальную `Service Aptitude` без собственной причинной модели и обязательную Passive только ради симметрии профилей. Эти понятия допустимы лишь если позже появится самостоятельная ответственность, которую невозможно честно выразить текущими owners.

---

# 1. Исходная задача

Исследование началось с Personal Traits:

> Как сделать конкретную смертную Пешку механически значимой и отличимой через gameplay, не превращая Eldrain в каталог bespoke-исключений?

Желаемая причинность:

```
personal property
→ common capability / state
→ changed opportunity value
→ different player decision
```

Нежелательная:

```
Trait
→ special Weapon callback
→ special Biome callback
→ special Quest callback
→ special Module callback
→ ...
```

Но затем Reference Note об экономике подготовки расширил задачу.

Выяснилось, что даже выразительная в поле Пешка остаётся механически слабой концепцией, если её конкретная жизнь не меняет:

- подготовку;
    
- материалы;
    
- работу;
    
- маршрут;
    
- риски;
    
- будущие возможности.

## Research target

Успех этой архитектуры определяется не количеством персональных модификаторов, а тем, создаёт ли она **разные разумные планы игры**.

Проверка должна проходить сразу на нескольких масштабах:

```
Micro
→ как человек исполняет действие сейчас

Meso
→ как из-за него меняется build / preparation / route / cargo

Macro
→ какие работы и результаты становятся рациональными
```

Допустимо, что конкретная Пешка сильна на одном масштабе и слаба на другом. Combat-weak специалист может быть ценным в preparation/work; сильный боец может не открывать особых экономических возможностей. Архитектура не должна сводить эти виды ценности в один универсальный рейтинг.

Главный критерий разнообразия:

> **ценнее несколько качественно разных стратегий, чем большое число комбинаций, которые ведут к одному и тому же оптимальному решению.**

---

# 2. Две неудачные крайности

## Expressive Pawn

Пешка имеет:

- историю;
    
- раны;
    
- отношения;
    
- Traits;
    
- характерные боевые свойства;
    

но её замена на другого человека почти не меняет решения игрока.

Это:

> expressive but mechanically shallow Pawn.

---

## Valuable Pawn / Keeper

Конкретная Пешка предоставляет сильное преимущество только пока она жива:

```
Pawn alive
→ valuable economic/service opportunity

Pawn lost
→ opportunity disappears
```

Рациональный игрок начинает:

- парковать;
    
- морозить;
    
- не рисковать;
    
- использовать человека как пассивный экономический актив.
    

Это Keeper problem.

---

# 3. Consequential Life

Главный causal turn:

> **Пешка не является контейнером ценности. Пешка является причиной преобразования ценности.**

Целевая цепочка:

```
concrete Pawn
→ special way/opportunity to act
→ changed preparation/material/route/risk
→ completed work
→ achieved result
→ result can continue under its own owner
```

Передаётся:

> **результат работы, а не уникальность человека.**

## Three layers of Pawn value

### 1. Personal / embodied value

То, что принадлежит конкретной Пешке и действительно теряется вместе с ней:

- body/morphology;
- scars/mutations/current condition;
- Field Profile;
- Personal Traits;
- Pawn↔Frame Proficiency;
- персональные способности и знания там, где они действительно embodied;
- конкретные личные связи и состояния.

Universal `Mastery` не возвращается.

```
death
→ personal / embodied value LOST
```

### 2. Active opportunity / ongoing work

То, что конкретная Пешка сейчас делает возможным или рациональным через пересечение:

```
Pawn capabilities
× work requirements
× preparation
× materials
× environment
× current world state
```

Это может быть ещё не начатая возможность, ongoing project, нестандартная процедура, цепочка подготовки или работа на несколько рейдов. Это не permanent progression и не passive living bonus.

```
death
→ active opportunity / unfinished work RE-EVALUATE
```

Работа может стать невозможной, дороже, продолжимой другим способом, требующей другого человека или временно зависшей. Она не обязана просто исчезнуть.

Не создавать `PawnOpportunityList` как новый mega-owner.

### 3. Externalized achieved result

То, что уже было реально создано или доказано действием:

- ItemID;
- вынесенный материал;
- подтверждённый факт;
- completed obligation;
- изготовленный результат;
- иная законченная externalized consequence.

```
personal capability
→ performed work
→ externalized result
```

Результат не становится бессмертным. Он становится **причинно независимым от дальнейшей жизни автора**. После этого его судьбой владеет соответствующий owner результата.

Смерть Пешки сама по себе не должна:

```
destroy ItemID
erase established fact
reverse completed obligation
erase delivered result
```

Но результат может быть позже потрачен, уничтожен, украден, устареть или потерять ценность по собственным правилам.

### Acceptance principle

> **Ценность конкретной Пешки должна преимущественно реализовываться через meaningful work, commitment, opportunity cost и действие, а не через простое сохранение её живого статуса.**

Это не означает, что вся ценность обязана реализовываться в combat/raid. Допустимы workshop work, preparation, research, negotiation, analysis, training и field procedures.

Проблемой является модель:

```
keep Pawn alive and parked
→ receive passive value indefinitely
```

## Death as an ownership test

Смерть — полезный диагностический тест для всей системы ценности:

```
personal / embodied value
→ LOST

active opportunity / unfinished work
→ RE-EVALUATE

externalized achieved result
→ NOT REVERSED BY DEATH ITSELF
```

Это не означает, что любой достигнутый результат permanent. Он может исчезнуть по законам своего owner. Проверяется только причинность: **смерть автора не должна откатывать уже совершённое действие без отдельной причины мира.**

Три слоя выше — player-facing модель ценности. Четыре ответственности ниже — owner-facing декомпозиция состояний и результатов. Они описывают одну причинную систему с разных сторон и не являются конкурирующими классификациями.

---

# 4. Четыре разных ответственности

Не смешивать:

## Living-person opportunity

То, что конкретная Пешка способна делать сейчас благодаря:

- телу;
    
- полевому профилю;
    
- личным свойствам;
    
- знаниям;
    
- отношениям;
    
- текущему состоянию.
    

---

## Unfinished work

Проект, обязательство или процесс, для которого работа ещё не завершена.

Это не постоянный бонус Пешки и не готовый account reward.

---

## Achieved result

То, что уже было реально достигнуто действиями.

Результат может быть:

- физическим предметом;
    
- материалом;
    
- подтверждённым знанием;
    
- выполненным обязательством;
    
- изменением мира;
    
- конечным рабочим результатом.
    

Он может продолжать существовать независимо от автора, если его природа это допускает.

---

## Life Closure

Отвечает за окончание полевой жизни Пешки.

```
completed work
!=
Closure reward
```

Closure не должна означать:

```
grow Pawn
→ retire Pawn
→ mint permanent account power
```

`work result != retirement reward`.

---

# 5. Главный Build Ecology test

Архитектура должна поддерживать:

```
WHO THIS PERSON IS
→ HOW THEY CAN ACT DIFFERENTLY
→ HOW THAT CHANGES BUILD / PREPARATION
→ HOW THAT CHANGES RAID DECISIONS
→ WHAT THEY CAN ACHIEVE
→ HOW THAT CHANGES THE NEXT GAME
```

Если существует только верхняя половина:

> выразительная, но механически мелкая Пешка.

Если нижняя часть существует только пока Пешка хранится живой:

> Keeper / frozen economic asset.

## Build Ecology is a decision ecology, not a combo graph

Build Ecology считается глубокой не тогда, когда можно перечислить много связок, а когда разные свойства меняют **relative value** уже существующих решений:

```
same obstacle
+ different Pawn / equipment / preparation
→ different best route, tool, cargo, timing or accepted risk
```

Хорошая связь обычно проходит через общий факт:

```
source property
→ shared physical / informational / capability state
→ consumer evaluates it by its own rule
```

Плохой симптом:

```
System A asks: "is exact Trait X present?"
System B asks: "is exact Weapon Y equipped?"
System C asks: "is exact Biome Z active?"
```

Такой graph масштабируется только ручным контентом и делает каждую новую сущность зависимой от каталога соседей.

## Strategy-space acceptance tests

Build Ecology должна выдерживать следующие проверки:

- **Trait-free depth:** meaningful build и preparation существуют без Personal Traits.
- **Same-profile divergence:** две Пешки одного Field Profile без Traits могут рационально собраться по-разному за счёт Body, Weapon Set, Thermos/modules, ресурсов и задачи.
- **No universal winner:** один Weapon/Module/защита не должен доминировать по всем релевантным аспектам.
- **Signature build is allowed:** устойчиво сильная личная связка допустима, пока её ценность зависит от ситуации и не превращается в единую моновалюту эффективности.
- **No universal Power Score:** сравнение разных билдов не обязано сводиться к одному числу.
- **No Build Manager:** никакая отдельная сущность `Build` не получает право централизованно переписывать правила владельцев.

---

# 6. Race × Spec / Field Profile

`Race × Spec` — authored field profile/framework.

Он нужен для:

- узнаваемости;
    
- authored направления;
    
- базовых возможностей;
    
- устойчивого игрового каркаса.
    

Он не является:

- готовым build;
    
- mega-owner всей Пешки;
    
- контейнером всех её свойств.
    

Игра должна быть содержательной уже на уровне:

```
Field Profile
+ Weapon
+ Body
+ Equipment
+ Environment
```

без Personal Traits.

## Profile recognizability vs build freedom

Race × Spec намеренно остаётся authored package: игрок должен узнавать общий способ существования профиля, даже когда конкретные сборки различаются.

При этом профиль не должен диктовать единственную экипировку. Body и Profile могут:

- делать часть решений естественно выгоднее;
- ограничивать физическую совместимость;
- задавать гарантированные способности;
- создавать устойчивые предпочтения.

Но итоговая сборка должна оставаться следствием конкретной задачи и доступных вещей.

Нежелательный результат:

```
Race × Spec
→ deterministic best Weapon
→ deterministic best Thermos
→ deterministic module package
```

В таком случае authored profile незаметно становится готовым класс-билдом.

---

# 7. Passive / Q / E

## Passive

P / Passive — это Trait той же сущности и той же rule grammar, что и Personal Trait. P является deterministic Chassis Trait: он authored и гарантирован Race × Spec / Field Profile. Personal Trait является недетерминированным свойством конкретной Пешки.
Разница между ними — в источнике и детерминированности, а не в механической природе правила.
Поэтому P и Personal Traits не требуют двух отдельных effect engines, interaction grammars или систем исполнения.

Не требуется создавать отдельную универсальную effect-систему только потому, что правило называется Passive.

---

## Q / E

Q/E — authored активные возможности Field Profile.

Они ближе к reusable utility/actions, чем к обязательной DPS-ротации.

Предпочтительно:

```
Q/E
→ create/use general situation
→ Weapon / Environment / other owner reacts according to own rules
```

а не:

```
Q
→ exact named Weapon gets bespoke bonus
```

Жёсткий запрет на weapon interaction не нужен.

Запрещена именно зависимость от bespoke pair catalogue.

## Profile actions are not a mandatory rotation

P/Q/E не обязаны образовывать боевой цикл вида:

```
P enables Q
→ Q primes E
→ E resets P
```

Их ценность может быть пространственной, подготовительной, ситуационной или процедурной. Хороший Profile остаётся узнаваемым, даже если игрок сознательно долго не нажимает Q/E.

Это важно для Weapon autonomy: оружие не становится mere delivery mechanism для class rotation, а Q/E не обязаны знать точный Weapon Pattern.

Если способность использует батарею или иной физический ресурс, энергетический контракт принадлежит самой операции и соответствующей resource system; Field Profile не должен дублировать inventory accounting.

---

# 8. Weapon

Weapon является самостоятельным крупным источником поведения.

> **Оружие в руках Пешки является боевым архетипом.**

Оно должно менять:

- дистанцию;
    
- геометрию;
    
- commitment;
    
- окна;
    
- counterplay;
    
- риск;
    
- способ исполнения задачи.
    

Подробный authoritative contract определён в отдельном Weapon Architecture milestone.

---

# 9. Personal Traits

Personal Traits — дополнительный roguelike-слой индивидуальности. Personal Trait использует ту же rule grammar, что и P. P — deterministic Chassis Trait; Personal Trait — недетерминированный Trait конкретной Пешки.

Игра должна быть глубокой **без них**.

Trait:

- относится к конкретной жизни;
    
- преимущественно не выбирается как обычный build perk;
    
- может быть положительным, отрицательным или контекстным;
    
- может заставить перестраивать уже существующую сборку;
    
- не обязан создавать ability button.
    

Рабочая формулировка:

> **Trait — комбинаторика интересных сценариев или правил, в которые приходится влиться.**

Trait не является universal build-script controller.

Предпочтительный принцип:

```
Trait
→ human property / capability / physical relation
→ existing system evaluates consequence
```

```
TRAIT RULE GRAMMAR
├─ P / Passive
│  └─ deterministic Chassis Trait
│     authored by Race × Spec
│
└─ Personal Trait
   └─ non-deterministic
      belongs to concrete Pawn
```

## Pawn information boundary

> **Информационная доступность свойства определяется тем, чьё решение оно меняет. Владелец может знать личное свойство напрямую; союзнику нужна информация, необходимая для координации. Противнику не обязательно знать Trait, профильную причину или численное значение свойства — но если наблюдаемый результат меняет требуемый от него непосредственный ответ, соответствующее действие или состояние должно дать своевременный читаемый tell. Влияние только на preparation, маршрут, экономику или ценность возможностей само по себе не требует enemy-facing telegraph.**

Trait Grammar будет определена после weapon migration.

## Trait strength budget

Traits могут быть сильными. Ограничение не в размере эффекта, а в **форме ответственности**.

Допустимо, что Trait:

- существенно меняет ценность уже существующего Weapon Frame;
- делает определённые environment states привлекательнее или опаснее;
- меняет отношение Пешки к физическому состоянию;
- повышает или понижает Frame Proficiency через явно определённую semantic transition;
- создаёт новую проблему, вокруг которой приходится перестраиваться.

Недопустимо, чтобы Trait становился мини-скриптом, который знает каталог конкретных Pattern, Module, Biome и Q/E и вручную переписывает их поведение.

Главная проверка:

> Если удалить все Traits, остаётся ли Eldrain глубокой игрой с различимыми профилями, оружием, оборудованием, подготовкой и средой?

Если нет, Traits используются для латания пустой базовой системы.

---

# 10. Thermos

Сохраняются независимые слои:

```
Body Fit
Thermos Model topology
physical Thermos Instance
Assembly legality/budget
Installed Module ItemIDs
```

## Body Fit

Может ли конкретное тело физически носить модель.

## Thermos Model

Определяет:

- fit envelope;
    
- topology;
    
- mount nodes;
    
- authored physical platform.
    

## Thermos Instance

Конкретный ItemID:

- fit state;
    
- installed modules;
    
- damage;
    
- loss;
    
- physical history.
    

## Assembly budget

Существующий `BaseServiceCapacity` пока остаётся authored profile/assembly budget.

**Не вводить отдельную человеческую Service Aptitude сущность только ради симметрии с Weapon Proficiency.**

Она появится только если существует самостоятельная причинная модель навыка обслуживания.

## Modules

Модули — реальные устанавливаемые вещи/функции.

Не должны self-fund собственную assembly legality.

Trait предпочтительно меняет взаимодействие человека с результатом работы оборудования, а не просто даёт:

```
+1 universal service capacity
```

## Thermos design rationale

Thermos должен оставаться **физическим оборудованием**, а не вторым class-tree. Поэтому разделяются вопросы:

```
Body Fit
→ могу ли я вообще носить эту модель?

Model topology
→ что физически можно установить?

Assembly budget / legality
→ может ли эта конфигурация работать как заявлено?

Installed Module ItemID
→ какие конкретные вещи сейчас установлены и что с ними произошло?
```

Слияние этих слоёв в один `equipment score` уничтожит две важные вещи: физическую понятность сборки и возможность локальных последствий повреждения/утраты конкретного ItemID.

`BaseServiceCapacity` пока остаётся authored budget именно потому, что отдельной модели человеческого навыка обслуживания ещё нет. Создавать `Service Aptitude` заранее означало бы придумать owner без собственной причинной ответственности.

---

# 11. Environment

Biome/Environment предоставляет:

- температуру;
    
- токсичность;
    
- поверхность;
    
- свет;
    
- ingress;
    
- visibility;
    
- material conditions;
    
- signal;
    
- аномальные состояния;
    
- route constraints/opportunities.
    

Environment не должен знать конкретные build IDs.

Подготовка должна позволять:

> хорошо закрыть часть рисков, частично закрыть другие и сознательно оставить некоторые открытыми.

Не нужен ни универсальный RPG Power Score, ни bespoke biome × build matrix.

## Environment as pressure and opportunity

Environment должен не только взыскивать налог за пребывание, но и менять ценность решений. Защита не должна сводиться к обязательной оплате `anti-biome tax`, после которой среда перестаёт существовать как gameplay.

Желаемая структура:

```
environment condition
→ creates pressure / constraint / opportunity
→ preparation changes exposure and available choices
→ player still makes a scene-level decision
```

То есть хорошая подготовка может:

- полностью закрыть отдельный известный риск;
- смягчить другой;
- открыть новый маршрут или процедуру;
- оставить осознанную слабость ради другой выгоды.

Не требуется заранее канонизировать полный список resistance axes. Это отдельная content/system task. Milestone фиксирует только то, что будущие оси должны быть причинными и не схлопываться в один универсальный `resistance score`.

---

# 12. Языки взаимодействия

Не нужен один универсальный Interaction Bus.

Использовать несколько узких доменных языков:

```
physical state
capability
operation requirements
contact/material state
signal/information
provenance/evidence
work/economic contract
```

Принцип:

> Source публикует локальный факт. Appropriate consumer реагирует по собственному закону. Undeclared interaction не существует.

## Interface discipline

Узкий язык должен существовать только там, где есть реальные producer и consumer. Не создавать заранее универсальные словари свойств «на будущее».

Хороший interface отвечает на три вопроса:

1. **Кто публикует факт?**
2. **Кто имеет право его читать?**
3. **Какое решение меняется от этого факта?**

Если третий ответ отсутствует, свойство пока не нужно в общей grammar.

Если один consumer начинает спрашивать десятки exact IDs соседних систем, interface превратился в bespoke callback graph.

---

# 13. Build — derived concept

`Build` не является отдельным runtime owner.

Он является результатом композиции:

```
specific Pawn
+ Field Profile
+ Weapon Set
+ Body
+ Thermos/modules
+ Traits
+ prepared resources
+ current Environment
```

Не создавать отдельный `Build Manager`, который переписывает правила соседних систем.

## Build evaluation principle

Build может быть назван, сохранён как preset или обсуждаться игроком, но системная причинность должна оставаться разложенной по владельцам.

Допустимы emergent signature builds и явно сильные специализации. Они становятся архитектурной проблемой только если:

```
one build property
→ dominates combat + preparation + economy + survivability
→ across most relevant environments
```

То есть проблема не в существовании BiS для локальной задачи, а в **monocurrency**, когда одна ось качества отвечает почти за всё.

---

# 14. Owner boundaries

## Pawn / body / personal facts

Владеют человеческими свойствами и состояниями.

## Field Profile

Владеет authored базовыми возможностями профиля.

## Weapon architecture

Владеет оружейной грамматикой и исполнением оружейных действий.

## Thermos Assembly

Владеет fit/topology/assembly legality.

## Environment

Владеет состояниями мира.

## Work / obligations

Владеют задачей, требованиями и завершённостью работы.

## Economy / result owner

Владеет судьбой достигнутого результата там, где это необходимо.

## Lifecycle / Closure

Владеет окончанием полевой жизни.

Не создавать persistent institutional-rights owner заранее. Только если конкретная будущая система действительно его потребует.

## Ownership collapse tests

При дальнейшей миграции проверить:

- Field Profile не хранит конкретные ItemID и не определяет moveset Weapon Pattern.
- Trait не владеет Environment и не назначает результат Work.
- Thermos Assembly не решает, что считается завершённым проектом.
- Work не копирует уникальную способность Пешки в будущих Пешек.
- Result owner не зависит от `PawnAlive == true`, если результат уже externalized.
- Lifecycle не выдаёт completed-work rewards повторно при Closure.
- Inventory/ItemID custody не превращается в Build Manager.

Если один документ вынужден объяснять правила трёх соседних owners, вероятно, responsibility split снова нарушен.

---

# 15. Что не решается этим milestone

Пока не канонизируются:

- Trait Grammar;
    
- широкая progression-система;
    
- institutional legacy;
    
- exact Closure implementation;
    
- полный environment vocabulary;
    
- массовый content.
    

Следующий dependency:

```
Weapon Architecture migration
→ representative fixtures
→ Trait Grammar
→ mature Build Ecology contract
→ Build Ecology Workbench
→ broader content
```

## Representative Consequential-Life vertical slice

До масштабирования контента архитектура должна выдержать хотя бы один end-to-end slice без bespoke shortcuts:

```
1. конкретная Пешка имеет личное свойство/capability
2. появляется работа или возможность, где оно меняет relative value
3. игрок меняет preparation / equipment / cargo / route
4. в поле возникают иные решения и риски
5. работа либо проваливается, либо завершается
6. завершённый результат получает собственного owner
7. дальнейшая смерть Пешки не отменяет результат автоматически
8. следующая Пешка не получает уникальную capability автора
```

Slice считается проваленным, если для его работы потребовалось добавить special-case ссылку вида `exact Pawn/Trait → exact Quest/Weapon/Biome`, либо если оптимальный способ использовать Пешку — навсегда исключить её из meaningful work.

## Milestone falsification

Milestone требует пересмотра, если representative implementation показывает хотя бы одно из следующего:

- индивидуальность не меняет решений без сюжетного текста;
- ценная Пешка рационально превращается в parked aura;
- achieved result приходится хранить внутри живого Pawn owner;
- Traits необходимы для базовой глубины;
- Field Profile детерминирует готовый build;
- Environment работает только как обязательный resistance tax;
- новые связи требуют роста pair-specific callback graph;
- build quality естественно схлопывается в один общий Power Score.

---

# Milestone principle

> **Конкретная Пешка должна менять ценность решений не потому, что она хранит пассивный бонус, а потому, что её способ действовать меняет подготовку, действия и достижимые результаты. Build Ecology должна обеспечивать эту причинность через независимых owners и общие доменные факты, а не через bespoke graph.**
