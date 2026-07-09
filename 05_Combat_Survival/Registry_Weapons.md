---
type: registry
status: active
system: combat_survival_registry
registry_type: weapon_frames
tags:
  - database
  - equipment
  - frames
related_files:
  - "[[05_Combat_Survival/Combat_Three_Debts|Combat_Three_Debts]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[04_Player_Entities/Combat_Profile_Pipeline|Combat_Profile_Pipeline]]"
  - "[[04_Player_Entities/_Registries/Registry_Combos|Registry_Combos]]"
---
# Реестр: фреймы оружия

> Оружие определяется фреймом, вариантом и паттерном. Фрейм задаёт форму обязательства: чем игрок угрожает, на какое окно ставит темп и чем становится наказуем во время действия.

> [!TODO] Оружейные взаимодействия с линиями мутаций
> - [ ] Определить теги для локального выжигания роста, безопасной проверки мимика и переноса сигнальной метки без универсального «правильного оружия».
> - [ ] Проверить цену шума: быстрый ответ против Корнехвата или Двереглота должен менять риск встречи со стандартной экосистемой.
> - **Основа:** [[08_World_Generation/_Registries/Registry_Anomaly_Mutations|Registry_Anomaly_Mutations]]. Урон, дальность и имплициты этой правкой не меняются.

> [!TODO] Калибровка фреймов
> - [ ] Проверить коридор летальности `spark_handcannon 45` против `condenser_longframe 75` на HP, пластинах, точности, полном цикле заряда, Heat, Pulse и стоимости потери; разница одиночного урона сама по себе не доказывает ни норму, ни нарушение прогрессии.

## Правило реестра

Канонические данные каждого фрейма хранятся на странице самого фрейма в `05_Combat_Survival/Weapons/`. Этот реестр только собирает семейство, как [[03_Factions_Societies/_Registries/Registry_Factions|Registry_Factions]] собирает фракции.

Фрейм может иметь `frame_vector`, но это не `base_vector`, не третий архетипный вектор и не новый источник `weak_to`.

```text
base_vector = кто Пешка по телу и практике
frame_vector = чем она временно выставилась во время обязательства
```

`frame_vector` активен только в фазах из `activates_on`: замах, прицеливание, удержание заряда, выстрел, блок, recovery. Он нужен для статистики экспозиции и компактной панели "чем это наказать сейчас", а не для пересчёта Двойного Парадокса.

## Контракт фрейма

```yaml
type: weapon_frame
frame_id: condenser_longframe
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on: [aim_hold, charge, shot_recovery]
primary_window_function: create
creates_window: [weakspot_open]
exploits_window: [exposed_weakspot]
mitigates_window: [none]
exposure_channels: [open_line, flank, charge_interrupt, heat]
frame_power: 4
exposure_weight: 4
mastery_unlock: [stable_charge_cancel]
```

- `weapon_family` — семейство допуска и proficiency: `blade`, `blunt`, `polearm`, `arcanegun`, `catalyst`, `shield`.
- `frame_vector` — временный вектор обязательства, используемый только для moment/exposure-аналитики.
- `vector_scope: commitment` — обязательная метка, отделяющая фрейм от архетипных векторов.
- `activates_on` — фазы, где экспозиция видима и наказуема.
- `frame_power` — черновая шкала 1-5: насколько фрейм создаёт, использует или закрывает окно.
- `exposure_weight` — черновая шкала 1-5: насколько дорого промахнуться, задержаться или быть прерванным.
- `mastery_unlock` — что открывает высокий proficiency: техника, стабильность, cancel, темп или снижение экспозиции, но не новый активный вектор.

## Главный MVP

`handcannon / spark_handcannon` является якорем MVP-оружия. Он не самый сильный и не самый безопасный фрейм; он лучше всех показывает сеттинг в одном раннем обмене: батарея становится импульсом, импульс даёт `stagger_entry`, выстрел оставляет Heat, DissonancePulse, шум, bloom и Recovery, а бой всё ещё требует добивания, позиции или отхода.

Главный MVP не заменяет мили и не превращает магострел в современный DPS. Он доказывает базовый язык Элдрейна: оружие создаёт временное окно и временную экспозицию.

## Взвешивание фреймов

```text
MVP Fit =
  mvp_signal
  + mvp_readability
  + mvp_coverage
  - mvp_dominance_risk
  - mvp_fantasy_drift_risk
```

- `mvp_signal` — насколько фрейм сразу показывает магипанк, батареи, Диссонанс, аномальность и цену действия.
- `mvp_readability` — насколько игрок понимает угрозу, окно и наказание без чтения таблиц.
- `mvp_coverage` — сколько MVP-задач фрейм помогает проверить: PvE, PvP, темп, маршрут, команда, экономика потери.
- `mvp_dominance_risk` — насколько легко фрейм станет скучным универсальным ответом.
- `mvp_fantasy_drift_risk` — насколько фрейм тянет игру в обычное фентези/RPG вместо Элдрейна.

