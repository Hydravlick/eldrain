# Milestone — Weapon Architecture

**Дата:** 2026-09-08  
**Роль:** design rationale / research synthesis после canon cutover.

**Gameplay authority:** [[05_Combat_Survival/Weapon_Core|Weapon identity]], [[05_Combat_Survival/Registries/Registry_Weapons|publication/schema]], [[05_Combat_Survival/Combat_Three_Debts|Action]], [[04_Player_Entities/Proficiency_Arsenal|Pawn↔Frame]], [[07_Gear_Inventory/Equipment_PaperDoll|Weapon Set]].

Этот документ сохраняет основания решений, failure modes, отвергнутые collapse-модели и acceptance/falsification criteria. Нормативные правила и schema читаются у linked active owners; формулировки исследования не являются второй gameplay authority. Исторические альтернативы ниже объясняют выбор, но не публикуют старую реализацию.

## Boundary guardrails

Target architecture не использует следующие responsibility collapses как базовую модель:

```
Frame owns exact full moveset
random ItemID owns its own hidden moveset
each Frame invents unrelated meaning of Proficiency
universal lead/support layer owns dual-wield
```

Если implementation снова требует одну из этих форм, нужно доказать новую причинную ответственность, а не возвращать её как удобный shortcut.

---

# 1. Центральная декомпозиция

Минимальная оружейная архитектура:

```
Frame
→ Pattern
→ ItemID

Pawn × Frame
→ Proficiency

Pattern + ItemID + Pawn + scene
→ Action
```

Каждая сущность имеет отдельную причину существования.

## Почему нужен именно этот split

Архитектура должна одновременно позволять две вещи, которые конфликтуют при более простом ownership:

1. игрок переносит долговременное знание между родственными оружиями;
2. реальные конструкции внутри этого семейства могут заметно различаться.

Если exact moveset принадлежит Frame:

```
Frame = exact moveset
→ каждый заметно другой moveset требует нового Frame
→ taxonomy дробится до каталога отдельных пушек
```

Если exact moveset принадлежит случайному ItemID:

```
loot instance = new grammar
→ каждую находку надо учить как новый класс
→ archive-memory и PvP unreadability
```

Поэтому:

```
Frame
→ transferable prior

Pattern
→ repeatable concrete construction

ItemID
→ physical runtime history
```

Это не абстрактная чистота данных, а cognitive-load contract.

## Ownership invariant

Одно значимое правило не должно одновременно иметь трёх владельцев. В целевой модели:

- Frame обещает язык и границы;
- Pattern обещает конкретную операцию;
- ItemID сообщает состояние экземпляра;
- Action сообщает состояние уже начатого исполнения;
- Pawn↔Frame Proficiency сообщает качество человеческого владения.

---

# 2. Frame

Frame — **переносимый язык оружейных возможностей и ограничений**.

Он задаёт:

- spatial job;
    
- характерную дистанцию;
    
- bodily organization;
    
- базовые типы операций;
    
- характер Commitment;
    
- natural debt / weakness;
    
- контригру;
    
- границы допустимой Pattern variation.
    

Frame не обязан задавать точный moveset каждого Pattern.

## Frame boundary test

> Новый Frame нужен, когда знание старого Frame систематически заставляет игрока выбирать неправильную позицию или неправильный тип ответа.

Если неизвестная конструкция полностью ломает ожидания игрока о:

- дистанции;
    
- угрозе;
    
- commitment;
    
- counterplay;
    

скорее всего это уже другой Frame.

## Frame prediction contract

Знание Frame должно позволять игроку сделать разумную гипотезу о неизвестном Pattern минимум по четырём вопросам:

```
Where should I stand?
What kind of commitment am I accepting?
What usually strips this Frame's advantage?
What kind of response is rational against it?
```

Точный timing и moveset могут быть неизвестны. Нельзя требовать, чтобы Frame предсказывал всё.

### Frame too broad

Frame слишком широк, если два его Pattern требуют противоположных базовых ответов и prior knowledge регулярно вредит игроку.

### Frame too narrow

Frame слишком узок, если его Pattern отличаются в основном косметикой/цифрами и игрок не получает нового decision grammar.

### Frame identity survives content growth

Добавление нового Pattern должно расширять язык Frame, не заставляя переписывать его обещание задним числом. Если каждое новое оружие меняет смысл Frame, boundary выбран неправильно.

---

# 3. Pattern

Pattern — повторяемая конкретная конструкция внутри Frame.

Pattern может владеть:

- конкретным moveset;
    
- trajectories;
    
- action ordering;
    
- preparation;
    
