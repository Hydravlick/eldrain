```dataviewjs
// --- НАСТРОЙКИ ПУТЕЙ ---
const files = {
    biomes: "Lang_RU/00_Variables/Registry_Biomes.md",
    mobs: "Lang_RU/00_Variables/Registry_Mobs.md",
    items: "Lang_RU/00_Variables/Registry_Items.md"
};

// --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---

function parseTagId(text, tag) {
    const regex = new RegExp(`\\[${tag}::\\s*(\\w+)\\]`);
    const match = text.match(regex);
    return match ? match[1].toLowerCase() : null;
}

function parseAllTags(text, tag) {
    const regex = new RegExp(`\\[${tag}::\\s*(\\w+)\\]`, "g");
    const matches = [...text.matchAll(regex)];
    return matches.map(m => m[1].toLowerCase());
}

async function parseFileBlocks(path, splitRegex) {
    const page = dv.page(path);
    if (!page) return [];
    const content = await dv.io.load(page.file.path);
    return content.split(splitRegex).slice(1);
}

function formatId(id) {
    if (!id) return "";
    return id.split('_')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

function getEffectInfo(lines) {
    let effectIdx = -1;
    let effectId = null;

    for (let i = 0; i < lines.length; i++) {
        if (lines[i].includes("[env_effect::")) {
            effectIdx = i;
            effectId = parseTagId(lines[i], "env_effect");
            break;
        }
    }

    if (effectIdx === -1 || !effectId) return null;

    const description = [];
    for (let i = effectIdx + 1; i < lines.length; i++) {
        const line = lines[i];
        if (/^(\t|\s{2,})[-*]/.test(line)) {
            let cleanLine = line.replace(/^(\t|\s{2,})[-*]\s*/, "").trim();
            description.push(cleanLine);
        } else if (line.trim() === "") {
            continue;
        } else {
            break;
        }
    }

    return { id: effectId, desc: description };
}

// --- СБОР ДАННЫХ ---

const itemBlocks = await parseFileBlocks(files.items, /^### /m);
const itemMap = {};
itemBlocks.forEach(block => {
    const lines = block.split("\n");
    const header = lines[0].trim();
    const displayName = header.split(" [")[0].replace(/\(.*\)/, "").trim();
    const id = parseTagId(block, "item") || parseTagId(block, "merit") || parseTagId(block, "key") || parseTagId(block, "weapon") || parseTagId(block, "artifact");
    if (id) itemMap[id] = `[[${files.items}#${header}|${displayName}]]`;
});

const mobBlocks = await parseFileBlocks(files.mobs, /^### /m);
const mobMap = {};
mobBlocks.forEach(block => {
    const lines = block.split("\n");
    const header = lines[0].trim();
    const displayName = header.replace(/\(.*\)/, "").trim();
    const id = parseTagId(block, "mob") || parseTagId(block, "boss");
    const lootIds = [];
    const itemMatches = [...block.matchAll(/\[(item|weapon|artifact|key|merit)::\s*(\w+)\]/g)];
    itemMatches.forEach(m => lootIds.push(m[2].toLowerCase()));
    if (id) {
        mobMap[id] = {
            link: `[[${files.mobs}#${header}|${displayName}]]`,
            loot: lootIds
        };
    }
});

// --- ГЕНЕРАЦИЯ ТАБЛИЦ ---

const biomeBlocks = await parseFileBlocks(files.biomes, /^## /m);

for (const biomeBlock of biomeBlocks) {
    const lines = biomeBlock.split("\n");
    const biomeHeader = lines[0].trim();
    const biomeName = biomeHeader.split(" [")[0].trim();
    
    dv.header(2, `[[${files.biomes}#${biomeHeader}|${biomeName}]]`);

    const levels = biomeBlock.split(/^### /m).slice(1);
    const tableRows = [];

    levels.forEach(lvlBlock => {
        const lvlLines = lvlBlock.split("\n");
        const lvlHeader = lvlLines[0].trim();
        
        // --- 1. Колонка: Уровень (ИЗМЕНЕНО) ---
        
        // 1. Ищем номер уровня (цифру после level/lvl)
        const lvlMatch = lvlHeader.match(/(?:level|lvl)\s*(\d+)/i);
        const num = lvlMatch ? lvlMatch[1] : "?";
        
        // 2. Ищем название (всё, что после "::", или весь текст минус "level N")
        const parts = lvlHeader.split("::");
        const name = parts.length > 1 
            ? parts[1].trim() 
            : lvlHeader.replace(/(?:level|lvl)\s*\d+/i, "").trim();
            
        // 3. Формируем единую ссылку: [[File#Header | (N) Name]]
        // Результат: (1) Сборочный Цех
        const label = `(${num}) ${name}`;
        const levelLink = `[[${files.biomes}#${lvlHeader}|${label}]]`;

        // --- 2. Колонка: Эффект ---
        const effectInfo = getEffectInfo(lvlLines);
        let effectCol = "*(Нет эффектов)*";
        if (effectInfo) {
            const effectTitle = `**${formatId(effectInfo.id)}**`;
            const descHtml = effectInfo.desc.length > 0 
                ? "<ul style='margin-top:0; padding-left:20px;'>" + effectInfo.desc.map(d => `<li>${d}</li>`).join("") + "</ul>"
                : "";
            effectCol = `${effectTitle}${descHtml}`;
        }

        // --- 3. Колонка: Враги ---
        const mobsOnLevel = [
            ...parseAllTags(lvlBlock, "mob"),
            ...parseAllTags(lvlBlock, "boss")
        ];

        let mobsColStr = mobsOnLevel.length > 0 ? "" : "*(Тихо)*";
        let combinedLootIds = [];

        if (mobsOnLevel.length > 0) {
            const mobLinks = mobsOnLevel.map(mid => {
                if (mobMap[mid]) {
                    combinedLootIds.push(...mobMap[mid].loot);
                    return mobMap[mid].link;
                }
                return `*${mid}*`;
            });
            mobsColStr = mobLinks.join("<br>");
        }

        // --- 4. Колонка: Лут ---
        const uniqueLoot = [...new Set(combinedLootIds)].sort();
        let lootColStr = uniqueLoot.length > 0 
            ? uniqueLoot.map(lid => itemMap[lid] || lid).join(", ")
            : "*(Пусто)*";

        tableRows.push([levelLink, effectCol, mobsColStr, lootColStr]);
    });

    dv.table(
        ["Локация", "Эффект Среды", "Враги", "Лут"],
        tableRows
    );
    
    dv.paragraph("---");
}
```