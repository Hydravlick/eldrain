---
type: mechanic
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
# Спецификация: Конструкция Боевого Профиля Пешки

## 1. Философия Сборки
Персонаж — это живой житель со своей биографией. Конструкция описывает его **боевой профиль**, а не создание тела и не сумму универсальных RPG-атрибутов:

```text
Person: Body | Chronicle
HeroKit: authored(Race × Spec)
CombatProfile: references Person | HeroKit | physical Loadout
```

Hero-kit является авторской ячейкой `Race × Spec`, а не арифметическим смешением двух наборов чисел. Конструктор не печатает человека, не определяет его ценность и не стирает личность.

1. **Race (Раса):** задаёт биологическую причинность, физику тела, capability/vulnerability и возможные способы исполнения.
2. **Specialization (Класс):** задаёт методологию давления, подготовки и решения задач.
3. **Hero-kit / Combo:** вручную определяет полный `P/Q/E`, разрешённый арсенал, proficiency, `module_capacity` и стартовые доктрины конкретного пересечения.
4. **Chronicle:** существует у каждой Пешки и хранит опыт, связи, Шрамы, tags/traits и последствия прожитых сцен.
5. **Loadout:** конкретные Frame, Термос, модули, батареи и инвентарь со своими локальными владельцами параметров.

Раса не поставляет готовую пассивку, а специализация — готовые активные кнопки. Такая расклейка признана устаревшей.

## 2. Структура Данных
Каждая Пешка содержит независимые блоки; ни один из них не является общим рейтингом человека:

1. **Body Contract:** authored-физиология, локальные `BaseCapacity / CurrentHP`, способы движения, capability/vulnerability и названные травмы.
2. **Hero Kit:** одна запись `Race × Spec`, владеющая своими `P/Q/E`, их `owned_parameters`, долгом, `counterplay_now`, арсеналом и `module_capacity`.
3. **Chronicle:** универсальная личная история; tags/traits ссылаются на конкретную ситуацию, владельца результата и цену, а не добавляют пакет общих статов.
4. **Physical Loadout:** предметы и их владельцы — Frame владеет базовым gunfeel, батарея своим пакетом, Термос ёмкостью установленных позиций, Inventory Owner весом и доступом.

## 2.1. Боевой профиль

Боевой профиль не рассчитывает «финального персонажа». Он соединяет уже authored-решения и проверяет локальную совместимость; полная цепочка описана в [[04_Player_Entities/Combat_Profile_Pipeline]]:

```text
Race × Spec
  -> authored HeroKit(P/Q/E + Arsenal + module_capacity)
  -> Body capability + Proficiency Gates
  -> selected Frame / Thermos / Battery / Inventory
  -> Combat Profile текущей вылазки

Chronicle
  -> только named situational edges и последствия
```

Для MVP `Registry_Combos` является главным источником authored-P/Q/E, арсенала и `module_capacity`. Раса и специализация объясняют, почему эта ячейка действует именно так, но не порождают её сложением полей.

## 3. Границы Изменения

- `Race` и `Spec` фиксируют identity hero-kit этой Пешки и не являются сменными предметными слотами.
- Chronicle универсальна: она есть у городского жителя, Ward, Foundling и любого другого живого происхождения на одинаковых правилах.
- У Chronicle нет лимита, зависящего от типа ростера. Конкретный tag/trait имеет собственные условия появления, совместимость, конфликт и последствия.
- Chronicle может изменить named-ситуацию, телесную травму, отношение, долг или локальный `downstream_edges`, если запись называет один результат, одного владельца и цену в той же сцене.
- Chronicle и её tags/traits **не меняют** базовый gunfeel Frame, authored-`P/Q/E`, разрешённый арсенал или `module_capacity` hero-kit. Такое изменение является новой авторской версией Frame/Combo, а не развитием биографии.
- Экипировка не переписывает hero-kit: она предоставляет собственный физический цикл, позиции и локальные интерфейсы, которые заново проходят capability/proficiency-проверку.
