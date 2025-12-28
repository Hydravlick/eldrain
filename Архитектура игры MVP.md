---
tags:
  - doc
---

# АРХИТЕКТУРА ЭКСТРАКШН ШУТЕРА

## ПРИНЦИПЫ АРХИТЕКТУРЫ

```
MVP-first подход с четким разделением на этапы
Гибридная архитектура: UE5 + ECS для специфических задач
Надежная сетевая архитектура для мультиплеера
Процедурная генерация на ECS
Расширяемость без переписывания
```

---

## АРХИТЕКТУРНЫЕ РЕШЕНИЯ

### Основная архитектура

- **Игроки и основная логика**: UE5 стандартная архитектура + репликация
- **ИИ системы**: ECS для производительности
- **Процедурная генерация**: ECS для генерации карт и городских кварталов
- **Сетевая часть**: Встроенная система репликации UE5

### Выбор технологий

- **Engine**: Unreal Engine 5
- **ECS Library**: Mass Entity (встроенная в UE5.1+)
- **Networking**: UE5 Replication System
- **AI**: Custom ECS + Behavior Trees для презентации

---

## СТРУКТУРА ПРОЕКТА
```
Source/
├── Core/                           # [MVP] Ядро системы
│   ├── GameFramework/
│   │   ├── [MVP] EldrainGameMode           # Основные игровые режимы
│   │   ├── [MVP] EldrainGameState          # Состояние мира
│   │   ├── [MVP] EldrainPlayerController   # Контроллер игрока
│   │   └── [MVP] EldrainGameInstance       # Глобальное состояние
│   ├── ECS/
│   │   ├── [MVP] ECSWorld                  # Центральный ECS мир
│   │   ├── [MVP] EntityManager            # Управление сущностями
│   │   ├── [MVP] ComponentManager         # Управление компонентами
│   │   └── [MVP] SystemManager            # Управление системами
│   └── Events/
│       ├── [MVP] EventBus                 # Центральная шина событий
│       └── [MVP] GameplayEvents           # Игровые события
│
├── Characters/                     # [MVP] Система персонажей
│   ├── Base/
│   │   ├── [MVP] BaseCharacter            # Базовый класс персонажа (UE5)
│   │   └── [MVP] CharacterFactory         # Фабрика персонажей
│   ├── Player/
│   │   ├── [MVP] PlayerCharacter          # Игровой персонаж
│   │   ├── [MVP] PlayerMovement           # Движение игрока
│   │   ├── [MVP] PlayerStats              # Характеристики
│   ├── NPC/
│   │   ├── [MVP] NPCCharacter             # NPC персонажи
│   │   └── [Extended] DialogueSystem      # Система диалогов
│   └── Components/                # Гибридные компоненты
│       ├── [MVP] HealthComponent          # Здоровье (UE5)
│       ├── [MVP] StatsComponent           # Характеристики (UE5)
│       ├── [MVP] SkillComponent           # Навыки (UE5)
│       ├── [MVP] TagComponent             # Теги персонажа (UE5)
│       └── [Extended] ReputationComponent # Репутация (UE5)
│
├── AI/                            # [MVP] ECS-based ИИ система
│   ├── ECS/
│   │   ├── Components/
│   │   │   ├── [MVP] AIPositionComponent       # Позиция ИИ
│   │   │   ├── [MVP] AIMovementComponent       # Движение ИИ
│   │   │   ├── [MVP] AIBehaviorComponent       # Поведение ИИ
│   │   │   ├── [MVP] AISocialComponent         # Социальное взаимодействие
│   │   │   └── [Extended] AITerritoryComponent # Территориальность
│   │   ├── Systems/
│   │   │   ├── [MVP] AIMovementSystem          # Система движения
│   │   │   ├── [MVP] AIBehaviorSystem          # Система поведения
│   │   │   ├── [MVP] AISocialSystem            # Социальная система
│   │   │   └── [Extended] AITerritorySystem    # Территориальная система
│   │   └── [MVP] AIECSWorld            # ECS мир для ИИ
│   └── Presentation/
│       ├── [MVP] AIPawn                        # UE5 представление ИИ
│       └── [MVP] AIController                  # Контроллер ИИ
│
├── Combat/                        # [MVP] Боевая система
│   ├── Base/
│   │   ├── [MVP] CombatSystem               # Основная боевая система (UE5)
│   │   ├── [MVP] DamageSystem               # Система урона
│   │   └── [MVP] DeathSystem                # Система смерти
│   ├── Skills/
│   │   ├── [MVP] SkillSystem                # Система навыков
│   │   ├── [MVP] SkillArchetypes            # Архетипы навыков
│   │   └── [MVP] ResourceSystem             # Система ресурсов
│   ├── StatusEffects/             # [MVP] ECS-based статусы
│   │   ├── ECS/
│   │   │   ├── Components/
│   │   │   │   ├── [MVP] StatusEffectComponent    # Статусные эффекты
│   │   │   │   ├── [MVP] EffectDurationComponent  # Длительность эффектов
│   │   │   │   └── [MVP] EffectStackComponent     # Стеки эффектов
│   │   │   ├── Systems/
│   │   │   │   ├── [MVP] StatusEffectSystem       # Обработка эффектов
│   │   │   │   ├── [MVP] EffectInteractionSystem  # Взаимодействие эффектов
│   │   │   │   └── [MVP] EffectCleanupSystem      # Очистка эффектов
│   │   │   └── [MVP] StatusEffectECS         # ECS мир статусов
│   │   └── [MVP] StatusEffectManager        # Менеджер эффектов (UE5 мост)
│   └── Weapons/
│       ├── [MVP] WeaponBase                 # Базовое оружие
│       ├── [MVP] MeleeWeapon                # Оружие ближнего боя
│       └── [MVP] RangedWeapon               # Дальнобойное оружие
│
├── Inventory/                     # [MVP] Система инвентаря
│   ├── [MVP] InventoryComponent             # Компонент инвентаря
│   ├── [MVP] ItemBase                       # Базовый предмет
│   ├── [MVP] Equipment                      # Снаряжение
│   ├── [MVP] Consumable                     # Расходуемые предметы
│   ├── [MVP] ItemContainer                  # Контейнер предметов
│   ├── [MVP] GridInventory                  # Сеточный инвентарь
│   └── [Extended] TradingSystem             # Система торговли
│
├── World/                              # Игровой мир
│   ├── Core/                          # [MVP] Основные системы мира
│   │   ├── [MVP] WorldManager         # Главный менеджер мира
│   │   ├── [MVP] LocationSystem       # Система локаций
│   │   └── [MVP] TransitionSystem     # Переходы между локациями
│   │
│   ├── City/                          # [MVP] Город-хаб
│   │   ├── Structure/                 # Структура города
│   │   │   ├── [MVP] District         # Район города
│   │   │   ├── [MVP] DistrictManager  # Менеджер районов
│   │   │   ├── [MVP] Building         # Здания
│   │   │   └── [MVP] CityLayout       # Планировка города
│   │   ├── Content/                   # Контент города
│   │   │   ├── [MVP] BuildingContent  # Содержимое зданий
│   │   │   ├── [MVP] NPCPlacement     # Размещение NPC
│   │   │   └── [MVP] LootDistribution # Распределение лута
│   │   ├── Social/                    # [Extended] Социальные системы
│   │   │   ├── [Extended] FactionSystem    # Система фракций
│   │   │   ├── [Extended] ReputationSystem # Система репутации
│   │   │   └── [Extended] QuestNetwork     # Сеть квестов
│   │   └── Economy/                   # [Extended] Экономика
│   │       ├── [Extended] CityEconomy      # Городская экономика
│   │       ├── [Extended] TradingSystem    # Система торговли
│   │       └── [Extended] CurrencyManager  # Менеджер валют
│   │
│   ├── Anomalies/                     # [Extended] Система аномалий
│   │   ├── Core/                      # Основа аномалий
│   │   │   ├── [Extended] AnomalyZone      # Зоны аномалий
│   │   │   ├── [Extended] AnomalyManager   # Менеджер аномалий
│   │   │   └── [Extended] AnomalyLifecycle # Жизненный цикл аномалий
│   │   ├── Content/                   # Контент аномалий
│   │   │   ├── [Extended] MonsterEcosystem # Экосистема монстров
│   │   │   ├── [Extended] LootSystem       # Система лута
│   │   │   └── [Extended] HazardSystem     # Система опасностей
│   │   ├── Mechanics/                 # Механики аномалий
│   │   │   ├── [Extended] MarkingSystem    # Система меток
│   │   │   ├── [Extended] SafeHouse        # Безопасные дома
│   │   │   └── [Extended] ExtractionSystem # Система экстракции
│   │   └── Types/                     # Типы аномалий
│   │       ├── [Extended] PortAnomalies    # Портовые аномалии
│   │
│   └── Generation/                    # [MVP] Процедурная генерация
│       ├── ECS/                       # ECS архитектура
│       │   ├── Components/            # Компоненты
│       │   │   ├── Core/              # Базовые компоненты
│       │   │   │   ├── [MVP] LocationComponent    # Локации
│       │   │   │   ├── [MVP] TransformComponent   # Трансформации
│       │   │   │   └── [MVP] TagComponent         # Теги
│       │   │   ├── City/              # Городские компоненты
│       │   │   │   ├── [MVP] DistrictComponent      # Районы
│       │   │   │   ├── [MVP] BuildingComponent      # Здания
│       │   │   │   ├── [MVP] PlacementComponent     # Размещение
│       │   │   │   └── [MVP] ContentComponent       # Содержимое
│       │   │   ├── Generation/        # Компоненты генерации
│       │   │   │   ├── [MVP] TagRequirementComponent # Требования тегов
│       │   │   │   ├── [MVP] GenerationRuleComponent # Правила генерации
│       │   │   │   └── [MVP] VariationComponent      # Вариации
│       │   │   └── Anomalies/         # Компоненты аномалий
│       │   │       ├── [Extended] AnomalyComponent    # Аномалии
│       │   │       ├── [Extended] MonsterComponent    # Монстры
│       │   │       └── [Extended] HazardComponent     # Опасности
│       │   │
│       │   ├── Systems/               # Системы
│       │   │   ├── Core/              # Базовые системы
│       │   │   │   ├── [MVP] WorldUpdateSystem      # Обновление мира
│       │   │   │   └── [MVP] LocationManagerSystem  # Менеджер локаций
│       │   │   ├── City/              # Городские системы
│       │   │   │   ├── [MVP] DistrictGenerationSystem # Генерация районов
│       │   │   │   ├── [MVP] BuildingPlacementSystem  # Размещение зданий
│       │   │   │   ├── [MVP] ContentGenerationSystem  # Генерация контента
│       │   │   │   └── [MVP] DistrictRotationSystem   # Ротация районов
│       │   │   ├── Validation/        # Системы валидации
│       │   │   │   ├── [MVP] TagValidationSystem     # Валидация тегов
│       │   │   │   ├── [MVP] PlacementValidationSystem # Валидация размещения
│       │   │   │   └── [MVP] ConstraintValidationSystem # Валидация ограничений
│       │   │   └── Anomalies/         # Системы аномалий
│       │   │       ├── [Extended] AnomalyGenerationSystem # Генерация аномалий
│       │   │       ├── [Extended] MonsterSpawnSystem      # Спавн монстров
│       │   │       └── [Extended] AnomalyLifecycleSystem  # Жизненный цикл
│       │   │
│       │   └── [MVP] WorldGenerationECS # ECS мир генерации
│       │
│       ├── Algorithms/                # Алгоритмы генерации
│       │   ├── [MVP] WeightedSelection      # Взвешенный выбор
│       │   ├── [MVP] ConstraintSolver       # Решатель ограничений
│       │   ├── [MVP] PatternMatching        # Сопоставление паттернов
│       │   └── [Extended] NoiseGeneration   # Генерация шума
│       │
│       ├── Rules/                     # Правила генерации
│       │   ├── [MVP] CityRules              # Правила города
│       │   ├── [MVP] BuildingRules          # Правила зданий
│       │   ├── [MVP] ContentRules           # Правила контента
│       │   └── [Extended] AnomalyRules      # Правила аномалий
│       │
│       └── Builders/                  # Строители
│           ├── [MVP] CityBuilder            # Строитель города
│           ├── [MVP] DistrictBuilder        # Строитель районов
│           ├── [MVP] BuildingBuilder        # Строитель зданий
│           └── [Extended] AnomalyBuilder    # Строитель аномалий
│
├── Economy/                       # [Extended] ECS-based экономика
│   ├── ECS/
│   │   ├── Components/
│   │   │   ├── [Extended] EconomyActorComponent   # Экономические акторы
│   │   │   ├── [Extended] SupplyDemandComponent   # Спрос и предложение
│   │   │   ├── [Extended] PriceComponent          # Ценообразование
│   │   │   └── [Extended] TransactionComponent    # Транзакции
│   │   ├── Systems/
│   │   │   ├── [Extended] MarketSimulationSystem  # Симуляция рынка
│   │   │   ├── [Extended] PriceCalculationSystem  # Расчет цен
│   │   │   └── [Extended] EconomyBalanceSystem    # Балансировка экономики
│   │   └── [Extended] EconomyECS            # ECS мир экономики
│   ├── [Extended] CurrencyManager           # Менеджер валют
│   └── [Extended] MarketSystem              # Рыночная система
│
├── Social/                        # [Extended] Социальная система
│   ├── [Extended] ReputationSystem          # Система репутации
│   ├── [Extended] FactionManager            # Менеджер фракций
│   ├── [Extended] QuestSystem               # Система квестов
│   └── [Extended] DialogueSystem            # Система диалогов
│
├── Network/                       # [MVP] Сетевая система
│   ├── [MVP] EldrainGameSession             # Игровая сессия
│   ├── [MVP] PlayerReplication              # Репликация игрока
│   ├── [MVP] WorldStateReplication          # Репликация мира
│   ├── [MVP] ECSNetworkBridge               # Мост ECS ↔ Network
│   ├── [Extended] AntiCheatSystem           # Защита от читов
│   └── [Extended] MatchmakingSystem         # Матчмейкинг
│
├── UI/                           # [MVP] Пользовательский интерфейс
│   ├── HUD/
│   │   ├── [MVP] MainHUD                    # Основной HUD
│   │   ├── [MVP] HealthWidget               # Виджет здоровья
│   │   └── [MVP] StatusEffectsWidget        # Виджет статусных эффектов
│   ├── Menus/
│   │   ├── [MVP] MainMenu                   # Главное меню
│   │   ├── [MVP] CharacterMenu              # Меню персонажа
│   │   ├── [MVP] InventoryMenu              # Меню инвентаря
│   │   ├── [MVP] SkillMenu                  # Меню навыков
│   │   └── [Extended] TradingMenu           # Меню торговли
│   └── Components/
│       ├── [MVP] ItemSlot                   # Слот предмета
│       ├── [MVP] SkillButton                # Кнопка навыка
│       └── [MVP] StatusEffectIcon           # Иконка статусного эффекта
│
├── Audio/                        # [MVP] Звуковая система
│   ├── [MVP] AudioManager                   # Менеджер звука
│   ├── [MVP] CombatSounds                   # Звуки боя
│   ├── [MVP] AmbientSounds                  # Звуки окружения
│   └── [Extended] SpatialAudio              # Пространственный звук
│
└── Utils/                        # [MVP] Утилиты
    ├── [MVP] GameplayStatics               # Игровые утилиты
    ├── [MVP] MathLibrary                   # Математические функции
    ├── [MVP] ECSBridge                     # Мост ECS ↔ UE5
    └── [MVP] DebugHelpers                  # Помощники отладки
```