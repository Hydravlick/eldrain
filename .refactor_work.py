from pathlib import Path
import re, sys, json
sys.path.insert(0, 'tools')
from document_model import parse_frontmatter
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path.cwd()
def find(stem):
    matches=list(ROOT.glob('0[1-8]*/**/'+stem+'.md'))
    assert len(matches)==1,(stem,matches)
    return matches[0]
def ref(stem): return '[['+find(stem).relative_to(ROOT).with_suffix('').as_posix()+']]'
def write(p,s):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
def meta(p, updates, remove=()):
    s=p.read_text(encoding='utf-8-sig');m=re.match(r'---\n(.*?)\n---\n?',s,re.S);assert m,p
    fm=m[1]
    for key in (*remove,*updates):
        fm=re.sub(r'^'+re.escape(key)+r':[^\n]*(?:\n[ \t]+[^\n]*)*\n?', '',fm,flags=re.M)
    for k,v in updates.items():
        fm+='\n'+k+': '+json.dumps(v,ensure_ascii=False)
    write(p,'---\n'+fm.strip()+'\n---\n'+s[m.end():])

def features():
    # Each row follows a player decision, not a folder boundary.
    rows=[
    ('Pawn_Lifecycle','pawn_lifecycle','Живые Пешки и цена возвращения',
     'Выбрать конкретного человека для вылазки и понять его судьбу после успеха, потери или спасения.',
     'Связать ставку рейда с жизнью Пешки, сохранив понятный путь обратно к игре после потери.',
     ['Lifecycle_Roster','Lifecycle_Resolver','Last_Thread_Recovery','Recovery_Lifecycle','Life_Closure','Spawn_Logic','Shell_Foundlings'],['Registry_Races','Registry_Specs'],['Entity_Grimoire'],
     'На Столе игрок выбирает готовую Пешку. После рейда ростер показывает результат её личного lifecycle; незавершённое спасение остаётся отдельным делом. При утрате доступного состава Первый Приём проверяет право на нового Ward.',
     ['Готовая Пешка возвращается и становится кандидатом следующей вылазки.','Смертельное событие получает одно решение; Last Thread проверяется только по переданному исходу.','Нет готовых Пешек, но есть CARE или незавершённая Recovery: интерфейс объясняет причину ожидания.','Найдёныш спасён, но это ещё не автоматическое присоединение к ростеру.'],
     'Не выбирать судьбу за Lifecycle Resolver и не превращать ростер в оценку стоимости людей.',
     'Привязанность к людям сосуществует с готовностью снова выйти после потери.',
     'После потери игрок объясняет судьбу Пешки и самостоятельно находит следующий доступный шаг.',
     'Наблюдение первых потерь и повторных вылазок; интервью после CARE, смерти и спасения.',
     'Игрок воспринимает новый Ward как продолжение погибшего или не понимает, почему не может выйти.',
     'Пересмотреть объяснение состояний и доступность следующего шага; не вводить скрытую защиту от последствий.',
     'UR-002: полный fail/retry-контракт Recovery; UR-003: Dawn и Life Closure. Эти ветви остаются открытыми у владельцев.',
     ['UX','narrative','gameplay','QA']),
    ('Expedition_Preparation','expedition_preparation','Снарядиться под вылазку',
     'Подготовить известную Пешку к выбранной работе: увидеть возможности, недостающее покрытие и цену снаряжения.',
     'Сделать подготовку ответом на среду и задачу, который заметен в рейде.',
     ['Combat_Profile_Pipeline','Thermos_System','Thermos_Assembly','Equipment_PaperDoll','Gear_Progression','Magic_Batteries'],['Registry_Combos','Registry_Thermoses','Registry_Thermos_Modules','Registry_Weapons'],['Item_Attributes_UI','Equipment_PaperDoll'],
     'Игрок выбирает цель, рассматривает тело и полевой профиль, собирает Термос и подбирает оружие с источником энергии. Предпросмотр показывает итог сборки и причины отказа; подтверждённая конфигурация идёт во входной контракт.',
     ['Собрать допустимый комплект из доступных вещей.','Модуль не помещается или не обслуживается: увидеть конкретное нарушение до Deploy.','Один ItemID оказался в двух черновиках: подтвердить только допустимую сборку.','Дорогой комплект даёт другой ответ, но не обещает безопасный исход.'],
     'Не выбирать Q/E сменой оружия; не создавать общий power score и не решать вход за ingress.',
     'Игрок меняет подготовку под задачу, сохраняя осмысленный бюджетный вариант.',
     'Перед повторной вылазкой игрок меняет конкретный инструмент и может назвать ожидаемый выигрыш и долг.',
     'Сопоставление выбранной работы, preview и фактического применения снаряжения в рейде.',
     'Один комплект вытесняет альтернативы независимо от среды либо игрок узнаёт собственные ограничения только после Deploy.',
     'Пересмотреть читаемость preview и предметные компромиссы у их владельцев.',
     'Калибровка сборок и данных Термоса не доказана; сначала один полный playable комплект.',
     ['UX','art','animation','gameplay','QA']),
    ('Raid_Entry','raid_entry','Выбрать подход и войти в рейд',
     'Принять понятную ставку входа в живой сектор одному или с группой.',
     'Связать подготовку и намерение с конкретной сессией без ложного обещания безопасной точки.',
     ['19_Raid_Approach_and_Entry','13_Insertion_Logic','20_Egress_Solvency','06_Async_Timers','05_Party_Syndicate'],['Registry_Raid_Interfaces'],['01_Hub_Map_Table','05_Difficulty_Slots'],
     'На Столе игрок выбирает сектор и подход. EntryQuote раскрывает точную ставку; участники подтверждают её независимо. Insertion проверяет кандидата и материализует группу только после общего результата Breach.',
     ['Подтверждённый подход приводит к обычному входу.','Quote устарела или окно недоступно: получить конечный отказ и новый выбор.','Один участник не готов: группа не получает частично исполненное обещание.','Соединение оборвалось на границе commit: восстановить уже принятое решение без второго тела.'],
     'Не обещать безопасный spawn; не разделять очередь по силе экипировки.',
     'Игрок принимает поздний риск осознанно, а отказ не воспринимает как произвольную потерю ставки.',
     'До подтверждения игрок различает цену подхода, фазу мира и неизвестность первого контакта.',
     'Наблюдение solo/party входов, устаревших quote, низкой населённости и reconnect.',
     'Игрок путает фазу с допуском по gear либо не может объяснить списание или отказ.',
     'Пересмотреть раскрытие quote и административный отказ; исследовать ingress pressure отдельно от обещания безопасности.',
     'Региональный service и плотность населения требуют прототипа; поздняя полоса может быть недоступна.',
     ['UX','level design','gameplay','QA']),
    ('Exploration_Traversal','exploration_traversal','Прочитать место и проложить маршрут',
     'Находить путь, читать следы и менять план в незнакомой сборке знакомого сектора.',
     'Дать знанию пространства ценность, сохранив решения после освоения карты.',
     ['Traversal_Core','Movement_Physics','Hunt_Frontier_Loop','Acoustic_Stealth','10_World_Topology','15_Traversal_Shortcuts','16_UI_Map_Protocol'],['00_Port_Manifest','Registry_POIs','Registry_Environment_States'],['16_UI_Map_Protocol','Grimoire_Truth_Triangulation'],
     'Игрок сопоставляет карту, геометрию, шум и физические следы, выбирает путь к цели и держит в уме отход. Изменившаяся сцена заставляет уточнить маршрут; наблюдение не гарантирует знание о чужом намерении.',
     ['Найти цель по неполному следу и выйти другим путём.','Замечена засада: обойти, ждать или отказаться от цели.','Проход изменился после события: найти читаемую альтернативу.','Груз мешает прежнему маршруту: решить, что нести дальше.'],
     'Не выдавать wallhack и не наказывать неподвижность отдельным таймером.',
     'После освоения карты игрок продолжает читать текущую сцену, а не только повторять маршрут из wiki.',
     'Знакомый маршрут меняется по наблюдаемой причине; игрок может объяснить свой обход.',
     'Повторные прохождения одной ревизии и нескольких сборок; разбор маршрутов после обмена знаниями.',
     'Есть неизменно лучший путь либо изменения требуют только лишнего бега без нового решения.',
     'Пересмотреть размещение следов, связность и альтернативы отхода.',
     'Данные первого знакомства не доказывают долговечность исследования; нужен повтор после общего знания карты.',
     ['level design','audio','art','UX','QA']),
    ('Combat','combat','Выбрать действие и пережить ответ',
     'Использовать оружие, способности и среду, чтобы создать окно, воспользоваться им или уйти из боя.',
     'Сделать сильное действие читаемым обязательством с доступным ответом.',
     ['Combat_Three_Debts','Weapon_Core','Skill_Build_Philosophy','Ballistics_Armor','Combat_Consumables','Status_Effects','Magic_Batteries','Dissonance_System'],['Registry_Weapons','Registry_Combos','Registry_StatusEffects','Registry_Mobs'],['Weapon_Manifesto','Item_Attributes_UI'],
     'Игрок читает угрозу, выбирает канал, входит в Commitment и получает эффект вместе с долгом. Противник отвечает через геометрию, окно или ресурс; Recovery оставляет цену выбора видимой до следующего действия.',
     ['Обмен попаданиями с понятным телеграфом и ответом.','Смена оружия после сильного действия не стирает долг.','Помощь союзника проходит через уязвимое применение.','PvE вмешивается в PvP: стороны читают новый след и могут сменить роль.'],
     'Не добавлять общий лист атрибутов, обязательного healer или бесплатную готовность всех каналов.',
     'Игрок объясняет поражение доступным окном и пробует другой ответ, а не только более дорогой предмет.',
     'В разборе столкновения обе стороны называют телеграф, обязательство и выполнимую контригру.',
     'Запись дуэлей, solo PvE и групповых столкновений с разными уровнями освоения.',
     'Ответ существует лишь в документации, либо дорогая сборка одновременно снимает ресурсный, пространственный и временной риск.',
     'Пересмотреть длительность и сигналы окон, геометрию сцены и связанные модификаторы.',
     'TTK, стоимость импульсов и harm-калибровка остаются прототипными; R61 не закрыт.',
     ['animation','audio','VFX','UX','gameplay','QA']),
    ('Looting_Carry','looting_carry','Найти, выбрать и унести',
     'Выбрать полезную добычу и физически доставить её к выходу под давлением.',
     'Превратить состав груза, доступ к вещам и маршрут в связанные решения.',
     ['Looting_Process','Inventory_Architecture','Physical_Weight','Containers_Slots','Loot_Distribution','Field_Crafting','Shell_Foundlings'],['Registry_Items','Registry_Consumables','Registry_Mobs'],['Item_Attributes_UI','Inventory_QoL'],
     'Обыск раскрывает содержимое постепенно. Игрок сравнивает находку с текущим грузом, размещает её в доступной зоне и продолжает путь. Работа с узлом или переноска человека меняет физическое обязательство и план отхода.',
     ['Взять полезный ингредиент вместо более тяжёлой находки.','Прервать обыск, когда появился чужой след.','Передать груз союзнику без второго экземпляра.','Нести Найдёныша и отказаться от несовместимого груза.'],
     'Не определять награду ценником и не превращать обыск или перенос в автоматическую экстракцию.',
     'Игрок оставляет ценную вещь по понятной маршрутной причине, а не из-за непонятного интерфейса.',
     'Изменение груза меняет доступ, путь или готовность; игрок замечает это до необратимой ошибки.',
     'Наблюдение обыска под угрозой, смены носителя и маршрутов с разным грузом.',
     'Перенос всегда сводится к максимальному value/kg или интерфейс прячет причину отказа.',
     'Пересмотреть адресную полезность, bulk/access-сигналы и физическую цену переноски.',
     'Проверять после появления общего знания цен и маршрутов; бытовой loot не должен стать мусорным налогом.',
     ['UX','animation','audio','level design','QA']),
    ('Extraction','extraction','Решить, когда уходить',
     'Найти обычный выход и завершить ставку либо осознанно отказаться от неё ради живого человека.',
     'Дать рейду завершение, вокруг которого сходятся время, груз и риск встречи.',
     ['14_Extraction_System','20_Egress_Solvency','Extraction_Stabilization_Loop','Return_Manifest_Contract','07_Server_Lifecycle','17_Apex_Last_Hour'],['Registry_Raid_Interfaces'],['15_Frequency_Tuner','Item_Attributes_UI'],
     'Игрок оценивает оставшийся путь и груз, ищет Порог и принимает обязательство Sync. Его исход передаётся возврату. Body-only отказ и запечатанный Apex читаются как другие ставки с собственными владельцами последствий.',
     ['Дойти до Порога и вернуть допустимый груз.','Порог недоступен или Sync прерван: прочитать отказ и оставшиеся варианты.','Союзник выходит отдельно: его решение не разрешает чужой исход.','Смерть, спор custody или фазовая граница во время обязательства дают один упорядоченный результат.','Breakline сохраняет живого человека ценой отказа от груза и расчёта контракта.'],
     'Не гарантировать безопасный отход и не присваивать выживание по факту наличия manifest.',
     'Жадность конкурирует с уходом, а столкновение у выхода сохраняет читаемую контригру.',
     'Игрок заранее меняет план выхода и объясняет, чем пожертвовал; проигравший видит доступный ответ.',
     'Запись ранних/поздних уходов, засад, split-party, custody-конфликтов и фазовых границ.',
     'Одна засада контролирует и первый удар, и добычу, и отход либо уход превращается в обязательную рутину без решения.',
     'Пересмотреть топологию поиска и контригру у выхода, не вводя скрытый таймер наказания.',
     'Населённость и координация групп меняют convergence; тестировать опытные группы, а не только первый рейд.',
     ['level design','UX','audio','VFX','QA']),
    ('Loot_Return','loot_return','Вернуть вещь и разобраться с последствиями',
     'Увидеть, что вернулось, кому принадлежит и какая обработка ещё нужна.',
     'Сохранить значение физического возврата и происхождения находки после рейда.',
     ['Return_Manifest_Contract','Extraction_Stabilization_Loop','Loot_Sync_Cycle','Stash_Architecture','Inventory_Architecture'],['Registry_Items','Registry_Faction_Interfaces'],['Item_Attributes_UI','01_Hub_Map_Table'],
     'Итог вылазки показывает человека отдельно от доставленного состава. Манифест переносит допустимые ItemID в общий Схрон. Stable-вещь доступна сразу; Volatile, спорный след или живой груз ведут к своей процедуре, а не к общей кнопке очистки.',
     ['Обычный возврат стабильного предмета и его использование в следующей подготовке.','Volatile доставлен, но ещё требует Напоминания.','Передача спорного груза не стирает происхождение.','Повторная доставка после технического сбоя сверяет прежний commit.','STANDARD Dawn проецирует вещевой результат принятого личного решения.'],
     'Не смешивать стабилизацию мира с сохранением личной добычи и не начислять контракт по любому возвращению.',
     'Игрок понимает последствия находки и выбирает обработку вместо обязательной послерейдовой бухгалтерии.',
     'Без подсказки ведущего игрок различает доставлено, стабильно и допустимо к выбранной сделке.',
     'Разбор послерейдового экрана, возврата после сбоя и цепочек передачи/обработки.',
     'Возврат Stable-вещи требует ритуальных лишних действий либо состояние происхождения выглядит произвольной блокировкой.',
     'Пересмотреть объяснение причин и лишние UI-шаги; preserve provenance проверять отдельно от удобства.',
     'Не обещать определённость unresolved Dawn-ветвей тегов и Closure через экран манифеста.',
     ['UX','audio','narrative','gameplay','QA']),
    ('Contracts','contracts','Выполнить работу и принять её цену',
     'Выбрать городскую просьбу, способ выполнения и последствия для людей и адресов.',
     'Связать мотив вылазки с изменением следующего выбора в городе.',
     ['Quest_Engine','Quest_Engine_Grammar','Pledge_Contracts','Reputation_Rules'],['Registry_Faction_Interfaces','Registry_POIs'],['Quest_Engine_Grammar','02_Hub_Services_Interaction'],
     'Игрок читает просьбу на Столе, выбирает намерение и выполняет работу в рейде. Свидетельство и объявленный trigger передаются Quest Engine; результат меняет доступный разговор, адрес или обязательство.',
     ['Выполнить условие и вернуться через объявленный trigger.','Принести вещь без нужного свидетельства: увидеть незавершённую часть.','Отказаться от поручения или выбрать спорный метод.','Вернуться body-only: не получить расчёт обычной успешной доставки.'],
     'Не превращать фракционную биографию в resolver и не вводить безопасную ферму поручений Пешек.',
     'Метод выполнения меняет следующий выбор, а игрок различает работу и повторяемый список наград.',
     'Игрок объясняет, кому и почему помог, и замечает последствие в следующем обращении к Столу.',
     'Сквозной контракт с normal/negative исходами и повтор после знакомства с выгодными методами.',
     'Все методы отличаются только временем до одинаковой награды или фракция остаётся невидимой шкалой.',
     'Пересмотреть причинную связь результата, адреса и видимого последствия.',
     'Авторские контракты и фракционные голоса требуют контента; схема сама не доказывает переживание долга.',
     ['narrative','UX','level design','QA']),
    ('Living_Table','living_table','Вернуться к живому Столу',
     'Понять, что изменилось в городе, и выбрать следующую работу через карту, предметы и голоса.',
     'Сделать паузу между рейдами местом осмысленного выбора и тепла.',
     ['01_Hub_Map_Table','02_Hub_Services_Interaction','03_Hub_Map_Interaction','Civic_Event_Lifecycle','17_Dual_State_POIs','05_Party_Syndicate'],['Registry_POIs','Registry_Faction_Interfaces'],['00_Hub_Environment','04_Time_Atmosphere','Entity_Grimoire'],
     'Возвращение меняет состав Схрона и видимые поводы на Столе. Игрок замечает адрес, рассматривает его причину, сопоставляет услугу с текущими вещами и закрепляет новую цель; для совместного выхода собирает группу.',
     ['После потери найти центральный минимум и следующую работу.','Внешний адрес исчез или изменился с ревизией: увидеть причину и fallback.','Городское явление показывает публичный исход отдельно от личного вклада.','Игрок пропускает необязательный разговор и продолжает подготовку.'],
     'Не добавлять прогулочное тело Бригадира, обязательный ежедневный обход или worker-dispatch.',
     'Игрок задерживается ради нового смысла, но освоивший Стол быстро проходит знакомую подготовку.',
     'После возвращения игрок замечает конкретное последствие и принимает новый выбор без обхода всех пинов.',
     'Наблюдение первых и повторных возвратов, после потери и у уставшего опытного игрока.',
     'Тепло требует повторять один разговор либо оптимальный путь превращается в полный обход Стола.',
     'Пересмотреть приоритет сигналов, сокращение повторов и связь повода с рейдом.',
     'Редкие поводы не должны стать FOMO-расписанием; ритм возвращения остаётся открытой задачей TODO.',
     ['art','audio','narrative','UX','QA']),
    ('Resource_Addressing','resource_addressing','Найти добыче применение',
     'Выбрать, превратить ли вынесенный состав в следующий рейд, специальную сборку или вклад в город.',
     'Сохранить конкретную полезность Common-добычи и осмысленный выбор адреса.',
     ['Resource_Cycle','Barter_System','Vendor_Logic','Blueprints','Craft_Modifiers','Economy_Core'],['Registry_CraftingRecipes','Registry_Items','Registry_Blueprints'],['01_Hub_Map_Table','02_Hub_Services_Interaction'],
     'Извлечённый состав сопоставляется с известными адресами. Игрок сравнивает точные результаты, выбирает услугу и подтверждает сделку. Её результат сохраняет происхождение входов и меняет подготовку следующего выхода.',
     ['Один ингредиент подходит для sustain и sidegrade: выбрать, чем пожертвовать.','Рецепт совпал по составу, но не по происхождению: увидеть отказ до передачи.','Внешний мастер недоступен: использовать ограниченный центральный минимум.','Повторная пакетная сделка исполняет только опубликованное точное совпадение.'],
     'Не создавать вторую ресурсную систему, универсальную топку, рыночный арбитраж или тайный рецепт, который обязана не решить wiki.',
     'Знание рецептов делает выбор яснее, но не сводит всё имущество к одному лучшему конвертеру.',
     'Опытный игрок выбирает разные назначения одного состава в зависимости от следующей работы.',
     'Сравнение решений до/после публикации рецептов и при накопленном богатстве; проверка замкнутых цепей услуг.',
     'Один адрес поглощает весь лут или безопасные сделки устойчиво финансируют себя без рейда.',
     'Пересмотреть составы и назначение результатов у владельцев рецептов и экономики.',
     'Курсы, replacement cost и ветеранское накопление не доказаны; числовой baseline ещё нужен.',
     ['UX','narrative','gameplay','QA']),
    ('Living_World','living_world','Выбрать момент в меняющемся мире',
     'Читать возраст сектора, переживать его изменение и видеть, что город унаследовал после него.',
     'Соединить короткую вылазку с более долгой жизнью места без подмены личного исхода общим событием.',
     ['07_Server_Lifecycle','04_Global_Map_Rotation','21_Location_Revision_Lifecycle','Anomaly_System','16_Anomaly_Mutation_Lines','03_Dynamic_Weather','08_Gate_Check','17_Apex_Last_Hour'],['Registry_Biomes','Registry_Anomaly_Mutations','Registry_Environment_States','00_Port_Manifest'],['05_Difficulty_Slots','00_Anomaly_Core_Loop','01_Hub_Map_Table'],
     'На Столе виден возраст доступного сектора. В рейде фаза, местные следы и погода предупреждают об изменении; игрок уходит, углубляется или принимает запечатанный последний час. После завершения публикуется новая мирная ревизия по своему lifecycle.',
     ['Короткая работа в ранней фазе.','Остаться на фазовый переход и увидеть последствия подготовки.','Поздний сектор ещё жив, но новые входы закрыты.','Несколько сессий одной ревизии сохраняют локальные изменения раздельно.','Dawn завершает сессию, но личные судьбы решаются отдельно.'],
     'Не считать Tier рейтингом человека, не подменять WorldRevision локальными событиями рейда.',
     'Игрок выбирает фазовый риск, а изменение мира добавляет решения после освоения сектора.',
     'Игрок различает время своего рейда и возраст мира, узнаёт предупреждение и меняет план до барьера.',
     'Повторные рейды через фазовые границы, наблюдение Apex и перехода к Stable-проекции.',
     'Переход читается как случайная казнь или после освоения остаётся только обязательный набор защиты.',
     'Пересмотреть сигналы, условия среды и ценность позднего выбора без изменения времени исподтишка.',
     'Плотность игроков, совместное знание и стоимость авторства разных фаз могут изменить ожидаемую динамику.',
     ['level design','art','audio','VFX','UX','QA']),
    ('Personal_Development','personal_development','Прожить собственную историю Пешки',
     'Узнавать приобретённые свойства человека и строить дальнейшие решения вокруг его опыта.',
     'Сделать развитие продолжением жизни, которое не заменяет полевой профиль и не переносится на нового человека.',
     ['Tags_System','Combat_Profile_Pipeline','Proficiency_Arsenal','Shell_Foundlings','Life_Closure'],['Registry_Tags','Registry_Combos'],['Entity_Grimoire','Item_Attributes_UI'],
     'Событие жизни назначает или раскрывает свойство по правилу владельца. Игрок читает условие, локальный эффект и долг, проверяет его в составе профиля и меняет привычку следующей вылазки. Завершение жизни сохраняет смысл человека без передачи его механической силы.',
     ['Раскрыть заранее назначенное свойство после соответствующего события.','Условный тег неактивен: понять условие, не получить новое свободное место.','Origin найденыша учитывается в том же личном контракте.','Новая Пешка после утраты не наследует теги погибшей.'],
     'Не вводить дерево, tag-shopping, повторный roll или account-множитель.',
     'Игрок приспосабливается к человеку, вместо выбраковки всех профилей вне решённой меты.',
     'В повторной вылазке игрок использует конкретное личное свойство и называет его ограничение.',
     'Продольное наблюдение нескольких жизней, редких конфигураций и решений после знакомства с метой.',
     'Рациональный путь — массово заменять людей ради желаемого тега либо свойство остаётся незаметным.',
     'Пересмотреть источники, видимость и локальные пересечения; не выдавать силу за ценность личности.',
     'UR-001: раскрытие First Return при STANDARD Dawn. Feature не выбирает эту ветвь.',
     ['narrative','UX','VFX','gameplay','QA']),
    ('Knowledge_Investigation','knowledge_investigation','Собрать свидетельства и понять находку',
     'Сопоставить чужие объяснения с найденным свидетельством и выбрать дальнейшее расследование.',
     'Сохранить исследованию смысл после открытия факта, связывая знание с новым действием.',
     ['Grimoire_Truth_Triangulation','Quest_Engine','Quest_Engine_Grammar'],['Registry_POIs','Registry_Faction_Interfaces'],['Grimoire_Truth_Triangulation','Entity_Grimoire','01_Hub_Map_Table'],
     'Игрок получает наблюдение, слух или объяснение адреса, видит источник и степень подтверждения в Гримуаре. Несогласие источников даёт повод проверить место в рейде; свидетельство возвращается к контракту и следующему вопросу.',
     ['Два источника расходятся: сохранить обе версии и их причины.','Новый след подтверждает часть объяснения, не всё утверждение сразу.','Факт уже известен сообществу: работа в рейде всё ещё имеет конкретный адрес и последствие.','Недостаточно свидетельств: показать неопределённость вместо окончательного ответа.'],
     'Не объявлять мнение жителя истиной и не обещать неразрешимую сообществом загадку.',
     'Игрок использует происхождение знания при выборе действия, а после разгадки сохраняется содержательная работа.',
     'Игрок различает слух и подтверждённый факт и называет, какое наблюдение изменит его решение.',
     'Разбор расследования до и после публичного решения; проверка спорных источников и повторного прохождения.',
     'Гримуар становится обязательным чтением без выбора или расследование после wiki остаётся только execution tax.',
     'Пересмотреть связь свидетельства, метода и результата; сократить повторную подачу известного.',
     'Сквозной authored пример и ритм поводов ещё требуют production; нельзя объявлять гипотезу validated по схеме.',
     ['narrative','UX','level design','audio','QA'])
    ]
    folder=ROOT/'01_Core_Vision/Features'
    for order,row in enumerate(rows,1):
        name,fid,title,promise,purpose,owners,data,ux,flow,cases,nongoals,dynamics,observable,evidence,falsify,response,debt,production=row
        p=folder/(name+'.md')
        fm={'type':'feature','status':'active','system':'player_experience','feature_id':fid,'feature_order':order,'display_name':title,'player_promise':promise,'expected_dynamics':dynamics,'maturity':'specified','mvp_scope':'vertical_slice_subset','validation_state':'untested','system_owners':[ref(x) for x in owners],'data_sources':[ref(x) for x in data],'ux_surfaces':[ref(x) for x in ux],'production_disciplines':production,'validation':['[[01_Core_Vision/Features/'+name+'#Проверка гипотезы]]']}
        out='---\n'+'\n'.join(k+': '+json.dumps(v,ensure_ascii=False) for k,v in fm.items())+'\n---\n\n# '+title+'\n\n'+promise+'\n\n'+purpose+'\n\n## За минуту\n\n'+flow+'\n\n## Сценарии и границы\n\n'+'\n'.join('- '+c for c in cases)+'\n\n'+nongoals+'\n\n## Кто исполняет и что видит игрок\n\nПравила и переходы: '+', '.join(ref(x) for x in owners)+'.\n\nДанные и авторские экземпляры: '+', '.join(ref(x) for x in data)+'.\n\nИгроковые экраны, сигналы и объяснение отказа: '+', '.join(ref(x) for x in ux)+'. Feature связывает эти поверхности; формулы, допуск и окончательные исходы остаются у владельцев правил.\n\n## Проверка гипотезы\n\n**PLAUSIBLE, не проверено:** '+dynamics+'\n\n- **Наблюдаем:** '+observable+'\n- **Доказательство и способ наблюдения:** '+evidence+'\n- **Опровержение:** '+falsify+'\n- **Ответ:** '+response+'\n\n## MVP и производство\n\n`active` означает принятое описание возможности; `specified` — описанные связи, не готовность реализации или доказанную динамику. В первый срез входит только сценарий, необходимый для полного пути «подготовка → рейд → последствие»; объём работ задаёт '+ref('Build_Extraction_Concept_Slice')+' и [[09_Project_Management/TODO]].\n\n'+debt+'\n\nНужны '+', '.join(production)+': согласовать связанные экраны и сигналы с перечисленными сценариями, подготовить авторский пример и проверить отказ вместе с успешным прохождением.\n'
        write(p,out)
    links=['[[01_Core_Vision/Features/'+r[0]+']]' for r in rows]
    write(ROOT/'01_Core_Vision/Feature_Map.md','---\ntype: view\nstatus: active\nsystem: feature_navigation\nview_kind: feature_map\nupstream_sources: '+json.dumps(links,ensure_ascii=False)+'\n---\n\n# Возможности игрока\n\nНачните с '+ref('GDD_Main')+', '+ref('01_Vision')+' и '+ref('02_Core_Loop')+'. Эта карта показывает законченные возможности, из которых складывается путь игрока. Она читает Feature-страницы и не определяет правила. Конкретное правило ищите через [[00_Index|доменные маршруты]].\n\n'+'\n'.join(f'{i}. '+link for i,link in enumerate(links,1))+'\n\n## Обещание, связи и готовность\n\n```dataview\nTABLE WITHOUT ID file.link AS "Feature", player_promise AS "Обещание", expected_dynamics AS "Гипотеза динамики", system_owners AS "Владельцы", ux_surfaces AS "UX", data_sources AS "Данные", maturity AS "Зрелость", mvp_scope AS "MVP", validation_state AS "Проверка"\nWHERE type = "feature" AND status = "active"\nSORT feature_order ASC\n```\n\nДвусторонние связи и пропуски: [[01_Core_Vision/Views/Feature_Owner_Coverage]]. Текущие работы: [[09_Project_Management/TODO]]; риски и свидетельства: [[09_Project_Management/Risk_Register]].\n')
    for name in ['GDD_Main','01_Vision','02_Core_Loop']:
        p=find(name);s=p.read_text(encoding='utf-8');write(p,s+'\nСвязанные возможности игрока: [[01_Core_Vision/Feature_Map|Feature Map]].\n')
    print('Created',len(rows),'features and Feature Map')
