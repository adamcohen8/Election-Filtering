"""Verified nominee metadata for modeled races."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Party = Literal["republican", "democratic"]
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
    last_verified: str = "2026-07-01"
    notes: str | None = None


NOMINEES_2026_BY_RACE: dict[str, RaceNominees] = {
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
    "ak_sen": RaceNominees(
        race_id="ak_sen",
        republican=Nominee(
            name="Dan Sullivan",
            party="republican",
            status="presumptive_nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/alaska-primary-senate-sullivan-peltola-congress-401f3d62876f44ee5e78c11c51be136a",
        ),
        democratic=Nominee(
            name="Mary Peltola",
            party="democratic",
            status="presumptive_nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/alaska-primary-senate-sullivan-peltola-congress-401f3d62876f44ee5e78c11c51be136a",
        ),
        last_verified="2026-08-18",
        notes=(
            "Alaska uses a top-four primary. Tracked as the public Sullivan/Peltola "
            "matchup pending final general-election qualification after the "
            "August 18, 2026 primary."
        ),
    ),
    "tx_sen": RaceNominees(
        race_id="tx_sen",
        republican=Nominee(
            name="Ken Paxton",
            party="republican",
            status="nominee",
            source_name="The Daily Beast",
            source_url="https://www.thedailybeast.com/bombshell-texas-senate-race-poll-delivers-dire-warning-for-trump-with-paxton-and-talarico-tied/",
        ),
        democratic=Nominee(
            name="James Talarico",
            party="democratic",
            status="nominee",
            source_name="Houston Chronicle",
            source_url="https://www.houstonchronicle.com/politics/texas-take/article/talarico-black-voters-democrat-convention-22322732.php",
        ),
    ),
    "tx_gov": RaceNominees(
        race_id="tx_gov",
        republican=Nominee(
            name="Greg Abbott",
            party="republican",
            status="nominee",
            source_name="Houston Chronicle",
            source_url="https://www.houstonchronicle.com/politics/election/2026/article/governor-primary-results-21329304.php",
        ),
        democratic=Nominee(
            name="Gina Hinojosa",
            party="democratic",
            status="nominee",
            source_name="Houston Chronicle",
            source_url="https://www.houstonchronicle.com/politics/election/2026/article/governor-primary-results-21329304.php",
        ),
    ),
    "az_gov": RaceNominees(
        race_id="az_gov",
        republican=Nominee(
            name="Andy Biggs",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://abcnews.com/US/wireStory/andy-biggs-wins-republican-nomination-challenge-democrat-katie-134938616",
        ),
        democratic=Nominee(
            name="Katie Hobbs",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://abcnews.com/US/wireStory/andy-biggs-wins-republican-nomination-challenge-democrat-katie-134938616",
        ),
        last_verified="2026-08-08",
    ),
    "nc_sen": RaceNominees(
        race_id="nc_sen",
        republican=Nominee(
            name="Michael Whatley",
            party="republican",
            status="nominee",
            source_name="2026 United States Senate election in North Carolina",
            source_url="https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_North_Carolina",
        ),
        democratic=Nominee(
            name="Roy Cooper",
            party="democratic",
            status="nominee",
            source_name="2026 United States Senate election in North Carolina",
            source_url="https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_North_Carolina",
        ),
    ),
    "ga_sen": RaceNominees(
        race_id="ga_sen",
        republican=Nominee(
            name="Mike Collins",
            party="republican",
            status="nominee",
            source_name="Axios Atlanta",
            source_url="https://www.axios.com/local/atlanta/2026/06/17/georgia-primary-runoff-elections-mike-collins-derek-dooley",
        ),
        democratic=Nominee(
            name="Jon Ossoff",
            party="democratic",
            status="nominee",
            source_name="Axios Atlanta",
            source_url="https://www.axios.com/local/atlanta/2026/06/17/georgia-primary-runoff-elections-mike-collins-derek-dooley",
        ),
    ),
    "ga_gov": RaceNominees(
        race_id="ga_gov",
        republican=Nominee(
            name="Rick Jackson",
            party="republican",
            status="nominee",
            source_name="Axios Atlanta",
            source_url="https://www.axios.com/local/atlanta/2026/06/17/georgia-governor-republican-primary-runoff-results",
        ),
        democratic=Nominee(
            name="Keisha Lance Bottoms",
            party="democratic",
            status="nominee",
            source_name="Axios Atlanta",
            source_url="https://www.axios.com/local/atlanta/2026/06/17/georgia-governor-republican-primary-runoff-results",
        ),
    ),
    "ia_sen": RaceNominees(
        race_id="ia_sen",
        republican=Nominee(
            name="Ashley Hinson",
            party="republican",
            status="nominee",
            source_name="The Guardian",
            source_url="https://www.theguardian.com/us-news/2026/jun/02/iowa-primary-election-results",
        ),
        democratic=Nominee(
            name="Josh Turek",
            party="democratic",
            status="nominee",
            source_name="The Guardian",
            source_url="https://www.theguardian.com/us-news/2026/jun/02/iowa-primary-election-results",
        ),
    ),
    "ia_gov": RaceNominees(
        race_id="ia_gov",
        republican=Nominee(
            name="Zach Lahn",
            party="republican",
            status="nominee",
            source_name="The Guardian",
            source_url="https://www.theguardian.com/us-news/2026/jun/02/iowa-primary-election-results",
        ),
        democratic=Nominee(
            name="Rob Sand",
            party="democratic",
            status="nominee",
            source_name="The Guardian",
            source_url="https://www.theguardian.com/us-news/2026/jun/02/iowa-primary-election-results",
        ),
    ),
    "me_sen": RaceNominees(
        race_id="me_sen",
        republican=Nominee(
            name="Susan Collins",
            party="republican",
            status="nominee",
            source_name="2026 United States Senate election in Maine",
            source_url="https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Maine",
        ),
        democratic=Nominee(
            name="Troy Jackson",
            party="democratic",
            status="presumptive_nominee",
            source_name="Portland Press Herald",
            source_url="https://www.pressherald.com/2026/07/18/how-mainers-began-picking-delegates-who-will-choose-graham-platners-replacement/",
        ),
        last_verified="2026-07-19",
        notes=(
            "Platner withdrew after the primary. Troy Jackson is tracked as the "
            "Democratic replacement candidate pending the formal Maine Democratic "
            "Party convention."
        ),
    ),
    "mi_sen": RaceNominees(
        race_id="mi_sen",
        republican=Nominee(
            name="Mike Rogers",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/c957db07eb78ea93c70208ba0a6bceed",
        ),
        democratic=Nominee(
            name="Abdul El-Sayed",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/c957db07eb78ea93c70208ba0a6bceed",
        ),
        last_verified="2026-08-06",
        notes="Michigan U.S. Senate nominees updated after the August 4, 2026 primary.",
    ),
    "mi_gov": RaceNominees(
        race_id="mi_gov",
        republican=Nominee(
            name="John James",
            party="republican",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/c957db07eb78ea93c70208ba0a6bceed",
        ),
        democratic=Nominee(
            name="Jocelyn Benson",
            party="democratic",
            status="nominee",
            source_name="Associated Press",
            source_url="https://apnews.com/article/c957db07eb78ea93c70208ba0a6bceed",
        ),
        last_verified="2026-08-06",
        notes="Michigan governor nominees updated after the August 4, 2026 primary.",
    ),
    "oh_sen": RaceNominees(
        race_id="oh_sen",
        republican=Nominee(
            name="Jon Husted",
            party="republican",
            status="nominee",
            source_name="The Guardian",
            source_url="https://www.theguardian.com/us-news/2026/may/05/jon-husted-sherrod-brown-ohio-senate-primary",
        ),
        democratic=Nominee(
            name="Sherrod Brown",
            party="democratic",
            status="nominee",
            source_name="The Guardian",
            source_url="https://www.theguardian.com/us-news/2026/may/05/jon-husted-sherrod-brown-ohio-senate-primary",
        ),
    ),
    "oh_gov": RaceNominees(
        race_id="oh_gov",
        republican=Nominee(
            name="Vivek Ramaswamy",
            party="republican",
            status="nominee",
            source_name="The Guardian",
            source_url="https://www.theguardian.com/us-news/2026/may/05/jon-husted-sherrod-brown-ohio-senate-primary",
        ),
        democratic=Nominee(
            name="Amy Acton",
            party="democratic",
            status="nominee",
            source_name="The Guardian",
            source_url="https://www.theguardian.com/us-news/2026/may/05/jon-husted-sherrod-brown-ohio-senate-primary",
        ),
    ),
    "pa_gov": RaceNominees(
        race_id="pa_gov",
        republican=Nominee(
            name="Stacy Garrity",
            party="republican",
            status="nominee",
            source_name="Axios Philadelphia",
            source_url="https://www.axios.com/local/philadelphia/2026/05/20/primary-election-philadelphia-pennsylvania-josh-shapiro-stacy-garrity",
        ),
        democratic=Nominee(
            name="Josh Shapiro",
            party="democratic",
            status="nominee",
            source_name="Axios Philadelphia",
            source_url="https://www.axios.com/local/philadelphia/2026/05/20/primary-election-philadelphia-pennsylvania-josh-shapiro-stacy-garrity",
        ),
    ),
    "wi_gov": RaceNominees(
        race_id="wi_gov",
        republican=Nominee(
            name="Tom Tiffany",
            party="republican",
            status="nominee",
            source_name="Wisconsin Public Radio",
            source_url="https://www.wpr.org/news/crowley-leading-tiffany-four-points-new-poll",
        ),
        democratic=Nominee(
            name="David Crowley",
            party="democratic",
            status="nominee",
            source_name="Wisconsin Public Radio",
            source_url="https://www.wpr.org/news/crowley-leading-tiffany-four-points-new-poll",
        ),
        last_verified="2026-08-18",
        notes="Wisconsin governor nominees updated after the August 11, 2026 primary.",
    ),
}
