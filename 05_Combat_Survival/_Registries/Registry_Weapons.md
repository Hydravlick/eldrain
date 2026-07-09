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

Качественная механика принадлежит фрейму. Вариант не дублирует `[implicit:: ...]` или `[implicit_rule:: ...]`; он хранит форму, числа, статус пригодности и семейный ввод.

```yaml
type: weapon_frame
frame_id: handcannon
weapon_family: arcanegun
frame_vector: ballistics
vector_scope: commitment
activates_on: [aim_snap, shot, shot_recovery]
primary_window_function: create
creates_window: [stagger_entry]
exploits_window: [none]
mitigates_window: [none]
exposure_channels: [open_line, noise, heat, reload_timing]
frame_power: 3
exposure_weight: 3
implicit_keyword: stopping_pulse
implicit_rule: "Короткий тяжёлый импульс сбивает вход, спринт или каст, но после выстрела стрелок платит шумом, Heat и recovery."
mastery_unlock: [recoil_recover]
```

- `weapon_family` — семейство допуска и proficiency: `blade`, `blunt`, `polearm`, `arcanegun`, `catalyst`, `shield`.
- `implicit_keyword` — короткое имя качественной механики фрейма.
- `implicit_rule` — читаемое правило поведения фрейма, наследуемое всеми вариантами.
- `vector_scope: commitment` — обязательная метка, отделяющая фрейм от архетипных векторов.
- `activates_on` — фазы, где экспозиция видима и наказуема.
- `frame_power` — черновая шкала 1-5: насколько фрейм создаёт, использует или закрывает окно.
- `exposure_weight` — черновая шкала 1-5: насколько дорого промахнуться, задержаться или быть прерванным.
- `mastery_unlock` — что открывает высокий proficiency: техника, стабильность, cancel, темп или снижение экспозиции, но не новый активный вектор.

## Контракт варианта

```markdown
### Баклер (Buckler) [1H]
[variant_id:: buckler] | [tier:: 1] | [weight:: 1.0kg] | [setting_status:: mvp]
[guard_input:: Tap Parry / Hold Guard] | [guard_mechanic:: parry_window -> active_block]
[combo_reset:: после block_recovery следующий блок снова начинается с cover twitch]

*Маленький кулачный щит.*
- **Отличие:** самый чистый тест точного parry_window.
- **Implicit:** `tight_parry` наследуется от фрейма.
- **Слабость:** окно блока очень маленькое; ошибка оставляет руку и корпус открытыми.
```

Семейные поля ввода:

| Семейство | Поля варианта |
|:---|:---|
| `blade`, `blunt`, `polearm` | `[combo_chain:: ...]`, `[alt_action:: ...]` |
| `arcanegun` | `[fire_input:: ...]`, `[reload_mechanic:: ...]` |
| `shield` | `[guard_input:: ...]`, `[guard_mechanic:: ...]` |
| `catalyst` | `[cast_input:: ...]`, `[draw_mechanic:: ...]` |

`setting_status:: TBD` оставляет вариант в странице фрейма как направление, но скрывает его из общих таблиц и combo-наследования.

## Главный MVP

`handcannon / spark_handcannon` является якорем MVP-оружия. Он не самый сильный и не самый безопасный фрейм; он лучше всех показывает сеттинг в одном раннем обмене: батарея становится импульсом, импульс даёт `stagger_entry`, выстрел оставляет Heat, DissonancePulse, шум, bloom и Recovery, а бой всё ещё требует добивания, позиции или отхода.

Главный MVP не заменяет мили и не превращает магострел в современный DPS. Он доказывает базовый язык Элдрейна: оружие создаёт временное окно и временную экспозицию.

## Взвешивание фреймов

Числа MVP-взвешивания живут в этом представлении, а не в YAML фреймов.

```text
MVP Fit =
  setting_signal
  + readability
  + coverage
  - dominance_risk
  - fantasy_drift_risk
```

