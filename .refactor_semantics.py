from importlib.machinery import SourceFileLoader
import re,json,subprocess
w=SourceFileLoader('w','.refactor_work.py').load_module();R=w.ROOT

# The address overview is synthesis; concrete routing, eligibility and settlement have owners.
p=w.find('Faction_Address_System');w.meta(p,{'type':'core_concept','system':'faction_address_overview'})
s=p.read_text(encoding='utf-8');s=s.replace('Эта страница отвечает на вопрос **как пользоваться фракциями в игре и GDD**.','Эта страница связывает городские нужды с адресами и объясняет **как пользоваться фракциями в игре и GDD**. Правила доступа, расчёта и provenance принадлежат системам в разделе «Интеграция в механику»; примеры адресации не являются опубликованными RecipeTransaction.')
line='- стандартный предмет имеет основной адрес и максимум одну альтернативу; два-три адреса нужны активному бартерному ингредиенту, а четыре и больше резервируются для редких, спорных, Trace/Disputed или сюжетных вещей;'
assert line in s
q=w.find('Resource_Cycle');t=q.read_text(encoding='utf-8');t+='\n## Число адресов и сложность находки\n\n'+line[2:].rstrip(';')+'.\n';w.write(q,t)
s=s.replace(line,'- число осмысленных назначений предмета определяет '+w.ref('Resource_Cycle')+';')
w.write(p,s)

# Registry_Factions' action table duplicates the explicit reputation owner.
p=w.find('Registry_Factions');s=p.read_text(encoding='utf-8');a,b=w.section(s,'## Типы действий');s=s[:a]+'## Типы действий\n\nИгровые изменения доверия и нарушения договора: '+w.ref('Reputation_Rules')+'.\n\n'+s[b:]
a=s.index('> **Правило реестра:**');b=s.index('Старые черновые фракции',a);s=s[:a]+'Реестр хранит контракт идентичности и отношений; значения принадлежат страницам сущностей. Игровые интерфейсы перечислены в '+w.ref('Registry_Faction_Interfaces')+', правила участия — в '+w.ref('Pledge_Contracts')+'.\n\n'+s[b:]
arch=R/'09_Project_Management/Architecture_MVP.md';ar=arch.read_text(encoding='utf-8')
a=ar.index('Отношения хранятся');b=ar.index('[[03_Factions_Societies/Registries/Registry_Factions|Registry_Factions]] после',a)
s+='\n## Контракт отношений\n\n'+ar[a:b]
s+='\n## Свойства фракционной сущности\n\n```yaml\ntype: entity\nentity_kind: faction\nstatus: active\nsystem: factions\nfaction_id: first_reception\ndisplay_name: Круг Первого Приёма\nfaction_role: major\nsort_order: 10\npromise: никто не остаётся один перед неизвестным состоянием\n```\n\n`faction_id` остаётся стабильным. Карта отношений читает `rel_*` на самой сущности: '+w.ref('Faction_Relationships')+'.\n'
w.write(p,s)

