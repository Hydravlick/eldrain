---
type: implementation_plan
status: active
system: hunt_frontier
tags: [mvp, combat, armor, extraction, poi, anomaly, routes]
related_files:
  - "[[09_Project_Management/Hunt_Frontier_Ecosystem_Design|Hunt_Frontier_Ecosystem_Design]]"
  - "[[09_Project_Management/Architecture_MVP|Architecture_MVP]]"
---
# Hunt Frontier Ecosystem Implementation Plan

> **For agentic workers:** execute one task at a time; preserve unrelated vault edits; do not use Git for this vault. Every task ends with a local link and contract check before the next task begins.

**Goal:** Make the active GDD describe one connected MVP ecosystem in which quests and Heat-POI create routes, weapons resolve hit geometry, armor enables deliberate plate play, skills alter scenes, and rare Unstable Thresholds provide contested exits throughout the T1/T2/T3 server cycle.

**Architecture:** `05_Combat_Survival` owns action, hit, sound and commitment rules; `04_Player_Entities` owns P/Q/E and allowed arsenal; `08_World_Generation` owns Heat-POI, route topology, phase evolution and Threshold generation; `06_Economy_Loot` retains manifest and post-extraction ownership. The new Hunt Frontier page coordinates these systems but does not duplicate their formulas or registries.

**Tech Stack:** Obsidian Markdown, YAML frontmatter, inline Dataview fields, PowerShell validation.

## Global Constraints

- This plan implements [[09_Project_Management/Hunt_Frontier_Ecosystem_Design|the approved design contract]], not a numeric balance pass.
- Do not add a Power Score, global noise meter, passive anti-camper timer, hidden anti-position protection, or a damage/weight/radius/price value not already calibrated by a prototype.
- T1 is the learnable entry ecology; T2 makes the whole ecology threatening; T3 is the pinnacle for the best prepared builds and their mechanics.
- Weapon frames only deliver physical or magostrel hits. Tether, scene defense and anomaly procedure belong to P/Q/E or a skill device.
- A plate is a visible, deliberately orientable collision surface. Its seams, coverage, mass, physical position and capacity price must be explicit before installation is legal.
- Plate readiness requires a projectile and melee-sweep audit against moving, crouching and turning targets, plus distinct feedback for plate, seam and soft hits.
- A Heat-POI offers work, route change and contest; it is never merely a larger loot container.
- Every ordinary active-sector evacuation uses an Unstable Threshold: rare, temporary, locally foreshadowed, contestable and available in T1, T2 and T3.
- Every valid active insertion retains at least one world-readable search path toward a possible Threshold; exact spawn time and anchor remain unknown.
- Threshold synchronization reserves no permanent ownership: successful departure consumes capacity, interruption returns an open readable reset state, and only physically carried cargo can leave with each body.
- Do not use Git, worktrees, archives, old namespaces or `docs/` as an active design target.

---

### Task 1: Establish the cross-system Hunt Frontier contract

**Files:**
- Create: `05_Combat_Survival/Hunt_Frontier_Loop.md`
- Modify: `05_Combat_Survival/Combat_Three_Debts.md`
- Modify: `05_Combat_Survival/Acoustic_Stealth.md`
- Modify: `05_Combat_Survival/Dissonance_System.md`

**Consumes:** the approved Hunt Frontier design, the existing `AcousticEvent` schema, `DissonanceLoad`, `DissonancePulse`, and the three-debt action cycle.

**Produces:** one authoritative connection between route, trace, commitment, changed situation, cargo and contested return; no new universal meter.

- [ ] **Step 1: Create the universal page with the player-facing promise and loop.**

  Begin the page with:

  ```markdown
  > В Аномалии засада законна, но после сильного действия охотник оставляет след и сам становится добычей.

  контракт / Heat-POI -> маршрут -> след -> Commitment
  -> изменённая сцена -> груз -> Нестабильный Порог -> уход или глубина
  ```

  Define physical, acoustic and aether traces as separate readable evidence. State that none reveals a live target coordinate.

- [ ] **Step 2: Add the hunt consequence to the combat contract.**

  Add a rule to `Combat_Three_Debts.md` after the common action cycle:

  ```markdown
  Сильное действие меняет охоту: оно оставляет доступный контр-игре след, меняет маршрут, создаёт груз или открывает спорную работу. Бездействие не получает отдельного наказания от системы.
  ```

- [ ] **Step 3: Connect sound and Dissonance without collapsing them.**

  In `Acoustic_Stealth.md`, state that sound supplies a last-heard area and material/height read. In `Dissonance_System.md`, state that aether attention is a reaction to foreign matter and strong ether action, never an idle-player detector.

