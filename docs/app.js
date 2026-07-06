const stateMeta = [
  { fips: "01", code: "AL", name: "Alabama" },
  { fips: "02", code: "AK", name: "Alaska" },
  { fips: "04", code: "AZ", name: "Arizona" },
  { fips: "05", code: "AR", name: "Arkansas" },
  { fips: "06", code: "CA", name: "California" },
  { fips: "08", code: "CO", name: "Colorado" },
  { fips: "09", code: "CT", name: "Connecticut" },
  { fips: "10", code: "DE", name: "Delaware" },
  { fips: "12", code: "FL", name: "Florida" },
  { fips: "13", code: "GA", name: "Georgia" },
  { fips: "15", code: "HI", name: "Hawaii" },
  { fips: "16", code: "ID", name: "Idaho" },
  { fips: "17", code: "IL", name: "Illinois" },
  { fips: "18", code: "IN", name: "Indiana" },
  { fips: "19", code: "IA", name: "Iowa" },
  { fips: "20", code: "KS", name: "Kansas" },
  { fips: "21", code: "KY", name: "Kentucky" },
  { fips: "22", code: "LA", name: "Louisiana" },
  { fips: "23", code: "ME", name: "Maine" },
  { fips: "24", code: "MD", name: "Maryland" },
  { fips: "25", code: "MA", name: "Massachusetts" },
  { fips: "26", code: "MI", name: "Michigan" },
  { fips: "27", code: "MN", name: "Minnesota" },
  { fips: "28", code: "MS", name: "Mississippi" },
  { fips: "29", code: "MO", name: "Missouri" },
  { fips: "30", code: "MT", name: "Montana" },
  { fips: "31", code: "NE", name: "Nebraska" },
  { fips: "32", code: "NV", name: "Nevada" },
  { fips: "33", code: "NH", name: "New Hampshire" },
  { fips: "34", code: "NJ", name: "New Jersey" },
  { fips: "35", code: "NM", name: "New Mexico" },
  { fips: "36", code: "NY", name: "New York" },
  { fips: "37", code: "NC", name: "North Carolina" },
  { fips: "38", code: "ND", name: "North Dakota" },
  { fips: "39", code: "OH", name: "Ohio" },
  { fips: "40", code: "OK", name: "Oklahoma" },
  { fips: "41", code: "OR", name: "Oregon" },
  { fips: "42", code: "PA", name: "Pennsylvania" },
  { fips: "44", code: "RI", name: "Rhode Island" },
  { fips: "45", code: "SC", name: "South Carolina" },
  { fips: "46", code: "SD", name: "South Dakota" },
  { fips: "47", code: "TN", name: "Tennessee" },
  { fips: "48", code: "TX", name: "Texas" },
  { fips: "49", code: "UT", name: "Utah" },
  { fips: "50", code: "VT", name: "Vermont" },
  { fips: "51", code: "VA", name: "Virginia" },
  { fips: "53", code: "WA", name: "Washington" },
  { fips: "54", code: "WV", name: "West Virginia" },
  { fips: "55", code: "WI", name: "Wisconsin" },
  { fips: "56", code: "WY", name: "Wyoming" },
];

const fipsToState = new Map(stateMeta.map((state) => [state.fips, state]));
const codeToState = new Map(stateMeta.map((state) => [state.code, state]));
const labelAnchors = {
  AK: [-150.0, 64.0],
  AL: [-86.8, 32.8],
  AR: [-92.4, 34.9],
  AZ: [-111.8, 34.3],
  CA: [-119.5, 37.2],
  CO: [-105.5, 39.0],
  CT: [-72.7, 41.6],
  DE: [-75.5, 39.0],
  FL: [-81.7, 28.4],
  GA: [-83.4, 32.7],
  HI: [-157.4, 20.8],
  IA: [-93.5, 42.1],
  ID: [-114.5, 44.2],
  IL: [-89.2, 40.0],
  IN: [-86.1, 40.0],
  KS: [-98.3, 38.5],
  KY: [-84.8, 37.7],
  LA: [-92.2, 31.0],
  MA: [-71.8, 42.2],
  MD: [-76.7, 39.0],
  ME: [-69.0, 45.2],
  MI: [-85.5, 44.5],
  MN: [-94.4, 46.1],
  MO: [-92.5, 38.5],
  MS: [-89.7, 32.7],
  MT: [-110.5, 46.9],
  NC: [-79.8, 35.5],
  ND: [-100.5, 47.5],
  NE: [-99.8, 41.5],
  NH: [-71.6, 43.7],
  NJ: [-74.7, 40.1],
  NM: [-106.1, 34.5],
  NV: [-116.6, 39.0],
  NY: [-75.4, 43.0],
  OH: [-82.8, 40.2],
  OK: [-97.5, 35.5],
  OR: [-120.5, 44.2],
  PA: [-77.8, 40.8],
  RI: [-71.5, 41.7],
  SC: [-80.9, 33.8],
  SD: [-100.2, 44.4],
  TN: [-86.4, 35.8],
  TX: [-99.3, 31.3],
  UT: [-111.7, 39.3],
  VA: [-78.6, 37.7],
  VT: [-72.7, 44.1],
  WA: [-120.7, 47.4],
  WI: [-89.8, 44.5],
  WV: [-80.6, 38.6],
  WY: [-107.5, 43.0],
};

