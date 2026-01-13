```dataviewjs
// --- НАСТРОЙКИ ПУТЕЙ ---
const files = {
    biomes: "Lang_RU/00_Variables/Registry_Biomes.md",
    mobs: "Lang_RU/00_Variables/Registry_Mobs.md",
    items: "Lang_RU/00_Variables/Registry_Items.md"
};

// --- ОПРЕДЕЛЕНИЕ КОНТЕКСТА (АДАПТИВНОСТЬ) ---
// 1. Определяем биом по папке (ищем папку после "Sectors" или используем текущую)
const currentPath = dv.current().file.path;
// Логика: берем сегмент пути после 'Sectors', если есть, иначе родительскую папку
const pathParts = currentPath.split("/");
const sectorIndex = pathParts.findIndex(p => p === "Sectors");
let targetBiomeId = null;

if (sectorIndex !== -1 && pathParts[sectorIndex + 1]) {
    targetBiomeId = pathParts[sectorIndex + 1].toLowerCase();
} else {
    // Резерв: берем название родительской папки (если файл лежит прямо в папке биома)
    targetBiomeId = dv.current().file.folder.split("/").pop().toLowerCase();
}

// 2. Определяем сложность по названию файла (01_Difficulty -> 1)
const fileName = dv.current().file.name;
const levelMatch = fileName.match(/^(\d+)/);
const targetLevel = levelMatch ? levelMatch[1] : "1"; // По умолчанию 1, если цифры нет

dv.paragraph(`> **Контекст:** Биом: \`${targetBiomeId}\` | Сложность: \`${targetLevel}\``);

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

// Загрузка предметов (Items)
let itemMap = {};
const itemBlocks = await parseFileBlocks(files.items, /^### /m);
if (itemBlocks.length > 0) {
    itemBlocks.forEach(block => {
        const lines = block.split("\n");
        const header = lines[0].trim();
        const displayName = header.split(" [")[0].replace(/\(.*\)/, "").trim();
        const id = parseTagId(block, "item") || parseTagId(block, "merit") || parseTagId(block, "key") || parseTagId(block, "weapon") || parseTagId(block, "artifact");
        if (id) itemMap[id] = `[[${files.items}#${header}|${displayName}]]`;
    });
}

// Загрузка мобов (Mobs)
const mobBlocks = await parseFileBlocks(files.mobs, /^### /m);
const mobMap = {};
mobBlocks.forEach(block => {
    const lines = block.split("\n");
    const header = lines[0].trim();
    const displayName = header.replace(/\(.*\)/, "").trim();
    const id = parseTagId(block, "mob");
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

// --- ПОИСК И ГЕНЕРАЦИЯ ---

const biomeBlocks = await parseFileBlocks(files.biomes, /^## /m);
let foundData = false;

for (const biomeBlock of biomeBlocks) {
    // 1. Проверяем, соответствует ли этот блок целевому биому
    const biomeId = parseTagId(biomeBlock, "biome");
    if (biomeId !== targetBiomeId) continue;

    const lines = biomeBlock.split("\n");
    const biomeHeader = lines[0].trim();
    const biomeName = biomeHeader.split(" [")[0].trim();
    
    // Разбиваем на уровни
    const levels = biomeBlock.split(/^### /m).slice(1);
    const tableRows = [];

    // Ищем нужный уровень
    for (const lvlBlock of levels) {
        const lvlLines = lvlBlock.split("\n");
        const lvlHeader = lvlLines[0].trim();
        
        // Проверяем тег difficulty
        const diffId = parseTagId(lvlBlock, "difficulty");
        
        // Если тег совпадает с цифрой из названия файла
        if (diffId === targetLevel) {
            foundData = true;

            // --- Формирование данных для строки ---
            
            // Название уровня
            const parts = lvlHeader.split("::");
            const name = parts.length > 1 
                ? parts[1].trim() 
                : lvlHeader.replace(/(?:level|lvl)\s*\d+/i, "").trim();
            const label = `${name}`;
            const levelLink = `[[${files.biomes}#${lvlHeader}|${label}]]`;

            // Эффект
            const effectInfo = getEffectInfo(lvlLines);
            let effectCol = "*(Нет эффектов)*";
            if (effectInfo) {
                const effectTitle = `**${formatId(effectInfo.id)}**`;
                const descHtml = effectInfo.desc.length > 0 
                    ? "<ul style='margin-top:0; padding-left:20px;'>" + effectInfo.desc.map(d => `<li>${d}</li>`).join("") + "</ul>"
                    : "";
                effectCol = `${effectTitle}${descHtml}`;
            }

            // Враги
            const mobsOnLevel = [
                ...parseAllTags(lvlBlock, "mob")
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

            // Лут
            const uniqueLoot = [...new Set(combinedLootIds)].sort();
            let lootColStr = uniqueLoot.length > 0 
                ? uniqueLoot.map(lid => itemMap[lid] || lid).join(", ")
                : "*(Пусто)*";

            tableRows.push([levelLink, effectCol, mobsColStr, lootColStr]);
            
            // Вывод таблицы только для этого уровня
            dv.header(3, `Сводка по уровню: ${biomeName} - ${name}`);
            dv.table(
                ["Локация / Уровень", "Эффект Среды", "Враги", "Лут"],
                tableRows
            );
            break; // Нашли - выходим из цикла уровней
        }
    }
    
    if (foundData) break; // Нашли биом и уровень - выходим из цикла биомов
}

if (!foundData) {
    dv.paragraph(`⚠️ **Данные не найдены.** \nУбедитесь, что:\n1. Папка называется корректно (текущая: \`${targetBiomeId}\`).\n2. Файл начинается с цифры уровня (текущая: \`${targetLevel}\`).\n3. В \`Registry_Biomes.md\` есть запись \`[biome:: ${targetBiomeId}]\` и внутри нее \`[difficulty::${targetLevel}]\`.`);
}
```