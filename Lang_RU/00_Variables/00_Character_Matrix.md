```dataviewjs
// --- НАСТРОЙКИ ПУТЕЙ ---
const files = {
    races: "Lang_RU/00_Variables/Registry_Races.md",
    specs: "Lang_RU/00_Variables/Registry_Specs.md",
    combos: "Lang_RU/00_Variables/Registry_Combos.md",
    weapons: "Lang_RU/00_Variables/Registry_Weapons.md",
    armor: "Lang_RU/00_Variables/Registry_Armors.md",
    attributes: "Lang_RU/00_Variables/Attributes_System.md"
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
        items.push({ header: match[1].trim(), key: match[2] });
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

function parseId(text, key = "id") {
    const regex = new RegExp(`\\[${key}::\\s*(\\w+)\\]`);
    const match = text.match(regex);
    return match ? match[1].toLowerCase() : null;
}

function parseRequiredTypes(text) {
    const regex = /\[type::\s*([\w\s,]+)\]/g; 
    const matches = [...text.matchAll(regex)];
    let types = [];
    matches.forEach(m => {
        types = types.concat(m[1].split(',').map(t => t.trim()));
    });
    return [...new Set(types)];
}

function parseType(text) {
    const regex = /\[type::\s*(\w+)\]/;
    const match = text.match(regex);
    return match ? match[1] : null;
}

function parseTier(header, body) {
    const headMatch = header.match(/\(T(\d+)\)/);
    if (headMatch) return parseInt(headMatch[1]);

    const bodyMatch = body.match(/\[tier::\s*(\d+)\]/);
    if (bodyMatch) return parseInt(bodyMatch[1]);

    return 0;
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

async function parseFile(path, type, attrKeys = [], splitRegex = /^## /m) {
    const file = dv.page(path);
    if (!file) return [];
    
    const content = await dv.io.load(file.file.path);
    const blocks = content.split(splitRegex).slice(1); 
    
    return blocks.map(block => {
        const lines = block.split("\n");
        const header = lines[0].trim(); // Например: "Боевой Нож (Combat Shiv) [1H]"
        const body = lines.slice(1).join("\n");
        
        // --- ИЗМЕНЕНИЯ ЗДЕСЬ ---
        // 1. Отсекаем [теги] в конце (например [1H])
        let tempName = header.split(" [")[0];
        // 2. Заменяем всё в круглых скобках (Combat Shiv) на пустоту
        const displayName = tempName.replace(/\s*\(.*?\)/g, "").trim();
        // -----------------------

        const data = {
            name: header,
            displayName: displayName,
            link: `[[${path}#${header}|${displayName}]]`,
            id: parseId(body, "id"),
            body: body,
            tier: parseTier(header, body)
        };

        if (type === 'races' || type === 'specs') {
            data.stats = parseStats(body, attrKeys);
        }
        
        if (type === 'combos') {
            data.req_race = parseId(body, "req_race");
            data.req_spec = parseId(body, "req_spec");
            data.allowedTypes = parseRequiredTypes(body);
        }

        if (type === 'weapons' || type === 'armor') {
            data.itemType = parseType(body);
        }

        return data;
    });
}

// --- ОСНОВНАЯ ЛОГИКА ---

const attrsInfo = await getAttributesInfo(files.attributes);
const attrKeys = attrsInfo.map(a => a.key);

const races = await parseFile(files.races, 'races', attrKeys, /^## /m);
const specs = await parseFile(files.specs, 'specs', attrKeys, /^## /m);
const combos = await parseFile(files.combos, 'combos', [], /^## /m);

const weapons = await parseFile(files.weapons, 'weapons', [], /^### /m);
const armor = await parseFile(files.armor, 'armor', [], /^### /m);

for (const race of races) {
    
    dv.header(2, race.link);
    
    let tableRows = [];

    for (const spec of specs) {
        let statsStr = "";
        for (const attr of attrsInfo) {
            const key = attr.key;
            const val = 10 + (race.stats[key] || 0) + (spec.stats[key] || 0);
            const label = attr.header ? `[[${files.attributes}#${attr.header}|${key}]]` : `**${key}**`;
            statsStr += `${label}: **${val}** <br>`;
        }
        statsStr = statsStr.slice(0, -4);

        const combo = combos.find(c => c.req_race === race.id && c.req_spec === spec.id);
        
        let archetypeLink = "";
        let abilitiesStr = "";
        let weaponStr = "";
        let armorStr = "";

        if (combo) {
            archetypeLink = `**[[${files.combos}#${combo.name}|${combo.displayName}]]**<br>*(Мутация)*`;
            abilitiesStr = parseAbilities(combo.body, files.combos, combo.name) || "*(Нет навыков)*";
            
            const validWeapons = weapons
                .filter(w => combo.allowedTypes.includes(w.itemType))
                .sort((a, b) => a.tier - b.tier);
            
            const validArmor = armor
                .filter(a => combo.allowedTypes.includes(a.itemType))
                .sort((a, b) => a.tier - b.tier);
            
            weaponStr = validWeapons.length > 0 
                ? validWeapons.map(w => w.link).join("<br>") 
                : "*(Нет)*";

            armorStr = validArmor.length > 0 
                ? validArmor.map(a => a.link).join("<br>") 
                : "*(Нет)*";

        } else {
            archetypeLink = `${spec.link}<br>*(Стандарт)*`;
            const specAbilities = parseAbilities(spec.body, files.specs, spec.name);
            const raceAbilities = parseAbilities(race.body, files.races, race.name);
            
            abilitiesStr = (raceAbilities ? raceAbilities + "<br>" : "") + (specAbilities || "");
            if (!abilitiesStr) abilitiesStr = "*(Нет данных)*";
            
            weaponStr = "*(Нет данных)*";
            armorStr = "*(Нет данных)*";
        }

        tableRows.push([
            spec.link,
            archetypeLink,
            statsStr,
            abilitiesStr,
            weaponStr,
            armorStr
        ]);
    }

    dv.table(
        ["Архетип", "Специализация", "Атрибуты", "Способности", "Оружие", "Броня"],
        tableRows
    );
    
    dv.paragraph("---");
}
```