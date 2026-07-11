---
type: registry
status: active
system: gear_inventory_registry
registry_type: thermos_modules
tags:
  - thermos
  - modules
  - protection
  - utility
  - dataview
related_files:
  - "[[07_Gear_Inventory/Thermos_System|Thermos_System]]"
  - "[[07_Gear_Inventory/_Registries/Registry_Thermoses|Registry_Thermoses]]"
  - "[[07_Gear_Inventory/Gear_Progression|Gear_Progression]]"
  - "[[05_Combat_Survival/Magic_Batteries|Magic_Batteries]]"
---
> [!TODO] Калибровка модулей
> - [ ] Разложить существующие многозонные пакеты со статусом `blocked_calibration` на отдельные устанавливаемые модули с подтверждёнными `slot_size` и физическими позициями.
> - [ ] Назначить `module_cost` только после проверки Welfare, Balanced, Armor Rat и гибридных сборок.
> - [ ] Добавить оптические, герметизирующие и чисто утилитарные модули; текущий набор унаследован от броневого реестра.
> - [ ] Для линий Чужой воды добавить проверяемые взаимодействия без комплекта полной иммунности.

# Реестр модулей Термоса

Реестр хранит устанавливаемые функции. Модуль может быть пластиной, оптикой, герметизацией, проводящей ветвью, обвязкой, плетением или гибридом нескольких семейств.

## Поля

- `[module:: ...]` и `[module_id:: ...]` — стабильный ID для лута и реестра;
- `[module_families:: ...]` — семейства через `|`;
- `[module_cost:: family value, ...]` — раздельная цена по каждому семейству;
- `[slot_size:: ...]` — занятые физические слоты;
- `[module_positions:: ...]` — допустимые позиции через `|`;
- `[tier:: ...]` — класс конструкции, не автоматическая стоимость;
- `[rarity:: ...]` — настройки экземпляра, не автоматическая стоимость;
- `[module_axes:: ...]` — фактические игровые оси;
- `[body_interface:: ...]` — тип Опорного контура либо `none`; это не семейство;
- `[touch_shift:: ...]` — фиксированный сдвиг первичного T.O.U.C.H. только активного контура;
- `[doctrine_exchange:: ...]` — ситуативное устройство меняет один названный конечный результат и показывает цену; оно не меняет T.O.U.C.H.;
- `[vulnerability:: ...]` — наблюдаемая цена усиления;
- `[interface_state:: inactive|active]` — работает ли `touch_shift` на текущей сборке;
- `[armor_plates:: ...]` — защищаемые зоны либо `none`;
- `[soft_coverage:: ...]` — мягкий слой, остающийся между пластинами либо `none`;
- `[seam_exposure:: ...]` — видимые стыки и открытые направления либо `none`;
- `[collision_silhouette:: ...]` — читаемое обещание формы коллайдера либо `none`;
- `[install_state:: installable|blocked_calibration]` — допущен ли модуль к сборке;
- `[install_location:: hub_professional]` — единственный обычный монтаж;
- `[field_state:: stitched_locked]` — в Аномалии сборка заблокирована.

Функциональный модуль обязан иметь положительный `module_cost` хотя бы в одном семействе. Гибрид платит каждую цену отдельно.

Мастер показывает только записи с `install_state:: installable`. Любой `UNKNOWN` в `slot_size`, `module_cost` или физических позициях автоматически блокирует монтаж. Устанавливаемая пластина также требует непустые `armor_plates`, `soft_coverage`, `seam_exposure`, `collision_silhouette`, вес, уязвимость и не-`unknown` состояние калибровки. Многозонный пакет со статусом `blocked_calibration` остаётся источником визуальной и лутовой концепции, но не считается одной устанавливаемой навеской и не участвует в расчёте сборки.

## Dataview: сводка модулей

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
    const id = field(block, "module_id");
    if (!id || id === "template_thermos_module") return null;
    return [
        "[[" + registryPath + "#" + header + "|" + header + "]]",
        (field(block, "module_families") || "UNKNOWN").replaceAll("|", ", "),
        field(block, "module_cost") || "UNKNOWN",
        field(block, "slot_size") || "UNKNOWN",
        (field(block, "module_positions") || "UNKNOWN").replaceAll("|", ", "),
        field(block, "tier") || "UNKNOWN",
        (field(block, "module_axes") || "UNKNOWN").replaceAll(",", ", "),
        field(block, "body_interface") || "none",
        field(block, "touch_shift") || "none",
        field(block, "vulnerability") || "none",
        (field(block, "armor_plates") || "none").replaceAll(",", ", "),
        field(block, "weight") || "UNKNOWN",
        field(block, "install_state") || "blocked_calibration",
        field(block, "balance_state") || "unknown"
    ];
}).filter(Boolean)
  .sort((a, b) => a[1].localeCompare(b[1]) || a[0].localeCompare(b[0]));