- конкретным Primary;
    
- optional Alt;
    
- optional Aim support;
    
- service requirements;
    
- construction-specific behavior;
    
- видимыми execution states.
    

Pattern не должен знать конкретный ID соседнего Pattern ради pair-specific synergy.

Никакого:

```
Pattern Sword X
+ Pattern Pistol Y
→ special authored pair moveset
```

как базовой системы.

## Pattern is authored, not procedural noise

Pattern может быть богатым. Ограничение не в количестве движений, а в том, чтобы движения составляли **одну читаемую конструкцию**.

Pattern variation должна происходить через различия, которые игрок может связать с устройством:

- геометрия действия;
- способ подготовки;
- механизм выпуска;
- естественный долг;
- доступный Alt/Aim;
- service contract.

Не использовать скрытые status/proc combinations как основной способ отличать Pattern. Иначе Pattern перестаёт быть изучаемой физической конструкцией и становится карточкой текста.

---

# 4. Pattern learnability

Большое число оружия допустимо.

Проблема не в том, что разные Pattern имеют разные movesets.

Проблема начинается, когда игрок должен помнить архив скрытых правил.

Неизвестный нормальный Pattern должен позволять относительно быстро восстановить:

```
how do I start?
where does effect go?
where is Commitment?
what continuation is possible?
when am I Ready again?
does it have Alt?
does it support Aim/preparation?
what can be cancelled?
```

Источники обучения:

- внешний вид;
    
- анимация;
    
- dry-use;
    
- несколько безопасных проб;
    
- короткая operational UI information.

## Learnability budget is recoverability, not a fixed trial count

Нельзя заранее канонизировать правило вроде «любой Pattern должен быть понят за три удара». Некоторые конструкции объективно сложнее.

Критерий другой:

> **после ошибки игрок должен понимать, какой наблюдаемый факт он не прочитал, и иметь способ скорректировать следующую попытку.**

Незнакомый Pattern может удивить. Он не должен требовать wiki-memory для базового безопасного взаимодействия.

## Three layers of weapon knowledge

```
Frame knowledge
→ долговременное: позиция, commitment family, counterplay

Pattern knowledge
→ локально изучаемое: concrete action grammar

ItemID knowledge
→ оперативное: состояние этого экземпляра прямо сейчас
```

Этот split позволяет иметь богатый arsenal без требования помнить историю каждой найденной вещи.

---

# 5. Archive-memory failure

Избегать:

```
third attack secretly special
hidden reset timer
identical windups with different commitment
unknown sequence dependency
random affix rewriting action
hidden contact proc zoo
```

Текущее видимое состояние должно давать достаточно информации для решения.

PvP opponent не обязан помнить ItemID историю или скрытую Pattern sequence.

## Readability boundary

Противник не обязан знать внутреннее название Pattern или точные параметры. Он должен своевременно читать то, что меняет его непосредственный ответ:

- опасную геометрию;
- начало существенного Commitment;
- видимую подготовку;
- окно после принятого долга;
- реально отличающийся механизм, если он требует другого ответа.

Скрытая provenance/rarity/history допустима, пока она не меняет required combat response без tell.

---

# 6. ItemID

ItemID — конкретная физическая вещь.

Он владеет runtime состояниями конкретного экземпляра:

- Pattern reference;
    
- condition;
    
- damage;
    
- Heat;
    
- magazine state;
    
- charge/mechanism state;
    
- rarity/affixes;
    
- provenance;
    
- custody;
    
- economic fate.
    

Обычный ItemID не получает новый moveset.

Ordinary rarity/affixes не переписывают базовую Pattern grammar.

Если уникальная Legendary/Relic действительно меняет способ использования оружия, это должно быть явное authored rule-level исключение, а не случайный ItemID moveset zoo.

## Loot-value boundary

Ценность находки может быть высокой без нового moveset. ItemID может отличаться через:

- состояние и надёжность;
- происхождение/редкость;
- стабильность рабочего цикла;
- material/contextual properties;
- уникальное rule-level исключение там, где оно действительно authored.

Weapon freedom ломается не тогда, когда один предмет иногда лучше другого, а когда один экземпляр/класс превосходит альтернативы **по всем релевантным аспектам** и выбор перестаёт зависеть от задачи.

---

# 7. Action

`Action` — конкретное исполнение конкретной операции.

Он владеет:

```
phases
Commitment
Effect
claims
interruption
Recovery
release points
```

Pattern описывает, какое действие возможно.

Action владеет уже начатым исполнением.

## Action timeline is the unit of commitment

Для любого combat action должна быть возможна причинная timeline-модель:

