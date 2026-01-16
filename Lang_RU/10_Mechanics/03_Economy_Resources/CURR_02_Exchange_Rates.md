---
type: mechanic
system: currency
tags: [exchange, rates, inflation]
related_files:
  - "[[Lang_RU/00_Variables/Registry_Exchange_Rates|Registry_Exchange_Rates]]"
---

# Валюта: Логика Обмена (Exchange Logic)

## 1. Реестр Курсов
Все текущие курсы обмена берутся из внешнего реестра.
![[Lang_RU/00_Variables/Registry_Exchange_Rates]]

## 2. Механика Конвертации
Конвертация происходит только через специальных NPC (Банкиры) или Терминалы.

### Формула
$$Output\_Amount = \lfloor (Input\_Amount \times Rate\_Multiplier) \rfloor$$

* **Округление:** Всегда вниз (Floor). Дробные части "сгорают" как налог системы.

## 3. Динамические Модификаторы
Курс может меняться глобальными событиями (см. `WRLD_Inflation`).
* *Пример:* Если Фракция "Собор" доминирует в войне, курс `Cathedral_Signet` растет (+20%).
* Сервер обновляет `Rate_Multiplier` в Реестре раз в цикл (например, каждые 4 часа).