---
status: active
system: inventory_ui
canonical_id: WEAPON_SET
owns:
  - weapon_set.prepared_configuration
  - weapon_set.active_set
  - weapon_set.wield_state
  - weapon_set.transition_context
tags:
  - slots
  - equipment
  - masks
  - restrictions
  - paper_doll
  - fashion
related_files:
  - "[[07_Gear_Inventory/Inventory_Architecture|Inventory_Architecture]]"
  - "[[07_Gear_Inventory/Fashion_Gear|Fashion_Gear]]"
  - "[[07_Gear_Inventory/Thermos_System|Thermos_System]]"
  - "[[05_Combat_Survival/Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[07_Gear_Inventory/Gear_Progression|Gear_Progression]]"
  - "[[07_Gear_Inventory/Registries/Registry_Thermoses|Registry_Thermoses]]"
  - "[[07_Gear_Inventory/Registries/Registry_Thermos_Modules|Registry_Thermos_Modules]]"
  - "[[07_Gear_Inventory/Thermos_Assembly|Thermos Assembly]]"
type: system
index_route: owner
index_group: gear_inventory
index_order: 120
index_summary: "Определяет Weapon Set, фактическое удержание и переходы; показывает экипировку Термоса."
read_when: Когда нужен контракт «Кукла Персонажа (Equipment Slots)» и его границы с соседними владельцами.
---
# Кукла Персонажа (Equipment Slots)

## 1. Философия: Tactical Goblincore
Пешка надевает одну выбранную модель [[07_Gear_Inventory/Thermos_System|Термоса]]. Термос является сменной основой с физическими узлами; защиту и утилиту создают вшитые модули, а не отдельный боевой комбинезон.

---

## 2. Схема Слотов (The Loadout)

### А. Голова (Head Zone)
1.  **Mask Slot (Маска):** Единственный жесткий элемент на лице. Защищает от газа и дает HUD.
2.  **Filter Slot (Фильтр):** Сменный картридж. Если таймер фильтра истек, маска перестает защищать.

### Б. Тело (Body Zone)
1. **Body Base (Основа):** реальный экземпляр модели Термоса с `fit_envelope`, `FitRecord`, физическими `mount_nodes` и собственной массой.
2. **Installed Modules:** кукла показывает выбранный pattern каждого реального ItemID и фактически занятые nodes из committed `ThermosAssemblySnapshot`; она не решает topology сама.
3. **Service Panel:** отдельная панель показывает `Base / SupportLoad / Final / Used / Remaining` по затронутым семействам `plate`, `optic`, `seal`, `conduit`, `rig`, `weave`.
4. **Installed State:** `stitched_locked`, damage и выбранный `active_body_interface_module_id` принадлежат экземпляру сборки. В рейде их можно осматривать, но нельзя переставлять.

Количество заплат и карточная внешность не создают слот и не повышают профильную ёмкость. Скрытый трансмог не используется.

### В. Weapon Set

Игрок готовит две полные конфигурации рук — Set A и Set B. В одной может быть один одноручный предмет, в другой — два; двуручная конструкция использует те же две позиции. Set хранит ссылки на реальные подготовленные ItemID, без копии вещи или её moveset. Размер не назначает оружию постоянную роль «главного» или «запасного».

PaperDoll владеет prepared layouts, active Set, фактическим wield presentation и контекстом физического перехода. [[07_Gear_Inventory/Inventory_Architecture|Inventory]] владеет custody, размещением, Ready Access, reservations и подготовкой Cargo → Ready. [[05_Combat_Survival/Combat_Three_Debts|Action]] владеет допуском, исполнением и принятыми claims. Это разные состояния.

Глобальные bindings принадлежат Input Contract, moveset — Pattern, device state — ItemID. Set не хранит собственные magazine, батарею, Heat или Recovery и не добавляет скрытого общего ресурса двух предметов.

### Prepared layout schema

```yaml
weapon_set_contract:
  set_ids: [A, B]
  hand_slots: [1, 2]
  item_reference: ItemID
  placement_fields: [item_ref, occupies]
  layout_shapes:
    single_1h: [[1]]
    dual_1h: [[1], [2]]
    two_handed: [[1, 2]]
  channel_mapping:
    single_1h:
      weapon_channel_1: {recipient_slots: [1], operation_field: primary_operation}
      weapon_channel_2: {recipient_slots: [1], operation_field: alt_operation}
    dual_1h:
      weapon_channel_1: {recipient_slots: [1], operation_field: primary_operation}
      weapon_channel_2: {recipient_slots: [2], operation_field: primary_operation}
    two_handed:
      weapon_channel_1: {recipient_slots: [1, 2], operation_field: primary_operation}
      weapon_channel_2: {recipient_slots: [1, 2], operation_field: alt_operation}
  transition_intent: switch_weapon_set
  eligibility_owner: ACTION_EXECUTION
```

