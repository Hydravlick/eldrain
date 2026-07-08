import assert from "node:assert/strict";
import { existsSync, readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const RACE_DIR = path.join(ROOT, "04_Player_Entities", "Races");
const SPEC_DIR = path.join(ROOT, "04_Player_Entities", "Specs");
const RACE_HUB = path.join(ROOT, "04_Player_Entities", "_Registries", "Registry_Races.md");
const SPEC_HUB = path.join(ROOT, "04_Player_Entities", "_Registries", "Registry_Specs.md");
const COMBO_REGISTRY = path.join(ROOT, "04_Player_Entities", "_Registries", "Registry_Combos.md");

function frontmatter(text) {
    return text.match(/^---\r?\n([\s\S]*?)\r?\n---/)?.[1] || "";
}

function scalar(source, key) {
    return source
        .match(new RegExp(`^${key}:\\s*([^\\n]+)$`, "m"))?.[1]
        ?.trim()
        .replace(/^["']|["']$/g, "");
}

function inlineList(source, key) {
    const raw = scalar(source, key) || "[]";
    return raw
        .replace(/^\[|\]$/g, "")
        .split(",")
        .map(value => value.trim())
        .filter(Boolean);
}

function entityPages(directory, expectedType) {
    if (!existsSync(directory)) return [];

    return readdirSync(directory)
        .filter(name => name.endsWith(".md"))
        .map(name => {
            const filePath = path.join(directory, name);
            const source = readFileSync(filePath, "utf8");
            const yaml = frontmatter(source);
            const inlineFields = Object.fromEntries(
                [...source.matchAll(/\[([a-z_]+)::\s*([^\]]+)\]/g)]
                    .map(match => [match[1], match[2].trim()])
            );
            return {
                filePath,
                source,
                yaml,
                type: scalar(yaml, "type"),
                id: scalar(yaml, "id"),
                contentScope: scalar(yaml, "content_scope"),
                baseVector: scalar(yaml, "base_vector"),
                weakTo: inlineList(yaml, "weak_to"),
                touch: Object.fromEntries(
                    ["TRQ", "GRP", "LYR", "GLW", "SNS"]
                        .map(key => [key, scalar(yaml, `touch_${key}`)])
                ),
                inlineFields,
                expectedType
            };
        });
}

function comboRecords(source) {
    const inline = (body, key) => body.match(new RegExp(`\\[${key}::\\s*([^\\]]+)\\]`, "i"))?.[1]?.trim();

    return source.split(/^##\s+/m).slice(1).flatMap(block => {
        const lines = block.split("\n");
        const header = lines[0].trim();
        const body = lines.slice(1).join("\n");
        const id = inline(body, "id")?.toLowerCase();
        if (!id || id.startsWith("template_")) return [];
        return [{
            id,
            header,
            reqRace: inline(body, "req_race")?.toLowerCase(),
            reqSpec: inline(body, "req_spec")?.toLowerCase()
        }];
    });
}

test("race and spec folders are the unique page-level entity sources", () => {
    const races = entityPages(RACE_DIR, "race");
    const specs = entityPages(SPEC_DIR, "spec");
    const raceIds = races.map(item => item.id).sort();
    const specIds = specs.map(item => item.id).sort();

    assert.deepEqual(raceIds, ["hedgehog", "lizard", "rat", "squirrel", "toad"]);
    assert.deepEqual(specIds, ["assault", "guard", "scout", "specialist", "support"]);
    assert.equal(new Set(raceIds).size, raceIds.length);
    assert.equal(new Set(specIds).size, specIds.length);

    const expectedInlineFields = {
        hedgehog: ["cap_mod", "substats"],
        rat: ["cap_mod", "substats", "tradeoff"],
        squirrel: ["cap_mod", "substats", "tradeoff"],
        toad: ["cap_mod", "substats"],
        lizard: ["substats"],
        guard: ["condition_bonus", "substats", "tradeoff"],
        assault: ["condition_bonus", "substats", "tradeoff"],
        support: ["condition_bonus", "substats"],
        scout: ["condition_bonus", "substats", "tradeoff"],
        specialist: ["condition_bonus", "substats"]
    };

    for (const entity of [...races, ...specs]) {
        assert.equal(entity.type, entity.expectedType, `${entity.filePath} has the expected type`);
        assert.ok(entity.contentScope, `${entity.filePath} has content_scope`);
        assert.ok(entity.baseVector, `${entity.filePath} has base_vector`);
        assert.equal(entity.weakTo.length, 3, `${entity.filePath} has three weak_to entries`);
        assert.deepEqual(
            Object.keys(entity.touch),
            ["TRQ", "GRP", "LYR", "GLW", "SNS"],
            `${entity.filePath} exposes the TOUCH schema`
        );
        for (const [key, value] of Object.entries(entity.touch)) {
            assert.ok(value !== undefined, `${entity.filePath} has touch_${key}`);
            assert.ok(Number.isFinite(Number(value)), `${entity.filePath} touch_${key} is numeric`);
        }
        assert.doesNotMatch(
            entity.yaml,
            /^(?:touch|substats|cap_mod|condition_bonus|tradeoff):\s*\{/m,
            `${entity.filePath} has no unsupported YAML object properties`
        );
        assert.deepEqual(
            Object.keys(entity.inlineFields).sort(),
            expectedInlineFields[entity.id],
            `${entity.filePath} keeps flexible modifiers in inline Dataview fields`
        );
    }
});

test("family hubs contain views but no duplicate inline entity data", () => {
    const raceHub = readFileSync(RACE_HUB, "utf8");
    const specHub = readFileSync(SPEC_HUB, "utf8");

    assert.match(raceHub, /FROM "04_Player_Entities\/Races"/);
    assert.match(specHub, /FROM "04_Player_Entities\/Specs"/);
    assert.doesNotMatch(raceHub, /\[id::/);
    assert.doesNotMatch(specHub, /\[id::/);
    assert.doesNotMatch(raceHub, /\[(?:base_vector|weak_to|TRQ|GRP|LYR|GLW|SNS)::/);
    assert.doesNotMatch(specHub, /\[(?:base_vector|weak_to|TRQ|GRP|LYR|GLW|SNS)::/);
});

test("combo registry stores only combo deltas and every parent resolves", () => {
    const races = entityPages(RACE_DIR, "race");
    const specs = entityPages(SPEC_DIR, "spec");
    const raceIds = new Set(races.map(item => item.id));
    const specIds = new Set(specs.map(item => item.id));
    const source = readFileSync(COMBO_REGISTRY, "utf8");
    const combos = comboRecords(source);

    assert.equal(combos.length, 9);
    assert.equal(new Set(combos.map(item => item.id)).size, combos.length);
    assert.doesNotMatch(source, /\[base_weakness::/);
    assert.match(source, /dv\.pages\('\"04_Player_Entities\/Races\"'\)/);
    assert.match(source, /dv\.pages\('\"04_Player_Entities\/Specs\"'\)/);

    for (const combo of combos) {
        assert.ok(raceIds.has(combo.reqRace), `${combo.id} resolves race ${combo.reqRace}`);
        assert.ok(specIds.has(combo.reqSpec), `${combo.id} resolves spec ${combo.reqSpec}`);
    }
});