const senateSeatsBefore = {
  republican: 53,
  democratic: 47,
};

const senateIncumbentParties2026 = {
  AL: "republican",
  AK: "republican",
  AR: "republican",
  CO: "democratic",
  DE: "democratic",
  FL: "republican",
  GA: "democratic",
  ID: "republican",
  IL: "democratic",
  IA: "republican",
  KS: "republican",
  KY: "republican",
  LA: "republican",
  ME: "republican",
  MA: "democratic",
  MI: "democratic",
  MN: "democratic",
  MS: "republican",
  MT: "republican",
  NE: "republican",
  NH: "democratic",
  NJ: "democratic",
  NM: "democratic",
  NC: "republican",
  OH: "republican",
  OK: "republican",
  OR: "democratic",
  RI: "democratic",
  SC: "republican",
  SD: "republican",
  TN: "republican",
  TX: "republican",
  VA: "democratic",
  WV: "republican",
  WY: "republican",
};

const governorIncumbentParties = {
  AL: "republican",
  AK: "republican",
  AZ: "democratic",
  AR: "republican",
  CA: "democratic",
  CO: "democratic",
  CT: "democratic",
  DE: "democratic",
  FL: "republican",
  GA: "republican",
  HI: "democratic",
  ID: "republican",
  IL: "democratic",
  IN: "republican",
  IA: "republican",
  KS: "democratic",
  KY: "democratic",
  LA: "republican",
  ME: "democratic",
  MD: "democratic",
  MA: "democratic",
  MI: "democratic",
  MN: "democratic",
  MS: "republican",
  MO: "republican",
  MT: "republican",
  NE: "republican",
  NV: "republican",
  NH: "republican",
  NJ: "democratic",
  NM: "democratic",
  NY: "democratic",
  NC: "democratic",
  ND: "republican",
  OH: "republican",
  OK: "republican",
  OR: "democratic",
  PA: "democratic",
  RI: "democratic",
  SC: "republican",
  SD: "republican",
  TN: "republican",
  TX: "republican",
  UT: "republican",
  VT: "republican",
  VA: "democratic",
  WA: "democratic",
  WV: "republican",
  WI: "democratic",
  WY: "republican",
};

