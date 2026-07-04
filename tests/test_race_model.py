from pathlib import Path

import numpy as np
from election_modeling.public import PublicExportOptions, _status_for_margin

from election_modeling import (
    ElectionModel,
    Electorate,
    IngestionLedger,
    NOMINEES_2026_BY_RACE,
    NormalizedPoll,
    PartyIDCrosstab,
    PollAdjustment,
    PollIngestionPipeline,
    PollObservation,
    RACES_2026,
    RACES_2026_BY_ID,
    RaceModel,
    StaticPollSource,
    create_2026_election_model,
    ensure_2026_races,
    export_public_forecasts,
    load_election_model,
    public_forecast_payload,
    run_2026_poll_io,
    save_election_model,
    ToplineResult,
)


def test_poll_update_moves_forecast_toward_observation() -> None:
    model = RaceModel.default(
        electorate=Electorate(republican=0.35, democratic=0.35, independent=0.30),
    )

    before = model.forecast().margin
    observation = PollObservation.from_party_id_shares(
        values={
            "republican": (0.90, 0.07),
            "democratic": (0.07, 0.90),
            "independent": (0.55, 0.38),
        },
        subgroup_sample_sizes={
            "republican": 400,
            "democratic": 420,
            "independent": 300,
        },
    )

    model.update(observation)
    after = model.forecast().margin

    assert after > before


def test_margin_uncertainty_shrinks_after_precise_poll() -> None:
    model = RaceModel.default(
        electorate=Electorate(republican=0.36, democratic=0.34, independent=0.30),
        initial_variance=0.10,
    )

    before = model.forecast().margin_standard_error
    observation = PollObservation.from_party_id_shares(
        values={
            "republican": (0.88, 0.09),
            "democratic": (0.08, 0.89),
            "independent": (0.49, 0.45),
        },
        subgroup_sample_sizes={
            "republican": 2_000,
            "democratic": 2_000,
            "independent": 2_000,
        },
    )

    model.update(observation)
    after = model.forecast().margin_standard_error

    assert after < before


def test_poll_adjustment_unbiases_state_cells() -> None:
    model = RaceModel.default(
        electorate=Electorate(republican=0.33, democratic=0.34, independent=0.33),
        initial_mean=(0.50, 0.50, 0.50, 0.50, 0.50, 0.50),
        initial_variance=0.01,
    )
    adjustment = PollAdjustment.from_values([0, 0, 0, 0, 0.05, -0.05])
    observation = PollObservation.from_party_id_shares(
        values={
            "independent": (0.45, 0.45),
        },
        subgroup_sample_sizes={"independent": 500},
        adjustment=adjustment,
    )

    model.update(observation)

    assert model.filter.state.mean[4] > model.filter.state.mean[5]


def test_missing_party_id_cells_are_ignored() -> None:
    model = RaceModel.default(
        electorate=Electorate(republican=0.36, democratic=0.34, independent=0.30),
    )
    prior_republican = model.filter.state.mean[:2].copy()
    observation = PollObservation.from_party_id_shares(
        values={"independent": (0.60, 0.35)},
        subgroup_sample_sizes={"independent": 250},
    )

    model.update(observation)

    np.testing.assert_allclose(model.filter.state.mean[:2], prior_republican)


def test_topline_update_moves_weighted_forecast() -> None:
    model = RaceModel.default(
        electorate=Electorate(republican=0.36, democratic=0.34, independent=0.30),
    )

    before = model.forecast().margin
    model.update_topline(
        candidate_a_share=0.54,
        candidate_b_share=0.42,
        sample_size=1_000,
    )
    after = model.forecast().margin

    assert after > before


def test_election_model_forecasts_multiple_races() -> None:
    election = ElectionModel.from_electorates(
        {
            "az_sen": Electorate(republican=0.36, democratic=0.34, independent=0.30),
            "pa_gov": Electorate(republican=0.37, democratic=0.33, independent=0.30),
        }
    )

    observation = PollObservation.from_party_id_shares(
        values={
            "republican": (0.88, 0.08),
            "democratic": (0.07, 0.90),
            "independent": (0.52, 0.41),
        },
        subgroup_sample_sizes={
            "republican": 500,
            "democratic": 500,
            "independent": 400,
        },
    )

    election.update("az_sen", observation)
    forecasts = election.forecast_all()

    assert set(forecasts) == {"az_sen", "pa_gov"}
    assert forecasts["az_sen"].margin != forecasts["pa_gov"].margin


