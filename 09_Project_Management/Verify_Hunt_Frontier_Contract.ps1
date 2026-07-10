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
        if (-not $body.Contains($needle)) { $errors.Add("$([IO.Path]::GetFileName($Path)): missing contract phrase '$needle'") }
    }
}

$paths = @{
    Hunt       = Join-Path $VaultRoot '05_Combat_Survival\Hunt_Frontier_Loop.md'
    Armor      = Join-Path $VaultRoot '05_Combat_Survival\Ballistics_Armor.md'
    Thermos    = Join-Path $VaultRoot '07_Gear_Inventory\_Registries\Registry_Thermos_Modules.md'
    Sector     = Join-Path $VaultRoot '08_World_Generation\Generation\14_Sector_Content_Rules.md'
    Metadata   = Join-Path $VaultRoot '08_World_Generation\Generation\18_POI_Metadata_Registry.md'
    POIs       = Join-Path $VaultRoot '08_World_Generation\_Registries\Registry_POIs.md'
    Threshold  = Join-Path $VaultRoot '08_World_Generation\Anomaly\14_Extraction_System.md'
    Lifecycle  = Join-Path $VaultRoot '08_World_Generation\Generation\07_Server_Lifecycle.md'
    Access     = Join-Path $VaultRoot '08_World_Generation\Generation\19_Access_Contracts.md'
}

Require-Text $paths.Hunt @('не наказывает бездействие', 'не заменяет восприятие глобальным индикатором')
Require-Text $paths.Armor @('Hitbox Porn', 'projectile и мили-sweep', 'силуэт пластины, стык, мягкую зону')
Require-Text $paths.Sector @('Heat-POI', 'approach_cost', 'refusal_path', 'минимум два различающихся подхода')
Require-Text $paths.Metadata @('heat_state', 'approach_contract', 'approach_id', 'entry_anchor', 'route_layer', 'refusal_path')
Require-Text $paths.POIs @('[poi_id:: port_reverse_tide_relay]', '[heat_state:: hot]', 'relay_drain_inlet', 'relay_crane_gantry', 'tide_lift_void')
Require-Text $paths.Threshold @('поисковый путь', 'Прерванная синхронизация', 'физически забрать груз', 'T1', 'T2', 'T3', '06:00')
Require-Text $paths.Lifecycle @('Нестабильных Порогов', 'поисковых путей')
Require-Text $paths.Access @('гарантией немедленного Нестабильного Порога', 'честный вход в существующий поисковый путь')

if (Test-Path -LiteralPath $paths.Thermos) {
    $body = Get-Content -LiteralPath $paths.Thermos -Raw -Encoding UTF8
    $blocks = [regex]::Matches($body, '(?ms)^###\s+.+?\r?\n(.*?)(?=^###\s|\z)')
    foreach ($match in $blocks) {
        $block = $match.Groups[1].Value
        if ($block -notmatch '\[install_state::\s*installable\]') { continue }
        if ($block -match '\[module_id::\s*template_') { continue }
        foreach ($field in @('armor_plates', 'soft_coverage', 'seam_exposure', 'collision_silhouette', 'weight', 'vulnerability', 'balance_state')) {
            $value = [regex]::Match($block, "\[$field::\s*([^\]]+)\]").Groups[1].Value.Trim()
            if (-not $value -or $value -match '^(none|unknown|UNKNOWN)$') { $errors.Add("installable Thermos module lacks calibrated $field") }
        }
    }
}

if ($errors.Count) {
    $errors | ForEach-Object { Write-Error $_ }
    throw "Hunt frontier contract failed with $($errors.Count) issue(s)."
}

Write-Output 'Hunt frontier contract OK: hunt, plates, Heat POI and Threshold guarantees are present.'
