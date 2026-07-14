---
type: migration_note
status: superseded
system: player_core
tags: [superseded, two_paradox, migration]
superseded_by:
  - "[[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile Pipeline]]"
  - "[[04_Player_Entities/_Matrices/00_Synergy_Map|Карта решений hero-kit]]"
  - "[[04_Player_Entities/Ability_Synergy|Ability Synergy]]"
---
# Матрица Двойного Парадокса — снята с активного баланса

Семивекторная схема больше не вычисляет силу, слабость или matchup персонажа из расы и практики.

Причина снятия: она назначала ещё не спроектированному пересечению готовый боевой профиль. При расширении числа рас и специализаций это воспроизводило главную ошибку T.O.U.C.H.: свойства родителей становились общей скрытой валютой, а комбинаторика подменяла authored-качество hero-kit.

## Что сохраняется

- Историческая идея «контра создаёт возможность, а не автоматическую победу».
- Требование к наблюдаемому окну, которое игрок способен использовать из текущей позиции.
- Frame Commitment: оружейное действие временно занимает руки, линию, стойку, ресурс и Recovery.

## Что стало каноном

\`\`\`text
Race + Spec
  -> отдельный authored hero-kit
  -> named actions, arsenal and modules
  -> current loadout and Chronicle
  -> observable Combat Profile
\`\`\`

Контра существует только через конкретные \`creates_window\`, \`exploits_window\`, \`mitigates_window\`, \`exposure_channels\` и \`counterplay_now\` готового hero-kit. Тематические ярлыки не дают числового бонуса и не создают наследуемую слабость.

Старые поля \`base_vector\`, \`weak_to\`, \`add_vector\` и \`block_vector\` не переносятся. Исторические ссылки должны вести к [[04_Player_Entities/_Matrices/00_Synergy_Map|карте решений]], где незаполненный kit остаётся честным \`pending\`.
