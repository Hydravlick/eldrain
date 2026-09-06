from importlib.machinery import SourceFileLoader
import re,json
w=SourceFileLoader('w','.refactor_work.py').load_module()
R=w.ROOT
def edit(stem,fn):
 p=w.find(stem);w.write(p,fn(p.read_text(encoding='utf-8')))
def append(stem,heading,body):
 edit(stem,lambda s:s+'\n## '+heading+'\n\n'+body.strip()+'\n')
def metadata():
 w.meta(w.find('Culture_Design_Grammar'),dict(type='core_concept',system='world_lore',index_route='owner',index_group='world_lore',index_order=15,index_summary='Задаёт историческую грамматику культур: эпохи, общественные противоречия и границы телесного детерминизма.',read_when='При разработке народа или проверке культурной причинности.'))
 for stem,system in [('Hub_Dispatch_Investigation_Context','hub_research'),('Generation_Algorithm_Research','generation_research')]:
  p=R/'10_Reference'/f'{stem}.md';w.meta(p,dict(type='reference',status='superseded_contextual' if stem.startswith('Hub') else 'draft',system=system))
  s=p.read_text(encoding='utf-8');end=s.index('\n---',4)+4
  intro=('\n\n# Гипотезы алгоритма генерации\n\nНепроверенная исследовательская записка. Перечисленные алгоритмы, порядок стадий, оценки сложности и интерактивные инструменты — кандидаты для эксперимента, а не принятый runtime pipeline. Текущие обязанности генерации задают [[08_World_Generation/Generation/Generation_Strategies]] и [[08_World_Generation/Generation/World_Topology]].\n' if stem.startswith('Generation') else '\n\nКонтекст прежнего варианта расследований и отправок. Действующий путь задают [[01_Core_Vision/Features/Knowledge_Investigation]], [[03_Factions_Societies/Quest_Engine]] и [[08_World_Generation/Hub/Hub_Services_Interaction]]; эта записка не выдаёт правила доступа, наград или readiness.\n')
  w.write(p,s[:end]+intro+s[end:])
 m=json.loads((R/'.refactor_moves.json').read_text(encoding='utf-8'))
 m.update({'09_Project_Management/People_Design_Framework.md':'02_World_Lore/Culture_Design_Grammar.md','09_Project_Management/Hub_Dispatch_Investigation_Design.md':'10_Reference/Hub_Dispatch_Investigation_Context.md','09_Project_Management/Generation_Algorithm_Notes.md':'10_Reference/Generation_Algorithm_Research.md'})
 w.write(R/'.refactor_moves.json',json.dumps(m,ensure_ascii=False,indent=2))
def registries():
 p=w.find('Registry_Tags');s=p.read_text(encoding='utf-8');a,b=w.section(s,'## Правила реестра')
 w.write(p,s[:a]+'## Правила реестра\n\nПожизненные места, формы, сигналы и ограничения действия определяет '+w.ref('Tags_System')+'; допуск Frame-mastery рассчитывает '+w.ref('Proficiency_Arsenal')+'.\n\nЗапись публикует `tag_form:: light | situational`, точные поля выбранной формы и ссылку на зарегистрированный сигнал. Frame-mastery называет один `mastery_frame` и ровно одно из полей: `mastery_step:: 1` либо `mastery_expression`. `design_status:: concept` и `prototype` не означают финальную калибровку.\n\n'+s[b:])
 w.transfer('Registry_Environment_States','## Как игрок читает среду','Anomaly_System')
 p=w.find('Registry_Environment_States');s=p.read_text(encoding='utf-8')
 para=re.search(r'^Personal Tag может.*$',s,re.M)[0]
 append('Tags_System','Чтение локального средового инстанса',para)
 s=s.replace(para,'Связь тега с локальным `state_id` проверяет '+w.ref('Tags_System')+'.')
 para=re.search(r'^Один инстанс обязан.*$',s,re.M)[0]
 append('Anomaly_System','Граница локального средового состояния',para)
 s=s.replace(para,'Схема описывает один локальный инстанс; правила его действия и последствия принадлежат '+w.ref('Anomaly_System')+'.')
 w.write(p,s)
 p=w.find('Registry_Mobs');s=p.read_text(encoding='utf-8');para=re.search(r'^`HP / AR / SPD`.*$',s,re.M)[0]
 append('Ballistics_PvE','Совместимость физиологии и воздействий',para)
 w.write(p,s.replace(para,'Совместимость воздействия с физиологией и границы тюнинга определяет '+w.ref('Ballistics_PvE')+'.'))
 # Entity selectors should survive moves as well as current folder cleanup.
 for p in R.glob('0*/**/*.md'):
  s=p.read_text(encoding='utf-8');n=re.sub(r'''dv\.pages\('\"04_Player_Entities/(?:Races|Specs)\"'\)\.where\(page => page\.entity_kind === \"(race|spec)\"\)''',lambda m:'dv.pages().where(page => page.type === "entity" && page.status === "active" && page.entity_kind === "'+m[1]+'")',s)
  if n!=s:w.write(p,n)
