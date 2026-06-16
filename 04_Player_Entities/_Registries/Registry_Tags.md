---
type: registry
status: active
registry_type: tags
tags: [customization, modifiers, dna, loot]
---
# Реестр: Теги Памяти и Мутации (Memory Tags)

> **Логика системы:** теги - это физические изменения, импланты, татуировки, травмы или ментальные программы, вставляемые в слоты персонажа.
> **Роль в пайплайне:** `Race + Spec -> Combo P/Q/E -> Allowed Arsenal -> Tags -> Proficiency Gates -> Combat Profile`.
> **Dataview-контракт:** каждый объект начинается с `[id:: ...]`, а затем хранит тип, полярность, модификаторы, исключения и возможное слияние.

## Правила тегов

- `[tag_kind:: proficiency]` меняет владение оружием или инструментами.
- `[tag_kind:: mutation]` меняет физику тела и активные/заблокированные векторы.
- `[tag_kind:: attribute]` меняет атрибуты T.O.U.C.H. и вторичные параметры.
- `[tag_kind:: flaw]` дает штраф и может возвращать бюджет через `[resonance_credit:: ...]`.
- `[tag_kind:: fusion]` описывает мощный тег, который появляется при слиянии двух малых тегов.
- `[exclusive_with:: ...]` запрещает одновременную установку несовместимых тегов.
- `[fusion_with:: other_tag -> result_tag]` показывает простой путь слияния прямо у исходного тега.
- `[fusion_requires:: tag_a, tag_b]` у результата фиксирует, какие два тега нужно объединить.

---
## 0. Нулевой пациент: шаблон тега

### Шаблон Тега (Template Tag)
[id:: template_tag]
[tag:: template_tag]
[tag_kind:: mutation]
[tag_polarity:: mixed]
[add_vector:: tech]
[block_vector:: hazard]
[prof_delta:: arcanegun +1, catalyst -1]
[attr_delta:: TRQ +2, SNS -1]
[override_race_ban:: heavy_weapon]
[exclusive_with:: incompatible_tag]
[fusion_with:: other_tag -> result_tag]
[fusion_requires:: source_tag_a, source_tag_b]
[resonance_cost:: 0]
[resonance_credit:: 0]
* **Название:** Шаблонный Тег
* **Тип:** Mutation / Proficiency / Attribute / Flaw / Fusion
* **Эффект:** что меняется в арсенале, теле, векторах или экономике риска.
* **Штраф:** какая слабость, блокировка или цена удерживает тег в балансе.
* **Окно Двойного Парадокса:** какая общая слабость появляется после добавления или блокировки вектора.
* **Лор:** короткое физическое или ментальное объяснение.

## Категория A: Теги Мастерства (Proficiency Tags)
*Опыт, тренировки и чужие воспоминания. Повышают эффективность арсенала, но почти всегда сужают другой стиль игры.*

### Окопный Рефлекс (Trench Reflex)
[id:: trench_veteran]
[tag:: trench_veteran]
[tag_kind:: proficiency]
[tag_polarity:: mixed]
[prof_delta:: arcanegun +1, blade +1, catalyst -1]
[exclusive_with:: cultist_mark]
[fusion_with:: street_rat -> street_breacher]
[resonance_cost:: 4]
* **Эффект:** `[arcanegun +1]` | `[blade +1]`
* **Штраф:** `[catalyst -1]` - технологии подавляют магическое чутье.
* **Смысл:** тег усиливает ближний бой в коридорах и стрельбу в упор, но мешает чистой магии.
* **Лор:** *«В узком коридоре нет времени на заклинания. Бей штыком, стреляй в упор.» - наставление штурмовиков.*

