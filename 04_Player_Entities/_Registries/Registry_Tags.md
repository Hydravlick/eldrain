---
type: registry
status: active
system: player_entities_registry
registry_type: tags
tags: [customization, modifiers, dna, loot]
related_files:
  - "[[04_Player_Entities/Tags_System|Tags_System]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
  - "[[07_Gear_Inventory/Thermos_System|Thermos_System]]"
---
# Реестр: Теги/Трейты, Мутации и Модификации

> **Логика системы:** реестр хранит исполняемые эффекты. Биография и события развития определены в [[04_Player_Entities/Trait_Development|Trait Development]].
> **Роль в пайплайне:** `Race + Spec -> Combo P/Q/E + Module Capacity -> Allowed Arsenal -> Tags -> Proficiency Gates -> Combat Profile и допустимая сборка Термоса`.
> **Dataview-контракт:** каждый объект начинается с `[id:: ...]`, а затем хранит тип, полярность, модификаторы, исключения и возможное слияние.
> **Терминология:** `tag` и `trait` обозначают один объект. `[tag:: ...]` — канонический ключ данных; `трейт` — допустимое игроко-нарративное название этого же эффекта.

## Правила тегов

- `[tag_kind:: proficiency]` меняет владение оружием и/или профильную ёмкость модулей Термоса, но не добавляет архетипный вектор.
- `[arsenal_grant:: frame_id @N]` добавляет фрейм с proficiency `N`; `[arsenal_block:: frame_id]` явно его запрещает.
- `[module_capacity_delta:: family +N, family -N]` сдвигает ёмкости, но не создаёт физический слот.
- `[tag_kind:: mutation]` меняет физику тела и активные/заблокированные векторы.
- `[add_vector:: ...]` допустим только для мутаций, физической перестройки или curated Fusion; обычное мастерство работает через `prof_delta` и мастерство фрейма.
- `[tag_kind:: attribute]` меняет видимые атрибуты T.O.U.C.H. или явную физическую capability.
- `[tag_kind:: flaw]` дает штраф или сужает стиль игры без автоматической компенсации Диссонансом.
- `[tag_kind:: fusion]` описывает curated Trait Fusion, возникающий из двух проявленных тегов и связующего события.
- `[exclusive_with:: ...]` запрещает одновременную установку несовместимых тегов.
- `[fusion_with:: other_tag -> result_tag]` показывает простой путь слияния прямо у исходного тега.
- `[fusion_requires:: tag_a, tag_b]` у результата фиксирует, какие два тега нужно объединить.
- `[trait_pool:: standard, specialist]` задает доступность. Если поле отсутствует, тег считается доступным обоим каталогам.
- `[event_family:: ...]` перечисляет события, повышающие вес результата.
- `[power_weight:: ...]` является внутренним балансным весом и не существует как ресурс внутри мира.
- `[dissonance_load:: ...]` используется только при физическом или эфирном источнике постоянного фона.

---
## 0. Нулевой пациент: шаблон тега

### Шаблон Тега (Template Tag)
[id:: template_tag]
[tag:: template_tag]
[tag_kind:: mutation]
[tag_polarity:: mixed]
[add_vector:: tech]
[block_vector:: hazard]
[prof_delta:: arcanegun +1]
[module_capacity_delta:: weave +1, plate -1]
[attr_delta:: TRQ +2, SNS -1]
[owned_output_mod:: none]
[capability:: none]
[vulnerability:: none]
[deferred_rule:: none]
[override_race_ban:: heavy_weapon]
[arsenal_grant:: breach_impact_2h @1]
[arsenal_block:: none]
[exclusive_with:: incompatible_tag]
[fusion_with:: other_tag -> result_tag]
[fusion_requires:: source_tag_a, source_tag_b]
[trait_pool:: standard, specialist]
[event_family:: survival]
[power_weight:: 0]
[dissonance_load:: 0]
* **Название:** Шаблонный Тег
* **Тип:** Mutation / Proficiency / Attribute / Flaw / Fusion
* **Эффект:** что меняется в арсенале, теле, векторах или экономике риска.
* **Штраф:** какая слабость, блокировка или цена удерживает тег в балансе.
* **Окно Двойного Парадокса:** какая общая слабость появляется после добавления или блокировки вектора.
* **Лор:** короткое физическое или ментальное объяснение.

