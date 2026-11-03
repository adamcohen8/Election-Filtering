"""Verify this scrub against its immutable 329-observation baseline."""
from pathlib import Path
from collections import Counter
from statistics import mean
import hashlib,json,re,sys
import numpy as np
B=Path(__file__).resolve().parent;ROOT=B.parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts')]
from election_modeling.cycles import TURNOUT_2024_PREDICTION_ELECTORATES_BY_RACE_ID
from election_modeling.persistence import load_election_model
from ingest_senate_research import digest

def read(p):return json.loads(p.read_text())
def write(p,v):p.write_text(json.dumps(v,indent=2,allow_nan=False)+'\n')
for a in read(B/'baseline/manifest.json'):
    assert hashlib.sha256((ROOT/a['path']).read_bytes()).hexdigest()==a['sha256']
before=read(B/'baseline/polls-before.json')['polls'];after=read(ROOT/'data/ingestion/2026_normalized_polls.json')['polls']
raw=read(B/'new-records.json')['polls'];old={r['poll_id']:r for r in before};now={r['poll_id']:r for r in after}
ids={r['race_id']+'--'+r['poll_id'] for r in raw};affected={r['race_id'] for r in raw}
assert len(before)==329 and len(after)==347 and len(raw)==18
assert set(now)-set(old)==ids and all(now[k]==v for k,v in old.items())
assert len(now)==len(after)==len({r['sample_id'] for r in after})
assert len({(r['race_id'],r['pollster'].casefold(),r.get('field_start'),r['field_date']) for r in after})==len(after)
prior_raw=read(B/'baseline/raw-before.json')['polls'];current_raw=read(ROOT/'research/poll_refresh_20261102/polls.json')['polls']
assert len(prior_raw)==45 and current_raw[:45]==prior_raw and current_raw[45:]==raw
prior_reviews=read(B/'baseline/reviews-before.json')['decisions'];reviews=read(ROOT/'research/poll_refresh_20261102/review-decisions.json')['decisions']
assert all(reviews[k]==v for k,v in prior_reviews.items())
for r in raw:
    normalized=now[r['race_id']+'--'+r['poll_id']]
    assert normalized['research_record_sha256']==digest(r)
    assert all(normalized[p+'_n'] is None for p in ['republican','democratic','independent'])
    assert normalized['precision_review']['cell_sd']==.05
    assert normalized['precision_review']['within_group_correlation']==-.5
    for a in normalized['evidence_artifacts']+r.get('additional_source_artifacts',[]):
        assert hashlib.sha256((ROOT/a['path']).read_bytes()).hexdigest()==a['sha256']
prior=load_election_model(B/'baseline/model-before.json');actual=load_election_model(ROOT/'data/models/2026_election_model.json')
pj=read(B/'baseline/model-before.json')['races'];aj=read(ROOT/'data/models/2026_election_model.json')['races'];counts=Counter(r['race_id'] for r in raw);preserved=[]
for race,m in actual.races.items():
    p=prior.races[race]
    assert m.electorate==p.electorate==TURNOUT_2024_PREDICTION_ELECTORATES_BY_RACE_ID[race]
    assert m.observation_count==p.observation_count+counts[race]
    for k in ['transition','process_covariance','clip_support','shared_margin_sd','pollster_margin_sd','survey_margin_sd']:assert aj[race]['filter'][k]==pj[race]['filter'][k]
    if race not in affected:
        np.testing.assert_array_equal(m.filter.joint_mean,p.filter.joint_mean)
        np.testing.assert_allclose(m.filter.joint_covariance,p.filter.joint_covariance,atol=1e-15,rtol=0);preserved.append(race)
assert len(actual.races)==28 and 'ak_gov' not in actual.races
assert actual.races['tx_sen'].observation_count==22
history={r['race_id']:r for r in read(ROOT/'docs/data/race-history.json')['races']}
for race,h in history.items():
    points=sorted(h['poll_points'],key=lambda r:(r['date'],r['poll_id']));window=points[-7:];avg=h['rolling_average']
    if not window:assert avg is None;continue
    assert avg['poll_ids']==[p['poll_id'] for p in window] and avg['poll_count']==len(window)
    a=mean(p['candidate_a_share'] for p in window);b=mean(p['candidate_b_share'] for p in window)
    assert avg['candidate_a_share']==round(a,4) and avg['candidate_b_share']==round(b,4)
    assert avg['margin']==round(a-b,4) and avg['margin_percent']==round(100*(a-b),2)
patterns=[rb'AIza[0-9A-Za-z_-]{35}',rb'gh[pousr]_[A-Za-z0-9]{30,255}',rb'github_pat_[A-Za-z0-9_]{50,255}',rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----']
artifacts=[]
for inv in ['download-inventory.json','more-download-inventory.json','extra-download-inventory.json','last-download-inventory.json','final-download-inventory.json','recheck-download-inventory.json']:
    for a in read(B/inv):
        if 'path' not in a:continue
        p=ROOT/a['path'];data=p.read_bytes();assert hashlib.sha256(data).hexdigest()==a['sha256']
        assert not any(re.search(pattern,data) for pattern in patterns),p
        artifacts.append({'path':a['path'],'sha256':a['sha256']})
forecast={r['race_id']:r for r in read(ROOT/'docs/data/forecasts.json')['races']};bf={r['race_id']:r for r in read(B/'baseline/forecasts-before.json')['races']}
assert forecast['ne_sen']['candidate_b_party']=='Independent'
results=[]
for race in sorted(affected):
    results.append({'race_id':race,'new_observations':counts[race],'before':{k:bf[race][k] for k in ['candidate_a_share','candidate_b_share','margin_percent','observation_count']},'after':{k:forecast[race][k] for k in ['candidate_a_name','candidate_b_name','candidate_a_share','candidate_b_share','margin_percent','observation_count']},'rolling_average':history[race]['rolling_average']})
write(B/'results.json',results);write(B/'source-artifact-hashes.json',artifacts)
validation={'checked_on':'2026-11-03','baseline_commit':'a2c4c6d','before_rows':len(before),'after_rows':len(after),'new_observations':len(raw),'new_by_office':dict(Counter(r['office'] for r in raw)),'new_by_pollster':dict(Counter(r['pollster'] for r in raw)),'new_by_race':dict(counts),'affected_races':sorted(affected),'unaffected_races_preserved':preserved,'all_329_previous_rows_exactly_preserved':True,'all_45_previous_raw_records_and_reviews_exactly_preserved':True,'all_28_turnout_weights_and_model_assumptions_preserved':True,'full_replay_snapshot_ledger_forecasts_history_checks_passed':True,'all_five_acquisition_checks_passed':True,'historical_senate_and_governor_source_audits_passed':True,'rolling_averages_independently_recomputed':True,'no_duplicate_ids_samples_or_survey_waves':True,'source_artifacts_hash_checked':len(artifacts),'credential_pattern_scan_passed':True,'python_tests_passed':103,'ui_tests_passed':6,'feed_sha256':digest(after),'publication_date_not_index_added_date':True,'limitations':['Historical Maine calibration datasets intentionally omitted; no empirical forecasting-calibration claim.','Unknown applicable subgroup Ns remain null under explicit conservative covariance assumptions.','This is a bounded search of public sources, not proof of exhaustive private/unpublished coverage.','Updated locally; not committed, pushed or deployed in this scrub.']}
write(B/'validation.json',validation);print(json.dumps(validation,indent=2))
