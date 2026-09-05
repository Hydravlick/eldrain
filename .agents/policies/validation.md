# Mechanical validation

[document-model.json](document-model.json) is the shared machine-readable source for document statuses, current corpus domains and feature/view/route fields. Its status descriptions are the documentation of lifecycle semantics. Status is separate from task checkboxes, risk workflow state, `design_status`, and `content_scope`: an active page may describe unfinished content or post-MVP scope.

Run from the vault root with Python 3.10+ and `PyYAML` installed from [tools/requirements.txt](../../tools/requirements.txt):

```powershell
python -m pip install -r tools/requirements.txt
python tools/vault_guard.py
python tools/build_routes.py --check
python tools/check_harness.py
python -m unittest discover -s tools -p "test_*.py"
```

Use the actual Python executable when `python`/`python3` is absent from PATH. In Codex Desktop, `load_workspace_dependencies` supplies the bundled runtime. Do not assume another machine's path.

`vault_guard` validates YAML syntax/duplicate keys, required gameplay metadata, supported status values, optional ownership declarations and duplicate active owner IDs/keys. It rejects gameplay ownership in management and other contextual material, checks declared feature contracts and derived Base structure, and resolves local links. Non-active documents remain valid but do not participate in active ownership or routes. Historical `owns` declarations can coexist with their active successor.

The View contract is opt-in through `type: view`, not inferred from names, folders or DataviewJS blocks. Active Markdown views require nonempty `upstream_sources`; when supplied at any status, this must be a list of quoted wikilinks to existing sources other than the view itself. Draft/non-active views may be incomplete. Views cannot declare `owns`/`canonical_id` at any status or serve as Feature `system_owners`; `index_route: owner` may still make a gameplay-domain View navigable without granting authority. The checker resolves sources, but does not certify their canonical authority, currency or completeness: historical diagnostics may intentionally cite retired sources. Review those meanings and visible provenance manually. No legacy relabeling, renderer migration or fixed document counts are required.

`build_routes --check` detects missing/stale projections and ensures active routable owners appear in their domain routes and root navigation. It uses the same YAML/status model. `--write` regenerates projections after authorized metadata or path changes; never hand-edit generated routes. The root/domain layout stays as it is until a placement change is authorized.

`check_harness` discovers actual SKILL.md files, validates metadata/UI invocation targets and local policy/reference links. It does not enforce skill count, prose length, headings or exact instructions. The test suite checks behavior using temporary vaults, not historical audit manifests or prompt phrases.

`vault_guard --strict` additionally checks heading/block fragments on Markdown links. It is a diagnostic for existing deep-link debt, not a filename allowlist. Normal validation checks file targets. Unknown headings introduced or moved by an edit must be reviewed even when strict checking is not part of the requested batch.

Bases are YAML view definitions with filters, formulas, properties and views; author records in source notes or registries. The checker rejects embedded ownership/record stores, missing view definitions and undefined formula references. It does not execute the Obsidian formula language, prove query results or detect disguised duplicated rules in a formula. Inspect changed views in Obsidian when available and manually verify source/empty-result behavior otherwise; state the rendering limitation.

DataviewJS is a supported derived surface, not a validation failure. The checker does not parse arbitrary JavaScript semantics or prove that native link updates repair string literals. Structural migrations must perform the exact old-path/name searches and non-link consumer checks in [obsidian-workflow.md](obsidian-workflow.md).

Focused batches can run relevant unit modules and the affected structural checks. Finish with the full commands above and inspect the diff. Passing mechanics is not proof of semantic conservation, design quality, causal truth or human prose: those require reading and evidence. Do not suppress failures or mark missing owners active to get a green check.
