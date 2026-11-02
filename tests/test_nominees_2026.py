from election_modeling import (
    NOMINEES_2026_BY_RACE,
    RACES_2026,
    NormalizedPoll,
    create_2026_election_model,
    ensure_2026_races,
    public_forecast_payload,
)
from election_modeling.cycles import TURNOUT_2024_PREDICTION_ELECTORATES_BY_STATE
from election_modeling.ingestion import RaceClassifier


def test_all_modeled_2026_races_have_two_candidates() -> None:
    missing = {
        race.race_id
        for race in RACES_2026
        if (nominees := NOMINEES_2026_BY_RACE.get(race.race_id)) is None
        or nominees.republican is None
        or nominees.candidate_b is None
    }

    assert missing == set()


def test_nominees_match_november_2026_general_election_audit() -> None:
    expected = {
        "ak_sen": ("Dan Sullivan", "Mary Peltola"),
        "az_gov": ("Andy Biggs", "Katie Hobbs"),
        "fl_sen": ("Ashley Moody", "Angie Nixon"),
        "fl_gov": ("Byron Donalds", "David Jolly"),
        "ga_sen": ("Mike Collins", "Jon Ossoff"),
        "ga_gov": ("Rick Jackson", "Keisha Lance Bottoms"),
        "ia_sen": ("Ashley Hinson", "Josh Turek"),
        "ia_gov": ("Zach Lahn", "Rob Sand"),
        "ks_sen": ("Roger Marshall", "Adam Hamilton"),
        "ks_gov": ("Ty Masterson", "Cindy Holscher"),
        "me_sen": ("Susan Collins", "Troy Jackson"),
        "me_gov": ("Bobby Charles", "Hannah Pingree"),
        "mi_sen": ("Mike Rogers", "Abdul El-Sayed"),
        "mi_gov": ("John James", "Jocelyn Benson"),
        "mn_sen": ("Michele Tafoya", "Peggy Flanagan"),
        "mn_gov": ("Lisa Demuth", "Amy Klobuchar"),
        "ne_sen": ("Pete Ricketts", "Dan Osborn"),
        "nv_gov": ("Joe Lombardo", "Aaron Ford"),
        "nh_sen": ("John E. Sununu", "Chris Pappas"),
        "nh_gov": ("Kelly Ayotte", "Cinde Warmington"),
        "nc_sen": ("Michael Whatley", "Roy Cooper"),
        "oh_sen": ("Jon Husted", "Sherrod Brown"),
        "oh_gov": ("Vivek Ramaswamy", "Amy Acton"),
        "pa_gov": ("Stacy Garrity", "Josh Shapiro"),
        "tx_sen": ("Ken Paxton", "James Talarico"),
        "tx_gov": ("Greg Abbott", "Gina Hinojosa"),
        "wi_gov": ("Tom Tiffany", "David Crowley"),
    }

    assert set(NOMINEES_2026_BY_RACE) == set(expected) | {"us_house_generic"}
    for race_id, (republican, democratic) in expected.items():
        nominees = NOMINEES_2026_BY_RACE[race_id]
        assert nominees.republican is not None
        assert nominees.candidate_b is not None
        assert nominees.republican.name == republican
        assert nominees.candidate_b.name == democratic
        assert nominees.republican.status == "nominee"
        assert nominees.candidate_b.status == "nominee"
        assert nominees.republican.party == "republican"
        assert nominees.candidate_b.party == ("independent" if race_id == "ne_sen" else "democratic")
        assert nominees.last_verified == "2026-11-01"


def test_race_coverage_matches_included_states_and_2026_elections() -> None:
    # Checked against the 2026 election calendar; Alaska governor is excluded
    # by the user's explicit instruction because it has multiple GOP finalists.
    expected = {
        "Alaska": {"senate"},
        "Arizona": {"governor"},
        "Florida": {"senate", "governor"},
        "Georgia": {"senate", "governor"},
        "Iowa": {"senate", "governor"},
        "Kansas": {"senate", "governor"},
        "Maine": {"senate", "governor"},
        "Michigan": {"senate", "governor"},
        "Minnesota": {"senate", "governor"},
        "Nevada": {"governor"},
        "Nebraska": {"senate"},
        "New Hampshire": {"senate", "governor"},
        "North Carolina": {"senate"},
        "Ohio": {"senate", "governor"},
        "Pennsylvania": {"governor"},
        "Texas": {"senate", "governor"},
        "Wisconsin": {"governor"},
        "United States": {"generic_ballot"},
    }
    assert set(expected) == set(TURNOUT_2024_PREDICTION_ELECTORATES_BY_STATE)
    assert {(race.state, race.office) for race in RACES_2026} == {
        (state, office) for state, offices in expected.items() for office in offices
    }


def test_added_races_use_state_weights_classify_and_export() -> None:
    election = create_2026_election_model()
    added = {"ks_sen", "ks_gov", "me_gov", "nv_gov", "mn_sen", "mn_gov", "ne_sen"}
    # Exercise upgrading an older in-memory model as well as a fresh model.
    for race_id in added:
        del election.races[race_id]
    ensure_2026_races(election)
    payload = {race["race_id"]: race for race in public_forecast_payload(election)["races"]}

    for race in RACES_2026:
        if race.race_id not in added:
            continue
        assert election.races[race.race_id].electorate == (
            TURNOUT_2024_PREDICTION_ELECTORATES_BY_STATE[race.state]
        )
        poll = NormalizedPoll(
            poll_id=f"test-{race.race_id}",
            pollster="Example Polling",
            field_date="2026-11-01",
            state=race.state,
            office=race.office,
        )
        assert RaceClassifier().classify(poll) == race.race_id
        nominees = NOMINEES_2026_BY_RACE[race.race_id]
        assert payload[race.race_id]["candidate_a_name"] == nominees.republican.name
        assert payload[race.race_id]["candidate_b_name"] == nominees.candidate_b.name
