---
status: active
system: inventory_ui
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
index_summary: "Определяет состояния, разрешение и связи: Кукла Персонажа (Equipment Slots)."
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

### В. Оружие и Логистика (Weaponry)
Логика слотов построена на **размере**, а не на типе.

1.  **Primary Holster (Спина/Ремень):**
    * Для двуручного оружия (конденсаторы, веерные эмиттеры, тяжелые арбалеты, копья).
2.  **Secondary Holster (Бедро/Грудь):**
    * Для одноручного оружия (ручные разрядники, ножи, клещи).
3.  **Ammunition Logic (Боезапас):**
    * У оружия **нет своего инвентаря** для боеприпасов.
    * **Магострелы/Арбалеты:** Для перезарядки (R) система ищет *Батареи* или *Болты* в зоне **Ready Access**.
    * *Если батарея в рюкзаке:* Перезарядка невозможна, пока игрок не подготовит ее для быстрого доступа.

---
## 3. Визуализация
У мастера сначала выбираются Пешка и модель Термоса. Кукла показывает nodes, допустимые mount patterns, затронутые service families и `service_load` каждого модуля. До подтверждения игрок видит единый список причин отказа и доменные проекции массы, Диссонанса, эффектов и покрытия. Покрытие показывает тот же Ballistics-owned `ResolvedCoverageSnapshot`, который использует hit resolver; PaperDoll не строит собственную геометрию.

В Аномалии экран работает только на чтение: видны установленные, повреждённые и отключённые модули, но перетаскивание недоступно. Маска остаётся отдельным предметом, а визуальная отделка не скрывает фактическую геометрию Термоса.
