---
status: active
system: inventory
tags:
  - weight
  - access
  - ui
  - items
  - physics
related_files:
  - "[[07_Gear_Inventory/Containers_Slots|Containers and Slots]]"
  - "[[06_Economy_Loot/Extraction_Stabilization_Loop|Extraction_Stabilization_Loop]]"
  - "[[08_World_Generation/Anomaly/Extraction_System|Extraction_System]]"
  - "[[04_Player_Entities/Registries/Registry_Interaction_Families|Семейства взаимодействий]]"
  - "[[07_Gear_Inventory/Thermos_Assembly|Thermos Assembly]]"
  - "[[07_Gear_Inventory/Registries/Registry_Thermos_Interfaces|Thermos Interfaces]]"
type: system
index_route: owner
index_group: gear_inventory
index_order: 150
index_summary: "Определяет состояния, разрешение и связи: Механика: Архитектура Инвентаря (Mass & Access)."
read_when: "Когда нужен контракт «Механика: Архитектура Инвентаря (Mass & Access)» и его границы с соседними владельцами."
---
# Механика: Архитектура Инвентаря (Mass & Access)

## 1. Базовый Принцип
Инвентарь строится на гибридной системе, где баланс задают **Вес (Weight)**, **Доступность (Access)** и занятый **Back Slot**. Вес сравнивается с локальным телесным `SustainedCarryLimit` конкретного полевого профиля и обвязки; Ready Access и Back Slot принадлежат инвентарю и не выводятся из общего рейтинга Пешки.

* **Единица измерения:** Килограмм (kg).
* **Визуализация:** Список (List View) с иконками.
* **Геймплей:** Меньше микроменеджмента форм, больше тактических решений по весу, доступу и обязательству груза.

> Каноническая проверка вместимости для рейда: общий вес, зона доступа и занятый Back Slot. Форма предметов не является боевым ограничителем.

## 2. Три Зоны Инвентаря

### А. Быстрый Доступ (Ready Access)
Небольшой набор предметов, подготовленных к применению в бою.

* **Принцип:** игрок заранее выбирает батареи, расходники и инструменты, которые можно применить без копания в грузе.
* **Источник:** самостоятельная зона управления, а не число карманов на броне.
* **Броня:** не добавляет ячейки быстрого доступа. Ось `cargo` модуля описывает собственную физическую работу с грузом и Back Slot, но не меняет телесный `CarryLoad` и не превращается в скрытый объём инвентаря. Прежний queue-effect `battery_rack` deprecated; он не расширяет Ready Access и не публикует действующий энергетический эффект.
* **Неопределено:** точное число позиций, общий вес и правила смены раскладки проверяются прототипом.

### Б. Рюкзак (Cargo Backpack)
Зона логистики и хранения лута.
* **Лимит:** **Нет лимита слотов** (Infinite Scroll). Ограничение задают общий вес, физический Back Slot и intrinsic bulk предметов; bulk — не сетка ячеек, а маршрутная, силуэтная или carry-обязанность.
* **Принцип:** общий вес сравнивается с `CarryLoad`. Ниже Sustained Carry Limit груз `stowed`; сверх него игрок сознательно несёт `carry_committed` груз с объявленной Exposure. Предмет из груза нельзя мгновенно применить в бою, пока игрок не переложит его в Ready Access через уязвимую ручную операцию.
* **Extraction-решение:** низкая редкость не означает низкую нужность. Тяжёлый серый материал может закрывать несколько рецептов, но конкурирует с редким `value/kg` по массе, Back Slot и маршрутной обязанности, а не через скрытый штраф базовой скорости.

### В. Слот Спины (Back Slot)
Физический слот для крупного груза.

* **Варианты:** рюкзак, капсула найденыша, тело, генератор, тяжелый ящик.
* **Правило:** одновременно можно надежно нести только один Back Slot объект.
* **Выбор:** рюкзак дает объем лута, капсула найденыша дает будущего персонажа, тело может закрыть контракт.
* **Манифест:** на выходе защищается только фактически занятый Back Slot. Брошенный генератор, тело или капсула не считаются эвакуированными и получают отдельный исход финальной Стабилизации.
* **Носитель:** у груза один текущий carrier. Передача, кэш, волочение или эстафета остаются физическими состояниями мира; они не создают виртуальный общий инвентарь и не снимают массу, bulk либо риск потери.

## 3. ItemID, custody и сборка Термоса

`INVENTORY_CUSTODY` единолично владеет существованием, текущим владельцем/контейнером и reservation-state каждого физического `ItemID`. [[07_Gear_Inventory/Thermos_Assembly|Thermos Assembly]] решает законность монтажа, но не может клонировать, самовольно перемещать либо считать свободным предмет, которого нет в подтверждённом custody snapshot.

### Обычная account custody

Каждый извлечённый не-Welfare `ItemID` возвращается через [[06_Economy_Loot/Return_Manifest_Contract|Return Manifest]] в общий account путь custody. У обычного предмета нет состояния «у Пешки до будущего адреса», личной находки, release-to-bank или скрытой очереди применимости. Фитинг может временно ограничивать использование совместимостью, но не создаёт личную собственность: после законного снятия ItemID снова доступен совместимой Ready-Пешке из общего Схрона.