- [ ] **Step 4: Verify ownership and links.**

  Run:

  ```powershell
  rg -n "Hunt_Frontier_Loop|последнюю слышимую область|бездействие" C:\eldrain\05_Combat_Survival
  ```

  Expected: the new page is linked by the combat, sound and Dissonance pages; neither page introduces a global target coordinate or idle timer.

### Task 2: Separate weapon hit geometry from scene-changing skills

**Files:**
- Modify: `05_Combat_Survival/Weapon_Core.md`
- Modify: `05_Combat_Survival/Weapon_Ranged.md`
- Modify: `05_Combat_Survival/Weapons/Weapon_Manifesto.md`
- Modify: `05_Combat_Survival/_Registries/Registry_Weapons.md`
- Modify: `04_Player_Entities/_Registries/Registry_Skill_Types.md`
- Modify: `04_Player_Entities/Combat_Profile_Pipeline.md`
- Modify: `04_Player_Entities/Proficiency_Arsenal.md`
- Modify: `04_Player_Entities/_Registries/Registry_Combos.md`
- Modify: `04_Player_Entities/Tags_System.md`
- Modify: `09_Project_Management/Verify_Weapons_Contract.ps1`
- Reclassify: `05_Combat_Survival/Weapons/Tether_Launcher_2H.md`, `05_Combat_Survival/Weapons/Catalyst_Rig_2H.md`, `05_Combat_Survival/Weapons/Interposition_Panel_1H.md`

**Consumes:** `weapon_frame` records, Combo arsenal rows, the existing `mobility`, `defense` and `device` energy contracts.

**Produces:** an active weapon registry containing only hit-delivery frames, and skill categories that own tether, defense panel and anomaly procedure.

- [ ] **Step 1: State the weapon boundary in all three weapon overviews.**

  Use the same rule in each overview:

  ```markdown
  Фрейм отвечает только на то, как оружие поражает тело или поверхность: хват, траекторию, линию, конус, подготовку и Recovery. Изменение маршрута, переносной заслон и аномальная процедура не являются функцией оружейного фрейма.
  ```

- [ ] **Step 2: Reclassify the three non-weapon concepts before removing active access.**

  Change their frontmatter to a non-`weapon_frame` proposal type, set `status: deferred`, and add a one-line destination:

  ```markdown
  Тросовая связь станет `mobility`/`crowd_control` навыком; заслон — `defense` навыком; аномальная процедура — `device` навыком с явным источником энергии.
  ```

  Do not delete their material, risks or fiction; they are valid sources for future Combo abilities.

- [ ] **Step 3: Move only the ownership, not invented abilities.**

  Add `anomaly_procedure` as a skill type in `Registry_Skill_Types.md` with `energy_contract:: device`; retain existing `mobility` for tether and `defense` for the panel. In `Registry_Combos.md`, remove the three reclassified frame rows and their `combat_role`; do not replace them with unnamed P/Q/E. The active MVP audit already states that no Combo is content-approved.

- [ ] **Step 4: Reduce the active weapon contract to the remaining ten frames.**

  Remove the three IDs from `Registry_Weapons.md`, `Tags_System.md` and `$expectedFrames` in `Verify_Weapons_Contract.ps1`. The current nine Combo blocks contain ten rows for these three concepts, so update the expected live mastery-row count from `36` to `26`, then run:

  ```powershell
  powershell -NoProfile -ExecutionPolicy Bypass -File C:\eldrain\09_Project_Management\Verify_Weapons_Contract.ps1 -VaultRoot C:\eldrain
  ```

  Expected: the validator reports the exact active-frame and active-mastery-row counts with no references to the three deferred concepts.

### Task 3: Make armor a legal, readable hitbox game

**Files:**
- Modify: `05_Combat_Survival/Ballistics_Armor.md`
- Modify: `07_Gear_Inventory/Thermos_System.md`
- Modify: `07_Gear_Inventory/_Registries/Registry_Thermoses.md`
- Modify: `07_Gear_Inventory/_Registries/Registry_Thermos_Modules.md`
- Modify: `07_Gear_Inventory/Item_Attributes_UI.md`

**Consumes:** soft mesh reduction, hard-plate colliders, Tермос physical slots and module capacity.

**Produces:** an installable armor contract whose coverage and seams can be read and played before numeric tuning.

