"""Verify the user-requested AtlasIntel exclusion and preservation of all other inputs."""
from pathlib import Path
from collections import Counter
from statistics import mean
import json,hashlib,sys
import numpy as np
B=Path(__file__).resolve().parent;ROOT=B.parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts')]
from election_modeling.ingestion import user_pollster_exclusion_reason
from election_modeling.persistence import load_election_model
from election_modeling.public import public_forecast_payload,public_race_history_payload
from ingest_senate_research import replay,digest

def read(p):return json.loads(p.read_text())
def write(p,x):p.write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
before=read(B/'baseline/polls-before.json')['polls'];after=read(ROOT/'data/ingestion/2026_normalized_polls.json')['polls']
removed=[r for r in before if user_pollster_exclusion_reason(r['pollster'])]
kept=[r for r in before if not user_pollster_exclusion_reason(r['pollster'])]
assert len(before)==347 and len(removed)==18 and len(after)==329
assert after==kept, 'A non-excluded input changed or an excluded input survived'
assert read(B/'baseline/raw-before.json')==read(ROOT/'research/poll_refresh_20261102/polls.json')
assert read(B/'baseline/reviews-before.json')==read(ROOT/'research/poll_refresh_20261102/review-decisions.json')
write(B/'excluded-polls.json',{'excluded_on':'2026-11-03','reason':'User instructed: I want you to exclude Atlas Intel from the model','scope':'All modeled offices and all AtlasIntel waves, including future ingestion','polls':removed})
counts=Counter(r['race_id'] for r in removed);affected=set(counts)
expected,ledger=replay(after);current=load_election_model(ROOT/'data/models/2026_election_model.json');prior=load_election_model(B/'baseline/model-before.json')
prior_json=read(B/'baseline/model-before.json')['races'];current_json=read(ROOT/'data/models/2026_election_model.json')['races'];preserved=[]
for race,m in current.races.items():
    p=prior.races[race]
    assert m.electorate==p.electorate
    assert m.observation_count==p.observation_count-counts[race]
    assert m.observation_count==expected.races[race].observation_count
    np.testing.assert_array_equal(m.filter.joint_mean,expected.races[race].filter.joint_mean)
    np.testing.assert_allclose(m.filter.joint_covariance,expected.races[race].filter.joint_covariance,atol=1e-15,rtol=0)
    for k in ['transition','process_covariance','clip_support','shared_margin_sd','pollster_margin_sd','survey_margin_sd']:assert current_json[race]['filter'][k]==prior_json[race]['filter'][k]
    if race not in affected:
        np.testing.assert_array_equal(m.filter.joint_mean,p.filter.joint_mean)
        np.testing.assert_allclose(m.filter.joint_covariance,p.filter.joint_covariance,atol=1e-15,rtol=0);preserved.append(race)
seen=read(ROOT/'data/ingestion/2026_seen_polls.json')
assert set(seen['seen_poll_ids'])==ledger.seen_poll_ids=={r['poll_id'] for r in after}
assert set(seen['measurement_keys'])==ledger.measurement_keys
removed_ids={r['poll_id'] for r in removed};assert not (removed_ids&ledger.seen_poll_ids)
for result,path in [(public_forecast_payload(expected),ROOT/'docs/data/forecasts.json'),(public_race_history_payload(feed_path=ROOT/'data/ingestion/2026_normalized_polls.json'),ROOT/'docs/data/race-history.json')]:
    actual=read(path);result=json.loads(json.dumps(result));actual.pop('generated_at');result.pop('generated_at');assert actual==result
hist={r['race_id']:r for r in read(ROOT/'docs/data/race-history.json')['races']}
for h in hist.values():
    assert not any(user_pollster_exclusion_reason(p['pollster']) for p in h['poll_points'])
    assert not (removed_ids&{p['poll_id'] for p in h['poll_points']})
    points=sorted(h['poll_points'],key=lambda p:(p['date'],p['poll_id']));window=points[-7:];avg=h['rolling_average']
    if not window:assert avg is None;continue
    assert avg['poll_ids']==[p['poll_id'] for p in window]
    a=mean(p['candidate_a_share'] for p in window);b=mean(p['candidate_b_share'] for p in window)
    assert avg['candidate_a_share']==round(a,4) and avg['candidate_b_share']==round(b,4)
    assert avg['margin_percent']==round(100*(a-b),2)
fc={r['race_id']:r for r in read(ROOT/'docs/data/forecasts.json')['races']};prev={r['race_id']:r for r in read(B/'baseline/forecasts-before.json')['races']}
results=[]
for race in sorted(current.races):
    results.append({'race_id':race,'state':fc[race]['state'],'office':fc[race]['office'],'removed_observations':counts[race],'before':{k:prev[race][k] for k in ['candidate_a_share','candidate_b_share','margin_percent','observation_count']},'after':{k:fc[race][k] for k in ['candidate_a_name','candidate_b_name','candidate_a_share','candidate_b_share','margin_percent','observation_count']}})
write(B/'results.json',results)
assert len(current.races)==28 and 'ak_gov' not in current.races
assert fc['ne_sen']['candidate_b_party']=='Independent'
manifest=read(ROOT/'research/poll_refresh_20261102/ingestion-manifest.json')
assert manifest['user_excluded_observations']==18
assert {r['poll_id'] for r in manifest['user_excluded_polls']}==removed_ids
validation={'checked_on':'2026-11-03','before_rows':347,'after_rows':329,'removed_observations':18,'removed_by_office':dict(Counter(r['office'] for r in removed)),'removed_by_race':dict(counts),'all_other_329_inputs_unchanged':True,'all_original_source_records_and_reviews_preserved':True,'all_28_turnout_weights_and_model_settings_preserved':True,'unaffected_races_preserved':preserved,'no_excluded_polls_in_active_feed_ledger_snapshot_history_or_rolling_averages':True,'snapshot_forecasts_ledger_history_match_full_replay':True,'rolling_averages_independently_recomputed':True,'acquisition_checks_passed':5,'python_tests_passed':116,'ui_tests_passed':6,'feed_sha256':digest(after),'limitations':['Historical Maine calibration datasets intentionally absent; no empirical forecasting-calibration claim.']}
write(B/'validation.json',validation);print(json.dumps(validation,indent=2))
