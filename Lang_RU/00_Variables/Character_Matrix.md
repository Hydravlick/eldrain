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

// 1. Обновлено: Получаем и ключ, и заголовок для ссылок
async function getAttributesInfo(path) {
    const page = dv.page(path);
    // Если файла нет, возвращаем дефолтный список без заголовков (ссылки не будут работать, но код не упадет)
    if (!page) return ["PHY", "AGI", "VIG", "TEC", "RES"].map(k => ({ key: k, header: null }));
    
    const content = await dv.io.load(page.file.path);
    
    // Ищем строки заголовков: ## 1. СИЛА (PHY - Physique)
    // Группа 1: Полный текст заголовка (для ссылки)
    // Группа 2: Ключ из скобок (PHY)
    const regex = /^##\s+(.*?\(([A-Z]{3,4})[\s-).].*?)$/gm;
    
    const items = [];
    let match;
    while ((match = regex.exec(content)) !== null) {
        items.push({
            header: match[1].trim(), // "1. СИЛА (PHY - Physique)"
            key: match[2]            // "PHY"
        });
    }
    return items.length > 0 ? items : ["PHY", "AGI", "VIG", "TEC", "RES"].map(k => ({ key: k, header: null }));
}

// Парсинг атрибутов (принимает массив ключей)
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

function parseAbilities(text, filePath, headerName) {
    const regex = /-\s*\*\*(?:.*?)\s*\(([PQE])\):\*\*\s*\*\*(.*?)\*\*/g;
    const matches = [...text.matchAll(regex)];
    
    if (matches.length === 0) return null;

    return matches.map(m => {
        const key = m[1];      
        let name = m[2].trim();
        if (name.endsWith(".")) name = name.slice(0, -1);
        return `[[${filePath}#${headerName}|(${key}) ${name}]]`;
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
            link: `[[${path}#${header}|${displayName}]]`,
            id: parseId(body, "id"),
            body: body
        };

        if (type === 'races' || type === 'specs') {
            data.stats = parseStats(body, attrKeys);
        }
        
        if (type === 'combos' || type === 'items') {
            data.req_race = parseId(body, "req_race");
            data.req_spec = parseId(body, "req_spec");
        }

        return data;
    });
}

// --- ОСНОВНАЯ ЛОГИКА ---

// 1. Получаем объекты атрибутов { key, header }
const attrsInfo = await getAttributesInfo(files.attributes);
// Вытаскиваем просто список ключей ['PHY', 'AGI'...] для парсера
const attrKeys = attrsInfo.map(a => a.key);

const races = await parseFile(files.races, 'races', attrKeys);
const specs = await parseFile(files.specs, 'specs', attrKeys);
const combos = await parseFile(files.combos, 'combos');
const items = await parseFile(files.items, 'items');

let tableRows = [];

for (let i = 0; i < races.length; i++) {
    const race = races[i];
    
    if (i > 0) {
        tableRows.push(["---", "---", "---", "---", "---"]);
    }

    for (const spec of specs) {
        // 1. СТАТЫ
        let statsStr = "";

        // Проходимся по списку объектов (чтобы был доступ к header)
	    for (const attr of attrsInfo) {
            const key = attr.key;
	        const val = 10 + (race.stats[key] || 0) + (spec.stats[key] || 0);
            
            // Формируем ссылку: [[Attributes_System.md#Полный Заголовок|КЛЮЧ]]
            // Если заголовок не найден (файл удален), просто пишем жирный текст
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
            abilitiesStr = parseAbilities(combo.body, files.combos, combo.name) || "*(Нет данных)*";
        } else {
            archetypeLink = `${spec.link}<br>*(Стандарт)*`;
            const specAbilities = parseAbilities(spec.body, files.specs, spec.name);
            const racePassiveMatch = race.body.match(/\*\*Пассивный навык:\*\*\s*\*\*(.*?)\*\*/);
            const racePassive = racePassiveMatch 
                ? `[[${files.races}#${race.name}|(P) ${racePassiveMatch[1]}]]` 
                : "";
            
            abilitiesStr = racePassive;
            if (specAbilities) abilitiesStr += "<br>" + specAbilities;
        }

        // 3. АРСЕНАЛ
        const validItems = items.filter(item => {
            const raceMatch = item.req_race === 'any' || item.req_race === race.id;
            const specMatch = item.req_spec === 'any' || item.req_spec === spec.id;
            return raceMatch && specMatch;
        });
        
        const itemsList = validItems.length > 0 
            ? validItems.map(i => `• ${i.link}`).join("<br>") 
            : "*Нет подходящего*";

        tableRows.push([
            `**${race.link}**<br>+<br>**${spec.link}**`,
            archetypeLink,
            statsStr,
            abilitiesStr,
            itemsList
        ]);
    }
}

dv.header(2, "Матрица Классов и Рас (Linked Attributes)");
dv.table(
    ["Связка", "Архетип", "Атрибуты", "Способности", "Арсенал"],
    tableRows
);