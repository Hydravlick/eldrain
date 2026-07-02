---
type: registry
status: active
system: gear_inventory_registry
registry_type: attire
tags:
  - attire
  - wearable_loot
  - culture
  - dataview
related_files:
  - "[[07_Gear_Inventory/Civic_Attire|Civic_Attire]]"
  - "[[07_Gear_Inventory/Thermos_System|Thermos_System]]"
  - "[[02_World_Lore/Hedgehog_Culture|Hedgehog_Culture]]"
  - "[[02_World_Lore/Rat_Culture|Rat_Culture]]"
  - "[[02_World_Lore/Toad_Culture|Toad_Culture]]"
  - "[[02_World_Lore/Squirrel_Culture|Squirrel_Culture]]"
  - "[[02_World_Lore/Lizard_Culture|Lizard_Culture]]"
---
# Реестр мирской одежды

Этот реестр хранит носимые ценности, которые занимают Body Base, но не являются бронёй. Культурное происхождение описывает язык вещи, а native_fit — тело, под которое она действительно скроена. Несовместимый наряд нельзя надеть без уничтожающего исходную форму перешива.

## Поля

- [attire_id:: ...] — стабильный ID;
- [attire_type:: everyday|ceremonial|heirloom|stage] — назначение;
- [cultural_origin:: ...] — культурная традиция;
- [native_fit:: ...] — совместимая морфология Пешки;
- [body_adaptation:: ...] — исходная телесная посадка;
- [cut_module:: ...] — единственный выход необратимого перешива;
- [module_axis:: ...] — допустимая игровая ось модуля Термоса;
- [signature_tags:: ...] — только фактическая заметность через |;
- [value_axes:: ...] — основания оценки через |;
- [right_rule:: source_context] — право определяется местом, владельцем и контрактом;
- [body_slot:: body_base], [armor_profile:: none], [environment_profile:: none] — обязательная граница с Термосом и его модулями;
- [balance_state:: unknown] — числовая ценность не установлена.

## Dataview: сводка одежды

```dataviewjs
const registryPath = dv.current().file.path;
const content = await dv.io.load(registryPath);
const blocks = content.split(/^### /m).slice(1);

function field(block, key) {
    const match = block.match(new RegExp("\\[" + key + "::\\s*([^\\]]+)\\]", "i"));
    return match ? match[1].trim() : "";
}

const rows = blocks.map(block => {
    const header = block.split("\n")[0].trim();
    const attireId = field(block, "attire_id");
    if (!attireId || attireId === "template_attire") return null;
    return [
        "[[" + registryPath + "#" + header + "|" + header + "]]",
        field(block, "attire_type") || "—",
        field(block, "cultural_origin") || "—",
        field(block, "native_fit") || "—",
        field(block, "cut_module") || "—",
        field(block, "module_axis") || "—",
        field(block, "signature_tags").replaceAll("|", ", ") || "—",
        field(block, "value_axes").replaceAll("|", ", ") || "—",
        field(block, "balance_state") || "—"
    ];
}).filter(Boolean)
  .sort((a, b) => a[2].localeCompare(b[2]) || a[0].localeCompare(b[0]));

if (rows.length) {
    dv.table(["Наряд", "Тип", "Происхождение", "Посадка", "Cut Module", "Ось модуля", "Заметность", "Ценность", "Баланс"], rows);
} else {
    dv.paragraph("⚠️ В Registry_Attire нет активных записей.");
}
```

---

### Ночная накидка с кольцами
[attire_id:: night_ring_mantle]
[attire_type:: ceremonial]
[cultural_origin:: hedgehog]
[native_fit:: hedgehog]
[body_adaptation:: detachable_spine_drape]
[cut_module:: spine_safe_drape]
[module_axis:: mobility]
[signature_tags:: visual_high|acoustic_low]
[value_axes:: craft|cultural_address]
[right_rule:: source_context]
[body_slot:: body_base]
[armor_profile:: none]
[environment_profile:: none]
[portability:: cargo]
[balance_state:: unknown]

Тонкая накидка закрывает иглы полупрозрачными складками; съёмные кольца и ленты позволяют владельцу самому выбрать, сколько тела станет частью наряда.

