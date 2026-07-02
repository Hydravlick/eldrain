---
type: registry
status: active
system: combat_survival_registry
registry_type: weapons
tags:
  - database
  - equipment
  - templates
related_files:
  - "[[05_Combat_Survival/Combat_Three_Debts|Combat_Three_Debts]]"
---
> [!TODO] Оружейные взаимодействия с линиями мутаций
> - [ ] Определить теги для локального выжигания роста, безопасной проверки мимика и переноса сигнальной метки без универсального «правильного оружия».
> - [ ] Проверить цену шума: быстрый ответ против Корнехвата или Двереглота должен менять риск встречи со стандартной экосистемой.
> - **Основа:** [[08_World_Generation/_Registries/Registry_Anomaly_Mutations|Registry_Anomaly_Mutations]]. Урон, дальность и имплициты этой правкой не меняются.
> [!TODO] Добавить свойства архетипов
> - [ ] Прописать поле `[implicit:: ...]` для всех пушек (напр. `ambush`, `armor_break`).
> - [ ] Прописать поле `[sweet_spot_range:: float]` для алебард.
> - [ ] Проверить коридор летальности `spark_handcannon 45` против `condenser_longframe 75` на HP, пластинах, точности, полном цикле заряда, Heat, Pulse и стоимости потери; разница одиночного урона сама по себе не доказывает ни норму, ни нарушение прогрессии.

# Реестр: Типы Оружия (Magipunk Arsenal)

> **Философия Дизайна:**
> Оружие определяется не "именем", а **Конструкцией (Frame)** и **Паттерном (Pattern)**.
> * **Frame:** Определяет хитбокс, анимации и встроенное свойство (Implicit).
> * **Pattern:** Определяет происхождение, тип импульса и стабильность.
> * **Tier:** Определяет допустимую энергетическую нагрузку, Heat/Recovery-коридор и совместимость с усиленными батареями.
> * **Rarity:** Определяет аффиксы и специализацию экземпляра, но не входит в общий Power Score.
> * **Battery Cycle:** Для магострелов темп задается батареей, охлаждением, heat, bloom и Dissonance.

> **Легенда Типов:**
> `blade` — Клинковое (Мечи, Ножи)
> `blunt` — Дробящее (Молоты, Булавы)
> `polearm` — Древковое (Копья, Алебарды)
> `arcanegun` — Магострел и дальнобойный фрейм (разрядники, конденсаторы, эмиттеры, игольники)
> `catalyst` — совместимое имя семейства специализированных эфирных устройств; оно не является обязательным оружием кастера
> `shield` — Щит (Баклеры, Ростовые)

> **Параметры:**
> `[range:: N]` — Дальность (м).
> `[weapon_vector:: ...]` — скрытый тактический вектор оружия.
> `[vector_gate:: 3]` — минимальный итоговый proficiency tier, при котором оружие добавляет свой вектор в Combat Profile.
> `[frame:: ...]` — конкретный дальнобойный фрейм.
> `[impulse_cost:: N]` — сколько импульсов выбранного резерва тратит действие.
> `[impulse_reserve:: N]` — текущий внутренний запас уже переданной энергии.
> `[load_acceptance:: base/stable/overcharge]` — какие транзакции зарядки выдерживает Frame.
> `[heat:: N]` — сколько тепла создает импульс.
> `[bloom:: low/medium/high]` — насколько быстро растет эфирный разброс.
> `[dissonance_pulse:: N]` — временный эфирный всплеск при применении.
> `[primary_window_function:: create/exploit/mitigate]` — главная работа фрейма с окном.
> `[creates_window:: ...]`, `[exploits_window:: ...]`, `[mitigates_window:: ...]` — нормализованные ID окон либо `none`.
> До открытия гейта оружие остается инструментом урона/анимаций, но не становится отдельным узлом Двойного Парадокса.

---
## 1. Клинковое Оружие (Blades)
*Режущий/колющий урон. Вызывает кровотечения и хорошо закрывает окна, созданные дальним боем.*

