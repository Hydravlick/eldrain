---
type: matrix
status: active
system: player_entities_matrix
tags: [dataview, matrix]
---

```dataviewjs
// --- НАСТРОЙКИ ПУТЕЙ ---
const files = {
    races: "04_Player_Entities/_Registries/Registry_Races.md",
    specs: "04_Player_Entities/_Registries/Registry_Specs.md",
    combos: "04_Player_Entities/_Registries/Registry_Combos.md",
    weapons: "05_Combat_Survival/Registry_Weapons.md",
    modules: "07_Gear_Inventory/_Registries/Registry_Thermos_Modules.md",
    attributes: "04_Player_Entities/Attributes_TOUCH.md",
    // registry: удален, так как больше не нужен
};

// --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---

async function getAttributesInfo(path) {
    const page = dv.page(path);
    if (!page) throw new Error(`Attributes source not found: ${path}`);

    const schema = Array.from(page.touch_schema ?? []);
    if (schema.length !== 5) throw new Error("touch_schema must contain exactly five attributes");

    return schema.map((item, index) => ({
        key: String(item.key),
        header: `${index + 2}. ${item.key} - ${item.label}`
    }));
}

function getBaseStat(page) {
    const value = Number(page.base_attribute);
    if (!Number.isFinite(value)) throw new Error("base_attribute is missing");
    return value;
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
    const regex = /\[arsenal_type::\s*([\w\s,]+)\]/g; 
    const matches = [...text.matchAll(regex)];
    let types = [];
    matches.forEach(m => {
        types = types.concat(m[1].split(',').map(t => t.trim()));
    });
    return [...new Set(types)];
}

function parseArsenalEntries(text) {
    const regex = /\[arsenal_type::\s*([^\]]+)\][^\n]*?\[prof::\s*([^\]]+)\]/g;
    return [...text.matchAll(regex)].map(m => ({
        type: m[1].trim(),
        prof: parseInt(m[2].trim()) || 0
    }));
}

function parseNamedNumbers(text, key) {
    const value = parseInlineValue(text, key);
    if (!value) return {};
    const result = {};
    const regex = /([a-z_]+)\s+([+-]?\d+)/gi;
    let match;
    while ((match = regex.exec(value)) !== null) {
        result[match[1].toLowerCase()] = parseInt(match[2]);
    }
    return result;
}

function parseType(text) {
    const regex = /\[(?:weapon_type|armor_type)::\s*(\w+)\]/;
    const match = text.match(regex);
    return match ? match[1] : null;
}

function parseInlineValue(text, key) {
    const regex = new RegExp(`\\[${key}::\\s*([^\\]]+)\\]`);
    const match = text.match(regex);
    return match ? match[1].trim() : null;
}

function parseInlineList(text, key) {
    const value = parseInlineValue(text, key);
    if (!value) return [];
    return value.split(",").map(v => v.trim()).filter(Boolean);
}

function getCommonWeakness(leftWeaknesses, rightWeaknesses) {
    const right = new Set(rightWeaknesses);
    return leftWeaknesses.filter(v => right.has(v));
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
        const header = lines[0].trim();
        const body = lines.slice(1).join("\n");

        if (/template|шаблон|нулевой пациент/i.test(header)) return null;
        
        let tempName = header.split(" [")[0];
        const displayName = tempName.replace(/\s*\(.*?\)/g, "").trim();

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
            data.baseVector = parseInlineValue(body, "base_vector");
            data.weakTo = parseInlineList(body, "weak_to");
        }
        
        if (type === 'combos') {
            data.req_race = parseId(body, "req_race");
            data.req_spec = parseId(body, "req_spec");
            data.arsenal = parseArsenalEntries(body);
            data.allowedTypes = data.arsenal.length > 0
                ? [...new Set(data.arsenal.map(a => a.type))]
                : parseRequiredTypes(body);
            data.moduleCapacity = parseNamedNumbers(body, "module_capacity");
        }

        if (type === 'weapons') {
            data.itemType = parseType(body);
        }

        if (type === 'modules') {
            data.moduleCost = parseNamedNumbers(body, "module_cost");
        }

        return data;
    }).filter(Boolean);
}

// --- ОСНОВНАЯ ЛОГИКА ---

try {
const attributesPage = dv.page(files.attributes);
if (!attributesPage) throw new Error(`Attributes source not found: ${files.attributes}`);

// 1. Получаем ключи атрибутов
const attrsInfo = await getAttributesInfo(files.attributes);
const attrKeys = attrsInfo.map(a => a.key);

// 2. Получаем базовое значение из структурированного источника Attributes_TOUCH
const globalBaseStat = getBaseStat(attributesPage);

// 3. Парсим файлы контента
const races = await parseFile(files.races, 'races', attrKeys, /^## /m);
const specs = await parseFile(files.specs, 'specs', attrKeys, /^## /m);
const combos = await parseFile(files.combos, 'combos', [], /^## /m);

const weapons = await parseFile(files.weapons, 'weapons', [], /^### /m);
const modules = await parseFile(files.modules, 'modules', [], /^### /m);

// 4. Генерация таблицы
for (const race of races) {
    
    dv.header(2, race.link);
    
    let tableRows = [];

    for (const spec of specs) {
        let statsStr = "";
        for (const attr of attrsInfo) {
            const key = attr.key;
            // Используем полученное из таблицы значение
            const val = globalBaseStat + (race.stats[key] || 0) + (spec.stats[key] || 0);
            const label = attr.header ? `[[${files.attributes}#${attr.header}|${key}]]` : `**${key}**`;
            statsStr += `${label}: **${val}** <br>`;
        }
        statsStr = statsStr.slice(0, -4);

        const combo = combos.find(c => c.req_race === race.id && c.req_spec === spec.id);
        
        let archetypeLink = "";
        let abilitiesStr = "";
        let weaponStr = "";
        let armorStr = "";
        const commonWeakness = getCommonWeakness(race.weakTo || [], spec.weakTo || []);
        const comboPrimary = race.baseVector;
        const comboSecondary = spec.baseVector;
        const comboWeakness = commonWeakness.join(", ");
        const abilityModel = comboPrimary && comboSecondary && comboPrimary === comboSecondary
            ? "mono_vector_fusion"
            : "race_spec_fusion";
        const arsenalGateStr = combo?.arsenal?.length
            ? combo.arsenal.map(a => `${a.type}: T${a.prof}${a.prof >= 3 ? " (vector on)" : ""}`).join("<br>")
            : "*(нет данных)*";
        const moduleCapacityStr = combo && Object.keys(combo.moduleCapacity || {}).length
            ? Object.entries(combo.moduleCapacity).map(([k, v]) => `${k}: ${v}`).join("<br>")
            : "*(нет данных)*";
        const vectorStr = [
            comboPrimary ? `Primary: **${comboPrimary}**` : "Primary: *(нет)*",
            comboSecondary ? `Secondary: **${comboSecondary}**` : "Secondary: *(нет)*",
            comboWeakness
                ? `Shared weakness: **${comboWeakness}**`
                : "Общая слабость: *(не найдена)*"
            ,
            `Model: ${abilityModel}`,
            "Source: Registry_Races + Registry_Specs",
            `Arsenal gates:<br>${arsenalGateStr}`,
            `Module capacity:<br>${moduleCapacityStr}`
        ].join("<br>");

        if (combo) {
            archetypeLink = `**[[${files.combos}#${combo.name}|${combo.displayName}]]**<br>*(Мутация)*`;
            abilitiesStr = parseAbilities(combo.body, files.combos, combo.name) || "*(Нет навыков)*";
            
            const validWeapons = weapons
                .filter(w => combo.allowedTypes.includes(w.itemType))
                .sort((a, b) => a.tier - b.tier);
            
            const validModules = modules
                .filter(m => {
                    const costs = Object.entries(m.moduleCost || {});
                    return costs.length > 0 && costs.every(([family, cost]) => (combo.moduleCapacity?.[family] || 0) >= cost);
                })
                .sort((a, b) => a.tier - b.tier);
            
            weaponStr = validWeapons.length > 0 
                ? validWeapons.map(w => w.link).join("<br>") 
                : "*(Нет)*";

            armorStr = validModules.length > 0 
                ? validModules.map(a => a.link).join("<br>") 
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
            vectorStr,
            statsStr,
            abilitiesStr,
            weaponStr,
            armorStr
        ]);
    }

    dv.table(
        ["Архетип", "Специализация", "Двойной Парадокс", "Атрибуты", "Способности", "Оружие", "Потенциальные модули"],
        tableRows
    );
    
    dv.paragraph("---");
}
} catch (error) {
    dv.paragraph(`⚠️ Character Matrix: ${error.message}`);
}
```
