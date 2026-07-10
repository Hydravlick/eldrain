---
type: registry
status: active
system: player_entities_registry
registry_type: combos
tags: [database, builds, proficiency, mvp]
related_files:
  - "[[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]]"
  - "[[04_Player_Entities/_Registries/Registry_Races|Registry Races]]"
  - "[[04_Player_Entities/_Registries/Registry_Specs|Registry Specs]]"
  - "[[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile Pipeline]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency Arsenal]]"
  - "[[07_Gear_Inventory/Thermos_System|Thermos System]]"
---
# Реестр: ячейки Race × Spec

> Реестр содержит девять проектных слотов MVP. Старые curated-комбинации выведены из канона: они не образовывали целостную матрицу и смешивали черновые способности с утверждёнными правилами.
>
> Главный фильтр проектирования: [[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]].

## Зафиксированная матрица

```dataviewjs
const races = dv.pages('"04_Player_Entities/Races"').where(page => page.type === "race");
const specs = dv.pages('"04_Player_Entities/Specs"').where(page => page.type === "spec");
const currentPath = dv.current().file.path;
const comboSource = await dv.io.load(currentPath);

const cleanId = value => value ? String(value).trim().toLowerCase() : null;
const inline = (body, key) => body.match(new RegExp(`\\[${key}::\\s*([^\\]]+)\\]`, "i"))?.[1]?.trim();
const asList = value => Array.from(value || []).map(cleanId).filter(Boolean);
const displayName = header => header.replace(/\s*\(.*?\)\s*/g, "").trim();

function pageRecord(page) {
    return {
        id: cleanId(page.id),
        name: page.display_name || page.file.name,
        path: page.file.path,
        link: page.file.link,
        sortOrder: Number(page.sort_order) || 999,
        scope: page.content_scope || "unknown",
        baseVector: cleanId(page.base_vector),
        weakTo: asList(page.weak_to)
    };
}

const raceRecords = Array.from(races).map(pageRecord).filter(item => item.id);
const specRecords = Array.from(specs).map(pageRecord).filter(item => item.id);
const comboRecords = comboSource.split(/^##\s+/m).slice(1).flatMap(block => {
    const lines = block.split("\n");
    const header = (lines[0] || "").trim();
    const body = lines.slice(1).join("\n");
    const id = cleanId(inline(body, "id"));
    if (!id || id.startsWith("template_")) return [];
    return [{
        id,
        header,
        name: displayName(header),
        raceId: cleanId(inline(body, "req_race")),
        specId: cleanId(inline(body, "req_spec")),
        status: cleanId(inline(body, "design_status")) || "missing"
    }];
});

const duplicateIds = values => values
    .filter((id, index) => values.indexOf(id) !== index)
    .filter((id, index, all) => all.indexOf(id) === index);
const duplicates = [
    ...duplicateIds(raceRecords.map(item => item.id)),
    ...duplicateIds(specRecords.map(item => item.id)),
    ...duplicateIds(comboRecords.map(item => item.id))
];

if (duplicates.length) {
    dv.paragraph(`⚠️ Дублирующиеся ID: ${duplicates.join(", ")}`);
}

const racesById = new Map(raceRecords.map(item => [item.id, item]));
const specsById = new Map(specRecords.map(item => [item.id, item]));
const combosByPair = new Map(comboRecords.map(item => [`${item.raceId}::${item.specId}`, item]));
const mvpRaces = raceRecords.filter(item => item.scope === "mvp").sort((a, b) => a.sortOrder - b.sortOrder);
const mvpSpecs = specRecords.filter(item => item.scope === "mvp").sort((a, b) => a.sortOrder - b.sortOrder);

if (!mvpRaces.length || !mvpSpecs.length) {
    dv.paragraph("⚠️ Не найдены MVP-расы или MVP-практики.");
} else {
    dv.table(
        ["Раса \\ Практика", ...mvpSpecs.map(spec => spec.link)],
        mvpRaces.map(race => [
            race.link,
            ...mvpSpecs.map(spec => {
                const combo = combosByPair.get(`${race.id}::${spec.id}`);
                if (!combo) return "⚠️ missing";
                return `${dv.sectionLink(currentPath, combo.header, false, combo.name)}<br><small>${combo.status}</small>`;
            })
        ])
    );
}

const inheritedRows = comboRecords.map(combo => {
    const race = racesById.get(combo.raceId);
    const spec = specsById.get(combo.specId);
    const sharedWeakness = race && spec
        ? race.weakTo.filter(value => spec.weakTo.includes(value))
        : [];
    const issues = [
        race ? null : `нет расы ${combo.raceId || "UNKNOWN"}`,
        spec ? null : `нет практики ${combo.specId || "UNKNOWN"}`
    ].filter(Boolean);

    return [
        dv.sectionLink(currentPath, combo.header, false, combo.name),
        race?.link || `⚠️ ${combo.raceId || "UNKNOWN"}`,
        spec?.link || `⚠️ ${combo.specId || "UNKNOWN"}`,
        [race?.baseVector, spec?.baseVector].filter(Boolean).join(" + ") || "⚠️ нет",
        sharedWeakness.join(", ") || "⚠️ нет общей слабости",
        issues.length ? `⚠️ ${issues.join("; ")}` : combo.status
    ];
});

if (inheritedRows.length) {
    dv.header(3, "Производный профиль");
    dv.table(["Комбинация", "Раса", "Практика", "Векторы", "Общая слабость", "Статус"], inheritedRows);
} else {
    dv.paragraph("⚠️ В Registry_Combos не найдено ни одной записи.");
}
```

