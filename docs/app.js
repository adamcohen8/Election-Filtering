const states = [
  { code: "AK", name: "Alaska", col: 1, row: 1 },
  { code: "ME", name: "Maine", col: 11, row: 1 },
  { code: "VT", name: "Vermont", col: 9, row: 2 },
  { code: "NH", name: "New Hampshire", col: 10, row: 2 },
  { code: "WA", name: "Washington", col: 2, row: 2 },
  { code: "ID", name: "Idaho", col: 3, row: 3 },
  { code: "MT", name: "Montana", col: 4, row: 3 },
  { code: "ND", name: "North Dakota", col: 5, row: 3 },
  { code: "MN", name: "Minnesota", col: 6, row: 3 },
  { code: "WI", name: "Wisconsin", col: 7, row: 3 },
  { code: "MI", name: "Michigan", col: 8, row: 3 },
  { code: "NY", name: "New York", col: 9, row: 3 },
  { code: "MA", name: "Massachusetts", col: 10, row: 3 },
  { code: "OR", name: "Oregon", col: 2, row: 4 },
  { code: "NV", name: "Nevada", col: 3, row: 4 },
  { code: "WY", name: "Wyoming", col: 4, row: 4 },
  { code: "SD", name: "South Dakota", col: 5, row: 4 },
  { code: "IA", name: "Iowa", col: 6, row: 4 },
  { code: "IL", name: "Illinois", col: 7, row: 4 },
  { code: "IN", name: "Indiana", col: 8, row: 4 },
  { code: "OH", name: "Ohio", col: 9, row: 4 },
  { code: "PA", name: "Pennsylvania", col: 10, row: 4 },
  { code: "RI", name: "Rhode Island", col: 11, row: 4 },
  { code: "CA", name: "California", col: 2, row: 5 },
  { code: "UT", name: "Utah", col: 3, row: 5 },
  { code: "CO", name: "Colorado", col: 4, row: 5 },
  { code: "NE", name: "Nebraska", col: 5, row: 5 },
  { code: "MO", name: "Missouri", col: 6, row: 5 },
  { code: "KY", name: "Kentucky", col: 7, row: 5 },
  { code: "WV", name: "West Virginia", col: 8, row: 5 },
  { code: "VA", name: "Virginia", col: 9, row: 5 },
  { code: "MD", name: "Maryland", col: 10, row: 5 },
  { code: "CT", name: "Connecticut", col: 11, row: 5 },
  { code: "AZ", name: "Arizona", col: 3, row: 6 },
  { code: "NM", name: "New Mexico", col: 4, row: 6 },
  { code: "KS", name: "Kansas", col: 5, row: 6 },
  { code: "AR", name: "Arkansas", col: 6, row: 6 },
  { code: "TN", name: "Tennessee", col: 7, row: 6 },
  { code: "NC", name: "North Carolina", col: 8, row: 6 },
  { code: "SC", name: "South Carolina", col: 9, row: 6 },
  { code: "DE", name: "Delaware", col: 10, row: 6 },
  { code: "OK", name: "Oklahoma", col: 5, row: 7 },
  { code: "LA", name: "Louisiana", col: 6, row: 7 },
  { code: "MS", name: "Mississippi", col: 7, row: 7 },
  { code: "AL", name: "Alabama", col: 8, row: 7 },
  { code: "GA", name: "Georgia", col: 9, row: 7 },
  { code: "NJ", name: "New Jersey", col: 10, row: 7 },
  { code: "HI", name: "Hawaii", col: 1, row: 8 },
  { code: "TX", name: "Texas", col: 5, row: 8 },
  { code: "FL", name: "Florida", col: 10, row: 8 },
];

const map = document.querySelector("#state-map");
const tabs = document.querySelectorAll(".tab");
const modeledCount = document.querySelector("#modeled-count");
const redCount = document.querySelector("#red-count");
const blueCount = document.querySelector("#blue-count");
const tossupCount = document.querySelector("#tossup-count");
const updatedAt = document.querySelector("#updated-at");
const detailOffice = document.querySelector("#detail-office");
const detailTitle = document.querySelector("#detail-title");
const detailLeader = document.querySelector("#detail-leader");
const detailMargin = document.querySelector("#detail-margin");
const detailMoe = document.querySelector("#detail-moe");
const detailStatus = document.querySelector("#detail-status");
const detailRepublicanShare = document.querySelector("#detail-republican-share");
const detailDemocraticShare = document.querySelector("#detail-democratic-share");
const detailBar = document.querySelector(".bar");
const detailBarLeft = document.querySelector("#detail-bar-left");
const detailBarRight = document.querySelector("#detail-bar-right");

let selectedOffice = "senate";
let selectedState = null;
let forecastPayload = { generated_at: null, races: [] };