```dataviewjs
const audit = {
  handcannon: {fit: 10, setting: 5, read: 5, coverage: 4, dominance: 3, drift: 1},
  harpoon_driver: {fit: 9, setting: 5, read: 4, coverage: 4, dominance: 3, drift: 1},
  condenser_longframe: {fit: 7, setting: 5, read: 4, coverage: 4, dominance: 4, drift: 2},
  scatter_emitter: {fit: 7, setting: 5, read: 4, coverage: 3, dominance: 3, drift: 2},
  catalyst_focus: {fit: 6, setting: 5, read: 3, coverage: 3, dominance: 4, drift: 1},
  hook_polearm: {fit: 2, setting: 2, read: 4, coverage: 3, dominance: 3, drift: 4},
  needle_crossbow: {fit: 2, setting: 2, read: 4, coverage: 2, dominance: 2, drift: 4},
  heavy_impact: {fit: 1, setting: 2, read: 4, coverage: 3, dominance: 4, drift: 4},
  tower_shield: {fit: 1, setting: 2, read: 4, coverage: 3, dominance: 4, drift: 4},
  short_blade: {fit: 0, setting: 1, read: 5, coverage: 2, dominance: 3, drift: 5},
  compact_impact: {fit: 0, setting: 1, read: 4, coverage: 2, dominance: 2, drift: 5},
  reach_polearm: {fit: 0, setting: 1, read: 4, coverage: 3, dominance: 3, drift: 5},
  buckler: {fit: 0, setting: 1, read: 4, coverage: 2, dominance: 2, drift: 5},
  heavy_blade: {fit: -1, setting: 1, read: 4, coverage: 2, dominance: 3, drift: 5},
  needle_blade: {fit: -1, setting: 1, read: 4, coverage: 2, dominance: 3, drift: 5}
};

const frames = Array.from(dv.pages('"05_Combat_Survival/Weapons"'))
  .filter(page => page.type === "weapon_frame")
  .sort((a, b) => (audit[b.frame_id]?.fit ?? -99) - (audit[a.frame_id]?.fit ?? -99));

dv.table(
  ["Фрейм", "Fit", "Вердикт", "Сеттинг", "Чтение", "Покрытие", "Риск доминации", "Риск RPG", "Почему"],
  frames.map(page => {
    const score = audit[page.frame_id] || {};
    return [
      page.file.link,
      score.fit ?? "⚠️",
      page.mvp_verdict || "⚠️",
      score.setting ?? "⚠️",
      score.read ?? "⚠️",
      score.coverage ?? "⚠️",
      score.dominance ?? "⚠️",
      score.drift ?? "⚠️",
      page.mvp_reason || "⚠️"
    ];
  })
);
```

## Фреймы

```dataview
TABLE WITHOUT ID
  file.link AS "Фрейм",
  weapon_family AS "Семейство",
  frame_vector AS "Commitment",
  implicit_keyword AS "Implicit",
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

```dataviewjs
const noWrap = value => `<span style="white-space: nowrap">${value}</span>`;
const field = (text, key) => text.match(new RegExp(`\\[${key}::\\s*([^\\]]+)\\]`, "i"))?.[1]?.trim();
const inputKeys = {
  blade: ["combo_chain", "alt_action"],
  blunt: ["combo_chain", "alt_action"],
  polearm: ["combo_chain", "alt_action"],
  arcanegun: ["fire_input", "reload_mechanic"],
  shield: ["guard_input", "guard_mechanic"],
  catalyst: ["cast_input", "draw_mechanic"]
};

async function variantsFor(page) {
  const text = await dv.io.load(page.file.path);
  return text.split(/^###\s+/m).slice(1).flatMap(section => {
    const lines = section.split("\n");
    const title = lines[0].trim();
    const body = lines.slice(1).join("\n");
    const id = field(body, "variant_id");
    if (!id) return [];
    const status = field(body, "setting_status") || "prototype";
    if (status === "TBD") return [];
    const keys = inputKeys[page.weapon_family] || [];
    const input = keys.map(key => field(body, key)).filter(Boolean).join("<br>");
    return [{
      frame: page,
      title,
      id,
      status,
      tier: field(body, "tier"),
      weight: field(body, "weight"),
      dmg: field(body, "dmg"),
      pulse: field(body, "dissonance_pulse"),
      input,
      reset: field(body, "combo_reset")
    }];
  });
}

const frames = Array.from(dv.pages('"05_Combat_Survival/Weapons"'))
  .filter(page => page.type === "weapon_frame")
  .sort((a, b) => (a.sort_order ?? 999) - (b.sort_order ?? 999));
const variants = (await Promise.all(frames.map(variantsFor))).flat();

dv.table(
  ["Фрейм", "Вариант", "T", "Вес", "Урон", "Implicit", "Ввод", "Reset", "Status"],
  variants.map(item => [
    item.frame.file.link,
    noWrap(item.id),
    item.tier || "—",
    item.weight || "—",
    item.dmg || "—",
    noWrap(item.frame.implicit_keyword || "⚠️"),
    item.input || "⚠️",
    item.reset || "⚠️",
    item.status
  ])
);
```

## Оружие в MVP-комбинациях

```dataviewjs
const comboPath = "04_Player_Entities/_Registries/Registry_Combos.md";
const comboSource = await dv.io.load(comboPath);
const clean = value => value ? String(value).trim() : "";
const field = (text, key) => text.match(new RegExp(`\\[${key}::\\s*([^\\]]+)\\]`, "i"))?.[1]?.trim();
const displayName = header => header.replace(/\s*\(.*?\)\s*/g, "").trim();
const noWrap = text => `<span style="white-space: nowrap">${text}</span>`;

