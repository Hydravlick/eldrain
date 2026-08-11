# Terra 5.6 High — микропромпт единой проходки

Используй модель `gpt-5.6-terra` с reasoning effort `high`.

Выполни `docs/plans/2026-08-11-canonical-corpus-prose-refactor-plan.md` как одну
полную проходку, читая сначала `AGENTS.md`, затем план,
`docs/audits/2026-08-11-canonical-prose-refactor-manifest.md` и
`docs/audits/2026-08-11-responsibility-migration-map.md`.

Работай напрямую в текущем checkout. `canonical-prose-refactor-manifest.md` и
`responsibility-migration-map.md` — writable execution state: обновляй их по
ходу работы, даже если они уже отмечены modified. Для других status-путей сначала
смотри `git diff -- <path>`: пустой diff является line-ending/stat noise и не
блокирует пакет. Содержательный посторонний diff сохрани и останови только
пересекающийся owner-пакет. Не делай stash/reset, не создавай ветки и коммиты.

Обязательные навыки: `eldraine-system-architect` как ведущий Pass B;
`eldraine-vault-curator` для
аудита, удаления AI-shaped prose и проверки границ; `eldraine-gdd-author` только
для одобренного переноса в канонического владельца; `eldraine-lorekeeper` для
фракций, сущностей и лорного смысла. Условные специалисты — строго по таблице
skill routing в плане и через один bounded handoff.

Это GDD/Markdown-рефактор. План является доменным контрактом, а не software
workflow. Редактируй текст owner-scoped пакетами, после
каждого пакета проверяй смысл, структуру и точный diff.

Pass A выполняется на уровне абзацев и секций внутри owner-страницы. Не своди
его к замене scanner-hit или одной строки: если дефект охватывает opening,
повтор тезиса, meta-scaffold или механически собранную секцию, перепиши весь
доказанный prose surface. `Bounded` означает один owner и ясные границы смысла,
а не минимальный diff.

Отдельно выполни массовую редактуру owner metadata. Для всех 126 owners замени
шаблонные `index_summary` и `index_when` конкретными owner-specific формулировками.
Начиная с `03_Factions_Societies`, summary должен ясно показывать первичную
ответственность LORE/ENTITY, MECHANIC, SYSTEM, INTERFACE REGISTRY, CONTENT
INSTANCE или PRESENTATION и не присваивать странице чужую runtime-власть.
Другие YAML-поля защищены. После каждого домена запускай
`python tools/build_routes.py --write` и принимай только точную generated
projection этих prose-полей.

Закрой все 116 owner-записей от `03_Factions_Societies` до
`08_World_Generation`: для каждого `AUDIT_REQUIRED` прочитай владельца и только
его прямые зависимости, добавь доказательный `DETAILED`-вердикт и явные границы
лор/сущность, механика, универсальная система и interface registry. Не изменяй
`02_World_Lore` в Pass B. Не придумывай владельцев или значения и не считай
повторяемые поля реестра AI-слопом. Переноси текст только для
`APPROVED_FOR_MIGRATION`, малыми owner-scoped пакетами, с обновлением прямых
потребителей и ссылок. В этой же сессии повышай доказанную строку до
`APPROVED_FOR_MIGRATION`, только если точные source/target/consumers не конфликтуют,
смысл и negative boundaries сохранены и не требуется новое правило, число,
хронология или дизайн-решение. Остальные строки оставляй явно заблокированными,
но не останавливай из-за них независимые потоки. Не делай вторую аудиторскую проходку;
заверши эту только когда `AUDIT_REQUIRED` не осталось.

После каждого пакета проверь точный diff и protected invariants. В финале запусти
существующие проектные валидаторы:

```powershell
python tools/test_responsibility_migration_map.py
python tools/test_eldraine_skill_contracts.py
python tools/test_vault_curator.py
python tools/test_canonical_guidance.py
python tools/test_management_hygiene.py
python tools/build_routes.py --write  # только если менялась owner metadata
python tools/vault_guard.py
git diff --check
```

Не обходи ошибки в исходниках. Если `vault_guard.py` падает только из-за
внешнего состояния среды, вынеси это отдельным environment blocker; не скрывай
результат и не меняй канон ради обхода.
