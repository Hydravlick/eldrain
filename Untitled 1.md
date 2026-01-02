```dataviewjs
// === НАСТРОЙКИ ПУТЕЙ ===
// Убедитесь, что имена файлов совпадают с вашими
const paths = {
    races: "Lang_RU/00_Variables/Registry_Races.md",
    specs: "Lang_RU/00_Variables/Registry_Specs.md",
    items: "Lang_RU/00_Variables/Registry_Items.md",
    combos: "Lang_RU/00_Variables/Registry_Combos.md"
};

// === ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ===

// Парсинг числовых атрибутов (например, [PHY:: +3])
function getStats(text) {
    const stats = { PHY: 0, AGI: 0, VIG: 0, TEC: 0 };
    const regex = /\[(PHY|AGI|VIG|TEC)::\s*([+-]?\d+)\]/g;
    let match;
    while ((match = regex.exec(text)) !== null) {
        stats[match[1]] = parseInt(match[2]);
    }
    return stats;
}

// Создание ссылки на блок: [[Файл#Заголовок|Текст]]
function makeLink(file, header, text) {
    if (!header) return text;
    // Очищаем заголовок от MD символов для ссылки
    const cleanHeader = header.replace(/[\[\]]/g, ""); 
    return `[[${file}#${cleanHeader}|${text}]]`;
}

// Парсинг блоков из файла (разделение по заголовкам ##)
function parseBlocks(content, fileName) {
    const blocks = {};
    if (!content) return blocks;
    
    // Разбиваем по заголовкам ##
    const rawBlocks = content.split(/^## /m).slice(1);
    
    rawBlocks.forEach(raw => {
        const lines = raw.split("\n");
        const header = lines[0].trim(); // Текст заголовка для ссылки
        
        // Ищем ID
        const idMatch = raw.match(/\[id::\s*(\w+)\]/);
        if (idMatch) {
            const id = idMatch[1];
            blocks[id] = {
                id: id,
                header: header,
                fullText: raw,
                stats: getStats(raw),
                fileName: fileName
            };
        }
    });
    return blocks;
}

// === ЗАГРУЗКА ДАННЫХ ===

const files = {
    races: await dv.io.load(paths.races),
    specs: await dv.io.load(paths.specs),
    items: await dv.io.load(paths.items),
    combos: await dv.io.load(paths.combos)
};

// 1. Парсим Расы и Классы
const races = parseBlocks(files.races, paths.races);
const specs = parseBlocks(files.specs, paths.specs);

// 2. Парсим Оружие (связываем по req_race + req_spec)
const itemsMap = {};
const itemBlocks = parseBlocks(files.items, paths.items);
// В Registry_Items часто нет [id::], поэтому перепарсим их иначе, или используем req_ теги
// Для надежности пройдемся по itemBlocks, но если там нет ID, используем ручной поиск требований
const rawItems = files.items.split(/^## /m).slice(1);
rawItems.forEach(raw => {
    const lines = raw.split("\n");
    const header = lines[0].trim();
    
    // Ищем требования
    const raceMatch = raw.match(/\[req_race::\s*(\w+|any)\]/);
    const specMatch = raw.match(/\[req_spec::\s*(\w+|any)\]/);
    
    if (raceMatch && specMatch) {
        const key = `${raceMatch[1]}_${specMatch[1]}`;
        // Достаем статы оружия для отображения
        const dmg = (raw.match(/\[dmg::\s*([^\]]+)\]/) || [])[1] || "-";
        
        itemsMap[key] = {
            name: header,
            link: makeLink(paths.items, header, header),
            stats: `DMG: ${dmg}`,
            raw: raw
        };
    }
});

// 3. Парсим Комбо (Билды) из таблицы
const combosMap = {};
if (files.combos) {
    const rows = files.combos.split("\n").filter(l => l.trim().startsWith("|") && !l.includes("---"));
    rows.forEach(row => {
        const cols = row.split("|").map(c => c.trim().replace(/\*\*/g, "")); // Убираем жирный шрифт
        // Структура: | Race | Spec | BuildName | Passive | ...
        if (cols.length >= 5) {
            const rId = cols[1];
            const sId = cols[2];
            combosMap[`${rId}_${sId}`] = {
                name: cols[3],
                passive: cols[4]
            };
        }
    });
}

// === ГЕНЕРАЦИЯ МАТРИЦЫ ===

const tableData = [];

// Цикл по ВСЕМ расам
Object.values(races).forEach(race => {
    // Цикл по ВСЕМ классам (специализациям)
    Object.values(specs).forEach(spec => {
        
        // 1. Идентификаторы
        const comboKey = `${race.id}_${spec.id}`;
        
        // 2. Данные Билда (из Registry_Combos)
        const build = combosMap[comboKey] || { name: "—", passive: "Нет уникальной синергии" };
        
        // 3. Данные Оружия (Ищем точное совпадение, затем 'any')
        let item = itemsMap[comboKey] 
                   || itemsMap[`any_${spec.id}`] 
                   || itemsMap[`${race.id}_any`] 
                   || { link: "Нет оружия", stats: "" };

        // 4. Суммирование Статов
        const totalStats = {};
        ["PHY", "AGI", "VIG", "TEC"].forEach(stat => {
            const rVal = race.stats[stat] || 0;
            const sVal = spec.stats[stat] || 0;
            const sum = rVal + sVal;
            // Красивое форматирование (+ перед положительными)
            totalStats[stat] = sum > 0 ? `+${sum}` : `${sum}`;
        });
        
        // 5. Способности (парсим из текста класса)
        const qMatch = spec.fullText.match(/Навык \(Q\):\*\*([^\n]+)/);
        const eMatch = spec.fullText.match(/Ульта \(E\):\*\*([^\n]+)/);
        const qText = qMatch ? qMatch[1].trim() : "Нет Q";
        const eText = eMatch ? eMatch[1].trim() : "Нет E";
        
        // Сборка строки таблицы
        tableData.push([
            // Колонка 1: Комбинация (Ссылки)
            `${makeLink(paths.races, race.header, race.header)}<br>+<br>${makeLink(paths.specs, spec.header, spec.header)}`,
            
            // Колонка 2: Билд и Статы
            `**${build.name}**<br>` + 
            `<small>PHY: ${totalStats.PHY} | AGI: ${totalStats.AGI}</small><br>` +
            `<small>VIG: ${totalStats.VIG} | TEC: ${totalStats.TEC}</small>`,
            
            // Колонка 3: Способности (Q/E) с ссылкой на блок класса
            `Q: ${makeLink(paths.specs, spec.header, qText)}<br>` +
            `E: ${makeLink(paths.specs, spec.header, eText)}`,
            
            // Колонка 4: Арсенал
            `${item.link}<br><small>${item.stats}</small><br>` + 
            `<small>_Пассивка:_ ${build.passive}</small>`
        ]);
    });
});

// === ВЫВОД ТАБЛИЦЫ ===

dv.table(
    ["Комбинация", "Билд / Сумм. Статы", "Способности (Связи)", "Арсенал и Бонусы"],
    tableData
);
```