## Категория A: Теги Мастерства (Proficiency Tags)
*Опыт, тренировки и чужие воспоминания. Повышают эффективность арсенала, но почти всегда сужают другой стиль игры.*

### Коридорный Рефлекс (Corridor Reflex)
[id:: trench_veteran]
[tag:: trench_veteran]
[tag_kind:: proficiency]
[tag_polarity:: mixed]
[prof_delta:: arcanegun +1, blade +1]
[exclusive_with:: cultist_mark]
[fusion_with:: street_rat -> street_breacher]
[trait_pool:: standard, specialist]
[event_family:: close_combat, corridor_survival]
[power_weight:: 4]
* **Эффект:** `[arcanegun +1]` | `[blade +1]`
* **Смысл:** тег усиливает ближний бой в коридорах и стрельбу в упор; аномальные процедуры не получают скрытого общего штрафа и оплачиваются собственным устройством и контрактом.
* **Лор:** *«В узком проходе не спорят с дистанцией. Упрись, пережди вспышку и бей, когда стена вернёт тебе шаг.» — наставление аварийных дозорных.*

### Портовый Грузчик (Dock Hand)
[id:: heavy_lifter]
[tag:: heavy_lifter]
[tag_kind:: proficiency]
[tag_polarity:: mixed]
[prof_delta:: blunt +1, arcanegun +1]
[arsenal_grant:: breach_impact_2h @1]
[attr_delta:: TRQ +1, SNS -1]
[exclusive_with:: hollow_bones]
[fusion_with:: piston_arm -> siege_frame]
[trait_pool:: standard, specialist]
[event_family:: carrying, rescue, labor]
[power_weight:: 3]
* **Эффект:** открывает двуручный проломный ударник на `prof:: 1`; тросовая работа принадлежит отдельному навыку, если Combo её получает.
* **Мастерство:** техника тяжёлого Frame открывается только его обычным proficiency gate; тег не создаёт отдельную перезарядку на ходу.
* **Штраф:** `[SNS -1]` - привычка к шуму делает мелкие сигналы менее заметными.
* **Лор:** *Мышечная память тех, кто таскал ящики с хламом по 16 часов в сутки.*

### Метка Послушника (Acolyte Mark)
[id:: cultist_mark]
[tag:: cultist_mark]
[tag_kind:: proficiency]
[tag_polarity:: mixed]
[exclusive_with:: trench_veteran]
[fusion_with:: alchemical_eye -> echo_oracle]
[trait_pool:: specialist]
[event_family:: ritual, aether_exposure, faction_cathedral]
[power_weight:: 8]
[dissonance_load:: 8]
* **Навык:** знак объясняет доступ к культовым процедурам в контенте и фракционной реакции, но не даёт общего рейтинга навыков, скрытого штрафа защиты, нового P/Q/E, `aether` или Frame.
* **Лор:** *Выжженный на лбу символ позволяет проводить больше эфира через тело, игнорируя боль.*

### Дитя Улиц (Gutter Born)
[id:: street_rat]
[tag:: street_rat]
[tag_kind:: proficiency]
[tag_polarity:: mixed]
[prof_delta:: blade +1]
[module_capacity_delta:: weave +1, plate -1]
[capability:: vent_fit]
[exclusive_with:: loud_aura]
[fusion_with:: trench_veteran -> street_breacher, hollow_bones -> vent_runner]
[trait_pool:: standard, specialist]
[event_family:: stealth, scavenging, escape]
[power_weight:: 3]
* **Эффект:** `[blade +1]` и `[weave capacity +1]`.
* **Штраф:** `[plate capacity -1]` — тяжёлая пластинчатая навеска ломает привычный ритм движения.
* **Фрейм:** лучше обслуживает клинковые и маршрутные доктрины, но не добавляет `shadow` как архетипный вектор.
* **Лор:** *Ты знаешь, куда ударить заточкой, чтобы пробить фильтр противогаза.*

---

## Категория B: Теги Мутации (Mutation Tags)
*Искажения плоти под влиянием Аномалии или алхимии. Меняют не цифры, а правила тела.*

