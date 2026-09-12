---
type: entity
system: combat_survival
status: draft
publication_state: diagnostic_fixture
canonical_content: false
entity_kind: weapon_pattern
pattern_id: fixture_tap
frame_id: fixture_line
hand_requirement: "1H"
primary_operation: fixture_tap_fire
supports_focus: true
focus_operation: fixture_tap_focus
magazine_capacity: 2
shot_consumption: 1
reload_service_ref: "[[05_Combat_Survival/Diagnostic_Fixtures/fixture_tap#fixture_tap_reload]]"
operation_ids:
  - fixture_tap_fire
  - fixture_tap_focus
  - fixture_tap_reload
---
# fixture_tap — короткий одиночный выпуск

Конструкция внутри [[05_Combat_Survival/Diagnostic_Fixtures/fixture_line]] выпускает один прямой импульс на press Primary. Два выпуска после одного сервиса — пробное значение для различения magazine и Battery; это не рекомендация ёмкости. Alt отсутствует: RMB single Set сообщает отсутствие операции.

## fixture_tap_fire
[operation_id:: fixture_tap_fire]

Primary принимает Commit на press: выстрел по текущей оси, один magazine unit, видимая вспышка и толчок кисти. Попадание ограничено первой преградой. Без Focus широкий допуск попадания пригоден по близкой крупной цели, но не обещает попадание в узкую щель. Стабилизированное решение Focus этого ItemID сужает envelope; Primary принимает его в тот же Action transition. Нет дополнительной автоматической атаки.

Рабочая рука и управление линией заняты до видимого возврата кисти; движение до и после выстрела разрешено, но выстрел не очищает остаточные claims. После телесного возврата устройство может ещё остывать. Промах, прерывание после выпуска и смена Set сохраняют расход и долг. Ни Heat, ни телесный возврат не обнуляются reload.

Handling: ограниченное владение оставляет ось после отдачи вне выбранного коридора — требуется видимая коррекция кистью; уверенное исполнение возвращает её к краю коридора; исключительное возвращает внутрь. Это локальное качество возврата по [[04_Player_Entities/Proficiency_Arsenal]], без изменения времени анимации, magazine, урона, moveset или долга. Точные углы и длительность человеческой коррекции измеряются прототипом.

## fixture_tap_focus
[operation_id:: fixture_tap_focus]

Hold Focus готовит line target solution собственного ItemID. Preview показывает текущий коридор рассеивания, камера сохраняет обычный обзор. Для узкого коридора нужно остановиться и удержать facing до завершения settle; шаг снимает накопленную стабилизацию. Поднятая неподвижная кисть и светящаяся ось дают tell. Это оплачивается потерянным временем и exposure до выпуска. Отпускание отменяет подготовку без выстрела; нового attack Recovery не возникает. После отмены кисть опускается по release path. Q/E, R и Switch Set прекращают intent по [[05_Combat_Survival/Weapon_Core#Weapon Focus]].

## fixture_tap_reload
[operation_id:: fixture_tap_reload]

R обслуживает один неполный magazine по [[05_Combat_Survival/Magic_Batteries#3. Reload и получатель энергии]]. Оружие удерживается рабочей рукой; вторая действительно свободная рука открывает сервисный контакт, подтверждает конкретный Full ItemID в доступном креплении и замыкает его. Энергетический Commit атомарно разряжает источник и наполняет magazine до 2. Drained остаётся там же. До этого Commit отмена сохраняет Full и magazine; после него кисть закрывает контакт и возвращается, не возвращая ресурс. Dual требует физически убрать вторую вещь перед этой процедурой. Время зависит от манипуляций; «пустая позиция» не отменяет чужой claim.

Операции задают требования; [[05_Combat_Survival/Combat_Three_Debts|Action]] хранит принятые claims/Recovery. Независимые экземпляры и сцены находятся в [[09_Project_Management/Diagnostic_Fixtures/fixture_batch7]].
