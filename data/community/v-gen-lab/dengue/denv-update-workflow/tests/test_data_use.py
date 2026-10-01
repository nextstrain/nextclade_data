import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from data_use import index_records, metadata_for


class TermsTests(unittest.TestCase):
    def setUp(self):
        self.row = dict(accession='PP_TEST', geoLocCountry='Brazil', dataUseTerms='RESTRICTED',
                        dataUseTermsRestrictedUntil='2020-01-01',
                        dataUseTermsUrl='https://pathoplexus.org/about/terms-of-use/restricted-data')

    def test_preserves_terms_even_after_date(self):
        index = index_records([self.row, self.row])
        self.assertEqual(metadata_for('PP_TEST|2019', index)['dataUseTerms'], 'RESTRICTED')
        self.assertEqual(metadata_for('PP_TEST|2019', index)['url'],
                         'https://pathoplexus.org/seq/PP_TEST')

    def test_missing_is_not_open(self):
        with self.assertRaises(ValueError):
            metadata_for('PP_MISSING|2026', {})
        self.assertEqual(metadata_for('EPI_ISL_123|2026', {}), {})

    def test_conflicts_rejected(self):
        with self.assertRaises(ValueError):
            index_records([self.row, dict(self.row, dataUseTerms='OPEN')])

    def test_invalid_terms_rejected(self):
        for changes in [dict(dataUseTerms='UNKNOWN'), dict(dataUseTermsRestrictedUntil=None),
                        dict(dataUseTermsRestrictedUntil='bad'), dict(dataUseTermsUrl=None)]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                index_records([dict(self.row, **changes)])


if __name__ == '__main__':
    unittest.main()