Жаба, Ящерица, Страж и Догмат остаются expansion-направлениями. Для них не создаются фиктивные готовые комбо до отдельного прохода.

## Контракт записи

Завершённая ячейка хранит:

```markdown
[id:: template_combo]
[req_race:: template_race]
[req_spec:: template_spec]
[design_status:: approved]
[primary_window_function:: create]
[creates_window:: route_open, concealment]
[exploits_window:: blind, distraction]
[mitigates_window:: trap_pressure]
[creates_state:: none]
[exploits_state:: low_visibility]
[position_role:: route_control]
[resource_pressure:: tools, bolts]
[thrives_on:: confined_space, low_visibility]
[mitigates:: traps]
[preferred_targets:: stationary_lurker, support_core]
[bad_matchups:: detection, open_sightline, swarm]
[route_affinity:: confined_space, alternate_route]
[solo_gaps:: armor, sustained_pressure]
[condition_bonus:: ...]
[tradeoff:: ...]
[weapon_frame:: pulse_tool_1h] | [prof:: 1] | [combat_role:: stagger_opener]
[weapon_frame:: short_cut_1h] | [prof:: 2] | [combat_role:: window_finish]
[module_capacity:: plate 1, optic 1, seal 1, conduit 1, rig 2, weave 2]
```

После полей идут фантазия, повторяемый цикл, смешанные `P/Q/E`, 2–4 доктрины, результаты успеха/отхода/провала и заметки прототипа. Числа шаблона показывают формат; каждая ячейка получает собственные значения только после отдельного прохода.

`design_status:: pending` означает, что слот существует, но способности, арсенал и доктрины не являются каноном.

`primary_window_function` называет доминирующую работу повторяемого цикла. `creates_window`, `exploits_window` и `mitigates_window` используют тот же словарь, что оружие и способности; ячейка не должна одинаково хорошо выполнять все три функции без отдельной цены.

---

## Ёж × Авангард

[id:: hedgehog_assault]
[req_race:: hedgehog]
[req_spec:: assault]
[design_status:: pending]
[module_capacity:: UNKNOWN]
[weapon_frame:: breach_impact_2h] | [prof:: 2] | [combat_role:: breach]
[weapon_frame:: pulse_tool_1h] | [prof:: 1] | [combat_role:: stagger_opener]
[weapon_frame:: reach_line_2h] | [prof:: 1] | [combat_role:: distance_control]

Проектный слот. Не наследует автоматически старого «Джаггернаута», стационарную турель или «Сенсорную Броню».

---

## Ёж × Технократ

[id:: hedgehog_support]
[req_race:: hedgehog]
[req_spec:: support]
[design_status:: pending]
[module_capacity:: UNKNOWN]
[weapon_frame:: compact_impact_1h] | [prof:: 1] | [combat_role:: concussion_window]
[weapon_frame:: pulse_tool_1h] | [prof:: 1] | [combat_role:: interrupt]

Проектный слот. Сила должна рождаться из смешения телесной массы и инженерной методологии, а не из универсальной роли танка.

---

## Ёж × Странник

[id:: hedgehog_scout]
[req_race:: hedgehog]
[req_spec:: scout]
[design_status:: pending]
[module_capacity:: UNKNOWN]
[weapon_frame:: reach_line_2h] | [prof:: 2] | [combat_role:: route_hold]
[weapon_frame:: needle_thrower_2h] | [prof:: 1] | [combat_role:: quiet_pick]
[weapon_frame:: pulse_tool_1h] | [prof:: 1] | [combat_role:: emergency_stop]

Проектный слот. Мобильность Странника не обязана означать рывок; допустимы маршрутизация, контролируемый перенос массы и подготовленное изменение позиции.

---

## Крыса × Авангард

