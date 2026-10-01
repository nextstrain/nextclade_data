import copy
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from snapshot_data_use import collect_snapshot, package_fingerprints, validate_snapshot
from update_dataset import checked_run_snapshot, compare_metadata, main, prepare_run


class MetadataUpdateTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.package = self.root / 'package'
        self.package.mkdir()
        for n in range(1, 5):
            for kind in ('representatives', 'test_set'):
                (self.package / f'DENV{n}_{kind}.fasta').write_text('>PP_TEST|2026\nN\n')
        self.record = {'accession': 'PP_TEST', 'geoLocCountry': 'Brazil',
                       'dataUseTerms': 'RESTRICTED', 'dataUseTermsRestrictedUntil': '2027-01-01',
                       'dataUseTermsUrl': 'https://pathoplexus.org/about/terms-of-use/restricted-data'}
        self.snapshot = {'retrievedAt': '2026-09-28T00:00:00+00:00',
                         'info': {'dataVersion': '1'},
                         'inputSha256': package_fingerprints(self.package), 'data': [self.record]}
        self.baseline = self.root / 'baseline.json'
        self.baseline.write_text(json.dumps(self.snapshot))
        self.config = {'input_package': str(self.package),
                       'metadata_runs_dir': str(self.root / 'runs'),
                       'data_use_snapshot': str(self.baseline)}

    def test_collection_requests_latest_and_keeps_api_provenance(self):
        payload = {'data': [self.record], 'info': {'dataVersion': '2'}}
        with patch('snapshot_data_use.urlopen', return_value=io.BytesIO(json.dumps(payload).encode())) as request:
            result = collect_snapshot(self.package)
        self.assertIn('versionStatus=LATEST_VERSION', request.call_args.args[0])
        self.assertEqual(result['info']['dataVersion'], '2')
        self.assertEqual(result['inputSha256'], self.snapshot['inputSha256'])

    def test_absent_accession_stops_collection(self):
        payload = {'data': [], 'info': {'dataVersion': '2'}}
        with patch('snapshot_data_use.urlopen', return_value=io.BytesIO(json.dumps(payload).encode())):
            with self.assertRaisesRegex(ValueError, 'Accessions absent'):
                collect_snapshot(self.package)

    def test_changed_package_cannot_replay(self):
        (self.package / 'DENV1_test_set.fasta').write_text('>PP_TEST|2026\nNN\n')
        with self.assertRaisesRegex(ValueError, 'does not match'):
            validate_snapshot(self.snapshot, self.package)

    def test_diff_includes_release_country_and_accession_changes(self):
        current = copy.deepcopy(self.snapshot)
        current['info']['dataVersion'] = '2'
        current['data'][0].update(dataUseTerms='OPEN', dataUseTermsRestrictedUntil=None, geoLocCountry='Peru')
        current['data'].append(dict(self.record, accession='PP_NEW'))
        previous = copy.deepcopy(self.snapshot)
        previous['data'].append(dict(self.record, accession='PP_OLD'))
        report = compare_metadata(previous, current)
        self.assertEqual(report['added'], ['PP_NEW'])
        self.assertEqual(report['removed'], ['PP_OLD'])
        terms = next(change for change in report['changes'] if change['field'] == 'dataUseTerms')
        self.assertEqual((terms['before'], terms['after']), ('RESTRICTED', 'OPEN'))
        self.assertIn('geoLocCountry', {change['field'] for change in report['changes']})

    def test_replay_is_offline_and_preserves_source(self):
        original = self.baseline.read_bytes()
        with patch('update_dataset.collect_snapshot', side_effect=AssertionError('Replay used network')):
            manifest = prepare_run(self.config, replay=self.baseline)
        frozen = Path(checked_run_snapshot(manifest, self.package))
        self.assertEqual(json.loads(frozen.read_text()), self.snapshot)
        self.assertEqual(self.baseline.read_bytes(), original)
        self.assertEqual(json.loads(manifest.read_text())['mode'], 'replay')

    def test_snapshot_change_after_preparation_is_rejected(self):
        manifest = prepare_run(self.config, replay=self.baseline)
        frozen = Path(json.loads(manifest.read_text())['snapshot'])
        frozen.write_text('{}')
        with self.assertRaisesRegex(ValueError, 'modified'):
            checked_run_snapshot(manifest, self.package)

    def test_next_refresh_compares_with_previous_refresh(self):
        first = copy.deepcopy(self.snapshot)
        first['info']['dataVersion'] = '2'
        second = copy.deepcopy(self.snapshot)
        second['info']['dataVersion'] = '3'
        with patch('update_dataset.collect_snapshot', side_effect=[first, second]):
            prepare_run(self.config)
            manifest = prepare_run(self.config)
        report = json.loads(Path(json.loads(manifest.read_text())['changes']).read_text())
        self.assertEqual(report['previousDataVersion'], '2')
        self.assertEqual(report['currentDataVersion'], '3')

    def test_network_failure_never_starts_pipeline(self):
        config_path = self.root / 'config.yaml'
        config_path.write_text(yaml.safe_dump(self.config))
        with patch.object(sys, 'argv', ['update_dataset.py', '--configfile', str(config_path)]), \
             patch('update_dataset.collect_snapshot', side_effect=OSError('API unavailable')), \
             patch('update_dataset.subprocess.run') as run:
            self.assertEqual(main(), 1)
        run.assert_not_called()
        self.assertFalse((self.root / 'runs').exists())


if __name__ == '__main__':
    unittest.main()
