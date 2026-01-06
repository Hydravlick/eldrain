```dataviewjs
// --- НАСТРОЙКИ ПУТЕЙ ---
const files = {
    races: "Lang_RU/00_Variables/Registry_Races.md",
    specs: "Lang_RU/00_Variables/Registry_Specs.md",
    combos: "Lang_RU/00_Variables/Registry_Combos.md",
    weapons: "Lang_RU/00_Variables/Registry_Weapon.md",
    armor: "Lang_RU/00_Variables/Registry_Armor.md",
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
    const regex = /\[type::\s*(\w+)\]/g;
    const matches = [...text.matchAll(regex)];
    return [...new Set(matches.map(m => m[1]))];
}

function parseType(text) {
    const regex = /\[type::\s*(\w+)\]/;
    const match = text.match(regex);
    return match ? match[1] : null;
}

// Новая функция: парсинг тира из заголовка вида "(T2) Название"
function parseTier(header) {
    const match = header.match(/\(T(\d+)\)/);
    return match ? parseInt(match[1]) : 0; // Если тир не указан, считаем T0
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
            link: `[[${path}#${header}|${displayName}]]`, // Ссылка без иконки
            id: parseId(body, "id"),
            body: body,
            tier: parseTier(header) // Сохраняем тир
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

const races = await parseFile(files.races, 'races', attrKeys);
const specs = await parseFile(files.specs, 'specs', attrKeys);
const combos = await parseFile(files.combos, 'combos');
const weapons = await parseFile(files.weapons, 'weapons');
const armor = await parseFile(files.armor, 'armor');

for (const race of races) {
    
    dv.header(2, race.link);
    
    let tableRows = [];

    for (const spec of specs) {
        // СТАТЫ
        let statsStr = "";
        for (const attr of attrsInfo) {
            const key = attr.key;
            const val = 10 + (race.stats[key] || 0) + (spec.stats[key] || 0);
            const label = attr.header ? `[[${files.attributes}#${attr.header}|${key}]]` : `**${key}**`;
            statsStr += `${label}: **${val}** <br>`;
        }
        statsStr = statsStr.slice(0, -4);

        // МУТАЦИЯ / АРХЕТИП
        const combo = combos.find(c => c.req_race === race.id && c.req_spec === spec.id);
        
        let archetypeLink = "";
        let abilitiesStr = "";
        let weaponStr = "";
        let armorStr = "";

        if (combo) {
            archetypeLink = `**[[${files.combos}#${combo.name}|${combo.displayName}]]**<br>*(Мутация)*`;
            abilitiesStr = parseAbilities(combo.body, files.combos, combo.name) || "*(Нет навыков)*";
            
            // Фильтрация и Сортировка (T0 -> T3)
            const validWeapons = weapons
                .filter(w => combo.allowedTypes.includes(w.itemType))
                .sort((a, b) => a.tier - b.tier); // Сортировка по тиру
            
            const validArmor = armor
                .filter(a => combo.allowedTypes.includes(a.itemType))
                .sort((a, b) => a.tier - b.tier); // Сортировка по тиру
            
            // Формирование строк (без иконок)
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
            weaponStr, // Отдельная колонка Оружие
            armorStr   // Отдельная колонка Броня
        ]);
    }

    dv.table(
        ["Архетип", "Специализация", "Атрибуты", "Способности", "Оружие", "Броня"],
        tableRows
    );
    
    dv.paragraph("---");
}
```