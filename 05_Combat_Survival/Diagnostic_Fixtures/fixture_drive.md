---
type: entity
system: combat_survival
status: draft
publication_state: diagnostic_fixture
canonical_content: false
entity_kind: weapon_pattern
pattern_id: fixture_drive
frame_id: fixture_line
hand_requirement: "2H"
primary_operation: fixture_drive_fire
supports_focus: true
focus_operation: fixture_drive_focus
magazine_capacity: 1
shot_consumption: 1
reload_service_ref: "[[05_Combat_Survival/Diagnostic_Fixtures/fixture_drive#fixture_drive_reload]]"
operation_ids:
  - fixture_drive_fire
  - fixture_drive_focus
  - fixture_drive_reload
---
# fixture_drive — двухручный удерживаемый выпуск

Второй Pattern [[05_Combat_Survival/Diagnostic_Fixtures/fixture_line]] собирает импульс вдоль длинной оси. Он занимает обе руки, удерживает линию во время подготовки и может поразить два совмещённых открытых тела одним выпуском. Стена останавливает импульс; он не решает встречу за углом. Один выпуск за сервис — диагностическая конфигурация, без вывода об экономической равноценности двух Pattern.

## fixture_drive_fire
[operation_id:: fixture_drive_fire]

Primary press/hold готовит line solution, release после видимого сбора принимает Commit и расходует один magazine unit; ранний release отменяет подготовку без выпуска. Камера обычная, полоса preview показывает линию и готовность. Сбор позволяет медленный шаг с широким envelope, но разворот за новой целью сбрасывает сбор. Шум и свет вдоль корпуса дают противнику время уйти за укрытие. После выпуска обе руки возвращают опущенную ось; до освобождения coordinated claim нельзя мгновенно исполнить несовместимое Q либо перейти ко второму оружию. Промах сохраняет расход; прерывание после Commit не возвращает его.

Если уже готов Focus того же owner, press Primary принимает его решение и завершённый сбор в Commit. Это единственный переход Preparation → Commit, без параллельного накопления двух подготовок. Focus не меняет назначение Primary и не создаёт Alt.

Handling этого Pattern выражает тот же [[04_Player_Entities/Proficiency_Arsenal|возврат контролируемой линии]]: ограниченное исполнение требует коррекции поднятой оси после Recovery, уверенное оставляет её у края нужного коридора, исключительное — внутри. Дополнительная опора меняет вид телесного движения, но не переносимую пространственную задачу Frame; базовый долг остаётся.

## fixture_drive_focus
[operation_id:: fixture_drive_focus]

Hold Focus собирает и стабилизирует линию с обеими руками: стопы неподвижны, facing удерживается, светящаяся продольная полоса заметна противнику. Камера сохраняет обычный обзор. Только завершённый settle даёт узкий envelope; движение сбрасывает его. Отпускание отменяет подготовку, не стреляет и освобождает позу через опускание корпуса. Q/E, R и Switch Set прекращают intent. Встреча на фланге до settle делает unprepared Primary с широким envelope либо отход разумнее Focus.

## fixture_drive_reload
[operation_id:: fixture_drive_reload]

R связывает эту неполную конструкцию с одним Full ItemID Ready Access. Нижняя рука удерживает устройство у тела; верхняя прекращает рабочий хват и замыкает сервисный контакт у крепления батареи. При энергетическом Commit тот же источник становится Drained на прежнем месте, magazine становится 1. До него оба энергетических состояния неизменны. Затем верхняя рука возвращает хват; Action освобождает coordinated claim после видимого восстановления опоры. Другой объект в этой руке или оставшийся claim блокирует процедуру. Физическая история и прерывания следуют [[05_Combat_Survival/Magic_Batteries]] и [[05_Combat_Survival/Combat_Three_Debts]].
