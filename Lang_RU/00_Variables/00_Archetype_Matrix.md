```dataviewjs
// --- НАСТРОЙКИ ПУТЕЙ ---
const files = {
    races: "Lang_RU/00_Variables/Registry_Races.md",
    specs: "Lang_RU/00_Variables/Registry_Specs.md",
    combos: "Lang_RU/00_Variables/Registry_Combos.md"
};

// --- ФУНКЦИИ ПАРСИНГА ---

function parseId(text, key = "id") {
    const regex = new RegExp(`\\[${key}::\\s*(\\w+)\\]`);
    const match = text.match(regex);
    return match ? match[1].toLowerCase() : null;
}

// Парсинг способностей из заголовков #### (возвращает компактные ссылки)
function parseAbilities(text, filePath, headerName) {
    const regex = /^####\s+(.*?\(([PQE])\):\s*(.*?))$/gm;
    const matches = [...text.matchAll(regex)];
    
    if (matches.length === 0) return "";

    return matches.map(m => {
        const fullHeader = m[1].trim(); 
        const key = m[2]; // P, Q, E
        let name = m[3].trim().replace(/`/g, ""); // Убираем кавычки
        
        // Формат: [Link|(Q) Name]
        return `[[${filePath}#${fullHeader}|(${key}) ${name}]]`;
    }).join("<br>");
}

async function parseFile(path, type) {
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
        
        if (type === 'combos') {
            data.req_race = parseId(body, "req_race");
            data.req_spec = parseId(body, "req_spec");
        }
        return data;
    });
}

// --- СБОР ДАННЫХ ---

const races = await parseFile(files.races, 'races');
const specs = await parseFile(files.specs, 'specs');
const combos = await parseFile(files.combos, 'combos');

// --- ПОСТРОЕНИЕ МАТРИЦЫ ---

// 1. Заголовки таблицы: Первая колонка пустая (для названий спец), дальше имена Рас
const tableHeaders = ["Спец. \\ Раса", ...races.map(r => r.link)];

const tableRows = [];

// 2. Проходим по каждой специализации (создаем строки)
for (const spec of specs) {
    const row = [];
    
    // Первая ячейка строки - название специализации
    row.push(`**${spec.link}**`); 
    
    // Дальше заполняем ячейки для каждой расы
    for (const race of races) {
        // Ищем, есть ли уникальная комбинация
        const combo = combos.find(c => c.req_race === race.id && c.req_spec === spec.id);
        
        let cellContent = "";
        
        if (combo) {
            // == ВАРИАНТ 1: МУТАЦИЯ ==
            const abilities = parseAbilities(combo.body, files.combos, combo.name);
            cellContent = `${combo.link}<br><small>${abilities}</small>`;
        } else {
            // == ВАРИАНТ 2: СТАНДАРТ ==
            // Если уникальной комбы нет, собираем: Спек + Пассивка расы
            
            // Ищем пассивку расы
            const raceAbs = parseAbilities(race.body, files.races, race.name);
            // Ищем абилки спека
            const specAbs = parseAbilities(spec.body, files.specs, spec.name);
            
            // Формируем вывод (Спек (Std) + список абилок)
            cellContent = `<span style="opacity:0.3">Standard</span><br><small>${raceAbs}<br>${specAbs}</small>`;
        }
        
        row.push(cellContent);
    }
    
    tableRows.push(row);
}

// --- ВЫВОД ---
dv.header(2, "Матрица Архетипов");
dv.table(tableHeaders, tableRows);
```