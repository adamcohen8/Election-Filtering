"""Regression and synthetic statistical checks; no historical datasets required."""
from copy import deepcopy
from dataclasses import replace
import json

import numpy as np
import pytest

from election_modeling import (
    Electorate, ElectionModel, KalmanState, RaceKalmanFilter, RaceModel,
    NormalizedPoll, PartyIDCrosstab, PollObservation, PollIngestionPipeline,
    StaticPollSource, create_2026_election_model, public_forecast_payload,
    save_election_model, load_election_model, public_race_history_payload,
)
from election_modeling.ingestion import canonical_poll
from election_modeling.polls import LinearPollObservation, PollAdjustment

W = Electorate(.37, .33, .30)
VALUES = {'republican': (.90, .08), 'democratic': (.08, .90), 'independent': (.55, .40)}


def observation(date='2026-10-01', *, values=VALUES, pollster='Synthetic', n=500, **kwargs):
    return PollObservation.from_party_id_shares(
        values=values, subgroup_sample_sizes=dict.fromkeys(values, n),
        field_date=date, pollster=pollster, **kwargs,
    )


def poll(identifier, date, *, values=VALUES, **kwargs):
    return NormalizedPoll(identifier, 'Synthetic', date, race_id='us_house_generic',
        crosstab=PartyIDCrosstab(values, dict.fromkeys(values, 500)), **kwargs)


def run(polls, *, model=None):
    election = ElectionModel(races={'us_house_generic': model or RaceModel.default(electorate=W)})
    result = PollIngestionPipeline(sources=tuple(StaticPollSource([p]) for p in polls)).run(election)
    return election.races['us_house_generic'], result


def test_party_aliases_are_republican_first():
    row = {'pollster':'Synthetic','field_date':'2026-11-01', 'race_id':'ks_sen'}
    for party in VALUES:
        row.update({f'{party}_rep': 90, f'{party}_dem': 10, f'{party}_n': 500})
    parsed = NormalizedPoll.from_mapping(row)
    assert all(pair == (.9, .1) for pair in parsed.crosstab.values.values())
    model = create_2026_election_model()
    result = PollIngestionPipeline(sources=(StaticPollSource([parsed]),)).run(model)
    assert not result.errors
    assert model.races['ks_sen'].forecast().margin > .5


def test_named_reverse_order_is_canonicalized_for_all_measurements():
    p = NormalizedPoll.from_mapping({
        'poll_id':'reverse', 'pollster':'Synthetic', 'field_date':'2026-10-31',
        'race_id':'ks_sen', 'candidate_a':'Adam Hamilton','candidate_b':'Roger Marshall',
        'republican_a':.1,'republican_b':.9,'republican_n':500,
        'topline_a':.4,'topline_b':.6,'topline_n':1000,
    })
    fixed = canonical_poll(p, 'ks_sen')
    assert fixed.crosstab.values['republican'] == (.9,.1)
    assert fixed.topline.candidate_a_share == .6
    assert fixed.candidate_a == 'Roger Marshall'
    assert p.candidate_a == 'Adam Hamilton'
    with pytest.raises(ValueError, match='conflicting candidate labels'):
        canonical_poll(replace(p, party_named_crosstabs=True), 'ks_sen')
    with pytest.raises(ValueError, match='disagree'):
        canonical_poll(replace(p, candidate_a_party='R'), 'ks_sen')


def test_calendar_time_changes_learning_and_uncertainty():
    changed = dict(VALUES, independent=(.35,.60))
    same, r1 = run([poll('a','2026-10-01'),poll('b','2026-10-01',values=changed)],
                   model=RaceModel.default(electorate=W, survey_margin_sd=0))
    later, r2 = run([poll('a','2026-10-01'),poll('b','2026-11-01',values=changed)],
                    model=RaceModel.default(electorate=W, survey_margin_sd=0))
    assert not r1.errors and not r2.errors
    assert later.filter.state.mean[4] < same.filter.state.mean[4]
    assert later.forecast().polling_variance > same.forecast().polling_variance
    zero, _ = run([poll('a','2026-10-01'),poll('b','2026-11-01',values=changed)],
                  model=RaceModel.default(electorate=W, process_variance=0, survey_margin_sd=0))
    np.testing.assert_allclose(zero.filter.state.mean, same.filter.state.mean)