def feature_polish():
 edit('Extraction',lambda s:s.replace(w.ref('Frequency_Tuner'),w.ref('Extraction_System')).replace(w.ref('Item_Attributes_UI'),w.ref('Extraction_Stabilization_Loop')))
 rows={
 'Pawn_Lifecycle':('Одна выбранная Пешка, успешное возвращение, потеря и следующий доступный вход; отдельный тест показывает незавершённую Recovery без ложного обещания срока.','UX связывает ростер с объяснением исхода; narrative сохраняет имя и причину привязанности; gameplay и QA воспроизводят потерю и повторный вход.'),
 'Expedition_Preparation':('Один полностью заданный комплект с работающим preview и один недопустимый вариант установки; неопубликованные topology не подменяются условными числами.','Art и animation показывают место установки и телесные ограничения; UX называет причину отказа; gameplay и QA сопоставляют preview с рейдовой конфигурацией.'),
 'Raid_Entry':('Один сектор, solo и party подтверждение, устаревшая quote и отказ до Breach; региональное масштабирование проверяется отдельно.','UX показывает цену и конечный результат подтверждения; level design обеспечивает валидных кандидатов; gameplay и QA проверяют commit и восстановление соединения.'),
 'Exploration_Traversal':('Одна сборка Порта с различимыми альтернативами пути, следом и отказом от опасного прохода; повторный заход меняет маршрутную задачу.','Level design собирает различающиеся подходы; art, audio и VFX делают причину читаемой; QA проверяет доступность контрхода и отсутствие слепого обязательного прохода.'),
 'Combat':('Одна полная связка тела, Frame и P/Q/E в сцене «Непрошеный гость»: попадание, срыв обязательства, отход и бой с третьей стороной.','Animation и gameplay согласуют tell, попадание и Recovery; audio/VFX различают контакт с пластиной и уязвимостью; QA проверяет движущиеся тела, а не неподвижную мишень.'),
 'Looting_Carry':('Одна спорная находка, смена custody, рост нагрузки и физическая потеря; один предмет проходит до итогового Stash.','UX объясняет занятую руку и недоступное действие; animation показывает перенос; gameplay и QA проверяют гонку за одним ItemID и исчезновение носителя.'),
 'Extraction':('Найти Порог, завершить и прервать Sync, разойтись с группой; отдельно воспроизвести body-only отказ и фазовую границу.','Level design оставляет читаемый поиск и контригру; audio/VFX показывают рождение шва и reset; UX объясняет вместимость и личный исход; QA проверяет спор за груз.'),
 'Loot_Return':('Один физически вынесенный ItemID, спорный manifest и повторная доставка результата; игрок видит один итоговый возврат.','Gameplay связывает custody и durable manifest; UX объясняет судьбу каждого спорного предмета; QA проверяет повтор, reconnect и сбой между подготовкой и commit.'),
 'Contracts':('Один field-контракт меняет маршрут и момент выхода, один Hub-only контракт находится рядом с материальной сделкой; отказ от обоих оставляет обычную вылазку.','Quest design задаёт конкретную процедуру и стороны; UX различает сделку и цель; narrative сохраняет мотив заказчика; QA проверяет провал, отказ и повтор награды.'),
 'Living_Table':('Выбор Пешки, осмотр вернувшегося груза, адрес и переход к следующей вылазке на одном Столе.','UX и art связывают карту, вещи и живых людей; narrative и audio дают короткие реакции на последствия; QA проверяет путь без обязательной прогулки по Хабу.'),
 'Resource_Addressing':('Одна находка с основным и альтернативным адресом, недостающий ингредиент и исполненная RecipeTransaction.','Economy/content design задаёт конечный рецепт; UX показывает недостающее; narrative объясняет интерес адресата; QA проверяет расход и отказ без скрытого контракта.'),
 'Living_World':('Один сектор проходит наблюдаемое изменение локального POI и завершение ревизии; account-знание показывается отдельно от общей топологии.','World и level design авторствуют смену сцены; audio/VFX показывают её заранее; gameplay и QA проверяют переход при разных Presence и повторном входе.'),
 'Personal_Development':('Известный профиль и заранее назначенный First Return при обычном возвращении; один личный тег имеет видимые действие и цену.','Narrative связывает проявление с человеком; UX отличает раскрытие от выдачи случайной силы; combat design и QA проверяют локальность эффекта и отсутствие reroll-оптимума.'),
 'Knowledge_Investigation':('Один физический след, проверка его происхождения и использование подтверждённого знания в следующем выборе маршрута.','Content и narrative design создают проверяемое свидетельство; UX показывает известное и неподтверждённое; gameplay и QA сохраняют источник при возврате и повторном просмотре.')}
 for stem,(scope,production) in rows.items():
  p=w.find(stem);s=p.read_text(encoding='utf-8')
  s=re.sub(r'`active` означает.*?\n\n',f'Первый срез: {scope} Связный сценарий задаёт [[01_Core_Vision/Build_Extraction_Concept_Slice]], очередь работ — [[09_Project_Management/TODO]]. `specified` означает описание, `untested` — отсутствие подтверждённого испытания.\n\n',s,count=1)
  s=re.sub(r'^Нужны .*$',production,s,flags=re.M);w.write(p,s)
 for stem,owners in [('Combat',['Skill_Execution','Interaction_Constraints']),('Expedition_Preparation',['Calibration_Contract']),('Looting_Carry',['Interaction_Constraints'])]:
  p=w.find(stem);s=p.read_text(encoding='utf-8')
  s=s.replace('system_owners:\n','system_owners:\n'+''.join('  - '+json.dumps(w.ref(x))+'\n' for x in owners))
  s=s.replace('Правила и переходы: ','Правила и переходы: '+', '.join(w.ref(x) for x in owners)+', ');w.write(p,s)