def test_2026_registry_contains_initial_senate_and_governor_races() -> None:
    race_ids = {race.race_id for race in RACES_2026}

    assert len(RACES_2026) == 21
    assert {"fl_sen", "tx_sen", "ga_sen", "me_sen", "pa_gov", "wi_gov", "us_house_generic"} <= race_ids
    assert "nc_gov" not in race_ids
    assert RACES_2026_BY_ID["ga_gov"].state == "Georgia"
    assert RACES_2026_BY_ID["me_sen"].state == "Maine"
    assert RACES_2026_BY_ID["us_house_generic"].office == "generic_ballot"
    assert RACES_2026_BY_ID["us_house_generic"].state == "United States"


def test_2026_nominee_registry_tracks_concluded_primaries() -> None:
    assert NOMINEES_2026_BY_RACE["tx_sen"].republican.name == "Ken Paxton"
    assert NOMINEES_2026_BY_RACE["nc_sen"].democratic.name == "Roy Cooper"
    assert NOMINEES_2026_BY_RACE["ga_gov"].democratic.name == "Keisha Lance Bottoms"
    assert "nc_gov" not in NOMINEES_2026_BY_RACE


def test_create_2026_election_model_preloads_all_races() -> None:
    election = create_2026_election_model(
        electorates={
            "fl_sen": Electorate(republican=0.38, democratic=0.32, independent=0.30),
        }
    )

    assert set(election.races) == set(RACES_2026_BY_ID)
    assert "us_house_generic" in election.races
    assert election.races["fl_sen"].electorate.republican == 0.38
    assert election.races["tx_sen"].electorate.republican == 0.41
    assert election.races["tx_sen"].electorate.democratic == 0.30
    assert election.races["tx_sen"].electorate.independent == 0.29
    assert election.races["ia_sen"].electorate.republican == 36.0 / 101.0
    assert election.races["ia_sen"].electorate.democratic == 26.0 / 101.0
    assert election.races["ia_sen"].electorate.independent == 39.0 / 101.0
    assert election.races["ak_sen"].electorate.republican == 1.0 / 3.0
    assert election.races["me_sen"].electorate.republican == 0.233
    assert election.races["me_sen"].electorate.democratic == 0.275
    assert election.races["me_sen"].electorate.independent == 0.492
    assert election.races["us_house_generic"].electorate.republican == 1.0 / 3.0


def test_ensure_2026_races_adds_generic_ballot_to_existing_snapshot_model() -> None:
    election = ElectionModel.from_electorates(
        {"fl_sen": Electorate(republican=0.38, democratic=0.32, independent=0.30)}
    )

    ensure_2026_races(election)

    assert set(election.races) == set(RACES_2026_BY_ID)
    assert election.races["fl_sen"].electorate.republican == 0.38
    assert "us_house_generic" in election.races


def test_ingestion_pipeline_classifies_and_updates_race() -> None:
    election = create_2026_election_model()
    before = election.forecast("fl_sen").margin
    poll = NormalizedPoll(
        poll_id="example-fl-sen",
        pollster="Example Polling",
        field_date="2026-03-15",
        state="Florida",
        office="senate",
        text="Florida Senate general election",
        crosstab=PartyIDCrosstab(
            values={
                "republican": (0.88, 0.08),
                "democratic": (0.07, 0.90),
                "independent": (0.55, 0.38),
            },
            subgroup_sample_sizes={
                "republican": 400,
                "democratic": 400,
                "independent": 300,
            },
        ),
    )
    pipeline = PollIngestionPipeline(
        sources=(StaticPollSource([poll]),),
        ledger=IngestionLedger(),
    )

    result = pipeline.run(election)

    assert result.errors == ()
    assert result.applied[0].race_id == "fl_sen"
    assert election.forecast("fl_sen").margin > before