```yaml
ItemCustodySnapshot:
  item_id: ItemID
  item_definition_id: DefinitionID
  custody_revision: Revision
  current_container: SharedStashID | AssemblyID | RaidEntityID | WorldEntityID
  condition_revision: Revision
  reservation_state: FREE | PREPARED(ReservationID) | COMMITTED(AssemblyID)
```

### Prepare / commit

Монтаж у мастера использует одну транзакционную границу:

1. `AssemblyDraft` передаёт список требуемых реальных `ItemID` и ожидаемые revisions.
2. `INVENTORY_CUSTODY` атомарно проверяет существование, контейнер, condition и отсутствие другого reservation.
3. Успешный prepare создаёт durable `ItemReservation`; он ещё не меняет живую сборку.
4. Assembly Resolver проверяет fit, topology, service legality и effect/debt contracts только на подготовленных snapshots.
5. Финальный commit одной операцией:
   - привязывает новые ItemID к `AssemblyID`;
   - возвращает снятые ItemID в указанный легальный контейнер;
   - фиксирует новый `assembly_revision`;
   - завершает reservation.
6. Любой отказ до commit оставляет прежнюю сборку и custody без частичного монтажа. После подтверждённого commit восстановление после сбоя читает durable journal, а не откатывает предметы в два места.

Один `ItemID` не может одновременно находиться в двух reservations, сборках либо контейнерах. Повреждение меняет `condition_revision`, но не создаёт новый предмет. `AssemblyID` фиксирует физическую сборку, а не личный кошелёк Пешки.

### Preset и ghost plan

Preset хранит DefinitionID, желаемые patterns и предпочтения замены. Он не хранит custody и не резервирует ItemID. После потери сборки ghost plan может помнить состав и показывать отсутствующие части, но:

- не создаёт уничтоженный предмет;
- не выбирает substitute без preview;
- не подтверждает денежную цену;
- не обходит новый fit/topology/service resolver;
- не превращает одну редкую вещь в несколько подготовленных комплектов.

## Weapon Set и physical custody

[[07_Gear_Inventory/Equipment_PaperDoll|Weapon Set]] хранит prepared references конкретных ItemID. Inventory подтверждает существование, физическое размещение, Ready Access и reservations; запись ссылки в Set не перемещает предмет из Cargo и не создаёт ещё одну копию. Подготовка использует актуальные custody revisions и не обходит существующий запрет двух reservations одного ItemID.

Set layout, actual hand occupancy и Action claims не являются контейнерами. PaperDoll фиксирует достигнутое удержание и контекст перехода; реальные stow/retrieve/drop movements подтверждаются Inventory. Потеря доступа к предмету делает его ссылку недоступной для операции, но не подменяет recipient и не выбирает другой предмет автоматически.

Существующие запреты двойной custody и превращения одной вещи в несколько подготовленных комплектов сохраняются. Возможность **shared ItemID reference между A и B одной Пешки** отдельно не определена: форма Set schema сама её не подтверждает. До явного physical preparation contract такая раскладка остаётся unresolved, а не разрешением клонирования или телепортации.

## Battery source reservation

Full Battery и Drained Cell — состояния одной физической вещи по [[05_Combat_Survival/Magic_Batteries|Magic Batteries]]. Inventory сохраняет ItemID, custody, placement и provenance при разрядке. Он не хранит числовой энергетический wallet; состояние батареи не является magazine оружия.

Существующая исключительная `ItemReservation` применяется и к service Action: `PREPARED(ReservationID)` связывает source ItemID, ActionID и проверенные revisions. Это не `COMMITTED(AssemblyID)` и не установка батареи в сборку. Повторная reservation того же предмета другой операцией отклоняется.

Battery owner проверяет Full eligibility и принимает атомарный commit вместе с результатом consumer; Inventory подтверждает reservation/custody и сохраняет физическую вещь. После исхода reservation завершается по service release contract. Поздняя команда с прежней revision не может использовать новое Full-состояние или другую Battery вместо исходной. Перемещение во время обслуживания явно проходит custody; одно энергетическое изменение не создаёт drop, teleport или clone.

## 4. Граница полномочий

- Inventory владеет `ItemID`, custody, condition revision, Ready Access и Back Slot.
- Weapon Set / PaperDoll владеет prepared layouts, active Set и фактическим wield transition state; Action сохраняет собственные claims.
- Thermos Assembly владеет fit/topology/service-legality и атомарным составом сборки.
- [[07_Gear_Inventory/Physical_Weight|Physical Weight]] владеет итоговой массой и load stages.
- [[07_Gear_Inventory/Containers_Slots|Containers and Slots]] владеет поведением физического контейнера как предмета: содержимым, выпадением, сбросом и потерей доступа.
- Экономика владеет получением, ценой и заменой, но не монтажной законностью.
- Повреждённый support-модуль не запускает полевой демонтаж или каскадный пересчёт legality. Его runtime-эффект может отключиться; повторная полная валидация выполняется только у мастера.
