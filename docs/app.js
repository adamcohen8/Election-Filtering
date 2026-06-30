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

const map = document.querySelector("#state-map");
const mapWrap = document.querySelector(".map-wrap");
const tooltip = document.querySelector("#map-tooltip");
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
      return `state-shape ${race ? race.status : "unmodeled"}${selected}`;
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
      const tooltipEvent = {
        clientX: event.clientX,
        clientY: event.clientY,
      };
      selectFeature(feature);
      tooltipPinnedUntil = Date.now() + 900;
      setTimeout(() => showTooltip(tooltipEvent, feature), 120);
    })
    .on("keydown", (event, feature) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        selectFeature(feature);
      }
    })
    .append("title")
    .text((feature) => {
      const state = stateForFeature(feature);
      const race = state ? byState.get(state.code) : null;
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
    .attr("x", (feature) => labelPoint(path, feature)[0])
    .attr("y", (feature) => labelPoint(path, feature)[1])
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

  return `
    <div class="tooltip-kicker">${officeLabel(selectedOffice)}</div>
    <strong>${race.state}</strong>
    <span>${leaderLabel(race)} · ${statusLabel(race.status)}</span>
    <dl>
      <div><dt>Margin</dt><dd>${signedPercent(race.margin_percent)}</dd></div>
      <div><dt>MOE</dt><dd>±${race.margin_of_error_percent.toFixed(2)} pts</dd></div>
      <div><dt>Rep</dt><dd>${(race.candidate_a_share * 100).toFixed(1)}%</dd></div>
      <div><dt>Dem</dt><dd>${(race.candidate_b_share * 100).toFixed(1)}%</dd></div>
    </dl>
  `;
}

function labelPoint(path, feature) {
  const state = stateForFeature(feature);
  const manual = {
    CT: [858, 176],
    DE: [827, 260],
    FL: [760, 455],
    HI: [335, 548],
    LA: [535, 410],
    MD: [805, 249],
    MA: [874, 151],
    NH: [850, 112],
    NJ: [825, 227],
    RI: [892, 176],
    VT: [817, 113],
  };
  if (state && manual[state.code]) {
    return manual[state.code];
  }
  return path.centroid(feature);
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
  const state = selectedState ? codeToState.get(selectedState) : null;
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

function stateForFeature(feature) {
  return fipsToState.get(String(feature.id).padStart(2, "0"));
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
    renderMap();
    renderDetail();
  });
});

Promise.all([
  fetch("data/forecasts.json", { cache: "no-store" }).then((response) => {
    if (!response.ok) {
      throw new Error(`Forecast data unavailable: ${response.status}`);
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
  .then(([payload, topology]) => {
    forecastPayload = payload;
    window.usTopology = topology;
    stateFeatures = topojson
      .feature(topology, topology.objects.states)
      .features.filter((feature) => fipsToState.has(String(feature.id).padStart(2, "0")));
    selectedState = defaultStateForOffice(selectedOffice);
    renderMap();
    renderDetail();
  })
  .catch(() => {
    renderMap();
    renderDetail();
    updatedAt.textContent = "Data unavailable";
  });
