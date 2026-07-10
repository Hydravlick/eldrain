---
type: weapon_frame
status: active
system: combat_survival
frame_id: hook_polearm
display_name: Обход щита
weapon_family: polearm
frame_vector: kinetics
vector_scope: commitment
activates_on:
  - hook
  - reap_recovery
primary_window_function: exploit
creates_window:
  - none
implicit_keyword: reap
exploits_window:
  - shield_flank
mitigates_window:
  - none
exposure_channels:
  - close_commit
  - whiff_recovery
  - armor_check
frame_power: 3
exposure_weight: 3
mastery_unlock:
  - hook_reset
mvp_verdict: support
mvp_reason: Показывает фрейм как ответ на щит и угол, но требует уже понятной мили-геометрии.
sort_order: 320
tags:
  - weapon_frame
  - weapons
  - polearm
related_files:
  - "[[05_Combat_Survival/_Registries/Registry_Weapons|Registry_Weapons]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Proficiency_Arsenal]]"
---
# Обход щита

Этот фрейм не проламывает защиту напрямую, а ищет боковой угол и край щита. Он силён против неверно поставленного блока, но слабее держит прямой вход.

## Варианты

### Боевая коса (War Scythe) [2H]
[variant_id:: war_scythe]
[tier:: 1]
[weight:: 4.0kg] | [dmg:: 42]
[heat:: 0] | [dissonance_pulse:: 0]
[combo_chain:: Draw Cut -> Shield Reap -> Step Reset]
[alt_action:: None]
[combo_reset:: пауза после Ready возвращает цепочку к Draw Cut]

Лезвие под углом, заходящее за блок.

- **Мувсет:** жёстко прописанный изогнутый хитбокс (Arc Sweep) появляется в нужный кадр, смещённый в сторону — это позволяет обогнуть щит противника сбоку.
- **Implicit:** `reap` использует неверный угол защиты, но хуже держит прямой вход.
- **Слабость:** хуже держит прямой вход и требует правильного угла; фаза Recovery длится дольше секунды, спам невозможен.

### Осмотический Хлыст (Osmotic Lash) [2H]
[variant_id:: osmotic_lash]
[tier:: 2]
[weight:: 2.8kg] | [dmg:: 38]
[heat:: 0] | [dissonance_pulse:: 0]
[combo_chain:: Cross Sweep -> Overhead Crack]
[alt_action:: None]
[combo_reset:: пауза после Ready возвращает цепочку к Cross Sweep]

Гибкое древко без real-time физики цепи: хитбокс жёстко прописан как дуга.

- **Мувсет:** взмах справа налево с хитбоксом, смещённым влево, огибающий щит противника сбоку; второй удар — прямой хлёсткий удар сверху вниз, оглушающий цель.
- **Implicit:** `reap` здесь читается через огибание щита дугой, а не через геометрию древка.
- **Слабость:** ещё длиннее Recovery, чем у Косы (дольше секунды); полностью исключает повторный спам.
- **Отличие:** легче Косы и лучше обходит щит по дуге, но не имеет прямого укола и наказывает промах ещё дольше.
