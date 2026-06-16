---
type: kanban
status: active
system: project_management
tags: [todo, roadmap, mvp, project_management]
sources:
  - "[[09_Project_Management/TO-DO_List_Legacy]]"
  - "[[09_Project_Management/Action_Plan_Update]]"
  - "[[09_Project_Management/Lore_Update]]"
---
# Единая доска задач

> Цель: держать развитие Элдрейна в одном рабочем месте, а старые списки использовать как источник деталей.

## Now: фундамент MVP

- [ ] **First-Person Controller:** body awareness, procedural sway, free look.
- [ ] **Вес оружия:** инерция прицела, задержка после спринта, физическое ощущение массы.
- [ ] **Projectile combat:** отказаться от hitscan, описать скорость, падение и стабилизацию дыхания.
- [ ] **Melee commitment:** sweet spots, impact stop, дистанция как часть мастерства.
- [x] **Loop Pacing:** закрепить 6-часовой цикл локации, 10-45+ минут личного рейда и фазовый серфинг через Gate Check.
- [x] **Environment Gatekeeping:** добавить давление среды, типы угроз и сопротивление среды в биомы/снаряжение.
- [ ] **Loot Stabilization:** добить UI и стоимость стабилизации; базовая логика `Volatile` -> `Stabilized` уже уточнена в экономике.
- [ ] **Foundlings:** капсулы как лут, ограничения переноски, отличие сосудов от найденышей.

## Next: системная связность

- [ ] **Разделение магии:** магия тела платит здоровьем/рассудком, артефакты платят батареями.
- [ ] **Инвентарь в рейде:** лутание без паузы, отвязка курсора, drag & drop, поворот предметов.
- [ ] **Физическая броня:** manual tanking, sprint guard, head-duck mechanic.
- [ ] **Аукцион душ:** продажа капсул 3+ уровня, просмотр модели, перков и травм.
- [ ] **Roster UI:** карточки пешек, состояние, история травм, пригодность под контракт.
- [ ] **Mutation trigger:** выдача трейтов после эвакуации на основе лога боя.
- [x] **Tutorial Debt:** первый долг перед Синдикатом и обучение через погашение процента.

## Two-Paradox: баланс векторов

- [x] Перенести идею “Рождение Двойного Парадокса” из корня в блок персонажей.
- [x] Создать рабочую матрицу 7 тактических векторов.
- [x] Проставить базовые `weak_to` для текущих рас.
- [x] Проставить базовые `weak_to` для текущих классов.
- [x] Научить `00_Character_Matrix` выводить общую слабость пары `race + spec`.
- [x] Привязать теги мутаций к пересчету `add_vector` / `block_vector`.
- [x] Проверить оружие и броню на соответствие векторам Двойного Парадокса.
- [x] Зафиксировать pipeline `Race + Spec -> Combo P/Q/E -> Allowed Arsenal -> Tags -> Proficiency Gates -> Combat Profile`.
- [ ] Расширить DataviewJS до полного учета активных тегов конкретной Оболочки.
- [ ] Вынести RaceList/SpecList/RaceBanned из дизайна в структурные поля рас и классов, если combo-арсенала станет мало.

## Later: контент и полировка

- [ ] **The Keeper's Breach:** событие после первой эвакуации персонажа 10-го уровня.
- [ ] **Anchor Hall:** тир, демонстрация зон брони, безопасный онбординг.
- [ ] **Volatile visuals:** мерцание/глитч для нестабильных предметов.
- [ ] **Audio pass:** звук стабилизации, звук подбора глюка, индустриальный тон интерфейса.
- [ ] **Squad identification:** близкие руны/метки свой-чужой для тумана и плохой видимости.
- [ ] **Monsters as entropy:** закрепить лор мобов и volatile-лут в реестре мобов.

## Refactor cleanup

- [ ] Проверить Dataview-матрицы после переноса реестров.
- [x] Сравнить архивный `Physical_Weight_v2` и [[07_Gear_Inventory/Physical_Weight]]; перенести формулы v2 в канонический файл.
- [x] Проверить [[03_Factions_Societies/Quest_Engine]] и [[03_Factions_Societies/Quest_Engine_Grammar]]; оставить грамматику как актуальную, старую слоистую версию зафиксировать в [[_Archive/_MERGED_SOURCES]].
- [x] Очистить `_Archive` после мержа и оставить единый merge-log.
- [ ] Решить судьбу [[04_Player_Entities/_Registries/Registry_Races]]: заполнить или перенести в архив после подтверждения.
- [ ] Проверить пустые старые папки `Lang_RU` и `New`; удалить вручную после проверки Obsidian.

## Legacy sources

- [[09_Project_Management/TO-DO_List_Legacy]] - полный старый список задач.
- [[09_Project_Management/Action_Plan_Update]] - актуализация механик: среда, стабилизация лута, найденыши, магия.
- [[09_Project_Management/Lore_Update]] - нарративные заметки для последующей интеграции.
- [[09_Project_Management/Architecture_MVP]] - техническая архитектура MVP.
- [[09_Project_Management/Generation_Algorithm_Notes]] - заметки по алгоритму генерации.