def owner(p,kind='system'):
    d=parse_frontmatter(p);s=p.read_text(encoding='utf-8');title=re.search(r'^# (.+)',s,re.M)
    title=title[1] if title else p.stem
    group=p.relative_to(ROOT).parts[0][3:].lower()
    summary=d.get('index_summary','')
    if not summary or summary.startswith('Задаёт правила и последствия системы'):
        verb={'registry':'Хранит схему и записи','lore':'Описывает мир и общественные причины','core_concept':'Объясняет замысел','mechanic':'Определяет действие и его границы','system':'Определяет состояния, разрешение и связи'}[kind]
        summary=f'{verb}: {title}.'
    meta(p,{'type':kind,'index_route':'owner','index_group':d.get('index_group',group),'index_order':d.get('index_order',200),'index_summary':summary,'read_when':d.get('read_when') if d.get('read_when') and not d.get('read_when').startswith('Читайте при изменении входов, состояний, стоимости') else f'Когда нужен контракт «{title}» и его границы с соседними владельцами.'})

def taxonomy():
    systems='Pledge_Contracts Quest_Engine Quest_Engine_Grammar Reputation_Rules Grimoire_Truth_Triangulation Proficiency_Arsenal Shell_Foundlings Spawn_Logic Tags_System Acoustic_Stealth Ballistics_Armor Combat_Consumables Combat_Three_Debts Dissonance_System Hunt_Frontier_Loop Magic_Batteries Movement_Physics Status_Effects Weapon_Core Barter_System Blueprints Currency_Rez Economy_Core Extraction_Stabilization_Loop Loot_Distribution Loot_Sync_Cycle Resource_Cycle Sinks_Insurance Vendor_Logic Affix_Grammar Containers_Slots Equipment_PaperDoll Gear_Progression Inventory_Architecture Physical_Weight Stash_Architecture Anomaly_System 16_Anomaly_Mutation_Lines 11_Socket_System 12_Generation_Strategies 13_Async_Double_Buffer 14_Sector_Content_Rules 16_UI_Map_Protocol 01_Hub_Map_Table 02_Hub_Services_Interaction 03_Hub_Map_Interaction'.split()
    concepts='02_Core_Loop GDD_Main Glossary Build_Extraction_Concept_Slice Ability_Synergy Entity_Grimoire Shell_Construction Two_Paradox_Birth Weapon_Manifesto 01_World_Concept_Palimpsest 00_Anomaly_Core_Loop 00_Hub_Environment 04_Time_Atmosphere'.split()
    for name in systems: owner(find(name))
    for name in concepts: meta(find(name),{'type':'core_concept'})
    # UI contracts have their own presentation rules; they are not analytical vault views.
    for name in ['05_Difficulty_Slots','15_Frequency_Tuner']: owner(find(name),'mechanic')
    for p in ROOT.glob('0[1-8]*/**/*.md'):
        d=parse_frontmatter(p);t=d.get('type')
        if t=='system_contract' or t=='system': owner(p)
        elif t=='lore_framework': owner(p,'lore')
        elif t in ['race','spec','faction','weapon_frame','location']:
            meta(p,{'type':'entity','entity_kind':t})
        elif t=='anomaly_instance': meta(p,{'type':'content','content_kind':'anomaly_instance'})
        elif t=='template': meta(p,{'type':'content','content_kind':'template'})
        elif t=='interface_registry': owner(p,'registry')
        elif t=='registry': owner(p,'registry')
    owner(find('Glossary'),'core_concept')
    for name in ['City_District_Social_Grammar','Civic_Order','Hearth_Anatomy']:
        p=find(name);d=parse_frontmatter(p);meta(p,{'index_summary':d['index_summary'].replace('правила и последствия системы','мир и общественные причины')})
    for p in ROOT.glob('09_Project_Management/*.md'):
        d=parse_frontmatter(p);meta(p,{'type':'project_management'})
    # Fix type consumers, retaining the named family on source notes.
    for p in ROOT.glob('0*/**/*.md'):
        s=p.read_text(encoding='utf-8-sig');n=s
        for family in ['race','spec','faction','weapon_frame']:
            n=re.sub(r'\btype\s*=\s*"'+family+r'"', 'entity_kind = "'+family+'"',n)
            n=re.sub(r'\.type\s*===?\s*"'+family+r'"', '.entity_kind === "'+family+'"',n)
            n=n.replace('type: '+family+'`','type: entity`, `entity_kind: '+family+'`')
        if n!=s:write(p,n)
    print('Classified stateful owners, local mechanics, entities, concepts and management')

