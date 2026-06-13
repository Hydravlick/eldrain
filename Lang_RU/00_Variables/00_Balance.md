```dataviewjs
// --- 1. ГЛОБАЛЬНЫЕ ПРАВИЛА: МАТРИЦА 7 ВЕКТОРОВ (ДВОЙНОЙ ПАРАДОКС) ---
// Математический паттерн [Win, Win, Lose, Win, Lose, Lose] со сдвигом.
const paradoxRules = {
    "hazard": ["shadow", "kinetics", "ballistics"], // Биохимия бьет Тень, Кинетику, Баллистику
    "shadow": ["kinetics", "tech", "aether"],       // Тень бьет Кинетику, Технику, Эфир
    "kinetics": ["tech", "ballistics", "detection"],// Кинетика бьет Технику, Баллистику, Сенсорику
    "tech": ["ballistics", "aether", "hazard"],     // Техника бьет Баллистику, Эфир, Биохимию
    "ballistics": ["aether", "detection", "shadow"],// Баллистика бьет Эфир, Сенсорику, Тень
    "aether": ["detection", "hazard", "kinetics"],  // Эфир бьет Сенсорику, Биохимию, Кинетику
    "detection": ["hazard", "shadow", "tech"]       // Сенсорика бьет Биохимию, Тень, Технику
};

// Словари переводов
const vNames = {
    "hazard": "Биохимия 🧪", "shadow": "Тень 🌫️", "kinetics": "Кинетика 🔨", 
    "tech": "Техника ⚙️", "ballistics": "Баллистика 🔫", "aether": "Эфир 🔮", "detection": "Сенсорика 👁️"
};

// Привязка Рас к Векторам
const raceVectors = {
    "toad": "hazard", "hedgehog": "kinetics", "rat": "tech", "squirrel": "aether", "lizard": "detection"
};

// Привязка Классов к Векторам
const specVectors = {
    "guard": "kinetics", "assault": "ballistics", "support": "tech", "scout": "shadow", "specialist": "aether"
};

// --- 2. СБОР И ПАРСИНГ ДАННЫХ ИЗ РЕЕСТРА ---
const page = dv.page("Registry_Combos");
if (!page) {
    dv.paragraph("❌ Файл Registry_Combos.md не найден.");
    return;
}

const rawContent = await dv.io.load(page.file.path);
const blocks = rawContent.split(/^##\s+/m).slice(1);
const archetypes = [];

blocks.forEach(block => {
    const lines = block.split("\n");
    const header = lines[0].trim();
    if (header === "END_MARKER" || !header) return;

    const body = lines.slice(1).join("\n");
    
    const idMatch = body.match(/\[id::\s*([^\]]+)\]/);
    const raceMatch = body.match(/\[req_race::\s*([^\]]+)\]/);
    const specMatch = body.match(/\[req_spec::\s*([^\]]+)\]/);
    
    if (!idMatch || !raceMatch || !specMatch) return;

    const id = idMatch[1].toLowerCase().trim();
    const race = raceMatch[1].toLowerCase().trim();
    const spec = specMatch[1].toLowerCase().trim();
    const displayName = header.split('(')[0].trim();

    // Формируем уникальные векторы сборки (если Раса и Класс дают один вектор, он не дублируется)
    const activeVectors = [...new Set([raceVectors[race], specVectors[spec]])].filter(Boolean);

    archetypes.push({ 
        id, name: displayName, race, spec, vectors: activeVectors, dominates: [], vulnerableTo: []
    });
});

// --- 3. РАСЧЕТ СТОЛКНОВЕНИЙ В ГРАФЕ ---
for (let i = 0; i < archetypes.length; i++) {
    for (let j = 0; j < archetypes.length; j++) {
        if (i === j) continue;
        
        const A = archetypes[i];
        const B = archetypes[j];
        
        let scoreA = 0;
        let scoreB = 0;
        let reasonsA = [];
        let reasonsB = [];

        // Проверяем векторы А против векторов Б
        A.vectors.forEach(vA => {
            B.vectors.forEach(vB => {
                if (paradoxRules[vA] && paradoxRules[vA].includes(vB)) {
                    scoreA++;
                    reasonsA.push(`${vNames[vA]} бьет ${vNames[vB]}`);
                }
                if (paradoxRules[vB] && paradoxRules[vB].includes(vA)) {
                    scoreB++;
                    reasonsB.push(`${vNames[vB]} бьет ${vNames[vA]}`);
                }
            });
        });

        // Жесткая доминация: если А пробивает Б чаще, чем Б пробивает А
        if (scoreA > scoreB) {
            A.dominates.push(`**${B.name}** <span style="font-size:0.8em; color:var(--text-muted);">(${reasonsA.join(", ")})</span>`);
        }
        
        // Поиск "Абсолютного хард-контра" (по правилу двойного парадокса)
        // Если Б бьет ОБА вектора А, это критическая уязвимость
        if (scoreB === A.vectors.length && A.vectors.length > 0) {
             A.vulnerableTo.push(`**${B.name}** <span style="color:#e06c75; font-size:0.8em;">(Ломает весь билд)</span>`);
        }
    }
}

// --- 4. ОТРИСОВКА ИНТЕРФЕЙСА ---
dv.header(2, "🕸️ Эмерджентная Матрица: Тактические Векторы");
dv.paragraph("*Баланс формируется автоматически на пересечении Биологии (Раса) и Метода (Класс).*");

const headers = ["Оболочка (Сборка)", "Активные Векторы", "Уверенно доминирует над", "Абсолютная уязвимость (Хард-контр)"];
const rows = archetypes.map(arch => {
    
    const vecDisplay = arch.vectors.map(v => vNames[v]).join("<br>");
    
    return [
        `**${arch.name}**<br><span style="font-size:0.8em;">${arch.race} + ${arch.spec}</span>`,
        vecDisplay,
        arch.dominates.join("<br><br>") || "*Нет доминации*",
        arch.vulnerableTo.join("<br>") || `<span style="color:#98c379;">Нет Хард-контра</span>`
    ];
});

dv.table(headers, rows);