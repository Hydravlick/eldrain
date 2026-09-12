---
status: active
system: life_closure
tags: [lifecycle, permanent_choice, civic_outcome]
related_files:
  - "[[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]]"
type: "system"
index_route: "owner"
index_group: "player_entities"
index_order: 200
index_summary: "Определяет состояния, разрешение и связи: Life Closure."
read_when: "Когда нужен контракт «Life Closure» и его границы с соседними владельцами."
---
# Life Closure

Life Closure — необязательное осмысленное завершение полевой жизни конкретной Пешки. Человек может навсегда остаться жить в городе; долгая жизнь без Closure также допустима. Его ценность реализуется через действия, работу, отношения, риск и достигнутые результаты в течение жизни. Окончание не обязано компенсировать эту ценность и не служит обязательной ротацией или обменом человека на account power.

## Responsibility

`LIFE_CLOSURE` владеет eligibility, экземпляром authored closure arc, её конкретным offer, подтверждением и immutable `LifeClosureResolution`. Он читает факты истории у их владельцев, не создаёт отдельную общую биографию, не назначает Traits, не раскрывает их, не выдаёт предметы, услуги или репутацию и не принимает нового человека в ростер.

[[04_Player_Entities/Lifecycle_Roster|Lifecycle Roster]] потребляет terminal факт и единолично проецирует готовность и deployment. [[03_Factions_Societies/Quest_Engine|Quest]] и другие work owners хранят свою работу и факты её исполнения; Body, Tags и lifecycle owners предоставляют собственные факты. Они не разрешают Closure вместо этого владельца.

## Authored opportunity и offer

Конкретные authored facts истории и конкретная authored terminal opportunity дают основание предложения именно этой Пешке. Trait slots не измеряют полноту жизни. Универсального порога числа reserved/revealed manifestations, life/maturity score, рейдов, возраста, Scar count или Proficiency нет. Отдельная arc может требовать конкретный Trait, Scar, relationship или work fact, если это причинно необходимо; наличие свойства само по себе не превращается в стоимость человека.

Предложение закреплено за `PawnID` и своей authored причиной. Для обычного civic Closure подтверждение требует живую READY Пешку в Hub и сохраняющиеся условия предложения. Чтение истории и возникновение возможности не выводят человека из deployment. First Return condition и Dawn settlement не выбираются здесь.

```text
authored history facts + authored terminal opportunity
  → OFFER_AVAILABLE
      accept + confirm при валидных условиях
        → LifeClosureResolution
        → terminal projection у Lifecycle Roster
      decline
        → этот offer окончательно отклонён
        → дальнейшая field life сохраняется
      defer
        → тот же offer доступен, пока сохраняются его реальные условия
```

Отказ хранится для конкретного offer. Он не запрещает обычное civic ending через иное предложение или будущую Closure из причинно независимой истории. Переименование или повтор той же причины не создаёт новое предложение для обхода отказа. Cancel, reconnect, Breakline, Recovery, повторный вход и смена UI не reroll-ят arc, не отменяют её отказ и не создают более выгодный offer. Отмена до confirmation не создаёт terminal результата; defer не начисляет выгоду и не продлевает утраченное основание.

При изменении реальных условий доступность переоценивается с объяснением причины. Ни открытие Hub, ни чтение карточки не требуют немедленного выбора. Нет искусственного таймера давления, случайного оффера или ожидания как способа исправить farming.

## Подтверждение и ordinary civic Closure

До confirmation игрок видит конкретное предложение, почему оно относится к этой Пешке, что она потеряет, что гарантировано и какие уже полученные результаты сохранятся. Неопределённое будущее последствие не показывается гарантированной наградой. Предварительный выбор accept ещё не является terminal исходом.

При confirmation владелец повторно проверяет условия и актуальную Presence. Успешное подтверждение фиксирует единственный необратимый `LifeClosureResolution`; устаревшая карточка не может закрыть уже недоступного человека. Повтор обработки возвращает тот же исход. Совместимость с deployment проверяется по авторитетной Presence, а не по выбранному экрану; принятый исход нельзя откатить через reconnect или задержку потребителя.