# Common world identity and runtime constraints leave the POI record store.
p=w.find('Registry_POIs');s=p.read_text(encoding='utf-8');a=s.index('### Общий POI и отношение аккаунта');b=s.index('## Контракт рейдового Реквиема',a)
block=s[a:b]
q=w.find('Location_Revision_Lifecycle');w.write(q,q.read_text(encoding='utf-8')+'\n## Общий POI и отношение аккаунта\n\n'+block.split('\n',1)[1])
s=s[:a]+'### Общий POI и отношение аккаунта\n\nСостояние и разграничение общей ревизии и знания аккаунта: '+w.ref('Location_Revision_Lifecycle')[:-2]+'#Общий POI и отношение аккаунта]].\n\n'+s[b:]
first='Реквием создаётся только как вариант уже существующего рейдового POI. Он не является постоянным пином Хаба, отдельной линией мутации или персональной инстанс-локацией.'
start=s.index('`constant_ref` и `relic_trace_family_ref`');end=s.index('# 0. Центральные Пины',start);rule=s[start:end]
q=w.find('Anomaly_System');w.write(q,q.read_text(encoding='utf-8')+'\n## Рейдовый Реквием\n\n'+first+'\n\n'+rule)
s=s.replace(first,'Поля наложения исполняются по '+w.ref('Anomaly_System')[:-2]+'#Рейдовый Реквием]].');s=s.replace(rule,'Смысл полей и обязательные сигналы: '+w.ref('Anomaly_System')[:-2]+'#Рейдовый Реквием]].\n\n')
a=s.index('> **Концепция Карты:**');b=s.index('## Контракт адресного POI',a)
s=s[:a]+'Представление фаз, выбор цели и переход к подготовке принадлежат '+w.ref('Hub_Map_Table')+' и '+w.ref('Raid_Approach_and_Entry')+'.\n\n'+s[b:]
a=s.index('# 3. UX Взаимодействие');b=s.index('## 0. Нулевой пациент: шаблон POI',a)
s=s[:a]+'# Представление на Столе\n\n'+w.ref('Hub_Map_Table')+' показывает опубликованную ревизию и известные источники; '+w.ref('Raid_Approach_and_Entry')+' раскрывает и подтверждает ставку. Поля POI не выбирают точку высадки и не дают Бригадиру перки Пешки.\n\n'+s[b:]
w.write(p,s)
q=w.find('Hub_Map_Table');t=q.read_text(encoding='utf-8');t+='\n## Подсказка об источнике\n\nКарточка известного источника может сообщать «Сигнал: высокое содержание медикаментов»; для неизвестной структуры она показывает неопределённость. Основанием служит доступное аккаунту свидетельство по '+w.ref('Grimoire_Truth_Triangulation')+', а не личный перк выбранной Пешки. Выбор силуэта передаёт намерение во входной поток; он сам не назначает точку materialization.\n';w.write(q,t)
p=w.find('The_Entity');s=p.read_text(encoding='utf-8');law='У Реквиема всегда есть ранний читаемый признак, человеческая цена исходного решения и доступный путь отказа либо контригры. Сущность может довести правило до жестокой буквальности, но не вправе в T3 отменить уже прочитанное условие без нового ясного сигнала.'
assert law in s;s=s.replace(law,'Сущность доводит правило до жестокой буквальности. То, как игрок замечает наложение, отвечает на него или отказывается, определяет '+w.ref('Anomaly_System')[:-2]+'#Рейдовый Реквием]].')
law2='Поэтому один и тот же POI остаётся общим для всех игроков; личные решения могут менять лишь их доверие, доступный адрес и локальный след, но не топологию, физику или население сектора.'
assert law2 in s;s=s.replace(law2,'Общий слепок и личное знание о нём разделяет '+w.ref('Location_Revision_Lifecycle')+'.');w.write(p,s)
# New System has all operative constraints, fiction keeps cause and voice.

# Preserve the useful authored prototype specification, retire its obsolete migration instructions.
p=R/'09_Project_Management/Hunt_Frontier_Ecosystem_Design.md';s=p.read_text(encoding='utf-8')
a=s.index('## Первый MVP-срез:');b=s.index('## Карта внедрения',a);slice_text=s[a:b]
q=R/'08_World_Generation/Content/Hunt_Frontier_Slice.md';w.write(q,'---\ntype: content\nstatus: active\nsystem: prototype_slice\ncontent_kind: acceptance_scenario\nmaturity: specified\nlogic_owners: ['+json.dumps(w.ref('Hunt_Frontier_Loop'),ensure_ascii=False)+', '+json.dumps(w.ref('Extraction_System'),ensure_ascii=False)+']\n---\n\n# Непрошеный гость: прототипный срез\n\nАвторское задание на сцену и наблюдение. Оно применяет '+w.ref('Hunt_Frontier_Loop')+', '+w.ref('Ballistics_Armor')+' и '+w.ref('Extraction_System')+', не заменяя их разрешение. Реализованного результата и playtest evidence пока нет.\n\n'+slice_text)
for name in ['Combat','Exploration_Traversal','Extraction']:
 p=w.find(name);d=w.parse_frontmatter(p);w.meta(p,{'data_sources':d['data_sources']+[w.ref('Hunt_Frontier_Slice')]})