function renderMap() {
  const byState = racesByState(selectedOffice);
  map.innerHTML = "";
  states.forEach((state) => {
    const race = byState.get(state.code);
    const button = document.createElement("button");
    button.type = "button";
    button.className = `state ${race ? race.status : "unmodeled"}`;
    button.textContent = state.code;
    button.title = race ? `${state.name} ${officeLabel(selectedOffice)}` : `${state.name}`;
    button.style.gridColumn = state.col;
    button.style.gridRow = state.row;
    button.dataset.state = state.code;
    button.setAttribute("aria-label", button.title);
    if (selectedState === state.code) {
      button.classList.add("is-selected");
    }
    button.addEventListener("click", () => {
      selectedState = state.code;
      renderMap();
      renderDetail();
    });
    map.appendChild(button);
  });
  renderSummary();
}

function renderSummary() {
  const races = forecastPayload.races.filter((race) => race.office === selectedOffice);
  modeledCount.textContent = races.length;
  redCount.textContent = races.filter((race) => race.status === "republican").length;
  blueCount.textContent = races.filter((race) => race.status === "democratic").length;
  tossupCount.textContent = races.filter((race) => race.status === "tossup").length;
  updatedAt.textContent = forecastPayload.generated_at
    ? new Intl.DateTimeFormat(undefined, {
        month: "short",
        day: "numeric",
        hour: "numeric",
        minute: "2-digit",
      }).format(new Date(forecastPayload.generated_at))
    : "Unavailable";
}

function renderDetail() {
  const race = selectedState ? racesByState(selectedOffice).get(selectedState) : null;
  const state = states.find((item) => item.code === selectedState);
  detailOffice.textContent = officeLabel(selectedOffice);

  if (!race) {
    detailTitle.textContent = state ? `${state.name}` : "Select a modeled state";
    detailLeader.textContent = "-";
    detailMargin.textContent = "-";
    detailMoe.textContent = "-";
    detailStatus.textContent = state ? "Unmodeled" : "-";
    detailRepublicanShare.textContent = "-";
    detailDemocraticShare.textContent = "-";
    detailBar.classList.add("is-empty");
    detailBarLeft.style.width = "50%";
    detailBarRight.style.width = "50%";
    return;
  }

  detailBar.classList.remove("is-empty");
  detailTitle.textContent = `${race.state} ${officeLabel(selectedOffice)}`;
  detailLeader.textContent = leaderLabel(race);
  detailMargin.textContent = signedPercent(race.margin_percent);
  detailMoe.textContent = `±${race.margin_of_error_percent.toFixed(2)} pts`;
  detailStatus.textContent = statusLabel(race.status);
  detailRepublicanShare.textContent = `${(race.candidate_a_share * 100).toFixed(1)}%`;
  detailDemocraticShare.textContent = `${(race.candidate_b_share * 100).toFixed(1)}%`;

  const total = race.candidate_a_share + race.candidate_b_share;
  const republicanWidth = total > 0 ? (race.candidate_a_share / total) * 100 : 50;
  detailBarLeft.style.width = `${republicanWidth}%`;
  detailBarRight.style.width = `${100 - republicanWidth}%`;
}

function racesByState(office) {
  const byState = new Map();
  forecastPayload.races
    .filter((race) => race.office === office)
    .forEach((race) => byState.set(race.state_code, race));
  return byState;
}

function officeLabel(office) {
  return office === "senate" ? "Senate" : "Governor";
}

function leaderLabel(race) {
  if (race.status === "tossup") {
    return "No clear leader";
  }
  if (race.leader === "republican") {
    return "Republican";
  }
  if (race.leader === "democratic") {
    return "Democratic";
  }
  return "Tie";
}

function statusLabel(status) {
  if (status === "republican") {
    return "Red";
  }
  if (status === "democratic") {
    return "Blue";
  }
  return "Tossup";
}

function signedPercent(value) {
  const sign = value > 0 ? "+" : "";
  return `${sign}${value.toFixed(2)} pts`;
}

function defaultStateForOffice(office) {
  const races = forecastPayload.races.filter((race) => race.office === office);
  const preferred = office === "senate" ? "FL" : "FL";
  if (races.some((race) => race.state_code === preferred)) {
    return preferred;
  }
  return races[0]?.state_code ?? null;
}

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    selectedOffice = tab.dataset.office;
    selectedState = defaultStateForOffice(selectedOffice);
    tabs.forEach((item) => {
      const active = item === tab;
      item.classList.toggle("is-active", active);
      item.setAttribute("aria-selected", String(active));
    });
    renderMap();
    renderDetail();
  });
});

fetch("data/forecasts.json", { cache: "no-store" })
  .then((response) => {
    if (!response.ok) {
      throw new Error(`Forecast data unavailable: ${response.status}`);
    }
    return response.json();
  })
  .then((payload) => {
    forecastPayload = payload;
    selectedState = defaultStateForOffice(selectedOffice);
    renderMap();
    renderDetail();
  })
  .catch(() => {
    renderMap();
    renderDetail();
    updatedAt.textContent = "Data unavailable";
  });
