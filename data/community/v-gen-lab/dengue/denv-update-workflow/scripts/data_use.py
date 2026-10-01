"""Read and validate the local Pathoplexus metadata snapshot (offline)."""
import json
import re
from datetime import date
from pathlib import Path

TERMS = ('dataUseTerms', 'dataUseTermsRestrictedUntil', 'dataUseTermsUrl')
COLUMNS = ('accession', 'url', 'geoLocCountry', 'country', *TERMS,
           'PPX_accession', 'PPX_accession__url', 'INSDC_accession',
           'INSDC_accession__url', 'dataUseTerms__url', 'restrictedUntil')
# Keep geoLocCountry verbatim; normalize only established spelling variants
# for the country coloring and Augur's bundled map coordinates.
COUNTRY_ALIASES = {
    "Cote d'Ivoire": "Côte d'Ivoire",
    'Reunion': 'Réunion',
    'Viet Nam': 'Vietnam',
}


def accession_for(name):
    accession = name.split('|', 1)[0]
    return accession if re.fullmatch(r'PP_[A-Z0-9]+', accession) else None


def ncbi_accession_for(name):
    """Recognize nucleotide accessions, never arbitrary local or GISAID IDs."""
    accession = name.split('|', 1)[0]
    if accession.startswith('PP_'):
        return None
    return accession if re.fullmatch(r'(?:[A-Z]{1,2}\d{5,6}|[A-Z]{4}\d{8,10}|[A-Z]{6}\d{9,11}|[A-Z]{2}_\d+)(?:\.\d+)?', accession) else None


def fasta_names(path):
    with Path(path).open() as handle:
        return [line[1:].strip().split()[0] for line in handle if line.startswith('>')]


def index_records(records):
    indexed = {}
    for row in records:
        accession = row['accession']
        if accession_for(accession) != accession:
            raise ValueError(f'Invalid Pathoplexus accession: {accession}')
        values = {key: row[key] for key in (*TERMS, 'geoLocCountry')}
        values['insdcAccessionFull'] = row.get('insdcAccessionFull')
        country = values['geoLocCountry']
        if country is not None and (not isinstance(country, str) or not country.strip()):
            raise ValueError(f'Invalid country for {accession}: {country!r}')
        if values['dataUseTerms'] not in ('OPEN', 'RESTRICTED'):
            raise ValueError(f'Unknown data-use terms for {accession}: {values}')
        if not (values['dataUseTermsUrl'] or '').startswith('https://pathoplexus.org/'):
            raise ValueError(f'Missing or invalid terms URL for {accession}')
        until = values['dataUseTermsRestrictedUntil']
        if until:
            date.fromisoformat(until)
        elif values['dataUseTerms'] == 'RESTRICTED':
            raise ValueError(f'Missing restriction end date for {accession}')
        if accession in indexed and indexed[accession] != values:
            raise ValueError(f'Conflicting terms for {accession}')
        indexed[accession] = values
    return indexed


def load_snapshot(path):
    return snapshot_records(json.loads(Path(path).read_text()))


def snapshot_records(snapshot):
    from ncbi_metadata import index_ncbi_records
    return {**index_records(snapshot['data']),
            **index_ncbi_records(snapshot.get('ncbi', {}).get('data', []))}


def metadata_for(name, records):
    accession = accession_for(name)
    if not accession:
        accession = ncbi_accession_for(name)
        if not accession or accession not in records:
            return {}  # Older offline snapshots may not contain NCBI metadata.
        country = records[accession]['geoLocCountry']
        url = f'https://www.ncbi.nlm.nih.gov/nuccore/{accession}'
        return {'accession': accession, 'url': url, 'geoLocCountry': country,
                'country': COUNTRY_ALIASES.get(country, country),
                'INSDC_accession': accession, 'INSDC_accession__url': url}
    if accession not in records:
        raise ValueError(f'Pathoplexus terms missing from snapshot: {accession}')
    values = records[accession]
    insdc = values.get('insdcAccessionFull')
    return {'accession': accession,
            'url': f'https://pathoplexus.org/seq/{accession}',
            'country': COUNTRY_ALIASES.get(records[accession]['geoLocCountry'], records[accession]['geoLocCountry']),
            **{key: values[key] for key in ('geoLocCountry', *TERMS)},
            'PPX_accession': accession,
            'PPX_accession__url': f'https://pathoplexus.org/seq/{accession}',
            'INSDC_accession': insdc or '',
            'INSDC_accession__url': f'https://www.ncbi.nlm.nih.gov/nuccore/{insdc}' if insdc else '',
            'dataUseTerms__url': values['dataUseTermsUrl'],
            'restrictedUntil': values['dataUseTermsRestrictedUntil']}
