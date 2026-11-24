// Spark Declarative Visual Engine: energy-budget
// Interactive physics calculator + animated energy/heat flow bar schematic.

const NS = "http://www.w3.org/2000/svg";

export function mountEnergyBudget(figure, stage, controls, payload) {
  const params = payload.params || {};
  const labels = payload.labels || {};

  const massRange = params.mass_range_t || [10, 500];
  const dvRange = params.delta_v_range_km_s || [1, 25];
  const state = {
    massT: Number(params.mass_t || 100),
    dvKmS: Number(params.delta_v_km_s || 10),
    effPct: Math.round(Number(params.efficiency || 0.9) * 100),
    cadence: Number(params.cadence_per_day || 1)
  };

  const resetBtn = document.createElement("button");
  resetBtn.type = "button";
  resetBtn.className = "sp-btn";
  resetBtn.textContent = labels.reset || "Reset";
  controls.appendChild(resetBtn);

  stage.innerHTML = "";

  // Sliders container
  const slidersWrap = document.createElement("div");
  slidersWrap.className = "sp-eb-sliders";

  function makeSlider(labelText, min, max, step, initialVal, unit, onChange) {
    const field = document.createElement("label");
    field.className = "sp-eb-field";
    const head = document.createElement("div");
    head.className = "sp-eb-field-head";
    const nameEl = document.createElement("span");
    nameEl.textContent = labelText;
    const valEl = document.createElement("span");
    valEl.className = "sp-eb-field-val";
    valEl.textContent = `${initialVal}${unit}`;
    head.append(nameEl, valEl);

    const input = document.createElement("input");
    input.type = "range";
    input.className = "sp-eb-range";
    input.min = String(min);
    input.max = String(max);
    input.step = String(step);
    input.value = String(initialVal);
    input.addEventListener("input", () => {
      const v = Number(input.value);
      valEl.textContent = `${v}${unit}`;
      onChange(v);
      update();
    });
    field.append(head, input);
    slidersWrap.appendChild(field);
    return { input, valEl, unit };
  }

  const sMass = makeSlider(labels.mass_label || "Ship Mass (t)", massRange[0], massRange[1], 10, state.massT, " t", (v) => { state.massT = v; });
  const sDv = makeSlider(labels.delta_v_label || "Δv (km/s)", dvRange[0], dvRange[1], 0.5, state.dvKmS, " km/s", (v) => { state.dvKmS = v; });
  const sEff = makeSlider(labels.efficiency_label || "Efficiency (%)", 40, 98, 1, state.effPct, "%", (v) => { state.effPct = v; });
  const sCad = makeSlider(labels.cadence_label || "Departures / Day", 0.5, 12, 0.5, state.cadence, "/day", (v) => { state.cadence = v; });
  stage.appendChild(slidersWrap);

  // Live metrics strip
  const metricsEl = document.createElement("div");
  metricsEl.className = "sp-metric-strip";
  metricsEl.innerHTML = `
    <div class="sp-metric">
      <div class="sp-metric-value" data-eb="ek">—</div>
      <div class="sp-metric-label">${labels.kinetic_energy || "Ship Kinetic Energy"}</div>
    </div>
    <div class="sp-metric">
      <div class="sp-metric-value" data-eb="ee">—</div>
      <div class="sp-metric-label">${labels.electrical_input || "Electrical Input"}</div>
    </div>
    <div class="sp-metric">
      <div class="sp-metric-value" data-eb="pavg">—</div>
      <div class="sp-metric-label">${labels.avg_power || "Mean Useful Power"}</div>
    </div>
    <div class="sp-metric">
      <div class="sp-metric-value" data-eb="heat">—</div>
      <div class="sp-metric-label">${labels.waste_heat || "Waste Heat (Daily Avg)"}</div>
    </div>
  `;
  stage.appendChild(metricsEl);

  // SVG proportional energy split bar (Useful Kinetic vs Waste Heat)
  const svg = document.createElementNS(NS, "svg");
  svg.setAttribute("class", "sp-visual-svg");
  svg.setAttribute("viewBox", "0 0 720 68");
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-label", payload.title || "Energy Conversion Split");
  stage.appendChild(svg);

  function el(tag, attrs = {}) {
    const node = document.createElementNS(NS, tag);
    Object.entries(attrs).forEach(([k, v]) => node.setAttribute(k, String(v)));
    return node;
  }

  const barBg = el("rect", { x: 0, y: 20, width: 720, height: 18, rx: 6, fill: "var(--bg-surface-elevated)", stroke: "var(--border-default)", "stroke-width": 1 });
  const barUseful = el("rect", { x: 0, y: 20, width: 648, height: 18, rx: 6, fill: "var(--accent-primary)" });
  const barLoss = el("rect", { x: 648, y: 20, width: 72, height: 18, rx: 4, fill: "var(--val-open-question-accent)" });
  const lblLeft = el("text", { x: 0, y: 56, fill: "var(--text-secondary)", "font-family": "var(--font-mono)", "font-size": 11 });
  const lblRight = el("text", { x: 720, y: 56, "text-anchor": "end", fill: "var(--val-open-question-accent)", "font-family": "var(--font-mono)", "font-size": 11 });
  svg.append(barBg, barUseful, barLoss, lblLeft, lblRight);

  const elEk = metricsEl.querySelector('[data-eb="ek"]');
  const elEe = metricsEl.querySelector('[data-eb="ee"]');
  const elPavg = metricsEl.querySelector('[data-eb="pavg"]');
  const elHeat = metricsEl.querySelector('[data-eb="heat"]');

  function update() {
    const massKg = state.massT * 1000;
    const vMs = state.dvKmS * 1000;
    const ekJ = 0.5 * massKg * vMs * vMs;
    const eff = state.effPct / 100;
    const eeJ = ekJ / eff;
    const lossJ = eeJ - ekJ;

    const ekTJ = ekJ / 1e12;
    const eeTJ = eeJ / 1e12;
    const eeMWh = eeJ / 3.6e9;
    const pAvgMW = (ekJ * state.cadence) / 86400 / 1e6;
    const heatMW = (lossJ * state.cadence) / 86400 / 1e6;

    elEk.textContent = `${ekTJ.toFixed(2)} TJ`;
    elEe.textContent = `${eeTJ.toFixed(2)} TJ (${eeMWh >= 1000 ? (eeMWh / 1000).toFixed(2) + " GWh" : eeMWh.toFixed(0) + " MWh"})`;
    elPavg.textContent = `${pAvgMW.toFixed(1)} MW`;
    elHeat.textContent = `${heatMW.toFixed(1)} MW`;

    const usefulW = Math.max(24, Math.round(720 * eff));
    barUseful.setAttribute("width", String(usefulW));
    barLoss.setAttribute("x", String(usefulW));
    barLoss.setAttribute("width", String(Math.max(0, 720 - usefulW)));
    lblLeft.textContent = `Useful ΔK = ${state.effPct}% (${ekTJ.toFixed(2)} TJ)`;
    lblRight.textContent = `Thermal Loss = ${100 - state.effPct}% (${(lossJ / 1e12).toFixed(2)} TJ)`;
  }

  resetBtn.addEventListener("click", () => {
    state.massT = Number(params.mass_t || 100);
    state.dvKmS = Number(params.delta_v_km_s || 10);
    state.effPct = Math.round(Number(params.efficiency || 0.9) * 100);
    state.cadence = Number(params.cadence_per_day || 1);
    sMass.input.value = String(state.massT); sMass.valEl.textContent = `${state.massT}${sMass.unit}`;
    sDv.input.value = String(state.dvKmS); sDv.valEl.textContent = `${state.dvKmS}${sDv.unit}`;
    sEff.input.value = String(state.effPct); sEff.valEl.textContent = `${state.effPct}${sEff.unit}`;
    sCad.input.value = String(state.cadence); sCad.valEl.textContent = `${state.cadence}${sCad.unit}`;
    update();
  });

  update();
}