```
request
→ preparation/presentation
→ commitment point
→ effect
→ protected recovery
→ release of claims
→ controlled readiness
```

Не все действия обязаны иметь каждую фазу в явном виде. Но если система не может ответить, **когда и почему** возникает обязательство и когда оно заканчивается, она не сможет честно работать со swap, dual-wield, interruption и Proficiency.

---

# 8. Action-owned debt

После принятого Commitment:

```
switch hand
switch ItemID
Switch Set
Q
E
another weapon
```

не стирают долг предыдущего действия.

Ключевой invariant:

> Recovery принадлежит совершённому Action, а не текущей выбранной вещи.

## Why debt belongs to Action

Если Recovery принадлежит «текущему оружию», то смена оружия становится естественным exploit:

```
commit with A
→ swap to B
→ A no longer current
→ debt disappears
```

Если Recovery принадлежит Action:

```
commit with A
→ swap/reorganize when physically allowed
→ outstanding obligation still exists
```

Это позволяет честно делать быстрые перестройки, не вводя artificial swap lock и не стирая цену предыдущего решения.

---

# 9. Bodily recovery != device recovery

Разделять:

```
Pawn bodily/control recovery
```

и:

```
ItemID technical recovery
Heat
cooling
mechanism reset
vent
```

Возможна ситуация:

```
Pawn control restored
weapon A still cooling
weapon B technically ready
```

Тогда B может стать рациональным следующим действием.

Но:

```
weapon B technically ready
```

не разрешает стрелять внутри защищённого bodily Recovery A.

## Honest cadence principle

Независимое техническое состояние двух устройств может честно создавать преимущество:

```
A fired
→ body recovered
→ A still technically unavailable
→ B ready
→ B becomes a valid next choice
```

Это не exploit. Если такая последовательность разрушает identity конкретного Frame, проблема должна решаться его реальным Natural Debt/Action timeline, а не фиктивным shared Heat или произвольным global cooldown.

---

# 10. Не создавать скрытый global combat lock

Нельзя защищать Action debt просто флагом:

```
pawn_combat_locked = true
```

без физической причинности.

Release points должны соответствовать:

- видимой позе;
    
- контролю тела;
    
- положению рук;
    
- реально оставшемуся обязательству.
    

Если персонаж визуально полностью контролируем, но операция всё ещё запрещена, нужно пересматривать Action timeline или presentation.

---

# 11. Hand semantics

Нужен небольшой authoritative hand/wield contract.

Различать:

```
held
technically operational
presented / physically arranged
action eligible now
```

Это не одно состояние.

Также:

```
empty hand
!=
available hand
```

Рука может быть пустой, но всё ещё занята незавершённым Action claim.

## Minimal claim grammar

Не нужен универсальный full-body mutex. Для оружейной архитектуры достаточно начинать с узких claims:

1. **конкретные hand slots**, нужные операции в конкретной фазе;
2. **coordinated bodily execution**, если несовместимое направленное действие физически невозможно до release point.

Claims должны освобождаться в наблюдаемый момент. Если claim остаётся только потому, что «так проще балансировать», его нужно либо материализовать через анимацию/позу, либо удалить.

---

# 12. 1H / 2H

## 1H

Означает:

> рабочая операция конструкции может быть выполнена с одним hand slot.

Не означает:

- другая рука обязательно свободна;
    
- предмет автоматически хорош как offhand;
    
- второй предмет не влияет на позу.
    

## 2H

Означает:

> рабочая grammar требует двух hand slots для соответствующих операций.

Предмет потенциально можно временно удерживать иначе, если физика допускает, но это не означает сохранённую 2H Ready grammar.

---

# 13. Dual-wield

Dual-wield — базовая физическая возможность.

Не нужны:

```
DualWieldPermission
DualWieldProf
```

Не нужен Trait, чтобы просто держать и использовать два совместимых 1H предмета.

Не создавать universal pair movesets.

UX и Set semantics определяются отдельным milestone.

## What dual-wield is allowed to buy

Dual может покупать:

- два разных immediate Primary;
- независимые device states;
- возможность выбрать второй инструмент после освобождения тела;
- комбинирование разных spatial jobs в одной подготовленной Set.

Dual не получает автоматически:

- два независимых Recovery channels тела;
- независимые полные movesets обоих Pattern на тех же двух кнопках;
- pair-specific techniques;
- offhand damage tax или universal dual bonus.

Таким образом, ценность и цена dual возникают из реальной конфигурации действий, а не из отдельной подсистемы `Dual Wield`.

---

# 14. Два оружия — не два независимых тела

