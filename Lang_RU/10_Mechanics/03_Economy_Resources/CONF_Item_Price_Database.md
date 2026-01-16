---
type: mechanic
system: economy_config
tags: [config, parsing, prices]
related_files:
  - "[[Lang_RU/00_Variables/Registry_Items|Registry_Items]]"
  - "[[Lang_RU/10_Mechanics/03_Economy_Resources/TRD_03_Dynamic_Pricing|TRD_Dynamic_Pricing]]"
---

# Конфиг: База Цен (Computed Price Database)

## 1. Назначение
Этот модуль не содержит хардкода цен. Он является **Парсером**, который при запуске сервера сканирует `Registry_Items` и собирает кэшированную таблицу стоимости для всех предметов.

## 2. Логика Расчета (Pricing Logic)

### Базовая Стоимость
`Base_Value` берется из параметров предмета в Реестре.

### Формула Оценки
$$CurrentPrice = (Base\_Value \times Global\_Multiplier) \times Durability\_Mod$$

1.  **Global_Multiplier:** Глобальный коэффициент экономики (обычно 1.0).
2.  **Durability_Mod:** Если предмет имеет прочность < 100%, цена снижается линейно.
    * *Пример:* Винтовка (50/100 hp) стоит 50% от цены.
    * *Broken Item:* Если предмет сломан (0 hp), он стоит как `Scrap` (Мусор).

## 3. API Методы
* `GetItemBasePrice(ItemID)` — возвращает эталонную цену.
* `CalculateSellPrice(ItemInstance)` — возвращает цену продажи торговцу (с учетом износа).
* `CalculateBuyPrice(ItemID, VendorModifier)` — возвращает цену покупки у торговца (с наценкой).