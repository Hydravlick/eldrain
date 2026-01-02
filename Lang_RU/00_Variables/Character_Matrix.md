```dataviewjs
// --- НАСТРОЙКИ ПУТЕЙ ---
const files = {
    races: "00_Variables/Registry_Races.md",
    specs: "00_Variables/Registry_Specs.md",
    combos: "00_Variables/Registry_Combos.md",
    items: "00_Variables/Registry_Items.md"
};

// --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---

// Парсинг атрибутов
function parseStats(text) {
    const stats = { PHY: 0, AGI: 0, VIG: 0, TEC: 0 };
    const regex = /\[(PHY|AGI|VIG|TEC)::\s*([+-]?\d+)\]/g;
    let match;
    while ((match = regex.exec(text)) !== null) {
        stats[match[1]] = parseInt(match[2]);
    }
    return stats;
}

// Парсинг ID
function parseId(text, key = "id") {
    const regex = new RegExp(`\\[${key}::\\s*(\\w+)\\]`);
    const match = text.match(regex);
    return match ? match[1].toLowerCase() : null;
}

// Извлечение способностей и создание ссылок на СЕКЦИЮ (Header), но с именем СПОСОБНОСТИ
function parseAbilities(text, filePath, headerName) {
    // Ищет строки: - **Тип (Ключ):** **Название**
    // Пример: - **Пассивка (P):** **Предчувствие**
    const regex = /-\s*\*\*(?:.*?)\s*\(([PQE])\):\*\*\s*\*\*(.*?)\*\*/g;
    const matches = [...text.matchAll(regex)];
    
    if (matches.length === 0) return null;

    return matches.map(m => {
        const key = m[1];       // P, Q или E
        let name = m[2].trim(); // Название (напр. Предчувствие)
        if (name.endsWith(".")) name = name.slice(0, -1);
        
        // Ссылка ведет на Файл#Заголовок, но отображается как "(P) Название"
        return `[[${filePath}#${headerName}|(${key}) ${name}]]`;
    }).join("<br>");
}

// Чтение файла
async function parseFile(path, type) {
    const file = dv.page(path);
    if (!file) return [];
    
    const content = await dv.io.load(file.file.path);
    const blocks = content.split(/^## /m).slice(1); 
    
    return blocks.map(block => {
        const lines = block.split("\n");
        const header = lines[0].trim();
        const body = lines.slice(1).join("\n");
        
        // Короткое имя (только русское, до скобки)
        const displayName = header.split(" (")[0];

        const data = {
            name: header, // Полный заголовок для ссылок
            displayName: displayName,
            // Ссылка с отображением короткого имени
            link: `[[${path}#${header}|${displayName}]]`,
            id: parseId(body, "id"),
            body: body
        };

        if (type === 'races' || type === 'specs') {
            data.stats = parseStats(body);
        }
        
        if (type === 'combos' || type === 'items') {
            data.req_race = parseId(body, "req_race");
            data.req_spec = parseId(body, "req_spec");
        }

        return data;
    });
}

// --- ОСНОВНАЯ ЛОГИКА ---

const races = await parseFile(files.races, 'races');
const specs = await parseFile(files.specs, 'specs');
const combos = await parseFile(files.combos, 'combos');
const items = await parseFile(files.items, 'items');

let tableRows = [];

for (let i = 0; i < races.length; i++) {
    const race = races[i];
    
    // Разделитель между расами
    if (i > 0) {
        tableRows.push(["---", "---", "---", "---", "---"]);
    }

    for (const spec of specs) {
        // 1. СТАТЫ
	    const totalStats = {};
	    // Добавил "RES", если он есть в твоей системе, или удали его из списка
	    for (const key of ["PHY", "AGI", "VIG", "TEC", "RES"]) {
	        // База 10 + Бонус Расы + Бонус Класса
	        const val = 10 + (race.stats[key] || 0) + (spec.stats[key] || 0);
	        
	        // Просто записываем число (12, 8, 15). Плюс тут уже не нужен.
	        totalStats[key] = val;
	    }
	    
	    // Формируем строку для вывода
	    const statsStr = `**PHY:** ${totalStats.PHY} <br> **AGI:** ${totalStats.AGI} <br> **VIG:** ${totalStats.VIG} <br> **TEC:** ${totalStats.TEC}`;

        // 2. БИЛД / МУТАЦИЯ
        const combo = combos.find(c => c.req_race === race.id && c.req_spec === spec.id);
        
        let archetypeLink = "";
        let abilitiesStr = "";

        if (combo) {
            // МУТАЦИЯ
            // Ссылка на имя комбо
            archetypeLink = `**[[${files.combos}#${combo.name}|${combo.displayName}]]**<br>*(Мутация)*`;
            // Ссылки на способности
            abilitiesStr = parseAbilities(combo.body, files.combos, combo.name) || "*(Нет данных)*";
        } else {
            // СТАНДАРТ
            // Ссылка на класс
            archetypeLink = `${spec.link}<br>*(Стандарт)*`;
            
            // Способности стандарта
            const specAbilities = parseAbilities(spec.body, files.specs, spec.name);
            
            // Пассивка расы (парсим вручную, так как формат отличается)
            const racePassiveMatch = race.body.match(/\*\*Пассивный навык:\*\*\s*\*\*(.*?)\*\*/);
            // Делаем ссылку на расу для пассивки
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

        // СБОРКА СТРОКИ
        // Здесь используем .link для первого столбца, чтобы работали клики
        tableRows.push([
            `**${race.link}**<br>+<br>**${spec.link}**`,
            archetypeLink,
            statsStr,
            abilitiesStr,
            itemsList
        ]);
    }
}

dv.header(2, "Матрица Классов и Рас");
dv.table(
    ["Связка (Раса + Класс)", "Архетип", "Атрибуты", "Способности", "Арсенал"],
    tableRows
);