async function variantsFor(page) {
  const text = await dv.io.load(page.file.path);
  return text.split(/^###\s+/m).slice(1).flatMap(section => {
    const body = section.split("\n").slice(1).join("\n");
    const id = field(body, "variant_id");
    if (!id) return [];
    const status = field(body, "setting_status") || "prototype";
    if (status === "TBD") return [];
    return [[id, {page, status}]];
  });
}

const weaponPages = Array.from(dv.pages('"05_Combat_Survival/Weapons"'))
  .filter(page => page.type === "weapon_frame");
const byFrame = new Map(weaponPages.map(page => [clean(page.frame_id), {page, status: "frame"}]));
const byVariant = new Map((await Promise.all(weaponPages.map(variantsFor))).flat());

const rows = comboSource.split(/^##\s+/m).slice(1).reduce((acc, block) => {
  const lines = block.split("\n");
  const header = clean(lines[0]);
  const body = lines.slice(1).join("\n");
  const comboId = body.match(/\[id::\s*([^\]]+)\]/i)?.[1]?.trim();
  if (!comboId || comboId.startsWith("template_")) return acc;

  const weaponLines = lines.filter(line => line.includes("[weapon_instance::"));
  if (weaponLines.length === 0) return acc;

  const weapons = [], profs = [], roles = [], implicits = [];
  weaponLines.forEach(line => {
    const instanceId = clean(field(line, "weapon_instance"));
    const frameId = clean(field(line, "weapon_frame"));
    const match = byVariant.get(instanceId) || byFrame.get(frameId);
    weapons.push(noWrap(match?.page?.file?.link || `⚠️ ${instanceId || frameId || "missing"}`));
    profs.push(noWrap(clean(field(line, "prof")) || "⚠️"));
    roles.push(noWrap(clean(field(line, "combat_role")) || "—"));
    implicits.push(noWrap(match?.page?.implicit_keyword || "⚠️"));
  });

  acc.push([
    dv.sectionLink(comboPath, header, false, displayName(header)),
    weapons.join("<br>"),
    profs.join("<br>"),
    roles.join("<br>"),
    implicits.join("<br>")
  ]);
  return acc;
}, []);

if (rows.length) {
  dv.table(["Комбо", "Оружие", "Prof", "Роль", "Inherited Implicit"], rows);
} else {
  dv.paragraph("⚠️ Нет данных в Registry_Combos.");
}
```

## Проверки

Пустая таблица ниже означает, что проверка не нашла проблем.

```dataviewjs
const field = (text, key) => text.match(new RegExp(`\\[${key}::\\s*([^\\]]+)\\]`, "i"))?.[1]?.trim();
const inputKeys = {
  blade: ["combo_chain", "alt_action"],
  blunt: ["combo_chain", "alt_action"],
  polearm: ["combo_chain", "alt_action"],
  arcanegun: ["fire_input", "reload_mechanic"],
  shield: ["guard_input", "guard_mechanic"],
  catalyst: ["cast_input", "draw_mechanic"]
};

const rows = [];
const frames = Array.from(dv.pages('"05_Combat_Survival/Weapons"'))
  .filter(page => page.type === "weapon_frame");

for (const page of frames) {
  const text = await dv.io.load(page.file.path);
  const issues = [];
  if (page.vector_scope !== "commitment") issues.push("scope");
  if (!page.activates_on) issues.push("activates_on");
  if (!page.mastery_unlock) issues.push("mastery");
  if (!page.implicit_keyword) issues.push("implicit_keyword");
  if (!page.implicit_rule) issues.push("implicit_rule");
  if (text.match(/\[(implicit|implicit_rule|input_pattern)::/i)) issues.push("old inline field");
  if (text.includes("sweet_spot_range:: UNKNOWN")) issues.push("UNKNOWN sweet spot");

  const variants = text.split(/^###\s+/m).slice(1).filter(section => field(section, "variant_id"));
  if (variants.length < 2) issues.push("variant_count < 2");
  const keys = inputKeys[page.weapon_family] || [];
  variants.forEach(section => {
    const id = field(section, "variant_id") || "UNKNOWN";
    const missing = keys.filter(key => !field(section, key));
    if (missing.length) issues.push(`${id}: ${missing.join(", ")}`);
  });

  if (issues.length) {
    rows.push([page.file.link, page.frame_id, page.weapon_family, issues.join("<br>")]);
  }
}

if (rows.length) {
  dv.table(["Фрейм", "frame_id", "family", "Проблемы"], rows);
} else {
  dv.paragraph("Проверка не нашла проблем.");
}
```
