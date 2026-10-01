import copy
import io
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import test_update_metadata
from data_use import metadata_for, ncbi_accession_for, snapshot_records
from ncbi_metadata import collect_ncbi
from snapshot_data_use import collect_snapshot, package_fingerprints, validate_snapshot
from update_dataset import compare_metadata

XML = b'''<GBSet><GBSeq><GBSeq_accession-version>AB123456.1</GBSeq_accession-version>
<GBSeq_update-date>28-SEP-2026</GBSeq_update-date><GBSeq_feature-table><GBFeature>
<GBFeature_key>source</GBFeature_key><GBFeature_quals>
<GBQualifier><GBQualifier_name>geo_loc_name</GBQualifier_name><GBQualifier_value>Brazil: Sao Paulo</GBQualifier_value></GBQualifier>
<GBQualifier><GBQualifier_name>collection_date</GBQualifier_name><GBQualifier_value>2022</GBQualifier_value></GBQualifier>
</GBFeature_quals></GBFeature></GBSeq_feature-table></GBSeq></GBSet>'''


class NcbiTests(unittest.TestCase):
    def test_exact_version_and_country(self):
        with patch('ncbi_metadata.urlopen', return_value=io.BytesIO(XML)):
            data = collect_ncbi({'AB123456.1'})
        row = data['data'][0]
        self.assertEqual(row['geoLocCountry'], 'Brazil')
        self.assertEqual(row['geoLocName'], 'Brazil: Sao Paulo')
        attrs = metadata_for('AB123456.1|2022', {row['accession']: row})
        self.assertEqual(attrs['INSDC_accession__url'], 'https://www.ncbi.nlm.nih.gov/nuccore/AB123456.1')
        self.assertNotIn('dataUseTerms', attrs)

    def test_wrong_version_and_api_errors_fail(self):
        for response in (XML.replace(b'AB123456.1', b'AB123456.2'), b'<ERROR>unavailable</ERROR>', b'bad xml'):
            with self.subTest(response=response), patch('ncbi_metadata.urlopen', return_value=io.BytesIO(response)):
                with self.assertRaises(ValueError):
                    collect_ncbi({'AB123456.1'})

    def test_ignored_identifiers(self):
        for name in ('EPI_ISL_123|2022', 'EHIE21409Y22|2022', 'PP_123ABC|2022',
                     'PP_0058227', 'PP_0058227|2022', 'PP_0058227.1|2022'):
            self.assertIsNone(ncbi_accession_for(name))

    def test_ncbi_and_refseq_accessions_remain_recognized(self):
        for accession in ('OK040058.1', 'NC_001477.1'):
            self.assertEqual(ncbi_accession_for(accession + '|2022'), accession)

    def test_empty_set_does_not_contact_ncbi(self):
        with patch('ncbi_metadata.urlopen') as request:
            self.assertEqual(collect_ncbi(set())['data'], [])
        request.assert_not_called()

    def test_collection_validation_and_diff(self):
        fixture = test_update_metadata.MetadataUpdateTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        (fixture.package / 'DENV4_representatives.fasta').write_text('>PP_TEST|2026\nN\n>AB123456.1|2022\nN\n')
        payload = {'info': {'dataVersion': '2'}, 'data': [dict(fixture.record, insdcAccessionFull='AB999999.1')]}
        with patch('snapshot_data_use.urlopen', return_value=io.BytesIO(json.dumps(payload).encode())), \
             patch('ncbi_metadata.urlopen', return_value=io.BytesIO(XML)):
            snapshot = collect_snapshot(fixture.package)
        attrs = metadata_for('PP_TEST|2026', snapshot_records(snapshot))
        self.assertEqual(attrs['INSDC_accession'], 'AB999999.1')
        self.assertEqual(attrs['restrictedUntil'], '2027-01-01')
        self.assertEqual(attrs['dataUseTerms__url'], fixture.record['dataUseTermsUrl'])
        changed = copy.deepcopy(snapshot)
        changed['ncbi']['data'][0]['geoLocCountry'] = 'Peru'
        self.assertIn('geoLocCountry', {c['field'] for c in compare_metadata(snapshot, changed)['changes']})
        snapshot['ncbi']['data'] = []
        with self.assertRaisesRegex(ValueError, 'NCBI accessions absent'):
            validate_snapshot(snapshot, fixture.package)


class AugurLinksTests(unittest.TestCase):
    def test_export_native_tooltip_links_for_all_configs(self):
        import csv
        import sys
        from data_use import COLUMNS, index_records
        root = Path(__file__).resolve().parents[1]
        row = dict(accession='PP_TEST', geoLocCountry='Brazil', dataUseTerms='RESTRICTED',
                   dataUseTermsRestrictedUntil='2027-01-01', insdcAccessionFull='AB123456.1',
                   dataUseTermsUrl='https://pathoplexus.org/about/terms-of-use/restricted-data')
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            (temp / 'tree.nwk').write_text('(PP_TEST:0.1,OTHER:0.2)ROOT;')
            (temp / 'nodes.json').write_text(json.dumps({'nodes': {
                'ROOT': {'branch_length': 0}, 'PP_TEST': {'branch_length': 0.1},
                'OTHER': {'branch_length': 0.2}}}))
            with (temp / 'metadata.tsv').open('w') as handle:
                writer = csv.DictWriter(handle, fieldnames=['strain', *COLUMNS], delimiter='\t')
                writer.writeheader()
                writer.writerow(dict(strain='PP_TEST', **metadata_for('PP_TEST', index_records([row]))))
                writer.writerow(dict(strain='OTHER'))
            for n in range(1, 5):
                result = subprocess.run([str(Path(sys.executable).with_name('augur')), 'export', 'v2',
                    '--tree', str(temp / 'tree.nwk'), '--metadata', str(temp / 'metadata.tsv'),
                    '--node-data', str(temp / 'nodes.json'),
                    '--auspice-config', str(root / f'config/auspice_config_d{n}.json'),
                    '--output', str(temp / 'tree.json')], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                tree = json.loads((temp / 'tree.json').read_text())
                attrs = tree['tree']['children'][0]['node_attrs']
                self.assertEqual(attrs['PPX_accession'], {'value': 'PP_TEST', 'url': 'https://pathoplexus.org/seq/PP_TEST'})
                self.assertEqual(attrs['INSDC_accession']['url'], 'https://www.ncbi.nlm.nih.gov/nuccore/AB123456.1')
                self.assertEqual(attrs['dataUseTerms']['url'], row['dataUseTermsUrl'])
                self.assertEqual(attrs['restrictedUntil']['value'], '2027-01-01')
                self.assertIn('dataUseTerms', {c['key'] for c in tree['meta']['colorings']})