const map = document.querySelector("#state-map");
const mapWrap = document.querySelector(".map-wrap");
const tooltip = document.querySelector("#map-tooltip");
const dashboardPage = document.querySelector("#dashboard-page");
const racePage = document.querySelector("#race-page");
const tabs = document.querySelectorAll(".tab");
const modeledCount = document.querySelector("#modeled-count");
const redCount = document.querySelector("#red-count");
const blueCount = document.querySelector("#blue-count");
const tossupCount = document.querySelector("#tossup-count");
const updatedAt = document.querySelector("#updated-at");
const genericLeader = document.querySelector("#generic-leader");
const genericMargin = document.querySelector("#generic-margin");
const genericMoe = document.querySelector("#generic-moe");
const genericStatus = document.querySelector("#generic-status");
const genericRepublicanShare = document.querySelector("#generic-republican-share");
const genericDemocraticShare = document.querySelector("#generic-democratic-share");
const genericBar = document.querySelector("#generic-bar");
const genericBarLeft = document.querySelector("#generic-bar-left");
const genericBarRight = document.querySelector("#generic-bar-right");
const senateTotal = document.querySelector("#senate-total");
const senateRepublicanSeats = document.querySelector("#senate-republican-seats");
const senateDemocraticSeats = document.querySelector("#senate-democratic-seats");
const senateTossupSeats = document.querySelector("#senate-tossup-seats");
const senateRepublicanBar = document.querySelector("#senate-republican-bar");
const senateDemocraticBar = document.querySelector("#senate-democratic-bar");
const senateTossupBar = document.querySelector("#senate-tossup-bar");
const senateMakeupCard = document.querySelector("#senate-makeup-card");
const governorTotal = document.querySelector("#governor-total");
const governorRepublicanSeats = document.querySelector("#governor-republican-seats");
const governorDemocraticSeats = document.querySelector("#governor-democratic-seats");
const governorTossupSeats = document.querySelector("#governor-tossup-seats");
const governorRepublicanBar = document.querySelector("#governor-republican-bar");
const governorDemocraticBar = document.querySelector("#governor-democratic-bar");
const governorTossupBar = document.querySelector("#governor-tossup-bar");
const governorMakeupCard = document.querySelector("#governor-makeup-card");
const raceOffice = document.querySelector("#race-office");
const raceTitle = document.querySelector("#race-title");
const raceStatus = document.querySelector("#race-status");
const raceLeader = document.querySelector("#race-leader");
const raceMargin = document.querySelector("#race-margin");
const raceMoe = document.querySelector("#race-moe");
const raceRating = document.querySelector("#race-rating");
const raceRepublicanLabel = document.querySelector("#race-republican-label");
const raceDemocraticLabel = document.querySelector("#race-democratic-label");
const raceRepublicanShare = document.querySelector("#race-republican-share");
const raceDemocraticShare = document.querySelector("#race-democratic-share");
const raceBar = document.querySelector("#race-bar");
const raceBarLeft = document.querySelector("#race-bar-left");
const raceBarRight = document.querySelector("#race-bar-right");
const raceChart = document.querySelector("#race-chart");

let selectedOffice = "senate";
let selectedState = null;
let forecastPayload = { generated_at: null, races: [] };
let raceHistoryPayload = { generated_at: null, races: [] };
let stateFeatures = [];
let tooltipPinnedUntil = 0;

function renderMap() {
  const byState = racesByState(selectedOffice);
  map.innerHTML = "";

  if (!stateFeatures.length || !window.d3 || !window.topojson) {
    map.classList.add("is-loading");
    map.textContent = "Map data unavailable";
    renderSummary();
    return;
  }

  map.classList.remove("is-loading");
  const width = 975;
  const height = 610;
  const featureCollection = { type: "FeatureCollection", features: stateFeatures };
  const projection = d3.geoAlbersUsa().fitSize([width, height], featureCollection);
  const path = d3.geoPath(projection);
  const svg = d3
    .select(map)
    .append("svg")
    .attr("viewBox", `0 0 ${width} ${height}`)
    .attr("role", "img")
    .attr("aria-label", `${officeLabel(selectedOffice)} forecast map`);

  svg
    .append("g")
    .attr("class", "states-layer")
    .selectAll("path")
    .data(stateFeatures)
    .join("path")
    .attr("class", (feature) => {
      const state = stateForFeature(feature);
      const race = state ? byState.get(state.code) : null;
      const selected = state?.code === selectedState ? " is-selected" : "";
      const statusClass = race ? `${race.status} ${race.leader}` : "unmodeled";
      return `state-shape ${statusClass}${selected}`;
    })
    .attr("d", path)
    .attr("tabindex", 0)
    .attr("role", "button")
    .attr("aria-label", (feature) => {
      const state = stateForFeature(feature);
      const race = state ? byState.get(state.code) : null;
      return race
        ? `${state.name} ${officeLabel(selectedOffice)} ${statusLabel(race.status)}`
        : `${state?.name ?? "State"} unmodeled`;
    })
    .on("pointerenter", (event, feature) => showTooltip(event, feature))
    .on("pointermove", (event, feature) => showTooltip(event, feature))
    .on("pointerleave", hideTooltip)
    .on("mouseenter", (event, feature) => showTooltip(event, feature))
    .on("mousemove", (event, feature) => showTooltip(event, feature))
    .on("mouseleave", hideTooltip)
    .on("focus", (event, feature) => showTooltip(event, feature))
    .on("blur", hideTooltip)
    .on("click", (event, feature) => {
      if (!openRaceForFeature(feature)) {
        const tooltipEvent = {
          clientX: event.clientX,
          clientY: event.clientY,
        };
        selectFeature(feature);
        tooltipPinnedUntil = Date.now() + 900;
        setTimeout(() => showTooltip(tooltipEvent, feature), 120);
      }
    })
    .on("keydown", (event, feature) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        if (!openRaceForFeature(feature)) {
          selectFeature(feature);
        }
      }
    })
    .append("title")
    .text((feature) => {
      const state = stateForFeature(feature);
      const race = state ? byState.get(state.code) : null;
      if (race && !hasForecastData(race)) {
        return `${state.name}: No data available`;
      }
      return race
        ? `${state.name}: ${statusLabel(race.status)}, ${signedPercent(race.margin_percent)}`
        : `${state?.name ?? "State"}: unmodeled`;
    });

  svg
    .append("path")
    .datum(topojson.mesh(window.usTopology, window.usTopology.objects.states, (a, b) => a !== b))
    .attr("class", "state-borders")
    .attr("d", path);

  svg
    .append("g")
    .attr("class", "state-labels")
    .selectAll("text")
    .data(stateFeatures)
    .join("text")
    .attr("x", (feature) => labelPoint(projection, path, feature)[0])
    .attr("y", (feature) => labelPoint(projection, path, feature)[1])
    .text((feature) => stateForFeature(feature)?.code ?? "")
    .attr("dy", "0.35em");

  renderSummary();
}

