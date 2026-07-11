param(
    [string]$VaultRoot = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
$errors = [System.Collections.Generic.List[string]]::new()

function Read-Text([string]$relativePath) {
    $path = Join-Path $VaultRoot $relativePath
    if (-not (Test-Path -LiteralPath $path)) {
        $errors.Add("Missing required file: $relativePath")
        return ''
    }
    Get-Content -LiteralPath $path -Raw -Encoding UTF8
}

function Field([string]$body, [string]$name) {
    $match = [regex]::Match($body, "(?m)^\[$([regex]::Escape($name))::\s*([^\]]+)\]")
    if ($match.Success) { return $match.Groups[1].Value.Trim() }
    return $null
}

function Require-Field([string]$body, [string]$name, [string]$label) {
    if (-not (Field $body $name)) { $errors.Add("$label misses [${name}:: ...]") }
}

function Require-Concrete([string]$body, [string]$name, [string]$label) {
    $value = Field $body $name
    if (-not $value -or $value -eq 'none') { $errors.Add("$label requires concrete [${name}:: ...]") }
}

function Strip-FencedBlocks([string]$body) {
    [regex]::Replace($body, '(?ms)^```.*?^```\s*', '')
}

$touch = Read-Text '04_Player_Entities\Attributes_TOUCH.md'
$skills = Read-Text '04_Player_Entities\Skill_Build_Philosophy.md'
$grammar = Read-Text '04_Player_Entities\_Registries\Registry_Skill_Types.md'
$combos = Read-Text '04_Player_Entities\_Registries\Registry_Combos.md'
$validatorFixture = Read-Text '09_Project_Management\_Fixtures\Skill_Contract_Valid.md'

if ($skills -notmatch '(?m)^status:\s*active\s*$') {
    $errors.Add('Skill_Build_Philosophy must be active.')
}

$abilityFields = @(
    'skill_slot', 'kernel', 'window_function', 'effect_domain', 'delivery_form',
    'carrier_contract', 'supply_contract', 'carrier_fate', 'effect_persistence',
    'target_scope', 'required_interface', 'compatible_frames', 'carrier_ref', 'consume_amount',
    'consumption_point', 'depletion_rule', 'retrieval_rule', 'economic_output', 'placement_limit',
    'reserve_id', 'reserve_capacity', 'reserve_recovery', 'nonextractable',
    'payload_family', 'status_effect', 'output_properties', 'passive_trigger', 'passive_state',
    'passive_properties', 'passive_loss_rule', 'touch_components', 'fixed_terms',
    'fixed_debt', 'interrupt_rule', 'counterplay', 'downstream_edges',
    'energy_contract', 'battery_version', 'cantrip_version', 'overcharge_version',
    'impulse_cost', 'casting_reserve_required'
)

$enumFields = @{
    kernel = @('strike', 'deploy', 'alter', 'guard', 'traverse', 'treat', 'perceive', 'operate')
    window_function = @('create', 'exploit', 'mitigate')
    effect_domain = @('harm', 'displacement', 'state', 'restore', 'protection', 'information', 'interaction')
    delivery_form = @('self', 'contact', 'weapon_bound', 'projectile', 'thrown', 'placed', 'tether', 'field', 'channel', 'procedure')
    carrier_contract = @('body', 'current_frame', 'consumable', 'device', 'environment_node')
    supply_contract = @('stamina', 'biological_reserve', 'battery_impulse', 'item_charge', 'device_charge', 'local_material')
    carrier_fate = @('retained', 'consumed', 'deployed')
    effect_persistence = @('instant', 'maintained', 'attached', 'anchored')
    target_scope = @('self', 'single', 'line', 'cone', 'area', 'surface', 'device', 'environment_node')
    consumption_point = @('none', 'commitment', 'release', 'placement', 'maintenance')
    economic_output = @('none', 'nonextractable')
    nonextractable = @('true', 'false')
    energy_contract = @('body', 'hybrid', 'device')
    casting_reserve_required = @('true', 'false')
}
foreach ($required in $abilityFields) {
    if ($skills -notmatch "\[$([regex]::Escape($required))::") {
        $errors.Add("Skill philosophy misses schema field: $required")
    }
    if ($grammar -notmatch "\[$([regex]::Escape($required))::") {
        $errors.Add("Skill grammar misses schema field: $required")
    }
}

$skillSchema = [regex]::Match($skills, '(?ms)```markdown\s*(\[skill_slot::.*?\])\s*```').Groups[1].Value.Trim()
$grammarSchema = [regex]::Match($grammar, '(?ms)```markdown\s*(\[skill_slot::.*?\])\s*```').Groups[1].Value.Trim()
if (-not $skillSchema -or -not $grammarSchema -or $skillSchema -ne $grammarSchema) {
    $errors.Add('Skill philosophy and Registry_Skill_Types must expose the exact same schema and enums.')
}

foreach ($required in @('OwnerResolve', 'R(FinalTOUCH)^w', 'ExplicitCorruptionException')) {
    if (($touch + "`n" + $skills) -notmatch [regex]::Escape($required)) {
        $errors.Add("TOUCH contract misses: $required")
    }
}

$scanRoots = @('04_Player_Entities', '05_Combat_Survival', '07_Gear_Inventory', '08_World_Generation')
$forbiddenField = '\[(substats|substat_bonus|substat_mult|condition_bonus|tradeoff|cap_mod|skill_prof_delta|touch_condition|ability_kernel|skill_functions|downstream|output_mod)::'
foreach ($scanRoot in $scanRoots) {
    $path = Join-Path $VaultRoot $scanRoot
    Get-ChildItem -LiteralPath $path -Recurse -Filter '*.md' | ForEach-Object {
        $body = Get-Content -LiteralPath $_.FullName -Raw -Encoding UTF8
        $relative = $_.FullName.Substring($VaultRoot.Length).TrimStart('\')
        if ($body -match $forbiddenField) {
            $errors.Add("Retired field remains: $relative")
        }
        foreach ($match in [regex]::Matches($body, '(?m)^\[owned_output_mod::\s*([^\]]+)\]')) {
            $value = $match.Groups[1].Value.Trim()
            if ($value -ne 'none' -and $value -notmatch '^[A-Za-z0-9_-]+\.[A-Za-z0-9_.-]+\s+[+-][A-Za-z0-9.%_-]+$') {
                $errors.Add("owned_output_mod must be one owner.final_parameter delta: $relative")
            }
        }
    }
}

$entityPaths = @(
    Get-ChildItem -LiteralPath (Join-Path $VaultRoot '04_Player_Entities\Races') -Filter '*.md'
    Get-ChildItem -LiteralPath (Join-Path $VaultRoot '04_Player_Entities\Specs') -Filter '*.md'
)
foreach ($entity in $entityPaths) {
    $body = Get-Content -LiteralPath $entity.FullName -Raw -Encoding UTF8
    foreach ($attribute in @('TRQ', 'GRP', 'LYR', 'GLW', 'SNS')) {
        if ($body -notmatch "(?m)^touch_${attribute}:\s*-?\d+") {
            $errors.Add("$($entity.Name) misses touch_$attribute")
        }
    }
}

$allowedInterfaces = @('edge', 'point', 'impact_surface', 'contact_surface', 'brace', 'conduit', 'projectile', 'reach', 'free_hand')
$weaponPath = Join-Path $VaultRoot '05_Combat_Survival\Weapons'
$weaponInterfaces = @{}
foreach ($weapon in Get-ChildItem -LiteralPath $weaponPath -Filter '*.md') {
    $body = Get-Content -LiteralPath $weapon.FullName -Raw -Encoding UTF8
    $line = [regex]::Match($body, '(?m)^skill_interfaces:\s*\[([^\]]+)\]')
    if (-not $line.Success) {
        $errors.Add("Weapon frame misses skill_interfaces: $($weapon.Name)")
        continue
    }
    foreach ($interface in ($line.Groups[1].Value -split ',' | ForEach-Object { $_.Trim() })) {
        if ($interface -notin $allowedInterfaces) {
            $errors.Add("Unknown skill interface '$interface' in $($weapon.Name)")
        }
    }
    $frameId = [regex]::Match($body, '(?m)^frame_id:\s*([^\s]+)').Groups[1].Value
    if ($frameId) { $weaponInterfaces[$frameId] = @($line.Groups[1].Value -split ',' | ForEach-Object { $_.Trim() }) }
}

$consumableText = Read-Text '07_Gear_Inventory\_Registries\Registry_Consumables.md'
$consumableRefs = @([regex]::Matches($consumableText, '(?m)^\[consumable_id::\s*([^\]]+)\]') | ForEach-Object { $_.Groups[1].Value.Trim() })
$deviceRefs = @()
$environmentRefs = @()
Get-ChildItem -LiteralPath $VaultRoot -Recurse -Filter '*.md' | ForEach-Object {
    $body = Get-Content -LiteralPath $_.FullName -Raw -Encoding UTF8
    $deviceRefs += @([regex]::Matches($body, '(?m)^\[(?:device_id|module_id)::\s*([^\]]+)\]') | ForEach-Object { $_.Groups[1].Value.Trim() })
    $environmentRefs += @([regex]::Matches($body, '(?m)^\[(?:environment_node_id|poi_id)::\s*([^\]]+)\]') | ForEach-Object { $_.Groups[1].Value.Trim() })
}

$canonicalCombos = Strip-FencedBlocks $combos
$canonicalApprovedCount = [regex]::Matches($canonicalCombos, '(?m)^\[design_status::\s*approved\s*\]$').Count
$cleanCombos = $canonicalCombos + "`n" + $validatorFixture
$comboBlocks = [regex]::Matches($cleanCombos, '(?ms)^## (?!Контракт|Зафиксированная|Статическая)(.+?)\r?\n(.*?)(?=^## |\z)')
foreach ($comboMatch in $comboBlocks) {
    $comboName = $comboMatch.Groups[1].Value.Trim()
    $comboBody = $comboMatch.Groups[2].Value
    if ((Field $comboBody 'design_status') -ne 'approved') { continue }

    $slotBodies = @{}
    foreach ($slot in @('P', 'Q', 'E')) {
        $slotMatch = [regex]::Match($comboBody, "(?ms)^###\s+$slot(?:\s|:|—).*?(?=^###\s+(?:P|Q|E)(?:\s|:|—)|\z)")
        if (-not $slotMatch.Success) {
            $errors.Add("Approved combo '$comboName' misses ### $slot block")
            continue
        }
        $ability = $slotMatch.Value
        $slotBodies[$slot] = $ability
        foreach ($fieldName in $abilityFields) {
            $fieldMatches = [regex]::Matches($ability, "(?m)^\[$([regex]::Escape($fieldName))::")
            if ($fieldMatches.Count -ne 1) { $errors.Add("$comboName/$slot must contain exactly one [${fieldName}:: ...]") }
        }
        if ((Field $ability 'skill_slot') -ne $slot) { $errors.Add("$comboName/$slot has mismatched skill_slot") }
        foreach ($fieldName in $enumFields.Keys) {
            $value = Field $ability $fieldName
            if ($value -notin $enumFields[$fieldName]) { $errors.Add("$comboName/$slot has invalid $fieldName '$value'") }
        }

        $outputs = @((Field $ability 'output_properties') -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ -and $_ -ne 'none' })
        if ($outputs.Count -lt 1 -or $outputs.Count -gt 6 -or ($outputs | Sort-Object -Unique).Count -ne $outputs.Count) {
            $errors.Add("$comboName/$slot must declare 1-6 unique output_properties")
        }

        $properties = @()
        if ($slot -eq 'P') {
            foreach ($fieldName in @('passive_trigger', 'passive_state', 'passive_properties', 'passive_loss_rule')) {
                $value = Field $ability $fieldName
                if (-not $value -or $value -eq 'none') { $errors.Add("$comboName/P requires a concrete $fieldName") }
            }
            $properties = @((Field $ability 'passive_properties') -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
            if ($properties.Count -lt 1 -or $properties.Count -gt 3) {
                $errors.Add("$comboName/P must declare 1-3 passive_properties")
            }
            if ((($properties | Sort-Object) -join ';') -ne (($outputs | Sort-Object) -join ';')) {
                $errors.Add("$comboName/P passive_properties must equal output_properties")
            }
        } else {
            foreach ($fieldName in @('passive_trigger', 'passive_state', 'passive_properties', 'passive_loss_rule')) {
                if ((Field $ability $fieldName) -ne 'none') { $errors.Add("$comboName/$slot must keep $fieldName = none") }
            }
        }

        $components = Field $ability 'touch_components'
        if ($components) {
            $items = @($components -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ -and $_ -ne 'none' })
            if ($items.Count -lt 1 -or $items.Count -gt 3) {
                $errors.Add("$comboName/$slot must have 1-3 TOUCH components")
            }
            $seen = @{}
            $seenParameters = @{}
            $sum = 0.0
            foreach ($item in $items) {
                $component = [regex]::Match($item, '^(TRQ|GRP|LYR|GLW|SNS)\s*->\s*([A-Za-z0-9_.-]+)\s*@(0(?:\.\d+)?|1(?:\.0+)?)$')
                if (-not $component.Success) {
                    $errors.Add("Malformed TOUCH component in $comboName/${slot}: $item")
                    continue
                }
                $attr = $component.Groups[1].Value
                $parameter = $component.Groups[2].Value
                if ($parameter -notin $outputs) { $errors.Add("$comboName/$slot component '$parameter' is not declared in output_properties") }
                if ($slot -eq 'P' -and $parameter -notin $properties) {
                    $errors.Add("$comboName/P component '$parameter' is not declared in passive_properties")
                }
                if ($seen.ContainsKey($attr)) { $errors.Add("Duplicate $attr in $comboName/$slot") }
                if ($seenParameters.ContainsKey($parameter)) { $errors.Add("Duplicate parameter $parameter in $comboName/$slot") }
                $seen[$attr] = $true
                $seenParameters[$parameter] = $true
                if ($component.Groups[3].Success) {
                    $weight = [double]::Parse($component.Groups[3].Value, [Globalization.CultureInfo]::InvariantCulture)
                    if ($weight -le 0) { $errors.Add("TOUCH weight must be positive in $comboName/$slot") }
                    $sum += $weight
                }
            }
            if ($sum -gt 1.000001) { $errors.Add("TOUCH weights exceed 1 in $comboName/$slot") }
        }

        $edges = Field $ability 'downstream_edges'
        if ($edges -and $edges -ne 'none') {
            foreach ($edge in ($edges -split ';')) {
                if ($edge.Trim() -notmatch '^[A-Za-z0-9_.-]+\s*->\s*(?:P|Q|E|weapon|frame|device|status)\.[A-Za-z0-9_.-]+$') {
                    $errors.Add("Malformed downstream edge in $comboName/${slot}: $($edge.Trim())")
                }
            }
        }

        $carrier = Field $ability 'carrier_contract'
        $supply = Field $ability 'supply_contract'
        $fate = Field $ability 'carrier_fate'
        if ((Field $ability 'economic_output') -notin @('none', 'nonextractable')) {
            $errors.Add("$comboName/$slot cannot create an extractable economic output")
        }
        if ($carrier -eq 'consumable') {
            foreach ($f in @('carrier_ref', 'consume_amount', 'consumption_point', 'payload_family')) { Require-Concrete $ability $f "$comboName/$slot consumable" }
            if ($supply -ne 'item_charge' -or $fate -ne 'consumed') { $errors.Add("$comboName/$slot has invalid consumable tuple") }
            if ((Field $ability 'carrier_ref') -notin $consumableRefs) { $errors.Add("$comboName/$slot references unknown consumable") }
        }
        if ($carrier -eq 'current_frame') {
            foreach ($f in @('carrier_ref', 'required_interface', 'compatible_frames')) { Require-Concrete $ability $f "$comboName/$slot current_frame" }
            $needed = Field $ability 'required_interface'
            $compatible = Field $ability 'compatible_frames'
            if ((Field $ability 'carrier_ref') -ne 'equipped_frame') { $errors.Add("$comboName/$slot current_frame must use carrier_ref equipped_frame") }
            if ($supply -notin @('stamina', 'battery_impulse', 'item_charge') -or $fate -ne 'retained') { $errors.Add("$comboName/$slot has invalid current_frame tuple") }
            if ($compatible -eq 'any_with_interface') {
                if (-not @($weaponInterfaces.Keys | Where-Object { $weaponInterfaces[$_] -contains $needed }).Count) {
                    $errors.Add("$comboName/$slot has no Frame exposing interface '$needed'")
                }
            } elseif ($compatible -and $compatible -ne 'none') {
                foreach ($frameId in ($compatible -split ';' | ForEach-Object { $_.Trim() })) {
                    if (-not $weaponInterfaces.ContainsKey($frameId)) {
                        $errors.Add("$comboName/$slot references unknown Frame '$frameId'")
                    } elseif ($weaponInterfaces[$frameId] -notcontains $needed) {
                        $errors.Add("$comboName/$slot Frame '$frameId' lacks interface '$needed'")
                    }
                }
            }
        }
        if ($carrier -in @('device', 'consumable', 'environment_node')) {
            Require-Concrete $ability 'carrier_ref' "$comboName/$slot physical carrier"
        }
        if ($carrier -eq 'body' -and ($supply -notin @('stamina', 'biological_reserve', 'battery_impulse') -or $fate -ne 'retained')) {
            $errors.Add("$comboName/$slot has invalid body carrier tuple")
        }
        if ($carrier -eq 'body' -and $supply -eq 'stamina' -and ((Field $ability 'payload_family') -ne 'none' -or (Field $ability 'status_effect') -eq 'from_carrier' -or (Field $ability 'effect_persistence') -eq 'anchored')) {
            $errors.Add("$comboName/$slot body+stamina cannot create a material or anchored payload")
        }
        if ($carrier -eq 'environment_node') {
            foreach ($f in @('carrier_ref', 'required_interface', 'depletion_rule')) { Require-Concrete $ability $f "$comboName/$slot environment_node" }
            if ($supply -ne 'local_material') { $errors.Add("$comboName/$slot environment_node must use local_material") }
            if ($fate -notin @('retained', 'consumed')) { $errors.Add("$comboName/$slot has invalid environment_node fate") }
            if ((Field $ability 'carrier_ref') -notin $environmentRefs) { $errors.Add("$comboName/$slot references unknown environment node") }
            if ((Field $ability 'depletion_rule') -match '(?i)never|infinite|free') { $errors.Add("$comboName/$slot has a non-depleting local material rule") }
        }
        if ($carrier -eq 'body' -and $supply -eq 'biological_reserve') {
            foreach ($f in @('reserve_id', 'reserve_capacity', 'reserve_recovery', 'consume_amount', 'consumption_point', 'nonextractable')) { Require-Concrete $ability $f "$comboName/$slot biological reserve" }
            if ((Field $ability 'nonextractable') -ne 'true') { $errors.Add("$comboName/$slot biological reserve must be nonextractable") }
        }
        if ($carrier -eq 'device' -and $fate -eq 'deployed') {
            foreach ($f in @('carrier_ref', 'placement_limit', 'depletion_rule', 'retrieval_rule')) { Require-Concrete $ability $f "$comboName/$slot deployed device" }
        }
        if ($carrier -eq 'device') {
            if ($supply -notin @('device_charge', 'battery_impulse', 'item_charge') -or $fate -notin @('retained', 'deployed')) { $errors.Add("$comboName/$slot has invalid device tuple") }
            if ((Field $ability 'carrier_ref') -notin $deviceRefs) { $errors.Add("$comboName/$slot references unknown device") }
        }
        if ($supply -in @('device_charge', 'item_charge')) {
            foreach ($f in @('consume_amount', 'consumption_point', 'depletion_rule')) { Require-Concrete $ability $f "$comboName/$slot charge supply" }
        }
        if ($supply -eq 'battery_impulse') {
            if ((Field $ability 'impulse_cost') -notmatch '^[1-9][0-9]*$') { $errors.Add("$comboName/$slot battery_impulse requires positive impulse_cost") }
            if ((Field $ability 'casting_reserve_required') -ne 'true') { $errors.Add("$comboName/$slot battery_impulse requires casting_reserve_required true") }
        }
        $consumeAmount = Field $ability 'consume_amount'
        if ($consumeAmount -ne 'none') {
            $amountMatch = [regex]::Match($consumeAmount, '^([0-9]+(?:\.[0-9]+)?)\s+\S+')
            if (-not $amountMatch.Success -or [double]::Parse($amountMatch.Groups[1].Value, [Globalization.CultureInfo]::InvariantCulture) -le 0) { $errors.Add("$comboName/$slot consume_amount must be positive with a unit") }
        }
        foreach ($numericField in @('placement_limit', 'reserve_capacity')) {
            $numericValue = Field $ability $numericField
            if ($numericValue -ne 'none' -and ($numericValue -notmatch '^[1-9][0-9]*(?:\s+\S+)?$')) { $errors.Add("$comboName/$slot $numericField must be positive") }
        }
        if ((Field $ability 'impulse_cost') -notmatch '^[0-9]+$') { $errors.Add("$comboName/$slot impulse_cost must be a non-negative integer") }
        if ((Field $ability 'status_effect') -eq 'from_carrier') {
            foreach ($f in @('carrier_ref', 'payload_family')) { Require-Concrete $ability $f "$comboName/$slot status_from_carrier" }
        }
    }

    if ($slotBodies.Count -eq 3) {
        $graph = @{}
        $startsByTouch = @{}
        $nodeWeights = @{}
        $declaredNodes = @{}
        $edgeSources = @()
        $edgeTargets = @()
        foreach ($slot in @('P', 'Q', 'E')) {
            $ability = $slotBodies[$slot]
            foreach ($property in ((Field $ability 'output_properties') -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ -and $_ -ne 'none' })) {
                $declaredNodes["$slot.$property"] = $true
            }
            $components = Field $ability 'touch_components'
            foreach ($item in ($components -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ -and $_ -ne 'none' })) {
                $component = [regex]::Match($item, '^(TRQ|GRP|LYR|GLW|SNS)\s*->\s*([A-Za-z0-9_.-]+)\s*@(0(?:\.\d+)?|1(?:\.0+)?)$')
                if ($component.Success) {
                    $attr = $component.Groups[1].Value
                    $node = "$slot.$($component.Groups[2].Value)"
                    if (-not $startsByTouch.ContainsKey($attr)) { $startsByTouch[$attr] = @() }
                    $startsByTouch[$attr] += $node
                    $nodeWeights[$node] = [double]::Parse($component.Groups[3].Value, [Globalization.CultureInfo]::InvariantCulture)
                    $declaredNodes[$node] = $true
                }
            }
            $edges = Field $ability 'downstream_edges'
            if ($edges -and $edges -ne 'none') {
                foreach ($edgeText in ($edges -split ';')) {
                    $edge = [regex]::Match($edgeText.Trim(), '^([A-Za-z0-9_.-]+)\s*->\s*((?:P|Q|E|weapon|frame|device|status)\.[A-Za-z0-9_.-]+)$')
                    if ($edge.Success) {
                        $source = "$slot.$($edge.Groups[1].Value)"
                        $target = $edge.Groups[2].Value
                        if (-not $graph.ContainsKey($source)) { $graph[$source] = @() }
                        $graph[$source] += $target
                        $edgeSources += $source
                        $edgeTargets += $target
                    }
                }
            }
        }
        foreach ($source in ($edgeSources | Sort-Object -Unique)) {
            if (-not $declaredNodes.ContainsKey($source)) {
                $errors.Add("$comboName has downstream source '$source' not declared as a component, passive property or incoming target")
            }
        }
        foreach ($target in ($edgeTargets | Where-Object { $_ -match '^(P|Q|E)\.' } | Sort-Object -Unique)) {
            if (-not $declaredNodes.ContainsKey($target)) {
                $errors.Add("$comboName has downstream target '$target' absent from destination output_properties")
            }
        }
        foreach ($attr in $startsByTouch.Keys) {
            $queue = [System.Collections.Generic.Queue[string]]::new()
            $visited = @{}
            foreach ($node in $startsByTouch[$attr]) { $queue.Enqueue($node) }
            while ($queue.Count -gt 0) {
                $node = $queue.Dequeue()
                if ($visited.ContainsKey($node)) { continue }
                $visited[$node] = $true
                if ($graph.ContainsKey($node)) {
                    foreach ($next in $graph[$node]) { $queue.Enqueue($next) }
                }
            }
            $reachedSlots = @($visited.Keys | Where-Object { $_ -match '^(P|Q|E)\.' } | ForEach-Object { ($_ -split '\.')[0] } | Sort-Object -Unique)
            if ($reachedSlots.Count -eq 3) {
                $errors.Add("${comboName}: $attr reaches P, Q and E through direct/transitive downstream edges")
            }
        }
        foreach ($start in $nodeWeights.Keys) {
            $queue = [System.Collections.Generic.Queue[object]]::new()
            $queue.Enqueue([pscustomobject]@{ Node = $start; Sum = [double]$nodeWeights[$start]; Path = @($start) })
            while ($queue.Count -gt 0) {
                $state = $queue.Dequeue()
                if (-not $graph.ContainsKey($state.Node)) { continue }
                foreach ($next in $graph[$state.Node]) {
                    if ($state.Path -contains $next) {
                        $errors.Add("$comboName has a downstream cycle: $($state.Path -join ' -> ') -> $next")
                        continue
                    }
                    $nextSum = [double]$state.Sum
                    if ($nodeWeights.ContainsKey($next)) { $nextSum += [double]$nodeWeights[$next] }
                    if ($nextSum -gt 1.000001) {
                        $errors.Add("$comboName exceeds path envelope at $($state.Path -join ' -> ') -> $next (Σw=$nextSum)")
                        continue
                    }
                    $queue.Enqueue([pscustomobject]@{ Node = $next; Sum = $nextSum; Path = @($state.Path) + $next })
                }
            }
        }
        foreach ($start in $declaredNodes.Keys) {
            $queue = [System.Collections.Generic.Queue[object]]::new()
            $queue.Enqueue([pscustomobject]@{ Node = $start; Path = @($start) })
            while ($queue.Count -gt 0) {
                $state = $queue.Dequeue()
                if (-not $graph.ContainsKey($state.Node)) { continue }
                foreach ($next in $graph[$state.Node]) {
                    if ($state.Path -contains $next) {
                        $errors.Add("$comboName has a downstream cycle independent of scaling: $($state.Path -join ' -> ') -> $next")
                        continue
                    }
                    if ($next -match '^(P|Q|E)\.') {
                        $queue.Enqueue([pscustomobject]@{ Node = $next; Path = @($state.Path) + $next })
                    }
                }
            }
        }
        $pQueue = [System.Collections.Generic.Queue[string]]::new()
        $pVisited = @{}
        foreach ($node in ($declaredNodes.Keys | Where-Object { $_ -like 'P.*' })) { $pQueue.Enqueue($node) }
        while ($pQueue.Count -gt 0) {
            $node = $pQueue.Dequeue()
            if ($pVisited.ContainsKey($node)) { continue }
            $pVisited[$node] = $true
            if ($graph.ContainsKey($node)) { foreach ($next in $graph[$node]) { $pQueue.Enqueue($next) } }
        }
        $pReach = @($pVisited.Keys | ForEach-Object { ($_ -split '\.')[0] } | Sort-Object -Unique)
        if ('weapon' -in $pReach -and 'Q' -in $pReach -and 'E' -in $pReach) {
            $errors.Add("$comboName passive reaches weapon, Q and E in one graph")
        }
    }
}

$squirrelBlock = [regex]::Match($cleanCombos, '(?ms)^## Белка × Авангард.*?(?=^## |\z)').Value
if ($squirrelBlock -notmatch '\[design_status::\s*pending\s*\]') {
    $errors.Add('squirrel_assault must remain pending until a new component design passes review.')
}
if ($squirrelBlock -match '\[(substat_consumer|spark_rule)::') {
    $errors.Add('squirrel_assault still contains retired Inertial Charge data.')
}

if ($errors.Count -gt 0) {
    $errors | ForEach-Object { Write-Output "ERROR: $_" }
    exit 1
}

Write-Output "Skill-build contract OK: schema and migration clean; validator fixture exercised; canonical approved combos checked: $canonicalApprovedCount."
