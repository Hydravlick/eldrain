---
status: active
system: player_core
tags:
  - weapons
  - proficiency
  - arsenal
related_files:
  - "[[05_Combat_Survival/Registries/Registry_Weapons|Registry Weapons]]"
  - "[[04_Player_Entities/Registries/Registry_Combos|Registry Combos]]"
  - "[[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]]"
  - "[[07_Gear_Inventory/Thermos_System|Thermos System]]"
  - "[[04_Player_Entities/Skill_Build_Philosophy|Field Profile]]"
  - "[[05_Combat_Survival/Combat_Three_Debts|Action contract]]"
canonical_id: PROFICIENCY_RELATION
owns:
  - proficiency.pawn_frame_relation
  - proficiency.admission_and_handling
type: system
index_route: owner
index_group: player_entities
index_order: 90
index_summary: "Определяет состояния, разрешение и связи: Proficiency: владение языком Frame."
read_when: "Когда нужен контракт владения Frame, допуска и границ человеческого исполнения."
---
# Proficiency: владение языком Frame

Один человек может уверенно исполнять знакомую оружейную grammar и ограниченно владеть другой. Игрок учитывает это при выборе позиции и действия, но подходящая пространственная работа оружия остаётся причиной взять его даже при меньшем prof.

## 1. Отношение Pawn ↔ Frame

Proficiency — качество практического владения конкретной Пешкой языком конкретного Frame. Identity отношения — `PawnID + FrameID`; runtime state принадлежит этой Пешке под правилами данного owner. Frame, Pattern, ItemID и Weapon Set не хранят собственного уровня владения.

