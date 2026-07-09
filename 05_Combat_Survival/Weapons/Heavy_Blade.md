---
type: weapon_frame
status: active
system: combat_survival
frame_id: heavy_blade
display_name: Тяжёлое лезвие
weapon_family: blade
frame_vector: shadow
vector_scope: commitment
activates_on: [swing, cleave_recovery]
primary_window_function: exploit
creates_window: [soft_zone_exposed]
exploits_window: [soft_zone_exposed]
mitigates_window: [none]
exposure_channels: [whiff_recovery, armor_check, noise]
frame_power: 3
exposure_weight: 3
implicit_keyword: maim
implicit_rule: "Повторный рубящий контакт по уже раскрытой мягкой зоне усиливает травму и замедляет отход цели."
mastery_unlock: [cleave_chain_control]
mvp_verdict: specialist
mvp_reason: "Хорошо показывает физику траектории и стены, но как главный MVP уводит в обычное фентези."
sort_order: 120
tags: [weapon_frame, weapons, blade]
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Тяжёлое лезвие

Тяжёлое лезвие ставит на широкое движение и мягкие зоны. Оно хорошо добирает цель, которая уже раскрылась, но платит шумом, recovery и плохой работой по твёрдой пластине.

## Варианты

### Мачете / Тесак (Cleaver) [1H]
[variant_id:: cleaver] | [tier:: 1] | [weight:: 1.5kg] | [dmg:: 35] | [setting_status:: mvp]
[combo_chain:: chop -> drag cut -> committed cleave] | [alt_action:: shoulder check]
[combo_reset:: пауза после Ready возвращает цепочку к chop]

*Тяжёлое лезвие со смещённым центром тяжести.*
- **Отличие:** простая проверка стен, мягких целей и recovery.
- **Implicit:** `maim` награждает за уже созданное окно, а не за рубку брони в лоб.
- **Слабость:** заметный recovery после промаха и плохая работа по твёрдой пластине.

### Рельсовая мачета (Rail Machete) [1H]
[variant_id:: rail_machete] | [tier:: 1] | [weight:: 1.9kg] | [dmg:: 38] | [setting_status:: prototype]
[combo_chain:: low hack -> rising hook -> overcommit chop] | [alt_action:: wedge pry]
[combo_reset:: удар о стену или пластину возвращает цепочку к low hack]

*Снятый с ремонтной тележки кусок рельсового резака с грубой рукоятью.*
- **Отличие:** лучше цепляет ткань, ремни и тонкие перегородки, но тяжелее на переносе.
- **Implicit:** `maim` проявляется как удержание цели в плохом состоянии, а не как чистый burst.
- **Слабость:** шум и вес быстро выдают ближний бой.

### Цеховой серпорез (Shop Reaper) [2H]
[variant_id:: shop_reaper] | [tier:: 2] | [weight:: 3.2kg] | [dmg:: 44] | [setting_status:: prototype]
[combo_chain:: setup sweep -> cloth bite -> pull-through cut] | [alt_action:: haft shove]
[combo_reset:: потеря угла сбрасывает цепочку к setup sweep]

*Полуинструмент для разделки плотных материалов, переделанный под бой.*
- **Отличие:** лучше работает по толпе мягких целей, но требует пространства.
- **Implicit:** `maim` полезен после контроля маршрута или чужого stagger.
- **Слабость:** в узком коридоре сам становится источником whiff_recovery.