# Architecture keeps placement and reading directions, not predicates or entity schema.
a=ar.index('| Блок |');b=ar.index('\n---',a);domains=ar[a:b]
prose='''---
type: project_management
status: active
system: project_management
version: 4
---

# Архитектура GDD и границы MVP

Локальный vault — рабочая поверхность, Git — история и восстановление. Архитектура отвечает за размещение и связность документов; игровые решения принимают активные владельцы в доменах `01_`–`08_`.

## Два пути чтения

Новому дизайнеру: [[01_Core_Vision/GDD_Main]] → [[01_Core_Vision/01_Vision]] → [[01_Core_Vision/02_Core_Loop]] → [[01_Core_Vision/Feature_Map]] → Feature. Feature объясняет цель, сценарии, ожидаемую динамику, UX, зависимости и проверку.

Для правки правила: [[00_Index]] → доменный Route → System/Mechanic → Registry или authored Entity/Content. Lore объясняет людей, историю и причинность мира. View, Base и граф показывают связи источников и не принимают игровое решение.

Feature-страницы находятся в `01_Core_Vision/Features`: это общий путь игрока поверх доменов. Системы поддерживают несколько Features; создавать копию владельца внутри каждой Feature нельзя. Обратные связи и пропуски видны в [[01_Core_Vision/Views/Feature_Owner_Coverage]].

## Домены

'''+domains+'''

## Типы и источник значения

| Тип | Ответственность |
|---|---|
| `core_concept` | Vision, обещание, основной цикл и замысел |
| `feature` | законченная возможность, её сценарии и полнота интеграции |
| `system` | связная модель состояний, переходов и разрешения |
| `mechanic` | локальное действие или правило |
| `content` | авторская конфигурация правил или сценарий; `content_kind` уточняет семейство |
| `entity` | самостоятельная идентичность; `entity_kind` различает race, spec, faction, weapon_frame и location |
| `registry` | схема, стабильные записи и bounded interfaces; для каталога сущностей сами значения остаются на сущностях |
| `lore` | факты мира, культура, вера и историческая причинность |
| `view` | производное представление с `upstream_sources` |
| `index` | навигация |
| `project_management` | открытая работа, риск, решение о размещении |

Race/Spec и оружейный Frame имеют самостоятельные страницы. Их YAML — источник стабильных полей; семейные реестры читают их. Предметы, рецепты, теги и ячейки Combo остаются блоками реестра, пока им не нужен самостоятельный контекст. Вариант оружия остаётся внутри Frame. Большой реестр можно разделить по семейству без изменения ID и формата записи; отдельный файл на каждый ID не обязателен.

Контракт фракционной идентичности и направленных отношений — [[03_Factions_Societies/Registries/Registry_Factions]]; участие институтов в игре — [[03_Factions_Societies/Registries/Registry_Faction_Interfaces]]. Lore не разрешает награду, услугу или право на выход. Лорную синтезирующую прозу сохраняют, даже когда игровое правило переезжает.

## Имена и представления

Домены сохраняют числовой порядок; `00_Index` и `00_Routes` обозначают входы навигации. `01_Vision` → `02_Core_Loop` остаётся короткой последовательностью знакомства. В таблицах Порта `01`–`03` означают реальную сложность, также указанную в properties. Независимые системы Generation, Anomaly и Hub имеют семантические имена; их номера не образовывали pipeline.

`Registries`, `Views`, `Lore` и семейства контента обозначают ответственность. `_Matrices` больше нет. Матрица Двойного Парадокса остаётся System, потому что определяет топологию; Synergy Map читает её. Item Calibration Matrix — View, а состав испытаний задаёт [[07_Gear_Inventory/Calibration_Contract]].

DataviewJS сохраняется. Три таблицы сложности Порта вызывают один `tools/dataview/sector_difficulty/view.js`, передавая свойства wrapper. Ссылки на источники находятся в свойствах; путь custom view — техническая зависимость. Тестовые fixtures находятся в `tools/tests/fixtures`.

## MVP, зрелость и доказательства

[[01_Core_Vision/Build_Extraction_Concept_Slice]] и [[08_World_Generation/Content/Hunt_Frontier_Slice]] задают связный срез; [[09_Project_Management/TODO]] хранит незавершённые работы, [[09_Project_Management/Risk_Register]] — риски и необходимые свидетельства. Не весь объём каждой major Feature входит в первый прототип.

`status: active` означает актуальное описание, а не реализованную систему. `maturity: specified` означает описанные связи; `validation_state: untested` означает отсутствие подтверждённого результата испытаний. Значения `prototype_ready` и `validated` допустимы только после соответствующего свидетельства, а не после проверки Markdown.

## Читаемость и обслуживание

Первый экран объясняет ситуацию до схемы. Схема должна позволять исполнить правило без толкования метафоры. Обещание, цикл, условия и исключения раскрываются по сложности страницы; маленькой Mechanic не нужны пустые разделы. Машинный ключ отделён от имени, а атмосферная фраза сохраняется, когда объясняет цену, последствие или взгляд жителя.

Routes строятся из свойств источников и не редактируются вручную. Для переименования используется установленный Obsidian CLI, затем проверяются ссылки и arbitrary literals в скриптах, запросах и конфигурации. Валидаторы проверяют структуру, но не заменяют чтение и design review.
'''
w.write(arch,prose)

