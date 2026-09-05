# Obsidian workflow

The local Obsidian vault is the working surface. Use filesystem reads and edits directly. Preserve unrelated `.obsidian` settings and workspace state; these are valid application files, not canon violations. Use [editing.md](editing.md) for semantic changes.

General format skills come from [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills), installed outside the vault under `~/.codex/skills`. Load only the needed upstream SKILL.md: `obsidian-markdown` for properties/wikilinks/embeds, `obsidian-bases` for `.base`, `json-canvas` for derived visual maps. Eldrain skills describe design and authority; do not copy upstream instructions into them.

Installation checked 2026-09-05 against upstream commit `a1dc48e68138490d522c04cbf5822214c6eb1202`: Markdown, Bases, JSON Canvas and CLI installed. The running official CLI responded to `help` and identified `Eldrain` at `C:\Hobby\Eldrain`. It is absent from this shell's PATH but available at `C:\Users\Andrii\AppData\Local\Programs\Obsidian\Obsidian.com`; sandbox access to that application directory may need escalation. An access denial is not evidence that an application is absent. `defuddle` is optional external ingestion tooling, not part of GDD editing.

For native operations load `~/.codex/skills/obsidian-cli/SKILL.md`. Before every structural migration, ask the installed CLI for its current contract: `obsidian version`, `obsidian help`, `obsidian help rename`, `obsidian help move`. From that command inventory, request help for available backlink, unresolved-link, property, search and Base commands you will use. Do not rely on remembered syntax or invent missing commands. Explicitly target `vault=Eldrain` and exact `path=` where supported to avoid operating on another open vault or active note. For example, in this environment:

```powershell
& 'C:/Users/Andrii/AppData/Local/Programs/Obsidian/Obsidian.com' vault=Eldrain read path=00_Index.md
```

Do not change PATH or app settings just to invoke it. If the app is closed, IPC fails or access is unavailable, use the filesystem and state which native checks were unavailable. A future machine must rediscover the executable rather than assume this installation path.

Installed contract checked 2026-09-06: Obsidian 1.13.7 (installer 1.13.4). `rename path=<path> name=<name>` renames a file; `move path=<path> to=<path>` accepts a destination folder or path. Available checks include `backlinks path=<path> format=json`, `links path=<path>`, `unresolved verbose format=json`, `properties path=<path> format=json`, `property:read path=<path> name=<property>`, `search query=<text>` and `search:context query=<text>`. Bases support `bases` and `base:query path=<path> format=json`; `base:views` refers to the current Base and advertises no path selector. These are a verified snapshot, not a substitute for rediscovery.

Use quoted root-relative wikilinks for canonical note properties, preserve aliases and block IDs, and escape the alias pipe as `\|` in tables. Keep page properties flat: text, numbers, booleans, dates and lists of scalars/quoted links. Nested records belong in the existing registry/data format. Do not reinterpret an embed as inheritance.

## Native structural migration

When installed help confirms rename/move support, prefer native Obsidian CLI migration for Markdown notes over filesystem renames. This vault has `alwaysUpdateLinks: true` (verified in `.obsidian/app.json`); preserve the setting and check it before migration. Automatic internal-link updates do not guarantee repair of arbitrary strings. If native operations are unavailable, a filesystem fallback requires explicit consumer repair and the same validation; report the limitation.

Before the first broad structural rename in an authorized refactor, perform one reversible smoke test:

1. Choose a low-risk bounded note, check destination availability, and record current references/backlinks and unresolved-link baseline.
2. Rename or move it through the installed CLI using the confirmed contract.
3. Inspect links/backlinks at the destination and exact-search the old path and name, including non-link consumers.
4. Check unresolved links against the baseline and repair regressions. Preserve aliases, headings, block IDs and their consumers.
5. Restore the note if needed, validating the reverse operation too. Do not scale up a failed smoke test.

After a successful smoke test, use coherent batches: Obsidian rename/move -> exact old-path/name search -> repair non-link consumers -> regenerate projections/routes -> focused validation. This preflight defines the contract; it does not authorize note migration.

Hardcoded paths inside DataviewJS, scripts, query strings, Bases, Canvas/config, generated tooling and custom metadata text are structural dependencies. Native backlinks alone will not enumerate them. Use exact filesystem search, for example `rg -n --hidden -F -e 'old/path' -e 'Old_Name' --glob '!.git/**'`, across affected consumers; inspect remaining matches, including intentional history, and repair live references. Prefer internal links, stable IDs, explicit properties, bounded configuration or passed `dv.view()` input over repeated literal paths when practical. Preserve semantic references instead of knowledge of historical layout, without building a configuration framework for a few links. Compare destination meaning before retiring a source.

## Interactive derived views

DataviewJS is allowed and useful for interactive analytical/presentation views: relationship maps, matrices, derived comparisons, diagnostics and cross-system visualization. Show the canonical upstream sources in the view or its readable wrapper. Applying a formula does not authorize defining gameplay law inside the script. Preserve useful interactivity; Bases and Canvas are alternatives, not mandatory replacements.

When several notes use the same algorithm with different parameters, prefer a shared reusable Dataview view plus thin parameterized Markdown wrappers. Installed Dataview 0.5.68 has JavaScript enabled and implements `await dv.view(path, input)`, loading `<path>.js` or `<path>/view.js` (optionally `view.css`). This was verified in the local plugin implementation; confirm support again in a different environment. Keep shared code in an appropriate tooling-support location chosen during the refactor, not copied into each note.

Put design-meaningful parameters in explicit properties and pass them from `dv.current()` to the shared view; do not derive them only from filenames, folders, hardcoded paths or copied JS. Illustrative properties, not an existing note or prescribed location:

```yaml
type: view
view_kind: sector_difficulty
upstream_sources:
  - "[[Canonical_Source]]"
difficulty: 1
sector_ref: "[[Sector]]"
```

Filename sorting may reflect a real parameter (`01_Difficulty` for Difficulty 1) without becoming its sole data source. Inspect inputs, missing-source/empty-result states and rendered interactions after extracting shared logic. Do not apply this pattern to existing Port notes without an authorized migration. Authority distinctions are in [design-architecture.md](design-architecture.md); naming and duplicate classification are in [editing.md](editing.md).

## Bases and Canvas

For a Base, choose its source notes/registry properties, define filters, then view columns and optional derived formulas. Verify selected sources, missing properties and empty results. The Base stores no canonical rows, duplicated values or ownership declarations. Edits through the Base change source properties and must respect those owners. Canvas is a navigation/explanation artifact and never a canonical rule source.

[Routable_Owners.base](../../09_Project_Management/Routable_Owners.base) lists active routable pages in gameplay domains, reading their properties directly. Verify native results with `obsidian vault=Eldrain base:query path=09_Project_Management/Routable_Owners.base format=json` and compare paths with route metadata. `index_route: owner` establishes navigation membership, not canonical rule authority; a successful query verifies this routing surface only. The Base stores no copied canonical data.

When the app cannot be inspected, report filesystem/YAML/link checks separately from rendering. Do not claim a view has rendered just because the file parses.