- [ ] **Step 1: Add the active armor promise and collision rules.**

  Add this contract to `Ballistics_Armor.md`:

  ```markdown
  Пластина не прибавляет общую жизнь. Она даёт телу конкретную поверхность, которую игрок может развернуть под удар. Контригра живёт в покрытии, стыке, боковой линии, спине, высоте и движении, а не в скрытом пробитии.
  ```

- [ ] **Step 2: Define the mandatory fields for an installable plate.**

  Every `install_state:: installable` plate record must contain `armor_plates`, `soft_coverage`, `seam_exposure`, `slot_size`, `module_positions`, `module_cost`, `weight`, `vulnerability`, and a non-`unknown` balance state. Add the same fields to the registry template and master UI card.

- [ ] **Step 3: Keep uncalibrated multi-zone packages blocked.**

  Preserve `blocked_calibration` for existing packages until they are split into legal modules. Do not convert an `UNKNOWN` plate package into an installable item merely to make the roster look complete.

- [ ] **Step 4: Verify no plate lies to the player.**

  Run:

  ```powershell
  rg -n "\[install_state:: installable\]|\[armor_plates::|\[seam_exposure::|\[soft_coverage::" C:\eldrain\07_Gear_Inventory\_Registries\Registry_Thermos_Modules.md
  ```

  Expected: every installable plate exposes coverage and seams; blocked packages remain visibly blocked. Then run projectile and melee-sweep checks on moving, crouching and turning targets; the acceptance report records visible silhouette, hit feedback and post-death cause recognition.

### Task 4: Put Heat-POI and route counterplay in world generation

**Files:**
- Modify: `08_World_Generation/Generation/14_Sector_Content_Rules.md`
- Modify: `08_World_Generation/Generation/17_Dual_State_POIs.md`
- Modify: `08_World_Generation/Generation/18_POI_Metadata_Registry.md`
- Modify: `08_World_Generation/_Registries/Registry_POIs.md`
- Modify: `08_World_Generation/Generation/07_Server_Lifecycle.md`
- Modify: `05_Combat_Survival/Movement_Physics.md`

**Consumes:** Active T1/T2/T3 POI state, route metadata, movement commitment and weight/verticality rules.

**Produces:** Heat as a visible active-POI state and a route contract that protects counterplay without forcing map symmetry.

- [ ] **Step 1: Add the Heat field to raid POI metadata.**

  Extend `raid_state` with:

  ```text
  heat_state: cold | warm | hot
  heat_signal: world-readable cue
  heat_work: contract / rare method / embedded node / rescue / route key
  approach_contract: quiet_long | loud_fast | vertical | skill | hazard
  ```

  `heat_state` is current-instance state and never persists as a Stable market bonus.

- [ ] **Step 2: Define the three Heat states and their route promise.**

  In sector rules, require Hot POI to contain valuable work, observable activity, at least two differing approaches and one refusal/avoidance route. Each approach must expose a world cue before Commitment, a distinct price/exposure and a readable refusal result. Prohibit a Hot POI whose only interaction is a larger loot roll.

- [ ] **Step 3: Tie phase progression to ecology, not raw enemy level.**

  Add to `Server_Lifecycle.md` and the POI resolver: T1 teaches readable danger in an accessible ecology; T2 makes environment, creatures, players and routes jointly demanding; T3 is the full build-and-mechanics culmination. Preserve T1/T2/T3 changes to rooms, routes and work, not only mob health or loot color.

- [ ] **Step 4: Verify the route contract.**

  Run:

  ```powershell
  rg -n "heat_state|approach_contract|тихий|шумный|вертик" C:\eldrain\08_World_Generation C:\eldrain\05_Combat_Survival\Movement_Physics.md
  ```

  Expected: Heat is defined in one metadata schema and sector rules; movement documents the body cost of the offered routes.

### Task 5: Replace fixed exits with Unstable Thresholds across the full cycle

**Files:**
- Modify: `08_World_Generation/Anomaly/14_Extraction_System.md`
- Modify: `08_World_Generation/Generation/07_Server_Lifecycle.md`
- Modify: `08_World_Generation/Generation/19_Access_Contracts.md`
- Modify: `06_Economy_Loot/Extraction_Stabilization_Loop.md`
- Modify: `08_World_Generation/Generation/14_Sector_Content_Rules.md`

**Consumes:** six-hour cycle, Phase Shift, confirmed cargo manifest, Access Contract and sector route topology.

**Produces:** one ordinary evacuation system: rare temporary Thresholds that can be found, contested and used in every phase, while 06:00 remains fatal.

- [ ] **Step 1: Replace the fixed-exit taxonomy with the Threshold state machine.**

  Make `14_Extraction_System.md` own:

  ```text
  forewarning -> seam birth -> contested approach -> synchronization
  -> individual departure -> fade / local reconfiguration
  ```

  State that Thresholds are exits home, not entrances, and that ordinary evacuation does not use a permanent map-edge exit.