Обычный `CLOSE_CIVIC` создаёт `LifeClosureResolution=CLOSED_CIVIC`: человек остаётся живым в городе и навсегда покидает ordinary field deployment. Он не redeploy-ится, не становится обычным cargo, MIA, KIA или recruitment content, не возвращается через Spawn. Traits, Proficiency, Body и Scars не передаются следующей Пешке.

Обычный безопасный civic Closure допустим без account reward. Special institutional offer не является единственным способом осмысленно закончить полевую жизнь; наличие выгодного downstream результата не является общим условием Closure.

У другого человека может быть собственное authored civic ending. Ограничение повторного институционального результата ниже не запрещает завершать разные личные жизни; оно запрещает заново получать уже созданное право за смену PawnID.

## Граница работы и результата

Work result != Closure reward. Уже выполненная работа получает результат у своего владельца в момент completion. ItemID, изготовленный результат, заработанный исследованием recipe, доказанный факт, переданный источник, исполненное обязательство и иной completed externalized result не удерживаются до retirement и не выдаются повторно после него.

| Слой | Death | Closure |
|---|---|---|
| Personal / embodied | LOST | Больше недоступно для deployment; не наследуется |
| Unfinished work | RE-EVALUATE у work owner | RE-EVALUATE у work owner |
| Completed result | Сохраняется под собственным owner | Не меняется самим окончанием; сохраняет собственные правила |
| Terminal action | Смерть не создаёт Closure | Может создать одно специально authored внешнее следствие нового добровольного поступка |

`KIA` закрывает незавершённую closure arc без LifeClosureResolution. Другие terminal death/loss outcomes также не превращаются потребителем в Closure. Закрытие arc не удаляет все незавершённые работы: их владельцы переоценивают требования и доступного исполнителя. Сохранённый результат продолжает расходоваться, уточняться или утрачиваться по своим правилам. Closure не является `death + reward`.

## Named downstream consequence

Life Closure публикует факт окончания, а заранее названный downstream owner может разрешить только своё последствие. Сам terminal action должен создавать новый причинный факт, которого не было после уже выполненной работы.

Проверка authored записи: **если Пешка продолжила бы field life после уже выполненной работы, что именно ещё не произошло?** Если ответа нет, результат принадлежит work completion, а не Closure. Перенос выплаты другому owner эту проверку не заменяет.

- [[03_Factions_Societies/Reputation_Rules|Reputation]] и [[03_Factions_Societies/Pledge_Contracts|Pledge]] разрешают собственные отношения и допуски, не наследуют личную дружбу.
- [[04_Player_Entities/Grimoire_Truth_Triangulation|Гримуар]] ведёт источник и проверку знания; terminal факт сам не доказывает истинность показания.
- [[06_Economy_Loot/Barter_System|RecipeTransaction]], [[06_Economy_Loot/Vendor_Logic|Vendor]] и [[08_World_Generation/Hub/Hub_Services_Interaction|Service]] сохраняют свои технические, экономические и интерфейсные границы. Возможность последствий не учреждает permanent recipes, новую услугу или vendor ladder.

Authored запись называет unresolved дело, новый факт terminal action, единственного owner внешнего следствия и конкретный результат. До confirmation этот owner проверяет условия обещанного результата. Принятый факт и обработка потребителем должны переживать повторную доставку без второй выдачи или возврата Пешки в поле. Это handoff существующих владельцев, не Closure Reward Manager.

## Anti-farming и сохранённый результат

Единица внешнего результата — конкретное unresolved дело и конкретная terminal action, разрешающие одно причинное institutional следствие. Consumer различает новое реальное дело и повтор той же причины другим человеком. Уже созданное институциональное право не выдаётся снова только потому, что пришёл новый `PawnID`. Идемпотентность одного сообщения и неповторяемость результата дела — разные проверки; обе нужны у потребителя.

