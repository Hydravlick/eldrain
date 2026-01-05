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
    const width = 700;
    const radius = width / 2;
    const innerRadius = radius - 140; // Больше места для текста
    const bundleTension = 0.85; // 0.1 - прямые линии, 1.0 - сильно стянутые
    
    // Путь к файлу для ссылок
    const sourceFilePath = "00_Variables/Registry_Combos.md";

    // ЦВЕТА (Яркие для темной темы)
    const colorMap = {
        "synergy": "#00ff9d", // Неоновый зеленый (Хорош с)
        "counter": "#ff4757", // Яркий красный (Контрит)
        "bad": "#2ed573",     // (Ошибочно был синим, поправим) -> #ffa502 (Оранжевый для 'bad' или синий #1e90ff)
        // Давайте сделаем логичнее:
        // Synergy = Зеленый, Counter = Красный, Bad = Синий (Слабость)
        "bad": "#1e90ff",
        "default": "#555"
    };

    // === 3. ПОЛУЧЕНИЕ ДАННЫХ ===
    const page = dv.page(sourceFilePath);
    if (!page) throw new Error("Файл не найден: " + sourceFilePath);

    const content = await dv.io.load(page.file.path);
    
    // Регулярки
    const regexBlock = /^##\s+(.+?)$([\s\S]+?)(?=^##\s+|\z)/gm;
    const blocks = [...content.matchAll(regexBlock)];

    const getField = (text, key) => {
        const m = text.match(new RegExp(`\\[${key}::\\s*([^\\]]+)\\]`));
        return m ? m[1].trim().toLowerCase() : null;
    };
    
    const getRel = (text, type) => {
        const re = new RegExp(`\\[rel_${type}::\\s*([^\\]]+)\\]`, 'g');
        return [...text.matchAll(re)].map(m => m[1].trim().toLowerCase());
    };

    const nodes = [];

    blocks.forEach(m => {
        // Очистка имени от скобок для красивого вывода
        const fullName = m[1].trim(); 
        const displayName = fullName.split('(')[0].trim(); 
        
        const body = m[2];
        const id = getField(body, "id");
        // Если ID нет, пропускаем или генерируем
        if (!id) return; 

        const race = getField(body, "req_race") || "unknown"; 

        nodes.push({
            id: id,
            name: displayName,
            fullName: fullName, // Нужно для ссылки на заголовок
            group: race,
            synergies: getRel(body, "synergy"),
            counters: getRel(body, "counter"),
            bads: getRel(body, "bad")
        });
    });

    // === 4. ПОДГОТОВКА ИЕРАРХИИ D3 ===
    const groups = d3.group(nodes, d => d.group);
    const hierarchyData = {
        name: "root",
        children: Array.from(groups, ([key, value]) => ({ name: key, children: value }))
    };

    const root = d3.hierarchy(hierarchyData)
        .sort((a, b) => d3.ascending(a.data.group, b.data.group) || d3.ascending(a.data.name, b.data.name));

    const cluster = d3.cluster().size([360, innerRadius]);
    cluster(root);

    // Карта узлов
    const nodeMap = new Map(root.leaves().map(d => [d.data.id, d]));

    // Формирование линий
    const graphLinks = [];
    nodes.forEach(srcData => {
        const sourceNode = nodeMap.get(srcData.id);
        if (!sourceNode) return;

        const addLinks = (targets, type) => {
            targets.forEach(targetId => {
                const targetNode = nodeMap.get(targetId);
                if (targetNode) {
                    graphLinks.push({
                        source: sourceNode,
                        target: targetNode,
                        type: type,
                        path: sourceNode.path(targetNode)
                    });
                }
            });
        };

        addLinks(srcData.synergies, "synergy");
        addLinks(srcData.counters, "counter");
        addLinks(srcData.bads, "bad");
    });

    // === 5. РЕНДЕРИНГ ===
    dv.container.innerHTML = "";
    const svg = d3.select(dv.container).append("svg")
        .attr("viewBox", [-width/2, -width/2, width, width])
        .style("font-family", "var(--font-interface)")
        .style("background", "transparent");

    // Генератор радиальных линий
    const line = d3.lineRadial()
        .curve(d3.curveBundle.beta(bundleTension))
        .radius(d => d.y)
        .angle(d => d.x / 180 * Math.PI);

    // Рисуем связи
    const linkPaths = svg.append("g")
        .selectAll("path")
        .data(graphLinks)
        .join("path")
        .attr("d", d => line(d.path))
        .style("fill", "none")
        .style("stroke", d => colorMap[d.type] || colorMap.default)
        .style("stroke-width", 1.5)
        .style("stroke-opacity", 0.6)
        // ВАЖНО: Screen делает линии светящимися на темном фоне
        .style("mix-blend-mode", "screen"); 

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
        .style("transition", "fill 0.2s")
        
        // === ИНТЕРАКТИВНОСТЬ: ХОВЕР ===
        .on("mouseover", function(event, d) {
            // Затемняем все линии
            linkPaths.style("stroke-opacity", 0.1);
            
            // Подсвечиваем активные (входящие и исходящие)
            linkPaths.filter(l => l.source === d || l.target === d)
                .style("stroke-opacity", 1)
                .style("stroke-width", 3)
                .raise(); // Поднимаем на передний план

            d3.select(this)
                .style("fill", "#ffda79") // Желтый при наведении
                .style("font-weight", "bold");
        })
        .on("mouseout", function(event, d) {
            // Возвращаем как было
            linkPaths.style("stroke-opacity", 0.6).style("stroke-width", 1.5);
            d3.select(this)
                .style("fill", "var(--text-normal)")
                .style("font-weight", "normal");
        })
        
        // === ИНТЕРАКТИВНОСТЬ: КЛИК (ПЕРЕХОД) ===
        .on("click", (event, d) => {
            // Открываем заметку на нужном заголовке
            // Формат: "Path/To/File.md#Header Name"
            const link = `${sourceFilePath}#${d.data.fullName}`;
            dv.app.workspace.openLinkText(link, sourceFilePath, false);
        });

} catch (e) {
    dv.paragraph("❌ **Ошибка:** " + e.message);
}