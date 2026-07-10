param(
    [string]$VaultRoot = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
$errors = [System.Collections.Generic.List[string]]::new()
$weaponsPath = Join-Path $VaultRoot '05_Combat_Survival\Weapons'
$expectedFrames = @{
    short_cut_1h        = 'one_hand'
    point_tool_1h       = 'one_hand'
    compact_impact_1h   = 'one_hand'
    breach_impact_2h    = 'two_hand'
    reach_line_2h       = 'two_hand'
    hook_reach_2h       = 'two_hand'
    pulse_tool_1h       = 'one_hand'
    condenser_rig_2h    = 'two_hand'
    scatter_valve_2h    = 'two_hand'
    tether_launcher_2h  = 'two_hand'
    needle_thrower_2h   = 'two_hand'
    catalyst_rig_2h     = 'two_hand'
    interposition_panel_1h = 'one_hand'
}

$frameFiles = Get-ChildItem $weaponsPath -Filter '*.md' | Where-Object {
    (Get-Content -Raw $_.FullName) -match '(?m)^type:\s*weapon_frame\s*$'
}
$frames = @{}

foreach ($file in $frameFiles) {
    $body = Get-Content -Raw $file.FullName
    $frameId = [regex]::Match($body, '(?m)^frame_id:\s*(\S+)\s*$').Groups[1].Value
    $grip = [regex]::Match($body, '(?m)^grip:\s*(\S+)\s*$').Groups[1].Value
    if (-not $frameId) {
        $errors.Add("$($file.Name): missing frame_id")
        continue
    }
    $frames[$frameId] = @{ File = $file; Body = $body; Grip = $grip }
    if (-not $grip) { $errors.Add("${frameId}: missing grip") }
    if ($grip -notin @('one_hand', 'two_hand')) { $errors.Add("${frameId}: invalid grip '$grip'") }

    $instances = [regex]::Matches($body, '(?ms)^###\s+.+?\r?\n(.*?)(?=^###\s|\z)')
    if ($instances.Count -lt 2) { $errors.Add("${frameId}: requires at least two instances") }
    foreach ($instance in $instances) {
        $block = $instance.Groups[1].Value
        foreach ($field in @('instance_id', 'rarity_band', 'origin_kind', 'origin_function', 'spawn_profile', 'moveset_profile', 'commitment_cost')) {
            if ($block -notmatch "\[$field::\s*[^\]]+\]") { $errors.Add("${frameId}: instance missing $field") }
        }
        if ($block -match '\[handedness::\s*([^\]]+)\]') {
            $instanceGrip = $Matches[1].Trim()
            if ($instanceGrip -ne $grip) { $errors.Add("${frameId}: instance grip '$instanceGrip' differs from frame grip '$grip'") }
        }
    }

    $family = [regex]::Match($body, '(?m)^weapon_family:\s*(\S+)\s*$').Groups[1].Value
    if ($family -in @('arcanegun', 'catalyst')) {
        foreach ($instance in $instances) {
            $block = $instance.Groups[1].Value
            foreach ($field in @('energy_mode', 'emission_profile', 'cadence_gate')) {
                if ($block -notmatch "\[$field::\s*[^\]]+\]") { $errors.Add("${frameId}: ranged instance missing $field") }
            }
        }
    }
    if ($family -eq 'accessory') {
        foreach ($instance in $instances) {
            $block = $instance.Groups[1].Value
            foreach ($field in @('guard_input', 'guard_mechanic')) {
                if ($block -notmatch "\[$field::\s*[^\]]+\]") { $errors.Add("${frameId}: accessory instance missing $field") }
            }
        }
    }
}

foreach ($frameId in $expectedFrames.Keys) {
    if (-not $frames.ContainsKey($frameId)) { $errors.Add("missing required frame $frameId") }
    elseif ($frames[$frameId].Grip -ne $expectedFrames[$frameId]) { $errors.Add("${frameId}: expected grip $($expectedFrames[$frameId])") }
}
foreach ($frameId in $frames.Keys) {
    if (-not $expectedFrames.ContainsKey($frameId)) { $errors.Add("unexpected active frame $frameId") }
}

$comboPath = Join-Path $VaultRoot '04_Player_Entities\_Registries\Registry_Combos.md'
$combos = Get-Content -Raw $comboPath
if ($combos -match '\[weapon_instance::') { $errors.Add('Registry_Combos still stores weapon_instance entries') }
$comboFrames = @()
foreach ($block in ($combos -split '(?m)^##\s+')) {
    if ($block -notmatch '\[id::\s*([^\]]+)\]') { continue }
    if ($Matches[1].Trim().StartsWith('template_')) { continue }
    $comboFrames += [regex]::Matches($block, '\[weapon_frame::\s*([^\]]+)\]\s*\|\s*\[prof::\s*([12])\]')
}
if ($comboFrames.Count -ne 36) { $errors.Add("Registry_Combos: expected 36 live frame mastery rows, found $($comboFrames.Count)") }
foreach ($entry in $comboFrames) {
    $frameId = $entry.Groups[1].Value.Trim()
    if (-not $expectedFrames.ContainsKey($frameId)) { $errors.Add("Registry_Combos references unknown frame $frameId") }
}

$tagsPath = Join-Path $VaultRoot '04_Player_Entities\Tags_System.md'
$tags = Get-Content -Raw $tagsPath
foreach ($field in @('arsenal_grant', 'arsenal_block')) {
    if ($tags -notmatch "\[$field::") { $errors.Add("Tags_System does not define $field") }
}

if ($errors.Count) {
    $errors | ForEach-Object { Write-Error $_ }
    throw "Weapon contract failed with $($errors.Count) issue(s)."
}

Write-Output "Weapon contract OK: $($frames.Count) frames, $($comboFrames.Count) Combo mastery rows."
