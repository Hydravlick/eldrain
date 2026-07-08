import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";
import vm from "node:vm";

const NOTE_PATH = new URL("../04_Player_Entities/_Matrices/00_Synergy_Map.md", import.meta.url);

function loadHelpers() {
    const markdown = readFileSync(NOTE_PATH, "utf8");
    const block = markdown.match(/```dataviewjs\s*([\s\S]*?)```/);
    assert.ok(block, "DataviewJS block is present");

    const renderStart = block[1].indexOf("\ntry {");
    assert.ok(renderStart > 0, "DataviewJS has a render boundary");

    const source = `${block[1].slice(0, renderStart)}
globalThis.__smHelpers = {
    counterScore: typeof counterScore === "function" ? counterScore : undefined,
    supportScore: typeof supportScore === "function" ? supportScore : undefined,
    sharedWeaknessScore: typeof sharedWeaknessScore === "function" ? sharedWeaknessScore : undefined,
    buildModeLinks: typeof buildModeLinks === "function" ? buildModeLinks : undefined,
    computeWeightedAngles: typeof computeWeightedAngles === "function" ? computeWeightedAngles : undefined,
    matrixCell: typeof matrixCell === "function" ? matrixCell : undefined
};`;

    const context = {
        dv: { current: () => null },
        globalThis: null,
        console
    };
    context.globalThis = context;
    vm.runInNewContext(source, context, { filename: "00_Synergy_Map.helpers.js" });
    return { helpers: context.__smHelpers, markdown };
}

function profile(id, vectors, sharedWeakness, group = id) {
    return { id, name: id, vectors, sharedWeakness, groupName: group };
}

function parseRegistry(relativePath, kind) {
    const text = readFileSync(new URL(`../${relativePath}`, import.meta.url), "utf8");
    const inline = (body, key) => body.match(new RegExp(`\\[${key}::\\s*([^\\]]+)\\]`, "i"))?.[1]?.trim();
    const inlineList = (body, key) => (inline(body, key) || "")
        .split(",")
        .map(value => value.trim().toLowerCase())
        .filter(Boolean);

    return text.split(/^##\s+/m).slice(1).flatMap(block => {
        const lines = block.split("\n");
        const header = lines[0].trim();
        const body = lines.slice(1).join("\n");
        const id = inline(body, "id")?.toLowerCase();
        if (!id || id.startsWith("template_")) return [];

        const record = { id, name: header, header };
        if (kind === "combo") {
            record.reqRace = inline(body, "req_race")?.toLowerCase();
            record.reqSpec = inline(body, "req_spec")?.toLowerCase();
        } else {
            record.baseVector = inline(body, "base_vector")?.toLowerCase();
            record.weakTo = inlineList(body, "weak_to");
        }
        return [record];
    });
}

test("counter mode keeps only a strict directional advantage", () => {
    const { counterScore, buildModeLinks } = loadHelpers().helpers;
    assert.equal(typeof counterScore, "function", "counterScore must exist");
    assert.equal(typeof buildModeLinks, "function", "buildModeLinks must exist");

    const kinetics = profile("kinetics", ["kinetics"], []);
    const tech = profile("tech", ["tech"], []);
    const mirror = profile("mirror", ["kinetics"], []);

    assert.equal(counterScore(kinetics, tech).score, 1);
    assert.equal(counterScore(tech, kinetics).score, 0);

    const decisive = buildModeLinks([kinetics, tech], "counter");
    assert.equal(decisive.length, 1);
    assert.equal(decisive[0].sourceId, "kinetics");
    assert.equal(decisive[0].targetId, "tech");
    assert.equal(decisive[0].strength, 1);

    assert.equal(buildModeLinks([kinetics, mirror], "counter").length, 0);
});

test("support mode requires at least two covered common weaknesses", () => {
    const { supportScore, buildModeLinks } = loadHelpers().helpers;
    assert.equal(typeof supportScore, "function", "supportScore must exist");
    assert.equal(typeof buildModeLinks, "function", "buildModeLinks must exist");

    const source = profile("source", ["tech", "ballistics"], []);
    const strongTarget = profile("strong", ["detection"], ["hazard", "shadow"]);
    const weakTarget = profile("weak", ["detection"], ["hazard"]);

    assert.equal(supportScore(source, strongTarget).score, 2);
    assert.equal(supportScore(source, weakTarget).score, 1);

    const links = buildModeLinks([source, strongTarget, weakTarget], "support");
    assert.ok(links.some(link => link.sourceId === "source" && link.targetId === "strong"));
    assert.ok(links.every(link => link.strength >= 2));
    assert.ok(!links.some(link => link.sourceId === "source" && link.targetId === "weak"));
});