### Портовый Грузчик (Dock Hand)
[id:: heavy_lifter]
[tag:: heavy_lifter]
[tag_kind:: proficiency]
[tag_polarity:: mixed]
[prof_delta:: heavy_weapon +1]
[attr_delta:: TRQ +1, SNS -1]
[exclusive_with:: hollow_bones]
[fusion_with:: piston_arm -> siege_frame]
[resonance_cost:: 3]
* **Эффект:** `[heavy_weapon +1]` - пулеметы, гарпуны, молоты.
* **Эффект:** позволяет перезаряжать тяжелое оружие на ходу, если итоговый proficiency не ниже `2`.
* **Штраф:** `[SNS -1]` - привычка к шуму делает мелкие сигналы менее заметными.
* **Лор:** *Мышечная память тех, кто таскал ящики с хламом по 16 часов в сутки.*

### Метка Послушника (Acolyte Mark)
[id:: cultist_mark]
[tag:: cultist_mark]
[tag_kind:: proficiency]
[tag_polarity:: mixed]
[prof_delta:: catalyst +2, shield -1]
[add_vector:: aether]
[exclusive_with:: trench_veteran]
[fusion_with:: alchemical_eye -> echo_oracle]
[resonance_cost:: 8]
* **Эффект:** `[catalyst +2]`
* **Штраф:** `[shield -1]` - вера становится единственной защитой.
* **Матрица Парадокса:** добавляет `aether`, если слот тегов не заблокирован.
* **Лор:** *Выжженный на лбу символ позволяет проводить больше эфира через тело, игнорируя боль.*

### Дитя Улиц (Gutter Born)
[id:: street_rat]
[tag:: street_rat]
[tag_kind:: proficiency]
[tag_polarity:: mixed]
[prof_delta:: blade +1, stealth +1, heavy_armor -1]
[add_vector:: shadow]
[exclusive_with:: loud_aura]
[fusion_with:: trench_veteran -> street_breacher, hollow_bones -> vent_runner]
[resonance_cost:: 3]
* **Эффект:** `[blade +1]` | `[stealth +1]`
* **Штраф:** `[heavy_armor -1]` - тяжелая броня ломает привычный ритм движения.
* **Матрица Парадокса:** добавляет `shadow`, но делает сборку зависимой от темпа и позиции.
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
[exclusive_with:: ether_leech, rust_allergy]
[resonance_cost:: 10]
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
[exclusive_with:: voltaic_blood, brittle_nerves]
[resonance_cost:: 12]
* **Эффект:** убийство врага восстанавливает часть маны и дает заряд перегрузки.
* **Штраф:** естественное восстановление маны отключено.
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
[resonance_cost:: 7]
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
[resonance_cost:: 6]
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
[exclusive_with:: tremor_hands]
[fusion_with:: cultist_mark -> echo_oracle]
[resonance_cost:: 5]
* **Эффект:** `[SNS +2]` - лут, точность, распознавание следов.
* **Эффект:** видит живых существ сквозь дым и темноту.
* **Матрица Парадокса:** добавляет `detection`.
* **Лор:** *Глаз заменен на колбу с реактивом, реагирующим на тепло.*

### Полые Кости (Avian DNA)
[id:: hollow_bones]
[tag:: hollow_bones]
[tag_kind:: attribute]
[tag_polarity:: mixed]
[add_vector:: shadow]
[block_vector:: kinetics]
[attr_delta:: speed +10%, LYR -2]
[exclusive_with:: stone_skin, piston_arm, heavy_lifter]
[fusion_with:: street_rat -> vent_runner]
[resonance_cost:: 2]
* **Эффект:** `[Speed +10%]` | `[Fall Damage -50%]`
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
[exclusive_with:: tremor_hands]
[resonance_cost:: 4]
* **Эффект:** `[GRP +2]` - хват, перезарядка, скорость лута.
* **Матрица Парадокса:** добавляет `tech`.
* **Лор:** *Выглядит жутко, но позволяет перезаряжать револьвер одной рукой, пока вторая держит меч.*

---

## Категория D: Негативные Трейты (Flaw Tags)
*Штрафные теги нужны для баланса сильных плюсов. Они не являются "плохим билдом"; они создают дешевую, но опасную специализацию.*

