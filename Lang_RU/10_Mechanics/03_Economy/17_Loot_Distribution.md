---
type: mechanic
system: loot_generation
tags: [rng, spawn, containers, probability, biomes]
related_files:
  - "[[Lang_RU/10_Mechanics/04_Inventory_Gear/02_Containers_Slots|Containers_Slots]]"
  - "[[Lang_RU/00_Variables/Registry_Biomes|Registry_Biomes]]"
  - "[[Lang_RU/00_Variables/Registry_Items|Registry_Items]]"
---

# Распределение Лута (Loot Distribution Logic)

## 1. Матрица Генерации
В Элдрейне лут не привязан жестко к контейнеру. Содержимое ящика определяется пересечением двух осей:
1.  **Биом (`[biome:: id]`):** Определяет **ТЕМА** лута (ЧТО падает).
2.  **Тир Угрозы (`[difficulty:: XX]`):** Определяет **КАЧЕСТВО** лута (СКОЛЬКО, КАКОГО тира и КАКОЙ редкости).

---

## 2. Влияние Биома (Thematic Filtering)
Когда генерируется лут, система накладывает "Биомный Фильтр" на общую базу предметов (`Registry_Items`).

| Биом (Пример) | Тег Биома | Приоритетные категории лута | Штрафные категории |
| :--- | :--- | :--- | :--- |
| **Ржавый Порт** | `[biome:: port]` | `Industrial`, `Tools`, `Scrap_Metal`, `Water_Gear` | `High_Tech`, `Magic_Scrolls` |
| **Собор / Храм** | `[biome:: temple]` | `Artifacts`, `Books`, `Ritual_Items`, `Gold` | `Military_Ammo`, `Modern_Tech` |
| **Военная База** | `[biome:: military]` | `Weapons`, `Ammo`, `Armor`, `Explosives` | `Civilian_Trash`, `Food` |

> *Логика:* В порту вы с 80% вероятностью найдете ржавый гаечный ключ или гарпун, и только с 1% — магический гримуар.

---

## 3. Влияние Тира (Difficulty Scaling)
Уровень локации (Tier 1-3) напрямую модифицирует математику "ролла" (броска кубика).

### Tier 1: Periphery (Периферия)
`[difficulty:: 01]` — Зона высадки.
* **Empty Chance (Шанс пустого слота):** 40%
* **Rarity Cap:** Максимум **Uncommon (Зеленое)**. Rare (Синее) падает только с боссов.
* **Durability:** Предметы спавнятся с прочностью 20-50%.

### Tier 2: Deep Zone (Глубина)
`[difficulty:: 02]` — Основная зона активности.
* **Empty Chance:** 25%
* **Rarity Bonus:** +10% к шансу повысить редкость.
* **Durability:** Предметы спавнятся с прочностью 40-70%.
* **Exclusive:** Начинают падать специфические ресурсы биома (например, *Deep Coral* в Порту).

### Tier 3: Epicenter (Эпицентр)
`[difficulty:: 03]` — Штормовая зона / Логово босса.
* **Empty Chance:** 10% (Почти все контейнеры полные).
* **Min Rarity:** **Uncommon**. (Обычный "серый" мусор отфильтровывается).
* **High Roll:** Шанс найти **Artifact** или **Blueprint** увеличен в 3 раза.
* **Danger:** При открытии контейнера есть 5% шанс активировать ловушку или спавн моба ("Mimic").

---

## 4. Алгоритм Спавна (The Spawn Step)
При генерации контейнера в локации `Rusty Port (Tier 2)`:

1.  **Fetch:** Система берет список всех предметов.
2.  **Filter (Biome):** Оставляет предметы, имеющие теги `generic` ИЛИ `port`. Предметы с тегом `temple` исключаются.
3.  **Filter (Container):** Если это "Аптечка" (`Medcase`), оставляет только теги `meds` + `stimulators`.
4.  **Roll Rarity (Tier 2 Modifier):**
    * Бросок d100.
    * Если результат > 80 -> **Rare**.
    * Если результат > 40 -> **Uncommon**.
    * Иначе -> **Common**.
5.  **Spawn:** Предмет помещается в слот.

---

## 5. Глобальные Таблицы Лута (Global Tables)
Некоторые предметы игнорируют биомы (универсальный лут).

* **Global_Trash:** (`Scrap`, `Cloth`, `Tape`) — спавнится везде.
* **Currency:** (`Rez`) — спавнится только в:
    * Сейфах (`Safe`).
    * Кассах.
    * Карманах курток.
    * *Шанс спавна Реза скалируется от Тира (в Т3 пачки денег жирнее).*

## 6. Связь с Мобами
Лут с мобов (описанный в `Registry_Mobs`) обрабатывается отдельно.
* Моб `[mob:: scavenger]` в Т1 имеет ржавый пистолет.
* Тот же моб в Т3 может иметь тот же пистолет, но с лучшими патронами или модами.