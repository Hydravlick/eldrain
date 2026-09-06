---
type: view
status: active
system: feature_navigation
view_kind: feature_map
upstream_sources: ["[[01_Core_Vision/Features/Pawn_Lifecycle]]", "[[01_Core_Vision/Features/Expedition_Preparation]]", "[[01_Core_Vision/Features/Raid_Entry]]", "[[01_Core_Vision/Features/Exploration_Traversal]]", "[[01_Core_Vision/Features/Combat]]", "[[01_Core_Vision/Features/Looting_Carry]]", "[[01_Core_Vision/Features/Extraction]]", "[[01_Core_Vision/Features/Loot_Return]]", "[[01_Core_Vision/Features/Contracts]]", "[[01_Core_Vision/Features/Living_Table]]", "[[01_Core_Vision/Features/Resource_Addressing]]", "[[01_Core_Vision/Features/Living_World]]", "[[01_Core_Vision/Features/Personal_Development]]", "[[01_Core_Vision/Features/Knowledge_Investigation]]"]
navigation_role: "Feature_Map"
navigation_order: 3
navigation_label: "Возможности игрока"
---

# Возможности игрока

Начните с [[01_Core_Vision/GDD_Main]], [[01_Core_Vision/01_Vision]] и [[01_Core_Vision/02_Core_Loop]]. Эта карта показывает законченные возможности, из которых складывается путь игрока. Она читает Feature-страницы и не определяет правила. Конкретное правило ищите через [[00_Index|доменные маршруты]].

1. [[01_Core_Vision/Features/Pawn_Lifecycle|Живые Пешки и цена возвращения]]
2. [[01_Core_Vision/Features/Expedition_Preparation|Снарядиться под вылазку]]
3. [[01_Core_Vision/Features/Raid_Entry|Выбрать подход и войти в рейд]]
4. [[01_Core_Vision/Features/Exploration_Traversal|Прочитать место и проложить маршрут]]
5. [[01_Core_Vision/Features/Combat|Выбрать действие и пережить ответ]]
6. [[01_Core_Vision/Features/Looting_Carry|Найти, выбрать и унести]]
7. [[01_Core_Vision/Features/Extraction|Решить, когда уходить]]
8. [[01_Core_Vision/Features/Loot_Return|Вернуть вещь и разобраться с последствиями]]
9. [[01_Core_Vision/Features/Contracts|Выполнить работу и принять её цену]]
10. [[01_Core_Vision/Features/Living_Table|Вернуться к живому Столу]]
11. [[01_Core_Vision/Features/Resource_Addressing|Найти добыче применение]]
12. [[01_Core_Vision/Features/Living_World|Выбрать момент в меняющемся мире]]
13. [[01_Core_Vision/Features/Personal_Development|Прожить собственную историю Пешки]]
14. [[01_Core_Vision/Features/Knowledge_Investigation|Собрать свидетельства и понять находку]]

## Обещание, связи и готовность

```dataview
TABLE WITHOUT ID link(file.path, display_name) AS "Feature", player_promise AS "Обещание", expected_dynamics AS "Гипотеза динамики", system_owners AS "Владельцы", ux_surfaces AS "UX", data_sources AS "Данные", maturity AS "Зрелость", mvp_scope AS "MVP", validation_state AS "Проверка"
WHERE type = "feature" AND status = "active"
SORT feature_order ASC
```

Двусторонние связи и пропуски: [[01_Core_Vision/Views/Feature_Owner_Coverage]]. Текущие работы: [[09_Project_Management/TODO]]; риски и свидетельства: [[09_Project_Management/Risk_Register]].
