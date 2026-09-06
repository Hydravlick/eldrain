from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.document_model import MODEL, MetadataError, parse_frontmatter
from tools.vault_guard import (check_bases, check_features, check_frontmatter, check_index,
                               check_links, check_owners, check_surface, check_views,
                               project_files, resolve_wikilink, run)


class VaultGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, text=""):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def page(self, name="Rule", fields="", body=""):
        return self.write("01_Core_Vision/" + name + ".md",
                          "---\ntype: system\nstatus: active\nsystem: test\n" + fields + "---\n" + body)

    def codes(self, function):
        return {v.code for v in function(self.root)}

    def owner(self, name="Rule", extra=""):
        return self.page(name, 'index_route: owner\nindex_group: test\nindex_order: 0\n'
                         'index_summary: "Rule: behavior."\nread_when: When changing behavior.\n' + extra)

    def test_real_yaml_supports_block_lists_quotes_and_bom(self):
        path = self.write("sample.md", '\ufeff---\naliases:\n  - "One, two"\n  - Three\nflag: true\norder: 0\n---\n')
        self.assertEqual(parse_frontmatter(path), {"aliases": ["One, two", "Three"], "flag": True, "order": 0})

    def test_duplicate_yaml_keys_and_unclosed_frontmatter_rejected(self):
        for text in ("---\nstatus: active\nstatus: draft\n---\n", "---\nstatus: active\n"):
            path = self.write("sample.md", text)
            with self.assertRaises(MetadataError):
                parse_frontmatter(path)

    def test_yaml_errors_are_diagnostics_not_tracebacks(self):
        self.write("01_Core_Vision/Bad.md", "---\nstatus: [\n---\n")
        self.assertIn("INVALID_YAML", self.codes(check_frontmatter))

    def test_all_document_statuses_are_accepted_without_granting_authority(self):
        for status in MODEL["statuses"]:
            self.write(f"01_Core_Vision/{status}.md", f"---\ntype: system\nsystem: test\nstatus: {status}\n---\n")
        self.assertEqual(check_frontmatter(self.root), [])

    def test_invalid_status_type_and_value_are_reported(self):
        for status in ("in_progress", "[active]"):
            self.write("01_Core_Vision/Bad.md", f"---\ntype: system\nsystem: test\nstatus: {status}\n---\n")
            self.assertIn("INVALID_STATUS", self.codes(check_frontmatter))

    def test_missing_metadata_and_nested_properties_are_reported(self):
        self.write("01_Core_Vision/Missing.md", "# Missing")
        self.page(fields="record:\n  cost: 10\n")
        self.assertTrue({"MISSING_METADATA", "NONFLAT_PROPERTY"} <= self.codes(check_frontmatter))

    def test_valid_yaml_needs_no_arbitrary_quote_rule(self):
        self.owner()
        self.assertEqual(check_frontmatter(self.root), [])

    def test_route_order_must_be_integer_not_boolean(self):
        self.page(fields="index_route: owner\nindex_order: true\n")
        self.assertIn("INVALID_ROUTE_METADATA", self.codes(check_frontmatter))

    def test_owns_requires_id_and_active_owner_route(self):
        self.page(fields="owns: [rule.one]\n")
        self.assertIn("OWNER_MISSING_CANONICAL_ID", self.codes(check_frontmatter))
        self.page(fields="canonical_id: rule\n")
        self.assertIn("OWNER_NOT_ROUTABLE", self.codes(check_frontmatter))

    def test_duplicate_rule_and_owner_ids_reported(self):
        for name in ("A", "B"):
            self.owner(name, "canonical_id: shared\nowns:\n  - shared.rule\n")
        self.assertTrue({"DUPLICATE_OWNS", "DUPLICATE_CANONICAL_ID"} <= self.codes(check_owners))

    def test_historical_owner_does_not_conflict_with_successor(self):
        self.owner(extra="canonical_id: shared\nowns: [shared.rule]\n")
        self.write("01_Core_Vision/Old.md", "---\ntype: system\nsystem: test\nstatus: deprecated\ncanonical_id: shared\nowns: [shared.rule]\n---\n")
        self.assertEqual(check_owners(self.root), [])

    def test_management_cannot_be_gameplay_owner(self):
        self.write("09_Project_Management/Rule.md", "---\ntype: system\nstatus: active\n---\n")
        self.assertIn("OWNERSHIP_OUTSIDE_GAMEPLAY", self.codes(check_owners))

    def test_reference_cannot_declare_active_rule_ownership(self):
        self.write("10_Reference/Rule.md", "---\nstatus: active\ncanonical_id: shared\n---\n")
        self.assertIn("OWNERSHIP_OUTSIDE_GAMEPLAY", self.codes(check_owners))

    def test_indexes_reject_nonactive_targets_in_root_and_domain(self):
        self.write("00_Index.md", "[[01_Core_Vision/Old]]")
        self.write("01_Core_Vision/00_Routes.md", "[[01_Core_Vision/Old]]")
        self.write("01_Core_Vision/Old.md", "---\nstatus: deferred\n---\n")
        self.assertEqual(len(check_index(self.root)), 2)

    def test_observes_actual_wikilinks_not_literal_examples(self):
        self.page(body='```markdown\n[[MissingExample]]\n```\n`[[MissingInline]]`\n[[MissingReal]]')
        result = check_links(self.root)
        self.assertEqual([v.detail for v in result], ["MissingReal"])

    def test_root_relative_alias_heading_embed_and_self_link(self):
        source = self.page(body="# Heading\n^block\n[[#Heading]] [[#^block]]\n![[image.png|300]]\n[[01_Core_Vision/Target#Rule\\|Shown]]")
        target = self.page("Target", body="# Rule")
        self.write("image.png")
        self.assertEqual(resolve_wikilink(source, "01_Core_Vision/Target#Rule|Shown", set(project_files(self.root))), target)
        self.assertEqual(check_links(self.root, strict=True), [])

    def test_basename_ambiguity_does_not_choose_random_owner(self):
        source = self.write("Source.md")
        self.write("A/Target.md")
        self.write("B/Target.md")
        self.assertIsNone(resolve_wikilink(source, "Target", set(project_files(self.root))))

    def test_alias_resolves_but_duplicate_alias_does_not(self):
        source = self.write("Source.md")
        target = self.page(fields="aliases: [Other]\n")
        self.assertEqual(resolve_wikilink(source, "Other", set(project_files(self.root))), target)
        self.page("Second", fields="aliases: [Other]\n")
        self.assertIsNone(resolve_wikilink(source, "Other", set(project_files(self.root))))

    def test_relative_corpus_resolution(self):
        source, target = Path("A/Source.md"), Path("A/Target.md")
        self.assertEqual(resolve_wikilink(source, "A/Target", {source, target}), target)

    def test_markdown_links_with_spaces_and_percent_encoding(self):
        self.write("A/File Name.md", "# Title")
        self.write("A/Source.md", "[Name](<File Name.md#Title>) [Name](File%20Name.md) [Web](https://example.com)")
        self.assertEqual(check_links(self.root, strict=True), [])

    def test_missing_fragment_is_optional_diagnostic(self):
        self.page(body="[[#Missing]]")
        self.assertEqual(check_links(self.root), [])
        self.assertIn("MISSING_LINK_FRAGMENT", {v.code for v in check_links(self.root, strict=True)})

    def test_markdown_image_target_is_checked(self):
        self.page(body="![Missing asset](missing.png)")
        self.assertIn("MISSING_LINK_TARGET", self.codes(check_links))

    def test_application_state_and_new_management_names_are_allowed(self):
        self.write(".obsidian/workspace.json", "{}")
        self.write(".git/hidden.md", "[[Missing]]")
        self.write("09_Project_Management/New.md", "---\ntype: project_plan\nstatus: active\n---\n- [x] Done")
        self.write("10_Reference/Reference.md", "# Reference")
        self.assertEqual(check_surface(self.root, strict=True), [])
        self.assertEqual(check_links(self.root), [])
        self.assertNotIn(self.root / ".git/hidden.md", project_files(self.root))

    def feature(self, fields="feature_id: test\nsystem_owners:\n  - '[[01_Core_Vision/Rule]]'\n", status="active", name="Feature"):
        return self.write(f"01_Core_Vision/{name}.md", f"---\ntype: feature\nsystem: test\nstatus: {status}\n" + fields + "---\n")

    def test_feature_contract_without_choosing_feature_folder(self):
        self.owner()
        self.feature()
        self.assertEqual(check_features(self.root), [])
        self.assertEqual(check_frontmatter(self.root), [])
        self.assertEqual(check_owners(self.root), [])

    def test_feature_requires_id_and_system_dependencies(self):
        self.feature("")
        self.assertEqual({v.detail for v in check_features(self.root)}, {"feature_id", "system_owners"})

    def test_deferred_feature_may_be_incomplete(self):
        self.feature("", status="deferred")
        self.assertEqual(check_features(self.root), [])

    def test_feature_cannot_own_lower_level_rules(self):
        self.feature("feature_id: test\ncanonical_id: duplicate\nowns: [rule.one]\n")
        self.assertIn("FEATURE_RULE_OWNERSHIP", self.codes(check_owners))

    def test_feature_rejects_lore_nonactive_and_management_dependencies(self):
        for target in ("01_Core_Vision/Lore", "01_Core_Vision/Old", "09_Project_Management/Rule"):
            self.write(target + ".md", "---\ntype: lore\nstatus: active\nindex_route: owner\n---\n")
            self.feature(f"feature_id: test\nsystem_owners: ['[[{target}]]']\n")
            self.assertIn("FEATURE_INVALID_SYSTEM_OWNER", self.codes(check_features))
        self.write("01_Core_Vision/Old.md", "---\ntype: system\nstatus: deprecated\nindex_route: owner\n---\n")
        self.feature("feature_id: test\nsystem_owners: ['[[01_Core_Vision/Old]]']\n")
        self.assertIn("FEATURE_INVALID_SYSTEM_OWNER", self.codes(check_features))

    def test_feature_missing_and_malformed_links(self):
        self.feature("feature_id: test\nsystem_owners: ['[[Missing]]']\n")
        self.assertIn("FEATURE_MISSING_TARGET", self.codes(check_features))
        self.feature("feature_id: test\nsystem_owners: Rule\n")
        self.assertIn("FEATURE_INVALID_LINK_LIST", self.codes(check_features))

    def test_duplicate_active_feature_identity_rejected(self):
        self.owner()
        self.feature()
        self.feature(name="Second")
        self.assertIn("DUPLICATE_FEATURE_ID", self.codes(check_owners))

    def view(self, fields="upstream_sources: ['[[01_Core_Vision/Rule]]']\n", status="active",
             location="01_Core_Vision/Analysis.md"):
        return self.write(location, f"---\ntype: view\nsystem: test\nstatus: {status}\n" + fields + "---\n")

    def test_view_accepts_explicit_sources_and_semantic_parameters(self):
        self.page()
        self.view("upstream_sources: ['[[01_Core_Vision/Rule]]']\nview_kind: sector_difficulty\n"
                  "difficulty: 1\nsector_ref: '[[01_Core_Vision/Rule]]'\n")
        self.assertEqual(run(self.root), [])
        self.assertNotIn("view", MODEL["system_types"])

    def test_active_view_requires_sources_but_draft_may_be_incomplete(self):
        self.view("")
        self.assertIn("VIEW_MISSING_SOURCES", self.codes(run))
        self.view("", status="draft")
        self.assertEqual(check_views(self.root), [])

    def test_view_rejects_malformed_source_lists(self):
        for value in ("Rule", "[Rule]", "[1]", "{source: Rule}"):
            with self.subTest(value=value):
                self.view(f"upstream_sources: {value}\n")
                self.assertIn("VIEW_INVALID_SOURCES", self.codes(check_views))

    def test_view_rejects_missing_and_self_sources(self):
        self.view("upstream_sources: ['[[Missing]]']\n")
        self.assertIn("VIEW_MISSING_TARGET", self.codes(check_views))
        self.view("upstream_sources: ['[[01_Core_Vision/Analysis]]']\n")
        self.assertIn("VIEW_SELF_SOURCE", self.codes(check_views))

    def test_view_cannot_declare_authority_at_any_status_or_location(self):
        for status in MODEL["statuses"]:
            for field in ("owns: [rule.one]", "canonical_id: rule"):
                with self.subTest(status=status, field=field):
                    self.view(field + "\n", status=status)
                    self.assertIn("VIEW_RULE_OWNERSHIP", self.codes(run))
        self.view("owns: [rule.one]\n", location="09_Project_Management/Analysis.md")
        self.assertIn("VIEW_RULE_OWNERSHIP", self.codes(check_views))

    def test_management_view_may_read_gameplay_without_owning_it(self):
        self.page()
        self.view(location="09_Project_Management/Analysis.md")
        self.assertEqual(run(self.root), [])

    def test_view_cannot_enter_owner_routes_at_any_status(self):
        self.page()
        for status in MODEL["statuses"]:
            with self.subTest(status=status):
                self.view("upstream_sources: ['[[01_Core_Vision/Rule]]']\nindex_route: owner\n"
                          "index_group: test\nindex_order: 1\nindex_summary: Analysis\nread_when: Compare rules\n",
                          status=status)
                self.assertEqual(self.codes(run), {"VIEW_ROUTE_OWNERSHIP"})

    def test_view_is_not_a_feature_system_owner_even_with_route_metadata(self):
        self.page()
        self.feature("feature_id: test\nsystem_owners: ['[[01_Core_Vision/Analysis]]']\n")
        for route in ("", "index_route: owner\n"):
            with self.subTest(route=route):
                self.view("upstream_sources: ['[[01_Core_Vision/Rule]]']\n" + route)
                self.assertIn("FEATURE_INVALID_SYSTEM_OWNER", self.codes(check_features))

    def test_view_source_check_does_not_infer_authority_from_metadata(self):
        self.write("01_Core_Vision/History.md", "---\ntype: lore\nsystem: test\nstatus: deprecated\n---\n")
        self.view("upstream_sources: ['[[01_Core_Vision/History]]']\n")
        self.assertEqual(run(self.root), [])

    def test_representation_name_does_not_reclassify_legacy_owner(self):
        self.owner("Matrix", "canonical_id: topology\nowns: [world.topology]\n")
        self.assertEqual(run(self.root), [])

    def base(self, extra=""):
        return self.write("Views/Owners.base", 'filters: \'status == "active"\'\nviews:\n  - type: table\n    name: Owners\n    order: [file.name, status]\n' + extra)

    def test_derived_base_is_valid(self):
        self.base()
        self.assertEqual(check_bases(self.root), [])

    def test_base_cannot_store_records_or_ownership(self):
        for extra in ("records: [{id: a}]\n", "owns: [shared.rule]\n"):
            self.base(extra)
            self.assertIn("BASE_NONVIEW_DATA", self.codes(check_bases))

    def test_base_undefined_formula_detected(self):
        self.base('properties:\n  formula.missing:\n    displayName: Missing\n')
        self.assertIn("BASE_UNDEFINED_FORMULA", self.codes(check_bases))

    def test_base_named_formula_and_recursive_filters_work(self):
        self.write("View.base", 'filters:\n  and:\n    - \'status == "active"\'\n    - not: [\'file.hasTag("archive")\']\nformulas:\n  title: file.name\nviews:\n  - type: table\n    name: Test\n    order: [formula.title]\n')
        self.assertEqual(check_bases(self.root), [])

    def test_base_requires_filtered_named_views(self):
        self.write("View.base", "views: []\n")
        self.assertTrue({"BASE_INVALID_VIEWS", "BASE_INVALID_FILTERS"} <= self.codes(check_bases))

    def test_base_yaml_duplicate_key_rejected(self):
        self.write("View.base", "views: []\nviews: []\n")
        self.assertIn("INVALID_BASE_YAML", self.codes(check_bases))


if __name__ == "__main__":
    unittest.main()
