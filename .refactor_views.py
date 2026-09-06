from importlib.machinery import SourceFileLoader
import re,json
w=SourceFileLoader('w','.refactor_work.py').load_module()
R=w.ROOT
def view(name,sources,kind):
 p=w.find(name);w.meta(p,{'type':'view','view_kind':kind,'upstream_sources':[w.ref(x) for x in sources]},['index_route','index_group','index_order','index_summary','read_when']);return p
def prop(p,key,stem):w.meta(p,{key:w.ref(stem)})

p=view('00_Synergy_Map',['Two_Paradox_Vector_Matrix','Registry_Combos','Registry_Races','Registry_Specs'],'synergy_map')
prop(p,'combos_ref','Registry_Combos');prop(p,'topology_ref','Two_Paradox_Vector_Matrix')
s=p.read_text(encoding='utf-8')
a=s.index('const sources =');b=s.index('const modeMeta =',a)
s=s[:a]+'''const combosPage = dv.page(dv.current().combos_ref);
const topologyPage = dv.page(dv.current().topology_ref);
if (!combosPage || !topologyPage) throw new Error("Отсутствует источник Combo или топологии");
const sources = { races: "race", specs: "spec", combos: combosPage.file.path };
const currentPath = dv.current().file.path;
const topologyText = await dv.io.load(topologyPage.file.path);
const paradoxRules = {};
const vectorNames = {};
for (const block of topologyText.split(/^### /m).slice(1)) {
    const id = block.match(/\\[vector_id::\\s*(\\w+)\\]/)?.[1];
    const label = block.match(/\\[vector_label::\\s*([^\\]]+)\\]/)?.[1];
    const targets = block.match(/\\[dominates::\\s*([^\\]]+)\\]/)?.[1];
    if (!id) continue;
    if (paradoxRules[id] || !label || !targets) throw new Error("Некорректный vector record: " + id);
    paradoxRules[id] = targets.split(",").map(x => x.trim());
    vectorNames[id] = label.trim();
}
if (!Object.keys(paradoxRules).length) throw new Error("Нет записей vector_id в источнике топологии");
for (const targets of Object.values(paradoxRules)) {
    if (targets.some(id => !paradoxRules[id])) throw new Error("Неизвестная цель dominates");
}

'''+s[b:]
s=s.replace('Array.from(dv.pages(`"${folder}"`))','Array.from(dv.pages())').replace('.filter(page => page.type === type)','.filter(page => page.type === "entity" && page.entity_kind === type && page.status === "active")')
w.write(p,s)
p=view('00_Faction_Reputation',['Registry_Factions','Civic_Order'],'faction_relationships');s=p.read_text(encoding='utf-8');s=s.replace('const sourceFolder = "03_Factions_Societies/Lore";','const sourceFolder = dv.current().file.path;').replace("dv.pages('\"03_Factions_Societies/Lore\"')",'dv.pages()');s=s.replace('```dataviewjs','# Отношения городских сторон\n\nПроизводная карта читает идентичность и направленные `rel_*` записи фракционных сущностей через [[03_Factions_Societies/_Registries/Registry_Factions]]. Она показывает отношения и причины, но не определяет репутацию, услуги или доступ.\n\n```dataviewjs',1);w.write(p,s)
p=view('00_Biome_Matrix',['Registry_Biomes','Registry_Mobs','Registry_Items'],'biome_matrix')
for key,stem in [('biomes_ref','Registry_Biomes'),('mobs_ref','Registry_Mobs'),('items_ref','Registry_Items')]:prop(p,key,stem)
s=p.read_text(encoding='utf-8');a=s.index('const files =');b=s.index('// --- ВСПОМОГАТЕЛЬНЫЕ',a)
s=s[:a]+'''const files = {};
for (const kind of ["biomes", "mobs", "items"]) {
    const page = dv.page(dv.current()[kind + "_ref"]);
    if (!page) throw new Error("Отсутствует источник: " + kind);
    files[kind] = page.file.path;
}

'''+s[b:]
s=s.replace('```dataviewjs','# Биомы: среда, враги и добыча\n\nПроизводное сопоставление [[08_World_Generation/_Registries/Registry_Biomes]], [[08_World_Generation/_Registries/Registry_Mobs]] и [[07_Gear_Inventory/_Registries/Registry_Items]]. Таблица не задаёт spawn policy и не обещает конкретную награду.\n\n```dataviewjs',1)
s=s.replace('const lvlMatch = lvlHeader.match(/(?:level|lvl)\\s*(\\d+)/i);','const lvlMatch = lvlBlock.match(/\\[difficulty::\\s*(\\d+)\\]/i);')
w.write(p,s)

