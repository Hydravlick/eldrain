```dataviewjs
// === 1. ЗАГРУЗКА БИБЛИОТЕКИ ===
async function loadD3() {
    if (window.d3) return window.d3;
    dv.span("⏳ Загрузка визуализации...");
    return new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = "https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js";
        script.onload = () => { dv.span(""); resolve(window.d3); };
        script.onerror = () => reject(new Error("Ошибка загрузки D3"));
        document.head.appendChild(script);
    });
}

try {
    const d3 = await loadD3();
    
    // === 2. КОНФИГУРАЦИЯ ===
    const width = 500; 
    const outerRadius = width / 2 - 100; 
    const innerRadius = 50;             
    const bundleTension = 0.60;         
    
    const sourceFilePath = "Registry_Factions.md"; 

    // === 2.1 НАСТРОЙКА ЛЕГЕНДЫ ===
    const legendData = [
        { label: "Враги", groupingKey: "Enemies", color: "#ff4757", priority: 10, types: ["enemy", "rival", "conflict", "hunt"] },
        { label: "Власть", groupingKey: "Power", color: "#00b8ff", priority: 8, types: ["command", "client", "monitor"] },
        { label: "Союз", groupingKey: "Union", color: "#00ff9d", priority: 6, types: ["partner", "synergy", "friend"] },
        { label: "Культ", groupingKey: "Cult", color: "#d980fa", priority: 5, types: ["worship", "servant"] },
        { label: "Торговля", groupingKey: "Trade", color: "#ffa502", priority: 4, types: ["trade"] },
        { label: "Слежка", groupingKey: "Spy", color: "#a4b0be", priority: 2, types: ["spy"] }, 
        { label: "Нейтрально", groupingKey: "Neutral", color: "#a4b0be", priority: 1, types: ["neutral", "default"] }
    ];

    const colorMap = {};
    const priorityMap = {};
    const typeToGroupMap = {}; 
    const groupToLabelMap = {}; 

    legendData.forEach(g => {
        groupToLabelMap[g.groupingKey] = g.label;
        g.types.forEach(t => {
            colorMap[t] = g.color;
            priorityMap[t] = g.priority;
            typeToGroupMap[t] = g.groupingKey;
        });
    });

    const nodeColors = { "center": "#feca57", "default": "#ffffff" };

    // === 3. ПАРСИНГ ДАННЫХ ===
    const page = dv.page(sourceFilePath);
    if (!page) throw new Error("Файл не найден: " + sourceFilePath);

    const rawContent = (await dv.io.load(page.file.path)) + "\n\n## END_MARKER";
    const rawBlocks = rawContent.split(/^##\s+/m).slice(1); 
    const cleanID = (str) => str ? str.toLowerCase().trim() : null;
    
    const getRelDetails = (text) => {
        const re = /\[rel_([a-zA-Z0-9_]+)::\s*([^\]]+)\](?:[^\\n\\r]*?\(?([^)\n\r]+)\)?)?/g;
        return [...text.matchAll(re)].map(m => {
            let idRaw = m[2].trim();
            if (idRaw.includes('(')) idRaw = idRaw.split('(')[0].trim();
            let cleanReason = m[3] ? m[3].replace(/[`()]/g, "").trim() : null;
            return { 
                type: m[1].toLowerCase(), 
                targetId: cleanID(idRaw), 
                reason: cleanReason 
            };
        });
    };

    let nodes = [];
    nodes.push({
        id: "player", name: "Player", fullName: "Player Character",
        isCenter: true, desc: "Центр событий.", rawRelations: []
    });

    rawBlocks.forEach(blockText => {
        const lines = blockText.split('\n');
        const header = lines[0].trim();
        if (header === "END_MARKER") return; 

        const body = lines.slice(1).join('\n');
        const idMatch = body.match(/\[faction::\s*([^\]]+)\]/);
        if (!idMatch) return;
        
        const isCenter = /\[(role|tier|faction)::\s*(center|hidden|major)\]/i.test(body);
        const descMatch = body.match(/\*([^*]+)\*/);

        nodes.push({
            id: cleanID(idMatch[1]),
            name: header.split('(')[0].trim(),
            fullName: header,
            isCenter: isCenter,
            desc: descMatch ? descMatch[1] : "...",
            rawRelations: getRelDetails(body)
        });
    });

    // === 4. ГРУППИРОВКА СВЯЗЕЙ ===
    const nodeMap = new Map(nodes.map(n => [n.id, n]));
    const uniquePairs = new Map();

    const addRelation = (src, tgt, type, reason) => {
        if (!src || !tgt) return;
        const pairKey = [src.id, tgt.id].sort().join("-");
        
        if (!uniquePairs.has(pairKey)) {
            uniquePairs.set(pairKey, {
                source: src, target: tgt,
                relations: [],
                maxPriority: -1,
                dominantType: "neutral"
            });
        }
        
        const pair = uniquePairs.get(pairKey);
        pair.relations.push({
            fromName: src.name, 
            type: type,
            reason: reason
        });

        const p = priorityMap[type] || 0;
        if (p > pair.maxPriority) {
            pair.maxPriority = p;
            pair.dominantType = type;
        }
    };

    nodes.forEach(srcNode => {
        if (!srcNode.rawRelations) return;

        const explicitTargets = new Set();
        srcNode.rawRelations.forEach(r => {
            if (r.targetId !== "all" && r.targetId !== "any") {
                explicitTargets.add(r.targetId);
            }
        });

        srcNode.rawRelations.forEach(rel => {
            if (rel.targetId === "all" || rel.targetId === "any") {
                nodes.forEach(targetNode => {
                    if (targetNode.id !== srcNode.id && !explicitTargets.has(targetNode.id)) {
                         addRelation(srcNode, targetNode, rel.type, rel.reason || "Universal relation");
                    }
                });
            } else {
                const targetNode = nodeMap.get(rel.targetId);
                addRelation(srcNode, targetNode, rel.type, rel.reason);
            }
        });
    });

    // === 5. РАСЧЕТ КООРДИНАТ ===
    const root = d3.hierarchy({ children: nodes }).sum(() => 1);
    const cluster = d3.cluster().size([360, outerRadius]);
    cluster(root);

    const leaves = root.leaves();
    const centerNodes = leaves.filter(d => d.data.isCenter);
    const outerNodes = leaves.filter(d => !d.data.isCenter);

    outerNodes.forEach((d, i) => { d.y = outerRadius; d.x = i * (360 / outerNodes.length); });
    centerNodes.forEach((d, i) => { d.y = innerRadius; d.x = i * (360 / centerNodes.length); });

    const d3NodeMap = new Map(leaves.map(d => [d.data.id, d]));
    
    const finalLinks = Array.from(uniquePairs.values()).map(pair => {
        const src = d3NodeMap.get(pair.source.id);
        const tgt = d3NodeMap.get(pair.target.id);
        if (!src || !tgt) return null;
        return {
            source: src, target: tgt, 
            dominantType: pair.dominantType,
            relations: pair.relations,
            path: src.path(tgt) 
        };
    }).filter(l => l !== null);

    // === 6. ОТРИСОВКА ===
    dv.container.innerHTML = "";
    const mainContainer = dv.container.createDiv({ cls: "faction-container" });
    
    // 6.1 ЛЕГЕНДА (ОБНОВЛЕННАЯ ВЕРСИЯ С D3)
    const legendDiv = mainContainer.createDiv({ cls: "faction-legend" });
    Object.assign(legendDiv.style, {
        display: "flex", justifyContent: "center", flexWrap: "wrap", gap: "15px",
        marginBottom: "10px", padding: "10px", borderBottom: "1px solid var(--background-modifier-border)"
    });

    const legendItems = d3.select(legendDiv)
        .selectAll("div.legend-item")
        .data(legendData)
        .join("div")
        .style("display", "flex")
        .style("align-items", "center")
        .style("font-size", "11px")
        .style("color", "var(--text-muted)")
        .style("cursor", "pointer") // Курсор показывает кликабельность
        .on("mouseover", function(e, d) {
            d3.select(this).style("color", "var(--text-normal)").style("font-weight", "bold");
            highlightGroup(d.groupingKey, d.label, d.color);
        })
        .on("mouseout", function() {
            d3.select(this).style("color", "var(--text-muted)").style("font-weight", "normal");
            resetHighlight();
        });

    legendItems.append("span")
        .style("display", "inline-block")
        .style("width", "10px")
        .style("height", "10px")
        .style("background", d => d.color)
        .style("margin-right", "6px")
        .style("border-radius", "2px");

    legendItems.append("span")
        .text(d => d.label);

    // 6.2 SVG
    const svg = d3.select(mainContainer).append("svg")
        .attr("viewBox", [-width/2, -width/2, width, width])
        .style("width", "100%").style("height", "auto")
        .style("font-family", "var(--font-interface)");

    const lineGen = d3.lineRadial()
        .curve(d3.curveBundle.beta(bundleTension)) 
        .radius(d => d.y)
        .angle(d => d.x / 180 * Math.PI);

    const linkPaths = svg.append("g").selectAll("path")
        .data(finalLinks).join("path")
        .attr("d", d => lineGen(d.path))
        .style("fill", "none")
        .style("stroke", d => colorMap[d.dominantType] || "#555")
        .style("stroke-opacity", 0.4)
        .style("stroke-width", 2)
        .style("cursor", "pointer")
        .style("transition", "stroke-opacity 0.2s ease") // Плавность
        .on("mouseover", function(e, d) {
            d3.select(this).style("stroke-opacity", 1).style("stroke-width", 4);
            updateInfoPair(d);
        })
        .on("mouseout", function() {
            d3.select(this).style("stroke-opacity", 0.4).style("stroke-width", 2);
            setDefaultInfo();
        });

    const labels = svg.append("g").selectAll("g")
        .data(outerNodes).join("g")
        .attr("transform", d => `rotate(${d.x - 90}) translate(${d.y + 10},0)`);

    labels.append("text")
        .attr("dy", "0.31em")
        .attr("text-anchor", d => d.x < 180 ? "start" : "end")
        .attr("transform", d => d.x >= 180 ? "rotate(180)" : null)
        .text(d => d.data.name)
        .style("fill", "var(--text-normal)")
        .style("font-size", "11px")
        .style("cursor", "pointer")
        .style("transition", "opacity 0.2s ease")
        .on("mouseover", (e, d) => highlightNode(d))
        .on("mouseout", resetHighlight)
        .on("click", (e, d) => openLink(d));

    const centers = svg.append("g").selectAll("g")
        .data(centerNodes).join("g")
        .attr("transform", d => `rotate(${d.x - 90}) translate(${d.y},0)`);

    centers.append("circle")
        .attr("r", 14)
        .style("fill", d => d.data.id === "player" ? "#fff" : nodeColors.center)
        .style("stroke", "var(--background-primary)")
        .style("stroke-width", 4)
        .style("cursor", "pointer")
        .style("transition", "opacity 0.2s ease")
        .on("mouseover", (e, d) => highlightNode(d))
        .on("mouseout", resetHighlight);

    centers.append("text")
        .attr("dy", "0.35em")
        .attr("text-anchor", "middle")
        .attr("transform", d => `rotate(${-(d.x - 90)})`)
        .text(d => d.data.name[0])
        .style("fill", "var(--background-primary)")
        .style("font-weight", "bold")
        .style("font-size", "11px")
        .style("pointer-events", "none");

    // 6.3 ИНФО-ПАНЕЛЬ
    const infoPanel = mainContainer.createDiv({ cls: "faction-info-panel" });
    Object.assign(infoPanel.style, {
        minHeight: "50px", marginTop: "5px", padding: "10px",
        background: "var(--background-secondary)", borderRadius: "8px",
        textAlign: "center", fontSize: "0.9em", border: "1px solid var(--background-modifier-border)",
        display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center"
    });

    function setDefaultInfo() {
        const totalRelations = finalLinks.reduce((acc, l) => acc + l.relations.length, 0);
        
        const counts = {};
        legendData.forEach(g => counts[g.label] = 0);
        
        finalLinks.forEach(l => {
            l.relations.forEach(r => {
                const groupKey = typeToGroupMap[r.type];
                const label = groupToLabelMap[groupKey];
                if (label) counts[label]++;
            });
        });

        const statsHtml = legendData
            .filter(g => counts[g.label] > 0)
            .map(g => `<span style="color:${g.color}; margin: 0 6px">● ${g.label}: ${counts[g.label]}</span>`)
            .join("");

        infoPanel.innerHTML = `
            <div style="font-weight:bold; margin-bottom: 5px;">Активных взаимодействий: ${totalRelations}</div>
            <div style="font-size: 0.85em; display:flex; flex-wrap:wrap; justify-content:center; line-height: 1.4;">${statsHtml}</div>
            <div style="font-size: 0.8em; color:var(--text-muted); margin-top:5px">Наведите на узел или легенду для деталей</div>
        `;
    }
    
    setDefaultInfo();

    // === НОВАЯ ФУНКЦИЯ ДЛЯ ПОДСВЕТКИ ГРУППЫ ===
    function highlightGroup(groupKey, label, color) {
        // Глушим всё, что не относится к группе
        linkPaths.style("stroke-opacity", d => {
            const linkGroup = typeToGroupMap[d.dominantType];
            return linkGroup === groupKey ? 1 : 0.05;
        }).style("stroke-width", d => {
            const linkGroup = typeToGroupMap[d.dominantType];
            return linkGroup === groupKey ? 3 : 2;
        });
        
        // Считаем сколько их
        const count = finalLinks.filter(d => typeToGroupMap[d.dominantType] === groupKey).length;

        infoPanel.innerHTML = `
            <strong style="font-size:1.1em; color:${color}">${label}</strong>
            <hr style="margin:5px 0; border-color:var(--background-modifier-border); width: 50%">
            <div>Всего связей: <strong>${count}</strong></div>
        `;
    }

    function updateInfoPair(d) {
        const grouped = {};
        
        d.relations.forEach(r => {
            const groupKey = typeToGroupMap[r.type] || "Neutral";
            if (!grouped[groupKey]) {
                grouped[groupKey] = {
                    key: groupKey, reasons: [], directions: new Set(),
                    color: colorMap[r.type] || "#777", label: groupToLabelMap[groupKey] || r.type
                };
            }
            if (r.reason && !grouped[groupKey].reasons.includes(r.reason)) grouped[groupKey].reasons.push(r.reason);
            grouped[groupKey].directions.add(r.fromName);
        });

        let htmlContent = `<div style="margin-bottom: 6px; font-weight: bold; color: var(--text-normal)">Взаимодействия</div>`;
        const srcName = d.source.data.name;
        const tgtName = d.target.data.name;

        Object.values(grouped).forEach(g => {
            let arrowHtml = "";
            let leftName = srcName;
            let rightName = tgtName;
            const isBidirectional = g.directions.has(srcName) && g.directions.has(tgtName);
            
            if (isBidirectional) {
                arrowHtml = `<span style="color:${g.color}; font-size:1.2em">↔</span>`;
            } else {
                arrowHtml = `<span style="color:${g.color}; font-size:1.2em">→</span>`;
                if (g.directions.has(tgtName) && !g.directions.has(srcName)) {
                    leftName = tgtName; rightName = srcName;
                }
            }
            const reasonsText = g.reasons.length > 0 ? `"${g.reasons.join(" / ")}"` : "";

            htmlContent += `
                <div style="margin-bottom: 6px; border-bottom: 1px solid var(--background-modifier-border); padding-bottom: 4px;">
                    <div style="display:flex; justify-content:center; align-items:center; gap: 8px;">
                        <span style="font-weight:bold">${leftName}</span> 
                        ${arrowHtml}
                        <span style="font-weight:bold">${rightName}</span>
                    </div>
                    <div style="margin-top:2px;">
                        <span style="color:${g.color}; font-size: 0.85em; font-weight:bold;">[${g.label}]</span>
                        <span style="font-style:italic; color:var(--text-accent); font-size: 0.9em; margin-left: 5px">${reasonsText}</span>
                    </div>
                </div>
            `;
        });
        infoPanel.innerHTML = htmlContent;
    }

    function highlightNode(d) {
        linkPaths.style("stroke-opacity", 0.05);
        labels.style("opacity", 0.3);
        centers.style("opacity", 0.3);

        const related = linkPaths.filter(l => l.source === d || l.target === d)
            .style("stroke-opacity", 1).style("stroke-width", 3).raise();

        const neighbors = new Set([d]);
        related.each(l => { neighbors.add(l.source); neighbors.add(l.target); });

        labels.filter(n => neighbors.has(n)).style("opacity", 1).style("font-weight", "bold");
        centers.filter(n => neighbors.has(n)).style("opacity", 1);

        infoPanel.innerHTML = `
            <strong style="font-size:1.1em; color:var(--text-normal)">${d.data.name}</strong>
            <hr style="margin:5px 0; border-color:var(--background-modifier-border); width: 50%">
            <div style="font-style:italic; color:var(--text-muted)">${d.data.desc}</div>
        `;
    }

    function resetHighlight() {
        linkPaths.style("stroke-opacity", 0.4).style("stroke-width", 2);
        labels.style("opacity", 1).style("font-weight", "normal");
        centers.style("opacity", 1);
        setDefaultInfo();
    }

    function openLink(d) {
         const link = `${sourceFilePath}#${d.data.fullName}`;
         dv.app.workspace.openLinkText(link, sourceFilePath, false);
    }

} catch (e) {
    dv.paragraph("❌ Ошибка: " + e.message);
}
```