```dataview
TABLE WITHOUT ID
  file.link AS "Фрейм",
  mvp_fit AS "Fit",
  mvp_verdict AS "Вердикт",
  mvp_signal AS "Сеттинг",
  mvp_readability AS "Чтение",
  mvp_coverage AS "Покрытие",
  mvp_dominance_risk AS "Риск доминации",
  mvp_fantasy_drift_risk AS "Риск RPG",
  mvp_reason AS "Почему"
FROM "05_Combat_Survival/Weapons"
WHERE type = "weapon_frame"
SORT mvp_fit DESC, sort_order ASC
```

Формула аудита:

```text
Doctrine Score =
  Core Fit
  + Frame Power
  + Threat Coverage
  - Exposure Weight
  - Resource Burn
  - Weight / Carry Tax
```

Точные числа остаются предметом прототипа. Они не являются Gear Score.

## Фреймы

```dataview
TABLE WITHOUT ID
  file.link AS "Фрейм",
  weapon_family AS "Семейство",
  frame_vector AS "Commitment",
  primary_window_function AS "Работа",
  join(creates_window, ", ") AS "Создаёт",
  join(exploits_window, ", ") AS "Использует",
  join(mitigates_window, ", ") AS "Закрывает",
  frame_power AS "Power",
  exposure_weight AS "Exposure"
FROM "05_Combat_Survival/Weapons"
WHERE type = "weapon_frame"
SORT sort_order ASC
```

## Варианты

```dataview
TABLE WITHOUT ID
  file.link AS "Фрейм",
  variant_id AS "Вариант",
  tier AS "T",
  weight AS "Вес",
  dmg AS "Урон",
  implicit AS "Implicit",
  implicit_rule AS "Правило",
  input_pattern AS "Ввод",
  combo_reset AS "Reset",
  dissonance_pulse AS "Pulse"
FROM "05_Combat_Survival/Weapons"
WHERE type = "weapon_frame"
SORT sort_order ASC
```

## Оружие в MVP-комбинациях

```dataviewjs
const comboPath = "04_Player_Entities/_Registries/Registry_Combos.md";
const comboSource = await dv.io.load(comboPath);
const clean = value => value ? String(value).trim() : "";
const field = (line, key) => line.match(new RegExp(`\\[${key}::\\s*([^\\]]+)\\]`, "i"))?.[1]?.trim();
const displayName = header => header.replace(/\s*\(.*?\)\s*/g, "").trim();

const weaponPages = Array.from(dv.pages('"05_Combat_Survival/Weapons"'))
  .filter(page => page.type === "weapon_frame");
const byVariant = new Map(weaponPages.map(page => [clean(page.variant_id), page]));
const byFrame = new Map(weaponPages.map(page => [clean(page.frame_id), page]));

const rows = comboSource.split(/^##\s+/m).slice(1).flatMap(block => {
  const lines = block.split("\n");
  const header = clean(lines[0]);
  const body = lines.slice(1).join("\n");
  const comboId = body.match(/\[id::\s*([^\]]+)\]/i)?.[1]?.trim();
  if (!comboId || comboId.startsWith("template_")) return [];

  return lines
    .filter(line => line.includes("[weapon_instance::"))
    .map(line => {
      const instanceId = clean(field(line, "weapon_instance"));
      const frameId = clean(field(line, "weapon_frame"));
      const prof = clean(field(line, "prof"));
      const role = clean(field(line, "combat_role"));
      const weapon = byVariant.get(instanceId) || byFrame.get(frameId);
      return [
        dv.sectionLink(comboPath, header, false, displayName(header)),
        prof || "⚠️",
        role || "—",
        weapon?.file?.link || `⚠️ ${instanceId || frameId || "missing"}`,
        weapon?.implicit || "⚠️",
        weapon?.implicit_rule || "⚠️",
        weapon?.input_pattern || "⚠️"
      ];
    });
});

if (rows.length) {
  dv.table(["Комбо", "Prof", "Роль", "Оружие", "Implicit", "Правило", "Ввод"], rows);
} else {
  dv.paragraph("⚠️ Нет `[weapon_instance:: ...]` в Registry_Combos.");
}
```

## Проверки

Пустая таблица ниже означает, что проверка не нашла проблем.
```dataview
TABLE WITHOUT ID
  file.link AS "Фрейм",
  frame_id AS "frame_id",
  vector_scope AS "scope",
  activates_on AS "activates_on",
  mastery_unlock AS "mastery",
  implicit AS "implicit",
  implicit_rule AS "implicit_rule",
  input_pattern AS "input"
FROM "05_Combat_Survival/Weapons"
WHERE type = "weapon_frame"
  AND (vector_scope != "commitment"
    OR !activates_on
    OR !mastery_unlock
    OR !variant_id
    OR !implicit
    OR !implicit_rule
    OR !input_pattern
    OR implicit_rule = "UNKNOWN"
    OR input_pattern = "UNKNOWN"
    OR sweet_spot_range = "UNKNOWN")
SORT sort_order ASC
```