### Гальваническая Кровь
[id:: voltaic_blood]
[tag:: voltaic_blood]
[tag_kind:: mutation]
[tag_polarity:: mixed]
[add_vector:: aether]
[block_vector:: hazard]
[deferred_rule:: shock_output, wet_backlash]
[exclusive_with:: ether_leech, rust_allergy]
[trait_pool:: specialist]
[event_family:: shock_survival, aether_exposure]
[power_weight:: 10]
[dissonance_load:: 10]
* **Эффект:** физический урон может конвертироваться в электрический, если оружие или способность допускают проводимость.
* **Штраф:** `[block_vector:: hazard]` - токсичные и влажные среды становятся опаснее.
* **Побочный эффект:** при попадании в воду персонаж получает перегрев/короткое замыкание.
* **Лор:** *В ваших венах течет не кровь, а электролит из разбитых батарей.*

### Эфирная Пиявка
[id:: ether_leech]
[tag:: ether_leech]
[tag_kind:: mutation]
[tag_polarity:: mixed]
[add_vector:: aether]
[block_vector:: tech]
[deferred_rule:: natural_recharge]
[exclusive_with:: voltaic_blood, brittle_nerves]
[trait_pool:: specialist]
[event_family:: reality_burn, aether_exposure]
[power_weight:: 12]
[dissonance_load:: 12]
* **Отложенное правило:** `natural_recharge` не участвует в активном профиле. Будущая версия обязана иметь внешний энергетический источник и не может питаться собственным убийством по замкнутому циклу.
* **Матрица Парадокса:** усиливает `aether`, но блокирует стабильную технику.
* **Лор:** *Ваша батарея сломана. Теперь вы заряжаетесь, высасывая угасающий свет из глаз умирающих.*

### Серая Хворь (Greyscale)
[id:: stone_skin]
[tag:: stone_skin]
[tag_kind:: mutation]
[tag_polarity:: mixed]
[add_vector:: kinetics]
[block_vector:: shadow]
[attr_delta:: LYR +2, GRP -2]
[exclusive_with:: hollow_bones]
[trait_pool:: standard, specialist]
[event_family:: anomaly_exposure, trauma_survival]
[power_weight:: 7]
[dissonance_load:: 7]
* **Эффект:** кожа становится каменной и дает естественную броню.
* **Штраф:** `[GRP -2]` - пальцы теряют гибкость.
* **Матрица Парадокса:** добавляет `kinetics`, но закрывает полноценный `shadow`.
* **Лор:** *Полезная болезнь, если успеть остановить ее до того, как окаменеет сердце.*

---

## Категория C: Теги Атрибутов (Attribute Tags)
*Физические улучшения и настройки организма. Хороши как инженерные заплатки, но создают шум, вес или зависимость.*

### Пневмо-сустав (Piston Joint)
[id:: piston_arm]
[tag:: piston_arm]
[tag_kind:: attribute]
[tag_polarity:: mixed]
[add_vector:: kinetics]
[prof_delta:: blunt +1, heavy_weapon +1]
[attr_delta:: TRQ +2, SNS -1]
[override_race_ban:: heavy_weapon]
[exclusive_with:: hollow_bones]
[fusion_with:: heavy_lifter -> siege_frame]
[trait_pool:: specialist]
[event_family:: surgery, heavy_weapon_mastery]
[power_weight:: 6]
[dissonance_load:: 6]
* **Эффект:** `[TRQ +2]` и доступ к физиологически спорному тяжелому оружию.
* **Штраф:** `[SNS -1]` - грохот механизмов заглушает шаги и дыхание врагов.
* **Матрица Парадокса:** добавляет `kinetics`.
* **Лор:** *Ржавая, но надежная гидравлика, врезанная прямо в кость.*

### Алхимический Зрачок
[id:: alchemical_eye]
[tag:: alchemical_eye]
[tag_kind:: attribute]
[tag_polarity:: positive]
[add_vector:: detection]
[attr_delta:: SNS +2]
[vulnerability:: dissonance_load +5]
[exclusive_with:: tremor_hands]
[fusion_with:: cultist_mark -> echo_oracle]
[trait_pool:: specialist]
[event_family:: surgery, investigation]
[power_weight:: 5]
[dissonance_load:: 5]
* **Эффект:** `[SNS +2]`; конкретные навыки и устройства могут лучше читать тепловой контраст.
* **Граница:** глаз не видит сквозь стены и не выдаёт готовую цель без линии, следа или подготовленной процедуры.
* **Матрица Парадокса:** добавляет `detection`.
* **Лор:** *Глаз заменен на колбу с реактивом, реагирующим на тепло.*

