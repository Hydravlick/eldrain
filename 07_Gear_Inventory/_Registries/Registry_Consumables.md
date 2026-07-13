---
type: registry
status: active
system: gear_inventory_registry
registry_type: necessary_consumables
tags: [database, medicine, access, expedition]
related_files:
  - "[[05_Combat_Survival/Combat_Consumables|Медицина, здоровье и необходимые расходники]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
  - "[[05_Combat_Survival/_Registries/Registry_StatusEffects|Registry_StatusEffects]]"
---
# Реестр: необходимые расходники и экспедиционные предметы

> Расходник уничтожается или истощается конкретным применением. Батареи являются источниками энергии и описываются в [[05_Combat_Survival/Magic_Batteries|Magic_Batteries]], а не как второй payload боевого навыка.

## 1. Контракт записи

```markdown
[item_id:: stable_id]
[item_kind:: medical | access | evidence]
[consumed_on:: none | use | failure | access]
[use_time:: none | duration]
[movement_rule:: none | slow_walk | stationary]
[restores_current_hp:: none | amount]
[restores_field_capacity:: none | amount]
[removes_effect:: none | effect_id]
[applies_effect:: none | effect_id]
[countered_by:: none | response_id]
[waste_item:: none | item_id]
```

`restores_current_hp` и `restores_field_capacity` всегда разделены. Одно применение не заполняет обе шкалы автоматически. Числа, токсичность и лимиты стека являются предметом прототипа.

## 2. Медицина

### Бинт полевого ухода
[item_id:: field_bandage]
[item_kind:: medical]
[consumed_on:: use]
[use_time:: prototype]
[movement_rule:: slow_walk]
[restores_current_hp:: prototype_minor]
[restores_field_capacity:: none]
[removes_effect:: bleed]
[applies_effect:: none]
[countered_by:: interruption]
[waste_item:: none]

Останавливает открытую рану и покупает короткое окно. Не устраняет увечье, не возвращает `FieldCapacity` и не заменяет лечебную Q/E.

### Стимулятор
[item_id:: stim_pack]
[item_kind:: medical]
[consumed_on:: use]
[use_time:: prototype]
[movement_rule:: slow_walk]
[restores_current_hp:: prototype]
[restores_field_capacity:: none]
[removes_effect:: none]
[applies_effect:: none]
[countered_by:: interruption]
[waste_item:: empty_vial]

Быстро возвращает боеспособность ценой уязвимости применения. Отдельная система передозировки пока не объявлена: стимулятор не ссылается на несуществующий глобальный статус. Не закрывает тяжёлую травму и не подменяет аккумулятор навыка.

### Набор полевой коррекции
[item_id:: field_correction_kit]
[item_kind:: medical]
[consumed_on:: use]
[use_time:: prototype_long]
[movement_rule:: stationary]
[restores_current_hp:: none]
[restores_field_capacity:: prototype_limited]
[removes_effect:: cripple]
[applies_effect:: none]
[countered_by:: interruption]
[waste_item:: used_correction_frame]

Поддерживает повреждённую функцию тела и ограниченно возвращает доступную телесную ёмкость. Это уязвимая процедура, а не безопасная кнопка продолжить рейд.

## 3. Допуск и свидетельство

### Одноразовый ключ
[item_id:: single_use_key]
[item_kind:: access]
[consumed_on:: access]
[use_time:: prototype]
[movement_rule:: stationary]
[restores_current_hp:: none]
[restores_field_capacity:: none]
[removes_effect:: none]
[applies_effect:: none]
[countered_by:: none]
[waste_item:: broken_key]

Открывает конкретный доступ и не является боевой утилитой.

### Карта и след
[item_id:: expedition_trace]
[item_kind:: evidence]
[consumed_on:: none]
[use_time:: none]
[movement_rule:: none]
[restores_current_hp:: none]
[restores_field_capacity:: none]
[removes_effect:: none]
[applies_effect:: none]
[countered_by:: none]
[waste_item:: none]

Карта, след или доказательство дают информацию, маршрут либо право на дальнейшую процедуру. Они сохраняются, пока конкретный контракт не объявляет их расход.

## 4. Запреты

- колбы, гранаты, ловушки, химические зоны, световые шары и барьеры не существуют как обычные боевые расходники;
- боевой навык не требует медицинский предмет как второй платёж;
- расходник не создаёт новый P/Q/E или бесконечное восстановление по cooldown;
- доступ, карта и след не заменяют [[08_World_Generation/Generation/08_Gate_Check|Gate Check]], бой или обязательную экстракцию.