# TODO contains work, not a second adopted course. Preserve the unique post-loss UX in its owner.
p=R/'09_Project_Management/TODO.md';s=p.read_text(encoding='utf-8');a=s.index('## Зафиксированный курс');b=s.index('## Now:',a)
s=s[:a]+'Принятый путь игрока и границы возможностей: [[01_Core_Vision/Feature_Map]]. Порядок реализации ниже не меняет правил этих владельцев.\n\n'+s[b:]
s=s.replace('интегрировать материальные адреса Хаба, отдельные Quest-записи и общий путь обычного ItemID.','проверить сквозным прототипом уже описанные материальные адреса Хаба, отдельные Quest-записи и общий путь обычного ItemID.')
w.write(p,s)
p=w.find('Lifecycle_Resolver');s=p.read_text(encoding='utf-8');s+='\n## Объяснение личного исхода\n\nПосле потери игрок получает читаемую реконструкцию `предупреждение → обязательство → причина → следующий контрход`, а не только надпись KIA и таблицу урона. Экран объясняет уже принятое решение resolver и доступный следующий шаг; он не меняет судьбу человека.\n';w.write(p,s)

# Old calibration numbers are preserved as provenance, never restored as active item values.
old=subprocess.check_output(['git','show','HEAD:07_Gear_Inventory/Item_Calibration_Matrix.md']).decode('utf-8')
a,b=w.section(old,'## 3. Текущие Известные Значения Стартового Набора')
report=R/'10_Reference/Calibration_Starting_Observations.md'
w.write(report,'---\ntype: reference\nstatus: superseded_contextual\nsystem: calibration_context\n---\n\n# Исходные наблюдения стартового набора\n\nИсторическая таблица для сверки калибровки, не источник текущих значений. В текущих definitions Термоса topology и часть параметров ещё не опубликованы. Переносить эти числа в runtime без сверки нельзя. План проверки: '+w.ref('Calibration_Contract')+'.\n\n'+old[a:b])
print('Integrated ownership boundaries, prototype content, architecture and open-work cleanup')
