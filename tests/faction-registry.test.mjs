import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const LORE_DIR = path.join(ROOT, "03_Factions_Societies", "Lore");
const REGISTRY_PATH = path.join(ROOT, "03_Factions_Societies", "_Registries", "Registry_Factions.md");
const MAP_PATH = path.join(ROOT, "03_Factions_Societies", "_Matrices", "00_Faction_Reputation.md");

const EXPECTED_IDS = [
    "ash_commission",
    "cathedral_all_faiths",
    "chalk_hands",
    "circle_of_interposition",
    "common_storehouses",
    "contour_chamber",
    "first_reception",
    "free_benches",
    "funeral_circles",
    "garden_chains",
    "hidden_entity",
    "keepers",
    "lamp_shifts",
    "lift_families",
    "minstrels",
    "night_guarantors",
    "proving_houses",
    "support_artels",
    "warm_kitchens",
    "weighing_houses"
];

const EXPECTED_RELATION_COUNTS = {
    conflict: 18,
    hunt: 1,
    monitor: 5,
    spy: 5,
    trade: 9,
    union: 20
};

function frontmatter(source) {
    return source.match(/^---\r?\n([\s\S]*?)\r?\n---/)?.[1] || "";
}

function scalar(yaml, key) {
    return yaml
        .match(new RegExp(`^${key}:\\s*([^\\n]+)$`, "m"))?.[1]
        ?.trim()
        .replace(/^["']|["']$/g, "");
}

function relationRecords(source) {
    return [...source.matchAll(/^\[rel_([a-z0-9_]+)::\s*([^\]]+)\]\s*\(([^\n\r]*)\)/gmi)]
        .map(match => ({
            type: match[1].toLowerCase(),
            target: match[2].trim().toLowerCase(),
            reason: match[3].trim()
        }));
}

function factionPages() {
    return readdirSync(LORE_DIR).filter(name => name.endsWith(".md")).flatMap(name => {
        const filePath = path.join(LORE_DIR, name);
        const source = readFileSync(filePath, "utf8");
        const yaml = frontmatter(source);
        if (scalar(yaml, "type") !== "faction") return [];

        return [{
            name,
            filePath,
            source,
            id: scalar(yaml, "faction_id")?.toLowerCase(),
            displayName: scalar(yaml, "display_name"),
            role: scalar(yaml, "faction_role"),
            promise: scalar(yaml, "promise"),
            relations: relationRecords(source)
        }];
    });
}

test("faction pages preserve the exact entity and relation graph", () => {
    const factions = factionPages();
    const ids = factions.map(faction => faction.id).sort();
    const idSet = new Set(ids);
    const relations = factions.flatMap(faction => faction.relations);
    const counts = Object.fromEntries(Object.keys(EXPECTED_RELATION_COUNTS).map(type => [
        type,
        relations.filter(relation => relation.type === type).length
    ]));

    assert.deepEqual(ids, EXPECTED_IDS);
    assert.equal(idSet.size, 20);
    assert.equal(relations.length, 58);
    assert.deepEqual(counts, EXPECTED_RELATION_COUNTS);

    for (const faction of factions) {
        assert.ok(faction.displayName, `${faction.filePath} has display_name`);
        assert.ok(faction.role, `${faction.filePath} has faction_role`);
        assert.ok(faction.promise, `${faction.filePath} has promise`);
    }

    for (const relation of relations) {
        assert.ok(EXPECTED_RELATION_COUNTS[relation.type] !== undefined, `known relation type ${relation.type}`);
        assert.ok(relation.target === "all" || idSet.has(relation.target), `known target ${relation.target}`);
        assert.ok(relation.reason.length > 0, `${relation.type} -> ${relation.target} has a reason`);
    }
});

test("cartographers remain supporting lore instead of a registry faction", () => {
    const source = readFileSync(path.join(LORE_DIR, "The_Cartographers.md"), "utf8");
    assert.equal(scalar(frontmatter(source), "type"), "lore");
    assert.equal(scalar(frontmatter(source), "faction_id"), undefined);
});

test("Registry_Factions is a view with no duplicate faction records", () => {
    const source = readFileSync(REGISTRY_PATH, "utf8");
    assert.match(source, /FROM "03_Factions_Societies\/Lore"/);
    assert.match(source, /WHERE type = "faction"/);
    assert.doesNotMatch(source, /^\[faction::/m);
    assert.doesNotMatch(source, /^\[rel_[a-z0-9_]+::/mi);
});

test("faction reputation reads page entities instead of Registry_Factions", () => {
    const source = readFileSync(MAP_PATH, "utf8");
    assert.match(source, /dv\.pages\(`?['"]?"03_Factions_Societies\/Lore"/);
    assert.match(source, /faction_id/);
    assert.doesNotMatch(source, /sourceFilePath\s*=\s*["']Registry_Factions\.md["']/);
});
