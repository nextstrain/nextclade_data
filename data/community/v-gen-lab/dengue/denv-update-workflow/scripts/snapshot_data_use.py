#!/usr/bin/env python3
"""Explicitly fetch public metadata; normal workflow runs stay offline."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

from data_use import TERMS, accession_for, ncbi_accession_for, fasta_names, index_records
from ncbi_metadata import collect_ncbi, index_ncbi_records


def package_fingerprints(package):
    files = [Path(package) / f'DENV{n}_{kind}.fasta'
             for n in range(1, 5) for kind in ('representatives', 'test_set')]
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in files}


def package_accessions(package, parser=accession_for):
    return {parser(name) for filename in package_fingerprints(package)
            for name in fasta_names(Path(package) / filename)} - {None}


def validate_snapshot(snapshot, package):
    if snapshot.get('inputSha256') != package_fingerprints(package):
        raise ValueError('Metadata snapshot does not match the eight input FASTAs')
    if not snapshot.get('retrievedAt') or not snapshot.get('info', {}).get('dataVersion'):
        raise ValueError('Metadata snapshot lacks retrieval time or API data version')
    records = index_records(snapshot['data'])
    missing = package_accessions(package) - records.keys()
    if missing:
        raise ValueError(f'Accessions absent from metadata snapshot: {sorted(missing)}')
    if snapshot.get('schemaVersion', 1) >= 2:
        ncbi = snapshot['ncbi']
        if not ncbi.get('retrievedAt'):
            raise ValueError('NCBI snapshot lacks retrieval time')
        missing = package_accessions(package, ncbi_accession_for) - index_ncbi_records(ncbi['data']).keys()
        if missing:
            raise ValueError(f'NCBI accessions absent from metadata snapshot: {sorted(missing)}')
    return records


def collect_snapshot(package):
    fingerprints = package_fingerprints(package)
    wanted = package_accessions(package)
    if not wanted:
        raise ValueError('No Pathoplexus accessions found in the input FASTAs')
    # One API response provides a consistent metadata version for every build.
    # Only the latest accession versions are relevant to a fresh update.
    url = 'https://lapis.pathoplexus.org/dengue/sample/details?' + urlencode({
        'fields': ','.join(('accession', 'geoLocCountry', 'insdcAccessionFull', *TERMS)),
        'versionStatus': 'LATEST_VERSION',
    })
    with urlopen(url, timeout=60) as response:
        payload = json.load(response)
    records = index_records([row for row in payload['data'] if row['accession'] in wanted])
    snapshot = {
        'schemaVersion': 2,
        'retrievedAt': datetime.now(timezone.utc).isoformat(),
        'sourceUrl': url,
        'info': payload['info'],
        'inputSha256': fingerprints,
        'data': [{'accession': accession, **records[accession]} for accession in sorted(records)],
        'ncbi': collect_ncbi(package_accessions(package, ncbi_accession_for)),
    }
    # Also detects a package changed while the network request was in flight.
    validate_snapshot(snapshot, package)
    return snapshot


def write_json_exclusive(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8') as handle:
        json.dump(content, handle, indent=2, ensure_ascii=False)
        handle.write('\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-package', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(f'Refusing to overwrite snapshot: {args.output}')
    snapshot = collect_snapshot(args.input_package)
    write_json_exclusive(args.output, snapshot)
    print(f'Saved metadata for {len(snapshot["data"])} accessions to {args.output}')


if __name__ == '__main__':
    main()
