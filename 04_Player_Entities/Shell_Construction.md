---
status: active
system: player_core
tags:
  - shell
  - entity
  - structure
  - slots
related_files:
  - "[[04_Player_Entities/Tags_System|Tags_Modification]]"
  - "[[04_Player_Entities/Skill_Build_Philosophy|Skill_Build_Philosophy]]"
  - "[[04_Player_Entities/Lifecycle_Roster|Lifecycle_Roster]]"
  - "[[04_Player_Entities/Registries/Registry_Races|Registry_Races]]"
  - "[[04_Player_Entities/Registries/Registry_Specs|Registry_Specs]]"
  - "[[04_Player_Entities/Combat_Profile_Pipeline|Combat_Profile_Pipeline]]"
  - "[[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]]"
type: core_concept
---
# Конструкция боевого профиля Пешки

## Человек не вычисляется из билда

Пешка — живой житель с телом, биографией и отношениями. Боевой профиль описывает способ действовать в одной вылазке, но не создаёт человека и не назначает его ценность.

```text
Person: Body | origin | lifecycle
FieldProfile: authored(Race × Spec)
CombatProfile: Person | FieldProfile | physical Loadout | conditions
```

- **Race** даёт биологическую причинность, capability и vulnerability.
- **Spec** даёт освоенный метод давления, подготовки и решения задач.
- **Полевой профиль** вручную определяет решения конкретного пересечения, P/Q/E, исходные Frame relationships и BaseServiceCapacity.
- **Personal Tags** меняют один локальный параметр либо одно правило при зарегистрированном условии.
- **Loadout** добавляет Frame, Термос, модули, батареи и физический инвентарь со своими владельцами правил.

## Чтение профиля

```text
Body / Field Profile / personal rules / Pawn↔Frame
+ Inventory / ItemID / Thermos / current Action
+ Environment / work requirements / group
→ owner facts → read-only Combat Profile
```

Слои не сливаются в общий рейтинг. Предмет не выдаёт биологию, Personal Tag не переписывает authored P/Q/E, а экипировка не становится новым полевым профилем. Каждый эффект остаётся у локального владельца и сообщает собственную цену.

## Личное владение

Пешка хранит собственный `frame_proficiencies` snapshot по [[04_Player_Entities/Proficiency_Arsenal|Proficiency owner]]. При создании исходные отношения предоставляет authored Field Profile; после этого они не являются runtime полем профиля или вещей. Замена ItemID/Pattern/Set не переинициализирует человека. Пока active Frames отсутствуют, пустой список допустим; progression и реальные назначения здесь не создаются.

## Неизменные границы

- Race и Spec фиксируют identity полевого профиля Пешки и не являются предметными слотами.
- Personal Tags принадлежат [[04_Player_Entities/Tags_System|Tags System]]; последствия принадлежат lifecycle, Quest, Trace, custody или CityState.
- Frame задаёт переносимый язык, Pattern — moveset; при допуске по Pawn ↔ Frame он доступен полностью, без Mastery unlock;
- Термос и инвентарь владеют физической посадкой, доступом и переносом, а не параметрами тела или способности.
- Новая сборка может закрыть один authored-пробел только реальной ценой веса, ресурса, позиции, времени или зависимости от команды.

Read-only представление фактов описывает [[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile Pipeline]], данные конкретных полевых профилей — [[04_Player_Entities/Registries/Registry_Combos|Registry Combos]].

## Три слоя ценности Пешки

| Слой | Где существует | Что означает смерть |
|---|---|---|
| Personal / embodied value | Тело и morphology, current states, конкретное воплощение Field Profile, Personal Traits, Pawn↔Frame, действительно личные способности, знания и связи | LOST: этот человек больше не исполняет их; общая definition профиля и сохранённая история не стираются |
| Active opportunity / ongoing work | Пересечение возможностей человека с требованиями работы, подготовкой, материалами, средой и текущим миром | RE-EVALUATE: владелец работы пересматривает метод, исполнителя, стоимость, продолжение или невозможность |
| Externalized achieved result | Реально созданный ItemID, доставленный материал, подтверждённый факт, исполненное обязательство | NOT REVERSED BY DEATH ITSELF: после completion судьбой результата владеет его собственная система |

```yaml
pawn_value_contract:
  embodied_on_death: lost
  unfinished_work_on_capability_loss: re_evaluate
  completed_result_on_author_death: not_reversed
  completed_result_owner: result_domain
  unique_capability_transferred: false
  work_result_is_retirement_reward: false
  indefinite_parked_value: false
  opportunity_list_owner: false
```

Возможность может ещё не стать проектом: иной состав материалов или новая погода делают личный метод рациональным. Начатая работа хранится в Quest/контракте, производственной транзакции или расследовании, а не в PawnOpportunityList. Смерть может потребовать другого исполнителя, более дорогого пути или приостановки. Конкретная работа с обязательным живым участником может стать невозможной именно из-за утраты её требования, без общего правила удаления всех незавершённых дел.

```text
concrete Pawn → особый способ или возможность действовать
→ другая подготовка / материал / маршрут / риск
→ выполненная работа → достигнутый результат → собственный owner результата
```

Передаётся результат работы, а не уникальность человека. Результат не бессмертен: вещь можно потратить, уничтожить или украсть; факт уточняется и устаревает по правилам знания; адрес или обязательство меняют ценность по правилам мира. Утрата автора не является самостоятельным основанием откатить completion или создать capability у преемника.

## Реализация ценности и завершение жизни

Ценность конкретной Пешки должна преимущественно реализовываться через meaningful work, commitment, opportunity cost и действие, а не через простое сохранение её живого статуса. Это включает мастерскую, подготовку, исследование, переговоры, анализ и полевые процедуры; обязательного боевого риска для каждого свойства нет. Хранение живого человека без участия не производит пассивную ценность неопределённо долго.

Work result != retirement reward. [[04_Player_Entities/Life_Closure|Life Closure]] не выдаёт выполненную работу заново, не конвертирует её в наследуемую силу и не служит условием сохранения результата. Конкретные передачи и проверка четырёх исходов показаны в [[03_Factions_Societies/Quest_Engine#Сквозной срез: измерение и подтверждение|существующем контракте измерения]].

Информационное чтение свойств следует [[04_Player_Entities/Tags_System#Информационная граница|решению участника]]; одно личное отличие не обязано менять каждый горизонт игры.