function selectFeature(feature) {
  const state = stateForFeature(feature);
  if (!state) {
    return;
  }
  selectedState = state.code;
  renderMap();
  renderDetail();
}

function openRaceForFeature(feature) {
  const state = stateForFeature(feature);
  const race = state ? racesByState(selectedOffice).get(state.code) : null;
  if (!race) {
    return false;
  }
  window.location.hash = `race/${race.race_id}`;
  return true;
}

function showTooltip(event, feature) {
  const state = stateForFeature(feature);
  if (!state) {
    hideTooltip();
    return;
  }
  const race = racesByState(selectedOffice).get(state.code);
  tooltip.innerHTML = tooltipHtml(state, race);
  tooltip.setAttribute("aria-hidden", "false");
  tooltip.classList.add("is-visible");
  positionTooltip(event);
}

function hideTooltip() {
  if (Date.now() < tooltipPinnedUntil) {
    return;
  }
  tooltip.classList.remove("is-visible");
  tooltip.setAttribute("aria-hidden", "true");
}

function positionTooltip(event) {
  const wrapRect = mapWrap.getBoundingClientRect();
  const pointerX = "clientX" in event ? event.clientX : wrapRect.left + wrapRect.width / 2;
  const pointerY = "clientY" in event ? event.clientY : wrapRect.top + wrapRect.height / 2;
  const tooltipRect = tooltip.getBoundingClientRect();
  const padding = 12;
  let left = pointerX - wrapRect.left + 16;
  let top = pointerY - wrapRect.top - tooltipRect.height - 16;

  if (left + tooltipRect.width > wrapRect.width - padding) {
    left = pointerX - wrapRect.left - tooltipRect.width - 16;
  }
  if (left < padding) {
    left = padding;
  }
  if (top < padding) {
    top = pointerY - wrapRect.top + 16;
  }
  if (top + tooltipRect.height > wrapRect.height - padding) {
    top = wrapRect.height - tooltipRect.height - padding;
  }

  tooltip.style.left = `${left}px`;
  tooltip.style.top = `${top}px`;
}

