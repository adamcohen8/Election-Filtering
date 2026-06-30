import numpy as np

from election_modeling import (
    ElectionModel,
    Electorate,
    IngestionLedger,
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
    export_public_forecasts,
    load_election_model,
    public_forecast_payload,
    run_2026_poll_io,
    save_election_model,
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


def test_election_model_forecasts_multiple_races() -> None:
    election = ElectionModel.from_electorates(
        {
            "az_sen": Electorate(republican=0.36, democratic=0.34, independent=0.30),
            "nc_gov": Electorate(republican=0.37, democratic=0.33, independent=0.30),
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

    assert set(forecasts) == {"az_sen", "nc_gov"}
    assert forecasts["az_sen"].margin != forecasts["nc_gov"].margin


def test_2026_registry_contains_initial_senate_and_governor_races() -> None:
    race_ids = {race.race_id for race in RACES_2026}

    assert len(RACES_2026) == 20
    assert {"fl_sen", "tx_sen", "ga_sen", "nc_gov", "wi_gov"} <= race_ids
    assert RACES_2026_BY_ID["ga_gov"].state == "Georgia"


def test_create_2026_election_model_preloads_all_races() -> None:
    election = create_2026_election_model(
        electorates={
            "fl_sen": Electorate(republican=0.38, democratic=0.32, independent=0.30),
        }
    )

    assert set(election.races) == set(RACES_2026_BY_ID)
    assert election.races["fl_sen"].electorate.republican == 0.38
    assert election.races["tx_sen"].electorate.republican == 1.0 / 3.0


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
        poll_id="duplicate-nc-gov",
        pollster="Example Polling",
        field_date="2026-04-01",
        race_id="nc_gov",
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
    assert second.duplicate_poll_ids == ("duplicate-nc-gov",)


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
        poll_id="automation-nc-gov",
        pollster="Example Polling",
        field_date="2026-06-15",
        race_id="nc_gov",
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
    assert second.result.duplicate_poll_ids == ("automation-nc-gov",)
    assert snapshot_path.exists()
    assert ledger_path.exists()


def test_public_forecast_payload_exports_race_statuses() -> None:
    election = create_2026_election_model()

    payload = public_forecast_payload(election)

    race = next(race for race in payload["races"] if race["race_id"] == "fl_sen")
    assert race["office"] == "senate"
    assert race["state_code"] == "FL"
    assert race["status"] in {"republican", "democratic", "tossup"}


def test_export_public_forecasts_writes_static_json(tmp_path) -> None:
    output_path = tmp_path / "forecasts.json"

    payload = export_public_forecasts(
        snapshot_path=tmp_path / "missing-model.json",
        output_path=output_path,
    )

    assert output_path.exists()
    assert len(payload["races"]) == 20