def lore():
 dest=R/'08_World_Generation/Content/Faction_Encounter_Seeds.md'
 out='''---
type: content
status: draft
system: faction_encounter_content
content_kind: encounter_seeds
logic_owners:
  - "[[03_Factions_Societies/Quest_Engine]]"
  - "[[03_Factions_Societies/Quest_Engine_Grammar]]"
  - "[[03_Factions_Societies/Registries/Registry_Faction_Interfaces]]"
---
# Сцены, поручения и адреса Очагов

Авторские заготовки связывают учреждения с конкретными проблемами вылазки. Это сохранённые примеры из игровых разделов фракционных страниц, ранее помеченных `Downstream interface drift`; они ещё не являются опубликованными Quest, Recipe или POI definitions. История, люди и гражданские обязанности остаются в страницах сущностей.

Для производства выбрать одну сцену, оформить её конечные inputs, действие, отказ и результат у соответствующего владельца, затем создать отдельную запись. Сам список не выдаёт лечение, доступ, награду, изменение доверия или страхование. Принятые интерфейсы и незаданные системные владельцы перечислены в [[03_Factions_Societies/Registries/Registry_Faction_Interfaces]].

'''
 for p in sorted((R/'03_Factions_Societies/Lore').glob('*.md')):
  s=p.read_text(encoding='utf-8');parts=[]
  label=re.search(r'^player_label: (.*)$',s,re.M);access=re.search(r'^access_model: (.*)$',s,re.M)
  for heading in ['## Что получает игрок','## Квестовые глаголы','## Мастера и временные POI']:
   if heading not in s:continue
   a,b=w.section(s,heading);chunk=s[a:b]
   # This is civic ethics, not a service condition; keep it in the institution.
   ethics=re.search(r'^Минимум нельзя использовать.*$',chunk,re.M)
   if ethics:chunk=chunk.replace(ethics[0]+'\n','');s=s[:a]+ethics[0]+'\n\n'+s[b:]
   else:s=s[:a]+s[b:]
   chunk=re.sub(r'> \[!warning\] Downstream interface drift\n>[^\n]*\n\n','',chunk)
   chunk=chunk.replace('## Что получает игрок','### Предложенные взаимодействия').replace('## Квестовые глаголы','### Сюжеты поручений').replace('## Мастера и временные POI','### Места и участники сцены')
   parts.append(chunk.strip())
  if p.stem=='The_Cathedral':
   a=s.index('Игрок получает в Соборе:');b=s.index('### Почему Собор терпят',a)
   chunk=s[a:b];chunk=re.sub(r'> \[!warning\] Downstream interface drift\n>[^\n]*\n\n','',chunk)
   parts.append('### Предложенные взаимодействия\n\n'+chunk.replace('Игрок получает в Соборе:','Возможные сцены и услуги:').strip());s=s[:a]+s[b:]
  if not parts and not label and not access:continue
  fid=re.search(r'^faction_id: (.*)$',s,re.M)[1].strip();title=re.search(r'^# (.*)$',s,re.M)[1]
  out+='## '+fid+'\n\nСущность: [['+p.relative_to(R).with_suffix('').as_posix()+'|'+title+']].\n\n'
  if label:out+='[player_label:: '+label[1]+']\n'
  if access:out+='[access_model:: '+access[1]+']\n'
  out+='\n'+'\n\n'.join(parts)+'\n\n'
  s=re.sub(r'^(?:player_label|access_model):.*\n','',s,flags=re.M)
  # Only routing remains in Lore; examples live together in authored content.
  if parts:s+='\n## Игровые связи\n\nПринятые роли и границы: [[03_Factions_Societies/Registries/Registry_Faction_Interfaces]]. Заготовки сцен и поручений: [[08_World_Generation/Content/Faction_Encounter_Seeds#'+fid+'|'+title+']].\n'
  w.write(p,s)
 w.write(dest,out)
 edit('Registry_Factions',lambda s:s.replace('  player_label AS "Игроковый контур",\n',''))
 edit('Faction_Relationships',lambda s:s.replace('.filter(page => page.entity_kind === "faction")','.filter(page => page.type === "entity" && page.status === "active" && page.entity_kind === "faction")'))
 edit('The_Common_Storehouses',lambda s:re.sub(r'Бытовой минимум и боевой Welfare — не одно и то же\..*?(?=\n\n)', 'Еда, вода, кров и экстренная помощь остаются гражданским правом. Боевой комплект — отдельная материальная поддержка; условия её получения определяет [[04_Player_Entities/Spawn_Logic#3. Фиксированный Welfare loan|Spawn Logic]].',s,count=1))
 edit('Pawn_Lifecycle',lambda s:s.replace('Нет готовых Пешек, но есть CARE или незавершённая Recovery: интерфейс объясняет причину ожидания.','Нет готовых Пешек, но есть CARE или незавершённая Recovery: интерфейс показывает решение Continuity Admission и следующий доступный шаг.'))
 # Institutional claims from legacy seeds cannot silently override accepted owners.
 with (R/'09_Project_Management/TODO.md').open('a',encoding='utf-8') as f:
  f.write('\n## Контент городских взаимодействий\n\n- [ ] Оформить выбранные [[08_World_Generation/Content/Faction_Encounter_Seeds|сцены Очагов]] в отдельные Quest/Recipe/POI definitions. Сначала решить `MISSING_OWNER` для planned-интерфейсов в [[03_Factions_Societies/Registries/Registry_Faction_Interfaces]]; гражданское свидетельство само по себе не задаёт игровое разрешение.\n')