base=w.find('01_Difficulty');original=base.read_text(encoding='utf-8');code=re.search(r'```dataviewjs\n(.*?)\n```',original,re.S)[1]
a=code.index('// --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---')
code='''// Parameters and semantic dependencies come from the Markdown wrapper.
const config = input || dv.current();
const requirePage = (link, label) => {
    const page = link && dv.page(link);
    if (!page) throw new Error("Отсутствует источник: " + label);
    return page.file.path;
};
const registryFiles = {};
for (const kind of ["items", "modules", "headwear", "consumables", "blueprints"]) {
    registryFiles[kind] = requirePage(config[kind + "_ref"], kind);
}
const coreFiles = {
    biomes: requirePage(config.biomes_ref, "biomes"),
    mobs: requirePage(config.mobs_ref, "mobs")
};
requirePage(config.sector_ref, "sector");
const targetBiomeId = String(config.biome_id || "").toLowerCase();
const targetLevel = String(Number(config.difficulty));
if (!targetBiomeId || !Number.isInteger(Number(config.difficulty)) || Number(config.difficulty) < 1) {
    throw new Error("Нужны явные biome_id и положительная целая difficulty");
}
const validLootTags = ["item", "weapon", "armor", "module", "headwear", "consumable", "blueprint", "key", "merit", "artifact"];

'''+code[a:]
code=code.replace('if (!page) return [];','if (!page) throw new Error("Отсутствует источник: " + path);')
code=code.replace('await parseFileBlocks(path, /^### /m)','await parseFileBlocks(path, /^#{2,3} /m)')
code=code.replace('if (diffId === targetLevel)', 'if (diffId !== null && String(Number(diffId)) === targetLevel)')
code=code.replace('// 2. Загрузка мобов и их лута','''// Weapon variants are authored on entity pages, not copied into the family registry.
for (const frame of dv.pages().where(p => p.type === "entity" && p.entity_kind === "weapon_frame" && p.status === "active")) {
    const content = await dv.io.load(frame.file.path);
    if (frame.frame_id) itemMap[String(frame.frame_id)] = String(frame.file.link);
    for (const block of content.split(/^### /m).slice(1)) {
        const id = parseTagId(block, "instance_id");
        if (id) itemMap[id] = `[[${frame.file.path}#${block.split("\\n")[0].trim()}]]`;
    }
}
// 2. Загрузка мобов и их лута''')
code=code[:code.index('if (!foundData) {')]+'''if (!foundData) {
    dv.paragraph(`⚠️ Нет данных для biome_id=${targetBiomeId}, difficulty=${targetLevel}. Проверьте properties и записи источника биомов.`);
}
'''
w.write(R/'tools/dataview/sector_difficulty/view.js',code)
for i in range(1,4):
 p=w.find(f'{i:02}_Difficulty')
 sources=['Registry_Biomes','Registry_Mobs','Registry_Items','Registry_Thermos_Modules','Registry_Headwear','Registry_Consumables','Registry_Blueprints','Registry_Weapons','00_Port_Manifest']
 fm={'type':'view','status':'active','system':'world_atlas','view_kind':'sector_difficulty','difficulty':i,'biome_id':'port','sector_ref':w.ref('00_Port_Manifest'),'upstream_sources':[w.ref(x) for x in sources]}
 for key,stem in [('items','Registry_Items'),('modules','Registry_Thermos_Modules'),('headwear','Registry_Headwear'),('consumables','Registry_Consumables'),('blueprints','Registry_Blueprints'),('biomes','Registry_Biomes'),('mobs','Registry_Mobs')]:fm[key+'_ref']=w.ref(stem)
 w.write(p,'---\n'+'\n'.join(k+': '+json.dumps(v,ensure_ascii=False) for k,v in fm.items())+'\n---\n\n# Ржавый Порт: сложность '+str(i)+'\n\nПроизводная таблица среды, встреч и связанной добычи. Канон читается из `upstream_sources`; таблица не определяет состав рейда и не гарантирует выпадение предмета. Номер сложности задан в properties.\n\n```dataviewjs\nawait dv.view("tools/dataview/sector_difficulty", dv.current());\n```\n')

