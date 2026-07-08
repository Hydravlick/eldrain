---
type: matrix
status: active
system: player_entities_matrix
tags: [dataview, matrix]
---

```dataviewjs
// === 1. ЗАГРУЗКА И КОНФИГУРАЦИЯ ===
const sources = {
    races: "04_Player_Entities/Races",
    specs: "04_Player_Entities/Specs",
    combos: "04_Player_Entities/_Registries/Registry_Combos.md"
};

const currentPath = dv.current()?.file?.path || sources.combos;

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

const modeMeta = {
    counter: {
        label: "Контрпики",
        color: "#f7768e",
        incomingColor: "#7aa2f7",
        description: "Строгий перевес между направленными контр-окнами",
        dashed: false
    },
    support: {
        label: "Сильная поддержка",
        color: "#48c78e",
        description: "Покрытие минимум двух общих слабостей цели",
        dashed: false
    },
    shared_weakness: {
        label: "Общая слабость",
        color: "#e0af68",
        description: "Две комбинации делят хотя бы одну общую слабость",
        dashed: true
    }
};

async function loadD3() {
    if (window.d3) return window.d3;

    const loader = dv.container.createDiv();
    loader.textContent = "Загрузка карты синергий...";
    Object.assign(loader.style, {
        padding: "8px 0",
        color: "var(--text-muted)",
        textAlign: "center"
    });

    return new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = "https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js";
        script.onload = () => {
            loader.remove();
            resolve(window.d3);
        };
        script.onerror = () => {
            loader.remove();
            reject(new Error("Не удалось загрузить D3. Проверьте доступ к cdnjs.cloudflare.com."));
        };
        document.head.appendChild(script);
    });
}

// === 2. ПАРСИНГ РЕЕСТРОВ ===
function cleanId(value) {
    return value ? String(value).toLowerCase().trim() : null;
}

function parseInlineValue(text, key) {
    const regex = new RegExp(`\\[${key}::\\s*([^\\]]+)\\]`, "i");
    const match = text.match(regex);
    return match ? match[1].trim() : null;
}

function parseInlineList(text, key) {
    const value = parseInlineValue(text, key);
    if (!value) return [];
    return value.split(",").map(cleanId).filter(Boolean);
}

function displayName(header) {
    return header
        .replace(/^\d+\.\s*/, "")
        .replace(/\s*\(.*?\)/g, "")
        .trim();
}

function entityRecord(page) {
    return {
        id: cleanId(page.id),
        name: page.display_name || page.file.name,
        path: page.file.path,
        baseVector: cleanId(page.base_vector),
        weakTo: Array.from(page.weak_to || []).map(cleanId).filter(Boolean)
    };
}

function loadEntityFolder(folder, type) {
    const records = Array.from(dv.pages(`"${folder}"`))
        .filter(page => page.type === type)
        .map(entityRecord)
        .filter(record => record.id);

    if (!records.length) {
        return { records: [], error: `Не найдены сущности type=${type}: ${folder}` };
    }

    const ids = records.map(record => record.id);
    const duplicates = ids.filter((id, index) => ids.indexOf(id) !== index);
    if (duplicates.length) {
        return { records: [], error: `Дублирующиеся ID в ${folder}: ${unique(duplicates).join(", ")}` };
    }

    return { records, error: null };
}

async function parseComboRegistry(path) {
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
            body
        };

        record.reqRace = cleanId(parseInlineValue(body, "req_race"));
        record.reqSpec = cleanId(parseInlineValue(body, "req_spec"));

        records.push(record);
    }

    return { records, error: null };
}

// === 3. ЧИСТАЯ ЛОГИКА СВЯЗЕЙ ===
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
    return values.length ? values.map(vectorLabel).join(", ") : "нет";
}

function dominates(attacker, defender) {
    return (paradoxRules[attacker] || []).includes(defender);
}

function supportReasons(source, target) {
    const reasons = [];
    for (const weakness of target.sharedWeakness || []) {
        const coverVectors = source.vectors.filter(vector => dominates(vector, weakness));
        if (coverVectors.length) {
            reasons.push(`${vectorList(coverVectors)} прикрывает слабость к ${vectorLabel(weakness)}`);
        }
    }
    return reasons;
}

function counterReasons(source, target) {
    const reasons = [];
    for (const sourceVector of source.vectors) {
        for (const targetVector of target.vectors) {
            if (dominates(sourceVector, targetVector)) {
                reasons.push(`${vectorLabel(sourceVector)} давит ${vectorLabel(targetVector)}`);
            }
        }
    }
    return unique(reasons);
}

function counterScore(source, target) {
    const reasons = counterReasons(source, target);
    return { score: reasons.length, reasons };
}

function supportScore(source, target) {
    const reasons = supportReasons(source, target);
    return { score: reasons.length, reasons };
}

function sharedWeaknessScore(left, right) {
    const shared = intersect(left.sharedWeakness || [], right.sharedWeakness || []);
    return {
        score: shared.length,
        reasons: shared.map(weakness => `общая слабость: ${vectorLabel(weakness)}`)
    };
}

function createModeLink(type, source, target, result, direction = "one") {
    return {
        id: `${type}__${source.id}__${target.id}`,
        source,
        target,
        sourceId: source.id,
        targetId: target.id,
        type,
        direction,
        strength: result.score,
        reasons: result.reasons
    };
}

function buildModeLinks(profiles, mode) {
    const links = [];

    if (mode === "support") {
        for (const source of profiles) {
            for (const target of profiles) {
                if (source === target) continue;
                const result = supportScore(source, target);
                if (result.score >= 2) links.push(createModeLink(mode, source, target, result));
            }
        }
        return links;
    }

    for (let i = 0; i < profiles.length; i++) {
        for (let j = i + 1; j < profiles.length; j++) {
            const left = profiles[i];
            const right = profiles[j];

            if (mode === "counter") {
                const leftResult = counterScore(left, right);
                const rightResult = counterScore(right, left);
                if (leftResult.score > rightResult.score) {
                    links.push(createModeLink(mode, left, right, {
                        score: leftResult.score - rightResult.score,
                        reasons: leftResult.reasons
                    }));
                } else if (rightResult.score > leftResult.score) {
                    links.push(createModeLink(mode, right, left, {
                        score: rightResult.score - leftResult.score,
                        reasons: rightResult.reasons
                    }));
                }
            }

            if (mode === "shared_weakness") {
                const result = sharedWeaknessScore(left, right);
                if (result.score > 0) links.push(createModeLink(mode, left, right, result, "both"));
            }
        }
    }

    return links;
}

function computeWeightedAngles(items, groupAccessor, crossGroupWeight = 1.75) {
    if (!items.length) return [];
    if (items.length === 1) return [0];

    const gapWeights = items.map((item, index) => {
        const next = items[(index + 1) % items.length];
        return groupAccessor(item) === groupAccessor(next) ? 1 : crossGroupWeight;
    });
    const unit = 360 / gapWeights.reduce((sum, weight) => sum + weight, 0);
    const angles = [];
    let angle = unit / 2;

    for (let index = 0; index < items.length; index++) {
        angles.push(angle);
        angle += gapWeights[index] * unit;
    }

    return angles;
}

function matrixCell(source, target, mode) {
    if (source.id === target.id) return null;

    let result;
    if (mode === "counter") result = counterScore(source, target);
    else if (mode === "support") result = supportScore(source, target);
    else result = sharedWeaknessScore(source, target);

    return {
        mode,
        sourceId: source.id,
        targetId: target.id,
        score: result.score,
        reasons: result.reasons,
        strong: mode === "support" ? result.score >= 2 : result.score > 0,
        direction: mode === "shared_weakness" ? "both" : "one"
    };
}

// === 4. ЗАГРУЗКА И ПРОФИЛИ ===
try {
    const d3 = await loadD3();

    const [raceResult, specResult, comboResult] = await Promise.all([
        loadEntityFolder(sources.races, "race"),
        loadEntityFolder(sources.specs, "spec"),
        parseComboRegistry(sources.combos)
    ]);

    const loadErrors = [raceResult.error, specResult.error, comboResult.error].filter(Boolean);
    if (loadErrors.length) {
        dv.header(2, "Ошибка загрузки");
        dv.list(loadErrors);
        return;
    }

    const racesById = new Map(raceResult.records.map(race => [race.id, race]));
    const specsById = new Map(specResult.records.map(spec => [spec.id, spec]));
    const profiles = comboResult.records.map(combo => {
        const race = racesById.get(combo.reqRace);
        const spec = specsById.get(combo.reqSpec);
        const vectors = unique([race?.baseVector, spec?.baseVector]);
        const sharedWeakness = race && spec ? intersect(race.weakTo || [], spec.weakTo || []) : [];

        return {
            ...combo,
            race,
            spec,
            groupName: race?.name || combo.reqRace || "unknown",
            vectors,
            sharedWeakness
        };
    }).filter(profile => profile.race && profile.spec && profile.vectors.length);

    profiles.sort((left, right) =>
        left.groupName.localeCompare(right.groupName) ||
        left.spec.name.localeCompare(right.spec.name)
    );

    const modeLinks = Object.fromEntries(
        Object.keys(modeMeta).map(mode => [mode, buildModeLinks(profiles, mode)])
    );

    // === 5. DOM И УПРАВЛЕНИЕ РЕЖИМАМИ ===
    dv.container.innerHTML = "";
    const main = dv.container.createDiv({ cls: "synergy-map" });
    Object.assign(main.style, {
        maxWidth: "760px",
        margin: "0 auto",
        fontFamily: "var(--font-interface)"
    });

    let activeView = "map";
    const viewControl = main.createDiv({ cls: "synergy-view-control" });
    Object.assign(viewControl.style, {
        display: "flex",
        justifyContent: "center",
        gap: "2px",
        marginBottom: "4px"
    });

    const viewMeta = {
        map: "Карта",
        matrix: "Матрица"
    };
    const viewButtons = d3.select(viewControl)
        .selectAll("button")
        .data(Object.keys(viewMeta))
        .join("button")
        .attr("type", "button")
        .style("padding", "4px 12px")
        .style("border", "none")
        .style("border-bottom", "2px solid transparent")
        .style("background", "transparent")
        .style("color", "var(--text-muted)")
        .style("font-size", "12px")
        .style("cursor", "pointer")
        .text(view => viewMeta[view])
        .on("click", (event, view) => setView(view));

    const modeControl = main.createDiv({ cls: "synergy-mode-control" });
    Object.assign(modeControl.style, {
        display: "flex",
        justifyContent: "center",
        flexWrap: "wrap",
        gap: "4px",
        marginBottom: "8px",
        padding: "4px",
        borderBottom: "1px solid var(--background-modifier-border)"
    });

    let activeMode = "counter";
    const modeButtons = d3.select(modeControl)
        .selectAll("button")
        .data(Object.keys(modeMeta))
        .join("button")
        .attr("type", "button")
        .style("padding", "5px 9px")
        .style("border", "1px solid transparent")
        .style("border-radius", "4px")
        .style("background", "transparent")
        .style("color", "var(--text-muted)")
        .style("font-size", "12px")
        .style("cursor", "pointer")
        .style("white-space", "nowrap")
        .text(mode => `${modeMeta[mode].label}: ${modeLinks[mode].length}`)
        .on("click", (event, mode) => setMode(mode));

    const svgHost = main.createDiv({ cls: "synergy-svg-host" });
    Object.assign(svgHost.style, {
        width: "100%",
        minHeight: "500px",
        overflow: "hidden"
    });

    const matrixHost = main.createDiv({ cls: "synergy-matrix-host" });
    Object.assign(matrixHost.style, {
        display: "none",
        width: "100%",
        minHeight: "500px",
        overflowX: "auto",
        paddingBottom: "4px"
    });

    const info = main.createDiv({ cls: "synergy-info-panel" });
    Object.assign(info.style, {
        minHeight: "68px",
        marginTop: "8px",
        padding: "10px 12px",
        border: "1px solid var(--background-modifier-border)",
        borderRadius: "6px",
        background: "var(--background-secondary)",
        color: "var(--text-normal)",
        lineHeight: "1.4"
    });

    if (!profiles.length) {
        info.textContent = "Недостаточно данных: проверьте req_race, req_spec, base_vector и weak_to.";
        return;
    }

    // === 6. РАДИАЛЬНАЯ КАРТА ===
    const width = 500;
    const height = 500;
    const nodeRadius = 130;
    const labelRadius = 138;
    const svg = d3.select(svgHost)
        .append("svg")
        .attr("viewBox", [-width / 2, -height / 2, width, height])
        .style("width", "500px")
        .style("max-width", "100%")
        .style("height", "500px")
        .style("display", "block")
        .style("margin", "0 auto")
        .style("font-family", "var(--font-interface)");

    svg.append("circle")
        .attr("r", nodeRadius)
        .style("fill", "none")
        .style("stroke", "var(--background-modifier-border)")
        .style("stroke-opacity", 0.45)
        .style("stroke-width", 1);

    const root = d3.hierarchy({ name: "root", children: profiles });
    d3.cluster().size([360, nodeRadius])(root);
    const leaves = root.leaves();
    const angles = computeWeightedAngles(leaves, node => node.data.groupName, 1.75);
    leaves.forEach((node, index) => {
        node.x = angles[index];
        node.y = nodeRadius;
    });

    const nodeMap = new Map(leaves.map(node => [node.data.id, node]));
    for (const links of Object.values(modeLinks)) {
        for (const link of links) {
            link.sourceNode = nodeMap.get(link.sourceId);
            link.targetNode = nodeMap.get(link.targetId);
            link.path = link.sourceNode?.path(link.targetNode) || [];
        }
    }

    const lineGen = d3.lineRadial()
        .curve(d3.curveBundle.beta(0.72))
        .radius(node => node.y)
        .angle(node => node.x / 180 * Math.PI);
    const linkLayer = svg.append("g").attr("class", "mode-links");
    let edgePaths = linkLayer.selectAll("path");

    const labelGroups = svg.append("g")
        .attr("class", "labels")
        .selectAll("g")
        .data(leaves)
        .join("g")
        .attr("transform", node => `rotate(${node.x - 90}) translate(${labelRadius},0)`)
        .style("cursor", "pointer")
        .on("mouseover", function(event, node) {
            highlightNode(node);
            d3.select(this).select("text").style("fill", "var(--text-accent)");
        })
        .on("mouseout", resetHighlight)
        .on("click", (event, node) => {
            dv.app.workspace.openLinkText(`${sources.combos}#${node.data.header}`, currentPath, false);
        });

    const labels = labelGroups.append("text")
        .attr("dy", "0.31em")
        .attr("text-anchor", node => node.x < 180 ? "start" : "end")
        .attr("transform", node => node.x >= 180 ? "rotate(180)" : null)
        .text(node => node.data.name)
        .style("fill", "var(--text-normal)")
        .style("font-size", "11px")
        .style("transition", "fill 0.16s ease, opacity 0.16s ease");

    const centerLabel = svg.append("g").attr("text-anchor", "middle");
    const centerTitle = centerLabel.append("text")
        .attr("dy", "-0.1em")
        .style("fill", "var(--text-normal)")
        .style("font-weight", "bold")
        .style("font-size", "12px");
    const centerCount = centerLabel.append("text")
        .attr("dy", "1.35em")
        .style("fill", "var(--text-muted)")
        .style("font-size", "10px");

    // === 7. МАТРИЦА ЭФФЕКТИВНОСТИ ===
    const matrixTable = d3.select(matrixHost)
        .append("table")
        .style("width", "100%")
        .style("min-width", "700px")
        .style("border-collapse", "separate")
        .style("border-spacing", "2px")
        .style("table-layout", "fixed")
        .style("font-size", "10px");

    const headerRow = matrixTable.append("thead").append("tr");
    headerRow.append("th")
        .style("width", "132px")
        .style("font-weight", "normal")
        .style("color", "var(--text-muted)")
        .text("Источник ↓ / цель →");

    const columnHeaders = headerRow.selectAll("th.matrix-column")
        .data(profiles)
        .join("th")
        .attr("class", "matrix-column")
        .style("height", "58px")
        .style("padding", "3px")
        .style("vertical-align", "bottom")
        .style("font-weight", "normal")
        .style("line-height", "1.12")
        .style("color", "var(--text-muted)")
        .style("overflow-wrap", "anywhere")
        .text(profile => profile.name);

    const matrixRows = matrixTable.append("tbody")
        .selectAll("tr")
        .data(profiles)
        .join("tr");

    const rowHeaders = matrixRows.append("th")
        .attr("scope", "row")
        .style("width", "132px")
        .style("padding", "4px 6px")
        .style("text-align", "right")
        .style("font-weight", "normal")
        .style("color", "var(--text-muted)")
        .style("white-space", "normal")
        .text(profile => profile.name);

    const matrixCells = matrixRows.selectAll("td")
        .data(source => profiles.map(target => ({ source, target })))
        .join("td")
        .attr("tabindex", item => item.source.id === item.target.id ? -1 : 0)
        .style("height", "38px")
        .style("padding", "0")
        .style("text-align", "center")
        .style("vertical-align", "middle")
        .style("border", "1px solid var(--background-modifier-border)")
        .style("border-radius", "3px")
        .style("cursor", item => item.source.id === item.target.id ? "default" : "pointer")
        .style("transition", "background 0.14s ease, color 0.14s ease, border-color 0.14s ease")
        .on("mouseenter focus", function(event, item) {
            if (item.source.id !== item.target.id) highlightMatrixCell(this, item);
        })
        .on("mouseleave blur", resetHighlight);

    function baseStroke(mode) {
        return mode === "counter" ? "var(--text-muted)" : modeMeta[mode].color;
    }

    function setView(view) {
        if (!viewMeta[view] || view === activeView) return;
        activeView = view;
        renderBaseState();
    }

    function setMode(mode) {
        if (!modeMeta[mode] || mode === activeMode) return;
        activeMode = mode;
        drawModeLinks();
    }

    function drawModeLinks() {
        edgePaths = linkLayer.selectAll("path")
            .data(modeLinks[activeMode], link => link.id)
            .join(
                enter => enter.append("path")
                    .style("fill", "none")
                    .style("stroke-linecap", "round")
                    .style("cursor", "pointer")
                    .style("transition", "stroke 0.16s ease, stroke-opacity 0.16s ease, stroke-width 0.16s ease"),
                update => update,
                exit => exit.remove()
            )
            .attr("d", link => lineGen(link.path))
            .on("mouseover", function(event, link) {
                highlightLink(this, link);
            })
            .on("mouseout", resetHighlight);

        renderBaseState();
    }

    function modeSummary() {
        const meta = modeMeta[activeMode];
        if (activeView === "matrix") {
            info.innerHTML = `
                <strong>${meta.label} · матрица ${profiles.length}×${profiles.length}</strong>
                <div style="font-size:0.88em; color:var(--text-muted); margin-top:3px;">Строка воздействует на столбец</div>
            `;
            return;
        }
        const directionKey = activeMode === "counter"
            ? `<span style="color:${meta.color};">исходящие</span> · <span style="color:${meta.incomingColor};">входящие</span>`
            : meta.description;
        info.innerHTML = `
            <strong>${meta.label} · ${modeLinks[activeMode].length} связей</strong>
            <div style="font-size:0.88em; color:var(--text-muted); margin-top:3px;">${directionKey}</div>
        `;
    }

    function renderBaseState() {
        const meta = modeMeta[activeMode];
        svgHost.style.display = activeView === "map" ? "block" : "none";
        matrixHost.style.display = activeView === "matrix" ? "block" : "none";

        viewButtons
            .style("color", view => view === activeView ? "var(--text-normal)" : "var(--text-muted)")
            .style("font-weight", view => view === activeView ? "600" : "normal")
            .style("border-bottom-color", view => view === activeView ? "var(--text-accent)" : "transparent");

        modeButtons
            .style("background", mode => mode === activeMode ? "var(--background-modifier-hover)" : "transparent")
            .style("border-color", mode => mode === activeMode ? modeMeta[mode].color : "transparent")
            .style("color", mode => mode === activeMode ? "var(--text-normal)" : "var(--text-muted)")
            .style("font-weight", mode => mode === activeMode ? "600" : "normal");

        edgePaths
            .style("stroke", baseStroke(activeMode))
            .style("stroke-opacity", activeMode === "counter" ? 0.25 : 0.52)
            .style("stroke-width", activeMode === "counter" ? 1.8 : 2.2)
            .style("stroke-dasharray", meta.dashed ? "5 5" : null);

        labels
            .style("fill", "var(--text-normal)")
            .style("opacity", 1)
            .style("font-weight", "normal");

        renderMatrixState();
        modeSummary();
    }

    function resetHighlight() {
        renderBaseState();
    }

    function relatedLinks(node) {
        return modeLinks[activeMode].filter(link =>
            link.sourceId === node.data.id || link.targetId === node.data.id
        );
    }

    function relationList(links, direction) {
        if (!links.length) return `<span style="color:var(--text-muted);">нет</span>`;
        return links.map(link => {
            const other = direction === "out" ? link.target.name : link.source.name;
            return `<div>${other} <span style="color:var(--text-muted);">${link.strength}</span></div>`;
        }).join("");
    }

    function scoreBackground(score, mode) {
        if (!score) return "transparent";
        const color = modeMeta[mode].color;
        const alpha = Math.min(0.72, 0.10 + score * 0.18);
        const red = parseInt(color.slice(1, 3), 16);
        const green = parseInt(color.slice(3, 5), 16);
        const blue = parseInt(color.slice(5, 7), 16);
        return `rgba(${red}, ${green}, ${blue}, ${alpha})`;
    }

    function renderMatrixState() {
        matrixCells.each(function(item) {
            const cell = matrixCell(item.source, item.target, activeMode);
            d3.select(this)
                .text(cell ? cell.score : "—")
                .style("background", cell ? scoreBackground(cell.score, activeMode) : "var(--background-secondary)")
                .style("color", cell && cell.score ? "var(--text-normal)" : "var(--text-faint)")
                .style("font-weight", cell && cell.strong ? "700" : "normal")
                .style("border-color", cell && cell.strong ? modeMeta[activeMode].color : "var(--background-modifier-border)");
        });

        rowHeaders
            .style("color", "var(--text-muted)")
            .style("font-weight", "normal");
        columnHeaders
            .style("color", "var(--text-muted)")
            .style("font-weight", "normal");
    }

    function highlightMatrixCell(element, item) {
        const cell = matrixCell(item.source, item.target, activeMode);
        if (!cell) return;

        d3.select(element)
            .style("background", scoreBackground(Math.max(1, cell.score + 1), activeMode))
            .style("border-color", modeMeta[activeMode].color);

        rowHeaders
            .style("color", profile => profile.id === item.source.id ? "var(--text-accent)" : "var(--text-muted)")
            .style("font-weight", profile => profile.id === item.source.id ? "700" : "normal");
        columnHeaders
            .style("color", profile => profile.id === item.target.id ? "var(--text-accent)" : "var(--text-muted)")
            .style("font-weight", profile => profile.id === item.target.id ? "700" : "normal");

        const reasons = cell.reasons.length ? cell.reasons.join("<br>") : "Нет воздействия этого типа";
        const arrow = activeMode === "shared_weakness" ? "↔" : "→";
        const strengthNote = activeMode === "support" && cell.score === 1
            ? " · слабая, на карту не выведена"
            : "";
        info.innerHTML = `
            <strong>${item.source.name} ${arrow} ${item.target.name}</strong>
            <span style="color:${modeMeta[activeMode].color}; margin-left:6px;">${cell.score}${strengthNote}</span>
            <div style="font-size:0.88em; color:var(--text-muted); margin-top:4px;">${reasons}</div>
        `;
    }

    function highlightNode(node) {
        const nodeId = node.data.id;
        const connected = relatedLinks(node);
        const relatedIds = new Set([nodeId]);
        connected.forEach(link => {
            relatedIds.add(link.sourceId);
            relatedIds.add(link.targetId);
        });

        edgePaths
            .style("stroke", link => {
                if (activeMode === "counter" && link.sourceId === nodeId) return modeMeta.counter.color;
                if (activeMode === "counter" && link.targetId === nodeId) return modeMeta.counter.incomingColor;
                return modeMeta[activeMode].color;
            })
            .style("stroke-opacity", link =>
                link.sourceId === nodeId || link.targetId === nodeId ? 1 : 0.035
            )
            .style("stroke-width", link =>
                link.sourceId === nodeId || link.targetId === nodeId ? 3.2 : 1.2
            );

        labels
            .style("opacity", leaf => relatedIds.has(leaf.data.id) ? 1 : 0.2)
            .style("font-weight", leaf => relatedIds.has(leaf.data.id) ? "600" : "normal")
            .style("fill", leaf => leaf.data.id === nodeId ? "var(--text-accent)" : "var(--text-normal)");

        const outgoing = connected.filter(link => link.sourceId === nodeId);
        const incoming = connected.filter(link => link.targetId === nodeId && link.direction !== "both");
        const shared = connected.filter(link => link.direction === "both");
        const profile = node.data;

        if (activeMode === "counter") {
            info.innerHTML = `
                <strong style="color:var(--text-accent);">${profile.name}</strong>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:5px; font-size:0.9em;">
                    <div><strong style="color:${modeMeta.counter.color};">Исходящие · ${outgoing.length}</strong>${relationList(outgoing, "out")}</div>
                    <div><strong style="color:${modeMeta.counter.incomingColor};">Входящие · ${incoming.length}</strong>${relationList(incoming, "in")}</div>
                </div>
            `;
        } else if (activeMode === "support") {
            info.innerHTML = `
                <strong style="color:var(--text-accent);">${profile.name}</strong>
                <div style="margin-top:4px; font-size:0.9em;">Поддерживает: ${outgoing.length} · Получает поддержку: ${incoming.length}</div>
            `;
        } else {
            info.innerHTML = `
                <strong style="color:var(--text-accent);">${profile.name}</strong>
                <div style="margin-top:4px; font-size:0.9em;">Общая слабость с ${shared.length} комбинациями</div>
                <div style="color:var(--text-muted); font-size:0.88em; margin-top:2px;">${vectorList(profile.sharedWeakness)}</div>
            `;
        }
    }

    function highlightLink(element, link) {
        d3.select(element)
            .style("stroke", modeMeta[activeMode].color)
            .style("stroke-opacity", 1)
            .style("stroke-width", 4)
            .raise();

        labels
            .style("opacity", leaf =>
                leaf.data.id === link.sourceId || leaf.data.id === link.targetId ? 1 : 0.2
            )
            .style("font-weight", leaf =>
                leaf.data.id === link.sourceId || leaf.data.id === link.targetId ? "600" : "normal"
            );

        const arrow = link.direction === "both" ? "↔" : "→";
        info.innerHTML = `
            <strong>${link.source.name} ${arrow} ${link.target.name}</strong>
            <span style="color:var(--text-muted); margin-left:6px;">сила ${link.strength}</span>
            <div style="font-size:0.88em; color:var(--text-muted); margin-top:4px;">${link.reasons.join("<br>")}</div>
        `;
    }

    drawModeLinks();
} catch (error) {
    dv.container.innerHTML = "";
    dv.header(2, "Ошибка карты синергий");
    dv.paragraph(error.message);
}
```
