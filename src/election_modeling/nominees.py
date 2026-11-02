"""Verified nominee metadata for modeled races."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Party = Literal["republican", "democratic", "independent"]
NomineeStatus = Literal["nominee", "presumptive_nominee"]


@dataclass(frozen=True)
class Nominee:
    """A major-party nominee or settled candidate for a modeled race."""

    name: str
    party: Party
    status: NomineeStatus
    source_name: str
    source_url: str


@dataclass(frozen=True)
class RaceNominees:
    """Nominee metadata keyed to a race in the 2026 registry."""

    race_id: str
    republican: Nominee | None = None
    democratic: Nominee | None = None
    independent: Nominee | None = None
    last_verified: str = "2026-07-01"
    notes: str | None = None

    @property
    def candidate_b(self) -> Nominee | None:
        """Opponent of the Republican in this two-candidate race."""
        return self.democratic or self.independent


NOMINEES_2026_BY_RACE: dict[str, RaceNominees] = {
    "ne_sen": RaceNominees(
        race_id="ne_sen",
        republican=Nominee(
            name="Pete Ricketts", party="republican", status="nominee",
            source_name="Associated Press Nebraska election guide",
            source_url="https://apnews.com/article/78b5008f5c41597306574eccabec630f",
        ),
        independent=Nominee(
            name="Dan Osborn", party="independent", status="nominee",
            source_name="Associated Press Nebraska election guide",
            source_url="https://apnews.com/article/78b5008f5c41597306574eccabec630f",
        ),
        last_verified="2026-11-01",
        notes="Osborn is independent, not a Democratic nominee. Other minor candidates remain outside the two-candidate model. Nebraska electorate R57/D24/I19 is user-selected.",
    ),
    "mn_gov": RaceNominees(
        race_id="mn_gov",
        republican=Nominee(
            name="Lisa Demuth",
            party="republican",
            status="nominee",
            source_name="Associated Press election guide",
            source_url="https://apnews.com/article/0ad3241b58ecc7fa2ca1693bbd2f4013",
        ),
        democratic=Nominee(
            name="Amy Klobuchar",
            party="democratic",
            status="nominee",
            source_name="Associated Press election guide",
            source_url="https://apnews.com/article/0ad3241b58ecc7fa2ca1693bbd2f4013",
        ),
        last_verified="2026-11-01",
        notes="Minnesota governor added with the governor acquisition; Klobuchar is the DFL nominee. Uses the user's Minnesota electorate.",
    ),
    "mn_sen": RaceNominees(
        race_id="mn_sen",
        republican=Nominee(
            name="Michele Tafoya",
            party="republican",
            status="nominee",
            source_name="Minnesota Secretary of State",
            source_url="https://www.sos.mn.gov/elections-voting/election-results/2026/2026-primary-election-results/",
        ),
        democratic=Nominee(
            name="Peggy Flanagan",
            party="democratic",
            status="nominee",
            source_name="Minnesota Secretary of State",
            source_url="https://www.sos.mn.gov/elections-voting/election-results/2026/2026-primary-election-results/",
        ),
        last_verified="2026-11-01",
        notes="Flanagan is the Democratic-Farmer-Labor nominee; Minnesota Senate added by user request.",
    ),
    "us_house_generic": RaceNominees(
        race_id="us_house_generic",
        republican=Nominee(
            name="Generic Republican",
            party="republican",
            status="presumptive_nominee",
            source_name="Modeled generic congressional ballot",
            source_url="https://adamcohen8.github.io/Election-Filtering/",
        ),
        democratic=Nominee(
            name="Generic Democrat",
            party="democratic",
            status="presumptive_nominee",
            source_name="Modeled generic congressional ballot",
            source_url="https://adamcohen8.github.io/Election-Filtering/",
        ),
        last_verified="2026-07-04",
        notes="National generic congressional ballot model.",
    ),
    "fl_sen": RaceNominees(
        race_id="fl_sen",
        republican=Nominee(
            name="Ashley Moody",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/4e7c37012dae6fdb2427de8d1b222a4c",
        ),
        democratic=Nominee(
            name="Angie Nixon",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/4e7c37012dae6fdb2427de8d1b222a4c",
        ),
        last_verified="2026-11-01",
        notes="Florida special U.S. Senate election nominees from the August 18 primary.",
    ),
    "fl_gov": RaceNominees(
        race_id="fl_gov",
        republican=Nominee(
            name="Byron Donalds",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/4e7c37012dae6fdb2427de8d1b222a4c",
        ),
        democratic=Nominee(
            name="David Jolly",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/4e7c37012dae6fdb2427de8d1b222a4c",
        ),
        last_verified="2026-11-01",
        notes="Florida governor nominees from the August 18 primary.",
    ),
    "nh_sen": RaceNominees(
        race_id="nh_sen",
        republican=Nominee(
            name="John E. Sununu",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/b7e739aba1fe5f0525e55b973000cc1a",
        ),
        democratic=Nominee(
            name="Chris Pappas",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/b7e739aba1fe5f0525e55b973000cc1a",
        ),
        last_verified="2026-11-01",
        notes="New Hampshire Senate nominees from the September 8 primary.",
    ),
    "nh_gov": RaceNominees(
        race_id="nh_gov",
        republican=Nominee(
            name="Kelly Ayotte",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/b7e739aba1fe5f0525e55b973000cc1a",
        ),
        democratic=Nominee(
            name="Cinde Warmington",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/b7e739aba1fe5f0525e55b973000cc1a",
        ),
        last_verified="2026-11-01",
        notes="New Hampshire governor nominees from the September 8 primary.",
    ),
    "ak_sen": RaceNominees(
        race_id="ak_sen",
        republican=Nominee(
            name="Dan Sullivan",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/412ea91b906a29c038b5d2cc6e7b93d1",
        ),
        democratic=Nominee(
            name="Mary Peltola",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/412ea91b906a29c038b5d2cc6e7b93d1",
        ),
        last_verified="2026-11-01",
        notes=(
            "Alaska uses a top-four primary. Sullivan and Peltola advanced "
            "from the August 18, 2026 primary to the general election."
        ),
    ),
    "tx_sen": RaceNominees(
        race_id="tx_sen",
        republican=Nominee(
            name="Ken Paxton",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/04e87ff214dc580d4dc6751644fdc467",
        ),
        democratic=Nominee(
            name="James Talarico",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/04e87ff214dc580d4dc6751644fdc467",
        ),
        last_verified="2026-11-01",
    ),
    "tx_gov": RaceNominees(
        race_id="tx_gov",
        republican=Nominee(
            name="Greg Abbott",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/04e87ff214dc580d4dc6751644fdc467",
        ),
        democratic=Nominee(
            name="Gina Hinojosa",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/04e87ff214dc580d4dc6751644fdc467",
        ),
        last_verified="2026-11-01",
    ),
    "az_gov": RaceNominees(
        race_id="az_gov",
        republican=Nominee(
            name="Andy Biggs",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/42fd6bfa4d9010786e8af5ec9892be95",
        ),
        democratic=Nominee(
            name="Katie Hobbs",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/42fd6bfa4d9010786e8af5ec9892be95",
        ),
        last_verified="2026-11-01",
    ),
    "nc_sen": RaceNominees(
        race_id="nc_sen",
        republican=Nominee(
            name="Michael Whatley",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/5a8ec7df25bf8ee18df535bf8eeb2b0d",
        ),
        democratic=Nominee(
            name="Roy Cooper",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/5a8ec7df25bf8ee18df535bf8eeb2b0d",
        ),
        last_verified="2026-11-01",
    ),
    "ga_sen": RaceNominees(
        race_id="ga_sen",
        republican=Nominee(
            name="Mike Collins",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/e8b4d650269102ad4723a5a162a24cf4",
        ),
        democratic=Nominee(
            name="Jon Ossoff",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/e8b4d650269102ad4723a5a162a24cf4",
        ),
        last_verified="2026-11-01",
    ),
    "ga_gov": RaceNominees(
        race_id="ga_gov",
        republican=Nominee(
            name="Rick Jackson",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/e8b4d650269102ad4723a5a162a24cf4",
        ),
        democratic=Nominee(
            name="Keisha Lance Bottoms",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/e8b4d650269102ad4723a5a162a24cf4",
        ),
        last_verified="2026-11-01",
    ),
    "ia_sen": RaceNominees(
        race_id="ia_sen",
        republican=Nominee(
            name="Ashley Hinson",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/2e005b6badba2d106c43ce5bc25d07fc",
        ),
        democratic=Nominee(
            name="Josh Turek",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/2e005b6badba2d106c43ce5bc25d07fc",
        ),
        last_verified="2026-11-01",
    ),
    "ia_gov": RaceNominees(
        race_id="ia_gov",
        republican=Nominee(
            name="Zach Lahn",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/2e005b6badba2d106c43ce5bc25d07fc",
        ),
        democratic=Nominee(
            name="Rob Sand",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/2e005b6badba2d106c43ce5bc25d07fc",
        ),
        last_verified="2026-11-01",
    ),
    "me_sen": RaceNominees(
        race_id="me_sen",
        republican=Nominee(
            name="Susan Collins",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/0738e23c17299037479d9807d7f7bb62",
        ),
        democratic=Nominee(
            name="Troy Jackson",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/0738e23c17299037479d9807d7f7bb62",
        ),
        last_verified="2026-11-01",
        notes=(
            "Troy Jackson was selected at the July replacement convention after Graham Platner withdrew."
        ),
    ),
    "mi_sen": RaceNominees(
        race_id="mi_sen",
        republican=Nominee(
            name="Mike Rogers",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/ef0c10050672e639203efdc64d2b59f5",
        ),
        democratic=Nominee(
            name="Abdul El-Sayed",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/ef0c10050672e639203efdc64d2b59f5",
        ),
        last_verified="2026-11-01",
        notes="Michigan U.S. Senate nominees updated after the August 4, 2026 primary.",
    ),
    "mi_gov": RaceNominees(
        race_id="mi_gov",
        republican=Nominee(
            name="John James",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/ef0c10050672e639203efdc64d2b59f5",
        ),
        democratic=Nominee(
            name="Jocelyn Benson",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/ef0c10050672e639203efdc64d2b59f5",
        ),
        last_verified="2026-11-01",
        notes="Michigan governor nominees updated after the August 4, 2026 primary.",
    ),
    "oh_sen": RaceNominees(
        race_id="oh_sen",
        republican=Nominee(
            name="Jon Husted",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/edfb7e19f15c21bf6d1a1a785042c977",
        ),
        democratic=Nominee(
            name="Sherrod Brown",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/edfb7e19f15c21bf6d1a1a785042c977",
        ),
        last_verified="2026-11-01",
    ),
    "oh_gov": RaceNominees(
        race_id="oh_gov",
        republican=Nominee(
            name="Vivek Ramaswamy",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/edfb7e19f15c21bf6d1a1a785042c977",
        ),
        democratic=Nominee(
            name="Amy Acton",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/edfb7e19f15c21bf6d1a1a785042c977",
        ),
        last_verified="2026-11-01",
    ),
    "pa_gov": RaceNominees(
        race_id="pa_gov",
        republican=Nominee(
            name="Stacy Garrity",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/2b3e8b883d526a59c979a09581cb09f5",
        ),
        democratic=Nominee(
            name="Josh Shapiro",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/2b3e8b883d526a59c979a09581cb09f5",
        ),
        last_verified="2026-11-01",
    ),
    "wi_gov": RaceNominees(
        race_id="wi_gov",
        republican=Nominee(
            name="Tom Tiffany",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/b6fc54862bb0364082fd60a6b02b59fd",
        ),
        democratic=Nominee(
            name="David Crowley",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/b6fc54862bb0364082fd60a6b02b59fd",
        ),
        last_verified="2026-11-01",
        notes="Wisconsin governor nominees updated after the August 11, 2026 primary.",
    ),
    "ks_sen": RaceNominees(
        race_id="ks_sen",
        republican=Nominee(
            name="Roger Marshall",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/eef95708ad9460def594935ac301c4f5",
        ),
        democratic=Nominee(
            name="Adam Hamilton",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/eef95708ad9460def594935ac301c4f5",
        ),
        last_verified="2026-11-01",
    ),
    "ks_gov": RaceNominees(
        race_id="ks_gov",
        republican=Nominee(
            name="Ty Masterson",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/eef95708ad9460def594935ac301c4f5",
        ),
        democratic=Nominee(
            name="Cindy Holscher",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/eef95708ad9460def594935ac301c4f5",
        ),
        last_verified="2026-11-01",
    ),
    "me_gov": RaceNominees(
        race_id="me_gov",
        republican=Nominee(
            name="Bobby Charles",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/0738e23c17299037479d9807d7f7bb62",
        ),
        democratic=Nominee(
            name="Hannah Pingree",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/0738e23c17299037479d9807d7f7bb62",
        ),
        last_verified="2026-11-01",
    ),
    "nv_gov": RaceNominees(
        race_id="nv_gov",
        republican=Nominee(
            name="Joe Lombardo",
            party="republican",
            status="nominee",
            source_name="MultiState Elections",
            source_url="https://www.multistate.us/elections/governor-race/nevada-2026",
        ),
        democratic=Nominee(
            name="Aaron Ford",
            party="democratic",
            status="nominee",
            source_name="MultiState Elections",
            source_url="https://www.multistate.us/elections/governor-race/nevada-2026",
        ),
        last_verified="2026-11-01",
    ),
}
