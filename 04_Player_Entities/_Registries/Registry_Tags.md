---
type: registry
status: active
system: player_entities_registry
registry_type: personal_tags
tags: [database, personal_tags, chronicle, mastery, mutations, relics]
related_files:
  - "[[04_Player_Entities/Tags_System|Personal Tags]]"
  - "[[04_Player_Entities/Trait_Development|Chronicle]]"
  - "[[04_Player_Entities/Proficiency_Arsenal|Arsenal and Proficiency]]"
  - "[[04_Player_Entities/Shell_Foundlings|Найдёныши]]"
  - "[[06_Economy_Loot/Extraction_Stabilization_Loop|Extraction and Breakline]]"
---
# Реестр личных тегов

> Реестр хранит необратимые факты жизни Пешки, а не хорошие и плохие броски. Chronicle-запись использует `Trouble -> Leverage -> Residue`; mastery и мутации используют собственные грамматики, но подчиняются тому же пределу Major Tags.

## Правила реестра

- У одной Пешки не более четырёх `[major_tag:: true]`; Origin занимает одно обычное место.
- `rarity` описывает частоту источника, а не потенциал человека. Она не отменяет tell, цену или контригру.
- Тег не меняет базовый gunfeel, P/Q/E, арсенал, `prof`, `module_capacity`, Access или общий combat stat.
- Одновременно foreground может стать только одна личная ситуация Пешки.
- `design_status:: prototype` означает проверяемый пример контента, а не финальную калибровку.

---

## Шаблон

### Шаблон Chronicle-трейта
[id:: template_chronicle_trait]
[tag:: template_chronicle_trait]
[tag_kind:: chronicle]
[major_tag:: true]
[source_kind:: survived_event]
[source_event:: event_id]
[rarity:: common]
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
[continuation_seed:: none]
[does_not_affect:: gunfeel, p_q_e, arsenal, module_capacity, access]
[design_status:: template]

* **Игровая сцена:** когда и почему эта память снова становится настоящей.
* **Читаемость:** что игрок замечает до решения.
* **Цена:** что невозможно сохранить вместе с Leverage.
* **После:** какое состояние мира или отношений остаётся.

---

## Prototype: прожитое решение

### Имена раньше груза
[id:: names_before_cargo]
[tag:: names_before_cargo]
[tag_kind:: chronicle]
[major_tag:: true]
[source_kind:: survived_event]
[source_event:: abandoned_value_to_preserve_named_person_or_witness]
[rarity:: common]
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
[tag_kind:: scar]
[major_tag:: true]
[source_kind:: breakline]
[source_event:: survived_body_only_breakline]
[rarity:: uncommon]
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
- Origin получает дополнительную способность или место сверх четырёх Major Tags;
- один trait запускает второй поверх себя;
- решение требует знания скрытого будущего вместо текущей позиции и доступных предметов.