### Боевой Нож (Combat Shiv) [1H]
[weapon_type:: blade]
[weapon_vector:: shadow]
[vector_gate:: 3]
[heat:: 0]
[dissonance_pulse:: 0]
[primary_window_function:: exploit]
[creates_window:: none]
[exploits_window:: back_exposed, stagger_entry]
[mitigates_window:: none]
[weight:: 0.5kg]|[dmg:: 15]
*Короткий клинок для "грязной" работы в клинче.*
* **Мувсет:** Очень быстрые колющие удары. Минимальный расход стамины.
* **Implicit (Встроенное):** **(Ambush)** Урон в спину x1.5. Удары не сбивают скорость бега.

### Мачете / Тесак (Cleaver) [1H]
[weapon_type:: blade]
[weapon_vector:: shadow]
[vector_gate:: 3]
[heat:: 0]
[dissonance_pulse:: 0]
[primary_window_function:: exploit]
[creates_window:: none]
[exploits_window:: soft_zone_exposed]
[mitigates_window:: none]
[weight:: 1.5kg]|[dmg:: 35]
*Тяжелое лезвие с смещенным центром тяжести.*
* **Мувсет:** Широкие рубящие удары. Задевает несколько целей.
* **Implicit (Встроенное):** **(Maim)** Шанс 20% наложить "Глубокую рану" (снижает макс. HP до конца рейда). Урон по "мягким" целям +30%.

### Рапира / Эсток (Estoc) [1H]
[weapon_type:: blade]
[weapon_vector:: shadow]
[vector_gate:: 3]
[heat:: 0]
[dissonance_pulse:: 0]
[primary_window_function:: exploit]
[creates_window:: none]
[exploits_window:: joint_exposed]
[mitigates_window:: none]
[weight:: 1.2kg]|[dmg:: 25]
*Тонкий клинок для уколов в сочленения брони.*
* **Мувсет:** Линейные выпады. Длинная дистанция удара.
* **Implicit (Встроенное):** **(Needle Point)** Игнорирует часть мягкой защиты. Крит требует попадания в уязвимую зону; твердая пластина продолжает блокировать удар по физическим правилам.

---

## 2. Дробящее (Blunt / Impact)
*Урон ударом. Ломает кости и стамину. Эффективно против Латы.*

### Кувалда (Sledgehammer) [2H]
[weapon_type:: blunt]
[weapon_vector:: kinetics]
[vector_gate:: 3]
[heat:: 0]
[dissonance_pulse:: 0]
[primary_window_function:: create]
[creates_window:: guard_break]
[exploits_window:: none]
[mitigates_window:: none]
[weight:: 8kg]|[dmg:: 55]
*Инструмент, превращенный в оружие. Медленный и неотвратимый.*
* **Мувсет:** Вертикальный удар (пробивает блок) и Горизонтальный (сбивает с ног).
* **Implicit (Встроенное):** **(Breach)** Снимает у цели 30 ед. Выносливости (Stamina) за удар. Если Выносливость 0 — сбивает с ног. Разрушает двери/укрытия.

### Булава / Дубинка (Mace) [1H]
[weapon_type:: blunt]
[weapon_vector:: kinetics]
[vector_gate:: 3]
[heat:: 0]
[dissonance_pulse:: 0]
[primary_window_function:: create]
[creates_window:: disorientation]
[exploits_window:: none]
[mitigates_window:: none]
[weight:: 3.5kg]|[dmg:: 30]
*Компактный вес.*
* **Implicit (Встроенное):** **(Concussion)** Удары в голову накладывают эффект "Дезориентация" (размытие экрана, сбой звука) на 3 сек.

---

## 3. Древковое (Polearms)
*Контроль дистанции. "Зонинг" противников.*

### Алебарда (Halberd) [2H]
[weapon_type:: polearm]
[weapon_vector:: kinetics]
[vector_gate:: 3]
[heat:: 0]
[dissonance_pulse:: 0]
[primary_window_function:: create]
[creates_window:: distance_control]
[exploits_window:: none]
[mitigates_window:: melee_entry]
[weight:: 5.5kg]|[dmg:: 45]
*Топор на длинной палке с шипом.*
* **Мувсет:** Укол (Poke) на дистанции, Рубящий (Swing) вблизи.
* **Implicit (Встроенное):** **(Sweet Spot)** Наносит 100% урона только лезвием (на конце). Если ударить древком (вплотную) — урон 30%.

