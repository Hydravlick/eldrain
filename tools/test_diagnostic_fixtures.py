"""Batch 7 corpus integrity; no combat simulation or balance verdicts."""
import copy
import re
import unittest
from pathlib import Path

from tools.check_overhaul_contracts import discover, published, validate_records
from tools.document_model import load_yaml, parse_frontmatter
from tools.vault_guard import fragment_exists, iter_wikilinks, link_parts, project_files, resolve_wikilink


ROOT = Path(__file__).resolve().parents[1]
DEFINITIONS = Path('05_Combat_Survival/Diagnostic_Fixtures')
SCENARIOS = ROOT / '09_Project_Management/Diagnostic_Fixtures/fixture_batch7.md'


class DiagnosticFixturesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_records, cls.discovery_errors = discover(ROOT)
        cls.records = [r for r in cls.all_records if r.path.parent == DEFINITIONS]
        cls.text = SCENARIOS.read_text(encoding='utf-8')
        blocks = [load_yaml(b) for b in re.findall(r'```yaml\s*\n(.*?)```', cls.text, re.S)]
        manifests = [b['fixture_manifest'] for b in blocks if 'fixture_manifest' in b]
        if len(manifests) != 1:
            raise AssertionError('Expected one fixture manifest')
        cls.manifest = manifests[0]

    def assert_fixture_tuple(self, data):
        self.assertEqual(data['status'], 'draft')
        self.assertEqual(data['publication_state'], 'diagnostic_fixture')
        self.assertIs(data['canonical_content'], False)
        self.assertFalse(published(data))
        self.assertNotIn('canonical_id', data)
        self.assertNotIn('owns', data)
        self.assertNotEqual(data.get('index_route'), 'owner')

    def assert_manifest_integrity(self, manifest):
        frames = {r.data['frame_id'] for r in self.records
                  if r.data['entity_kind'] == 'weapon_frame'}
        patterns = {r.data['pattern_id']: r.data for r in self.records
                    if r.data['entity_kind'] == 'weapon_pattern'}
        relations = manifest['frame_proficiencies']
        self.assertEqual({r['frame_id'] for r in relations}, frames)
        self.assertEqual(len(relations), len(frames))
        for relation in relations:
            self.assertEqual(set(relation), {'frame_id', 'proficiency'})
            self.assertIs(type(relation['proficiency']), int)
            self.assertIn(relation['proficiency'], range(1, 4))
        items = manifest['items']
        by_id = {item['item_id']: item for item in items}
        self.assertEqual(len(by_id), len(items))
        for item in items:
            definition = patterns[item['pattern_id']]
            if 'magazine_capacity' in definition:
                self.assertIs(type(item['magazine_current']), int)
                self.assertTrue(0 <= item['magazine_current'] <= definition['magazine_capacity'])
            else:
                self.assertNotIn('magazine_current', item)
        for loadout in manifest['loadouts']:
            used_hands, used_items = set(), set()
            for placement in loadout['placements']:
                item_id, hands = placement['item_ref'], placement['occupies']
                self.assertIn(item_id, by_id)
                self.assertNotIn(item_id, used_items)
                self.assertEqual(len(hands), len(set(hands)))
                self.assertTrue(set(hands) <= {1, 2})
                self.assertFalse(used_hands & set(hands))
                required = patterns[by_id[item_id]['pattern_id']]['hand_requirement']
                self.assertEqual(len(hands), {'1H': 1, '2H': 2}[required])
                used_items.add(item_id)
                used_hands.update(hands)
        cells = {b['item_id']: b for b in manifest['batteries']}
        self.assertEqual(len(cells), len(manifest['batteries']))
        self.assertFalse(set(cells) & set(by_id))
        immediate = [b for b in cells.values() if b['placement'] != 'Cargo']
        self.assertEqual(len(immediate), 1)
        self.assertGreater(len(cells) - len(immediate), len(immediate))
        self.assertTrue(all(b['battery_state'] == 'Full' for b in cells.values()))
        variants = manifest['access_variants']
        self.assertEqual([v['dedicated_positions'] for v in variants], [0, 1, 2])
        for variant in variants:
            moved = variant['move_from_cargo']
            self.assertEqual(len(moved), variant['dedicated_positions'])
            self.assertEqual(len(moved), len(set(moved)))
            self.assertTrue(set(moved) <= set(cells))
            self.assertTrue(all(cells[b]['placement'] == 'Cargo' for b in moved))

    def test_real_definitions_are_valid_and_unpublished(self):
        self.assertEqual(self.discovery_errors, [])
        self.assertEqual(len(self.records), 5)
        self.assertEqual(validate_records(self.all_records), [])
        for record in self.records:
            with self.subTest(path=record.path):
                self.assert_fixture_tuple(record.data)
                key = 'frame_id' if record.data['entity_kind'] == 'weapon_frame' else 'pattern_id'
                self.assertTrue(record.data[key].startswith('fixture_'))
                for operation in record.data.get('operation_ids', []):
                    self.assertTrue(operation.startswith('fixture_'))
        self.assert_fixture_tuple(parse_frontmatter(SCENARIOS))
        canonical = [r for r in self.all_records if published(r.data)]
        self.assertTrue(all(r.path.parent != DEFINITIONS for r in canonical))

    def test_fixture_cannot_silently_be_promoted_to_canonical(self):
        changed = copy.deepcopy(self.records[0].data)
        changed.update(status='active', publication_state='canonical', canonical_content=True)
        with self.assertRaises(AssertionError):
            self.assert_fixture_tuple(changed)

    def test_new_wikilinks_include_valid_heading_targets(self):
        corpus = set(project_files(ROOT))
        for source in [ROOT / r.path for r in self.records] + [SCENARIOS]:
            for target in iter_wikilinks(source.read_text(encoding='utf-8-sig')):
                with self.subTest(source=source, target=target):
                    resolved = resolve_wikilink(source, target, corpus)
                    self.assertIsNotNone(resolved)
                    self.assertTrue(fragment_exists(resolved, link_parts(target)[1]))

    def test_two_patterns_share_frame_and_contrast_has_another(self):
        patterns = {r.data['pattern_id']: r.data for r in self.records
                    if r.data['entity_kind'] == 'weapon_pattern'}
        self.assertEqual(patterns['fixture_tap']['frame_id'], patterns['fixture_drive']['frame_id'])
        self.assertNotEqual(patterns['fixture_tap']['frame_id'], patterns['fixture_hook']['frame_id'])
        self.assertEqual({p['hand_requirement'] for p in patterns.values()}, {'1H', '2H'})

    def test_schema_rejects_broken_parent_and_missing_operation_definition(self):
        for mutation in ('parent', 'operation'):
            records = copy.deepcopy(self.records)
            pattern = next(r for r in records if r.data['entity_kind'] == 'weapon_pattern')
            if mutation == 'parent':
                pattern.data['frame_id'] = 'fixture_missing_frame'
            else:
                pattern.body = re.sub(r'\[operation_id::[^\]]+\]', '', pattern.body, count=1)
            with self.subTest(mutation=mutation):
                self.assertTrue(validate_records(records))

    def test_manifest_references_and_physical_comparisons(self):
        self.assert_manifest_integrity(self.manifest)
        for field in ('fixture_id', 'pawn_id', 'ability_id', 'battery_version', 'cantrip_version'):
            self.assertTrue(self.manifest[field].startswith('fixture_'))
        for group, key in (('items', 'item_id'), ('batteries', 'item_id'),
                           ('loadouts', 'fixture_id'), ('access_variants', 'fixture_id')):
            identifiers = [row[key] for row in self.manifest[group]]
            self.assertEqual(len(identifiers), len(set(identifiers)))
            self.assertTrue(all(i.startswith('fixture_') for i in identifiers))
        cases = self.manifest['case_ids']
        self.assertEqual(len(cases), 7)
        self.assertEqual(len(cases), len(set(cases)))
        for case in cases:
            self.assertTrue(case.startswith('fixture_'))
            self.assertIn('\n## ' + case + '\n', self.text)
        operations = re.findall(r'\[operation_id::\s*([^\]]+)\]', self.text)
        self.assertCountEqual(operations, [self.manifest['battery_version'], self.manifest['cantrip_version']])

    def test_invalid_physical_snapshots_are_detected(self):
        for mutation in ('duplicate_item', 'overlapping_hands', 'double_move', 'move_ready', 'extra_ammo'):
            changed = copy.deepcopy(self.manifest)
            if mutation == 'duplicate_item':
                changed['items'].append(copy.deepcopy(changed['items'][0]))
            elif mutation == 'overlapping_hands':
                changed['loadouts'][2]['placements'][1]['occupies'] = [1]
            elif mutation == 'double_move':
                changed['access_variants'][2]['move_from_cargo'][1] = 'fixture_cell_cargo_a'
            elif mutation == 'move_ready':
                changed['access_variants'][1]['move_from_cargo'] = ['fixture_cell_ready']
            else:
                changed['items'][0]['magazine_current'] = 999
            with self.subTest(mutation=mutation), self.assertRaises(AssertionError):
                self.assert_manifest_integrity(changed)


if __name__ == '__main__':
    unittest.main()
