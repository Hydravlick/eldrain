---
type: system
status: active
system: player_core
tags: [two_paradox, vectors, topology, analysis, synergy]
related_files:
  - "[[04_Player_Entities/_Matrices/00_Synergy_Map|Карта Двойного Парадокса и authored-взаимодействий]]"
  - "[[04_Player_Entities/_Registries/Registry_Races|Реестр рас]]"
  - "[[04_Player_Entities/_Registries/Registry_Specs|Реестр практик]]"
  - "[[04_Player_Entities/_Registries/Registry_Combos|Реестр hero-kit]]"
  - "[[04_Player_Entities/MVP_3x3_Design_Contract|Контракт MVP-матрицы 3×3]]"
---
# Матрица Двойного Парадокса

Двойной Парадокс — **автоматическая аналитическая топология** проекта. Он нужен, чтобы видеть всю карту `Race × Spec`, будущие расширения, формальные давления, прикрытия и общие риски без ручного заполнения каждого matchup.

Это не T.O.U.C.H. и не его замена. T.O.U.C.H. был универсальной игровой валютой характеристик, способной влиять на множество действий Пешки. Вектор Двойного Парадокса:

- не имеет числового уровня и не прокачивается;
- не меняет gunfeel, P/Q/E, Frame, proficiency, модульную ёмкость или Access;
- не является скрытым Power Score;
- существует как координата карты и источник дизайнерских гипотез.

## 1. Канонические векторы и доминация

Каждая строка ниже является машинно-читаемым источником истины. `dominates` означает формальное окно давления в топологии, а не автоматический урон, победу или контрпик.

### hazard
[vector_id:: hazard]
[vector_label:: Биохимия]
[dominates:: shadow, kinetics, ballistics]

### shadow
[vector_id:: shadow]
[vector_label:: Тень]
[dominates:: kinetics, tech, aether]

### kinetics
[vector_id:: kinetics]
[vector_label:: Кинетика]
[dominates:: tech, ballistics, detection]

### tech
[vector_id:: tech]
[vector_label:: Техника]
[dominates:: ballistics, aether, hazard]

### ballistics
[vector_id:: ballistics]
[vector_label:: Дальнее давление]
[dominates:: aether, detection, shadow]

### aether
[vector_id:: aether]
[vector_label:: Эфир]
[dominates:: detection, hazard, kinetics]

### detection
[vector_id:: detection]
[vector_label:: Сенсорика]
[dominates:: hazard, shadow, tech]

## 2. Автоматический профиль пересечения

Раса и практика публикуют по одному `base_vector`. Карта вычисляет профиль любой координаты, даже если её P/Q/E ещё `pending`:

```text
ComboVectors(Race, Spec) = unique(Race.base_vector, Spec.base_vector)
WeakTo(v) = все source_vector, для которых v входит в source_vector.dominates
SharedWeakness(Race, Spec) = WeakTo(Race.base_vector) ∩ WeakTo(Spec.base_vector)

RawPressure(A, B) = число directed dominance A.vectors -> B.vectors
NetPressure(A, B) = max(0, RawPressure(A, B) - RawPressure(B, A))
```

Если оба родителя имеют один вектор, пересечение получает `mono_vector_fusion`: один активный вектор и полный набор входящих слабостей этого вектора. Это диагностирует концентрацию, но не усиливает итоговый hero-kit автоматически.

## 3. Что карта имеет право утверждать

Автоматический слой отвечает на вопросы:

- где комбинация находится в общей топологии;
- какие формальные давления между координатами асимметричны по `NetPressure`;
- какую уязвимость два родителя разделяют;
- какие составы концентрируют один и тот же риск;
- где расширение рас, практик, мобов и POI оставляет пустой либо перенасыщенный участок карты.

Эти ответы существуют **до** готового контента и потому полезны для проектирования в ширину. Они являются картой вопросов, а не готовыми ответами баланса.

## 4. Authored-подтверждение

Полный hero-kit всё ещё проектируется отдельно и владеет P/Q/E, арсеналом, модулями, decision signature, Exposure и `counterplay_now`. Второй слой [[04_Player_Entities/_Matrices/00_Synergy_Map|Synergy Map]] проверяет, как формальная связь реализована или опровергнута в фактической сцене.

```text
структурное ребро Двойного Парадокса
  -> гипотеза о давлении, прикрытии или общем риске
  -> authored action / named window / observable Exposure
  -> playtest
  -> подтверждённая контра, опровергнутая гипотеза или намеренное исключение
```

Векторное ребро не обязано превращаться в прямой matchup. Но дизайнер не должен терять его молча: готовая ячейка либо показывает фактическую реализацию, либо фиксирует, почему authored-kit нарушает структурное ожидание.

## 5. Граница с игровыми свойствами

Любой игровой объект по-прежнему имеет собственные свойства. Вектор может классифицировать функцию объекта (`attack_vector`, `weakness_vector`, `dominant_vector`, временный `frame_vector`), но не заменяет локального владельца и его параметры.

Например, `attack_vector:: shadow` связывает моба с общей картой, но реальная атака всё равно обязана назвать телеграф, геометрию, урон, окно и counter action. `base_vector:: tech` у Крысы не ускоряет руки и не создаёт способность; он ставит её телесную линию в топологию Двойного Парадокса.

## 6. Правила представления

- Counter-матрица показывает `NetPressure`, а не почти полностью заполненный сырой score.
- Сырые причины остаются в пояснении ячейки и диагностике плотности.
- `support` по покрытию слабостей помечается как гипотеза, пока named windows не подтверждают фактическую поддержку.
- `shared_weakness` показывается как предупреждение состава, не как линия доминации.
- Authored-слой не заменяет автоматический: обе карты отвечают на разные вопросы и отображаются рядом.
