---
type: mechanic
status: active
index_route: owner
index_group: combat_survival
index_order: 190
index_summary: "Задаёт правила и последствия системы «Оружие: ближний бой»."
read_when: "Читайте при изменении входов, состояний, стоимости или последствий системы «Оружие: ближний бой»."
system: action_combat
tags:
  - melee
  - frames
  - movesets
  - collision
related_files:
  - "[[05_Combat_Survival/Combat_Three_Debts|Combat_Three_Debts]]"
  - "[[05_Combat_Survival/Registries/Registry_Weapons|Registry_Weapons]]"
---
# Оружие: ближний бой

Мили выплачивает долг дистанции до эффекта. Frame даёт переносимое понимание рабочей позиции, телесной организации и характерной цены. Pattern определяет конкретные траектории и moveset; найденный ItemID хранит состояние этой вещи. Полный identity contract — [[05_Combat_Survival/Weapon_Core|Weapon Core]].

## Цикл

```text
читать маршрут → занять дистанцию → Commitment
→ контакт или промах → Recovery → следующий выбор
```

Каждое продолжение снова сталкивается со стеной, блоком, изменившейся дистанцией, затратой сил и открытым углом. Pattern объявляет понятный порядок операций и возвращение к готовности; скрытый счётчик последовательности не заменяет чтение сцены. Принятый телесный долг исполняется по [[05_Combat_Survival/Combat_Three_Debts|Action contract]].

Коллизия с геометрией не создаёт скрытый stagger: рабочая часть отскакивает или теряет эффект по объявленным правилам контакта операции, а игрок видит, что сам выбрал неверную траекторию.

## Ввод и фактическая готовность

[[07_Gear_Inventory/Equipment_PaperDoll|Weapon Set]] запрашивает Primary либо optional Alt по своим channels. Второй предмет даёт собственную Primary, а не универсальный block/support moveset. Отсутствие Alt не создаёт fallback блока. Ни пустой prepared slot, ни смена Set не освобождают Action claim; доступность рук проверяется по фактическому удержанию и общему Action contract.

## Конструкция и экземпляр

Pattern может менять opener, короткое альтернативное действие, геометрию продолжения и ожидаемую форму Recovery внутри Frame envelope. Новый хват не классифицируется автоматически: применяется Frame boundary test. Конкретный ItemID не переписывает moveset и не владеет текущим Action debt.

Прежние шесть melee Frames и их authored-примеры сохранены как legacy scaffolding. Они не задают актуальные роли арсенала или будущие fixtures. Публикуемые определения и допустимое пустое состояние находятся в [[05_Combat_Survival/Registries/Registry_Weapons|Registry Weapons]].