# This calibration note contains copied values/formulas AND unique validation requirements.
# Keep the test contract as an owner; turn only the reading table into a projection.
p=w.find('Item_Calibration_Matrix');s=p.read_text(encoding='utf-8');a,b=w.section(s,'## 3. Текущие Известные Значения Стартового Набора');s=s[:a]+s[b:]
a=s.index('```text',s.index('## 4. Проверка Access Readiness'));b=s.index('```',a+3)+3
s=s[:a]+'Расчёты выполняются по '+w.ref('08_Gate_Check')+', '+w.ref('Dissonance_System')+' и '+w.ref('Threat_Thresholds')+'. Эта проверка читает результаты владельцев; собственных формул защиты или давления у неё нет.'+s[b:]
s=s.replace('Эта матрица является обязательным промежуточным слоем между реестрами предметов и балансными порогами.','Этот контракт задаёт состав проверяемых комплектов и вопросы калибровки. Он не владеет значениями предметов, защитой, давлением или правилами входа.')
s=s.replace('## 2. Обязательные Поля','## 2. Поля отчёта калибровки').replace('Каждый предмет, влияющий на вход в рейд или его экономику, должен иметь:','Для каждого предмета, влияющего на вход в рейд или экономику, отчёт собирает применимые поля из его владельцев:')
q=R/'07_Gear_Inventory/Calibration_Contract.md';w.write(q,s.replace('# Матрица Калибровки Предметов','# Контракт калибровки комплектов',1));w.owner(q)
w.write(p,'---\ntype: view\nstatus: active\nsystem: gear_balance\nview_kind: item_calibration\nupstream_sources: '+json.dumps([w.ref('Calibration_Contract'),w.ref('Registry_Items'),w.ref('Registry_Thermoses'),w.ref('Registry_Thermos_Modules'),w.ref('Registry_Weapons'),w.ref('Registry_Consumables'),w.ref('Registry_Headwear')],ensure_ascii=False)+'\n---\n\n# Калибровка: источники и пробелы\n\nПроизводная карта готовности предметных источников. Состав тестовых комплектов, поля отчёта и критерии проверки принадлежат '+w.ref('Calibration_Contract')+'. Значения читаются по ссылкам ниже: копия стартового набора здесь не хранится. `UNKNOWN` и `blocked_calibration` не означают нулевую цену или нулевой вклад.\n\n```dataview\nTABLE WITHOUT ID file.link AS "Источник", registry_type AS "Семейство", status AS "Канон"\nWHERE type = "registry" AND (registry_type = "thermos_models" OR registry_type = "thermos_modules" OR registry_type = "weapon_frames" OR registry_type = "items" OR registry_type = "consumables")\n```\n\n'+w.ref('Registry_Headwear')+'; '+w.ref('Registry_Items')+'; '+w.ref('Registry_Consumables')+'.\n')
print('Preserved graphs and biome table; three difficulty wrappers share one algorithm; calibration values no longer copied')