test("shared weakness mode creates one undirected pair", () => {
    const { sharedWeaknessScore, buildModeLinks } = loadHelpers().helpers;
    assert.equal(typeof sharedWeaknessScore, "function", "sharedWeaknessScore must exist");
    assert.equal(typeof buildModeLinks, "function", "buildModeLinks must exist");

    const left = profile("left", ["tech"], ["hazard"]);
    const right = profile("right", ["shadow"], ["hazard", "detection"]);
    const score = sharedWeaknessScore(left, right);

    assert.equal(score.score, 1);
    assert.deepEqual([...score.reasons], ["общая слабость: Биохимия"]);

    const links = buildModeLinks([left, right], "shared_weakness");
    assert.equal(links.length, 1);
    assert.equal(links[0].direction, "both");
});

test("weighted angles derive intra-race and cross-race gaps from item count", () => {
    const { computeWeightedAngles } = loadHelpers().helpers;
    assert.equal(typeof computeWeightedAngles, "function", "computeWeightedAngles must exist");

    const items = [
        { group: "A" },
        { group: "A" },
        { group: "B" },
        { group: "B" }
    ];
    const angles = computeWeightedAngles(items, item => item.group, 1.75);
    assert.equal(angles.length, items.length);

    const gaps = angles.map((angle, index) => {
        const next = angles[(index + 1) % angles.length];
        return (next - angle + 360) % 360;
    });

    assert.ok(Math.abs(gaps.reduce((sum, gap) => sum + gap, 0) - 360) < 1e-9);
    assert.ok(Math.abs(gaps[1] / gaps[0] - 1.75) < 1e-9);
    assert.ok(Math.abs(gaps[3] / gaps[2] - 1.75) < 1e-9);
});

test("radial UI exposes exactly three modes and label-only interaction", () => {
    const { markdown } = loadHelpers();

    assert.match(markdown, /activeMode\s*=\s*["']counter["']/);
    assert.match(markdown, /Контрпики/);
    assert.match(markdown, /Сильная поддержка/);
    assert.match(markdown, /Общая слабость/);
    assert.match(markdown, /var\(--text-accent\)/);
    assert.doesNotMatch(markdown, /node-dots|nodeDots/);
    assert.doesNotMatch(markdown, /shared_vector|shared_arsenal/);
});

test("matrix cells preserve directional scores and hide the diagonal", () => {
    const { matrixCell } = loadHelpers().helpers;
    assert.equal(typeof matrixCell, "function", "matrixCell must exist");

    const source = profile("source", ["tech", "ballistics"], []);
    const weakTarget = profile("weak", ["detection"], ["hazard"]);
    const strongTarget = profile("strong", ["detection"], ["hazard", "shadow"]);
    const kinetics = profile("kinetics", ["kinetics"], []);
    const tech = profile("tech", ["tech"], []);

    assert.equal(matrixCell(source, source, "counter"), null);
    assert.equal(matrixCell(kinetics, tech, "counter").score, 1);
    assert.equal(matrixCell(tech, kinetics, "counter").score, 0);

    const weakSupport = matrixCell(source, weakTarget, "support");
    const strongSupport = matrixCell(source, strongTarget, "support");
    assert.equal(weakSupport.score, 1);
    assert.equal(weakSupport.strong, false);
    assert.equal(strongSupport.score, 2);
    assert.equal(strongSupport.strong, true);

    const sharedLeft = profile("left", ["tech"], ["hazard"]);
    const sharedRight = profile("right", ["shadow"], ["hazard", "detection"]);
    assert.equal(matrixCell(sharedLeft, sharedRight, "shared_weakness").score, 1);
    assert.equal(matrixCell(sharedRight, sharedLeft, "shared_weakness").score, 1);
});

test("matrix view has tabs, a responsive host, and focusable cells", () => {
    const { markdown } = loadHelpers();

    assert.match(markdown, /activeView\s*=\s*["']map["']/);
    assert.match(markdown, /Карта/);
    assert.match(markdown, /Матрица/);
    assert.match(markdown, /synergy-matrix-host/);
    assert.match(markdown, /renderMatrixState/);
    assert.match(markdown, /tabindex/);
});

test("current registries produce the expected sparse radial counts", () => {
    const { buildModeLinks } = loadHelpers().helpers;
    const races = parseRegistry("04_Player_Entities/_Registries/Registry_Races.md", "race");
    const specs = parseRegistry("04_Player_Entities/_Registries/Registry_Specs.md", "spec");
    const combos = parseRegistry("04_Player_Entities/_Registries/Registry_Combos.md", "combo");
    const racesById = new Map(races.map(item => [item.id, item]));
    const specsById = new Map(specs.map(item => [item.id, item]));

    const profiles = combos.map(combo => {
        const race = racesById.get(combo.reqRace);
        const spec = specsById.get(combo.reqSpec);
        return {
            ...combo,
            race,
            spec,
            vectors: [...new Set([race?.baseVector, spec?.baseVector].filter(Boolean))],
            sharedWeakness: race && spec
                ? race.weakTo.filter(weakness => spec.weakTo.includes(weakness))
                : []
        };
    }).filter(item => item.race && item.spec);

    assert.equal(profiles.length, 9);
    assert.equal(buildModeLinks(profiles, "counter").length, 30);
    assert.equal(buildModeLinks(profiles, "support").length, 6);
    assert.equal(buildModeLinks(profiles, "shared_weakness").length, 6);
});
