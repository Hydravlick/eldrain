---
type: mechanic
status: active
index_route: owner
index_group: gear_inventory
index_order: 160
index_summary: "Задаёт правила и последствия системы «Система: Удобство и Сортировка (QoL)»."
read_when: "Читайте при изменении входов, состояний, стоимости или последствий системы «Система: Удобство и Сортировка (QoL)»."
system: inventory
tags:
  - qol
  - ui
  - sorting
  - controls
related_files:
  - "[[06_Economy_Loot/Extraction_Stabilization_Loop|Extraction_Stabilization_Loop]]"
---
# Система: Удобство и Сортировка (QoL)

## 1. Контекстная Иерархия Сортировки
Кнопка "Auto-Sort" не приравнивает редкость к полезности. По умолчанию она поднимает предметы, для которых у игрока уже есть решение.

**Приоритет Сортировки:**
1.  **Pinned / Contract / Reserved:** отмеченное игроком, квестовое и зарезервированное под известный рецепт.
2.  **Interaction Zone:** Ready Access, Back Slot, обычный груз.
3.  **Known Address:** мастер, Очаг, рецепт, разбор или собственный билд.
4.  **Reliability:** Trace/Disputed, Volatile, Stable.
5.  **Rarity:** Legendary -> Epic -> Rare -> Common -> Rusty внутри одной смысловой группы; Реликвия отмечается происхождением, а не местом в цветовой очереди.
6.  **Weight:** от тяжёлого к лёгкому либо по `value/kg`, если игрок выбрал этот фильтр.

### Пример результата сортировки:
1.  *[T3] [Purple] Heavy Plasma Cannon (12 kg)*
2.  *[T3] [Purple] Neural Chip (0.1 kg)*
3.  *[T3] [Blue] Steel Plate (5 kg)*
4.  *[T2] [Purple] Old Generator (15 kg)*
5.  *[T2] [Green] Bandage (0.1 kg)*

## 2. Визуальные Разделители
В списке инвентаря тонкие горизонтальные линии могут разделять редкость, но не должны сообщать ложную границу между «хорошим лутом» и «мусором».

Рядом с цветом редкости показываются независимые признаки:

- `Stable / Volatile / Trace`;
- `Native / Foreign / Hot` в рейде;
- известный мастер, контракт или рецепт;
- Ready Access, обычный груз или Back Slot;
- закреплённый игроком приоритет `оставить / использовать / разобрать / отдать`.

Common/серый предмет может быть критичным для ремонта или рецепта. Интерфейс не предлагает автоматическую продажу или выброс только по цвету редкости.

## 3. Быстрый Перенос (Quick Transfer)
* **`Shift + Click`:** Перенос между "Рюкзаком" и "Схроном/Трупом".
* **`Alt + Click`:** Перенос между рюкзаком и `Ready Access`, если позволяет вес и число готовых позиций.


Быстрый перенос применяется в сфокусированном UI-контексте управления переносом, по [[01_Core_Vision/Input_Contract|input collision policy]]. Он создаёт запрос Inventory preparation с её физической ценой, а не мгновенный Weapon Set switch. Перенос или Auto-Sort не переставляют Set channels и не подтверждают actual hand availability.

В экране управления Схроном Alt+Click может выполнять его локальную операцию Lock. Экран явно выбирает один контекст; одна комбинация не запускает Lock, Quick Transfer и gameplay Weapon Focus одновременно. Закрытие UI не превращает удерживаемый Alt или кнопку мыши в новое боевое намерение.

## Player Menu / Inventory

UI владеет persistent-open и temporary-open состояниями одного Player Menu / Inventory. [[01_Core_Vision/Input_Contract|Input Contract]] владеет binding и различением tap/hold. Tab down сначала создаёт pending intent, не открывает постоянное меню. Поэтому короткое нажатие не вызывает вспышку temporary view, а удержание не создаёт лишний persistent toggle.

| Исходное состояние | Событие | Результат |
|---|---|---|
| closed | tap: release до threshold | persistently open |
| persistent | tap | closed |
| closed | hold threshold crossed | temporarily open |
| temporary | release после hold | closed |
| persistent | hold threshold crossed, затем release | persistent сохраняется |

```yaml
player_menu_contract:
  intent: player_menu
  key_down: pending_only
  closed_tap: persistent
  persistent_tap: closed
  closed_hold_threshold: temporary
  temporary_release: closed
  persistent_hold_release: persistent
  threshold: prototype_bound_accessibility
```

При удержании, начатом поверх уже persistent-open меню, release ничего не закрывает. Явное закрытие меню отдельным UI action аннулирует pending/temporary intent; его поздний release не открывает меню заново. Сфокусированное text input имеет однозначный routing и не отправляет Tab в gameplay.

Этот контракт задаёт только invocation. Он не устанавливает pause, time dilation, cursor policy, multiplayer time, доступность манипуляций при опасности или состав панелей. Quick Transfer по-прежнему создаёт запрос физической операции, а не отменяет её цену.
