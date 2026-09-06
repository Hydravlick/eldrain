---
status: active
system: server_generation_pipeline
tags:
  - generation
  - staging
  - publication
  - networking
related_files:
  - "[[08_World_Generation/Generation/Location_Revision_Lifecycle|Location Revision Lifecycle]]"
  - "[[08_World_Generation/Generation/Server_Lifecycle|Server Lifecycle]]"
  - "[[08_World_Generation/Reality_Integrity|Reality Integrity]]"
type: system
index_route: owner
index_group: world_generation
index_order: 250
index_summary: Описывает безопасную подготовку следующей ревизии мира вне живых рейдовых сессий.
read_when: Читайте при изменении фоновой сборки, публикации или доставки новой LocationRevision.
---
# Фоновая сборка ревизии мира

## 1. Назначение

Следующая `LocationRevision` готовится вне опубликованной ревизии и вне любого живого `SessionRuntime`. Фоновая работа не меняет двери, противников, предметы или геометрию текущего рейда. Полный контракт состояний, Stable-постгенерации и публикации принадлежит [[08_World_Generation/Generation/Location_Revision_Lifecycle|Location Revision Lifecycle]].

## 2. Контур подготовки

```text
authored generation inputs
  -> staged location data
  -> topology and asset validation
  -> immutable LocationRevision candidate
  -> publisher acceptance
  -> distributable revision bundle
```

Черновик может собираться частями и переживать повторный запуск. Игроки не видят его до атомарной публикации. Ошибка подготовки отбрасывает кандидата, но не откатывает активный мир и не переносит в новый цикл состояние выбранной рейдовой сессии.

## 3. Производственные ограничения

- бюджет фоновой работы измеряется на целевой серверной сборке; фиксированный лимит кадра или конкретный движковый coroutine здесь не утверждается;
- тяжёлые ассеты допускают поэтапную подготовку, но ссылка становится публичной только после проверки целостности всего пакета;
- содержимое контейнера и другие рейдовые сущности создаются владельцами loot/runtime, а не этим pipeline;
- клиент получает идентификатор и проверяемый пакет опубликованной ревизии, а не доверенный seed, которым можно самостоятельно определить авторитетную геометрию или добычу;
- момент публикации задают владельцы lifecycle. Эта страница не вводит отдельный таймер фоновой подгрузки.

## 4. Отказ и наблюдаемость

Publisher хранит причину принятия или отказа кандидата, исходные authored inputs и версии валидаторов. Если пакет не готов, продолжает действовать последняя опубликованная ревизия либо lifecycle выбирает явный режим недоступности. Частично собранный мир не становится доступным молча.
