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
    const width = 600; 
    const radius = width / 2;
    const innerRadius = radius - 140; 
    const bundleTension = 0.85; 
    
    const sourceFilePath = "Registry_Combos.md"; 

    const colorMap = {
        "synergy": "#00ff9d", 
        "counter": "#ff4757", 
        "default": "#555"
    };
    
    const labelMap = {
        "synergy": "Синергия (Buff)",
        "counter": "Контр-пик (Kill)"
    };

    // === 3. НАДЕЖНЫЙ ПАРСИНГ ДАННЫХ ===
    const page = dv.page(sourceFilePath);
    if (!page) throw new Error("Файл не найден: " + sourceFilePath);

    // Добавляем искусственный конец, чтобы Regex/Split не терял последний блок
    const rawContent = (await dv.io.load(page.file.path)) + "\n\n## END_MARKER";
    
    // Разбиваем текст по заголовкам ## (более надежно)
    const rawBlocks = rawContent.split(/^##\s+/m).slice(1); 

    const cleanID = (str) => str ? str.toLowerCase().trim() : null;
    
    const getRelDetails = (text, type) => {
        const re = new RegExp(`\\[rel_${type}::\\s*([^\\]]+)\\](?:\\s*\\(([^)]+)\\))?`, 'g');
        return [...text.matchAll(re)].map(m => {
            let idRaw = m[1].trim();
            // Если описание попало внутрь скобок ID
            if (idRaw.includes('(')) idRaw = idRaw.split('(')[0].trim();
            return {
                id: cleanID(idRaw),
                reason: m[2] ? m[2].trim() : null
            };
        });
    };

    const nodes = [];

    rawBlocks.forEach(blockText => {
        const lines = blockText.split('\n');
        const header = lines[0].trim();
        if (header === "END_MARKER") return; 

        const body = lines.slice(1).join('\n');
        
        // Ищем ID
        const idMatch = body.match(/\[id::\s*([^\]]+)\]/);
        if (!idMatch) return;

        const id = cleanID(idMatch[1]);
        const displayName = header.split('(')[0].trim();
        const raceMatch = body.match(/\[req_race::\s*([^\]]+)\]/);

        nodes.push({
            id: id,
            name: displayName,
            fullName: header,
            group: raceMatch ? raceMatch[1].trim() : "unknown",
            synergies: getRelDetails(body, "synergy"),
            counters: getRelDetails(body, "counter")
        });
    });

    // === 4. ПОДГОТОВКА ГРАФА ===
    const groups = d3.group(nodes, d => d.group);
    const root = d3.hierarchy({
        name: "root",
        children: Array.from(groups, ([key, value]) => ({ name: key, children: value }))
    })
    .sort((a, b) => d3.ascending(a.data.group, b.data.group) || d3.ascending(a.data.name, b.data.name));

    const cluster = d3.cluster().size([360, innerRadius]);
    cluster(root);

    const nodeMap = new Map(root.leaves().map(d => [d.data.id, d]));
    const graphLinks = [];
    const errors = [];

    nodes.forEach(srcData => {
        const sourceNode = nodeMap.get(srcData.id);
        if (!sourceNode) return;

        const addLinks = (targets, type) => {
            targets.forEach(t => {
                const targetNode = nodeMap.get(t.id);
                if (targetNode) {
                    graphLinks.push({
                        source: sourceNode,
                        target: targetNode,
                        type: type,
                        reason: t.reason,
                        path: sourceNode.path(targetNode)
                    });
                } else {
                    errors.push(`⚠️ <b>${srcData.name}</b> ссылается на <code>${t.id}</code>, но ID не найден.`);
                }
            });
        };

        addLinks(srcData.synergies, "synergy");
        addLinks(srcData.counters, "counter");
    });

    // === 5. HTML ОТРИСОВКА (С БЛОЧНЫМ ФОРМАТИРОВАНИЕМ) ===
    dv.container.innerHTML = "";
    const mainContainer = dv.container.createDiv({ cls: "bundle-container" });
    
    // 5.1 ВЕРХНИЙ БЛОК (ЛЕГЕНДА)
    const legendDiv = mainContainer.createDiv({ cls: "bundle-legend" });
    legendDiv.style.display = "flex";
    legendDiv.style.justifyContent = "center";
    legendDiv.style.gap = "20px";
    legendDiv.style.marginBottom = "10px";
    legendDiv.style.fontSize = "12px";
    legendDiv.style.padding = "5px";

    ["synergy", "counter"].forEach(type => {
        const item = legendDiv.createSpan();
        item.innerHTML = `<span style="display:inline-block; width:10px; height:10px; background:${colorMap[type]}; margin-right:5px; border-radius:2px;"></span>${labelMap[type]}`;
    });

    // 5.2 ГРАФИК
    const svgContainer = mainContainer.createDiv();
    const svg = d3.select(svgContainer).append("svg")
        .attr("viewBox", [-width/2, -width/2, width, width])
        .style("font-family", "var(--font-interface)")
        .style("background", "transparent")
        .style("max-width", "100%")
        .style("height", "auto");

    // 5.3 НИЖНИЙ БЛОК (ИНФО-ПАНЕЛЬ)
    const infoDiv = mainContainer.createDiv({ cls: "bundle-info" });
    infoDiv.style.minHeight = "40px";
    infoDiv.style.marginTop = "10px";
    infoDiv.style.padding = "10px";
    infoDiv.style.background = "var(--background-secondary)";
    infoDiv.style.border = "1px solid var(--background-modifier-border)";
    infoDiv.style.borderRadius = "5px";
    infoDiv.style.textAlign = "center";
    infoDiv.innerHTML = "<span style='color:var(--text-muted)'>Наведите на название или линию для деталей</span>";

    // 5.4 БЛОК ОШИБОК (Если есть битые ссылки)
    if(errors.length > 0) {
        const errDiv = mainContainer.createDiv();
        errDiv.style.marginTop = "15px";
        errDiv.style.padding = "10px";
        errDiv.style.border = "1px solid #ff4757";
        errDiv.style.borderRadius = "5px";
        errDiv.style.backgroundColor = "rgba(255, 71, 87, 0.05)";
        errDiv.style.fontSize = "0.9em";
        errDiv.innerHTML = `<strong style="color:#ff4757">Обнаружены проблемы со связями:</strong><br>${errors.join("<br>")}`;
    }

    // === 6. ЛОГИКА D3 ===
    const line = d3.lineRadial()
        .curve(d3.curveBundle.beta(bundleTension))
        .radius(d => d.y)
        .angle(d => d.x / 180 * Math.PI);

    // Рисуем линии
    const linkPaths = svg.append("g")
        .selectAll("path")
        .data(graphLinks)
        .join("path")
        .attr("d", d => line(d.path))
        .style("fill", "none")
        .style("stroke", d => colorMap[d.type])
        .style("stroke-width", 2)
        .style("stroke-opacity", 0.4)
        .style("mix-blend-mode", "screen")
        .style("cursor", "pointer");

    // Рисуем текст
    const labels = svg.append("g")
        .selectAll("g")
        .data(root.leaves())
        .join("g")
        .attr("transform", d => `rotate(${d.x - 90}) translate(${d.y + 8},0)`);

    labels.append("text")
        .attr("dy", "0.31em")
        .attr("x", d => d.x < 180 ? 0 : -6)
        .attr("text-anchor", d => d.x < 180 ? "start" : "end")
        .attr("transform", d => d.x >= 180 ? "rotate(180)" : null)
        .text(d => d.data.name)
        .style("fill", "var(--text-normal)")
        .style("font-size", "12px")
        .style("cursor", "pointer")
        
        // ХОВЕР НА ТЕКСТ
        .on("mouseover", function(event, d) {
            linkPaths.style("stroke-opacity", 0.05);
            const activeLinks = linkPaths.filter(l => l.source === d || l.target === d)
                .style("stroke-opacity", 1)
                .style("stroke-width", 3)
                .raise();

            d3.select(this).style("fill", "#ffda79").style("font-weight", "bold");
            infoDiv.innerHTML = `<strong>${d.data.name}</strong>: ${activeLinks.size()} активных связей`;
        })
        .on("mouseout", function() {
            linkPaths.style("stroke-opacity", 0.4).style("stroke-width", 2);
            d3.select(this).style("fill", "var(--text-normal)").style("font-weight", "normal");
            infoDiv.innerHTML = "<span style='color:var(--text-muted)'>Наведите на название или линию для деталей</span>";
        })
        .on("click", (event, d) => {
            const link = `${sourceFilePath}#${d.data.fullName}`;
            dv.app.workspace.openLinkText(link, sourceFilePath, false);
        });

    // ХОВЕР НА ЛИНИИ
    linkPaths
        .on("mouseover", function(event, d) {
            d3.select(this).style("stroke-opacity", 1).style("stroke-width", 4);
            const reason = d.reason ? `<br><em>"${d.reason}"</em>` : "";
            infoDiv.innerHTML = `
                <span style="color:${colorMap[d.type]}">● ${labelMap[d.type]}</span><br>
                <strong>${d.source.data.name}</strong> ➝ <strong>${d.target.data.name}</strong>
                ${reason}
            `;
        })
        .on("mouseout", function() {
            d3.select(this).style("stroke-opacity", 0.4).style("stroke-width", 2);
            infoDiv.innerHTML = "<span style='color:var(--text-muted)'>Наведите на название или линию для деталей</span>";
        });

} catch (e) {
    dv.paragraph("❌ **Ошибка скрипта:** " + e.message);
}
```