if (rows.length) {
    dv.table(["Модуль", "Семейства", "Стоимость", "Слоты", "Позиции", "Tier", "Оси", "Контур", "T.O.U.C.H.", "Уязвимость", "Покрытие", "Вес", "Допуск", "Баланс"], rows);
} else {
    dv.paragraph("⚠️ В Registry_Thermos_Modules нет активных модулей.");
}
```

---

## Пластинчатые модули

### Навеска «Базальт»
[module:: basalt_shell]
[module_id:: basalt_shell]
[module_families:: plate]
[module_cost:: plate UNKNOWN]
[slot_size:: UNKNOWN]
[module_positions:: chest|arms|shoulders|shins]
[tier:: 2]
[rarity:: UNKNOWN]
[module_axes:: coverage, cargo]
[armor_plates:: chest, arm_guards, shoulder_pads, shin_guards]
[environment_resistance:: 55]
[conduit_layout:: segmented_fuses]
[weight:: 22kg]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: unknown]

Грубые керамические сегменты распределяются по нескольким узлам Термоса. Точная цена слотов и пластинчатой ёмкости требует разложения пакета на физические части.

### Сборка «Хранитель Очага»
[module:: hearth_keeper]
[module_id:: hearth_keeper]
[module_families:: plate|seal|conduit]
[module_cost:: plate UNKNOWN, seal UNKNOWN, conduit UNKNOWN]
[slot_size:: UNKNOWN]
[module_positions:: chest|shoulders|thighs]
[tier:: 3]
[rarity:: UNKNOWN]
[module_axes:: coverage, environment, energy]
[armor_plates:: l_shoulder, r_shoulder, thighs, chest_center]
[environment_resistance:: 70]
[conduit_layout:: frontal_manifold]
[weight:: 18kg]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: unknown]

Фронтальная гибридная навеска соединяет плиты, герметизацию и распределитель. Она не считается одной бесплатной функцией только потому, что собрана в один узнаваемый пакет.

## Обвязки

### Сбруя «Наёмник»
[module:: mercenary_rig]
[module_id:: mercenary_rig]
[module_families:: plate|rig]
[module_cost:: plate UNKNOWN, rig UNKNOWN]
[slot_size:: UNKNOWN]
[module_positions:: chest|forearms|waist]
[tier:: 2]
[rarity:: UNKNOWN]
[module_axes:: mobility, support]
[armor_plates:: upper_chest, stomach, forearms]
[environment_resistance:: 35]
[conduit_layout:: bracer_branch]
[weight:: 12kg]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: unknown]

Кожаная обвязка с керамическими чешуйками соединяет защиту корпуса и рабочие наручи.

### Обвязка «Собиратель»
[module:: scavenger_wrap]
[module_id:: scavenger_wrap]
[module_families:: plate|rig]
[module_cost:: plate UNKNOWN, rig UNKNOWN]
[slot_size:: UNKNOWN]
[module_positions:: chest|waist|back]
[tier:: 1]
[rarity:: UNKNOWN]
[module_axes:: mobility, cargo]
[armor_plates:: chest_heart]
[environment_resistance:: 15]
[conduit_layout:: single_heart_loop]
[weight:: 6kg]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: unknown]

Единственная плита прикрывает сердце, а остальная конструкция распределяет переносимый груз. Обвязка не создаёт универсальные карманы: её Cargo-функция обязана быть описана отдельно.

## Проводники и плетение

### Эфирная ветвь «Проводник»
[module:: conduit_robe]
[module_id:: conduit_robe]
[module_families:: conduit|weave]
[module_cost:: conduit UNKNOWN, weave UNKNOWN]
[slot_size:: UNKNOWN]
[module_positions:: spine|shoulder|collar]
[tier:: 2]
[rarity:: UNKNOWN]
[module_axes:: energy, cantrip]
[armor_plates:: r_shoulder, back_spine]
[environment_resistance:: 40]
[conduit_layout:: spine_branch]
[weight:: 3kg]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: unknown]

Эфирное полотно подключается вдоль позвоночной ветви, а сменный воротник принимает кристаллы и аварийный разрыв.

### Вуали «Призрак»
[module:: wraith_veils]
[module_id:: wraith_veils]
[module_families:: weave]
[module_cost:: weave UNKNOWN]
[slot_size:: UNKNOWN]
[module_positions:: shoulders|back|waist]
[tier:: 1]
[rarity:: UNKNOWN]
[module_axes:: mobility, stealth]
[armor_plates:: none]
[environment_resistance:: 20]
[conduit_layout:: diffused_threads]
[weight:: 2kg]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: unknown]

Дымчатые слои меняют движение и силуэт Термоса, но не изображают отсутствующую пластину.

## Prototype: Опорные контуры

Эти десять модулей фиксируют два разных обмена для каждого атрибута. Они заблокированы для монтажа до калибровки полных комплектов; числа являются проверяемыми prototype anchors, а не активным лутовым пулом.

### Противовесное ярмо
[module:: counterweight_yoke]
[module_id:: counterweight_yoke]
[module_families:: rig]
[module_cost:: rig 2]
[slot_size:: 2]
[module_positions:: back|shoulders]
[tier:: 1]
[rarity:: common]
[module_axes:: mobility, cargo]
[armor_plates:: none]
[weight:: 8kg]
[body_interface:: load_bearing]
[touch_shift:: TRQ +2]
[vulnerability:: weight +8kg, turn_speed -10%]
[interface_state:: inactive]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: prototype]

Груз уходит за плечи и делает Пешку устойчивее, но каждый разворот приходится начинать всем корпусом.

### Пневматическая распорка
[module:: pneumatic_brace]
[module_id:: pneumatic_brace]
[module_families:: rig|conduit]
[module_cost:: rig 1, conduit 1]
[slot_size:: 1]
[module_positions:: chest|forearms]
[tier:: 2]
[rarity:: uncommon]
[module_axes:: mobility, energy]
[armor_plates:: none]
[weight:: 4kg]
[body_interface:: none]
[touch_shift:: none]
[doctrine_exchange:: brace_hold_limit normal -> extended; activation_heat 0 -> +10; movement_noise 0 -> +8]
[vulnerability:: heat_per_activation +10, movement_noise +8]
[interface_state:: inactive]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: prototype]

Поршни коротко запирают грудь и руки в несущую раму; шипение и жар выдают каждое включение.

### Тонкомоторная сбруя
[module:: fine_motor_harness]
[module_id:: fine_motor_harness]
[module_families:: rig|weave]
[module_cost:: rig 1, weave 1]
[slot_size:: 1]
[module_positions:: forearms|waist]
[tier:: 1]
[rarity:: common]
[module_axes:: support, mobility]
[armor_plates:: none]
[weight:: 2kg]
[body_interface:: motor_control]
[touch_shift:: GRP +1, TRQ -1]
[vulnerability:: TRQ -1]
[interface_state:: inactive]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: prototype]

Натяжные нити держат кисть в точном рабочем диапазоне, отнимая часть силового хвата.

### Сервосухожилие
[module:: servo_tendon]
[module_id:: servo_tendon]
[module_families:: rig|conduit]
[module_cost:: rig 1, conduit 1]
[slot_size:: 1]
[module_positions:: forearms]
[tier:: 2]
[rarity:: uncommon]
[module_axes:: support, energy]
[armor_plates:: none]
[weight:: 3kg]
[body_interface:: none]
[touch_shift:: none]
[doctrine_exchange:: device_interaction_time normal -> shorter; heat_per_interaction 0 -> +8; rigid_handwear compatible -> incompatible]
[vulnerability:: heat_per_interaction +8, rigid_handwear_incompatible]
[interface_state:: inactive]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: prototype]

Тонкие тяги ускоряют пальцы, пока контур питается, но не терпят жёстких перчаток и копят жар на повторе.

### Компрессионное плетение
[module:: compression_weave]
[module_id:: compression_weave]
[module_families:: weave]
[module_cost:: weave 2]
[slot_size:: 1]
[module_positions:: chest|waist]
[tier:: 1]
[rarity:: common]
[module_axes:: coverage, support]
[armor_plates:: none]
[weight:: 2kg]
[body_interface:: layer_support]
[touch_shift:: LYR +1]
[vulnerability:: stamina_recovery -10%]
[interface_state:: inactive]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: prototype]

Тугие слои удерживают тело собранным после удара, но мешают свободно дышать после рывка.

### Решётка рубцовых пластин
[module:: scar_plate_lattice]
[module_id:: scar_plate_lattice]
[module_families:: plate|weave]
[module_cost:: plate 1, weave 1]
[slot_size:: 2]
[module_positions:: chest|back]
[tier:: 2]
[rarity:: uncommon]
[module_axes:: coverage, mobility]
[armor_plates:: chest, back]
[weight:: 6kg]
[body_interface:: layer_support]
[touch_shift:: LYR +2]
[vulnerability:: weight +6kg, move_speed -8%]
[interface_state:: inactive]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: prototype]

Пластины тянут мягкие слои друг к другу и спасают целостность ценой тяжёлого шага.

### Проводящая коса
[module:: conductor_braid]
[module_id:: conductor_braid]
[module_families:: conduit|weave]
[module_cost:: conduit 1, weave 1]
[slot_size:: 1]
[module_positions:: spine|collar]
[tier:: 1]
[rarity:: common]
[module_axes:: energy, cantrip]
[armor_plates:: none]
[weight:: 1kg]
[body_interface:: thermal_conduction]
[touch_shift:: GLW +1]
[vulnerability:: dissonance_load +4]
[interface_state:: inactive]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: prototype]

Коса принимает часть внутреннего жара, но её ровный фон легче слышит Аномалия.

### Шунт перегрева
[module:: overheat_shunt]
[module_id:: overheat_shunt]
[module_families:: conduit]
[module_cost:: conduit 2]
[slot_size:: 1]
[module_positions:: spine|shoulder]
[tier:: 2]
[rarity:: uncommon]
[module_axes:: energy]
[armor_plates:: none]
[weight:: 2kg]
[body_interface:: none]
[touch_shift:: none]
[doctrine_exchange:: overload_threshold normal -> higher; cantrip_backlash_outcome normal -> +1 step; dissonance_pulse 0 -> +3]
[vulnerability:: cantrip_backlash_outcome +1 step, dissonance_pulse +3]
[interface_state:: inactive]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: prototype]

Шунт даёт телу больший рабочий накал, но каждый импульс становится больнее и заметнее.

### Усатая антенна
[module:: whisker_array]
[module_id:: whisker_array]
[module_families:: optic|weave]
[module_cost:: optic 1, weave 1]
[slot_size:: 1]
[module_positions:: collar|shoulder]
[tier:: 1]
[rarity:: common]
[module_axes:: detection, stealth]
[armor_plates:: none]
[weight:: 1kg]
[body_interface:: sensory_gain]
[touch_shift:: SNS +1]
[vulnerability:: dissonance_load +3]
[interface_state:: inactive]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: prototype]

Тонкие жилы ловят дрожь среды раньше кожи, но сами оставляют ровный сенсорный след.

### Сетка эхо-линз
[module:: echo_lens_mesh]
[module_id:: echo_lens_mesh]
[module_families:: optic|conduit]
[module_cost:: optic 1, conduit 1]
[slot_size:: 1]
[module_positions:: collar|chest]
[tier:: 2]
[rarity:: uncommon]
[module_axes:: detection, energy]
[armor_plates:: none]
[weight:: 2kg]
[body_interface:: none]
[touch_shift:: none]
[doctrine_exchange:: cue_lead normal -> earlier; injury_threshold normal -> lower; heat_warning false_positives none -> enabled]
[vulnerability:: LYR -1, heat_warning false_positives]
[interface_state:: inactive]
[install_state:: blocked_calibration]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: prototype]

Сетка усиливает слабые эхо-сигналы вместе с ложными тревогами и делает тело менее цельным под нагрузкой.

---

### Шаблон модуля Термоса
[module:: template_thermos_module]
[module_id:: template_thermos_module]
[module_families:: plate|conduit]
[module_cost:: plate 2, conduit 1]
[slot_size:: 1]
[module_positions:: chest]
[tier:: 1]
[rarity:: common]
[module_axes:: coverage, energy]
[body_interface:: none]
[touch_shift:: none]
[vulnerability:: none]
[interface_state:: inactive]
[armor_plates:: chest]
[environment_resistance:: UNKNOWN]
[conduit_layout:: none]
[weight:: UNKNOWN]
[install_state:: installable]
[install_location:: hub_professional]
[field_state:: stitched_locked]
[balance_state:: unknown]

Короткое описание функции, видимого признака и цены модуля.