def section(s,heading):
    # Section boundary outside fenced blocks, preserving nested example headings.
    lines=s.splitlines(keepends=True);positions=[];offset=0;fence=False
    for l in lines:
        if l.startswith('```'): fence=not fence
        if not fence and l.startswith('## '):positions.append((l.strip(),offset))
        offset+=len(l)
    for i,(h,a) in enumerate(positions):
        if h==heading:return a,positions[i+1][1] if i+1<len(positions) else len(s)
    raise ValueError(heading)
def transfer(source,heading,destination):
    p=find(source);s=p.read_text(encoding='utf-8');a,b=section(s,heading);block=s[a:b].strip()
    q=find(destination);t=q.read_text(encoding='utf-8');assert heading not in t,(destination,heading)
    write(q,t.rstrip()+'\n\n'+block+'\n')
    write(p,s[:a]+heading+'\n\nСм. '+ref(destination)[:-2]+'#'+heading[3:]+']].\n\n'+s[b:])
    # Retarget deep references, preserving general registry/schema references.
    old=ref(source)[2:-2]+'#'+heading[3:];new=ref(destination)[2:-2]+'#'+heading[3:]
    for consumer in ROOT.glob('0*/**/*.md'):
        t=consumer.read_text(encoding='utf-8');u=t.replace(old,new)
        if t!=u:write(consumer,u)
