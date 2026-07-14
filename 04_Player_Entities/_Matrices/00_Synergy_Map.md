---
type: matrix
status: active
system: player_entities_matrix
tags: [dataview, matrix, hero_kit, decision_windows]
related_files:
  - "[[04_Player_Entities/_Registries/Registry_Combos|Registry Combos]]"
  - "[[04_Player_Entities/Ability_Synergy|Ability Synergy]]"
  - "[[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]]"
---
# Карта решений hero-kit

> Карта сравнивает **authored-поведение девяти hero-kit**, а не вычисляет силу пересечения из ярлыков расы и практики. Пока ячейка не называет собственные P/Q/E, сигнатуру, арсенал, модули, долги и наблюдаемые окна, её matchup не существует как каноническое правило.

## Что является связью

Связь между двумя наборами появляется только из фактической сцены:

```text
видимый источник или занятая позиция
  -> действие одного hero-kit создаёт named window
  -> другой hero-kit может использовать или закрыть это окно сейчас
  -> оба платят собственные Recovery, ресурс и Exposure
```

Совпадение тематических слов вроде `tech`, `shadow` или `kinetics` не создаёт контру. Карта также не выводит «общую слабость» из родителей: это вернуло бы скрытую универсальную шкалу и позволило бы балансировать ещё не спроектированный kit.

## Контракт полей

Каждая утверждённая запись в [[04_Player_Entities/_Registries/Registry_Combos|Registry_Combos]] публикует:

```markdown
[decision_signature:: read_scene -> commit_named_tool -> redirect_pressure -> leave_residue]
[primary_window_function:: create]
[creates_window:: route_open, concealment]
[exploits_window:: blind, distraction]
[mitigates_window:: trap_pressure]
[exposure_channels:: hands_busy, open_line, heat]
[counterplay_now:: break_line, contest_tool, punish_recovery]
```

- `creates_window` — что kit физически оставляет в мире для следующего решения;
- `exploits_window` — какое уже видимое окно он умеет реализовать;
- `mitigates_window` — какое давление он может пережить или перенаправить;
- `counterplay_now` — доступный противнику ответ из текущей позиции, предмета или маршрута;
- `exposure_channels` — чем kit платит, пока выполняет свою сигнатуру.

Одно совпадение слов является поводом для playtest-сцены, а не доказательством победы. Карта не присваивает весов, процентов или Power Score.

## Представление полноты

```dataviewjs
const path = "04_Player_Entities/_Registries/Registry_Combos.md";
const page = dv.page(path);

if (!page) {
    dv.paragraph(`⚠️ Не найден источник: ${path}`);
} else {
    const source = await dv.io.load(page.file.path);
    const inline = (body, key) => body.match(new RegExp(`\\[${key}::\\s*([^\\]]+)\\]`, "i"))?.[1]?.trim();
    const clean = value => value ? String(value).trim().toLowerCase() : null;
    const displayName = header => header.replace(/\\s*\\(.*?\\)\\s*/g, "").trim();

    const records = source.split(/^##\\s+/m).slice(1).flatMap(block => {
        const lines = block.split("\n");
        const header = (lines[0] || "").trim();
        const body = lines.slice(1).join("\n");
        const id = clean(inline(body, "id"));
        if (!id || id.startsWith("template_")) return [];

        return [{
            id,
            header,
            name: displayName(header),
            status: clean(inline(body, "design_status")) || "missing",
            signature: inline(body, "decision_signature"),
            primary: inline(body, "primary_window_function"),
            creates: inline(body, "creates_window"),
            exploits: inline(body, "exploits_window"),
            mitigates: inline(body, "mitigates_window"),
            exposure: inline(body, "exposure_channels"),
            counterplay: inline(body, "counterplay_now")
        }];
    });

    if (!records.length) {
        dv.paragraph("⚠️ В Registry_Combos нет hero-kit записей.");
    } else {
        dv.table(
            ["Hero-kit", "Сигнатура", "Создаёт", "Использует", "Закрывает", "Exposure / ответ", "Готовность"],
            records.map(record => {
                const missing = [
                    !record.signature || clean(record.signature) === "unknown" ? "signature" : null,
                    !record.primary ? "primary" : null,
                    !record.creates && !record.exploits && !record.mitigates ? "windows" : null,
                    !record.exposure ? "exposure" : null,
                    !record.counterplay ? "counterplay" : null
                ].filter(Boolean);

                return [
                    dv.sectionLink(page.file.path, record.header, false, record.name),
                    record.signature || "⚠️ UNKNOWN",
                    record.creates || "—",
                    record.exploits || "—",
                    record.mitigates || "—",
                    `${record.exposure || "⚠️ exposure"}<br><small>${record.counterplay || "⚠️ counterplay"}</small>`,
                    missing.length ? `⚠️ ${missing.join(", ")}` : record.status
                ];
            })
        );
    }
}
```

## Как карта используется

1. Дизайнер сначала проектирует отдельный hero-kit и две конкретные сцены его сигнатуры.
2. Затем связывает named windows с действиями другого готового hero-kit.
3. Playtest проверяет, заметил ли игрок источник и имел ли реальный ответ **до** разрешения эффекта.
4. Только повторяемое наблюдаемое взаимодействие становится частью контрметы.

Незаполненная ячейка остаётся честным `pending`. Карта не заполняет пустоту математикой родителей.
