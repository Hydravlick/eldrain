---
type: skill_device_concept
status: deferred
system: player_entities
device_id: interposition_panel
display_name: Панель заслона
skill_type: defense
tags: [skill_device, defense, transition, deferred]
related_files:
  - "[[04_Player_Entities/_Registries/Registry_Skill_Types|Registry_Skill_Types]]"
---
# Панель заслона

> Этот материал больше не описывает оружейный фрейм. Заслон меняет условия сцены и принадлежит защитному навыку или устройству, а не слоту оружия.

Панель существует как переносимая часть городской работы, а не как рыцарский щит. Она может дать секунды на переход, помощь или смену оружия, но конкретная Combo обязана назвать источник, подготовку, занимаемую руку, фланг, Recovery и контр-окно до допуска устройства в рейд.

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