- [ ] **Step 2: Define fair uncertainty.**

  Require each Threshold to use a valid seam anchor, a local physical forewarning, a contestable synchronization, a capacity rule for people and confirmed cargo, and an open reset state after interruption. Require every valid active insertion to retain a world-readable search path toward a possible Threshold. Prohibit a global map marker, exact respawn schedule and repeated farming of the same anchor.

- [ ] **Step 3: Bind Threshold meaning to T1/T2/T3.**

  In `Server_Lifecycle.md`, retain Threshold births throughout all six hours. T1 Thresholds are legible learning exits; T2 Thresholds emerge through remembered emergency routes and whole-ecology pressure; T3 Thresholds are rare Reassembly errors that test the best prepared builds. At 06:00 no Threshold overrides Stabilization death.

- [ ] **Step 4: Preserve cargo and contract integrity.**

  Keep `Secure Manifest` as the only route to personal ownership. A successful departure consumes capacity only for its own body and physically carried cargo; an interrupted synchronization consumes neither and returns the Threshold to open contention. A Threshold cannot stabilize a ground item remotely, extract a dead ally's body without the body being carried, or convert failed contract cargo into delivered progress.

- [ ] **Step 5: Verify no old ordinary exit survives as the active rule.**

  Run:

  ```powershell
  rg -n "Always Open|дойти до края|Static|Нестабильн(ый|ые) Порог|Стабилизац" C:\eldrain\08_World_Generation\Anomaly\14_Extraction_System.md C:\eldrain\08_World_Generation\Generation\07_Server_Lifecycle.md
  ```

  Expected: fixed public exits are absent as ordinary evacuation; Thresholds exist in all three phases; Stabilization remains absolute.

### Task 6: Turn the design into an MVP acceptance contract

**Files:**
- Modify: `09_Project_Management/TODO.md`
- Modify: `09_Project_Management/Risk_Register.md`
- Modify: `09_Project_Management/Hunt_Frontier_Ecosystem_Design.md`
- Create: `09_Project_Management/Verify_Hunt_Frontier_Contract.ps1`

**Consumes:** the active GDD changes from Tasks 1–5.

**Produces:** a small, repeatable structural check and a playtest acceptance list for the `Непрошеный гость` slice.

- [ ] **Step 1: Add the slice as a gated MVP item.**

  `TODO.md` must name one Hot POI, two spatially distinct approaches with separate entry anchors, explicit plate coverage/seams, one scene-changing skill, one Threshold anchor pool and success/retreat/failure observations. Do not schedule all 13 legacy frames or a full item economy.

- [ ] **Step 2: Add concrete risks and stop conditions.**

  `Risk_Register.md` must track: unreadable plate death, unavoidable choke point, static-exit regression, undiscoverable Threshold, ambiguous Threshold reservation/cargo, Heat becoming a loot multiplier, T3 becoming only higher health, T3 best-build rejection by Dissonance, and a deferred device returning as a weapon frame.

- [ ] **Step 3: Write a structural validator.**

  The validator pair must fail when the Hunt page is missing, an active weapon registry still lists tether/catalyst/panel, an installable plate lacks a required coverage field, a Hot POI lacks an approach contract, or the extraction page lacks all three Tier labels, the Threshold state machine, search-path availability and interruption reset semantics.

- [ ] **Step 4: Run both validators.**

  ```powershell
  powershell -NoProfile -ExecutionPolicy Bypass -File C:\eldrain\09_Project_Management\Verify_Weapons_Contract.ps1 -VaultRoot C:\eldrain
  powershell -NoProfile -ExecutionPolicy Bypass -File C:\eldrain\09_Project_Management\Verify_Hunt_Frontier_Contract.ps1 -VaultRoot C:\eldrain
  ```

  Expected: both return exit code 0. The result proves document structure, not balance; playtests answer the open measurements in the design contract.

## Plan Self-Review

**Coverage:** the plan has one task each for hunt/trace, weapon boundary, Hitbox Porn armor, Heat-POI, Threshold exit progression and MVP validation.

**Scope:** the plan deliberately postpones numerical calibration, final P/Q/E content and full economy implementation. The current MVP matrix has no approved Combo content, so inventing replacement skill abilities would be false canon.

**Consistency:** `Heat` remains a POI state, `Dissonance` remains a player/item signal, and an Unstable Threshold remains a rare exit home. These terms do not overlap or create a universal score.
