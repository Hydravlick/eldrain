---
type: registry
status: active
system: gear_inventory_registry
registry_type: thermos_models
tags:
  - thermos
  - body_base
  - slots
  - dataview
related_files:
  - "[[07_Gear_Inventory/Thermos_System|Thermos_System]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Thermos_Modules|Registry_Thermos_Modules]]"
  - "[[07_Gear_Inventory/Equipment_PaperDoll|Equipment_PaperDoll]]"
---
# Реестр моделей Термосов

Реестр хранит только физические основы: посадку, число и расположение узлов, собственный вес и конструктивные особенности. Профильные ёмкости принадлежат Пешке, а эффекты — установленным модулям.

## Поля

- `[thermos_id:: ...]` — стабильный ID модели;
- `[tier:: ...]` — класс конструкции, не число слотов и не Gear Score;
- `[slot_count:: ...]` — физическое число узлов;
- `[slot_layout:: ...]` — доступные позиции через `|`;
- `[fit_system:: eldrain_modular]` — возможность мастерской перенастройки;
- `[fit_profiles:: ...]` — поддерживаемые либо перенастраиваемые морфологии;
- `[base_traits:: ...]` — конструктивные особенности без модульного эффекта;
- `[weight:: ...]`, `[value:: ...]`, `[balance_state:: ...]` — калибровка.

## Dataview: модели

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
    const id = field(block, "thermos_id");
    if (!id || id === "template_thermos") return null;
    return [
        "[[" + registryPath + "#" + header + "|" + header + "]]",
        field(block, "tier") || "UNKNOWN",
        field(block, "slot_count") || "UNKNOWN",
        (field(block, "slot_layout") || "UNKNOWN").replaceAll("|", ", "),
        field(block, "fit_profiles") || "UNKNOWN",
        field(block, "weight") || "UNKNOWN",
        field(block, "balance_state") || "unknown"
    ];
}).filter(Boolean);

if (rows.length) {
    dv.table(["Модель", "Tier", "Слоты", "Позиции", "Посадка", "Вес", "Баланс"], rows);
} else {
    dv.paragraph("⚠️ В Registry_Thermoses пока нет активных моделей.");
}
```

---

### Городской серийный Термос
[thermos_id:: civic_standard]
[tier:: 1]
[slot_count:: UNKNOWN]
[slot_layout:: UNKNOWN]
[fit_system:: eldrain_modular]
[fit_profiles:: refittable]
[base_traits:: repairable_conduit, optional_alarm_thread]
[weight:: UNKNOWN]
[value:: civic_issue]
[balance_state:: unknown]

Простая городская основа, доступная через Право на Первую Кладку. Мастерская подгоняет её под тело и задачу, но модель не выдаётся вместе с защитными модулями.

---

### Шаблон Термоса
[thermos_id:: template_thermos]
[tier:: 1]
[slot_count:: UNKNOWN]
[slot_layout:: chest|shoulder]
[fit_system:: eldrain_modular]
[fit_profiles:: refittable]
[base_traits:: none]
[weight:: UNKNOWN]
[value:: UNKNOWN]
[balance_state:: unknown]

Краткое описание назначения модели и её физической топологии.
