---
type: mechanic
system: world_map
tags:
  - map
  - rotation
  - elements
  - biomes
related_files:
  - "[[Lang_RU/10_Mechanics/05_World_Systems/Systems/City_Structure_Generation|City_Structure_Generation]]"
  - "[[Lang_RU/10_Mechanics/05_World_Systems/Systems/Anomaly_System|Anomaly_System]]"
---

# Глобальный Атлас: Топология и Элементы

> **Концепция:** Мир Элдрейна — это "Дерево", растущее из Хаба. Корни стабильны, но ветви (дальние сектора) постоянно меняются под воздействием Эфирных Приливов.

---

## 1. Топология: Система "Корень и Ветви"

Карта мира состоит из **Узлов (Nodes)** и **Связей (Links)**.

### А. Стабильный Корень (The Root)
Эти локации существуют всегда. Их топология фиксирована, меняются только детали (декор, лут).

1.  **HUB (Центральный Банк/Собор):**
    * *Статус:* Безопасная зона.
    * *Функция:* Лобби, торговля, крафт.
2.  **GATEWAY (Порт):**
    * *Статус:* PvPvE (Low Risk).
    * *Механика:* Это "бутылочное горлышко". Все игроки начинают здесь.
    * *Генерация:* **Стазис/Глитч** (см. [[Lang_RU/10_Mechanics/05_World_Systems/Systems/City_Structure_Generation|City_Structure_Generation]]). Игроки могут выучить эту карту наизусть.

### Б. Нестабильные Ветви (The Branches)
От Порта отходят 5 выходов (Врала, Магистрали, Тоннели), ведущих в **Глубокие Сектора**.
* Эти сектора процедурно генерируются заново каждую **Ротацию**.
* Именно здесь работают Элементальные Биомы.

**Схема карты:**
```text
       [Deep Sector A] — (Hard)
            |
       [Deep Sector B] — (Medium)
            \
[HUB] —> [PORT (Gate)] —> [Deep Sector C] — (Medium)
            /
       [Deep Sector D] — (Hard)
            |
       [Deep Sector E] — (Hell / Raid Boss)