def test_sources_sort_globally_and_same_survey_is_deduplicated():
    model, result = run([poll('new','2026-11-01'),poll('old','2026-10-01')])
    assert [p.poll_id for p in result.applied] == ['old','new']
    assert model.last_date == '2026-11-01'
    model, result = run([poll('one','2026-10-01'),poll('mirror','2026-10-01',source_url='https://example.com/mirror')])
    assert model.observation_count == 1
    assert result.duplicate_poll_ids == ('one',)


def test_out_of_order_or_failed_updates_do_not_mutate_state():
    model = RaceModel.default(electorate=W)
    model.update(observation('2026-10-15'))
    before = deepcopy(model)
    with pytest.raises(ValueError, match='out-of-order'):
        model.update(observation('2026-10-01'))
    assert model.last_date == before.last_date
    assert model.observation_count == before.observation_count
    np.testing.assert_array_equal(model.filter.joint_mean, before.filter.joint_mean)
    np.testing.assert_array_equal(model.filter.joint_covariance, before.filter.joint_covariance)


def test_forecast_to_election_day_is_nonmutating_and_adds_movement():
    model = RaceModel.default(electorate=W)
    model.update(observation('2026-10-01'))
    current = model.forecast()
    future = model.forecast(target_date='2026-11-03')
    assert future.movement_variance > 0
    assert future.margin_standard_error > current.margin_standard_error
    assert future.forecast_date == '2026-11-03'
    assert model.last_date == '2026-10-01'
    np.testing.assert_array_equal(model.filter.state.covariance, current.state.covariance)


def test_prior_only_races_never_export_forecasts():
    rows = public_forecast_payload(create_2026_election_model())['races']
    assert all(not row['data_available'] for row in rows)
    assert all(row['estimate_type']=='prior_only' and row['margin'] is None for row in rows)
    assert all(row['status']=='unrated' and row['leader']=='unknown' for row in rows)


def test_public_uncertainty_budget_and_dated_observation_tracking():
    election = create_2026_election_model()
    election.update('ks_sen', observation('2026-11-01'))
    row = next(row for row in public_forecast_payload(election)['races'] if row['race_id']=='ks_sen')
    assert row['data_available'] and row['observation_count']==1
    assert row['state_date']=='2026-11-01' and row['forecast_date']=='2026-11-03'
    assert row['turnout_share_sd_points']==1
    components = row['margin_uncertainty_sd_points']
    variance = sum(value**2 for value in components.values())
    assert row['margin_of_error_percent'] == pytest.approx(1.96*np.sqrt(variance), abs=.005)


@pytest.mark.parametrize('margin, status', [(.03, 'lean-republican'), (-.03, 'lean-democratic')])
def test_public_rating_keeps_margin_bucket_when_uncertainty_includes_zero(margin, status):
    shares = ((1 + margin) / 2, (1 - margin) / 2)
    election = create_2026_election_model(initial_mean=shares * 3, shared_margin_sd=.1)
    election.update('ks_sen', observation('2026-11-01', values=dict.fromkeys(VALUES, shares)))
    row = next(row for row in public_forecast_payload(election)['races'] if row['race_id'] == 'ks_sen')
    assert abs(row['margin_percent']) < row['margin_of_error_percent']
    assert row['status'] == status


def test_shared_polling_error_does_not_average_away():
    model = RaceModel.default(electorate=W, process_variance=0,
                              shared_margin_sd=.02,pollster_margin_sd=.01,survey_margin_sd=.01)
    for _ in range(100):
        model.update(observation(n=10000))
    assert np.sqrt(model.forecast().polling_variance) > .023
    independent = RaceModel.default(electorate=W, process_variance=0,
        shared_margin_sd=0,pollster_margin_sd=0,survey_margin_sd=0)
    for _ in range(100):
        independent.update(observation(n=10000))
    assert model.forecast().polling_variance > 100 * independent.forecast().polling_variance