[id:: rat_assault]
[req_race:: rat]
[req_spec:: assault]
[design_status:: pending]
[module_capacity:: UNKNOWN]
[weapon_frame:: pulse_tool_1h] | [prof:: 2] | [combat_role:: third_grip_pressure]
[weapon_frame:: short_cut_1h] | [prof:: 2] | [combat_role:: clinch_finish]

Проектный слот. Третий хват и техническая биология должны менять способ ведения оружейного давления, а не давать бесплатную скорость действий.

---

## Крыса × Технократ

[id:: rat_support]
[req_race:: rat]
[req_spec:: support]
[design_status:: pending]
[ability_model:: mono_vector_fusion]
[module_capacity:: UNKNOWN]
[weapon_frame:: needle_thrower_2h] | [prof:: 2] | [combat_role:: quiet_tool]
[weapon_frame:: pulse_tool_1h] | [prof:: 1] | [combat_role:: interrupt]

Проектный слот. Совпадение `tech + tech` усиливает глубину технического исполнения, но не выдаёт бесплатный второй вектор.

---

## Крыса × Странник

[id:: rat_scout]
[req_race:: rat]
[req_spec:: scout]
[design_status:: pending]
[module_capacity:: UNKNOWN]
[weapon_frame:: short_cut_1h] | [prof:: 2] | [combat_role:: route_finish]
[weapon_frame:: needle_thrower_2h] | [prof:: 2] | [combat_role:: quiet_pick]
[weapon_frame:: pulse_tool_1h] | [prof:: 1] | [combat_role:: panic_stop]
[weapon_frame:: hook_reach_2h] | [prof:: 1] | [combat_role:: shield_angle]

Проектный слот. Должен работать через маршрут, инструмент и чтение пространства, не превращаясь в обязательный пик для закрытых локаций.

---

## Белка × Авангард

[id:: squirrel_assault]
[req_race:: squirrel]
[req_spec:: assault]
[design_status:: foundation_approved]
[module_capacity:: UNKNOWN]
[substat_consumer:: spark_gain]
[spark_rule:: meaningful_movement_impulse]
[weapon_frame:: pulse_tool_1h] | [prof:: 2] | [combat_role:: recoil_to_motion]
[weapon_frame:: short_cut_1h] | [prof:: 1] | [combat_role:: momentum_finish]
[weapon_frame:: reach_line_2h] | [prof:: 1] | [combat_role:: moving_reach]
[weapon_frame:: scatter_valve_2h] | [prof:: 1] | [combat_role:: entry_control]

### Утверждённая пассивная основа: «Инерционный заряд»

- заряд возникает от **значимого импульса движения**, а не от пройденных метров;
- источники: разгон, смена траектории, контролируемое приземление, смена высоты, выход из давления, перенос оружейной отдачи телом;
- повтор одного безопасного движения даёт убывающую отдачу;
- накопленный импульс готовит тяжёлое действие Авангарда, а не даёт постоянный DPS или бесплатное ускорение;
- `spark_gain` меняет скорость наполнения ограниченного заряда от значимых импульсов, но не увеличивает урон напрямую;
- точные пороги, расход заряда, оружейные связи и `Q/E` не утверждены.

Предложение «низкий заряд = высокая точность, нагрев = низкая точность, заряженный выстрел» остаётся примером возможного чтения, а не главным или каноническим решением.

---

## Белка × Технократ

[id:: squirrel_support]
[req_race:: squirrel]
[req_spec:: support]
[design_status:: pending]
[module_capacity:: UNKNOWN]
[weapon_frame:: scatter_valve_2h] | [prof:: 2] | [combat_role:: overload_cone]
[weapon_frame:: condenser_rig_2h] | [prof:: 1] | [combat_role:: held_line]

Проектный слот. Перегрузка — сильное направление фантазии, но требует цены, телеграфа и восстановления; не должна производить бесплатные батареи или бесконечное питание устройств.

---

## Белка × Странник

[id:: squirrel_scout]
[req_race:: squirrel]
[req_spec:: scout]
[design_status:: pending]
[module_capacity:: UNKNOWN]
[weapon_frame:: short_cut_1h] | [prof:: 2] | [combat_role:: vertical_ambush]
[weapon_frame:: needle_thrower_2h] | [prof:: 2] | [combat_role:: quiet_route]
[weapon_frame:: pulse_tool_1h] | [prof:: 1] | [combat_role:: emergency_stagger]
[weapon_frame:: point_tool_1h] | [prof:: 1] | [combat_role:: joint_line]

Проектный слот. Это наиболее мобильная методология матрицы, но мобильность должна жить в теле и маршруте; способности остаются медленными, ситуативными и уязвимыми.
