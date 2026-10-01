#!/usr/bin/env python3
"""Refresh and audit sequence metadata before starting the dataset workflow."""
import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

import yaml

from data_use import snapshot_records
from snapshot_data_use import collect_snapshot, validate_snapshot, write_json_exclusive

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def checksum(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def stored_path(path):
    """Keep paths inside the workflow relocatable with the repository."""
    path = Path(path).resolve()
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def compare_metadata(previous, current):
    old = snapshot_records(previous)
    new = snapshot_records(current)
    changes = []
    for accession in sorted(old.keys() & new.keys()):
        for field in sorted(old[accession].keys() | new[accession].keys()):
            if old[accession].get(field) != new[accession].get(field):
                changes.append({'accession': accession, 'field': field,
                                'before': old[accession].get(field), 'after': new[accession].get(field)})
    return {'previousDataVersion': previous['info']['dataVersion'],
            'currentDataVersion': current['info']['dataVersion'],
            'added': sorted(new.keys() - old.keys()),
            'removed': sorted(old.keys() - new.keys()), 'changes': changes}


def previous_snapshot(runs_dir, fallback):
    for path in sorted(Path(runs_dir).glob('*/run.json'), reverse=True):
        manifest = read_json(path)
        if manifest['mode'] == 'refresh':
            snapshot = Path(manifest['snapshot'])
            if checksum(snapshot) != manifest['snapshotSha256']:
                raise ValueError(f'Previous snapshot was modified: {snapshot}')
            return snapshot
    return Path(fallback)


def prepare_run(config, replay=None, baseline=None):
    package = Path(config['input_package'])
    runs_dir = Path(config['metadata_runs_dir'])
    mode = 'replay' if replay else 'refresh'
    previous = None
    prior = None
    if mode == 'refresh':
        previous = Path(baseline) if baseline else previous_snapshot(runs_dir, config['data_use_snapshot'])
        prior = read_json(previous)
    if prior is not None:
        snapshot_records(prior)
    snapshot = read_json(replay) if replay else collect_snapshot(package)
    validate_snapshot(snapshot, package)
    report = compare_metadata(prior, snapshot) if prior is not None else None
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ') + '-' + uuid4().hex[:8]
    run_dir = runs_dir / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    frozen = run_dir / 'snapshot.json'
    write_json_exclusive(frozen, snapshot)
    manifest = {
        'mode': mode, 'createdAt': datetime.now(timezone.utc).isoformat(),
        'snapshot': stored_path(frozen), 'snapshotSha256': checksum(frozen),
        'inputPackage': stored_path(package), 'inputSha256': snapshot['inputSha256'],
        'workflowConfig': config,
    }
    if report is not None:
        report.update(previousSnapshot=stored_path(previous), previousSnapshotSha256=checksum(previous))
        write_json_exclusive(run_dir / 'changes.json', report)
        manifest['changes'] = stored_path(run_dir / 'changes.json')
        print(f'Metadata: {len(report["changes"])} field changes, '
              f'{len(report["added"])} added accessions, {len(report["removed"])} removed accessions.', flush=True)
    else:
        manifest['replayedFrom'] = stored_path(replay)
    manifest_path = run_dir / 'run.json'
    write_json_exclusive(manifest_path, manifest)
    print(f'Metadata run: {stored_path(manifest_path)}', flush=True)
    return manifest_path


def checked_run_snapshot(manifest_path, package):
    """Validate the recorded snapshot again when Snakemake loads the run."""
    manifest = read_json(manifest_path)
    if manifest['mode'] not in ('refresh', 'replay'):
        raise ValueError('Unknown metadata run mode')
    if Path(manifest['inputPackage']).resolve() != Path(package).resolve():
        raise ValueError('Metadata run belongs to a different input package')
    snapshot = Path(manifest['snapshot'])
    if checksum(snapshot) != manifest['snapshotSha256']:
        raise ValueError('Metadata snapshot was modified after preparation')
    validate_snapshot(read_json(snapshot), package)
    return str(snapshot)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--configfile', default='config/config.yaml', type=Path)
    parser.add_argument('--cores', default=1, type=int)
    parser.add_argument('--snapshot', type=Path, help='Explicit offline replay; must match the input FASTAs')
    parser.add_argument('--previous-snapshot', type=Path, help='Override the comparison baseline')
    parser.add_argument('--metadata-only', action='store_true', help='Collect and audit metadata without running Snakemake')
    parser.add_argument('--dry-run', action='store_true', help='Prepare metadata, then ask Snakemake for a dry run')
    args = parser.parse_args()
    if args.cores < 1:
        parser.error('--cores must be positive')
    if args.snapshot and args.previous_snapshot:
        parser.error('--previous-snapshot is only used for fresh updates')
    os.chdir(ROOT)
    try:
        config = yaml.safe_load(args.configfile.read_text(encoding='utf-8'))
        manifest = prepare_run(config, args.snapshot, args.previous_snapshot)
        if args.metadata_only:
            return 0
        command = ['snakemake', '--snakefile', 'Snakefile', '--configfile', str(args.configfile),
                   '--cores', str(args.cores), '--config', f'metadata_run_manifest={manifest}']
        if args.dry_run:
            command.append('--dry-run')
        return subprocess.run(command, check=False).returncode
    except (OSError, ValueError, KeyError) as error:
        print(f'Metadata update stopped: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
