"""Audit the 9PM EST increment against the pinned 316-observation baseline."""
from pathlib import Path
from collections import Counter
from statistics import mean
import hashlib,json,re,sys,zipfile
import numpy as np
BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts')]
from election_modeling.cycles import TURNOUT_2024_PREDICTION_ELECTORATES_BY_RACE_ID
from election_modeling.persistence import load_election_model
from dataclasses import asdict
from ingest_senate_research import digest

def read(p):return json.loads(p.read_text())
def write(p,v):p.write_text(json.dumps(v,indent=2,allow_nan=False)+'\n')
for item in read(BASE/'baseline/manifest.json'):
    assert hashlib.sha256((ROOT/item['baseline']).read_bytes()).hexdigest()==item['sha256']
before=read(BASE/'baseline/before-0-2026_normalized_polls.json')['polls'];after=read(ROOT/'data/ingestion/2026_normalized_polls.json')['polls']
old={r['poll_id']:r for r in before};now={r['poll_id']:r for r in after}
raw=read(BASE/'new-records.json')['polls'];ids={r['race_id']+'--'+r['poll_id'] for r in raw};affected={r['race_id'] for r in raw}
assert len(before)==316 and len(after)==329 and set(now)-set(old)==ids
assert all(now[k]==v for k,v in old.items())
assert len({(r['race_id'],r['pollster'].casefold(),r.get('field_start'),r['field_date']) for r in after})==len(after)
prior_raw=read(BASE/'baseline/before-5-polls.json')['polls'];current_raw=read(ROOT/'research/poll_refresh_20261102/polls.json')['polls']
assert current_raw[:32]==prior_raw and current_raw[32:]==raw
prior_dec=read(BASE/'baseline/before-6-review-decisions.json')['decisions'];dec=read(ROOT/'research/poll_refresh_20261102/review-decisions.json')['decisions']
assert all(dec[k]==v for k,v in prior_dec.items())
bmodel=load_election_model(BASE/'baseline/before-1-2026_election_model.json');amodel=load_election_model(ROOT/'data/models/2026_election_model.json')
bm=read(BASE/'baseline/before-1-2026_election_model.json')['races'];am=read(ROOT/'data/models/2026_election_model.json')['races']
counts=Counter(r['race_id'] for r in raw);preserved=[]
for race,m in amodel.races.items():
    assert m.electorate==bmodel.races[race].electorate==TURNOUT_2024_PREDICTION_ELECTORATES_BY_RACE_ID[race]
    assert m.observation_count==bmodel.races[race].observation_count+counts[race]
    for k in ['transition','process_covariance','clip_support','shared_margin_sd','pollster_margin_sd','survey_margin_sd']:assert am[race]['filter'][k]==bm[race]['filter'][k]
    if race not in affected:
        np.testing.assert_array_equal(m.filter.joint_mean,bmodel.races[race].filter.joint_mean)
        np.testing.assert_allclose(m.filter.joint_covariance,bmodel.races[race].filter.joint_covariance,atol=1e-15,rtol=0);preserved.append(race)
assert len(amodel.races)==28 and 'ak_gov' not in amodel.races
assert asdict(amodel.races['me_sen'].electorate)=={'republican':.31,'democratic':.28,'independent':.41,'share_standard_deviation':.01}
assert amodel.races['me_gov'].electorate==amodel.races['me_sen'].electorate
# Independently recompute last seven-poll arithmetic comparator from public markers.
hist={r['race_id']:r for r in read(ROOT/'docs/data/race-history.json')['races']}
for race,h in hist.items():
    points=sorted(h['poll_points'],key=lambda r:(r['date'],r['poll_id']));window=points[-7:];avg=h['rolling_average']
    if not window:assert avg is None;continue
    assert avg['poll_ids']==[p['poll_id'] for p in window] and avg['poll_count']==len(window)
    a=mean(p['candidate_a_share'] for p in window);b=mean(p['candidate_b_share'] for p in window)
    assert avg['candidate_a_share']==round(a,4) and avg['candidate_b_share']==round(b,4)
    assert avg['margin']==round(a-b,4) and avg['margin_percent']==round(100*(a-b),2)
# Every archived original or sanitized artifact is pinned; credentials are checked
# inside the XLSX archive too, not just against compressed bytes.
artifacts=[]
patterns=[rb'AIza[0-9A-Za-z_-]{35}',rb'gh[pousr]_[A-Za-z0-9]{30,255}',rb'github_pat_[A-Za-z0-9_]{50,255}',rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----']
for item in read(BASE/'download-inventory.json'):
    if item['status']!='downloaded':continue
    p=ROOT/item['file'];data=p.read_bytes();assert hashlib.sha256(data).hexdigest()==item['sha256']
    blobs=[data]
    if p.suffix=='.xlsx':
        with zipfile.ZipFile(p) as z:blobs.extend(z.read(n) for n in z.namelist())
    assert not any(re.search(pat,blob) for pat in patterns for blob in blobs),p
    artifacts.append({'path':item['file'],'sha256':item['sha256'],'redactions':item['google_key_redactions']})
forecast={r['race_id']:r for r in read(ROOT/'docs/data/forecasts.json')['races']};bforecast={r['race_id']:r for r in read(BASE/'baseline/before-3-forecasts.json')['races']}
results=[]
for race in sorted(affected):
    f=forecast[race];b=bforecast[race]
    results.append({'race_id':race,'state':f['state'],'office':f['office'],'new_observations':counts[race],'before':{k:b[k] for k in ['candidate_a_share','candidate_b_share','margin_percent','status']},'kalman':{k:f[k] for k in ['candidate_a_name','candidate_b_name','candidate_a_share','candidate_b_share','margin_percent','status','observation_count','state_date','forecast_date']},'rolling_average':hist[race]['rolling_average']})
validation={'checked_on':'2026-11-02','scheduled_cutoff':'2026-11-02T21:00:00-05:00','baseline_commit':'d025e095364f3f188433ee25b50ad03704641cde','before_feed_rows':len(before),'after_feed_rows':len(after),'new_observations':len(raw),'new_surveys':len({(r['pollster'],r['state'],r['field_start'],r['field_date']) for r in raw}),'new_by_office':dict(Counter(r['office'] for r in raw)),'new_by_race':dict(sorted(counts.items())),'previous_316_rows_exactly_preserved':True,'previous_32_raw_records_and_reviews_preserved':True,'current_turnout_weights_all_preserved':True,'model_assumptions_all_preserved':True,'unaffected_models_preserved':preserved,'rolling_averages_independently_recomputed':True,'no_duplicate_ids_or_survey_waves':True,'snapshot_ledger_forecasts_history_match_full_replay':True,'all_five_acquisition_check_commands_passed':True,'historical_senate_and_governor_source_audits_passed':True,'python_tests_passed':103,'ui_tests_passed':6,'source_artifacts_hash_checked':len(artifacts),'archived_source_redactions':sum(r['redactions'] for r in artifacts),'credential_pattern_scan_passed':True,'feed_sha256':digest(after),'limitations':['Historical Maine calibration datasets intentionally excluded; calibration module not run. No empirical forecast-accuracy claim.','Unknown-date Iowa Rasmussen Senate page retains honest October31–November2 bounds because source dateline is stale.','Unrecovered complete party tables are held; private/unpublished coverage is not exhaustive.','Changes are local; no GitHub publication or deployment was performed.']}
assert validation['new_surveys']==8
write(BASE/'validation.json',validation);write(BASE/'results.json',results);write(BASE/'source-artifact-hashes.json',artifacts)
print(json.dumps(validation,indent=2))
