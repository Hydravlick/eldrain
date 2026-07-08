# Synergy Map: three readable modes

## Goal

Turn `00_Synergy_Map` into two complementary views of the same calculated data:

- a compact FR-style radial map for reading meaningful relationships;
- a 9x9 effectiveness matrix for inspecting the complete directional calculation.

The canonical `paradoxRules`, registries, and `00_Balance` logic are not changed.

## Relation modes

The interface has one mutually exclusive segmented control with three modes:

1. **Контрпики**
   - A pair is shown when its directional counter scores are not equal.
   - The stronger side is the counterpick; equal scores remain available in the matrix but do not create a radial line.
   - On label hover, outgoing counterpick lines use `#f7768e`; incoming lines use `#7aa2f7`.
   - If a pair has facts in both directions, the hover layer uses two slightly separated lanes so neither color hides the other.

2. **Сильная поддержка**
   - A directed support relation is shown only when it covers at least two of the target profile's common weaknesses.
   - With the current 3x3 data this reduces support from 52 directed facts to 6 strong relations.
   - The mode uses the existing support green `#48c78e`.

3. **Общая слабость**
   - One undirected line is shown when two profiles share at least one calculated common weakness.
   - Shared weakness remains derived from the intersection of Race and Practice `weak_to` values.
   - The mode uses `#e0af68` and a restrained dashed stroke.

No shared-vector or arsenal controls remain in the radial map. Their raw data may remain in the calculation layer for future use, but they are not part of this interface.

## Radial map

- Match FR's stable `500x500` canvas and visual scale.
- Remove all node dots. Labels are the interactive nodes.
- Keep labels inside the SVG viewBox and use the same readable 11px interface typography as FR.
- Label hover highlights the selected profile and related labels, dims unrelated labels, and shows only the active mode's relationships.
- Mouseout always restores the current mode through `renderBaseState()`.

### Angular layout

Angles are derived from the actual ordered profiles rather than fixed 30/60 degree increments.

- Adjacent profiles of the same race use gap weight `1`.
- A transition between races uses gap weight `1.75`.
- One angular unit is `360 / sum(all gap weights)`.
- Every profile angle is accumulated from the preceding weighted gap.

This keeps same-race combinations closer while distributing any future number of races and practices around the full circle.

## Effectiveness matrix

Two top-level tabs switch between **Карта** and **Матрица** without rebuilding the parsed data.

- Rows are the acting/source profiles; columns are target profiles.
- The diagonal is neutral and non-interactive.
- The same three relation modes control matrix cell meaning.
- Counter cells show the directional counter score `0-3`; support cells show covered common weaknesses `0-3`; shared-weakness cells show the number of shared weaknesses.
- Color intensity communicates magnitude. Hovering or focusing a cell shows the exact reasons in the information panel.
- Row and column headers highlight together so a cell can be traced without losing context.

## Information panel

The lower panel is contextual, not a second legend.

- Resting state: active mode and visible pair count, for example `Сильная поддержка · 6 связей`.
- Label hover: profile name, outgoing count, incoming count, and concise grouped relationships.
- Line or matrix-cell hover: source, target, direction, score, and reasons.
- Mouseout returns to the active mode summary.
- Repeated relation headings and instructional filler are removed.

## State and rendering

- `activeMode` is a single value: `counter`, `support`, or `shared_weakness`.
- Raw directed facts are calculated once and remain immutable during rendering.
- Derived radial links and matrix cells are produced by pure helper functions.
- `renderBaseState()` is the sole owner of resting opacity, stroke, label emphasis, selected control state, and panel summary.
- Hover handlers only apply temporary emphasis; reset delegates to `renderBaseState()`.

## Verification

- Automated checks cover weighted angle distribution, counter direction classification, strong-support threshold, shared-weakness aggregation, and matrix values.
- Syntax of the DataviewJS block is validated as an async function.
- Obsidian verification checks console errors, both tabs, all three modes, label hover, matrix-cell hover, and text containment at desktop and narrow widths.