### Боевая Коса (War Scythe) [2H]
[weapon_type:: polearm]
[weapon_vector:: kinetics]
[vector_gate:: 3]
[heat:: 0]
[dissonance_pulse:: 0]
[primary_window_function:: exploit]
[creates_window:: none]
[exploits_window:: shield_flank]
[mitigates_window:: none]
[weight:: 4.0kg]|[dmg:: 42]
*Лезвие под углом.*
* **Implicit (Встроенное):** **(Reap)** Игнорирует щиты (Shield Bypass), так как лезвие заходит за блок.

---

## 4. Дальний Бой: Магострельные Фреймы
*Медленное дальнее давление. Оружие может убивать, но чаще открывает окно для ближнего боя, Q/E или команды.*

### Ручной Разрядник (Spark Handcannon) [1H]
[weapon_id:: spark_handcannon]
[weapon_type:: arcanegun]
[frame:: handcannon]
[tier:: 1]
[weapon_vector:: ballistics]
[vector_gate:: 3]
[weight:: 1.8kg]|[dmg:: 45]
[impulse_cost:: 1]
[heat:: 35]
[bloom:: high]
[dissonance_pulse:: 4]
[primary_window_function:: create]
[creates_window:: stagger_entry]
[exploits_window:: none]
[mitigates_window:: none]
*Грубый одноручный магострел: короткая дистанция, сильный удар, плохая дисциплина разряда.*
* **Implicit:** **(Stopping Pulse)** попадание сбивает спринт и дает `Aim Punch`.
* **Слабость:** при стрельбе на бегу bloom резко растет.

### Конденсаторный Длинник (Condenser Longframe) [2H]
[weapon_id:: condenser_longframe]
[weapon_type:: arcanegun]
[frame:: condenser_longframe]
[tier:: 2]
[weapon_vector:: ballistics]
[vector_gate:: 3]
[weight:: 4.5kg]|[dmg:: 75]
[impulse_cost:: 1]
[charge_time:: 0.8s]
[heat:: 45]
[bloom:: medium]
[dissonance_pulse:: 6]
[primary_window_function:: create]
[creates_window:: weakspot_open]
[exploits_window:: exposed_weakspot]
[mitigates_window:: none]
*Дальний фрейм с удержанием заряда. Силен, если игрок успел стабилизировать импульс.*
* **Implicit:** **(Shield Breaker)** повышенное давление по щитам, барьерам и кастерам.
* **Слабость:** плох под давлением; сбитый заряд уходит в heat и Dissonance.

### Веерный Эмиттер (Scatter Emitter) [2H]
[weapon_id:: scatter_emitter]
[weapon_type:: arcanegun]
[frame:: scatter_emitter]
[tier:: 1]
[weapon_vector:: ballistics]
[vector_gate:: 3]
[weight:: 3.8kg]|[dmg:: 10x6]
[impulse_cost:: 1]
[charge_time:: 0.4s]
[heat:: 50]
[bloom:: high]
[dissonance_pulse:: 5]
[primary_window_function:: create]
[creates_window:: melee_entry]
[exploits_window:: none]
[mitigates_window:: enemy_entry]
*Выплескивает веер нестабильной энергии. Не про точность, а про остановку входа.*
* **Implicit:** **(Stagger Cone)** мелкие цели отбрасываются, крупные получают сильный aim punch.
* **Слабость:** на средней дистанции урон распадается, heat копится быстро.

### Гарпунный Драйвер (Harpoon Driver) [2H]
[weapon_id:: harpoon_driver]
[weapon_type:: arcanegun]
[frame:: harpoon_driver]
[tier:: 2]
[weapon_vector:: ballistics]
[vector_gate:: 3]
[weight:: 6.0kg]|[dmg:: 40]
[impulse_cost:: 1]
[charge_time:: 0.7s]
[heat:: 30]
[bloom:: low]
[dissonance_pulse:: 5]
[primary_window_function:: create]
[creates_window:: tether_control]
[exploits_window:: none]
[mitigates_window:: escape_route]
*Катушка разгоняет гарпун с тросом. Главная ценность - не урон, а фиксация.*
* **Implicit:** **(Tether)** цель замедлена, привязана или вытянута из укрытия.
* **Слабость:** промах оставляет игрока с тяжелым фреймом и потерянным темпом.