Каждый элемент layout — одна placement запись `{item_ref, occupies}`. В `two_handed` это **одна** ссылка ItemID с `occupies: [1, 2]`, а не предмет плюс фиктивная вторая запись. `single_1h`, `dual_1h` и `two_handed` — формы одной schema, не независимые режимы исполнения. Один layout не повторяет ItemID и не содержит пересекающихся placements. Требования конкретной конструкции читаются из Pattern, а не выводятся из названия Frame.

Single 1H использует slot 1. Dual даёт прямой доступ к двум Primaries, не требует Trait, отдельного permission, mastery или proficiency пары. Optional Alt обоих Patterns не получает дополнительных универсальных кнопок. Одноручный щит или иной combat accessory может занять обычную позицию и позднее предоставить Primary; отдельной категории offhand не вводится.

### Четыре разных состояния

| Состояние | Владелец | Что оно сообщает |
|---|---|---|
| Physical placement / custody | Inventory | Где существует ItemID, кто владеет им и доступен ли он подготовке |
| Prepared Set layout | PaperDoll | Какие ItemID подготовлены для каждой конфигурации и какие позиции они требуют |
| Actual hand occupancy / presentation | PaperDoll | Что фактически удерживается сейчас, включая временный operation object и частичный переход |
| Outstanding hand/body claim | Породивший его Action | Какие несовместимые операции пока нельзя начать и когда claim освободится |

Prepared slot `empty` не означает доступную руку. Она может удерживать временный объект, участвовать в переходе или оставаться под Action claim. Аналогично, 2H placement требует обе позиции для подготовленной организации, но не утверждает, что обе руки уже заняты ею в каждый момент извлечения.

PaperDoll хранит фактическое удержание по рукам и связи с подтверждёнными Inventory movements. Это не второй custody journal: размещение предмета меняется у Inventory, а PaperDoll фиксирует достигнутое удержание. Временное освобождение или занятие руки другой операцией не переписывает prepared layout.

### От channel к запросу

[[01_Core_Vision/Input_Contract|Input Contract]] передаёт `weapon_channel_1/2`. Таблица `channel_mapping` выбирает placement и поле operation definition у его Pattern. Потребитель фиксирует исходные Set/revision, ItemID и operation; копия moveset в Set не хранится. Получается **request**, который ещё должен пройти Action eligibility: bodily availability, outstanding claims, требования Pattern, состояние устройства и релевантную среду.

Если `alt_operation` отсутствует, результат — `no authored operation`. Нет fallback ability, выстрела или смены адресата. В dual отсутствует обязательный selector предмета: первый channel остаётся связан с Primary slot 1, второй — с Primary slot 2. Weapon Focus не меняет эту таблицу.

Depletion, поломка, потеря custody или временная недоступность ItemID не меняют раскладку. В частности, dual с потерянным B не превращается автоматически в single A с Alt на channel 2. Сохраняется недоступный исходный recipient; новая конфигурация требует явной подготовки. Magazine/reload rules здесь не реализуются.

### Switch Set и фактическое удержание

`switch_weapon_set` запрашивает переход всей конфигурации A → B либо B → A. Default Mouse Wheel scroll назначен в Input Contract. Это не выбор одного предмета внутри dual и не перестановка одной руки.

Контекст перехода хранит source/destination Set, ожидаемые revisions и ссылку на transition Action. Action хранит свою фазу, claims, Commitment и release points; PaperDoll не дублирует их счётчиком Recovery. Последовательность физического перехода:

```text
request destination Set
→ проверить доступность и текущие claims
→ начать допустимые операции освобождения / размещения / извлечения
→ подтвердить реальные Inventory movements и actual occupancy
→ достичь подготовленного удержания destination
→ подтвердить active Set
```

До подтверждения новая Set не объявляется wield-ready. Последняя подтверждённая active Set сохраняет mapping, но её уже убранный предмет не проходит физическую eligibility. Достижение подготовленного удержания не гарантирует техническую готовность устройства.

