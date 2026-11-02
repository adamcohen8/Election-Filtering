"""Compile the reviewed November 2 refresh and replay every model offline."""
import argparse
from collections import Counter
import hashlib,json,tempfile
from pathlib import Path
import numpy as np
from ingest_senate_research import ROOT,normalize_reviewed_row,digest,replay,write_json
from research_revisions import original_row
from election_modeling.cycles import RACES_2026_BY_ID
from election_modeling.nominees import NOMINEES_2026_BY_RACE
from election_modeling.persistence import load_election_model,save_election_model
from election_modeling.public import public_forecast_payload,public_race_history_payload
BASE=ROOT/'research/poll_refresh_20261102'


def compile_refresh():
    raw_rows=json.loads((BASE/'polls.json').read_text())['polls']
    config=json.loads((BASE/'review-decisions.json').read_text())
    baseline=json.loads((BASE/'baseline/polls-before.json').read_text())['polls']
    prior_by_id={r['poll_id']:r for r in baseline}
    keys=set();selected=[]
    for raw in raw_rows:
        race=RACES_2026_BY_ID[raw['race_id']];nom=NOMINEES_2026_BY_RACE[raw['race_id']]
        key=raw['race_id']+'/'+raw['poll_id'];assert key not in keys;keys.add(key)
        review=config['decisions'][key]
        assert review['action']=='accept' and review['record_sha256']==digest(raw)
        assert (raw['state'],raw['office'])==(race.state,race.office)
        assert (raw['candidate_a'],raw['candidate_b'],raw['candidate_a_party'],raw['candidate_b_party'])==(nom.republican.name,nom.candidate_b.name,nom.republican.party,nom.candidate_b.party)
        row=normalize_reviewed_row(raw,review,source_path=str((BASE/'polls.json').relative_to(ROOT)),start=config['window']['start'],end=config['window']['end'],expected_office=race.office)
        row['acquisition_id']=BASE.name
        row['refresh_id']=BASE.name
        if raw.get('supersedes_poll_id'):
            assert raw['supersedes_poll_id']==row['poll_id']
            prior=prior_by_id[row['poll_id']]
            row['acquisition_id']=prior['acquisition_id']
            row['sample_id']=prior['sample_id']
            row['supersedes_record']={'baseline_path':str((BASE/'baseline/polls-before.json').relative_to(ROOT)),'sha256':digest(prior)}
            assert original_row(row)==prior
        elif row['poll_id'] in prior_by_id:
            raise ValueError('Existing survey must be explicitly reviewed as a replacement')
        assert row['evidence_artifacts']
        for artifact in row['evidence_artifacts']:
            assert hashlib.sha256((ROOT/artifact['path']).read_bytes()).hexdigest()==artifact['sha256']
        selected.append(row)
    assert keys==set(config['decisions'])
    assert len({r['sample_id'] for r in selected})==len(selected)
    return sorted(selected,key=lambda r:(r['field_date'],r['poll_id'])),config,baseline


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    selected,config,baseline=compile_refresh()
    path=ROOT/'data/ingestion/2026_normalized_polls.json'
    existing=json.loads(path.read_text())['polls']
    # Refresh is replayable without multiplying waves or resurrecting predecessors.
    retained=[r for r in existing if r.get('refresh_id')!=BASE.name]
    revision_ids={r['poll_id'] for r in selected if r.get('supersedes_record')}
    retained=[r for r in retained if r['poll_id'] not in revision_ids]
    rows=sorted(retained+selected,key=lambda r:(r['field_date'],r['poll_id']))
    by_id={r['poll_id']:r for r in rows}
    assert len(by_id)==len(rows)
    assert all(original_row(by_id[r['poll_id']])==r for r in baseline), 'Previous input changed without a pinned revision'
    added=[r for r in selected if not r.get('supersedes_record')]
    assert len(rows)==len(baseline)+len(added)
    # Extra protection beyond poll IDs: same named pollster and field period per race.
    waves=[(r['race_id'],r['pollster'].casefold(),r.get('field_start'),r['field_date']) for r in rows]
    assert len(waves)==len(set(waves)), 'Survey wave duplicated'
    election,ledger=replay(rows)
    previous=load_election_model(BASE/'baseline/model-before.json')
    affected={r['race_id'] for r in selected};preserved=[]
    additions=Counter(r['race_id'] for r in added)
    for race,model in election.races.items():
        prior=previous.races[race]
        assert model.electorate==prior.electorate
        assert model.observation_count==prior.observation_count+additions[race]
        if race not in affected:
            np.testing.assert_array_equal(model.filter.joint_mean,prior.filter.joint_mean)
            np.testing.assert_allclose(model.filter.joint_covariance,prior.filter.joint_covariance,atol=1e-15,rtol=0)
            preserved.append(race)
    forecasts=public_forecast_payload(election)
    with tempfile.TemporaryDirectory(prefix='poll-refresh-') as directory:
        staged=Path(directory)/'polls.json';write_json(staged,{'polls':rows})
        history=public_race_history_payload(feed_path=staged)
    manifest={'acquisition_id':BASE.name,'window':config['window'],'new_observations':len(added),'revised_observations':len(selected)-len(added),'new_by_office':dict(Counter(r['office'] for r in added)),'new_by_race':dict(sorted(additions.items())),'new_by_pollster':dict(Counter(r['pollster'] for r in added)),'accepted_poll_ids':[r['poll_id'] for r in selected],'revision_poll_ids':sorted(revision_ids),'total_feed_rows':len(rows),'counts_by_race':dict(sorted(Counter(r['race_id'] for r in rows).items())),'unaffected_models_preserved':sorted(preserved),'all_turnout_weights_preserved':True,'acquisition_rows_sha256':digest(selected),'review_decisions_sha256':digest(config),'baseline_sha256':digest(baseline),'feed_sha256':digest(rows)}
    if args.check:
        assert existing==rows
        saved=load_election_model(ROOT/'data/models/2026_election_model.json')
        for race,model in election.races.items():
            actual=saved.races[race]
            np.testing.assert_array_equal(model.filter.joint_mean,actual.filter.joint_mean)
            np.testing.assert_allclose(model.filter.joint_covariance,actual.filter.joint_covariance,atol=1e-15,rtol=0)
            assert model.electorate==actual.electorate and model.observation_count==actual.observation_count
        for expected,output in [(forecasts,ROOT/'docs/data/forecasts.json'),(history,ROOT/'docs/data/race-history.json')]:
            actual=json.loads(output.read_text());expected=json.loads(json.dumps(expected));actual.pop('generated_at');expected.pop('generated_at');assert actual==expected
        seen=json.loads((ROOT/'data/ingestion/2026_seen_polls.json').read_text())
        assert set(seen['seen_poll_ids'])==ledger.seen_poll_ids and set(seen['measurement_keys'])==ledger.measurement_keys
        assert json.loads((BASE/'ingestion-manifest.json').read_text())==manifest
    else:
        write_json(path,{'polls':rows});save_election_model(election,ROOT/'data/models/2026_election_model.json')
        ledger.path=ROOT/'data/ingestion/2026_seen_polls.json';ledger.save()
        write_json(ROOT/'docs/data/forecasts.json',forecasts);write_json(ROOT/'docs/data/race-history.json',history)
        write_json(BASE/'ingestion-manifest.json',manifest)
    print(json.dumps({'check_only':args.check,**manifest},indent=2))


if __name__=='__main__':main()
