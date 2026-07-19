---
type: mechanic
status: active
system: factions
tags:
  - factions
---

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
    const outerRadius = width / 2 - 120; 
    const innerRadius = 50;             
    const bundleTension = 0.60;         
    
    const sourceFolder = "03_Factions_Societies/Lore";

    // === 2.1 НАСТРОЙКА ЛЕГЕНДЫ ===
    const legendData = [
        { label: "Враги", groupingKey: "Enemies", color: "#ff4757", priority: 10, types: ["conflict", "hunt"] },
        { label: "Власть", groupingKey: "Power", color: "#00b8ff", priority: 8, types: ["monitor"] },
        { label: "Союз", groupingKey: "Union", color: "#00ff9d", priority: 6, types: ["union"] }, 
        { label: "Торговля", groupingKey: "Trade", color: "#ffa502", priority: 4, types: ["trade"] },
        { label: "Тайны", groupingKey: "Spy", color: "#a4b0be", priority: 2, types: ["spy"] }
    ];

    const UNKNOWN_COLOR = "#57606f"; 

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
    const cleanID = (str) => str ? str.toLowerCase().trim() : null;
    
    const getRelDetails = (text) => {
        const re = /\[rel_([a-zA-Z0-9_]+)::\s*([^\]]+)\](?:[^\n\r]*?\(?([^)\n\r]+)\)?)?/g;
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

    const factionPages = Array.from(dv.pages('"03_Factions_Societies/Lore"'))
        .filter(page => page.type === "faction")
        .sort((a, b) => Number(a.sort_order ?? 9999) - Number(b.sort_order ?? 9999));

    if (factionPages.length === 0) {
        throw new Error("В папке фракций не найдено ни одной сущности");
    }

    const factionNodes = await Promise.all(factionPages.map(async page => {
        const body = await dv.io.load(page.file.path);
        return {
            id: cleanID(page.faction_id),
            name: page.display_name || page.file.name,
            path: page.file.path,
            isCenter: ["supra_faction", "hidden"].includes(cleanID(page.faction_role)),
            desc: page.promise || "...",
            rawRelations: getRelDetails(body)
        };
    }));

    const errors = [];
    const validTypes = new Set(legendData.flatMap(group => group.types));
    const factionIds = new Set();

    factionNodes.forEach(node => {
        if (!node.id) {
            errors.push(`Нет faction_id: ${node.path}`);
            return;
        }
        if (factionIds.has(node.id)) errors.push(`Повтор faction_id: ${node.id}`);
        factionIds.add(node.id);
    });

    factionNodes.forEach(node => {
        node.rawRelations.forEach(rel => {
            if (!validTypes.has(rel.type)) errors.push(`Неизвестный тип связи ${rel.type}: ${node.id}`);
            if (!["all", "any"].includes(rel.targetId) && !factionIds.has(rel.targetId)) {
                errors.push(`Неизвестная цель ${rel.targetId}: ${node.id}`);
            }
            if (!rel.reason) errors.push(`Нет причины связи ${node.id} -> ${rel.targetId}`);
        });
    });

    if (errors.length > 0) throw new Error(errors.join("; "));

    const nodes = [{
        id: "player", name: "Player", path: null,
        isCenter: true, desc: "Центр событий.", rawRelations: []
    }, ...factionNodes];

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
                dominantType: null
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
            return; 
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
    
    const centerOffset = 360 / 12; 
    centerNodes.forEach((d, i) => { 
        d.y = innerRadius; 
        d.x = i * (360 / centerNodes.length) + centerOffset; 
    });

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

    function linkHasGroup(link, groupKey) {
        return link.relations.some(r => typeToGroupMap[r.type] === groupKey);
    }

    function countRelationsForGroup(groupKey, links = finalLinks) {
        return links.reduce((total, link) =>
            total + link.relations.filter(r => typeToGroupMap[r.type] === groupKey).length,
            0
        );
    }

    function countPairsForGroup(groupKey, links = finalLinks) {
        return links.filter(link => linkHasGroup(link, groupKey)).length;
    }

    const legendRelationCounts = {};
    legendData.forEach(g => legendRelationCounts[g.groupingKey] = countRelationsForGroup(g.groupingKey));
    const totalRelations = finalLinks.reduce((acc, l) => acc + l.relations.length, 0);

    // === 6. ОТРИСОВКА ===
    dv.container.innerHTML = "";
    const mainContainer = dv.container.createDiv({ cls: "faction-container" });
    mainContainer.style.maxWidth = "500px";
    mainContainer.style.margin = "0 auto";
    
    // 6.1 ЛЕГЕНДА
    let activeFilters = new Set(); 

    const legendDiv = mainContainer.createDiv({ cls: "faction-legend" });
    Object.assign(legendDiv.style, {
        display: "flex", justifyContent: "center", flexWrap: "wrap", gap: "4px",
        marginBottom: "8px", padding: "4px", borderBottom: "1px solid var(--background-modifier-border)"
    });

    const allChip = d3.select(legendDiv)
        .append("button")
        .style("padding", "5px 9px")
        .style("border", "1px solid var(--background-modifier-border)")
        .style("border-radius", "4px")
        .style("background", "var(--background-secondary)")
        .style("color", "var(--text-normal)")
        .style("font-size", "12px")
        .style("cursor", "pointer")
        .style("font-family", "inherit")
        .text(`Всего: ${totalRelations}`)
        .on("click", () => {
            activeFilters.clear();
            applyFilters();
        })
        .on("mouseover", resetHighlight);

    const legendItems = d3.select(legendDiv)
        .selectAll("button.legend-item")
        .data(legendData)
        .join("button")
        .attr("class", "legend-item")
        .style("display", "inline-flex")
        .style("align-items", "center")
        .style("padding", "5px 9px")
        .style("border", "1px solid transparent")
        .style("border-radius", "4px")
        .style("background", "transparent")
        .style("color", "var(--text-muted)")
        .style("font-size", "12px")
        .style("cursor", "pointer")
        .style("white-space", "nowrap")
        .style("transition", "all 0.16s ease")
        .style("font-family", "inherit")
        .on("click", function(e, d) {
            if (activeFilters.has(d.groupingKey)) {
                activeFilters.delete(d.groupingKey);
            } else {
                activeFilters.add(d.groupingKey);
            }
            applyFilters();
        })
        .on("mouseover", function(e, d) {
            if (activeFilters.size === 0) {
                highlightGroup(d.groupingKey, d.label, d.color);
            } else {
                previewGroupWithinFilter(d.groupingKey, d.label, d.color);
            }
        })
        .on("mouseout", function() {
            resetHighlight();
        });

    legendItems.append("span")
        .style("display", "inline-block")
        .style("width", "10px")
        .style("height", "10px")
        .style("background", d => d.color)
        .style("margin-right", "6px")
        .style("border-radius", "2px");

    legendItems.append("span").text(d => `${d.label}: ${legendRelationCounts[d.groupingKey] || 0}`);

    // 6.2 SVG
    const svgContainer = mainContainer.createDiv();
    const svg = d3.select(svgContainer).append("svg")
        .attr("viewBox", [-width/2, -width/2, width, width])
        .style("width", "500px")
        .style("height", "500px")
        .style("display", "block")
        .style("margin", "0 auto")
        .style("font-family", "var(--font-interface)");

    const lineGen = d3.lineRadial()
        .curve(d3.curveBundle.beta(bundleTension)) 
        .radius(d => d.y)
        .angle(d => d.x / 180 * Math.PI);

    const linkPaths = svg.append("g").selectAll("path")
        .data(finalLinks).join("path")
        .attr("d", d => lineGen(d.path))
        .style("fill", "none")
        .style("stroke", d => colorMap[d.dominantType] || UNKNOWN_COLOR)
        .style("stroke-opacity", 0.4)
        .style("stroke-width", 2)
        .style("cursor", "pointer")
        .style("transition", "stroke-opacity 0.2s ease")
        .on("mouseover", function(e, d) {
            if (!isLinkActive(d)) {
                updateInfoPair(d);
                return;
            }
            d3.select(this).style("stroke-opacity", 1).style("stroke-width", 4).raise();
            updateInfoPair(d);
        })
        .on("mouseout", function() {
            resetHighlight();
        });

    const labelGroups = svg.append("g").selectAll("g")
        .data(outerNodes).join("g")
        .attr("transform", d => `rotate(${d.x - 90}) translate(${d.y + 8},0)`);

    const labels = labelGroups.append("text")
        .attr("dy", "0.31em")
        .attr("text-anchor", d => d.x < 180 ? "start" : "end")
        .attr("transform", d => d.x >= 180 ? "rotate(180)" : null)
        .text(d => d.data.name)
        .style("fill", "var(--text-normal)")
        .style("font-size", "11px")
        .style("cursor", "pointer")
        .style("transition", "all 0.2s ease")
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
        .style("cursor", d => d.data.id === "player" ? "default" : "pointer") 
        .style("transition", "opacity 0.2s ease")
        .on("mouseover", (e, d) => highlightNode(d))
        .on("mouseout", resetHighlight)
        .on("click", (e, d) => {
             if (d.data.id !== "player") openLink(d); 
        });

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
        minHeight: "60px",
        marginTop: "5px", padding: "10px",
        background: "var(--background-secondary)", borderRadius: "8px",
        textAlign: "center", 
        border: "1px solid var(--background-modifier-border)",
        display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center"
    });

    function setDefaultInfo() {
        infoPanel.innerHTML = `
            <div style="font-weight:bold; color:var(--text-normal); font-size: 1em;">Карта отношений</div>
            <div style="font-size: 0.82em; color:var(--text-muted); margin-top:4px">Наведите на узел, линию или тип связи для деталей</div>
        `;
    }
    
    setDefaultInfo();
    
    function isLinkActive(d) {
        if (activeFilters.size === 0) return true;
        return d.relations.some(r => activeFilters.has(typeToGroupMap[r.type]));
    }

    function dominantMatchedType(d) {
        if (activeFilters.size === 0) return d.dominantType;
        const matched = d.relations.filter(r => activeFilters.has(typeToGroupMap[r.type]));
        if (matched.length === 0) return d.dominantType;
        let maxP = -1, domT = d.dominantType;
        matched.forEach(r => {
            const p = priorityMap[r.type] ?? -1;
            if (p > maxP) { maxP = p; domT = r.type; }
        });
        return domT;
    }

    function resolveLinkColor(d) {
        return colorMap[dominantMatchedType(d)] || UNKNOWN_COLOR;
    }

    function nodeHasVisibleLink(n) {
        return finalLinks.some(l => (l.source === n || l.target === n) && isLinkActive(l));
    }

    function renderBaseState() {
        const filtered = activeFilters.size > 0;

        linkPaths
            .style("stroke", d => resolveLinkColor(d))
            .style("stroke-opacity", d => filtered ? (isLinkActive(d) ? 0.8 : 0.02) : 0.4)
            .style("stroke-width", d => filtered ? (isLinkActive(d) ? 3 : 1) : 2);

        labels
            .style("opacity", d => filtered ? (nodeHasVisibleLink(d) ? 1 : 0.25) : 1)
            .style("font-weight", "normal")
            .style("fill", "var(--text-normal)");
        centers
            .style("opacity", d => filtered ? (nodeHasVisibleLink(d) ? 1 : 0.25) : 1);

        if (filtered) {
            infoPanel.innerHTML = `<div style="font-weight:bold; font-size: 1.1em; color: var(--text-normal)">Режим фильтрации</div>
            <div style="font-size: 0.9em; color:var(--text-muted)">Показаны связи: ${Array.from(activeFilters).map(k => groupToLabelMap[k]).join(" + ")}</div>`;
        } else {
            setDefaultInfo();
        }
    }

    function applyFilters() {
        const isAll = activeFilters.size === 0;

        allChip
            .style("background", isAll ? "var(--background-secondary)" : "transparent")
            .style("border-color", isAll ? "var(--background-modifier-border)" : "transparent")
            .style("color", isAll ? "var(--text-normal)" : "var(--text-muted)");

        legendItems
            .style("background", d => activeFilters.has(d.groupingKey) ? "var(--background-modifier-hover)" : "transparent")
            .style("color", d => activeFilters.has(d.groupingKey) ? "var(--text-normal)" : "var(--text-muted)")
            .style("font-weight", d => activeFilters.has(d.groupingKey) ? "600" : "normal")
            .style("border-color", d => activeFilters.has(d.groupingKey) ? d.color : "transparent");

        renderBaseState();
    }

    function highlightGroup(groupKey, label, color) {
        linkPaths.style("stroke-opacity", d => {
            return linkHasGroup(d, groupKey) ? 1 : 0.05;
        }).style("stroke-width", d => {
            return linkHasGroup(d, groupKey) ? 3 : 2;
        });
        
        const relationCount = countRelationsForGroup(groupKey);
        const pairCount = countPairsForGroup(groupKey);

        infoPanel.innerHTML = `
            <div style="font-weight:bold; color:${color}; font-size: 1.1em">${label}</div>
            <hr style="margin:5px 0; border-color:var(--background-modifier-border); width: 50%">
            <div>Отношений: <strong>${relationCount}</strong>; пар: <strong>${pairCount}</strong></div>
        `;
    }

    function previewGroupWithinFilter(groupKey, label, color) {
        linkPaths.style("stroke-opacity", d => {
            if (!isLinkActive(d)) return 0.02;
            return linkHasGroup(d, groupKey) ? 1 : 0.15;
        }).style("stroke-width", d => {
            if (!isLinkActive(d)) return 1;
            return linkHasGroup(d, groupKey) ? 3 : 2;
        });

        const visibleLinks = finalLinks.filter(isLinkActive);
        const relationCount = countRelationsForGroup(groupKey, visibleLinks);
        const pairCount = countPairsForGroup(groupKey, visibleLinks);

        infoPanel.innerHTML = `
            <div style="font-weight:bold; color:${color}; font-size: 1.1em">${label}</div>
            <hr style="margin:5px 0; border-color:var(--background-modifier-border); width: 50%">
            <div>В текущем фильтре: <strong>${relationCount}</strong> отношений; <strong>${pairCount}</strong> пар</div>
        `;
    }

    function updateInfoPair(d) {
        const grouped = {};
        d.relations.forEach(r => {
            const groupKey = typeToGroupMap[r.type] || r.type;
            if (!grouped[groupKey]) {
                grouped[groupKey] = {
                    key: groupKey, reasons: [], directions: new Set(),
                    color: colorMap[r.type] || UNKNOWN_COLOR, label: groupToLabelMap[groupKey] || r.type
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
            
            if (isBidirectional) arrowHtml = `<span style="color:${g.color}; font-size:1.2em">↔</span>`;
            else {
                arrowHtml = `<span style="color:${g.color}; font-size:1.2em">→</span>`;
                if (g.directions.has(tgtName) && !g.directions.has(srcName)) { leftName = tgtName; rightName = srcName; }
            }
            const reasonsText = g.reasons.length > 0 ? `"${g.reasons.join(" / ")}"` : "";

            htmlContent += `
                <div style="margin-bottom: 6px; border-bottom: 1px solid var(--background-modifier-border); padding-bottom: 4px;">
                    <div style="display:flex; justify-content:center; align-items:center; gap: 8px;">
                        <strong>${leftName}</strong> 
                        ${arrowHtml}
                        <strong>${rightName}</strong>
                    </div>
                    <div style="margin-top:2px;">
                        <span style="color:${g.color}; font-size: 0.85em; font-weight:bold;">[${g.label}]</span>
                        <span style="font-style:italic; color:var(--text-accent); font-size: 0.9em; margin-left: 5px">${reasonsText}</span>
                    </div>
                </div>`;
        });
        infoPanel.innerHTML = htmlContent;
    }

    function highlightNode(d) {
        const filtered = activeFilters.size > 0;

        linkPaths
            .style("stroke-opacity", l => (filtered && !isLinkActive(l)) ? 0.02 : 0.08)
            .style("stroke-width", l => (filtered && !isLinkActive(l)) ? 1 : 2);

        labels.style("opacity", 0.3).style("font-weight", "normal").style("fill", "var(--text-normal)");
        centers.style("opacity", 0.3);

        const related = linkPaths
            .filter(l => (l.source === d || l.target === d) && (!filtered || isLinkActive(l)))
            .style("stroke-opacity", 1).style("stroke-width", 3).raise();

        const neighbors = new Set([d]);
        related.each(l => { neighbors.add(l.source); neighbors.add(l.target); });

        labels.filter(n => neighbors.has(n))
            .style("opacity", 1).style("font-weight", "bold").style("fill", "var(--text-normal)");

        centers.filter(n => neighbors.has(n)).style("opacity", 1);

        labels.filter(n => n === d)
            .style("fill", "#ffda79") 
            .style("opacity", 1)
            .style("font-weight", "bold");

        infoPanel.innerHTML = `
            <strong style="font-size:1.1em; display:block; margin-bottom: 2px;">${d.data.name}</strong>
            <hr style="margin:5px 0; border-color:var(--background-modifier-border); width: 50%">
            <div style="font-style:italic; color:var(--text-muted)">${d.data.desc}</div>
        `;
    }

    function resetHighlight() {
        renderBaseState();
    }

    function openLink(d) {
         if (!d.data.path) return;
         dv.app.workspace.openLinkText(d.data.path, sourceFolder, false);
    }

} catch (e) {
    dv.paragraph("❌ Ошибка: " + e.message);
}
```