function tooltipHtml(state, race) {
  if (!race) {
    return `
      <div class="tooltip-kicker">${officeLabel(selectedOffice)}</div>
      <strong>${state.name}</strong>
      <span class="tooltip-muted">No modeled ${officeLabel(selectedOffice).toLowerCase()} race</span>
    `;
  }

  if (!hasForecastData(race)) {
    return `
      <div class="tooltip-kicker">${officeLabel(selectedOffice)}</div>
      <strong>${race.state}</strong>
      <span class="tooltip-muted">No data available</span>
      <dl>
        <div><dt>Status</dt><dd>${statusLabel(race.status)}</dd></div>
      </dl>
    `;
  }

  return `
    <div class="tooltip-kicker">${officeLabel(selectedOffice)}</div>
    <strong>${race.state}</strong>
    <span>${leaderLabel(race)} · ${statusLabel(race.status)}</span>
    <dl>
      <div><dt>Margin</dt><dd>${signedPercent(race.margin_percent)}</dd></div>
      <div><dt>MOE</dt><dd>±${race.margin_of_error_percent.toFixed(2)} pts</dd></div>
      <div><dt>${candidateLabel(race, "republican", true)}</dt><dd>${(race.candidate_a_share * 100).toFixed(1)}%</dd></div>
      <div><dt>${candidateLabel(race, "democratic", true)}</dt><dd>${(race.candidate_b_share * 100).toFixed(1)}%</dd></div>
    </dl>
  `;
}

function labelPoint(projection, path, feature) {
  const state = stateForFeature(feature);
  if (state && labelAnchors[state.code]) {
    return projection(labelAnchors[state.code]) ?? path.centroid(feature);
  }
  return path.centroid(feature);
}

function renderSummary() {
  const races = forecastPayload.races.filter((race) => race.office === selectedOffice);
  modeledCount.textContent = races.length;
  redCount.textContent = races.filter((race) => race.leader === "republican").length;
  blueCount.textContent = races.filter((race) => race.leader === "democratic").length;
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
  renderGenericBallot();
  renderActiveMakeupCard();
  renderChamberMakeup("senate", senateMakeup(), {
    total: senateTotal,
    republicanSeats: senateRepublicanSeats,
    democraticSeats: senateDemocraticSeats,
    tossupSeats: senateTossupSeats,
    republicanBar: senateRepublicanBar,
    democraticBar: senateDemocraticBar,
    tossupBar: senateTossupBar,
  });
  renderChamberMakeup("governor", governorMakeup(), {
    total: governorTotal,
    republicanSeats: governorRepublicanSeats,
    democraticSeats: governorDemocraticSeats,
    tossupSeats: governorTossupSeats,
    republicanBar: governorRepublicanBar,
    democraticBar: governorDemocraticBar,
    tossupBar: governorTossupBar,
  });
}

function renderActiveMakeupCard() {
  senateMakeupCard.hidden = selectedOffice !== "senate";
  governorMakeupCard.hidden = selectedOffice !== "governor";
}

function renderGenericBallot() {
  const race = forecastPayload.races.find((item) => item.race_id === "us_house_generic");

  if (!race) {
    genericLeader.textContent = "-";
    genericMargin.textContent = "-";
    genericMoe.textContent = "-";
    genericStatus.textContent = "-";
    genericRepublicanShare.textContent = "-";
    genericDemocraticShare.textContent = "-";
    genericBar.classList.add("is-empty");
    genericBarLeft.style.width = "50%";
    genericBarRight.style.width = "50%";
    return;
  }

  genericBar.classList.remove("is-empty");
  genericLeader.textContent = leaderLabel(race);
  genericMargin.textContent = signedPercent(race.margin_percent);
  genericMoe.textContent = `±${race.margin_of_error_percent.toFixed(2)} pts`;
  genericStatus.textContent = statusLabel(race.status);
  genericRepublicanShare.textContent = `${(race.candidate_a_share * 100).toFixed(1)}%`;
  genericDemocraticShare.textContent = `${(race.candidate_b_share * 100).toFixed(1)}%`;

  const total = race.candidate_a_share + race.candidate_b_share;
  const republicanWidth = total > 0 ? (race.candidate_a_share / total) * 100 : 50;
  genericBarLeft.style.width = `${republicanWidth}%`;
  genericBarRight.style.width = `${100 - republicanWidth}%`;
}

function renderChamberMakeup(kind, counts, elements) {
  const total = counts.republican + counts.democratic + counts.tossup;
  const republicanWidth = total > 0 ? (counts.republican / total) * 100 : 50;
  const tossupWidth = total > 0 ? (counts.tossup / total) * 100 : 0;
  const democraticWidth = Math.max(0, 100 - republicanWidth - tossupWidth);
  elements.total.textContent =
    kind === "senate"
      ? `${counts.republican}-${counts.democratic}-${counts.tossup}`
      : `${total} seats`;
  elements.republicanSeats.textContent = counts.republican;
  elements.democraticSeats.textContent = counts.democratic;
  elements.tossupSeats.textContent = counts.tossup;
  elements.republicanBar.style.width = `${republicanWidth}%`;
  elements.tossupBar.style.width = `${tossupWidth}%`;
  elements.democraticBar.style.width = `${democraticWidth}%`;
}

