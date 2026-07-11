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
    needle_thrower_2h   = 'two_hand'
}
$allowedFamilies = @('blade', 'blunt', 'polearm', 'arcanegun')
$retiredFrameIds = @('tether_launcher_2h', 'catalyst_rig_2h', 'interposition_panel_1h')

$frameFiles = Get-ChildItem $weaponsPath -Filter '*.md' | Where-Object {
    (Get-Content -Raw $_.FullName) -match '(?m)^type:\s*weapon_frame\s*$'
}
$frames = @{}
foreach ($file in $frameFiles) {
    $body = Get-Content -Raw $file.FullName
    $frameId = [regex]::Match($body, '(?m)^frame_id:\s*(\S+)\s*$').Groups[1].Value
    $grip = [regex]::Match($body, '(?m)^grip:\s*(\S+)\s*$').Groups[1].Value
    if (-not $frameId) { $errors.Add("$($file.Name): missing frame_id"); continue }
    $frames[$frameId] = @{ File = $file; Body = $body; Grip = $grip }
    if ($grip -notin @('one_hand', 'two_hand')) { $errors.Add("${frameId}: invalid grip '$grip'") }
    $family = [regex]::Match($body, '(?m)^weapon_family:\s*(\S+)\s*$').Groups[1].Value
    if ($family -notin $allowedFamilies) { $errors.Add("${frameId}: forbidden active weapon_family '$family'") }
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
$comboFrames = @()
foreach ($block in ($combos -split '(?m)^##\s+')) {
    if ($block -notmatch '\[id::\s*([^\]]+)\]') { continue }
    if ($Matches[1].Trim().StartsWith('template_')) { continue }
    $comboFrames += [regex]::Matches($block, '\[weapon_frame::\s*([^\]]+)\]\s*\|\s*\[prof::\s*([12])\]')
}
if ($comboFrames.Count -ne 26) { $errors.Add("Registry_Combos: expected 26 live frame mastery rows, found $($comboFrames.Count)") }
foreach ($entry in $comboFrames) {
    $frameId = $entry.Groups[1].Value.Trim()
    if (-not $expectedFrames.ContainsKey($frameId)) { $errors.Add("Registry_Combos references unknown frame $frameId") }
}

$tags = Get-Content -Raw (Join-Path $VaultRoot '04_Player_Entities\Tags_System.md')
$registryTags = Get-Content -Raw (Join-Path $VaultRoot '04_Player_Entities\_Registries\Registry_Tags.md')
foreach ($retiredFrameId in $retiredFrameIds) {
    if ($combos -match "\[weapon_frame::\s*$retiredFrameId\s*\]") { $errors.Add("Registry_Combos still references retired frame $retiredFrameId") }
    if ($tags -match "\[arsenal_(grant|block)::[^\]]*$retiredFrameId") { $errors.Add("Tags_System still references retired frame $retiredFrameId") }
    if ($registryTags -match "\[arsenal_(grant|block)::[^\]]*$retiredFrameId") { $errors.Add("Registry_Tags still references retired frame $retiredFrameId") }
}

if ($errors.Count) {
    $errors | ForEach-Object { Write-Error $_ }
    throw "Weapon contract failed with $($errors.Count) issue(s)."
}

Write-Output "Weapon contract OK: $($frames.Count) frames, $($comboFrames.Count) Combo mastery rows."
