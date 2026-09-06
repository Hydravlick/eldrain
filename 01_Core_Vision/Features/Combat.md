---
type: feature
status: active
system: player_experience
feature_id: combat
feature_order: 5
display_name: Выбрать действие и пережить ответ
player_promise: Использовать оружие, способности и среду, чтобы создать окно, воспользоваться им или уйти из боя.
expected_dynamics: Игрок объясняет поражение доступным окном и пробует другой ответ, а не только более дорогой предмет.
maturity: specified
mvp_scope: vertical_slice_subset
validation_state: untested
system_owners:
  - "[[04_Player_Entities/Skill_Execution]]"
  - "[[04_Player_Entities/Interaction_Constraints]]"
  - "[[05_Combat_Survival/Combat_Three_Debts]]"
  - "[[05_Combat_Survival/Weapon_Core]]"
  - "[[04_Player_Entities/Skill_Build_Philosophy]]"
  - "[[05_Combat_Survival/Ballistics_Armor]]"
  - "[[05_Combat_Survival/Combat_Consumables]]"
  - "[[05_Combat_Survival/Status_Effects]]"
  - "[[05_Combat_Survival/Magic_Batteries]]"
  - "[[05_Combat_Survival/Dissonance_System]]"
ux_surfaces:
  - "[[05_Combat_Survival/Weapon_Manifesto]]"
  - "[[07_Gear_Inventory/Item_Attributes_UI]]"
production_disciplines:
  - animation
  - audio
  - VFX
  - UX
  - gameplay
  - QA
validation:
  - "[[01_Core_Vision/Features/Combat#Проверка гипотезы]]"
data_sources: ["[[05_Combat_Survival/Registries/Registry_Weapons]]", "[[04_Player_Entities/Registries/Registry_Combos]]", "[[05_Combat_Survival/Registries/Registry_StatusEffects]]", "[[08_World_Generation/Registries/Registry_Mobs]]", "[[08_World_Generation/Content/Hunt_Frontier_Slice]]"]
---

# Выбрать действие и пережить ответ

Использовать оружие, способности и среду, чтобы создать окно, воспользоваться им или уйти из боя.

Сделать сильное действие читаемым обязательством с доступным ответом.

## За минуту

Игрок читает угрозу, выбирает канал, входит в Commitment и получает эффект вместе с долгом. Противник отвечает через геометрию, окно или ресурс; Recovery оставляет цену выбора видимой до следующего действия.

## Сценарии и границы

- Обмен попаданиями с понятным телеграфом и ответом.
- Смена оружия после сильного действия не стирает долг.
- Помощь союзника проходит через уязвимое применение.
- PvE вмешивается в PvP: стороны читают новый след и могут сменить роль.

Не добавлять общий лист атрибутов, обязательного healer или бесплатную готовность всех каналов.

## Кто исполняет и что видит игрок

Правила и переходы: [[04_Player_Entities/Skill_Execution]], [[04_Player_Entities/Interaction_Constraints]], [[05_Combat_Survival/Combat_Three_Debts]], [[05_Combat_Survival/Weapon_Core]], [[04_Player_Entities/Skill_Build_Philosophy]], [[05_Combat_Survival/Ballistics_Armor]], [[05_Combat_Survival/Combat_Consumables]], [[05_Combat_Survival/Status_Effects]], [[05_Combat_Survival/Magic_Batteries]], [[05_Combat_Survival/Dissonance_System]].

Данные и авторские экземпляры: [[05_Combat_Survival/Registries/Registry_Weapons]], [[04_Player_Entities/Registries/Registry_Combos]], [[05_Combat_Survival/Registries/Registry_StatusEffects]], [[08_World_Generation/Registries/Registry_Mobs]].

Игроковые экраны, сигналы и объяснение отказа: [[05_Combat_Survival/Weapon_Manifesto]], [[07_Gear_Inventory/Item_Attributes_UI]]. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.

## Проверка гипотезы

**PLAUSIBLE, не проверено:** Игрок объясняет поражение доступным окном и пробует другой ответ, а не только более дорогой предмет.

- **Наблюдаем:** В разборе столкновения обе стороны называют телеграф, обязательство и выполнимую контригру.
- **Доказательство и способ наблюдения:** Запись дуэлей, solo PvE и групповых столкновений с разными уровнями освоения.
- **Опровержение:** Ответ существует лишь в документации, либо дорогая сборка одновременно снимает ресурсный, пространственный и временной риск.
- **Ответ:** Пересмотреть длительность и сигналы окон, геометрию сцены и связанные модификаторы.

## MVP и производство

Первый срез: Одна полная связка тела, Frame и P/Q/E в сцене «Непрошеный гость»: попадание, срыв обязательства, отход и бой с третьей стороной. Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.

TTK, стоимость импульсов и harm-калибровка остаются прототипными; R61 не закрыт.

Animation и gameplay согласуют tell, попадание и Recovery; audio/VFX различают контакт с пластиной и уязвимостью; QA проверяет движущиеся тела, а не неподвижную мишень.
