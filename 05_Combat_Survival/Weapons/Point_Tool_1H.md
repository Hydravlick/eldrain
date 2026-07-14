---
type: weapon_frame
status: active
system: combat_survival
frame_id: point_tool_1h
display_name: Линейный пробойник, одна рука
weapon_family: blade
grip: one_hand
skill_interfaces: [point, contact_surface, free_hand]
activates_on: [thrust, line_hold, precision_recovery]
commitment: fixed_thrust_line_until_withdrawal
primary_window_function: exploit
creates_window: [none]
implicit_keyword: seam_point
implicit_rule: Узкая рабочая точка требует видимой линии к стыку, щели или мягкой зоне; пластина и боковой обход сохраняют контригру.
exploits_window: [joint_exposed, soft_zone_exposed]
mitigates_window: [none]
exposure_channels: [line_commit, shield_angle, armor_check]
mastery_unlock: [seam_followup, measured_withdraw]
sort_order: 120
tags: [weapon_frame, melee, blade, one_hand]
related_files:
  - "[[05_Combat_Survival/Weapon_Melee|Weapon_Melee]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Линейный пробойник, одна рука

Фрейм проверяет точность линии, а не «фехтовальный класс». Его точка полезна там, где игрок уже прочитал стык защиты или узкий проход между телом и укрытием.

## Экземпляры

### Шовный щуп [1H]
[instance_id:: seam_probe]
[load_tier:: 1]
[rarity_band:: rusty..uncommon]
[origin_kind:: local_sector]
[origin_function:: проверка течи и ремонтных швов портовой сети]
[spawn_profile:: maintenance_locker]
[moveset_profile:: Probe -> Measured Thrust -> Withdraw]
[commitment_cost:: длинный укол фиксирует направление и проигрывает обходу]
[handedness:: one_hand]
[combo_chain:: Probe -> Measured Thrust -> Withdraw]
[alt_action:: Wall Brace]
[combo_reset:: пауза после Ready возвращает к Probe]

Рабочий щуп сохранил тонкую прямую линию: он проходит в узком коридоре, но не останавливает тяжёлую цель и не заменяет ударник.

### Прививочное шило [1H]
[instance_id:: grafting_awl]
[load_tier:: 1]
[rarity_band:: uncommon..rare]
[origin_kind:: foreign_snapshot]
[origin_function:: работа с живыми стеблями и защитными оболочками]
[spawn_profile:: source_garden_cache]
[moveset_profile:: Angle Test -> Deep Set -> Side Withdraw]
[commitment_cost:: глубокая постановка требует точного угла и создаёт долгий выход из контакта]
[handedness:: one_hand]
[combo_chain:: Angle Test -> Deep Set -> Side Withdraw]
[alt_action:: Twist Release]
[combo_reset:: пауза после Ready возвращает к Angle Test]

У экземпляра другой ритм руки: он проверяет угол перед глубоким уколом. Сила возникает из подготовленной точки, а не из критического множителя по умолчанию.
