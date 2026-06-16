---
type: index
system: navigation
version: 4.0
status: active
tags: [master_index, gdd, navigation, refactor]
---
# ЭЛДРЕЙН: Навигатор v4.0

> **Жанр:** Hardcore PvPvE Extraction FPS  
> **Сеттинг:** Magipunk / Scavenger-Fantasy  
> **Цикл:** Хаб -> Рейд -> Эвакуация -> Экономика  
> **Игрок:** Кукловод / Оператор

## Быстрый доступ

| Блок | Суть | Войти |
|:---|:---|:---|
| 01. Ядро | Видение, тон, базовый цикл | [[01_Core_Vision/01_Vision]] |
| 02. Лор | Законы мира, Якорь, Энтропия, магипанк | [[02_World_Lore/01_Cosmogony]] |
| 03. Фракции | Общества, репутация, печати, контракты | [[03_Factions_Societies/Registry_Factions]] |
| 04. Пешки | Сосуды, найденыши, расы, классы, T.O.U.C.H. | [[04_Player_Entities/Shell_Specification]] |
| 05. Бой | Оружие, акустика, статусы, выживание | [[05_Combat_Survival/Weapon_Core]] |
| 06. Экономика | Рез, бартер, аукцион, инфляция, лут | [[06_Economy_Loot/Economy_Core]] |
| 07. Снаряжение | Инвентарь, предметы, крафт, схрон | [[07_Gear_Inventory/Inventory_Architecture]] |
| 08. Мир | Генерация, аномалии, сервер, хаб, POI | [[08_World_Generation/Generation/07_Server_Lifecycle]] |
| 09. Разработка | MVP, задачи, техдолг, планы | [[09_Project_Management/TODO]] |

## 01. Ядро и видение

```dataview
TABLE status as "Статус", type as "Тип"
FROM "01_Core_Vision"
SORT file.name ASC
```

## 02. Мироустройство и лор

```dataview
TABLE status as "Статус", tags as "Теги"
FROM "02_World_Lore"
SORT file.name ASC
```

## 03. Фракции и общества

```dataview
TABLE type as "Тип", system as "Система", status as "Статус"
FROM "03_Factions_Societies"
SORT file.folder ASC, file.name ASC
```

## 04. Персонажи и прогрессия

```dataview
TABLE type as "Тип", system as "Система", status as "Статус"
FROM "04_Player_Entities"
SORT file.folder ASC, file.name ASC
```

## 05. Бой, магия и выживание

```dataview
TABLE type as "Тип", system as "Система", status as "Статус"
FROM "05_Combat_Survival"
SORT file.name ASC
```

## 06. Экономика и лут

```dataview
TABLE type as "Тип", system as "Система", status as "Статус"
FROM "06_Economy_Loot"
SORT file.name ASC
```

## 07. Инвентарь, предметы и крафт

```dataview
TABLE type as "Тип", system as "Система", status as "Статус"
FROM "07_Gear_Inventory"
SORT file.folder ASC, file.name ASC
```

## 08. Генерация, аномалии и сервер

```dataview
TABLE type as "Тип", system as "Система", status as "Статус"
FROM "08_World_Generation"
SORT file.folder ASC, file.name ASC
```

## 09. Активные задачи

```dataview
TASK
FROM "09_Project_Management"
WHERE !completed
SORT file.name ASC
```

## Архив

Архивные дубликаты и безымянные заметки разобраны. Карта переноса сохранена в [[_Archive/_MERGED_SOURCES]].
