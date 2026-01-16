---
type: mechanic
system: economy_config
tags: [config, parsing, loot, rng]
related_files:
  - "[[Lang_RU/00_Variables/Registry_LootTables|Registry_LootTables]]"
---

# Конфиг: Калькулятор Лута (Loot Resolver)

## 1. Назначение
Модуль для разрешения вложенных таблиц лута (Nested Loot Tables) и вычисления реального шанса выпадения предмета.

## 2. Структура Таблиц
Система читает `Registry_LootTables`.
* **Weighted Lists:** Список предметов, где у каждого есть Вес (Weight). Шанс = `Weight / Total_Weight`.
* **Rolls:** Количество попыток (например, "Roll 3 times").
* **Conditions:** Условия выпадения (например, `Min_Level: 10`).

## 3. Алгоритм Резолва (Loot Logic)

```csharp
List<ItemStack> ResolveLoot(TableID tableId, PlayerStats modifiers) {
    var result = new List();
    var table = LoadTable(tableId);

    // 1. Применить модификаторы удачи (Magic Find)
    float bonus = modifiers.GlobalLuck;

    // 2. Итерации (Rolls)
    for (int i = 0; i < table.Rolls; i++) {
        // Выбор категории на основе весов
        var entry = WeightedRandom(table.Entries, bonus);

        if (entry.IsNestedTable) {
            // Рекурсия: Если выпала другая таблица
            result.AddRange(ResolveLoot(entry.NestedID, modifiers));
        } else {
            // Прямое выпадение предмета
            result.Add(CreateItem(entry.ItemID, entry.Count));
        }
    }
    return result;
}