def test_ingestion_pipeline_skips_duplicate_poll_ids() -> None:
    election = create_2026_election_model()
    poll = NormalizedPoll(
        poll_id="duplicate-nc-sen",
        pollster="Example Polling",
        field_date="2026-04-01",
        race_id="nc_sen",
        crosstab=PartyIDCrosstab(
            values={"independent": (0.60, 0.35)},
            subgroup_sample_sizes={"independent": 250},
        ),
    )
    pipeline = PollIngestionPipeline(
        sources=(StaticPollSource([poll]),),
        ledger=IngestionLedger(),
    )

    first = pipeline.run(election)
    second = pipeline.run(election)

    assert len(first.applied) == 1
    assert second.applied == ()
    assert second.duplicate_poll_ids == ("duplicate-nc-sen",)


def test_ingestion_pipeline_applies_topline_poll() -> None:
    election = create_2026_election_model()
    before = election.forecast("oh_sen").margin
    poll = NormalizedPoll(
        poll_id="topline-oh-sen",
        pollster="Example Polling",
        field_date="2026-04-15",
        race_id="oh_sen",
        candidate_a="Jon Husted",
        candidate_b="Sherrod Brown",
        topline=ToplineResult(
            candidate_a_share=0.52,
            candidate_b_share=0.43,
            sample_size=800,
        ),
    )
    pipeline = PollIngestionPipeline(
        sources=(StaticPollSource([poll]),),
        ledger=IngestionLedger(),
    )

    result = pipeline.run(election)

    assert result.errors == ()
    assert result.applied[0].race_id == "oh_sen"
    assert election.forecast("oh_sen").margin > before


def test_normalized_poll_from_mapping_parses_wide_crosstab_row() -> None:
    poll = NormalizedPoll.from_mapping(
        {
            "pollster": "Example Polling",
            "field_date": "2026-05-01",
            "state": "Georgia",
            "office": "Governor",
            "republican_a": "12%",
            "republican_b": "84%",
            "republican_n": "400",
            "democratic_a": "91",
            "democratic_b": "6",
            "democratic_n": "410",
            "independent_a": "48",
            "independent_b": "45",
            "independent_n": "300",
        }
    )

    assert poll.race_id is None
    assert poll.office == "governor"
    assert poll.crosstab.values["democratic"] == (0.91, 0.06)


def test_normalized_poll_from_mapping_parses_topline_row() -> None:
    poll = NormalizedPoll.from_mapping(
        {
            "pollster": "Example Polling",
            "field_date": "2026-04-09",
            "race_id": "ga_sen",
            "candidate_a": "Mike Collins",
            "candidate_b": "Jon Ossoff",
            "topline_a": "44%",
            "topline_b": "51%",
            "topline_n": "407",
        }
    )

    assert poll.crosstab is None
    assert poll.topline.candidate_a_share == 0.44
    assert poll.topline.candidate_b_share == 0.51
    assert poll.topline.sample_size == 407


def test_generic_ballot_poll_classifies_by_race_id_and_office_terms() -> None:
    election = create_2026_election_model()
    poll = NormalizedPoll.from_mapping(
        {
            "pollster": "Example Polling",
            "field_date": "2026-06-15",
            "office": "generic congressional ballot",
            "text": "National generic congressional ballot",
            "republican_a": "91",
            "republican_b": "5",
            "republican_n": "330",
            "democratic_a": "4",
            "democratic_b": "92",
            "democratic_n": "340",
            "independent_a": "47",
            "independent_b": "41",
            "independent_n": "330",
        }
    )
    pipeline = PollIngestionPipeline(
        sources=(StaticPollSource([poll]),),
        ledger=IngestionLedger(),
    )

    result = pipeline.run(election)

    assert result.errors == ()
    assert result.applied[0].race_id == "us_house_generic"
    assert election.forecast("us_house_generic").margin > 0