def new_system(name,title,system,intro):
    p=ROOT/name;write(p,'---\ntype: system\nstatus: active\nsystem: '+system+'\n---\n\n# '+title+'\n\n'+intro+'\n');owner(p);return p
def registries():
    new_system('04_Player_Entities/Skill_Execution.md','Исполнение навыка: носитель, результат и границы','skill_execution','Навык объявляет, кто выполняет действие, чем оно оплачено и какое окно остаётся после эффекта. Эта страница владеет общей грамматикой исполнения; поля и иллюстративные записи находятся в '+ref('Registry_Skill_Types')+'.')
    for h in ['## 2. Владение','## 3. Закон исполнения','## 4. Границы спорных возможностей','## 5. Движение','## 6. Оружейный контур','## 8. Энергетический контракт','## 9. Проверки','## 10. Поддержка, восстановление и импульсы','## 11. Боевой результат']:
        transfer('Registry_Skill_Types',h,'Skill_Execution')
    new_system('04_Player_Entities/Interaction_Constraints.md','Общие циклы и неснимаемый долг','interaction_constraints','Несколько локальных улучшений могут относиться к одному физическому решению. Здесь определяется, как распознать общий цикл и сохранить его долг. Список семейств и разрешённые оси заданы в '+ref('Registry_Interaction_Families')+'.')
    for h in ['## 2. Проверка активного профиля','## 3. `thermal_cycle`','## 4. `manual_operation`','## 5. `self_backlash` и hard debt','## 6. `signal_reading`','## 7. `load_route`','## 8. Допуск нового семейства']:
        transfer('Registry_Interaction_Families',h,'Interaction_Constraints')
    p=find('Registry_Interaction_Families');s=p.read_text(encoding='utf-8');law='Если параметр делит запас, порог или правило отказа с уже существующим результатом, он обязан принадлежать тому же семейству независимо от имени модуля или анимационной стадии.'
    assert law in s;write(p,s.replace(law,'Правило объединения параметров и неизменяемые долги: '+ref('Interaction_Constraints')+'.'))
    q=find('Interaction_Constraints');write(q,q.read_text(encoding='utf-8')+'\n## Граница общего цикла\n\n'+law+'\n')
    # Preserve authored records. Move universal law to the existing behavioral owners.
    for src,h,dst in [
        ('Registry_StatusEffects','## Бюджет статуса: не геройский шутер','Status_Effects'),
        ('Registry_StatusEffects','## Граница глобального статуса','Status_Effects'),
        ('Registry_StatusEffects','## Среда не является таблицей реакций','Status_Effects'),
        ('Registry_CraftingRecipes','## 2. Рабочий цикл записи','Barter_System'),
        ('Registry_CraftingRecipes','## 6. Исключения','Barter_System'),
        ('Registry_Thermos_Interfaces','## Invariants','Thermos_System'),
        ('Registry_Consumables','## 4. Запреты','Combat_Consumables'),
        ('Registry_Blueprints','## 2. Рабочий цикл','Blueprints'),
        ('Registry_Blueprints','## 5. Сознательно отложено','Blueprints'),
        ('18_POI_Metadata_Registry','## 4. Resolver','17_Dual_State_POIs')]:
        transfer(src,h,dst)
    owner(find('18_POI_Metadata_Registry'),'registry')
    # Clear normative load from data intro; keep linkable schema.
    p=find('Registry_Parameter_Contracts');s=p.read_text(encoding='utf-8');a=s.index('`domain_owner` задаёт');b=s.index('## Активные домены',a);law=s[a:b]
    q=find('Skill_Build_Philosophy');write(q,q.read_text(encoding='utf-8')+'\n## Авторизация запроса параметра\n\n'+law)
    write(p,s[:a]+'Общая авторизация запроса: '+ref('Skill_Build_Philosophy')[:-2]+'#Авторизация запроса параметра]]. Записи ниже указывают доменного владельца и его bounded policy.\n\n'+s[b:])
    # Universal rules in these tables already have named owners; re-home their unique exact wording.
    transfer('Registry_Parameter_Contracts','## Инварианты','Combat_Profile_Pipeline')
    p=find('Registry_Thermos_Modules');s=p.read_text(encoding='utf-8');a=s.index('OR placement uses');b=s.index('## Candidate records',a);law=s[a:b]
    q=find('Thermos_Assembly');write(q,q.read_text(encoding='utf-8')+'\n## Правила definition binding\n\n'+law)
    write(p,s[:a]+'Размещение, service legality и atomicity определяет '+ref('Thermos_Assembly')[:-2]+'#Правила definition binding]].\n\n'+s[b:])
    print('Separated skill execution, shared cycles, status, recipe, blueprint, Thermos and POI law')

