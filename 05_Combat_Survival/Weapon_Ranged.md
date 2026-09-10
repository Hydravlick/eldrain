---
canonical_id: WEAPON_RANGED
owns:
  - ranged.magazine_semantics
  - ranged.device_state
type: mechanic
status: active
index_route: owner
index_group: combat_survival
index_order: 200
index_summary: "Задаёт правила и последствия системы «Оружие: дальний бой»."
read_when: "Читайте при изменении входов, состояний, стоимости или последствий системы «Оружие: дальний бой»."
system: action_combat
tags:
  - ranged
  - arcanegun
  - battery_cycle
  - mechanical
related_files:
  - "[[05_Combat_Survival/Combat_Three_Debts|Combat_Three_Debts]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
  - "[[05_Combat_Survival/Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Registries/Registry_Parameter_Contracts|Реестр параметрических контрактов]]"
---
# Оружие: дальний бой

Дальний бой покупает немедленное влияние на линии и платит вниманием мира. Он создаёт давление, срыв, связь или аномальное окно; самостоятельное убийство требует позиции, ресурса, слабой зоны и пережитого ответа.

## Готовность устройства и тела

Pattern задаёт технический цикл конструкции и ожидаемый долг операции. Текущий Heat, cooling и mechanism recovery принадлежат конкретному ItemID под правилами устройства. Текущий телесный долг совершённого выстрела принадлежит Action по [[05_Combat_Survival/Combat_Three_Debts#Телесное восстановление и технический цикл|общему контракту исполнения]].

После восстановления контроля A может ещё охлаждаться, а технически готовый B — стать допустимым следующим инструментом, если выполнены его требования и не осталось мешающих bodily claims. Пока защищённая фаза A исключает новое направленное действие, B не может выстрелить только потому, что находится в другой руке. Смена вещи не завершает ни технический цикл A, ни его принятый телесный долг.

## Semantic inputs

Primary request приходит из соответствующего [[07_Gear_Inventory/Equipment_PaperDoll|Set channel]]. Aim запрашивается отдельным intent по [[05_Combat_Survival/Weapon_Core#Aim intent и организация тела|Weapon Core]] и только при объявленной поддержке Pattern. Ни RMB, ни положение предмета во второй руке не определяют Aim capability.

Недоступный ranged ItemID сохраняет свой channel: он не передаёт ввод другому устройству, Alt или reload. Сервисное намерение отдельно адресуется по [[05_Combat_Survival/Magic_Batteries|battery/reload contract]].

## Magazine конкретного предмета

Magazine model является возможностью Pattern, а не обязательным свойством любого ranged оружия. Pattern, использующий эту модель, определяет `magazine_capacity`, `shot_consumption` и `reload_service_ref`. Текущий `magazine_current` принадлежит исключительно физическому Weapon ItemID; capacity читается из его Pattern definition. Копия capacity в runtime projection не становится независимым источником значения.

```yaml
magazine_contract:
  state_owner: WEAPON_RANGED
  runtime_owner: ItemID
  current_field: magazine_current
  capacity_owner: Pattern
  capacity_field: magazine_capacity
  consumption_field: shot_consumption
  reload_field: reload_service_ref
  optional_for_pattern: true
  shot_recipient: executing_weapon_itemid
  default_shot_cost: 1
  switch_preserves_state: true
  depletion_remaps_channel: false
```

Инвариант состояния: `0 <= magazine_current <= magazine_capacity`. Операция проверяет достаточность magazine перед своим ресурсным commit; обычный исполненный выпуск списывает одну единицу. Промах не возвращает её: valid shot означает состоявшийся выпуск, а не попадание в цель. Иная стоимость требует явно authored `shot_consumption`; новые многозарядные Patterns здесь не задаются.

Списание и факт выпуска относятся к одному resource commit конкретного Action. До него отменённый запрос не списывает magazine; после него позднее прерывание не возвращает расход. Последующие Heat, technical recovery и bodily Recovery не исчезают от исчерпания магазина.

В dual A и B хранят независимые magazine: выстрел A не меняет B. Inventory и Weapon Set не содержат общий ammo pool. Switch Set и возврат к прежнему ItemID сохраняют его magazine, Heat, condition и device state. EMPTY оставляет channel привязанным к той же Primary operation и даёт отказ; никаких автоматических reload, переключений или переноса ввода на B.

### Пополнение

[[05_Combat_Survival/Magic_Batteries#3. Reload и получатель энергии|Reload]] — сервисный Action с одной Full Battery и одним Weapon ItemID. Успешный атомарный commit переводит Battery в Drained Cell и устанавливает `magazine_current = magazine_capacity`. Цена одинакова при любом неполном остатке; полный получатель не расходует Battery. Обычный выстрел больше не обращается к использованной батарее.

Pattern описывает reload requirements и ожидаемую процедуру; Action проверяет её допустимость и сохраняет принятый долг. Reload не является reset устройства: Heat, техническое восстановление и condition не меняются от пополнения magazine без отдельно объявленного правила.

## Конструкция и публикация

Pattern определяет конкретное поведение выпуска, подготовку, optional Alt/Aim и сервисные требования внутри переносимого языка Frame. Две физические копии используют этот же moveset, сохраняя независимые device states. Ordinary ItemID не создаёт новый цикл атак. Владение определяется отношением Pawn ↔ Frame, без отдельного prof для моделей.

Прежние ranged Frames — legacy scaffolding, а не текущая taxonomy или будущие fixtures. Публикация определяется [[05_Combat_Survival/Registries/Registry_Weapons|Registry Weapons]]. Временное отсутствие активных ranged definitions допустимо.

Сильный дальний предмет покупает повторяемость или узкое покрытие попадания, но не получает право решать маршрут, открывать аномальную процедуру или игнорировать мили, Q/E, обход и третью сторону.