function senateMakeup() {
  const counts = { ...senateSeatsBefore, tossup: 0 };
  const senateRaces = racesByState("senate");

  Object.entries(senateIncumbentParties2026).forEach(([stateCode, incumbentParty]) => {
    const predictedParty = predictedPartyForRace(senateRaces.get(stateCode), incumbentParty);
    counts[incumbentParty] -= 1;
    counts[predictedParty] += 1;
  });

  return counts;
}

function governorMakeup() {
  const counts = { republican: 0, democratic: 0, tossup: 0 };
  const governorRaces = racesByState("governor");

  Object.entries(governorIncumbentParties).forEach(([stateCode, incumbentParty]) => {
    const predictedParty = predictedPartyForRace(governorRaces.get(stateCode), incumbentParty);
    counts[predictedParty] += 1;
  });

  return counts;
}

function predictedPartyForRace(race, incumbentParty) {
  if (!race) {
    return incumbentParty;
  }
  if (race.status === "tossup") {
    return "tossup";
  }
  if (race.margin > 0) {
    return "republican";
  }
  if (race.margin < 0) {
    return "democratic";
  }
  return incumbentParty;
}

function racesByState(office) {
  const byState = new Map();
  forecastPayload.races
    .filter((race) => race.office === office)
    .forEach((race) => byState.set(race.state_code, race));
  return byState;
}

function stateForFeature(feature) {
  return fipsToState.get(String(feature.id).padStart(2, "0"));
}

function officeLabel(office) {
  if (office === "senate") {
    return "Senate";
  }
  if (office === "governor") {
    return "Governor";
  }
  return "Generic Ballot";
}

function leaderLabel(race) {
  if (!hasForecastData(race)) {
    return "No data available";
  }
  if (race.status === "tossup") {
    return "No clear leader";
  }
  if (race.leader === "republican") {
    return candidateLabel(race, "republican");
  }
  if (race.leader === "democratic") {
    return candidateLabel(race, "democratic");
  }
  return "Tie";
}

function candidateLabel(race, party, compact = false) {
  if (party === "republican") {
    return race.candidate_a_name ?? (compact ? "Rep" : "Republican");
  }
  return race.candidate_b_name ?? (compact ? "Dem" : "Democratic");
}

function statusLabel(status) {
  const labels = {
    tossup: "Tossup",
    "tilt-republican": "Tilt Republican",
    "lean-republican": "Lean Republican",
    "likely-republican": "Likely Republican",
    "safe-republican": "Safe Republican",
    "tilt-democratic": "Tilt Democratic",
    "lean-democratic": "Lean Democratic",
    "likely-democratic": "Likely Democratic",
    "safe-democratic": "Safe Democratic",
  };
  if (status in labels) {
    return labels[status];
  }
  return "Unmodeled";
}

function signedPercent(value) {
  if (typeof value !== "number") {
    return "No data available";
  }
  const sign = value > 0 ? "+" : "";
  return `${sign}${value.toFixed(2)} pts`;
}

function hasForecastData(race) {
  return race?.data_available !== false;
}

function renderRoute() {
  const raceId = raceIdFromHash();
  if (raceId) {
    renderRacePage(raceId);
    return;
  }

  dashboardPage.hidden = false;
  racePage.hidden = true;
  renderMap();
  renderDetail();
}

