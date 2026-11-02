const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const vm = require('node:vm');
const source = readFileSync(join(__dirname, '../docs/app.js'), 'utf8');

function functionSource(name) {
  const start = source.indexOf(`function ${name}(`);
  assert(start >= 0);
  let end = source.indexOf('{', start), depth = 1;
  while (depth) {
    end++;
    if (source[end] === '{') depth++;
    if (source[end] === '}') depth--;
  }
  return source.slice(start, end + 1);
}

function context(race) {
  const scope = { forecastPayload: { races: race ? [race] : [] } };
  for (const name of ['genericLeader', 'genericMargin', 'genericMoe', 'genericStatus',
    'genericRepublicanShare', 'genericDemocraticShare', 'genericBar',
    'genericBarLeft', 'genericBarRight']) {
    scope[name] = { textContent: '', style: {}, classList: { add() {}, remove() {} } };
  }
  vm.createContext(scope);
  for (const name of ['hasForecastData', 'statusLabel', 'candidateLabel',
    'leaderLabel', 'signedPercent', 'renderGenericBallot', 'predictedPartyForRace']) {
    vm.runInContext(functionSource(name), scope);
  }
  return scope;
}

test('prior-only generic ballot renders without formatting null values', () => {
  const scope = context({ race_id: 'us_house_generic', data_available: false,
    status: 'unrated', candidate_a_share: null, candidate_b_share: null,
    margin_percent: null, margin_of_error_percent: null });
  scope.renderGenericBallot();
  assert.equal(scope.genericStatus.textContent, 'Awaiting polls');
  assert.equal(scope.genericMoe.textContent, '-');
  assert.equal(scope.genericRepublicanShare.textContent, '-');
  assert.equal(scope.predictedPartyForRace(scope.forecastPayload.races[0], 'republican'), 'tossup');
});

test('observed generic ballot retains numeric forecasts', () => {
  const scope = context({ race_id: 'us_house_generic', data_available: true,
    status: 'tossup', leader: 'democratic', candidate_a_share: .47,
    candidate_b_share: .49, margin_percent: -2, margin_of_error_percent: 5 });
  scope.renderGenericBallot();
  assert.equal(scope.genericMoe.textContent, '±5.00 pts');
  assert.equal(scope.genericRepublicanShare.textContent, '47.0%');
  assert(Math.abs(parseFloat(scope.genericBarLeft.style.width) - 100*.47/.96) < 1e-12);
});

test('independent candidate has a distinct leader and chamber allocation', () => {
  const race = { data_available: true, status: 'lean-independent', leader: 'independent',
    margin: -.04, candidate_a_name: 'Pete Ricketts', candidate_b_name: 'Dan Osborn',
    candidate_b_party: 'Independent' };
  const scope = context(race);
  assert.equal(scope.leaderLabel(race), 'Dan Osborn');
  assert.equal(scope.statusLabel(race.status), 'Lean Independent');
  assert.equal(scope.predictedPartyForRace(race, 'republican'), 'independent');
});

test('chamber totals preserve an independent seat separately', () => {
  const scope = {};
  vm.createContext(scope);
  vm.runInContext(functionSource('renderChamberMakeup'), scope);
  const elements = {};
  for (const key of ['total', 'republicanSeats', 'democraticSeats', 'tossupSeats',
    'independentSeats', 'republicanBar', 'democraticBar', 'tossupBar', 'independentBar']) {
    elements[key] = { textContent: '', style: {} };
  }
  scope.renderChamberMakeup('senate', { republican: 49, democratic: 48, independent: 1, tossup: 2 }, elements);
  assert.equal(elements.independentSeats.textContent, 1);
  assert.equal(elements.independentBar.style.width, '1%');
  assert.equal(elements.democraticBar.style.width, '48%');
});

function rollingContext(average) {
  const scope = { raceHistoryPayload: { races: [{ race_id: 'me_sen', rolling_average: average }] } };
  for (const name of ['raceRollingSummary', 'raceRollingRepublican', 'raceRollingDemocratic', 'raceRollingMargin']) {
    scope[name] = { textContent: '' };
  }
  vm.createContext(scope);
  for (const name of ['candidateLabel', 'signedPercent', 'renderRollingAverage']) {
    vm.runInContext(functionSource(name), scope);
  }
  return scope;
}

test('rolling average shows available poll count, shares and signed margin', () => {
  const scope = rollingContext({ poll_count: 3, window_start_date: '2026-10-01', date: '2026-10-03',
    candidate_a_share: .46, candidate_b_share: .49, margin_percent: -3 });
  scope.renderRollingAverage({ race_id: 'me_sen', candidate_a_name: 'Susan Collins', candidate_b_name: 'Troy Jackson' });
  assert.equal(scope.raceRollingSummary.textContent, '3 of 7 polls · 2026-10-01 to 2026-10-03');
  assert.equal(scope.raceRollingRepublican.textContent, 'Susan Collins: 46.0%');
  assert.equal(scope.raceRollingDemocratic.textContent, 'Troy Jackson: 49.0%');
  assert.equal(scope.raceRollingMargin.textContent, '-3.00 pts');
});

test('rolling average clears previous values when switching to a race without polls', () => {
  const scope = rollingContext(null);
  scope.raceRollingRepublican.textContent = 'Previous result';
  scope.renderRollingAverage({ race_id: 'me_sen' });
  assert.equal(scope.raceRollingSummary.textContent, 'Awaiting polls');
  assert.equal(scope.raceRollingRepublican.textContent, 'Republican: —');
  assert.equal(scope.raceRollingMargin.textContent, '—');
});
