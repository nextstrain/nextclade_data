"""Collect public NCBI nucleotide metadata for exact input accessions."""
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from urllib.parse import urlencode
from urllib.request import urlopen

from data_use import ncbi_accession_for


def index_ncbi_records(rows):
    result = {}
    for row in rows:
        accession = row['accession']
        if ncbi_accession_for(accession) != accession:
            raise ValueError(f'Invalid NCBI accession: {accession}')
        country = row['geoLocCountry']
        if country is not None and (not isinstance(country, str) or not country.strip()):
            raise ValueError(f'Invalid NCBI country for {accession}')
        if row.get('sourceUrl') != f'https://www.ncbi.nlm.nih.gov/nuccore/{accession}':
            raise ValueError(f'Invalid NCBI source URL for {accession}')
        if accession in result and result[accession] != row:
            raise ValueError(f'Conflicting NCBI metadata for {accession}')
        result[accession] = dict(row)
    return result


def collect_ncbi(accessions):
    rows, urls = [], []
    accessions = sorted(accessions)
    for offset in range(0, len(accessions), 100):
        if offset:
            time.sleep(0.4)  # Stay below the unauthenticated E-utilities rate limit.
        batch = accessions[offset:offset + 100]
        url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?' + urlencode({
            'db': 'nuccore', 'id': ','.join(batch), 'rettype': 'gb',
            'retmode': 'xml', 'tool': 'denv-update-workflow'})
        with urlopen(url, timeout=60) as response:
            try:
                root = ET.parse(response).getroot()
            except ET.ParseError as error:
                raise ValueError('Invalid NCBI XML response') from error
        urls.append(url)
        returned = {}
        for record in root.findall('GBSeq'):
            accession = record.findtext('GBSeq_accession-version')
            qualifiers = {}
            for feature in record.findall('./GBSeq_feature-table/GBFeature'):
                if feature.findtext('GBFeature_key') == 'source':
                    qualifiers.update({q.findtext('GBQualifier_name'): q.findtext('GBQualifier_value')
                                       for q in feature.findall('./GBFeature_quals/GBQualifier')})
            location = qualifiers.get('geo_loc_name') or qualifiers.get('country')
            returned[accession] = {
                'accession': accession, 'geoLocName': location,
                'geoLocCountry': location.split(':', 1)[0].strip() if location else None,
                'collectionDate': qualifiers.get('collection_date'),
                'updateDate': record.findtext('GBSeq_update-date'),
                'sourceUrl': f'https://www.ncbi.nlm.nih.gov/nuccore/{accession}'}
        for requested in batch:
            matches = [a for a in returned if a == requested or
                       ('.' not in requested and a.split('.')[0] == requested)]
            if len(matches) != 1:
                raise ValueError(f'NCBI did not return the requested accession/version: {requested}')
            row = dict(returned[matches[0]], accession=requested,
                       resolvedAccession=matches[0],
                       sourceUrl=f'https://www.ncbi.nlm.nih.gov/nuccore/{requested}')
            rows.append(row)
    index_ncbi_records(rows)
    return {'retrievedAt': datetime.now(timezone.utc).isoformat(), 'sourceUrls': urls, 'data': rows}