[[04_Player_Entities/Skill_Build_Philosophy#Field Profile: исходные отношения и service budget|Field Profile]] может author исходные отношения, а [[04_Player_Entities/Registries/Registry_Combos|Registry Combos]] публикует их definitions. Это источник инициализации, не вечный runtime writer. Смена ItemID, Pattern или Set не создаёт новое отношение и не возвращает профильную базу поверх сохранённого состояния человека.

```yaml
proficiency_contract:
  identity: [pawn_id, frame_id]
  runtime_owner: Pawn
  baseline_source: FieldProfile
  relation_field: frame_proficiencies
  record_fields: [frame_id, proficiency]
  levels: [0, 1, 2, 3]
  admission_level: 1
  admitted_moveset: full_pattern
  exceptional_technique_required: false
  handling_axis: return_to_controlled_readiness_after_commitment
  natural_debt_preserved: true
  spatial_job_may_outweigh_level: true
  universal_modifiers: []
  mastery_dependency: false
  action_owner: ACTION_EXECUTION
  device_state_owner: ItemID
  changes_input_mapping: false
  owns_service_capacity: false
```

Схема runtime snapshot, не запись нового человека:

```yaml
PawnFrameSnapshot:
  pawn_id: PawnID
  frame_proficiencies: []
```

Каждый элемент списка содержит ровно `frame_id` и целый `proficiency` от 0 до 3. FrameID уникален в пределах Pawn; активные назначения ссылаются только на canonical active Frame. PatternID, ItemID, SetID, bonus и Mastery не являются альтернативными ключами. Пустой список valid; отсутствующая запись не доказывает admission и не заполняется legacy-значением. При нулевом active Frame corpus назначения также могут отсутствовать. Конкретные записи здесь не создаются.

## 2. Уровни и смысл переходов

| Уровень | Практический смысл | Доступ к Pattern |
|---|---|---|
| `prof 0` | вне практического боевого repertoire | нет нормального combat admission; физическое удержание проверяется отдельно |
| `prof 1` | ограниченное, но реальное владение | полный authored moveset |
| `prof 2` | уверенное authored baseline-выполнение | тот же полный moveset |
| `prof 3` | исключительное человеческое исполнение | тот же moveset, без обязательной специальной техники |

`0 → 1` означает practical admission; `1 → 2` — улучшение исполнения доступной grammar; `2 → 3` — исключительное refinement. Это не одинаковые прибавки одного multiplier. Аварийного prof0 moveset, XP, обучения, respec или способа приобретения уровней данный контракт не вводит.

## 3. Handling и навык игрока

Общий ориентир — **качество возвращения к контролируемой готовности после принятого Commitment**. Подходящее выражение зависит от Frame: возвращение рабочей кисти, двухручной линии или контролируемой стойки. Локальный authored handling contract уточняет последствия в операциях Pattern, сохраняя общий смысл и Natural Debt; числовые deltas и timings остаются prototype-bound.

Это не умножение всех Recovery durations. Prof не выдаёт universal damage, attack/animation speed, Aim speed, reload speed, cooling, Heat/magazine efficiency, movement speed или ускорение всех восстановлений. Локальная связь с параметром требует причинности в grammar и Action/service contract; само число prof не разрешает такую связь.

Player skill выбирает линию, timing, цель, продолжение и риск. Pawn Proficiency определяет качество исполнения выбранного действия. Высокий prof не выбирает правильный ответ за игрока; ограниченное владение не должно превращать причинный ввод в случайную рулетку.

## 4. Definition, Action и устройство

При `prof >= 1` сохраняется полный moveset данного Pattern, включая Primary, optional Alt и authored Aim support. Set mapping по-прежнему определяет, какие операции доступны через текущие channels; полный moveset не создаёт дополнительные кнопки для dual Alt.

Pattern описывает операции и допустимые handling consequences. [[05_Combat_Survival/Combat_Three_Debts|Action]] проверяет eligibility и владеет конкретным Commitment, claims, interruption, Recovery и release points. Proficiency — вход в объявленное исполнение, не команда очистить текущий долг. Уже принятые claims не исчезают от чтения prof или изменения личного состояния.

Heat, cooling, magazine, condition, battery и mechanism state остаются у ItemID/профильных owners. Другой способ обслуживания возможен только через отдельную operation/service grammar. В dual каждый request читает отношение к Frame своего ItemID; больший prof не выбирает оружие, не меняет channel mapping и не создаёт proficiency пары.

## 5. Acceptance boundaries

- Frame с prof1 может быть рационально выбран вместо другого с prof2, когда его spatial job лучше соответствует задаче. Автоматическое превосходство большего числа независимо от задачи означает equipment rating.
- Prof3 сохраняет Natural Debt, контригру и своевременно читаемый остаток принятого обязательства. Он не превращает Frame в безопасную версию самого себя.
- Смена Pattern внутри Frame использует то же отношение; две физические копии Pattern не получают отдельных уровней.
- Practical admission не отменяет физические требования: actual occupancy, повреждение тела, device state и Action claims проверяются отдельно.
- BaseServiceCapacity не принадлежит Proficiency. Authored budget находится у Field Profile, окончательная assembly legality — у Thermos Assembly.

Эти условия проверяются позднее поведением representative fixtures; структурные проверки не доказывают баланс или читаемость. Fixtures, реальные назначения и content в этом cutover не создаются.

## 6. Superseded и будущие изменения

Universal Mastery, MasteryContribution, additive EffectiveProf, XOR step/expression, урезанный prof1 moveset и обязательная prof3 technique — superseded. Их нельзя сохранить переименованием в Expertise или Personal Proficiency Bonus. Deprecated research не является источником активного admission.

Будущее причинное изменение отношения конкретного человека должно объявлять смысл перехода у соответствующего owner. Training, Traits, scars, inheritance и acquisition здесь не проектируются. P и Personal Trait используют общую rule grammar с разным происхождением; ни один из них не получает автоматическую роль replacement Mastery.

## Контракт доступа

```text
ItemID → PatternID → FrameID
PawnID ↔ FrameID → proficiency
prof >= 1 → полный moveset выбранного Pattern
operation request + requirements + текущее состояние → Action eligibility
```