def test_design_effect_uses_effective_subgroup_sample_sizes():
    r1 = observation(design_effect=1).covariance
    r2 = observation(design_effect=2).covariance
    np.testing.assert_allclose(r2, r1*2)
    a = RaceModel.default(electorate=W)
    b = RaceModel.default(electorate=W)
    a.update_topline(candidate_a_share=.55,candidate_b_share=.40,sample_size=1000,design_effect=1)
    b.update_topline(candidate_a_share=.55,candidate_b_share=.40,sample_size=1000,design_effect=2)
    assert b.forecast().polling_variance > a.forecast().polling_variance


def test_turnout_covariance_matches_user_three_sigma_assumption():
    sigma = W.covariance()
    np.testing.assert_allclose(np.sqrt(np.diag(sigma))*3, [.03]*3)
    np.testing.assert_allclose(sigma.sum(axis=0), 0, atol=1e-18)
    assert np.linalg.eigvalsh(sigma).min() > -1e-18
    np.testing.assert_allclose(sigma[0,1]/sigma[0,0], -.5)


def test_bilinear_turnout_variance_matches_independent_monte_carlo():
    model = RaceModel.default(electorate=W, initial_variance=.0001,
        initial_mean=(.9,.08,.08,.9,.52,.45))
    forecast = model.forecast()
    rng = np.random.default_rng(8371)
    weights = rng.multivariate_normal(W.party_vector(), W.covariance(), size=150000)
    support = rng.multivariate_normal(forecast.state.mean, forecast.state.covariance, size=150000)
    margins = np.sum(weights*(support[:,::2]-support[:,1::2]), axis=1)
    assert np.std(margins) == pytest.approx(forecast.margin_standard_error, rel=.015)
    assert np.mean(margins) == pytest.approx(forecast.margin, abs=.0003)


def test_mean_constraints_preserve_nonzero_uncertainty_at_boundaries():
    model = RaceModel.default(electorate=W)
    model.update_topline(candidate_a_share=.99,candidate_b_share=.01,sample_size=100000)
    state = model.filter.state
    assert np.all(state.mean >= 0)
    assert np.all(state.mean.reshape(3,2).sum(axis=1) <= 1)
    assert np.linalg.eigvalsh(state.covariance).min() >= -1e-12
    assert np.diag(state.covariance).min() > 0
    # The constrained covariance and mean both differ from the unconstrained result.
    raw = RaceModel.default(electorate=W)
    raw.filter.clip_support=False
    raw.update_topline(candidate_a_share=.99,candidate_b_share=.01,sample_size=100000)
    assert not np.allclose(state.covariance, raw.filter.state.covariance)


@pytest.mark.parametrize('bad', [np.nan,np.inf,-.01])
def test_invalid_parameters_rejected(bad):
    with pytest.raises(ValueError):
        RaceModel.default(electorate=W, process_variance=bad)
    with pytest.raises(ValueError):
        RaceModel.default(electorate=W, shared_margin_sd=bad)
    with pytest.raises(ValueError):
        Electorate(.37,.33,.30,share_standard_deviation=bad)


def test_invalid_covariance_rejected_not_reported_as_zero_uncertainty():
    p = np.eye(6)*.01
    p[0,1]=p[1,0]=.02
    with pytest.raises(ValueError, match='positive semidefinite'):
        KalmanState(np.ones(6)*.5,p)
    with pytest.raises(ValueError, match='positive semidefinite'):
        PollObservation(np.ones(6)*.5,p)
    with pytest.raises(ValueError, match='positive semidefinite'):
        RaceKalmanFilter(KalmanState(np.ones(6)*.5,np.eye(6)),process_covariance=p)
    with pytest.raises(ValueError, match='symmetric'):
        LinearPollObservation(np.array([.5,.5]),np.array([[1,1],[0,1]]),np.eye(6)[:2])
    p = np.eye(6)
    p[0,0] = np.nan
    with pytest.raises(ValueError):
        KalmanState(np.ones(6)*.5,p)


