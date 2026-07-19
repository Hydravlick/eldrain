---
type: weapon_frame
status: active
system: combat_survival
frame_id: needle_thrower_2h
display_name: Игольный метатель, две руки
weapon_family: arcanegun
grip: two_hand
skill_interfaces: [projectile, reach]
activates_on: [wind, aim_hold, release, wind_recovery]
commitment: full_wind_and_fixed_rewind_between_shots
primary_window_function: exploit
creates_window: [none]
implicit_keyword: quiet_puncture
implicit_rule: Механический метатель выпускает тихую узкую иглу по мягкой зоне, но платит долгим взводом, малым контролем тяжёлой цели и зависимостью от чистой линии.
exploits_window: [soft_zone_exposed, concealment]
mitigates_window: [none]
exposure_channels: [slow_wind, armor_check, low_stagger]
mastery_unlock: [quiet_rewind, measured_release]
sort_order: 450
tags: [weapon_frame, ranged, arcanegun, two_hand, mechanical]
related_files:
  - "[[05_Combat_Survival/Weapon_Ranged|Weapon_Ranged]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Игольный метатель, две руки

Механический дальний фрейм не расходует батарею, но не получает её повторяемость. Взвод — его видимый долг, а не техническая пауза между одинаковыми выстрелами.

## Экземпляры

### Пробоотборный метатель [2H]
[instance_id:: sample_dart_thrower]
[load_tier:: 1]
[rarity_band:: rusty..rare]
[origin_kind:: local_sector]
[origin_function:: безопасный отбор биологических и водных проб]
[spawn_profile:: sanitary_station_cache]
[moveset_profile:: Wind -> Quiet Release -> Fixed Rewind]
[commitment_cost:: после выпуска владелец остаётся на месте, пока взводит следующую иглу]
[handedness:: two_hand]
[energy_mode:: mechanical]
[emission_profile:: single quiet dart]
[cadence_gate:: full_rewind]
[fire_input:: Tap]
[reload_mechanic:: single mechanical rewind]

Игла даёт шанс тихо использовать открытую мягкую зону, но не останавливает тяжёлую цель и не заменяет магострел на открытой линии.

### Кронный посыльный [2H]
[instance_id:: canopy_message_thrower]
[load_tier:: 1]
[rarity_band:: uncommon..rare]
[origin_kind:: foreign_snapshot]
[origin_function:: доставка меток и тонких тросов между верхними маршрутами]
[spawn_profile:: source_route_cache]
[moveset_profile:: High Aim -> Line Dart -> Long Rewind]
[commitment_cost:: высокий выстрел требует неподвижности и выдаёт силуэт на верхнем маршруте]
[handedness:: two_hand]
[energy_mode:: mechanical]
[emission_profile:: line-marking dart]
[cadence_gate:: long_rewind]
[fire_input:: Hold to Aim -> Release]
[reload_mechanic:: single mechanical rewind]

Экземпляр лучше работает с вертикальной линией, но получает ещё более долгую подготовку и не становится скорострельным игольником.