def moves():
    mapping={}
    for p in ROOT.glob('0*/**/*.md'):
        old=p.relative_to(ROOT).as_posix();new=old
        if '/_Registries/' in old:new=new.replace('/_Registries/','/Registries/')
        if '/_Matrices/' in old:
            new=new.replace('/_Matrices/','/Views/')
            new=new.replace('00_Faction_Reputation','Faction_Relationships').replace('00_Synergy_Map','Synergy_Map').replace('00_Biome_Matrix','Biome_Matrix')
        # These folders contain independent owners, not executable stages (Night Benches precedes weather,
        # entry is 19 and lifecycle is 07). Actual ordered pipelines remain inside their owning pages.
        if any('/'+family+'/' in old for family in ['Generation','Hub','Anomaly']):
            if re.match(r'\d\d_',p.stem):new=str(Path(new).with_name(re.sub(r'^\d\d_','',p.name))).replace('\\','/')
        if p.stem=='00_Port_Manifest':new=new.replace('00_Port_Manifest','Port_Manifest')
        if p.stem=='01_Foreign_Water_Mutation_Lines':new=new.replace('01_Foreign_Water_Mutation_Lines','Foreign_Water_Mutation_Lines')
        if '/Port/Tables/' in old:new=new.replace('/Port/Tables/','/Port/Views/')
        if p.stem=='Faction_Address_System':new='03_Factions_Societies/Faction_Address_System.md'
        if p.stem=='18_POI_Metadata_Registry':new='08_World_Generation/Registries/Registry_POI_Metadata.md'
        if p.stem=='Item_Calibration_Matrix':new='07_Gear_Inventory/Views/Item_Calibration_Matrix.md'
        if p.stem=='_Sector_Manifest_Template':new='08_World_Generation/Content/Templates/Sector_Manifest_Template.md'
        if p.stem=='Skill_Contract_Valid':new='tools/tests/fixtures/Skill_Contract_Valid.md'
        if old!=new:
            assert not (ROOT/new).exists(),new
            mapping[old]=new
    write(ROOT/'.refactor_moves.json',json.dumps(mapping,ensure_ascii=False,indent=2))
    print('Prepared',len(mapping),'native moves')

if __name__=='__main__':
    if sys.argv[1]=='features': features()
    if sys.argv[1]=='taxonomy': taxonomy()
    if sys.argv[1]=='registries': registries()
    if sys.argv[1]=='moves': moves()