### Дрожащие Руки
[id:: tremor_hands]
[tag:: tremor_hands]
[tag_kind:: flaw]
[tag_polarity:: negative]
[prof_delta:: arcanegun -1, blade -1, catalyst +1]
[block_vector:: ballistics]
[exclusive_with:: alchemical_eye, extra_fingers]
[resonance_cost:: 0]
[resonance_credit:: 2]
* **Штраф:** дальняя точность и чистая фехтовальная моторика падают.
* **Компенсация:** нервный тремор помогает чувствовать ритм эфира, поэтому `[catalyst +1]`.
* **Матрица Парадокса:** блокирует `ballistics`, если этот вектор был открыт только оружием.

### Хрупкая Воля
[id:: brittle_nerves]
[tag:: brittle_nerves]
[tag_kind:: flaw]
[tag_polarity:: negative]
[attr_delta:: GLW -2, SNS +1]
[block_vector:: aether]
[exclusive_with:: ether_leech, cultist_mark]
[resonance_cost:: 0]
[resonance_credit:: 3]
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
[resonance_cost:: 0]
[resonance_credit:: 2]
* **Штраф:** импланты, скрап-броня и грязные механизмы чаще вызывают воспаление.
* **Матрица Парадокса:** блокирует `tech`, если тот пришел только от тега.

### Громкая Аура
[id:: loud_aura]
[tag:: loud_aura]
[tag_kind:: flaw]
[tag_polarity:: negative]
[attr_delta:: SNS -1, GLW +1]
[block_vector:: shadow]
[exclusive_with:: street_rat]
[resonance_cost:: 0]
[resonance_credit:: 2]
* **Штраф:** персонажа легче заметить акустикой, эхом и магическими датчиками.
* **Компенсация:** нестабильная аура дает небольшой прирост `[GLW +1]`.
* **Матрица Парадокса:** блокирует `shadow`.

---

## Категория E: Теги Слияния (Fusion Tags)
*Слияние уничтожает два малых тега и заменяет их одним мощным. Это не третий бесплатный бонус, а уплотнение билда с более высоким риском Резонанса.*

### Уличный Проломщик (Street Breacher)
[id:: street_breacher]
[tag:: street_breacher]
[tag_kind:: fusion]
[tag_polarity:: positive]
[fusion_requires:: street_rat, trench_veteran]
[prof_delta:: blade +2, arcanegun +1, stealth +1, catalyst -1, heavy_armor -1]
[add_vector:: shadow]
[exclusive_with:: loud_aura, cultist_mark]
[resonance_cost:: 7]
* **Эффект:** превращает уличный стелс и окопную агрессию в стиль коротких засад.
* **Гейт:** если `blade` или `arcanegun` достигает `3+`, оружейный вектор может войти в Combat Profile.

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
[resonance_cost:: 10]
* **Эффект:** тело становится лафетом для тяжелого оружия.
* **Штраф:** акустический профиль резко растет; скрытность почти невозможна.

### Эхо-Оракул (Echo Oracle)
[id:: echo_oracle]
[tag:: echo_oracle]
[tag_kind:: fusion]
[tag_polarity:: positive]
[fusion_requires:: alchemical_eye, cultist_mark]
[prof_delta:: catalyst +2, shield -1]
[attr_delta:: SNS +3, GLW +1]
[add_vector:: aether, detection]
[exclusive_with:: brittle_nerves, trench_veteran]
[resonance_cost:: 11]
* **Эффект:** персонаж видит остаточные следы событий и может читать слабости через дым, стены и эфирные шумы.
* **Риск:** высокий Резонанс делает дорогой лут и активные заклинания заметнее.

### Вентиляционный Бегун (Vent Runner)
[id:: vent_runner]
[tag:: vent_runner]
[tag_kind:: fusion]
[tag_polarity:: positive]
[fusion_requires:: hollow_bones, street_rat]
[prof_delta:: stealth +2, blade +1, heavy_armor -2]
[attr_delta:: speed +15%, LYR -2]
[add_vector:: shadow]
[block_vector:: kinetics]
[exclusive_with:: stone_skin, piston_arm, loud_aura]
[resonance_cost:: 6]
* **Эффект:** максимальная мобильность в узких маршрутах, шахтах и вентиляции.
* **Штраф:** любые силовые столкновения становятся смертельно опасными.

---