Запрещены account XP, generic reputation payout за Closure, конверсия stats, Scar count, Proficiency, возраста или raid count в reward value, progression level от числа CLOSED Pawns, Keeper XP, Closure currency, retirement levels, универсальная reward table, generic legacy power и inherited strength. Closure не ускоряет recruitment, не reroll-ит кандидатов и не улучшает Continuity. Cooldown, случайный offer, повышенный threshold, таймер или дорогая жизнь не исправляют per-Pawn payout.

Созданный результат может сохраниться, но CLOSED Pawn не является permanent worker, discount/income/recipe source, service condition, production slot или account modifier. После handoff результат действует под собственным owner без проверки продолжающегося CLOSED-статуса человека как условия выгоды. Накопление закрытых людей не производит новые права. Общая система account progression и Biography Manager здесь не создаются.

## Keeper extension point

Account-level Keeper Recognition отличается от Pawn-specific Keeper terminal offer. Признание непрерывной воли Осколка через последствия нескольких жизней описано в [[04_Player_Entities/Entity_Grimoire#Позднее раскрытие|Entity Grimoire]] и [[03_Factions_Societies/Lore/The_Keepers#Позднее Прямое Общение|лоре Хранителей]]. Оно не является Closure/death/retired counter или biography score и само не создаёт terminal offer.

Будущее предложение требует specific cause, specific Pawn, specific unresolved matter и specific terminal consequence. Высокий Proficiency, возраст или Scar count не являются достаточным основанием. До отдельного решения fiction-specific branch не зарегистрирован: не установлены передача Хранителям, смерть, потеря памяти, CLOSED_CIVIC, Archive access, recipe или service.

Будущая ветка сначала определяет, что физически происходит с человеком, есть ли его информированное согласие, почему terminal outcome необходим и какой owner получает новый факт. Без доказанной terminal необходимости результат остаётся обычным work result. UR-003 о Dawn остаётся открытым у [[04_Player_Entities/Lifecycle_Resolver|Lifecycle Resolver]]; этот extension point не создаёт новый death или revive path.

## Проверяемые границы

```yaml
life_closure_contract:
  owner: LIFE_CLOSURE
  role: optional_field_life_ending
  long_life_without_closure: valid
  eligibility: authored_history_facts_and_terminal_opportunity
  universal_progress_gate: false
  specific_fact_requirement: causal_only
  offer_state: OFFER_AVAILABLE
  accept_requires: [explicit_confirmation, living_ready_pawn_in_hub, valid_offer_conditions, authoritative_presence]
  decline_scope: specific_offer
  decline_irreversible: true
  independent_future_offer_allowed: true
  defer: same_offer_while_real_conditions_hold
  reroll_sources: []
  immediate_hub_decision_required: false
  artificial_pressure_timer: false
  result: immutable_LifeClosureResolution
  ordinary_outcome: CLOSED_CIVIC
  ordinary_reward_required: false
  accepted_redeploy: false
  accepted_recruit_or_spawn: false
  accepted_ordinary_cargo: false
  inherited_embodied_value: false
  death_creates_closure: false
  unfinished_work: re_evaluate_by_work_owner
  completed_result_timing: work_completion
  completed_result_reissued: false
  downstream_requires: [named_owner, specific_unresolved_matter, new_terminal_causal_fact, specifically_authored_consequence]
  downstream_result_unit: unresolved_matter_and_terminal_action
  downstream_dedup: [resolution_delivery, same_cause_across_pawn_ids]
  generic_per_pawn_payout: false
  generic_account_power: false
  pawn_metrics_as_reward: false
  closed_pawn_as_service_condition: false
  result_continuation_owner: result_domain
  keeper_recognition_creates_offer: false
  keeper_recognition_counter: false
  keeper_terminal_branch_registered: false
  keeper_terminal_rewards: []
  keeper_extension_requires: [physical_fate, informed_consent, terminal_necessity, receiving_owner]
```
