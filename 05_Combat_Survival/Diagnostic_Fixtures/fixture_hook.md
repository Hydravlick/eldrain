---
type: entity
system: combat_survival
status: draft
publication_state: diagnostic_fixture
canonical_content: false
entity_kind: weapon_pattern
pattern_id: fixture_hook
frame_id: fixture_contact
hand_requirement: "1H"
primary_operation: fixture_hook_sweep
supports_focus: false
operation_ids:
  - fixture_hook_sweep
---
# fixture_hook — короткая боковая дуга

Pattern [[05_Combat_Survival/Diagnostic_Fixtures/fixture_contact]] даёт вторую Primary для dual. У него нет magazine, Battery service, Alt или dedicated Focus. Это диагностический контактный инструмент, а не название production-класса.

## fixture_hook_sweep
[operation_id:: fixture_hook_sweep]

Press Primary принимает Commit в короткую горизонтальную дугу от рабочего плеча к центру. Она задевает близкую цель сбоку от взгляда, если плечо и траектория имеют место; вне контакта не достаёт, стена останавливает дугу. Target solution — contact arc относительно своего тела, камера обычная; поворот плеча заранее показывает сторону удара. Попадание создаёт локальный толчок тела, без гарантированного прерывания любого Action или нового статуса.

Рабочая рука и опора корпуса заняты до завершения дуги и возврата плеча. Промах оставляет корпус открытым; прерывание следует собственной фазе Recovery, смена оружия не очищает claims. Другая Primary в dual доступна после совместимого release, а не одновременно с несовместимым разворотом.

Ограниченное владение после дуги требует заново собрать рабочую опору; уверенное возвращает плечо в рабочее положение; исключительное сохраняет контроль края контактного сектора. Это локальное исполнение [[04_Player_Entities/Proficiency_Arsenal|Proficiency]], не ускорение всех Actions. Числа прототипа не заданы. Источник runtime — [[05_Combat_Survival/Combat_Three_Debts]].
