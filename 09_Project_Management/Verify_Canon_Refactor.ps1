param(
    [string]$VaultRoot = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
$errors = [System.Collections.Generic.List[string]]::new()

function Require-Text {
    param([string]$Path, [string[]]$Needles)
    if (-not (Test-Path -LiteralPath $Path)) {
        $errors.Add("Missing required file: $Path")
        return
    }
    $body = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    foreach ($needle in $Needles) {
        if (-not $body.Contains($needle)) { $errors.Add("$([IO.Path]::GetFileName($Path)): missing '$needle'") }
    }
}

$retiredFiles = @(
    '04_Player_Entities\Shell_Projections.md',
    '05_Combat_Survival\Ballistics_PvP.md',
    '05_Combat_Survival\Архитектура.md',
    '05_Combat_Survival\Weapons\Tether_Launcher_2H.md',
    '05_Combat_Survival\Weapons\Catalyst_Rig_2H.md',
    '05_Combat_Survival\Weapons\Interposition_Panel_1H.md'
)
foreach ($relativePath in $retiredFiles) {
    if (Test-Path -LiteralPath (Join-Path $VaultRoot $relativePath)) { $errors.Add("Retired duplicate still exists: $relativePath") }
}

Require-Text (Join-Path $VaultRoot '04_Player_Entities\Accessible_Candidates.md') @('Доступный кандидат', 'Подопечный', 'Ward')
Require-Text (Join-Path $VaultRoot '01_Core_Vision\Glossary.md') @('Accessible Candidate', 'Подопечный (Ward)', 'Frame Class', 'Cadence Gate')
Require-Text (Join-Path $VaultRoot '05_Combat_Survival\Ballistics_Armor.md') @('0 Урона по HP', 'рикошет', 'Aim Punch')
Require-Text (Join-Path $VaultRoot '04_Player_Entities\_Registries\Registry_Combos.md') @('Статическая карта MVP', 'Единственный источник статуса')

$scanRoots = @(
    '00_Index.md',
    '01_Core_Vision',
    '04_Player_Entities',
    '05_Combat_Survival',
    '07_Gear_Inventory',
    '08_World_Generation',
    '09_Project_Management'
)
$legacyPatterns = @(
    '\bБомж(и|а|е|ей|у|ом)?\b',
    'Проекция / Бомж',
    'New Drifter',
    'Ballistics_PvP',
    'Shell_Projections',
    'tether_launcher_2h',
    'catalyst_rig_2h',
    'interposition_panel_1h'
)
foreach ($root in $scanRoots) {
    $path = Join-Path $VaultRoot $root
    $files = if (Test-Path -LiteralPath $path -PathType Leaf) { Get-Item -LiteralPath $path } else { Get-ChildItem -LiteralPath $path -Filter '*.md' -Recurse }
    foreach ($file in $files) {
        $body = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
        foreach ($pattern in $legacyPatterns) {
            if ($body -match $pattern) { $errors.Add("Legacy term '$pattern' remains in $($file.FullName)") }
        }
    }
}

if ($errors.Count) {
    $errors | ForEach-Object { Write-Error $_ }
    throw "Canon refactor failed with $($errors.Count) issue(s)."
}

Write-Output 'Canon refactor OK: roster terminology, frame vocabulary and retired duplicates are clean.'
