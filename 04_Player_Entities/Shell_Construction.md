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

Эта страница даёт короткую карту сущностей. Полный порядок разрешения принадлежит [[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile Pipeline]], а данные конкретных полевых профилей — [[04_Player_Entities/Registries/Registry_Combos|Registry Combos]].

## Человек не вычисляется из билда

Пешка — живой житель с телом, биографией и отношениями. Боевой профиль описывает способ действовать в одной вылазке, но не создаёт человека и не назначает его ценность.

```text
Person: Body | origin | lifecycle
FieldProfile: authored(Race × Spec)
CombatProfile: Person | FieldProfile | physical Loadout | conditions
```

- **Race** даёт биологическую причинность, capability и vulnerability.
- **Spec** даёт освоенный метод давления, подготовки и решения задач.
- **Полевой профиль** вручную определяет решения конкретного пересечения, P/Q/E и базовый арсенал.
- **Personal Tags** вносят небольшие личные изменения через зарегистрированные сигналы.
- **Loadout** добавляет Frame, Термос, модули, батареи и физический инвентарь со своими владельцами правил.

## Сборка профиля

```text
Race × Spec → authored FieldProfile
  → тело и допустимые техники
  → выбранные Frame / Thermos / Battery / Inventory
  → Personal Tags
  → контракт, среда, команда и груз
  → читаемый профиль текущей вылазки
```

Слои не сливаются в общий рейтинг. Предмет не выдаёт биологию, Personal Tag не переписывает authored P/Q/E, а экипировка не становится новым полевым профилем. Каждый эффект остаётся у локального владельца и сообщает собственную цену.

## Неизменные границы

- Race и Spec фиксируют identity полевого профиля Пешки и не являются предметными слотами.
- Personal Tags принадлежат [[04_Player_Entities/Tags_System|Tags System]]; последствия принадлежат lifecycle, Quest, Trace, custody или CityState.
- Frame сохраняет базовый gunfeel у своего владельца; личное mastery открывает только опубликованную технику совместимого Frame.
- Термос и инвентарь владеют физической посадкой, доступом и переносом, а не параметрами тела или способности.
- Новая сборка может закрыть один authored-пробел только реальной ценой веса, ресурса, позиции, времени или зависимости от команды.

Смысл конструкции — позволить игроку менять доктрину вылазки, не стирая личность Пешки и не превращая весь проект в одну шкалу силы.
