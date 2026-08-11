---
type: overview
status: active
system: player_core
tags: [shell, entity, structure, slots]
related_files:
  - "[[04_Player_Entities/Tags_System|Tags_Modification]]"
  - "[[04_Player_Entities/Skill_Build_Philosophy|Skill_Build_Philosophy]]"
  - "[[04_Player_Entities/Lifecycle_Roster|Lifecycle_Roster]]"
  - "[[04_Player_Entities/_Registries/Registry_Races|Registry_Races]]"
  - "[[04_Player_Entities/_Registries/Registry_Specs|Registry_Specs]]"
  - "[[04_Player_Entities/Combat_Profile_Pipeline|Combat_Profile_Pipeline]]"
  - "[[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]]"
  - "[[04_Player_Entities/Trait_Development|Trait_Development]]"
---
# Конструкция боевого профиля Пешки

Эта страница даёт короткую карту сущностей. Полный порядок разрешения принадлежит [[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile Pipeline]], а данные конкретных hero-kit — [[04_Player_Entities/_Registries/Registry_Combos|Registry Combos]].

## Человек не вычисляется из билда

Пешка — живой житель с телом, биографией и отношениями. Боевой профиль описывает способ действовать в одной вылазке, но не создаёт человека и не назначает его ценность.

```text
Person: Body | Chronicle
HeroKit: authored(Race × Spec)
CombatProfile: Person | HeroKit | physical Loadout | conditions
```

- **Race** даёт биологическую причинность, capability и vulnerability.
- **Spec** даёт освоенный метод давления, подготовки и решения задач.
- **Hero-kit** вручную определяет решения конкретного пересечения, P/Q/E и базовый арсенал.
- **Chronicle** хранит прожитые факты, связи и последствия, не становясь механическим тегом.
- **Personal Tags** вносят небольшие личные изменения через зарегистрированные сигналы.
- **Loadout** добавляет Frame, Термос, модули, батареи и физический инвентарь со своими владельцами правил.

## Сборка профиля

```text
Race × Spec → authored HeroKit
  → тело и допустимые техники
  → выбранные Frame / Thermos / Battery / Inventory
  → Personal Tags
  → контракт, среда, команда и груз
  → читаемый профиль текущей вылазки
```

Слои не сливаются в общий рейтинг. Предмет не выдаёт биологию, Chronicle не меняет механику сама, Personal Tag не переписывает authored P/Q/E, а экипировка не становится новым hero-kit. Каждый эффект остаётся у локального владельца и сообщает собственную цену.

## Неизменные границы

- Race и Spec фиксируют identity hero-kit Пешки и не являются предметными слотами.
- Chronicle существует у любого жителя независимо от происхождения и статуса ростера.
- Personal Tags принадлежат [[04_Player_Entities/Tags_System|Tags System]]; память и квестовые ситуации — [[04_Player_Entities/Trait_Development|Trait Development]].
- Frame сохраняет базовый gunfeel у своего владельца; личное mastery открывает только опубликованную технику совместимого Frame.
- Термос и инвентарь владеют физической посадкой, доступом и переносом, а не параметрами тела или способности.
- Новая сборка может закрыть один authored-пробел только реальной ценой веса, ресурса, позиции, времени или зависимости от команды.

Смысл конструкции — позволить игроку менять доктрину вылазки, не стирая личность Пешки и не превращая весь проект в одну шкалу силы.
