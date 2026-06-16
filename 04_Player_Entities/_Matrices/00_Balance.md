---
type: matrix
status: active
system: player_entities_matrix
tags: [dataview, matrix]
---

```dataviewjs
(async () => {
    const files = {
        races: "04_Player_Entities/_Registries/Registry_Races.md",
        specs: "04_Player_Entities/_Registries/Registry_Specs.md",
        combos: "04_Player_Entities/_Registries/Registry_Combos.md"
    };

    const paradoxRules = {
        hazard: ["shadow", "kinetics", "ballistics"],
        shadow: ["kinetics", "tech", "aether"],
        kinetics: ["tech", "ballistics", "detection"],
        tech: ["ballistics", "aether", "hazard"],
        ballistics: ["aether", "detection", "shadow"],
        aether: ["detection", "hazard", "kinetics"],
        detection: ["hazard", "shadow", "tech"]
    };

    const vectorNames = {
        hazard: "Биохимия",
        shadow: "Тень",
        kinetics: "Кинетика",
        tech: "Техника",
        ballistics: "Дальнее давление",
        aether: "Эфир",
        detection: "Сенсорика"
    };

    function cleanId(value) {
        return value ? value.toLowerCase().trim() : null;
    }

    function parseInlineValue(text, key) {
        const regex = new RegExp(`\\[${key}::\\s*([^\\]]+)\\]`, "i");
        const match = text.match(regex);
        return match ? match[1].trim() : null;
    }

    function parseInlineList(text, key) {
        const value = parseInlineValue(text, key);
        if (!value) return [];
        return value.split(",").map(v => cleanId(v)).filter(Boolean);
    }

    function parseArsenalEntries(text) {
        const regex = /\[arsenal_type::\s*([^\]]+)\][^\n]*?\[prof::\s*([^\]]+)\]/g;
        return [...text.matchAll(regex)].map(m => ({
            type: cleanId(m[1]),
            prof: parseInt(m[2].trim()) || 0
        })).filter(entry => entry.type);
    }

    function displayName(header) {
        return header
            .replace(/^\d+\.\s*/, "")
            .replace(/\s*\(.*?\)/g, "")
            .trim();
    }

    async function parseRegistry(path, kind) {
        const page = dv.page(path);
        if (!page) return { records: [], error: `Файл не найден: ${path}` };

        const content = await dv.io.load(page.file.path);
        const blocks = content.split(/^##\s+/m).slice(1);
        const records = [];

        for (const block of blocks) {
            const lines = block.split("\n");
            const header = (lines[0] || "").trim();
            const body = lines.slice(1).join("\n");

            if (!header || /нулевой пациент|template|шаблон/i.test(header)) continue;

            const id = cleanId(parseInlineValue(body, "id"));
            if (!id || id.startsWith("template_")) continue;

            const record = {
                id,
                name: displayName(header),
                header,
                link: `[[${path}#${header}|${displayName(header)}]]`,
                body
            };

            if (kind === "race" || kind === "spec") {
                record.baseVector = cleanId(parseInlineValue(body, "base_vector"));
                record.weakTo = parseInlineList(body, "weak_to");
            }

            if (kind === "combo") {
                record.reqRace = cleanId(parseInlineValue(body, "req_race"));
                record.reqSpec = cleanId(parseInlineValue(body, "req_spec"));
                record.arsenal = parseArsenalEntries(body);
            }

            records.push(record);
        }

        return { records, error: null };
    }

    function unique(values) {
        return [...new Set(values.filter(Boolean))];
    }

    function intersect(left, right) {
        const rightSet = new Set(right);
        return left.filter(value => rightSet.has(value));
    }

    function vectorLabel(vector) {
        return vectorNames[vector] || vector || "неизвестно";
    }

    function vectorList(values) {
        return values.length ? values.map(vectorLabel).join(", ") : "нет данных";
    }

    function expectedWeakTo(vector) {
        return Object.entries(paradoxRules)
            .filter(([, targets]) => targets.includes(vector))
            .map(([source]) => source);
    }

    function sameSet(left, right) {
        if (left.length !== right.length) return false;
        const rightSet = new Set(right);
        return left.every(value => rightSet.has(value));
    }

    function dominates(attacker, defender) {
        return (paradoxRules[attacker] || []).includes(defender);
    }

    function matchup(left, right) {
        const reasons = [];
        let score = 0;

        for (const leftVector of left.vectors) {
            for (const rightVector of right.vectors) {
                if (dominates(leftVector, rightVector)) {
                    score += 1;
                    reasons.push(`${vectorLabel(leftVector)} давит ${vectorLabel(rightVector)}`);
                }
            }
        }

        return { score, reasons };
    }

    function coversAll(attacker, defender) {
        return defender.vectors.length > 0 && defender.vectors.every(defenderVector =>
            attacker.vectors.some(attackerVector => dominates(attackerVector, defenderVector))
        );
    }

    const [raceResult, specResult, comboResult] = await Promise.all([
        parseRegistry(files.races, "race"),
        parseRegistry(files.specs, "spec"),
        parseRegistry(files.combos, "combo")
    ]);

    const loadErrors = [raceResult.error, specResult.error, comboResult.error].filter(Boolean);
    if (loadErrors.length) {
        dv.header(2, "Ошибка загрузки");
        dv.list(loadErrors);
        return;
    }

    const racesById = new Map(raceResult.records.map(race => [race.id, race]));
    const specsById = new Map(specResult.records.map(spec => [spec.id, spec]));

    const archetypes = comboResult.records.map(combo => {
        const race = racesById.get(combo.reqRace);
        const spec = specsById.get(combo.reqSpec);
        const vectors = unique([race?.baseVector, spec?.baseVector]);
        const sharedWeakness = race && spec ? intersect(race.weakTo || [], spec.weakTo || []) : [];

        return {
            ...combo,
            race,
            spec,
            vectors,
            sharedWeakness,
            model: vectors.length === 1 ? "mono_vector_fusion" : "race_spec_fusion",
            dominates: [],
            vulnerableTo: [],
            issues: [
                race ? null : `Не найдена раса: ${combo.reqRace}`,
                spec ? null : `Не найден класс: ${combo.reqSpec}`,
                vectors.length ? null : "Нет активных векторов",
                sharedWeakness.length ? null : "Нет общей слабости"
            ].filter(Boolean)
        };
    });

    for (let i = 0; i < archetypes.length; i++) {
        for (let j = 0; j < archetypes.length; j++) {
            if (i === j) continue;

            const left = archetypes[i];
            const right = archetypes[j];
            const leftAttack = matchup(left, right);
            const rightAttack = matchup(right, left);

            if (leftAttack.score > rightAttack.score) {
                left.dominates.push(`**${right.name}**<br><span style="font-size:0.85em; color:var(--text-muted);">${leftAttack.reasons.join("; ")}</span>`);
            }

            if (coversAll(right, left)) {
                left.vulnerableTo.push(`**${right.name}**<br><span style="font-size:0.85em; color:var(--text-muted);">закрывает все активные векторы</span>`);
            }
        }
    }

    const registryIssues = [];
    for (const item of [...raceResult.records, ...specResult.records]) {
        const expected = expectedWeakTo(item.baseVector);
        if (!item.baseVector || !sameSet(item.weakTo || [], expected)) {
            registryIssues.push([
                item.link,
                item.baseVector ? vectorLabel(item.baseVector) : "нет вектора",
                vectorList(item.weakTo || []),
                vectorList(expected)
            ]);
        }
    }

    dv.header(2, "Эмерджентная Матрица: Тактические Векторы");
    dv.paragraph("Профиль больше не хранится в Registry_Combos. Он вычисляется из Race + Spec: раса дает первый вектор, класс дает второй, общая слабость берется из пересечения weak_to. Для MVP Registry_Combos содержит curated-набор из 9 утвержденных комбинаций; отсутствующие пары 5x5 считаются неутвержденными, а не ошибкой данных.");

    dv.table(
        ["Оболочка", "Источник профиля", "Активные векторы", "Общая слабость", "Окна доминации", "Полная уязвимость"],
        archetypes.map(arch => [
            `**${arch.link}**<br><span style="font-size:0.85em;">${arch.id}</span>`,
            [
                arch.race ? `Race: ${arch.race.link}` : `Race: ${arch.reqRace}`,
                arch.spec ? `Spec: ${arch.spec.link}` : `Spec: ${arch.reqSpec}`,
                `Model: ${arch.model}`,
                arch.issues.length ? `<span style="color:var(--text-warning);">${arch.issues.join("<br>")}</span>` : "Данные полные"
            ].join("<br>"),
            arch.vectors.map(vectorLabel).join("<br>") || "нет данных",
            arch.sharedWeakness.map(vectorLabel).join("<br>") || "нет полного общего окна",
            arch.dominates.join("<br><br>") || "нет явного перевеса",
            arch.vulnerableTo.join("<br><br>") || "нет полного окна"
        ])
    );

    dv.header(3, "Проверка weak_to");
    if (registryIssues.length) {
        dv.table(["Объект", "Вектор", "Сейчас weak_to", "Ожидается из матрицы"], registryIssues);
    } else {
        dv.paragraph("Race/Spec weak_to согласованы с канонической матрицей Двойного Парадокса.");
    }
})();
```