def management():
 # Replace normative mitigation copies with the evidence still needed to close risk.
 criteria={
 'R06':'Сначала принять отдельное страховое решение; затем проверить его влияние на ставку пермадета.',
 'R07':'Спроектировать и испытать девять ячеек; различимость и полноту оценивать по общему контракту, а не по наличию строк.',
 'R23':'Пройти тихую первую вылазку и попытки suicide-reroll; проверить объяснение Origin без каталога скрытой силы.',
 'R27':'Сравнить полную стоимость замены и повторяемую добычу Armor Rat с альтернативными комплектами.',
 'R28':'Испытать группу с одним дорогим Frame на параллельной работе, длительном давлении и повторных дорогих циклах.',
 'R32':'Проверить широкий набор задач и контрмер: личный тег не должен вытеснить профиль без наблюдаемой цены.',
 'R34':'Для каждого заблокированного пакета получить topology, pattern-bound coverage и atomicity proof либо split; отсутствие данных оставляет публикацию заблокированной.',
 'R40':'Сравнить прибыль и командную полезность сохранённой Ready-Пешки с регулярно жертвуемым Ward.',
 'R47':'Пройти gearless, нулевой Ready-ростер, CARE и повторную попытку входа в ту же сессию после потери.',
 'R48':'Проверить враждебный вынос и цепочки передачи Foundling; согласие и происхождение должны оставаться прослеживаемыми.',
 'R57':'Проверить поиск выхода поздним solo-входом и группами, знающими карту; измерить устойчивость постоянного лагеря.',
 'R58':'Воспроизвести прерванный Sync, убийство носителя и гонку за грузом; сопоставить наблюдаемую вместимость с custody.',
 'R59':'Проверить движущиеся, приседающие и разворачивающиеся тела с Projectile/Sweep; проигравший объясняет пластину, шов и доступный контрход.',
 'R61':'Измерить marginal leverage каждого terminal в дуэли, маршруте и группе: TTK, батарея, контакт, число целей, Exposure и извлечение.',
 'R62':'Атаковать доступность wreck и ForfeitBeneficiarySet через геометрию, squad, посредников и последующие сессии.',
 'R63':'Воспроизвести hard-veto, отсутствие точки, ABORT и сбой на границе Breach; сверить единственность участия и тела.',
 'R64':'Сравнить минимум две доктрины полного профиля и пройти account-loop модуля до допуска installable.',
 'R65':'Наблюдать изменение обычных решений вылазки с контрактом и валидный raid без контракта; проверить давление chores и FOMO.',
 'R68':'Провести обычный ItemID через общий Stash и материальную сделку рядом с Hub-only Quest; проверить независимость readiness.'}
 p=R/'09_Project_Management/Risk_Register.md';s=p.read_text(encoding='utf-8')
 def row(m):
  cols=m[0].split('|');rid=cols[1].strip()
  if rid not in criteria:return m[0]
  owners=cols[5]
  def link(x):
   try:return w.ref(x[1])
   except AssertionError:
    p=R/'09_Project_Management'/(x[1]+'.md')
    return '[['+p.relative_to(R).with_suffix('').as_posix()+']]' if p.exists() else x[0]
  owners=re.sub(r'`([^`]+)`',link,owners)
  return '| '+rid+' | '+cols[2].strip()+' | '+criteria[rid]+' | '+cols[4].strip()+' | '+owners.strip()+' |'
 s=re.sub(r'^\| R\d+ \|.*$',row,s,flags=re.M).replace('## Решения MVP','## Риски MVP').replace('| Решение |','| Что нужно проверить или решить |')
 s=s.replace('## Риски MVP','Описанные правила читаются по ссылкам на владельцев. Все строки ниже остаются открытыми; реестр не свидетельствует о проведённых испытаниях.\n\n## Риски MVP')
 w.write(p,s)
 # Adopted exclusions are already owned; keep production scope and specific links.
 p=R/'09_Project_Management/TODO.md';s=p.read_text(encoding='utf-8');a=s.index('## Отсечено или помещено в карантин');b=s.index('## Reference sources',a)
 s=s[:a]+'''## Границы ближайшей работы

Первый срез не требует полной матрицы девяти ячеек, прогулочного Хаба, дорогих катсцен или полной экономики. Расширение следует после проверки связного сценария в [[01_Core_Vision/Build_Extraction_Concept_Slice]].

Принятые ограничения читаются у владельцев: [[05_Combat_Survival/Hunt_Frontier_Loop]] (причины движения), [[06_Economy_Loot/Barter_System]] (материальная сделка), [[04_Player_Entities/Shell_Foundlings]] (человек и происхождение), [[04_Player_Entities/Spawn_Logic]] (Welfare), [[08_World_Generation/Hub/Hub_Services_Interaction]] (услуги), [[07_Gear_Inventory/Thermos_System]] (рейдовая сборка). Их повторное введение в задаче требует явного продуктового решения.

'''+s[b:];w.write(p,s)
 # Current architecture and preserved slice replace obsolete execution choreography.
 destinations={
 'Canonical_Refactor_Migration_Map_2026-07-23':'09_Project_Management/Architecture_MVP',
 'Lore_Gameplay_Boundary_Refactor_Plan_2026-07-23':'03_Factions_Societies/Registries/Registry_Faction_Interfaces',
 'Worldbuilding_Refactor_Roadmap_2026-07-23':'02_World_Lore/Culture_Design_Grammar',
 'Hunt_Frontier_Ecosystem_Design':'08_World_Generation/Content/Hunt_Frontier_Slice',
 'Hunt_Frontier_Ecosystem_Implementation_Plan':'09_Project_Management/TODO'}
 for p in R.glob('0*/**/*.md'):
  if p.stem in destinations:continue
  s=p.read_text(encoding='utf-8');n=s
  for old,new in destinations.items():
   n=re.sub(r'\[\[09_Project_Management/'+old+r'(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]', '[['+new+']]',n)
   n=n.replace('09_Project_Management/'+old+'.md',new+'.md')
  if n!=s:w.write(p,n)
 for old in destinations:(R/'09_Project_Management'/f'{old}.md').unlink()

