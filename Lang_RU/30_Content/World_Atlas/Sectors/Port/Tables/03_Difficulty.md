```dataviewjs
// --- НАСТРОЙКИ ПУТЕЙ ---
// Список всех файлов, где могут быть определения предметов/лута
const registryFiles = {
    items: "Lang_RU/00_Variables/Registry_Items.md",
    weapons: "Lang_RU/00_Variables/Registry_Weapons.md",
    armors: "Lang_RU/00_Variables/Registry_Armors.md",
    headwear: "Lang_RU/00_Variables/Registry_Headwear.md",
    consumables: "Lang_RU/00_Variables/Registry_Consumables.md",
    blueprints: "Lang_RU/00_Variables/Registry_Blueprints.md"
};

// Пути к основным системным файлам
const coreFiles = {
    biomes: "Lang_RU/00_Variables/Registry_Biomes.md",
    mobs: "Lang_RU/00_Variables/Registry_Mobs.md"
};

// Список тегов, которые считаются идентификаторами предметов (для поиска определений и лута)
const validLootTags = [
    "item", "weapon", "armor", "headwear", 
    "consumable", "blueprint", "key", 
    "merit", "artifact"
];

// --- ОПРЕДЕЛЕНИЕ КОНТЕКСТА (АДАПТИВНОСТЬ) ---
const currentPath = dv.current().file.path;
const pathParts = currentPath.split("/");
const sectorIndex = pathParts.findIndex(p => p === "Sectors");
let targetBiomeId = null;

if (sectorIndex !== -1 && pathParts[sectorIndex + 1]) {
    targetBiomeId = pathParts[sectorIndex + 1].toLowerCase();
} else {
    targetBiomeId = dv.current().file.folder.split("/").pop().toLowerCase();
}

const fileName = dv.current().file.name;
const levelMatch = fileName.match(/^(\d+)/);
const targetLevel = levelMatch ? levelMatch[1] : "1";

dv.paragraph(`> **Контекст:** Биом: \`${targetBiomeId}\` | Сложность: \`${targetLevel}\``);

// --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---

// Поиск конкретного ID по тегу (возвращает первый найденный)
function parseTagId(text, tag) {
    const regex = new RegExp(`\\[${tag}::\\s*([\\w\\d_]+)\\]`, "i");
    const match = text.match(regex);
    return match ? match[1].toLowerCase() : null;
}

// Поиск ВСЕХ ID по тегу (для списка мобов на уровне)
function parseAllTags(text, tag) {
    const regex = new RegExp(`\\[${tag}::\\s*([\\w\\d_]+)\\]`, "gi");
    const matches = [...text.matchAll(regex)];
    return matches.map(m => m[1].toLowerCase());
}

// Поиск ID предмета среди всех возможных тегов
function findAnyItemId(text) {
    for (const tag of validLootTags) {
        const id = parseTagId(text, tag);
        if (id) return id;
    }
    return null;
}

// Загрузка и разбивка файла на блоки заголовков
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

// 1. Загрузка всех предметов из всех реестров
let itemMap = {};

// Проходим по каждому файлу реестра (items, weapons, armors и т.д.)
for (const [key, path] of Object.entries(registryFiles)) {
    const blocks = await parseFileBlocks(path, /^### /m);
    if (blocks.length > 0) {
        blocks.forEach(block => {
            const lines = block.split("\n");
            const header = lines[0].trim();
            // Убираем лишнее из заголовка для чистого названия
            const displayName = header.split(" [")[0].replace(/\(.*\)/, "").trim();
            
            // Ищем ID, проверяя все возможные теги (item, weapon, armor...)
            const id = findAnyItemId(block);
            
            if (id) {
                itemMap[id] = `[[${path}#${header}|${displayName}]]`;
            }
        });
    }
}

// 2. Загрузка мобов и их лута
const mobBlocks = await parseFileBlocks(coreFiles.mobs, /^### /m);
const mobMap = {};
// Создаем регулярку, включающую все валидные теги: (item|weapon|armor|...)
const lootRegex = new RegExp(`\\[(${validLootTags.join("|")})::\\s*(\\w+)\\]`, "gi");

mobBlocks.forEach(block => {
    const lines = block.split("\n");
    const header = lines[0].trim();
    const displayName = header.replace(/\(.*\)/, "").trim();
    
    const id = parseTagId(block, "mob") || parseTagId(block, "boss");
    
    const lootIds = [];
    const itemMatches = [...block.matchAll(lootRegex)];
    itemMatches.forEach(m => lootIds.push(m[2].toLowerCase())); // m[2] это ID

    if (id) {
        mobMap[id] = {
            link: `[[${coreFiles.mobs}#${header}|${displayName}]]`,
            loot: lootIds
        };
    }
});

// --- ПОИСК И ГЕНЕРАЦИЯ ТАБЛИЦЫ ---

const biomeBlocks = await parseFileBlocks(coreFiles.biomes, /^## /m);
let foundData = false;

for (const biomeBlock of biomeBlocks) {
    const biomeId = parseTagId(biomeBlock, "biome");
    if (biomeId !== targetBiomeId) continue;

    const lines = biomeBlock.split("\n");
    const biomeHeader = lines[0].trim();
    const biomeName = biomeHeader.split(" [")[0].trim();
    
    const levels = biomeBlock.split(/^### /m).slice(1);
    const tableRows = [];

    for (const lvlBlock of levels) {
        const lvlLines = lvlBlock.split("\n");
        const lvlHeader = lvlLines[0].trim();
        const diffId = parseTagId(lvlBlock, "difficulty");
        
        if (diffId === targetLevel) {
            foundData = true;

            // Название уровня
            const parts = lvlHeader.split("::");
            const name = parts.length > 1 
                ? parts[1].trim() 
                : lvlHeader.replace(/(?:level|lvl)\s*\d+/i, "").trim();
            const label = `${name}`;
            const levelLink = `[[${coreFiles.biomes}#${lvlHeader}|${label}]]`;

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

            // Лут
            const uniqueLoot = [...new Set(combinedLootIds)].sort();
            let lootColStr = uniqueLoot.length > 0 
                ? uniqueLoot.map(lid => itemMap[lid] || lid).join(", ")
                : "*(Пусто)*";

            tableRows.push([levelLink, effectCol, mobsColStr, lootColStr]);
            
            dv.table(
                ["Локация / Уровень", "Эффект Среды", "Враги", "Лут"],
                tableRows
            );
            break; 
        }
    }
    
    if (foundData) break; 
}

if (!foundData) {
    dv.paragraph(`⚠️ **Данные не найдены.** \nУбедитесь, что:\n1. Папка называется корректно (текущая: \`${targetBiomeId}\`).\n2. Файл начинается с цифры уровня (текущая: \`${targetLevel}\`).\n3. В \`Registry_Biomes.md\` есть запись \`[biome:: ${targetBiomeId}]\` и внутри нее \`[difficulty::${targetLevel}]\`.`);
}
```