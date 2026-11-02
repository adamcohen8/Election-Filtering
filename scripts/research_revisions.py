"""Preserve pinned acquisition history while applying reviewed source revisions."""
import json
from pathlib import Path

from ingest_senate_research import ROOT, digest


def original_row(row):
    """Resolve an explicitly pinned predecessor, never silently accept an edit."""
    revision = row.get('supersedes_record')
    if not revision:
        return row
    path = (ROOT / revision['baseline_path']).resolve()
    if not path.is_relative_to(ROOT / 'research'):
        raise ValueError('Revision predecessor must be archived under research')
    matches = [r for r in json.loads(path.read_text())['polls']
               if r['poll_id'] == row['poll_id']]
    if len(matches) != 1 or digest(matches[0]) != revision['sha256']:
        raise ValueError('Revision predecessor hash mismatch')
    prior = matches[0]
    if (prior['race_id'], prior['sample_id']) != (row['race_id'], row['sample_id']):
        raise ValueError('A revision must replace the same race and survey')
    return prior


def original_rows(rows):
    return [original_row(r) for r in rows]


def apply_current_revisions(selected, existing):
    """An older acquisition rebuild must retain a later reviewed revision."""
    revisions = {r['poll_id']: r for r in existing if r.get('supersedes_record')}
    result = []
    for row in selected:
        current = revisions.get(row['poll_id'])
        if current is not None:
            if original_row(current) != row:
                raise ValueError('Rebuilt acquisition differs from revision predecessor')
            row = current
        result.append(row)
    return result


def same_race_inputs(rows, baseline, race_id):
    current = {r['poll_id']: r for r in rows if r['race_id'] == race_id}
    previous = {r['poll_id']: r for r in baseline if r['race_id'] == race_id}
    return current == previous