def links():
 fixes={
 '04_Player_Entities/Lifecycle_Roster#1. Колода Оболочек (Shell Deck)':'04_Player_Entities/Lifecycle_Roster#Pawn record and Presence',
 '03_Factions_Societies/Lore/Civic_Ethos_Under_Lamps#Распределенная безопасность':'03_Factions_Societies/Lore/Civic_Ethos_Under_Lamps#Безопасность глазами улицы',
 '04_Player_Entities/Registries/Registry_Parameter_Contracts#dissonance_occurrence':'04_Player_Entities/Registries/Registry_Parameter_Contracts#`dissonance_occurrence`',
 '05_Combat_Survival/Combat_Three_Debts#Закон окна':'05_Combat_Survival/Combat_Three_Debts#4. Закон окна',
 '08_World_Generation/Anomaly/Anomaly_Core_Loop#3. Режиссёр как экология следов':'08_World_Generation/Anomaly/Anomaly_Core_Loop#Директор как экология следов',
 '08_World_Generation/Generation/Server_Lifecycle#2. Три Фазы Эволюции Одной Локации':'08_World_Generation/Generation/Server_Lifecycle',
 '04_Player_Entities/Lifecycle_Roster#4. Смерть и Неопределенная Судьба':'04_Player_Entities/Lifecycle_Resolver',
 '08_World_Generation/Persistence_Ledger#2. Глобальная Персистентность (Final Stabilization)':'08_World_Generation/Persistence_Ledger',
 '08_World_Generation/Anomaly/Anomaly_Core_Loop#3. Режиссер (The Director AI)':'08_World_Generation/Anomaly/Anomaly_Core_Loop#Директор как экология следов',
 '09_Project_Management/Worldbuilding_Refactor_Roadmap_2026-07-23':'02_World_Lore/Culture_Design_Grammar'}
 for p in list(R.glob('0*/**/*.md'))+list(R.glob('10_Reference/**/*.md')):
  s=p.read_text(encoding='utf-8');n=s
  for old,new in fixes.items():n=n.replace(old,new)
  if n!=s:w.write(p,n)
 edit('Item_Calibration_Matrix',lambda s:s.replace('registry_type = "consumables"','registry_type = "necessary_consumables" OR registry_type = "headwear"'))
 p=R/'09_Project_Management/Open_Design_Decisions.md';s=p.read_text(encoding='utf-8')
 s=s.replace('# Реестр неразрешённых расхождений рефактора','# Открытые продуктовые решения')
 s=s.replace('Player lifecycle, Tags, player-facing return flow',w.ref('Lifecycle_Roster')+', '+w.ref('Tags_System')+', '+w.ref('Lifecycle_Resolver'))
 s=s.replace('Last Thread, Lifecycle Roster, Recovery Lifecycle, Raid ingress, UI projection',w.ref('Last_Thread_Recovery')+', '+w.ref('Lifecycle_Roster')+', '+w.ref('Recovery_Lifecycle')+', '+w.ref('Raid_Approach_and_Entry'))
 s=s.replace('Life Closure, Pawn lifecycle, Tags, Dawn settlement',w.ref('Life_Closure')+', '+w.ref('Lifecycle_Resolver')+', '+w.ref('Tags_System'))
 s=re.sub(r'^Recovery, которая.*$', 'Принятый исход Recovery на Dawn находится у '+w.ref('Recovery_Lifecycle')+'. В `UR-002` остаётся открытым только начало и течение Case clock.',s,flags=re.M)
 w.write(p,s)
 m=json.loads((R/'.refactor_moves.json').read_text(encoding='utf-8'));m['09_Project_Management/Refactor_Unresolved_Registry_2026-07-23.md']='09_Project_Management/Open_Design_Decisions.md';w.write(R/'.refactor_moves.json',json.dumps(m,ensure_ascii=False,indent=2))
