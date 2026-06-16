```dataviewjs
(async () => {
    const files = {
        races: "04_Player_Entities/_Registries/Registry_Races.md",
        specs: "04_Player_Entities/_Registries/Registry_Specs.md",
        combos: "04_Player_Entities/_Registries/Registry_Combos.md"
    };

    const currentPath = dv.current()?.file?.path || files.combos;

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

    const vectorColors = {
        hazard: "#8fbf62",
        shadow: "#7c6f9f",
        kinetics: "#c7a66b",
        tech: "#69b3a2",
        ballistics: "#d8895f",
        aether: "#8aa4ff",
        detection: "#d6cf73"
    };

    const relationMeta = {
        support: {
            type: "support",
            label: "Поддержка",
            color: "#48c78e",
            description: "A прикрывает общую слабость B",
            dashed: false,
            directed: true,
            order: 1
        },
        counter: {
            type: "counter",
            label: "Контр-окно",
            color: "#f7768e",
            description: "A получает тактическое окно давления против B",
            dashed: false,
            directed: true,
            order: 2
        },
        shared_vector: {
            type: "shared_vector",
            label: "Общий вектор",
            color: "#7aa2f7",
            description: "две сборки играют через один тактический вектор",
            dashed: false,
            directed: false,
            order: 3
        },
        shared_arsenal: {
            type: "shared_arsenal",
            label: "Общий арсенал",
            color: "#4fd6c8",
            description: "две сборки используют пересекающиеся типы оружия или брони",
            dashed: false,
            directed: false,
            order: 4
        },
        shared_weakness: {
            type: "shared_weakness",
            label: "Общая слабость",
            color: "#e0af68",
            description: "пара делит одно окно уязвимости",
            dashed: true,
            directed: false,
            order: 5
        }
    };

    async function loadD3() {
        if (window.d3) return window.d3;

        const loader = document.createElement("div");
        loader.textContent = "Загрузка направленной карты...";
        Object.assign(loader.style, {
            padding: "8px 0",
            color: "var(--text-muted)",
            textAlign: "center"
        });
        dv.container.appendChild(loader);

        return new Promise((resolve, reject) => {
            const script = document.createElement("script");
            script.src = "https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js";
            script.onload = () => {
                loader.remove();
                resolve(window.d3);
            };
            script.onerror = () => {
                loader.remove();
                reject(new Error("Не удалось загрузить D3. Проверьте доступ к cdnjs.cloudflare.com или наличие D3 в Obsidian."));
            };
            document.head.appendChild(script);
        });
    }

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
        const regex = /\[type::\s*([^\]]+)\][^\n]*?\[prof::\s*([^\]]+)\]/g;
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
                record.arsenalTypes = [...new Set(record.arsenal.map(item => item.type))];
            }

            records.push(record);
        }

        return { records, error: null };
    }

    function createElement(tag, parent, className) {
        const element = document.createElement(tag);
        if (className) element.className = className;
        parent.appendChild(element);
        return element;
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
        return values.length ? values.map(vectorLabel).join(", ") : "нет";
    }

    function dominates(attacker, defender) {
        return (paradoxRules[attacker] || []).includes(defender);
    }

    function profileLink(profile) {
        return `[[${files.combos}#${profile.header}|${profile.name}]]`;
    }

    function supportReasons(source, target) {
        const reasons = [];
        for (const weakness of target.sharedWeakness) {
            const coverVectors = source.vectors.filter(vector => dominates(vector, weakness));
            if (coverVectors.length) {
                reasons.push(`${source.name}: ${vectorList(coverVectors)} прикрывает слабость ${target.name} к ${vectorLabel(weakness)}`);
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

    function addEdge(edges, type, source, target, reasons, direction = "one") {
        if (!reasons.length) return;
        edges.push({
            id: `${source.id}__${target.id}__${type}__${edges.length}`,
            sourceId: source.id,
            targetId: target.id,
            source,
            target,
            type,
            direction,
            reasons,
            strength: Math.min(8, Math.max(1, reasons.length)),
            pairKey: [source.id, target.id].sort().join("__"),
            parallelIndex: 0,
            parallelOffset: 0
        });
    }

    function buildEdgesForPair(left, right) {
        const edges = [];

        const sharedVectors = intersect(left.vectors, right.vectors);
        addEdge(
            edges,
            "shared_vector",
            left,
            right,
            sharedVectors.map(vector => `оба используют ${vectorLabel(vector)}`),
            "both"
        );

        const sharedArsenal = intersect(left.arsenalTypes || [], right.arsenalTypes || []);
        addEdge(
            edges,
            "shared_arsenal",
            left,
            right,
            sharedArsenal.map(type => `общий арсенал: ${type}`),
            "both"
        );

        const sharedWeaknesses = intersect(left.sharedWeakness, right.sharedWeakness);
        addEdge(
            edges,
            "shared_weakness",
            left,
            right,
            sharedWeaknesses.map(weakness => `общая слабость: ${vectorLabel(weakness)}`),
            "both"
        );

        addEdge(edges, "support", left, right, supportReasons(left, right), "one");
        addEdge(edges, "support", right, left, supportReasons(right, left), "one");

        const leftCounter = counterReasons(left, right);
        const rightCounter = counterReasons(right, left);
        if (leftCounter.length > rightCounter.length) addEdge(edges, "counter", left, right, leftCounter, "one");
        if (rightCounter.length > leftCounter.length) addEdge(edges, "counter", right, left, rightCounter, "one");
        if (leftCounter.length && leftCounter.length === rightCounter.length) {
            addEdge(edges, "counter", left, right, leftCounter, "one");
            addEdge(edges, "counter", right, left, rightCounter, "one");
        }

        return edges;
    }

    function assignParallelOffsets(edges) {
        const groups = new Map();
        for (const edge of edges) {
            if (!groups.has(edge.pairKey)) groups.set(edge.pairKey, []);
            groups.get(edge.pairKey).push(edge);
        }

        for (const groupEdges of groups.values()) {
            groupEdges.sort((a, b) =>
                relationMeta[a.type].order - relationMeta[b.type].order ||
                a.source.name.localeCompare(b.source.name) ||
                a.target.name.localeCompare(b.target.name)
            );

            const center = (groupEdges.length - 1) / 2;
            groupEdges.forEach((edge, index) => {
                edge.parallelIndex = index - center;
                edge.parallelOffset = edge.parallelIndex * 18;
            });
        }
    }

    function polarPoint(angleDeg, radius) {
        const angle = (angleDeg - 90) * Math.PI / 180;
        return [Math.cos(angle) * radius, Math.sin(angle) * radius];
    }

    function quadraticArcPath(edge) {
        const sourcePoint = polarPoint(edge.sourceNode.x, edge.sourceNode.y);
        const targetPoint = polarPoint(edge.targetNode.x, edge.targetNode.y);
        const [sx, sy] = sourcePoint;
        const [tx, ty] = targetPoint;
        const midX = (sx + tx) / 2;
        const midY = (sy + ty) / 2;
        const dx = tx - sx;
        const dy = ty - sy;
        const length = Math.max(1, Math.hypot(dx, dy));
        const normalX = -dy / length;
        const normalY = dx / length;
        const controlX = midX * 0.18 + normalX * edge.parallelOffset;
        const controlY = midY * 0.18 + normalY * edge.parallelOffset;

        return `M${sx},${sy} Q${controlX},${controlY} ${tx},${ty}`;
    }

    try {
        const d3 = await loadD3();

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

        const profiles = comboResult.records.map(combo => {
            const race = racesById.get(combo.reqRace);
            const spec = specsById.get(combo.reqSpec);
            const vectors = unique([race?.baseVector, spec?.baseVector]);
            const sharedWeakness = race && spec ? intersect(race.weakTo || [], spec.weakTo || []) : [];

            return {
                ...combo,
                race,
                spec,
                group: race?.id || "unknown",
                groupName: race?.name || combo.reqRace || "unknown",
                vectors,
                sharedWeakness,
                model: vectors.length === 1 ? "mono_vector_fusion" : "race_spec_fusion"
            };
        }).filter(profile => profile.race && profile.spec && profile.vectors.length);

        const edges = [];
        for (let i = 0; i < profiles.length; i++) {
            for (let j = i + 1; j < profiles.length; j++) {
                edges.push(...buildEdgesForPair(profiles[i], profiles[j]));
            }
        }
        assignParallelOffsets(edges);

        edges.sort((a, b) =>
            relationMeta[a.type].order - relationMeta[b.type].order ||
            b.strength - a.strength ||
            a.source.name.localeCompare(b.source.name)
        );

        dv.container.innerHTML = "";

        const main = createElement("div", dv.container, "synergy-directed-map");
        Object.assign(main.style, {
            maxWidth: "980px",
            margin: "0 auto",
            fontFamily: "var(--font-interface)"
        });

        const title = createElement("div", main);
        title.innerHTML = `
            <div style="font-size:1.3em; font-weight:750; color:var(--text-normal);">Карта Синергий: направленные линии</div>
            <div style="font-size:0.92em; color:var(--text-muted); margin-top:5px; line-height:1.45;">
                Каждая линия показывает один смысл связи. Стрелка отвечает на вопрос "кто влияет на кого"; двусторонние связи получают стрелки с двух сторон. MVP читает только 9 утвержденных комбо из Registry_Combos.
            </div>
        `;

        const legend = createElement("div", main);
        Object.assign(legend.style, {
            display: "flex",
            flexWrap: "wrap",
            alignItems: "center",
            gap: "8px",
            margin: "14px 0 10px"
        });

        const counts = Object.keys(relationMeta).reduce((acc, type) => {
            acc[type] = edges.filter(edge => edge.type === type).length;
            return acc;
        }, {});

        const allChip = createElement("button", legend);
        allChip.textContent = `Все линии: ${edges.length}`;
        Object.assign(allChip.style, {
            border: "1px solid var(--background-modifier-border)",
            background: "var(--background-secondary)",
            color: "var(--text-normal)",
            borderRadius: "6px",
            padding: "5px 9px",
            cursor: "pointer"
        });

        const chips = [];
        for (const type of Object.keys(relationMeta)) {
            const meta = relationMeta[type];
            const chip = createElement("button", legend);
            chip.innerHTML = `<span style="display:inline-block; width:11px; height:11px; border-radius:2px; background:${meta.color}; margin-right:6px;"></span>${meta.label}: ${counts[type]}`;
            Object.assign(chip.style, {
                border: "1px solid var(--background-modifier-border)",
                background: "transparent",
                color: "var(--text-muted)",
                borderRadius: "6px",
                padding: "5px 9px",
                cursor: "pointer",
                transition: "all 0.16s ease"
            });
            chip.dataset.type = type;
            chips.push(chip);
        }

        const visualWrap = createElement("div", main);
        Object.assign(visualWrap.style, {
            position: "relative",
            border: "1px solid var(--background-modifier-border)",
            borderRadius: "8px",
            background: "var(--background-primary-alt)",
            overflow: "hidden"
        });

        const svgHost = createElement("div", visualWrap);
        Object.assign(svgHost.style, {
            width: "100%",
            minHeight: "760px"
        });

        const info = createElement("div", main);
        Object.assign(info.style, {
            minHeight: "86px",
            marginTop: "10px",
            padding: "11px 13px",
            border: "1px solid var(--background-modifier-border)",
            borderRadius: "8px",
            background: "var(--background-secondary)",
            color: "var(--text-normal)",
            lineHeight: "1.45"
        });

        if (!profiles.length || !edges.length) {
            info.textContent = "Недостаточно данных для построения диаграммы: проверьте req_race, req_spec, base_vector и weak_to.";
            return;
        }

        const width = 920;
        const height = 760;
        const radius = Math.min(width, height) / 2;
        const innerRadius = radius - 164;
        const labelRadius = innerRadius + 46;

        const svg = d3.select(svgHost)
            .append("svg")
            .attr("viewBox", [-width / 2, -height / 2, width, height])
            .style("width", "100%")
            .style("height", "760px")
            .style("display", "block")
            .style("background", "transparent");

        const defs = svg.append("defs");
        for (const [type, meta] of Object.entries(relationMeta)) {
            defs.append("marker")
                .attr("id", `arrow-${type}`)
                .attr("viewBox", "0 -5 10 10")
                .attr("refX", 9)
                .attr("refY", 0)
                .attr("markerWidth", 5)
                .attr("markerHeight", 5)
                .attr("orient", "auto-start-reverse")
                .attr("markerUnits", "strokeWidth")
                .append("path")
                .attr("d", "M0,-4L9,0L0,4")
                .style("fill", meta.color);
        }

        const groups = d3.group(profiles, profile => profile.groupName);
        const root = d3.hierarchy({
            name: "root",
            children: Array.from(groups, ([groupName, children]) => ({ name: groupName, children }))
        }).sort((a, b) =>
            d3.ascending(a.data.name, b.data.name) ||
            d3.ascending(a.data.id, b.data.id)
        );

        d3.cluster().size([360, innerRadius])(root);

        const leaves = root.leaves();
        const nodeMap = new Map(leaves.map(node => [node.data.id, node]));
        for (const edge of edges) {
            edge.sourceNode = nodeMap.get(edge.sourceId);
            edge.targetNode = nodeMap.get(edge.targetId);
        }
        const drawableEdges = edges.filter(edge => edge.sourceNode && edge.targetNode);

        svg.append("circle")
            .attr("r", innerRadius + 20)
            .style("fill", "none")
            .style("stroke", "var(--background-modifier-border)")
            .style("stroke-width", 1);

        const edgePaths = svg.append("g")
            .attr("class", "directed-edges")
            .selectAll("path")
            .data(drawableEdges)
            .join("path")
            .attr("d", quadraticArcPath)
            .attr("marker-end", d => `url(#arrow-${d.type})`)
            .attr("marker-start", d => d.direction === "both" ? `url(#arrow-${d.type})` : null)
            .style("fill", "none")
            .style("stroke", d => relationMeta[d.type].color)
            .style("stroke-width", d => 1.35 + d.strength * 0.28)
            .style("stroke-opacity", 0.42)
            .style("stroke-linecap", "round")
            .style("stroke-dasharray", d => relationMeta[d.type].dashed ? "5 5" : null)
            .style("mix-blend-mode", "screen")
            .style("cursor", "pointer");

        const labelGroups = svg.append("g")
            .attr("class", "labels")
            .selectAll("g")
            .data(leaves)
            .join("g")
            .attr("transform", d => {
                const [x, y] = polarPoint(d.x, labelRadius);
                return `translate(${x},${y}) rotate(${d.x < 180 ? d.x - 90 : d.x + 90})`;
            });

        labelGroups.append("circle")
            .attr("r", 4.3)
            .attr("cx", d => d.x < 180 ? -12 : 12)
            .style("fill", d => vectorColors[d.data.race?.baseVector] || "var(--text-muted)")
            .style("stroke", "var(--background-primary)")
            .style("stroke-width", 1.5);

        labelGroups.append("text")
            .attr("dy", "0.32em")
            .attr("x", d => d.x < 180 ? 0 : -16)
            .attr("text-anchor", d => d.x < 180 ? "start" : "end")
            .text(d => d.data.name)
            .style("fill", "var(--text-normal)")
            .style("font-size", "13.5px")
            .style("font-weight", 650)
            .style("letter-spacing", "0")
            .style("paint-order", "stroke")
            .style("stroke", "var(--background-primary)")
            .style("stroke-width", "4px")
            .style("stroke-linejoin", "round")
            .style("cursor", "pointer");

        const centerLabel = svg.append("g")
            .attr("text-anchor", "middle");

        centerLabel.append("text")
            .attr("y", -10)
            .style("fill", "var(--text-normal)")
            .style("font-size", "18px")
            .style("font-weight", 750)
            .text(`${profiles.length} сборок`);

        centerLabel.append("text")
            .attr("y", 16)
            .style("fill", "var(--text-muted)")
            .style("font-size", "12.5px")
            .text(`${drawableEdges.length} отдельных линий`);

        function setDefaultInfo() {
            info.innerHTML = `
                <div style="font-weight:750; margin-bottom:4px;">Направленная карта связей</div>
                <div style="font-size:0.92em; color:var(--text-muted);">
                    Наведите на линию, сборку или тип связи. Параллельные линии разведены сдвигом, чтобы разные причины не слипались.
                </div>
            `;
        }

        function edgeSummary(edge) {
            const meta = relationMeta[edge.type];
            const arrow = edge.direction === "both" ? "↔" : "→";
            return `
                <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
                    <span style="display:inline-block; width:11px; height:11px; border-radius:2px; background:${meta.color};"></span>
                    <strong>${meta.label}</strong>
                    <span style="color:var(--text-muted);">линия ${edge.parallelIndex > 0 ? "+" : ""}${edge.parallelIndex}</span>
                </div>
                <div><strong>${edge.source.name}</strong> ${arrow} <strong>${edge.target.name}</strong></div>
                <div style="font-size:0.9em; color:var(--text-muted); margin-top:6px;">${edge.reasons.join("<br>")}</div>
            `;
        }

        function resetHighlight() {
            edgePaths
                .style("stroke-opacity", 0.42)
                .style("stroke-width", d => 1.35 + d.strength * 0.28);
            labelGroups.style("opacity", 1);
            chips.forEach(chip => {
                chip.style.background = "transparent";
                chip.style.color = "var(--text-muted)";
            });
            setDefaultInfo();
        }

        function highlightType(type) {
            const meta = relationMeta[type];
            edgePaths
                .style("stroke-opacity", d => d.type === type ? 0.92 : 0.04)
                .style("stroke-width", d => d.type === type ? 2 + d.strength * 0.38 : 1);
            labelGroups.style("opacity", 0.55);
            chips.forEach(chip => {
                const active = chip.dataset.type === type;
                chip.style.background = active ? "var(--background-modifier-hover)" : "transparent";
                chip.style.color = active ? "var(--text-normal)" : "var(--text-muted)";
            });
            info.innerHTML = `
                <div style="display:flex; align-items:center; gap:8px; font-weight:750;">
                    <span style="display:inline-block; width:11px; height:11px; border-radius:2px; background:${meta.color};"></span>
                    ${meta.label}: ${counts[type]}
                </div>
                <div style="font-size:0.92em; color:var(--text-muted); margin-top:5px;">${meta.description}</div>
            `;
        }

        function highlightNode(node) {
            const related = new Set([node.data.id]);
            const activeEdges = [];

            edgePaths
                .style("stroke-opacity", edge => {
                    const active = edge.sourceNode === node || edge.targetNode === node;
                    if (active) {
                        activeEdges.push(edge);
                        related.add(edge.sourceNode.data.id);
                        related.add(edge.targetNode.data.id);
                    }
                    return active ? 0.95 : 0.035;
                })
                .style("stroke-width", edge => {
                    const active = edge.sourceNode === node || edge.targetNode === node;
                    return active ? 2.15 + edge.strength * 0.38 : 1;
                });

            labelGroups.style("opacity", d => related.has(d.data.id) ? 1 : 0.22);

            const profile = node.data;
            info.innerHTML = `
                <div style="font-weight:750;">${profile.name}</div>
                <div style="font-size:0.92em; color:var(--text-muted); margin-top:4px;">
                    ${profile.race?.name || profile.reqRace} + ${profile.spec?.name || profile.reqSpec}<br>
                    Векторы: ${vectorList(profile.vectors)}<br>
                    Общая слабость: ${vectorList(profile.sharedWeakness)}<br>
                    Активных линий: ${activeEdges.length}
                </div>
            `;
        }

        edgePaths
            .on("mouseover", function(event, edge) {
                d3.select(this)
                    .style("stroke-opacity", 1)
                    .style("stroke-width", 2.5 + edge.strength * 0.45)
                    .raise();

                labelGroups.style("opacity", node =>
                    node === edge.sourceNode || node === edge.targetNode ? 1 : 0.25
                );
                info.innerHTML = edgeSummary(edge);
            })
            .on("mouseout", resetHighlight);

        labelGroups
            .on("mouseover", function(event, node) {
                d3.select(this).select("text")
                    .style("fill", "var(--text-accent)")
                    .style("font-weight", 800);
                highlightNode(node);
            })
            .on("mouseout", function() {
                d3.select(this).select("text")
                    .style("fill", "var(--text-normal)")
                    .style("font-weight", 650);
                resetHighlight();
            })
            .on("click", (event, node) => {
                dv.app.workspace.openLinkText(`${files.combos}#${node.data.header}`, currentPath, false);
            });

        allChip.onmouseover = resetHighlight;
        allChip.onclick = resetHighlight;

        chips.forEach(chip => {
            chip.onmouseover = () => highlightType(chip.dataset.type);
            chip.onfocus = () => highlightType(chip.dataset.type);
            chip.onmouseout = resetHighlight;
            chip.onblur = resetHighlight;
        });

        setDefaultInfo();

        dv.header(3, "Сильнейшие отдельные линии");
        dv.table(
            ["Направление", "Тип", "Причины"],
            edges
                .slice()
                .sort((a, b) => b.strength - a.strength || relationMeta[a.type].order - relationMeta[b.type].order)
                .slice(0, 14)
                .map(edge => [
                    `${profileLink(edge.source)} ${edge.direction === "both" ? "↔" : "→"} ${profileLink(edge.target)}`,
                    relationMeta[edge.type].label,
                    edge.reasons.join("<br>")
                ])
        );
    } catch (error) {
        dv.container.innerHTML = "";
        dv.header(2, "Ошибка направленной карты");
        dv.paragraph(error.message);
    }
})();
```
