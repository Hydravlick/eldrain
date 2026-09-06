---
type: feature
status: active
system: player_experience
feature_id: loot_return
feature_order: 8
display_name: Вернуть вещь и разобраться с последствиями
player_promise: Увидеть, что вернулось, кому принадлежит и какая обработка ещё нужна.
expected_dynamics: Игрок понимает последствия находки и выбирает обработку вместо обязательной послерейдовой бухгалтерии.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[06_Economy_Loot/Return_Manifest_Contract]]"
  - "[[06_Economy_Loot/Extraction_Stabilization_Loop]]"
  - "[[06_Economy_Loot/Loot_Sync_Cycle]]"
  - "[[07_Gear_Inventory/Stash_Architecture]]"
  - "[[07_Gear_Inventory/Inventory_Architecture]]"
data_sources:
  - "[[07_Gear_Inventory/Registries/Registry_Items]]"
  - "[[03_Factions_Societies/Registries/Registry_Faction_Interfaces]]"
ux_surfaces:
  - "[[07_Gear_Inventory/Item_Attributes_UI]]"
  - "[[08_World_Generation/Hub/Hub_Map_Table]]"
production_disciplines:
  - UX
  - audio
  - narrative
  - gameplay
  - QA
validation:
  - "[[01_Core_Vision/Features/Loot_Return#Проверка гипотезы]]"
---

# Вернуть вещь и разобраться с последствиями

Увидеть, что вернулось, кому принадлежит и какая обработка ещё нужна.

Сохранить значение физического возврата и происхождения находки после рейда.

## За минуту

Итог вылазки показывает человека отдельно от доставленного состава. Манифест переносит допустимые ItemID в общий Схрон. Stable-вещь доступна сразу; Volatile, спорный след или живой груз ведут к своей процедуре, а не к общей кнопке очистки.

## Сценарии и границы

- Обычный возврат стабильного предмета и его использование в следующей подготовке.
- Volatile доставлен, но ещё требует Напоминания.
- Передача спорного груза не стирает происхождение.
- Повторная доставка после технического сбоя сверяет прежний commit.
- STANDARD Dawn проецирует вещевой результат принятого личного решения.

Не смешивать стабилизацию мира с сохранением личной добычи и не начислять контракт по любому возвращению.

## Кто исполняет и что видит игрок

Правила и переходы: [[06_Economy_Loot/Return_Manifest_Contract]], [[06_Economy_Loot/Extraction_Stabilization_Loop]], [[06_Economy_Loot/Loot_Sync_Cycle]], [[07_Gear_Inventory/Stash_Architecture]], [[07_Gear_Inventory/Inventory_Architecture]].

Данные и авторские экземпляры: [[07_Gear_Inventory/Registries/Registry_Items]], [[03_Factions_Societies/Registries/Registry_Faction_Interfaces]].

Игроковые экраны, сигналы и объяснение отказа: [[07_Gear_Inventory/Item_Attributes_UI]], [[08_World_Generation/Hub/Hub_Map_Table]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Игрок понимает последствия находки и выбирает обработку вместо обязательной послерейдовой бухгалтерии.

- **Наблюдаем:** Без подсказки ведущего игрок различает доставлено, стабильно и допустимо к выбранной сделке.
- **Доказательство и способ наблюдения:** Разбор послерейдового экрана, возврата после сбоя и цепочек передачи/обработки.
- **Опровержение:** Возврат Stable-вещи требует ритуальных лишних действий либо состояние происхождения выглядит произвольной блокировкой.
- **Ответ:** Пересмотреть объяснение причин и лишние UI-шаги; preserve provenance проверять отдельно от удобства.

## MVP и производство

Первый срез: Один физически вынесенный ItemID, спорный manifest и повторная доставка результата; игрок видит один итоговый возврат. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

Не обещать определённость unresolved Dawn-ветвей тегов и Closure через экран манифеста.

Gameplay связывает custody и durable manifest; UX объясняет судьбу каждого спорного предмета; QA проверяет повтор, reconnect и сбой между подготовкой и commit.