Прерывание оставляет достигнутое физическое состояние: убранный предмет не телепортируется обратно, извлечённый не исчезает. Продолжение, отказ и дальнейшая реорганизация проверяются по текущей occupancy и outstanding claims. Stow/drop разрешаются соответствующей процедурой и custody-владельцем, а не автоматически самим запросом Switch Set. Точная choreography и длительности остаются prototype-bound.

Action из исходной Set освобождает собственные claims только по своим release points. Switch Set не отменяет его долг; допустимая часть перестройки зависит от оставшихся обязательств. Для фактической занятости используется этот же Action contract, без второго global hand resolver.

### Сохранение input intent

Удержание и buffer привязаны к исходной operation/recipient. Переключение Set, изменение layout или ItemID state не превращает старое намерение в действие новой конфигурации. Если исходная операция больше невозможна, остаётся её cancel/failure outcome, а новая требует нового намерения.

```text
hold channel_1 в Set A → Switch Set → Set B подтверждена
→ старое удержание не запускает Primary новой Set

buffer channel_2 для B → B недоступен
→ buffer не становится Alt другого Pattern
```

Отпускание завершает исходное намерение и не назначает его новому адресату. Точные buffer windows остаются prototype-bound.

### Focus и другие операции

`weapon_focus` передаётся [[05_Combat_Survival/Weapon_Core#Weapon Focus|Weapon Core]]: ровно один независимый weapon owner и поддержка его Pattern. 2H — один owner; dual 1H — два, Focus недоступен при любом порядке предметов. PaperDoll предоставляет Set и actual occupancy, не выбирает Focus recipient между двумя оружиями. LMB/RMB сохраняют исходные operation mappings.

Q/E, расходник или взаимодействие со средой используют требования собственной operation. Наличие двух предметов не создаёт третью руку, но и не запрещает все способности целиком. Если нужна свободная рука, необходимая перестройка должна реально произойти и пройти тот же Action/custody contract.

### Подготовка и открытые границы

Inventory подтверждает доступность реальных ItemID и их reservations перед подготовкой layout. Ссылка Set не резервирует предмет повторно, не меняет контейнер и не подменяет Cargo → Ready.

Один ItemID уже запрещён в двух независимых reservations, контейнерах или сборках. **Допустимость общей ссылки одного ItemID из Set A и Set B пока не определена физической preparation model.** Такой shared-reference layout нельзя считать подтверждённым по одной лишь форме schema; требуется отдельный контракт Inventory preparation. Это не разрешение клонировать предмет, телепортировать его или считать две ссылки двумя доступными вещами.

Текущий batch не создаёт оружейных определений: Frames, Patterns и diagnostic fixtures остаются пустыми.

---
## 3. Визуализация
У мастера сначала выбираются Пешка и модель Термоса. Кукла показывает nodes, допустимые mount patterns, затронутые service families и `service_load` каждого модуля. До подтверждения игрок видит единый список причин отказа и доменные проекции массы, Диссонанса, эффектов и покрытия. Покрытие показывает тот же Ballistics-owned `ResolvedCoverageSnapshot`, который использует hit resolver; PaperDoll не строит собственную геометрию.

В Аномалии экран работает только на чтение: видны установленные, повреждённые и отключённые модули, но перетаскивание недоступно. Маска остаётся отдельным предметом, а визуальная отделка не скрывает фактическую геометрию Термоса.

## Сервис и runtime ItemID

Switch Set сохраняет magazine, Heat, condition и device state каждого ItemID. Во время [[05_Combat_Survival/Magic_Batteries#3. Reload и получатель энергии|reload]] PaperDoll показывает фактическую временную занятость рук; подготовленный layout не превращается в источник энергии. Принятый reload остаётся связан с исходным получателем, а source custody/reservation подтверждает Inventory. Переход не переносит refill на destination Set и не сбрасывает Action debt.

### Switch как control barrier

Default Mouse Wheel scroll создаёт один `switch_weapon_set` request по [[01_Core_Vision/Input_Contract|Input Contract]]. Запрос отменяет текущую uncommitted Preparation, затем выполняет переход к другой Set на ближайшей legal Action boundary. Pending switch не разрешает старым weapon intents заново выбрать operation из новой конфигурации. Уже удерживаемые LMB/RMB/Focus остаются связаны с исходным context generation; после смены новое действие требует нового намерения. Outstanding committed debt остаётся у его Action.

```yaml
set_switch_input_contract:
  intent: switch_weapon_set
  cancels_uncommitted_preparation: true
  execution_boundary: earliest_legal_action_boundary
  bound_context: [operation, recipient, context_generation]
  old_held_intent_reinterpreted: false
  preserves_committed_debt: true
```