### Полые Кости (Avian DNA)
[id:: hollow_bones]
[tag:: hollow_bones]
[tag_kind:: attribute]
[tag_polarity:: mixed]
[add_vector:: shadow]
[block_vector:: kinetics]
[attr_delta:: LYR -2]
[owned_output_mod:: body.move_speed +10%]
[exclusive_with:: stone_skin, piston_arm, heavy_lifter]
[fusion_with:: street_rat -> vent_runner]
[trait_pool:: standard, specialist]
[event_family:: fall_survival, vertical_traversal]
[power_weight:: 2]
* **Эффект:** прямой модификатор скорости действует как один видимый телесный результат; бесшумность и снижение урона от падения не предоставляются автоматически.
* **Штраф:** `[LYR -2]` - кости ломаются от удара.
* **Матрица Парадокса:** добавляет `shadow`, но блокирует грубую `kinetics`.
* **Лор:** *Мутация, характерная для жителей верхних уровней, где гравитация слабее.*

### Лишние Пальцы
[id:: extra_fingers]
[tag:: extra_fingers]
[tag_kind:: attribute]
[tag_polarity:: positive]
[add_vector:: tech]
[attr_delta:: GRP +2]
[vulnerability:: rigid_handwear_incompatible]
[exclusive_with:: tremor_hands]
[trait_pool:: standard, specialist]
[event_family:: lockwork, rapid_handling]
[power_weight:: 4]
* **Эффект:** `[GRP +2]` - хват, перезарядка, скорость лута.
* **Матрица Парадокса:** добавляет `tech`.
* **Граница:** дополнительные пальцы объясняют `[GRP +2]`, но не создают свободную руку и не обходят хват, занятые руки или Commitment.

---

## Категория D: Негативные Теги/Трейты (Flaw Tags)
*Штрафные теги нужны для баланса сильных плюсов. Они не являются "плохим билдом"; они создают дешевую, но опасную специализацию.*

### Дрожащие Руки
[id:: tremor_hands]
[tag:: tremor_hands]
[tag_kind:: flaw]
[tag_polarity:: negative]
[prof_delta:: arcanegun -1, blade -1]
[block_vector:: ballistics]
[exclusive_with:: alchemical_eye, extra_fingers]
[trait_pool:: standard, specialist]
[event_family:: trauma, failed_precision]
[power_weight:: 0]
* **Штраф:** дальняя точность и чистая фехтовальная моторика падают.
* **Компенсация:** нервный тремор может быть художественным cue эфира, но не превращается в общий бонус ко всем аномальным процедурам.
* **Матрица Парадокса:** блокирует архетипный или телесный `ballistics`; оружейный `frame_vector` остаётся commitment-экспозицией и не пересчитывает `weak_to`.

### Хрупкая Воля
[id:: brittle_nerves]
[tag:: brittle_nerves]
[tag_kind:: flaw]
[tag_polarity:: negative]
[attr_delta:: GLW -2, SNS +1]
[block_vector:: aether]
[exclusive_with:: ether_leech, cultist_mark]
[trait_pool:: standard, specialist]
[event_family:: stress, backlash]
[power_weight:: 0]
* **Штраф:** персонаж хуже держит перегрузки, ритуалы и долгий каст.
* **Компенсация:** постоянная тревога дает `[SNS +1]`.
* **Матрица Парадокса:** блокирует `aether`.

### Аллергия на Ржавчину
[id:: rust_allergy]
[tag:: rust_allergy]
[tag_kind:: flaw]
[tag_polarity:: negative]
[attr_delta:: LYR -1]
[block_vector:: tech]
[exclusive_with:: voltaic_blood, piston_arm]
[trait_pool:: standard, specialist]
[event_family:: corrosion, industrial_exposure]
[power_weight:: 0]
* **Штраф:** импланты, скрап-броня и грязные механизмы чаще вызывают воспаление.
* **Матрица Парадокса:** блокирует `tech`, если тот пришел только от тега.

