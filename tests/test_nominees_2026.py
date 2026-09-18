from election_modeling import NOMINEES_2026_BY_RACE, RACES_2026


def test_all_modeled_2026_races_have_major_party_candidates() -> None:
    missing = {
        race.race_id
        for race in RACES_2026
        if (nominees := NOMINEES_2026_BY_RACE.get(race.race_id)) is None
        or nominees.republican is None
        or nominees.democratic is None
    }

    assert missing == set()


def test_florida_and_new_hampshire_nominees_match_primary_results() -> None:
    expected = {
        "fl_sen": ("Ashley Moody", "Angie Nixon"),
        "fl_gov": ("Byron Donalds", "David Jolly"),
        "nh_sen": ("John E. Sununu", "Chris Pappas"),
        "nh_gov": ("Kelly Ayotte", "Cinde Warmington"),
    }

    for race_id, (republican, democratic) in expected.items():
        nominees = NOMINEES_2026_BY_RACE[race_id]
        assert nominees.republican is not None
        assert nominees.democratic is not None
        assert nominees.republican.name == republican
        assert nominees.democratic.name == democratic
        assert nominees.republican.status == "nominee"
        assert nominees.democratic.status == "nominee"