Два ItemID могут иметь независимые:

- Heat;
    
- magazine;
    
- device readiness;
    
- mechanism state.
    

Но Пешка имеет одно coordinated bodily execution.

Следующее действие разрешается через реальные operation requirements и release points, а не потому, что «это другая рука».

---

# 15. Proficiency

Proficiency — локальное отношение:

```
specific Pawn ↔ specific Frame
```

Не XP.

Не gear rarity.

Не общий RPG stat.

Не Pattern-specific level.

## Player skill vs Pawn proficiency

Разделять две компетенции:

```
Player skill
→ chooses line, timing, target, continuation, risk

Pawn Proficiency
→ determines authored quality of human execution of this Frame
```

Высокий player skill не обязан магически отменять embodied limitations Пешки. Низкий Proficiency также не должен превращать действие в случайную рулетку, которая лишает игрока причинной обратной связи.

Хорошая модель даёт игроку возможность **учесть** ограниченное владение и всё равно принять умное решение.

---

# 16. Proficiency scale

Рабочая шкала:

### prof 0

Frame находится вне практического боевого repertoire Пешки.

Предмет можно:

- увидеть;
    
- нести;
    
- исследовать;
    
- возможно dry-handle согласно будущему UX;
    

но он не является нормальным Ready combat tool.

### prof 1

Ограниченное, но реальное владение.

Pattern предоставляет полный moveset.

### prof 2

Authored baseline выполнения Frame.

### prof 3

Исключительное личное владение тем же Frame.

Не новый moveset и не отдельная super-technique автоматически.

---

# 17. Proficiency semantic

Лучший общий semantic candidate после cross-Frame audit:

> **качество возвращения управляемой готовности после уже принятого Commitment.**

То есть proficiency относится прежде всего к человеческому исполнению оружейной grammar.

Разные Frames физически выражают это по-разному:

- вернуть рабочую кисть;
    
- восстановить двухручную линию;
    
- вернуть контролируемую стойку;
    
- освободиться от сложной работы конструкции.
    

Но смысл остаётся общим.

---

# 18. Proficiency не равен Weapon Speed

Не позволять prof автоматически улучшать:

```
damage
Aim speed
battery reload
routing
device cooling
Heat
all animations
service speed
```

Высокий prof может косвенно увеличить practical cadence, если лучшее человеческое восстановление раньше возвращает возможность следующего решения.

Это допустимо.

Но prof не является универсальным multiplicative efficiency stat.

## Spatial value survives low proficiency

> Frame с `prof 1` может быть рационально выбран вместо другого Frame с `prof 2`, если его spatial job лучше соответствует текущей задаче.

Если proficiency автоматически делает другой Frame всегда лучшим выбором, система начала превращаться в equipment rating.

## High proficiency preserves Frame debt

> `prof 3` не удаляет Natural Debt Frame, его контригру или читаемый остаток принятого обязательства.

Высокое владение улучшает человеческое исполнение той же grammar. Оно не превращает Frame в безопасную версию самого себя без его характерной цены.

Конкретные timings/deltas проверяются representative fixtures и остаются prototype-bound.

## Proficiency falsification tests

Модель proficiency провалена, если:

- `prof 1` делает Frame настолько плохим, что его spatial job перестаёт быть рациональной причиной выбора;
- `prof 3` удаляет Natural Debt и counterplay Frame;
- оптимальный способ выразить все уровни — один множитель `RecoverySpeed`;
- prof начинает ускорять routing, cooling, reload, Aim и damage без отдельной причинности;
- Pattern приходится урезать по moveset только ради демонстрации progression.

Proficiency должен менять **качество исполнения** одной grammar, а не превращаться в скрытый gear tier.

---

# 19. Proficiency transitions не арифметически идентичны

Не считать:

```
0 → 1
1 → 2
2 → 3
```

одним и тем же эффектом `+1`.

`0→1` затрагивает admission.

`1→2` и `2→3` меняют качество исполнения уже доступной grammar.

Если Trait позже меняет proficiency, Trait Grammar должна понимать semantic transition, а не просто слепо складывать integer.

## Proficiency is intentionally local

Не выводить из Frame Proficiency универсальную «боевую компетентность» Пешки. Человек может быть исключителен в одном Frame и посредственен в другом. Именно локальность позволяет личной истории владения оружием быть meaningful без отдельного Mastery-tree.

---

# 20. Mastery

Отдельная универсальная `Mastery` сущность удаляется из рабочей архитектуры.

Она имела responsibility collapse:

- access;
    
- proficiency modifier;
    
- special technique;
    