def navigation_polish():
 p=R/'01_Core_Vision/Feature_Map.md';s=p.read_text(encoding='utf-8')
 for f in (R/'01_Core_Vision/Features').glob('*.md'):
  data=f.read_text(encoding='utf-8');name=re.search(r'^display_name: (.*)$',data,re.M)[1].strip('"');path=f.relative_to(R).with_suffix('').as_posix()
  s=re.sub(r'^(\d+\. )\[\['+re.escape(path)+r'\]\]',lambda m:m[1]+'[['+path+'|'+name+']]',s,flags=re.M)
 s=s.replace('file.link AS "Feature"','link(file.path, display_name) AS "Feature"');w.write(p,s)
 p=w.find('Registry_Thermoses');s=p.read_text(encoding='utf-8');s=re.sub(r'^Models remain blocked.*$', 'Готовность definition и участие support delta проверяет [[07_Gear_Inventory/Thermos_Assembly]]. `blocked_topology` в записи явно отмечает отсутствие опубликованной геометрии и не разрешает сборку.',s,flags=re.M);w.write(p,s)
 # Canon-facing provenance points to the actual open work, not deleted execution plans.
 p=w.find('Registry_Faction_Interfaces');s=p.read_text(encoding='utf-8');s=s.replace('  - "[[03_Factions_Societies/Registries/Registry_Faction_Interfaces]]"','  - "[[08_World_Generation/Content/Faction_Encounter_Seeds]]"');w.write(p,s)
if __name__=='__main__':
 import sys
 globals()[sys.argv[1]]()