### Игольный Арбалет (Needle Crossbow) [2H]
[weapon_id:: needle_crossbow]
[weapon_type:: arcanegun]
[frame:: needle_crossbow]
[tier:: 1]
[power_source:: mechanical]
[weapon_vector:: ballistics]
[vector_gate:: 3]
[weight:: 2.4kg]|[dmg:: 35]
[impulse_cost:: 0]
[heat:: 0]
[bloom:: low]
[dissonance_pulse:: 0]
[primary_window_function:: exploit]
[creates_window:: none]
[exploits_window:: soft_zone_exposed, concealment]
[mitigates_window:: none]
*Механический дальнобойный фрейм без батареи. Тихий, но медленный.*
* **Implicit:** **(Puncture)** хорошо работает по мягким зонам и тканям.
* **Слабость:** долгий взвод, слабый stagger, плохая работа против тяжелых пластин.

## 5. Специализированные Эфирные Устройства
*Совместимое семейство `catalyst` хранит фокусы Reality Burn и ритуальные устройства. Оно не является обязательным оружием кастера и не обслуживает обычный цикл Q/E.*

### Фокус Реальности (Reality Focus) [2H]
[weapon_id:: reality_focus]
[weapon_type:: catalyst]
[frame:: catalyst_focus]
[tier:: 2]
[weapon_vector:: aether]
[vector_gate:: 3]
[weight:: 3.0kg]|[dmg:: 55]
[impulse_cost:: 1]
[charge_item:: reality_charge]
[charge_time:: 1.0s]
[heat:: 40]
[bloom:: medium]
[dissonance_pulse:: 8]
[primary_window_function:: create]
[creates_window:: reality_exposed]
[exploits_window:: none]
[mitigates_window:: anomalous_immunity]
*Проводник, который заставляет аномальное тело принять нормальные законы.*
* **Implicit:** **(Reality Burn)** временно делает аномальную цель уязвимой к обычному урону.
* **Расход:** тратит подготовленный `Reality Charge`, `Overcharge Cell` или стабилизатор. Не списывает сырой Рез из кошелька во время рейда.
* **Слабость:** высокий Dissonance, backlash без батареи, слабый темп против живых гуманоидов.

---

## 6. Щиты (Shields)

### Баклер (Buckler) [1H]
[weapon_type:: shield]
[primary_window_function:: mitigate]
[creates_window:: parry_stagger]
[exploits_window:: none]
[mitigates_window:: melee_entry]
[weight:: 1.0kg]
*Маленький кулачный щит.*
* **Implicit:** Окно блока очень маленькое (0.5 сек), но при идеальном блоке (Parry) ошеломляет атакующего.

### Ростовой Щит (Tower Shield) [1H]
[weapon_type:: shield]
[primary_window_function:: mitigate]
[creates_window:: covered_advance]
[exploits_window:: none]
[mitigates_window:: ranged_line]
[weight:: 15kg]
*Дверь от сейфа/машины.*
* **Implicit:** Создает "Полное укрытие". Можно стрелять из пистолета, не опуская щит (вслепую). Сильно режет скорость (-40 MS).
---

## 0. Нулевой пациент: шаблон оружия

### Шаблон Оружия (Template Weapon) [1H]
[weapon_id:: template_weapon]
[weapon_type:: blade]
[frame:: template_frame]
[tier:: 1]
[weapon_vector:: shadow]
[vector_gate:: 3]
[weight:: 1.0kg]
[impulse_cost:: 0]
[heat:: 0]
[bloom:: none]
[dissonance_pulse:: 0]
[primary_window_function:: create]
[creates_window:: template_window]
[exploits_window:: none]
[mitigates_window:: none]
[value:: 0]
*Короткое описание боевой фантазии.*
- **Сильная дистанция:** где оружие раскрывается.
- **Слабость:** что мешает реализовать урон.
- **Мастерство:** какие свойства открываются на высоком proficiency.