@pytest.mark.parametrize('n', [0, -1, 1.5, np.nan, np.inf, True])
def test_invalid_sample_sizes_rejected(n):
    with pytest.raises(ValueError):
        observation(n=n)
    with pytest.raises(ValueError):
        RaceModel.default(electorate=W).update_topline(candidate_a_share=.5,candidate_b_share=.5,sample_size=n)


def test_extreme_topline_has_continuity_floor_and_nonfinite_adjustments_fail():
    model = RaceModel.default(electorate=W)
    model.update_topline(candidate_a_share=1,candidate_b_share=0,sample_size=1000)
    assert np.all(np.isfinite(model.filter.state.mean))
    with pytest.raises(ValueError):
        PollAdjustment.from_values([np.nan]*6)
    with pytest.raises(ValueError):
        observation(values={'republican':(np.nan,.1)})
    with pytest.raises(ValueError):
        observation(adjustment=PollAdjustment.from_values([.2,0,0,0,0,0]))


def test_restart_preserves_dates_biases_covariance_and_custom_settings(tmp_path):
    model = RaceModel.default(electorate=W,process_variance=.0001,
                              shared_margin_sd=.03,pollster_margin_sd=.02,survey_margin_sd=.015)
    model.update(observation('2026-10-01'))
    election = ElectionModel({'ks_sen':model})
    path = tmp_path/'model.json'
    save_election_model(election,path)
    restored = load_election_model(path).races['ks_sen']
    assert restored.last_date==model.last_date and restored.observation_count==1
    np.testing.assert_allclose(restored.filter.joint_covariance,model.filter.joint_covariance,atol=1e-15)
    model.update(observation('2026-10-07',values=dict(VALUES,independent=(.4,.5))))
    restored.update(observation('2026-10-07',values=dict(VALUES,independent=(.4,.5))))
    np.testing.assert_allclose(restored.filter.joint_mean,model.filter.joint_mean,atol=1e-12)
    np.testing.assert_allclose(restored.filter.joint_covariance,model.filter.joint_covariance,atol=1e-12)
    assert restored.forecast(target_date='2026-11-03').margin_standard_error == pytest.approx(model.forecast(target_date='2026-11-03').margin_standard_error)
    path.write_text(json.dumps({'races':{}}))
    with pytest.raises(ValueError, match='Legacy snapshot'):
        load_election_model(path)


def test_history_matches_ingestion_including_dates_direction_and_dedup(tmp_path):
    rows = [dict(poll_id='new',pollster='Synthetic',field_date='2026-11-01',race_id='ks_sen',
                 candidate_a='Adam Hamilton',candidate_b='Roger Marshall',topline_a=.4,topline_b=.55,topline_n=1000),
            dict(poll_id='old',pollster='Synthetic',field_date='2026-10-01',race_id='ks_sen',
                 topline_a=.5,topline_b=.45,topline_n=1000)]
    rows.append(dict(rows[0],poll_id='mirror',source_url='https://example.com'))
    path=tmp_path/'polls.json'
    path.write_text(json.dumps(rows))
    election=create_2026_election_model()
    result=PollIngestionPipeline(sources=(StaticPollSource([NormalizedPoll.from_mapping(row) for row in rows]),)).run(election)
    assert not result.errors and len(result.applied)==2
    history=next(row for row in public_race_history_payload(feed_path=path)['races'] if row['race_id']=='ks_sen')
    assert len(history['poll_points'])==2
    assert history['model_points'][-1]['margin']==round(election.races['ks_sen'].forecast().margin,4)


