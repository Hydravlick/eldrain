```dataviewjs
// --- НАСТРОЙКИ ПУТЕЙ ---
const files = {
    races: "00_Variables/Registry_Races.md",
    specs: "00_Variables/Registry_Specs.md",
    combos: "00_Variables/Registry_Combos.md",
    items: "00_Variables/Registry_Items.md",
    attributes: "Attributes_System.md"
};

// --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---

async function getAttributesInfo(path) {
    const page = dv.page(path);
    if (!page) return ["PHY", "AGI", "VIG", "TEC", "RES"].map(k => ({ key: k, header: null }));
    
    const content = await dv.io.load(page.file.path);
    const regex = /^##\s+(.*?\(([A-Z]{3,4})[\s-).].*?)$/gm;
    
    const items = [];
    let match;
    while ((match = regex.exec(content)) !== null) {
        items.push({
            header: match[1].trim(),
            key: match[2]
        });
    }
    return items.length > 0 ? items : ["PHY", "AGI", "VIG", "TEC", "RES"].map(k => ({ key: k, header: null }));
}

function parseStats(text, validKeys) {
    const stats = {};
    validKeys.forEach(key => stats[key] = 0);
    const keysPattern = validKeys.join("|");
    const regex = new RegExp(`\\[(${keysPattern})::\\s*([+-]?\\d+)\\]`, "g");
    let match;
    while ((match = regex.exec(text)) !== null) {
        stats[match[1]] = parseInt(match[2]);
    }
    return stats;
}

function parseMultiId(text, key) {
    const regex = new RegExp(`\\[${key}::\\s*(\\w+)\\]`, "g");
    const matches = [...text.matchAll(regex)];
    if (matches.length === 0) return [];
    return matches.map(m => m[1].toLowerCase());
}

function parseId(text, key = "id") {
    const regex = new RegExp(`\\[${key}::\\s*(\\w+)\\]`);
    const match = text.match(regex);
    return match ? match[1].toLowerCase() : null;
}

function parseAbilities(text, filePath, headerName) {
    const regex = /^####\s+(.*?\(([PQE])\):\s*(.*?))$/gm;
    const matches = [...text.matchAll(regex)];
    
    if (matches.length === 0) return null;

    return matches.map(m => {
        const fullHeader = m[1].trim(); 
        const key = m[2];
        let name = m[3].trim();
        name = name.replace(/`/g, "");
        
        return `[[${filePath}#${fullHeader}|(${key}) ${name}]]`;
    }).join("<br>");
}

async function parseFile(path, type, attrKeys = []) {
    const file = dv.page(path);
    if (!file) return [];
    
    const content = await dv.io.load(file.file.path);
    const blocks = content.split(/^## /m).slice(1); 
    
    return blocks.map(block => {
        const lines = block.split("\n");
        const header = lines[0].trim();
        const body = lines.slice(1).join("\n");
        const displayName = header.split(" (")[0];

        const data = {
            name: header,
            displayName: displayName,
            // Ссылка формируется здесь
            link: `[[${path}#${header}|${displayName}]]`,
            id: parseId(body, "id"),
            body: body
        };

        if (type === 'races' || type === 'specs') {
            data.stats = parseStats(body, attrKeys);
        }
        
        if (type === 'combos') {
            data.req_race = parseId(body, "req_race");
            data.req_spec = parseId(body, "req_spec");
        }

        if (type === 'items') {
            data.req_races = parseMultiId(body, "req_race");
            data.req_specs = parseMultiId(body, "req_spec");
        }

        return data;
    });
}

// --- ОСНОВНАЯ ЛОГИКА ---

const attrsInfo = await getAttributesInfo(files.attributes);
const attrKeys = attrsInfo.map(a => a.key);

const races = await parseFile(files.races, 'races', attrKeys);
const specs = await parseFile(files.specs, 'specs', attrKeys);
const combos = await parseFile(files.combos, 'combos');
const items = await parseFile(files.items, 'items');

// Главный цикл по РАСАМ
for (const race of races) {
    
    // ИЗМЕНЕНИЕ 1: Ссылка на заголовок расы
    dv.header(2, race.link);
    
    let tableRows = [];

    for (const spec of specs) {
        // 1. СТАТЫ
        let statsStr = "";
        for (const attr of attrsInfo) {
            const key = attr.key;
            const val = 10 + (race.stats[key] || 0) + (spec.stats[key] || 0);
            const label = attr.header 
                ? `[[${files.attributes}#${attr.header}|${key}]]`
                : `**${key}**`;
            statsStr += `${label}: **${val}** <br>`;
        }
        statsStr = statsStr.slice(0, -4);

        // 2. БИЛД / МУТАЦИЯ
        const combo = combos.find(c => c.req_race === race.id && c.req_spec === spec.id);
        
        let archetypeLink = "";
        let abilitiesStr = "";

        if (combo) {
            archetypeLink = `**[[${files.combos}#${combo.name}|${combo.displayName}]]**<br>*(Мутация)*`;
            abilitiesStr = parseAbilities(combo.body, files.combos, combo.name) || "*(Нет навыков)*";
        } else {
            archetypeLink = `${spec.link}<br>*(Стандарт)*`;
            const specAbilities = parseAbilities(spec.body, files.specs, spec.name);
            const raceAbilities = parseAbilities(race.body, files.races, race.name);
            
            abilitiesStr = "";
            if (raceAbilities) abilitiesStr += raceAbilities + "<br>";
            if (specAbilities) abilitiesStr += specAbilities;
            if (!abilitiesStr) abilitiesStr = "*(Нет данных)*";
        }

        // 3. АРСЕНАЛ
        const validItems = items.filter(item => {
            const raceMatch = item.req_races.length === 0 || item.req_races.includes('any') || item.req_races.includes(race.id);
            const specMatch = item.req_specs.length === 0 || item.req_specs.includes('any') || item.req_specs.includes(spec.id);
            return raceMatch && specMatch;
        });
        
        const itemsList = validItems.length > 0 
            ? validItems.map(i => `• ${i.link}`).join("<br>") 
            : "*Нет подходящего*";

        tableRows.push([
            // ИЗМЕНЕНИЕ 2: Ссылка на специализацию в первой колонке
            spec.link,
            archetypeLink,
            statsStr,
            abilitiesStr,
            itemsList
        ]);
    }

    dv.table(
        ["Архетип", "Специализация", "Атрибуты", "Способности", "Арсенал"],
        tableRows
    );
    
    dv.paragraph("---");
}
```