def test_election_model_snapshot_round_trips(tmp_path) -> None:
    election = create_2026_election_model()
    poll = NormalizedPoll(
        poll_id="snapshot-fl-sen",
        pollster="Example Polling",
        field_date="2026-06-01",
        race_id="fl_sen",
        crosstab=PartyIDCrosstab(
            values={"independent": (0.58, 0.36)},
            subgroup_sample_sizes={"independent": 350},
        ),
    )
    PollIngestionPipeline(
        sources=(StaticPollSource([poll]),),
        ledger=IngestionLedger(),
    ).run(election)
    snapshot_path = tmp_path / "model.json"

    save_election_model(election, snapshot_path)
    restored = load_election_model(snapshot_path)

    np.testing.assert_allclose(
        restored.races["fl_sen"].filter.state.mean,
        election.races["fl_sen"].filter.state.mean,
    )


def test_run_2026_poll_io_persists_model_and_ledger(tmp_path) -> None:
    poll = NormalizedPoll(
        poll_id="automation-nc-sen",
        pollster="Example Polling",
        field_date="2026-06-15",
        race_id="nc_sen",
        crosstab=PartyIDCrosstab(
            values={"independent": (0.62, 0.31)},
            subgroup_sample_sizes={"independent": 300},
        ),
    )
    snapshot_path = tmp_path / "model.json"
    ledger_path = tmp_path / "seen.json"

    first = run_2026_poll_io(
        custom_sources=(StaticPollSource([poll]),),
        snapshot_path=snapshot_path,
        ledger_path=ledger_path,
    )
    second = run_2026_poll_io(
        custom_sources=(StaticPollSource([poll]),),
        snapshot_path=snapshot_path,
        ledger_path=ledger_path,
    )

    assert len(first.result.applied) == 1
    assert second.result.applied == ()
    assert second.result.duplicate_poll_ids == ("automation-nc-sen",)
    assert snapshot_path.exists()
    assert ledger_path.exists()


def test_public_forecast_payload_exports_race_statuses() -> None:
    election = create_2026_election_model()

    payload = public_forecast_payload(election)

    race = next(race for race in payload["races"] if race["race_id"] == "fl_sen")
    assert race["office"] == "senate"
    assert race["state_code"] == "FL"
    assert race["status"] in {
        "tossup",
        "lean-republican",
        "likely-republican",
        "safe-republican",
        "lean-democratic",
        "likely-democratic",
        "safe-democratic",
    }

    texas = next(race for race in payload["races"] if race["race_id"] == "tx_sen")
    assert texas["candidate_a_name"] == "Ken Paxton"
    assert texas["candidate_b_name"] == "James Talarico"
    assert texas["nominee_last_verified"] == "2026-07-01"

    generic = next(race for race in payload["races"] if race["race_id"] == "us_house_generic")
    assert generic["office"] == "generic_ballot"
    assert generic["state"] == "United States"
    assert generic["state_code"] == "US"
    assert generic["candidate_a_name"] == "Generic Republican"
    assert generic["candidate_b_name"] == "Generic Democrat"


def test_public_status_uses_margin_buckets() -> None:
    options = PublicExportOptions()

    assert _status_for_margin(margin=0.0199, leader="republican", options=options) == "tossup"
    assert _status_for_margin(margin=0.02, leader="republican", options=options) == "lean-republican"
    assert _status_for_margin(margin=-0.0499, leader="democratic", options=options) == "lean-democratic"
    assert _status_for_margin(margin=0.05, leader="republican", options=options) == "likely-republican"
    assert _status_for_margin(margin=-0.0799, leader="democratic", options=options) == "likely-democratic"
    assert _status_for_margin(margin=0.08, leader="republican", options=options) == "safe-republican"


def test_public_map_party_fallback_does_not_override_rating_buckets() -> None:
    css = (Path(__file__).resolve().parents[1] / "docs" / "styles.css").read_text()

    assert ".state-shape.republican:not(.tossup):not(.lean-republican):not(.likely-republican):not(.safe-republican)" in css
    assert ".state-shape.democratic:not(.tossup):not(.lean-democratic):not(.likely-democratic):not(.safe-democratic)" in css


def test_export_public_forecasts_writes_static_json(tmp_path) -> None:
    output_path = tmp_path / "forecasts.json"

    payload = export_public_forecasts(
        snapshot_path=tmp_path / "missing-model.json",
        output_path=output_path,
    )

    assert output_path.exists()
    assert len(payload["races"]) == 21
