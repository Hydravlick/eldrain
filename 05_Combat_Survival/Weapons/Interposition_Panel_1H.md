---
type: weapon_frame
status: active
system: combat_survival
frame_id: interposition_panel_1h
display_name: Панель заслона, одна рука
weapon_family: accessory
grip: one_hand
frame_vector: kinetics
vector_scope: commitment
activates_on: [raise, brace, lower_recovery]
primary_window_function: mitigate
creates_window: [covered_transition]
implicit_keyword: narrow_interposition
implicit_rule: Панель закрывает один выбранный угол на коротком переходе, но занимает руку, обзор и бок; она не даёт неподвижной полной неуязвимости.
exploits_window: [none]
mitigates_window: [ranged_line, melee_entry]
exposure_channels: [flank, low_mobility, open_side, lower_recovery]
mastery_unlock: [angle_shift, measured_lower]
sort_order: 610
tags: [weapon_frame, accessory, one_hand]
related_files:
  - "[[05_Combat_Survival/Weapon_Melee|Weapon_Melee]]"
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
---
# Панель заслона, одна рука

Аксессуар существует как переносимая часть городской работы, а не как рыцарский щит. Он даёт секунды на переход, помощь или смену оружия, но никогда не делает фронтальное стояние лучшей стратегией.

## Экземпляры

### Подъёмная подпорная панель [1H]
[instance_id:: lift_brace_panel]
[load_tier:: 1]
[rarity_band:: rusty..rare]
[origin_kind:: local_sector]
[origin_function:: удержание груза и защита лифтового прохода при ремонте]
[spawn_profile:: lift_service_cache]
[moveset_profile:: Raise Edge -> Short Advance -> Lower Reset]
[commitment_cost:: панель закрывает только узкий угол и оставляет бок открытым]
[handedness:: one_hand]
[guard_input:: Hold]
[guard_mechanic:: narrow_cover -> short_transition -> lower_recovery]

Панель помогает пересечь один простреливаемый край или убрать союзника, но при попытке стоять на месте быстро проигрывает обходу и опасной среде.

### Карантинная створка [1H]
[instance_id:: quarantine_shutter]
[load_tier:: 2]
[rarity_band:: uncommon..rare]
[origin_kind:: local_sector]
[origin_function:: закрытие заражённого окна и переносной барьер для санитарной группы]
[spawn_profile:: quarantine_cabinet]
[moveset_profile:: Snap Raise -> Angle Lock -> Forced Lower]
[commitment_cost:: фиксация угла отключает продвижение и требует явного снятия створки]
[handedness:: one_hand]
[guard_input:: Hold to Raise -> Tap to Lock]
[guard_mechanic:: narrow_cover -> angle_lock -> forced_lower]

Створка лучше держит один угол, но фиксированная позиция сразу становится читаемой проблемой для троса, обхода, среды и второй линии огня.
