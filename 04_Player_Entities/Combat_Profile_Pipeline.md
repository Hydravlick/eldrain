---
status: active
system: combat_profile
tags:
  - combat_profile
  - hero_kit
  - abilities
  - arsenal
  - modules
related_files:
  - "[[04_Player_Entities/Two_Paradox_Vector_Matrix|Двойной Парадокс]]"
  - "[[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]]"
  - "[[04_Player_Entities/Registries/Registry_Combos|Реестр полевых профилей]]"
  - "[[04_Player_Entities/Skill_Build_Philosophy|Философия навыков]]"
  - "[[04_Player_Entities/Ability_Synergy|Связность P/Q/E]]"
  - "[[04_Player_Entities/Registries/Registry_Parameter_Contracts|Реестр параметрических контрактов]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Арсенал и владение]]"
  - "[[07_Gear_Inventory/Thermos_System|Термос и модули]]"
type: system
index_route: owner
index_group: player_entities
index_order: 200
index_summary: "Показывает состояние Пешки и основания доступности из владельцев; read-only projection."
read_when: Когда нужен контракт «Combat Profile Pipeline» и его границы с соседними владельцами.
---
# Combat Profile Pipeline

Combat Profile показывает, что конкретная Пешка имеет сейчас, какие действия можно попытаться выполнить и почему часть возможностей недоступна. Он помогает выбрать подготовку, груз, маршрут и риск, но не оценивает человека одним числом.

## Контракт проекции

```text
owners → resolved facts + source references → read-only projection
```

Проекция не применяет modifiers повторно, не разрешает взаимодействия, не рассчитывает итоговый build для обратной записи в системы. Порядок и policy каждого расчёта принадлежат его доменному владельцу. Никакой общий Build Resolver между ними не требуется.

```yaml
combat_projection_contract:
  mode: read_only
  applies_modifiers: false
  resolves_gameplay: false
  writes_gameplay_state: false
  eligibility_owner: Action
  source_references_required: true
```

## Что читается

| Источник | Что показывает проекция | Что остаётся у источника |
|---|---|---|
| [[04_Player_Entities/Skill_Build_Philosophy|Field Profile]] и [[04_Player_Entities/Registries/Registry_Combos|его записи]] | identity Race × Spec, deterministic P, определения Q/E, decision signature, authored BaseServiceCapacity | authored факты профиля; профиль не хранит concrete ItemID и не является готовой сборкой |
| [[04_Player_Entities/Shell_Construction|Конкретная Пешка]] и Body | происхождение, текущее тело, доступные capabilities, раны и состояния | личные факты и последствия их изменения |
| [[04_Player_Entities/Tags_System|Общие Trait rules]] | профильное происхождение P, личное происхождение Personal Traits, их применимость и результаты, уже принятые владельцами | единая semantic grammar и доменное разрешение; P не пересчитывается отдельным effect engine |
| [[04_Player_Entities/Proficiency_Arsenal|Pawn ↔ Frame]] | сохранённое отношение конкретного человека | admission и authored handling; без EffectiveProf, MasteryContribution или moveset unlock |
| [[05_Combat_Survival/Weapon_Core|Frame / Pattern / ItemID]] | язык Frame, операции Pattern и независимые состояния физических копий | определения и runtime state оружия |
| [[07_Gear_Inventory/Equipment_PaperDoll|Weapon Set]] и [[07_Gear_Inventory/Inventory_Architecture|Inventory]] | prepared layout, действительная занятость рук, custody, Ready Access, груз | физическое размещение, подготовка и transition |
| [[05_Combat_Survival/Combat_Three_Debts|Action]] | текущие claims, принятый долг, опубликованные причины недоступности | eligibility, исполнение, прерывание, Recovery и release points |
| [[07_Gear_Inventory/Thermos_Assembly|Thermos Assembly]] | подтверждённый ThermosAssemblySnapshot: модель, nodes, установленные ItemID, разрешённые эффекты и legality | fit/topology/service-расчёт; проекция не чинит нелегальную сборку |
| [[05_Combat_Survival/Magic_Batteries|Battery]] и [[05_Combat_Survival/Weapon_Ranged|ranged ItemID]] | Full/Drained конкретной батареи; отдельные magazines, Heat и техническая готовность | source reservation/transaction и локальный device state |
| Environment, [[03_Factions_Societies/Quest_Engine|Quest]], группа и текущие обязательства | доступные методы, ограничения среды, цена груза, подтверждённые результаты | требования и состояние работы, средовые правила, completion и result handoff |

Каждый показанный результат имеет ссылку на источник и его актуальный snapshot/revision, если владелец их публикует. Изменение тела, Set, груза или мира требует обновления представления. Устаревшая карточка не разрешает действие: новый request повторно проверяется владельцем Action и требуемыми доменными owners. Буферизованное намерение сохраняет исходную operation/recipient.

## Profile, человек и физическая подготовка

Race объясняет физиологическую причинность, Spec — метод работы. Их пересечение вручную определяет Field Profile; оно не получается суммой RPG-атрибутов. [[04_Player_Entities/Two_Paradox_Vector_Matrix|Двойной Парадокс]] вычисляет аналитическую координату и вопросы к дизайну, но не игровые параметры.

Требования к законченному профилю принадлежат [[04_Player_Entities/Skill_Build_Philosophy#8. Уникальность полевого профиля|Skill Build Philosophy]] и [[04_Player_Entities/MVP_3x3_Design_Contract|MVP contract]]. Проекция не утверждает контент. Пока `arsenal_status: pending_content`, она показывает пустой арсенал; исторические `legacy_weapon_frame` не становятся fallback. Пустота валидна для архитектуры, но не означает готовый игровой профиль.

При `prof >= 1` разные люди используют полный moveset того же Pattern. Две копии Pattern имеют одно определение и разные runtime states. Проекция не меняет отношение Pawn ↔ Frame при смене предмета и не выбирает «лучшее оружие» вместо игрока.

## Чтение результата

Игрок видит P как гарантированное профильное правило, Q/E как отдельные активные операции, личные отклонения — с их источником. Для локального обмена `до → после` UI показывает готовый расчёт владельца, а не повторяет арифметику. Физические события Battery, Dissonance и status application сохраняют источники и не считаются повторно.

Резюме отвечает на вопросы: что можно попробовать, какой материал или доступ нужен, что сейчас занято, какова цена и почему предыдущая попытка сорвалась. Связность действий читается через факты мира — линию, груз, руки, состояние устройства; ID соседнего Trait или ярлык профиля не становится тайным условием синергии.

Информация раскрывается по [[04_Player_Entities/Tags_System#Информационная граница|решению участника]]. Проекция владельца не является HUD противника и не заменяет внешний tell.

## Инварианты

- Owners публикуют факты; Combat Profile только читает и объясняет их.
- Ни modifier requests, ни итоговые domain values не записываются проекцией обратно.
- BaseServiceCapacity читается из Field Profile; законность сборки — из Thermos Assembly.
- P и Personal Trait читаются через одну semantic grammar; Q/E — через active operation contract.
- Возможности работы не хранятся здесь как PawnOpportunityList. Их требования, изменения и завершение разрешают конкретные work owners.
- Нет общего Power Score, повторной оплаты одной причинной цепи или автоматического выбора за игрока.