- Personal Tag.
    

Не возвращать Mastery без независимого процесса/ответственности, который невозможно выразить существующими owners.

---

# 21. Traits × Weapon

Trait позже может менять:

- Frame admission;
    
- proficiency relation;
    
- конкретные физические условия исполнения;
    
- человеческое взаимодействие с состоянием.
    

Но Trait не должен:

- знать полный pair catalogue;
    
- создавать новый universal weapon skill tree;
    
- выдавать базовое право dual-wield;
    
- переписывать Pattern moveset через произвольные callbacks.
    

Точная Trait Grammar отложена.

---

# 22. Interfaces вместо global tag soup

Не строить один плоский универсальный словарь `weapon_tags`, через который читается всё.

Использовать доменные contracts:

```
item capability
operation requirement
contact/material property
body/resource requirement
resultant physical state
```

Широкие authored properties возможны там, где имеют реальный consumer.

Q/E или Trait могут читать broad capability/property, если это не превращается в hidden class tree.

---

# 23. Decision-chain, не combo rotation

Следующее melee/ranged решение должно зависеть от:

- позиции;
    
- состояния цели;
    
- собственного состояния;
    
- результата предыдущего действия;
    
- нового окна;
    
- сцены.
    

Не проектировать оптимальную memorized последовательность:

```
1 → 2 → 3 → reset
```

как основную глубину оружия.

Pause/scene change должны возвращать decision-making, а не требовать помнить скрытый combo counter.

## Decision-chain acceptance test

После каждого meaningful result следующий выбор должен хотя бы потенциально зависеть от изменившейся сцены. Если лучшая линия почти всегда:

```
Primary 1
→ Primary 2
→ Primary 3
→ repeat
```

независимо от контакта, позиции и ответа противника, глубина фактически принадлежит rotation memory, а не Weapon Grammar.

Authored continuations допустимы; запрещена именно зависимость глубины от скрытого обязательного combo state.

---

# 24. 2H value

2H должен покупать качественную физическую работу:

- leverage;
    
- reach;
    
- stable line control;
    
- heavy prepared emission;
    
- brace;
    
- geometry;
    

которую нельзя просто воспроизвести суммой двух 1H.

Не балансировать 2H через абстрактный bonus «за занятые две руки».

Не балансировать dual через искусственный global damage penalty.

## 2H / dual comparative test

Система считается здоровой, если существуют задачи, где рационально выбрать:

```
one specialized 2H Pattern
```

и другие задачи, где рационально выбрать:

```
two complementary 1H Primaries
```

без универсального правила «2H = больше damage» или «dual = больше DPS». Разница должна следовать из leverage, reach, preparation, coverage, device cycles, hand occupation и доступных operations.

---

# 25. Что prototype-bound

Для принятых owner contracts не требуется заранее знать:

- точные миллисекунды Recovery;
    
- финальные prof deltas;
    
- весь Frame taxonomy;
    
- восемь законченных Patterns;
    
- все animations;
    
- полный arsenal.
    

Нужны contracts и representative fixtures.

## Representative validation fixtures

Перед массовым arsenal достаточно небольшого диагностического набора, который заставляет архитектуру проявить все границы:

- compact 1H melee;
- reach/leverage 2H melee;
- compact ranged Pattern с Aim;
- ranged Pattern без Aim или с иной preparation grammar;
- heavy 2H ranged;
- dual melee;
- melee+ranged;
- dual ranged.

Для каждого fixture проверить:

```
Frame promise
Frame invariants
Natural Debt
Pattern moveset
readable commitment
Action claims
prof 1 / 2 / 3
unknown-Pattern learnability
PvP response readability
```

Не требуется, чтобы эти fixtures были финальным content. Их задача — диагностировать ownership и interaction grammar.

## Architecture falsification

Milestone требует пересмотра, если representative implementation вынуждает:

- хранить exact moveset одновременно во Frame и Pattern;
- давать обычному ItemID уникальную скрытую grammar;
- вводить pair-specific dual movesets для базовой жизнеспособности;
- стирать Action debt через swap;
- защищать debt невидимым global lock после визуального возврата контроля;
- превращать Proficiency в универсальный speed/power stat;
- требовать wiki-memory для безопасного ответа на незнакомый Pattern.

---

# Milestone principle

> **Frame сообщает переносимый язык оружия. Pattern определяет конкретную изучаемую конструкцию и её moveset. ItemID является физическим экземпляром. Action владеет уже принятым исполнением и его долгом. Proficiency описывает, насколько конкретная Пешка умеет исполнять Frame, не превращаясь в универсальный stat.**