- **Сенсорный признак:** кольца тихо касаются друг друга только при широком развороте корпуса.
- **После находки:** старые мастера спорят, была ли эта вещь парадной или вызывающе повседневной.
- **Основа:** [[02_World_Lore/Hedgehog_Culture#Одежда|ежиная одежда]].

### Куртка датированных швов
[attire_id:: dated_seam_coat]
[attire_type:: heirloom]
[cultural_origin:: rat]
[native_fit:: rat]
[body_adaptation:: tail_harness_cut]
[cut_module:: dated_replaceable_sections]
[module_axis:: support]
[signature_tags:: visual_low|acoustic_low]
[value_axes:: provenance|personal_memory|craft]
[right_rule:: source_context]
[body_slot:: body_base]
[armor_profile:: none]
[environment_profile:: none]
[portability:: cargo]
[balance_state:: unknown]

На внутренней стороне куртки каждый значимый ремонт отмечен своей строчкой и датой; снаружи вещь выглядит почти нарочито простой.

- **Сенсорный признак:** очищенная подкладка всё ещё удерживает запах травяного масла.
- **После находки:** без имени владельца швы доказывают возраст, но не право на продажу.
- **Основа:** [[02_World_Lore/Rat_Culture#Одежда|крысиная одежда]].

### Сухой праздничный плащ
[attire_id:: dry_festival_cloak]
[attire_type:: ceremonial]
[cultural_origin:: toad]
[native_fit:: toad]
[body_adaptation:: ventilated_skin_cut]
[cut_module:: moisture_exchange_lining]
[module_axis:: environment]
[signature_tags:: visual_high|scent_high]
[value_axes:: craft|cultural_address|provenance]
[right_rule:: source_context]
[body_slot:: body_base]
[armor_profile:: none]
[environment_profile:: none]
[portability:: cargo]
[balance_state:: unknown]

Лёгкий плащ держит преувеличенно сухую форму, застёгивается расписной керамикой и сохраняет след яркой пудры на воротнике.

- **Сенсорный признак:** искусственный цветочный запах перебивает даже старую сырость.
- **После находки:** молодые Жабы смеются, что такую вещь наверняка носили назло старшим; старшие не подтверждают.
- **Основа:** [[02_World_Lore/Toad_Culture#Одежда|жабья одежда]].

### Плащ закрытых кладок
[attire_id:: closed_cache_cloak]
[attire_type:: heirloom]
[cultural_origin:: squirrel]
[native_fit:: squirrel]
[body_adaptation:: quick_release_tail_cut]
[cut_module:: quick_release_thermal_layer]
[module_axis:: mobility]
[signature_tags:: visual_medium|acoustic_low]
[value_axes:: provenance|personal_memory|cultural_address]
[right_rule:: source_context]
[body_slot:: body_base]
[armor_profile:: none]
[environment_profile:: none]
[portability:: cargo]
[balance_state:: unknown]

Яркая внешняя ткань скрывает под клапанами семейные знаки и маленькие пустые карманы, назначение которых полагалось знать только дому.

- **Сенсорный признак:** при раскрытии подкладки пахнет сухими семенами и тёплой древесиной.
- **После находки:** оценщик видит дорогой крой, но настоящий адрес вещи может находиться среди тех, кто узнает внутреннюю кладку.
- **Основа:** [[02_World_Lore/Squirrel_Culture#Одежда|беличья одежда]].

### Глазурный вечерний покров
[attire_id:: glazed_evening_veil]
[attire_type:: stage]
[cultural_origin:: lizard]
[native_fit:: lizard]
[body_adaptation:: diagnostic_skin_frame]
[cut_module:: thermal_privacy_frame]
[module_axis:: stealth]
[signature_tags:: visual_high|thermal_distortion]
[value_axes:: craft|cultural_address]
[right_rule:: source_context]
[body_slot:: body_base]
[armor_profile:: none]
[environment_profile:: none]
[portability:: cargo]
[balance_state:: unknown]

Полупрозрачные и глухо окрашенные панели чередуются так, чтобы владелец сам определял, какие участки кожи становятся частью публичного образа.

- **Сенсорный признак:** глазурь меняет оттенок при тепле ладони, но не раскрывает состояние тела под ней.
- **После находки:** без владельца невозможно понять, был ли покров сценическим образом, модой или просьбой не читать его реакцию.
- **Основа:** [[02_World_Lore/Lizard_Culture#Одежда и видимая кожа|ящеричная одежда]].

---

### Шаблон мирской одежды
[attire_id:: template_attire]
[attire_type:: everyday]
[cultural_origin:: mixed]
[native_fit:: body_profile_id]
[body_adaptation:: standard]
[cut_module:: cut_module_id]
[module_axis:: module_axis]
[signature_tags:: visual_low|acoustic_low]
[value_axes:: craft]
[right_rule:: source_context]
[body_slot:: body_base]
[armor_profile:: none]
[environment_profile:: none]
[portability:: cargo]
[balance_state:: unknown]

Короткое описание вещи, её прежней жизни и причины сохранить целой.

- **Сенсорный признак:** материал, запах, звук или телесная посадка.
- **После находки:** адрес, спор о происхождении или неполное местное толкование.
- **Основа:** ссылка на точный раздел культурной заметки.
