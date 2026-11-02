"""Compile and replay reviewed national generic ballot polls, preserving other races."""
from collections import Counter
import argparse
import hashlib
import json
from pathlib import Path
import tempfile

import numpy as np

from ingest_senate_research import ROOT, compile_research, digest, replay, write_json
from election_modeling.cycles import RACES_2026_BY_ID
from election_modeling.persistence import load_election_model, save_election_model
from election_modeling.public import public_forecast_payload, public_race_history_payload

BASE = ROOT / 'research/generic_ballot_polls_20261101'
RACE = 'us_house_generic'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    config = json.loads((BASE / 'review-decisions.json').read_text())
    selected, held = compile_research(BASE, config, race_specs=(RACES_2026_BY_ID[RACE],),
                                     expected_office='generic_ballot')
    for row in selected:
        assert (row['candidate_a_party'], row['candidate_b_party']) == ('republican', 'democratic')
        row['acquisition_id'] = BASE.name
    path = ROOT / 'data/ingestion/2026_normalized_polls.json'
    existing = json.loads(path.read_text())['polls']
    retained = [r for r in existing if r.get('acquisition_id') != BASE.name]
    baseline = json.loads((BASE / 'baseline/polls-before.json').read_text())['polls']
    by_id = {r['poll_id']: r for r in retained}
    assert all(by_id.get(r['poll_id']) == r for r in baseline), 'Pre-existing source row changed'
    rows = sorted(retained + selected, key=lambda r: (r['field_date'], r['poll_id']))
    election, ledger = replay(rows)
    previous = load_election_model(BASE / 'baseline/model-before.json')
    preserved = []
    for race_id, prior in previous.races.items():
        if race_id == RACE:
            continue
        current = election.races[race_id]
        np.testing.assert_array_equal(current.filter.joint_mean, prior.filter.joint_mean)
        np.testing.assert_allclose(current.filter.joint_covariance, prior.filter.joint_covariance, atol=1e-15, rtol=0)
        assert current.electorate == prior.electorate
        assert current.observation_count == prior.observation_count
        preserved.append(race_id)
    model = election.races[RACE]
    assert (model.electorate.republican, model.electorate.democratic, model.electorate.independent) == (.37, .33, .30)
    assert model.electorate.share_standard_deviation == .01
    assert model.observation_count == len(selected) >= 10
    artifacts = set()
    for row in selected:
        assert row['evidence_artifacts'], row['poll_id']
        for item in row['evidence_artifacts']:
            assert hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest() == item['sha256']
            artifacts.add(item['path'])
    forecasts = public_forecast_payload(election)
    with tempfile.TemporaryDirectory(prefix='generic-ballot-replay-') as directory:
        staged = Path(directory) / 'polls.json'
        write_json(staged, {'polls': rows})
        history = public_race_history_payload(feed_path=staged)
    manifest = {
        'acquisition_id': BASE.name, 'accepted_count': len(selected), 'held': held,
        'counts_by_pollster': dict(Counter(r['pollster'] for r in selected)),
        'population_counts': dict(Counter(r['population'] for r in selected)),
        'party_basis_counts': dict(Counter(r['crosstab_basis'] for r in selected)),
        'precision_methods': dict(Counter(r['model_base_method'] for r in selected)),
        'window': config['window'], 'backfill_count': 0,
        'accepted_poll_ids': [r['poll_id'] for r in selected],
        'retained_baseline_rows': len(baseline), 'preserved_other_races': preserved,
        'source_artifacts_hash_checked': len(artifacts), 'total_feed_rows': len(rows),
        'electorate': {'republican': .37, 'democratic': .33, 'independent': .30, 'share_sd': .01},
        'review_decisions_sha256': digest(config), 'acquisition_rows_sha256': digest(selected),
        'feed_sha256': digest(rows), 'limitations': config['limitations'],
    }
    if args.check:
        actual = json.loads(path.read_text())['polls']
        assert actual == rows
        saved = load_election_model(ROOT / 'data/models/2026_election_model.json')
        for race_id, current in election.races.items():
            np.testing.assert_array_equal(current.filter.joint_mean, saved.races[race_id].filter.joint_mean)
            np.testing.assert_allclose(current.filter.joint_covariance, saved.races[race_id].filter.joint_covariance, atol=1e-15, rtol=0)
        for expected, output in [(forecasts, ROOT / 'docs/data/forecasts.json'), (history, ROOT / 'docs/data/race-history.json')]:
            observed = json.loads(output.read_text())
            expected = json.loads(json.dumps(expected))
            observed.pop('generated_at'); expected.pop('generated_at')
            assert observed == expected
        seen = json.loads((ROOT / 'data/ingestion/2026_seen_polls.json').read_text())
        assert set(seen['seen_poll_ids']) == ledger.seen_poll_ids
        assert set(seen['measurement_keys']) == ledger.measurement_keys
        stored = json.loads((BASE / 'ingestion-manifest.json').read_text())
        assert stored == manifest
    else:
        write_json(path, {'polls': rows})
        save_election_model(election, ROOT / 'data/models/2026_election_model.json')
        ledger.path = ROOT / 'data/ingestion/2026_seen_polls.json'; ledger.save()
        write_json(ROOT / 'docs/data/forecasts.json', forecasts)
        write_json(ROOT / 'docs/data/race-history.json', history)
        write_json(BASE / 'ingestion-manifest.json', manifest)
    print(json.dumps({'check_only': args.check, **manifest}, indent=2))


if __name__ == '__main__':
    main()