### Громкая Аура
[id:: loud_aura]
[tag:: loud_aura]
[tag_kind:: flaw]
[tag_polarity:: negative]
[attr_delta:: SNS -1, GLW +1]
[block_vector:: shadow]
[dissonance_load:: 6]
[exclusive_with:: street_rat]
[trait_pool:: standard, specialist]
[event_family:: anomaly_exposure, detection_failure]
[power_weight:: 0]
* **Штраф:** персонажа легче заметить акустикой, эхом и магическими датчиками.
* **Компенсация:** нестабильная аура дает небольшой прирост `[GLW +1]`.
* **Матрица Парадокса:** блокирует `shadow`.

---

## Категория E: Trait Fusion
*Trait Fusion уничтожает два малых тега и заменяет их одним мощным. Это не третий бесплатный бонус, а curated-развитие конкретной Пешки. Повышенный DissonanceLoad применяется только там, где результат физически или эфирно фонит.*

### Уличный Проломщик (Street Breacher)
[id:: street_breacher]
[tag:: street_breacher]
[tag_kind:: fusion]
[tag_polarity:: positive]
[fusion_requires:: street_rat, trench_veteran]
[prof_delta:: blade +2, arcanegun +1]
[module_capacity_delta:: weave +1, plate -1]
[add_vector:: shadow]
[exclusive_with:: loud_aura, cultist_mark]
[trait_pool:: standard, specialist]
[event_family:: ambush_chain, close_combat_escape]
[power_weight:: 7]
* **Эффект:** превращает знание улиц и коридорный напор в стиль коротких засад.
* **Гейт:** если `blade` или `arcanegun` достигает `3+`, открывается мастерство соответствующего фрейма: стабильность, техника, cancel, снижение экспозиции или дополнительное окно исполнения.

### Осадная Рама (Siege Frame)
[id:: siege_frame]
[tag:: siege_frame]
[tag_kind:: fusion]
[tag_polarity:: positive]
[fusion_requires:: heavy_lifter, piston_arm]
[prof_delta:: heavy_weapon +2, blunt +1]
[attr_delta:: TRQ +3, SNS -2, GRP -1]
[add_vector:: kinetics]
[override_race_ban:: heavy_weapon]
[exclusive_with:: hollow_bones, rust_allergy]
[trait_pool:: specialist]
[event_family:: siege_combat, heavy_weapon_mastery]
[power_weight:: 10]
[dissonance_load:: 10]
* **Эффект:** тело становится лафетом для тяжелого оружия.
* **Штраф:** акустический профиль резко растет; скрытность почти невозможна.

### Эхо-Оракул (Echo Oracle)
[id:: echo_oracle]
[tag:: echo_oracle]
[tag_kind:: fusion]
[tag_polarity:: positive]
[fusion_requires:: alchemical_eye, cultist_mark]
[attr_delta:: SNS +3, GLW +1]
[add_vector:: aether, detection]
[exclusive_with:: brittle_nerves, trench_veteran]
[trait_pool:: specialist]
[event_family:: investigation, ritual, trace_discovery]
[power_weight:: 11]
[dissonance_load:: 11]
* **Эффект:** персонаж лучше читает остаточные следы через подготовленную процедуру, дым и эфирный шум.
* **Граница:** стены и отсутствие физического следа не обходятся автоматически.
* **Риск:** высокий Диссонанс делает дорогой лут и активные заклинания заметнее.

### Вентиляционный Бегун (Vent Runner)
[id:: vent_runner]
[tag:: vent_runner]
[tag_kind:: fusion]
[tag_polarity:: positive]
[fusion_requires:: hollow_bones, street_rat]
[prof_delta:: blade +1]
[module_capacity_delta:: weave +2, plate -2]
[attr_delta:: LYR -2]
[owned_output_mod:: body.move_speed +15%]
[add_vector:: shadow]
[block_vector:: kinetics]
[capability:: vent_fit]
[exclusive_with:: stone_skin, piston_arm, loud_aura]
[trait_pool:: standard, specialist]
[event_family:: vent_escape, vertical_traversal]
[power_weight:: 6]
* **Эффект:** максимальная мобильность в узких маршрутах, шахтах и вентиляции.
* **Штраф:** любые силовые столкновения становятся смертельно опасными.

---