function raceIdFromHash() {
  const match = window.location.hash.match(/^#race\/([a-z0-9_-]+)$/i);
  return match ? match[1] : null;
}

function renderRacePage(raceId) {
  const race = forecastPayload.races.find((item) => item.race_id === raceId);
  if (!race) {
    window.location.hash = "";
    return;
  }

  dashboardPage.hidden = true;
  racePage.hidden = false;
  hideTooltip();

  raceOffice.textContent = officeLabel(race.office);
  raceTitle.textContent = raceTitleLabel(race);
  raceStatus.textContent = hasForecastData(race) ? statusLabel(race.status) : "No data available";
  raceStatus.className = `race-status ${hasForecastData(race) ? race.status : "tossup"}`;
  raceLeader.textContent = leaderLabel(race);
  raceMargin.textContent = signedPercent(race.margin_percent);
  raceMoe.textContent =
    typeof race.margin_of_error_percent === "number"
      ? `±${race.margin_of_error_percent.toFixed(2)} pts`
      : "No data available";
  raceRating.textContent = statusLabel(race.status);
  raceRepublicanLabel.textContent = `${candidateLabel(race, "republican")} share`;
  raceDemocraticLabel.textContent = `${candidateLabel(race, "democratic")} share`;
  raceRepublicanShare.textContent =
    typeof race.candidate_a_share === "number"
      ? `${(race.candidate_a_share * 100).toFixed(1)}%`
      : "No data available";
  raceDemocraticShare.textContent =
    typeof race.candidate_b_share === "number"
      ? `${(race.candidate_b_share * 100).toFixed(1)}%`
      : "No data available";

  const total =
    typeof race.candidate_a_share === "number" && typeof race.candidate_b_share === "number"
      ? race.candidate_a_share + race.candidate_b_share
      : 0;
  const republicanWidth = total > 0 ? (race.candidate_a_share / total) * 100 : 50;
  raceBar.classList.toggle("is-empty", !hasForecastData(race));
  raceBarLeft.style.width = `${republicanWidth}%`;
  raceBarRight.style.width = `${100 - republicanWidth}%`;

  renderRaceChart(race);
}

function renderRaceChart(race) {
  const history = raceHistoryPayload.races.find((item) => item.race_id === race.race_id);
  const modelPoints = (history?.model_points ?? [])
    .filter((point) => typeof point.candidate_a_share === "number" && typeof point.candidate_b_share === "number")
    .map((point) => ({ ...point, parsedDate: parseDate(point.date) }))
    .filter((point) => point.parsedDate);
  const pollPoints = (history?.poll_points ?? [])
    .filter((point) => typeof point.candidate_a_share === "number" && typeof point.candidate_b_share === "number")
    .map((point) => ({ ...point, parsedDate: parseDate(point.date) }))
    .filter((point) => point.parsedDate);

  raceChart.innerHTML = "";
  if (!hasForecastData(race) || (modelPoints.length < 1 && pollPoints.length < 1)) {
    raceChart.classList.add("is-empty");
    raceChart.textContent = hasForecastData(race) ? "No chart data available" : "No data available";
    return;
  }

  raceChart.classList.remove("is-empty");

  const width = 820;
  const height = 390;
  const margin = { top: 24, right: 28, bottom: 46, left: 54 };
  const innerWidth = width - margin.left - margin.right;
  const innerHeight = height - margin.top - margin.bottom;
  const allDates = [...modelPoints, ...pollPoints].map((point) => point.parsedDate);
  const allShares = [
    ...modelPoints.flatMap((point) => [point.candidate_a_share, point.candidate_b_share]),
    ...pollPoints.flatMap((point) => [point.candidate_a_share, point.candidate_b_share]),
  ];
  const dateExtent = d3.extent(allDates);
  const shareExtent = d3.extent(allShares);
  const xDomain = paddedDateDomain(dateExtent);
  const yMin = Math.max(0, (shareExtent[0] ?? 0.35) - 0.04);
  const yMax = Math.min(1, (shareExtent[1] ?? 0.55) + 0.04);
  const yDomain = yMin === yMax ? [yMin - 0.02, yMax + 0.02] : [yMin, yMax];

  const x = d3.scaleTime().domain(xDomain).range([0, innerWidth]);
  const y = d3.scaleLinear().domain(yDomain).nice().range([innerHeight, 0]);
  const svg = d3
    .select(raceChart)
    .append("svg")
    .attr("viewBox", `0 0 ${width} ${height}`)
    .attr("role", "img")
    .attr("aria-label", `${raceTitleLabel(race)} model prediction over time`);
  const plot = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

  plot
    .append("g")
    .attr("class", "chart-grid")
    .call(d3.axisLeft(y).ticks(5).tickSize(-innerWidth).tickFormat(""));

  plot
    .append("g")
    .attr("class", "chart-axis")
    .attr("transform", `translate(0,${innerHeight})`)
    .call(d3.axisBottom(x).ticks(5).tickSizeOuter(0));

  plot
    .append("g")
    .attr("class", "chart-axis")
    .call(d3.axisLeft(y).ticks(5).tickFormat(d3.format(".0%")));

  const republicanLine = d3
    .line()
    .x((point) => x(point.parsedDate))
    .y((point) => y(point.candidate_a_share))
    .curve(d3.curveMonotoneX);
  const democraticLine = d3
    .line()
    .x((point) => x(point.parsedDate))
    .y((point) => y(point.candidate_b_share))
    .curve(d3.curveMonotoneX);

  if (modelPoints.length >= 2) {
    plot
      .append("path")
      .datum(modelPoints)
      .attr("class", "model-line republican")
      .attr("d", republicanLine);
    plot
      .append("path")
      .datum(modelPoints)
      .attr("class", "model-line democratic")
      .attr("d", democraticLine);
  }

  drawPollMarkers(plot, pollPoints, x, y, "candidate_a_share", "republican", race);
  drawPollMarkers(plot, pollPoints, x, y, "candidate_b_share", "democratic", race);
}

function drawPollMarkers(plot, pollPoints, x, y, shareKey, party, race) {
  const symbol = d3.symbol().type(d3.symbolCross).size(76);
  plot
    .append("g")
    .attr("class", `poll-markers ${party}`)
    .selectAll("path")
    .data(pollPoints)
    .join("path")
    .attr("class", "poll-marker")
    .attr("transform", (point) => `translate(${x(point.parsedDate)},${y(point[shareKey])})`)
    .attr("d", symbol)
    .append("title")
    .text((point) => {
      const label = party === "republican" ? candidateLabel(race, "republican") : candidateLabel(race, "democratic");
      return `${point.pollster} (${point.date}): ${label} ${(point[shareKey] * 100).toFixed(1)}%`;
    });
}

function parseDate(value) {
  const date = new Date(`${value}T00:00:00`);
  return Number.isNaN(date.valueOf()) ? null : date;
}

function paddedDateDomain(extent) {
  const start = extent[0] ?? new Date();
  const end = extent[1] ?? start;
  if (start.valueOf() !== end.valueOf()) {
    return [start, end];
  }
  const oneDay = 24 * 60 * 60 * 1000;
  return [new Date(start.valueOf() - oneDay), new Date(end.valueOf() + oneDay)];
}

function raceTitleLabel(race) {
  if (race.race_id === "us_house_generic") {
    return "Generic Ballot";
  }
  return `${race.state} ${officeLabel(race.office)}`;
}

function defaultStateForOffice(office) {
  const races = forecastPayload.races.filter((race) => race.office === office);
  const preferred = "FL";
  if (races.some((race) => race.state_code === preferred)) {
    return preferred;
  }
  return races[0]?.state_code ?? null;
}

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    selectedOffice = tab.dataset.office;
    selectedState = defaultStateForOffice(selectedOffice);
    hideTooltip();
    tabs.forEach((item) => {
      const active = item === tab;
      item.classList.toggle("is-active", active);
      item.setAttribute("aria-selected", String(active));
    });
    renderRoute();
  });
});

Promise.all([
  fetch("data/forecasts.json", { cache: "no-store" }).then((response) => {
    if (!response.ok) {
      throw new Error(`Forecast data unavailable: ${response.status}`);
    }
    return response.json();
  }),
  fetch("data/race-history.json", { cache: "no-store" }).then((response) => {
    if (!response.ok) {
      throw new Error(`Race history unavailable: ${response.status}`);
    }
    return response.json();
  }),
  fetch("data/states-10m.json").then((response) => {
    if (!response.ok) {
      throw new Error(`Map data unavailable: ${response.status}`);
    }
    return response.json();
  }),
])
  .then(([payload, history, topology]) => {
    forecastPayload = payload;
    raceHistoryPayload = history;
    window.usTopology = topology;
    stateFeatures = topojson
      .feature(topology, topology.objects.states)
      .features.filter((feature) => fipsToState.has(String(feature.id).padStart(2, "0")));
    selectedState = defaultStateForOffice(selectedOffice);
    renderRoute();
  })
  .catch(() => {
    renderRoute();
    updatedAt.textContent = "Data unavailable";
  });

window.addEventListener("hashchange", renderRoute);
