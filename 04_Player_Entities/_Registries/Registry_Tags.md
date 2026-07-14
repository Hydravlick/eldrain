---
type: registry
status: active
system: player_entities_registry
registry_type: chronicle_traits
tags: [database, chronicle, traits, extraction, situations]
related_files:
  - "[[04_Player_Entities/Tags_System|Chronicle-трейты: системный слой]]"
  - "[[04_Player_Entities/Trait_Development|Развитие Chronicle]]"
  - "[[04_Player_Entities/Shell_Foundlings|Найдёныши]]"
  - "[[06_Economy_Loot/Extraction_Stabilization_Loop|Extraction and Breakline]]"
---
# Реестр Chronicle-трейтов

> Реестр хранит личные ситуации, а не хорошие и плохие броски. Каждая запись обязана содержать `Trouble -> Leverage -> Residue` и использовать общий потолок Chronicle независимо от происхождения Пешки.

## Правила реестра

- `Origin` является значением `source_kind`, а не редкостью и не отдельным пулом.
- Трейт не меняет gunfeel, P/Q/E, арсенал, `module_capacity`, Access или общий combat stat.
- Одновременно foreground может стать только одна личная ситуация Пешки.
- Конкретное число активных записей остаётся `UNKNOWN` до прототипа.
- `design_status:: prototype` означает проверяемый пример контента, а не финальную калибровку.

---

## Шаблон

### Шаблон Chronicle-трейта
[id:: template_chronicle_trait]
[tag:: template_chronicle_trait]
[trait_kind:: chronicle]
[source_kind:: survived_event]
[source_event:: event_id]
[situation_family:: threshold]
[foreground_weight:: authored_context]
[trouble_trigger:: visible_condition]
[trouble_rule:: world_or_decision_change]
[trouble_tell:: player_visible_cue]
[leverage_condition:: chosen_action_and_cost]
[leverage_rule:: one_situational_permission_or_exchange]
[leverage_cost:: time_and_exposure]
[residue_success:: consequence_id]
[residue_refusal:: consequence_id]
[residue_failure:: consequence_id]
[exclusive_with:: none]
[evolves_to:: none]
[continuation_seed:: none]
[does_not_affect:: gunfeel, p_q_e, arsenal, module_capacity, access]
[design_status:: template]

* **Игровая сцена:** когда и почему эта память снова становится настоящей.
* **Читаемость:** что игрок замечает до решения.
* **Цена:** что невозможно сохранить вместе с Leverage.
* **После:** какое состояние мира или отношений остаётся.

---

## Prototype: Origin

### Последний сигнал Порта
[id:: port_last_signal]
[tag:: port_last_signal]
[trait_kind:: origin]
[source_kind:: origin]
[source_event:: extracted_sealed_port_foundling]
[situation_family:: threshold, contract]
[foreground_weight:: port_sector_and_open_origin_continuation]
[trouble_trigger:: old_port_relay_enters_local_signal_range]
[trouble_rule:: relay_answers_the_foundling_and_emits_a_public_wake]
[trouble_tell:: named_voice_fragment_and_visible_relay_pulse]
[leverage_condition:: power_the_relay_hands_busy_with_one_carried_battery]
[leverage_rule:: reveal_one_additional_local_threshold_search_direction]
[leverage_cost:: battery, time, public_signal]
[residue_success:: origin_continuation_advances_and_relay_becomes_public_trace]
[residue_refusal:: continuation_remains_static_without_penalty]
[residue_failure:: relay_trace_becomes_disputed]
[exclusive_with:: none]
[evolves_to:: none]
[continuation_seed:: return_to_the_port_relay]
[does_not_affect:: gunfeel, p_q_e, arsenal, module_capacity, access]
[design_status:: prototype]

* **Сцена:** Порт узнаёт человека раньше, чем город успевает объяснить ему собственную гибель.
* **Решение:** батарея может стать маршрутом к выходу или остаться запасом на бой; включённый relay услышат все рядом.
* **Граница:** сигнал не открывает Порог и не даёт точный маркер — он добавляет направление к обычному физическому поиску.

---

## Prototype: прожитое решение

### Имена раньше груза
[id:: names_before_cargo]
[tag:: names_before_cargo]
[trait_kind:: relationship]
[source_kind:: survived_event]
[source_event:: abandoned_value_to_preserve_named_person_or_witness]
[situation_family:: custody, threshold, contract]
[foreground_weight:: carried_trace_tied_to_unresolved_person]
[trouble_trigger:: pawn_reaches_manifest_commitment_with_the_named_trace]
[trouble_rule:: trace_cannot_be_privately_settled_until_its_human_address_is_chosen]
[trouble_tell:: manifest_names_the_missing_person_and_refuses_private_seal]
[leverage_condition:: surrender_private_claim_and_register_the_trace_as_public_witness]
[leverage_rule:: receive_one_address_or_route_response_from_the_responsible_hearth]
[leverage_cost:: private_item_value, time, obligation]
[residue_success:: named_person_chain_advances_and_claim_becomes_public]
[residue_refusal:: cargo_remains_disputed_for_later_resolution]
[residue_failure:: witness_chain_records_the_broken_custody]
[exclusive_with:: none]
[evolves_to:: none]
[continuation_seed:: missing_name_address]
[does_not_affect:: gunfeel, p_q_e, arsenal, module_capacity, access]
[design_status:: prototype]

* **Сцена:** Пешка умеет превратить спорный груз в свидетельство, но только отказавшись от частной прибыли.
* **Граница:** это не бесплатный контракт; личная цепочка занимает обычный foreground и reward budget.

---

## Prototype: Breakline

### Шов, который помнит
[id:: seam_that_remembers]
[tag:: seam_that_remembers]
[trait_kind:: scar]
[source_kind:: breakline]
[source_event:: survived_body_only_breakline]
[situation_family:: catastrophe]
[foreground_weight:: later_breakline_in_similar_geometry]
[trouble_trigger:: catastrophe_opens_blind_seams]
[trouble_rule:: old_echo_adds_one_convincing_false_direction_and_makes_the_wake_earlier]
[trouble_tell:: doubled_body_echo_and_out_of_phase_direction]
[leverage_condition:: stop_hands_busy_and_burn_remaining_device_charge_to_test_the_echo]
[leverage_rule:: identify_the_false_direction_before_committing_to_a_seam]
[leverage_cost:: device_charge, time, stronger_wake]
[residue_success:: false_seam_becomes_a_trace_for_nearby_parties]
[residue_refusal:: pawn_chooses_without_confirmation]
[residue_failure:: pursuers_receive_the_same_false_and_true_wake]
[exclusive_with:: none]
[evolves_to:: none]
[continuation_seed:: none]
[does_not_affect:: gunfeel, p_q_e, arsenal, module_capacity, access]
[design_status:: prototype]

* **Сцена:** прошлый побег не делает следующий безопаснее; он создаёт узнаваемую ложь, которую можно проверить ценой времени.
* **Граница:** Breakline и повтор одного и того же побега не гарантируют появление этого трейта.

---

## Проверка записи

Трейт не проходит в `approved`, если:

- `trouble_trigger` не виден до решения;
- `leverage_cost` можно передать другому игроку без эквивалентного риска;
- `residue_*` возвращаются к исходному состоянию без следа;
- его проще оценить как rarity, DPS или «идеальный roll»;
- Origin получает дополнительную способность или слот;
- один trait запускает второй поверх себя;
- решение требует знания скрытого будущего вместо текущей позиции и доступных предметов.