def test_truncated_gaussian_constraint_updates_mean_and_variance():
    mean=np.array([-.05,.45,.2,.7,.45,.45])
    f=RaceKalmanFilter(KalmanState(mean,np.eye(6)*.01))
    # Exact lower-truncated N(-.05,.1^2) moments, independently computed.
    from math import exp, erfc, sqrt, pi
    ratio=exp(-.5*.5**2)/sqrt(2*pi)/(.5*erfc(.5/sqrt(2)))
    assert f.state.mean[0] == pytest.approx(-.05+.1*ratio)
    assert f.state.covariance[0,0] == pytest.approx(.01*(1-ratio*(ratio-.5)))
    assert f.state.mean[1] == .45


def test_randomized_valid_polls_keep_states_and_joint_covariance_valid():
    rng=np.random.default_rng(811)
    model=RaceModel.default(electorate=W)
    for day in range(1,29):
        probabilities=rng.dirichlet([2,2,1],size=3)
        values={party:tuple(row[:2]) for party,row in zip(VALUES,probabilities)}
        model.update(observation(f'2026-10-{day:02}',values=values,pollster=f'Pollster {day%3}',n=1000))
        assert np.all(model.filter.state.mean>=0)
        assert np.all(model.filter.state.mean.reshape(3,2).sum(axis=1)<=1)
        assert np.linalg.eigvalsh(model.filter.joint_covariance).min()>=-1e-12
        assert np.isfinite(model.forecast(target_date='2026-11-03').margin_of_error)


def test_synthetic_interval_coverage_under_declared_error_assumptions():
    # Each independent synthetic election has shared/house/survey errors and
    # turnout uncertainty drawn from the model's stated assumptions. This does
    # not establish coverage on real historical elections.
    rng=np.random.default_rng(92038)
    truth=np.array([[.8,.15],[.15,.8],[.5,.45]])
    covered=0
    for campaign in range(250):
        model=RaceModel.default(electorate=W,process_variance=0)
        shared=rng.normal(0,.02)
        houses=rng.normal(0,.01,size=2)
        for release in range(6):
            bias=shared+houses[release%2]+rng.normal(0,.01)
            probabilities=truth+np.array([.5,-.5])*bias
            values={}
            for party,row in zip(VALUES,probabilities):
                # Declared n=600, effective n=400 with DEFF=1.5.
                counts=rng.multinomial(400,[row[0],row[1],1-row.sum()])
                values[party]=tuple(counts[:2]/400)
            model.update(observation('2026-10-01',values=values,
                pollster=f'Pollster {release%2}',sample_id=str(release),n=600))
        weights=rng.multivariate_normal(W.party_vector(),W.covariance())
        actual_margin=float(weights@(truth[:,0]-truth[:,1]))
        forecast=model.forecast()
        covered += abs(forecast.margin-actual_margin)<=forecast.margin_of_error
    assert .90 <= covered/250 <= .99


def test_percentage_parsing_and_conflicting_aliases():
    row=dict(pollster='Synthetic',field_date='2026-10-31',race_id='ks_sen',
             republican_rep='99%',republican_dem='1%',republican_n=500)
    p=NormalizedPoll.from_mapping(row)
    assert p.crosstab.values['republican']==(.99,.01)
    with pytest.raises(ValueError,match='conflicting share aliases'):
        NormalizedPoll.from_mapping(dict(row,republican_a=.1))
    assert NormalizedPoll.from_mapping(dict(row,sample_id='a')).poll_id != NormalizedPoll.from_mapping(dict(row,sample_id='b')).poll_id


def test_tiny_covariance_roundoff_is_repaired_but_material_negative_variance_is_rejected():
    p=np.eye(6)*.01
    p[-1,-1]=-1e-15
    state=KalmanState(np.array([.8,.15,.15,.8,.5,.45]),p)
    assert np.linalg.eigvalsh(state.covariance).min()>=0
    p[-1,-1]=-.00001
    with pytest.raises(ValueError,match='positive semidefinite'):
        KalmanState(state.mean,p)
