// Spark Web Portal — Declarative Visual Engine Dispatcher (spark-visual)

import { mountOrbitalTransfer } from "./animations/orbital-transfer.js";
import { mountEnergyBudget } from "./animations/energy-budget.js";
import { mountPhaseProgression } from "./animations/phase-progression.js";

const REGISTRY = {
  "orbital-transfer": mountOrbitalTransfer,
  "energy-budget": mountEnergyBudget,
  "phase-progression": mountPhaseProgression
};

export function initSparkVisuals() {
  document.querySelectorAll('[data-component="spark-visual"]').forEach((figure) => {
    if (figure.dataset.svBound === "1") return;
    const dataEl = figure.querySelector("script.sp-visual-data");
    const stage = figure.querySelector(".sp-visual-stage");
    const controls = figure.querySelector(".sp-visual-controls");
    if (!dataEl || !stage || !controls) return;

    let payload;
    try {
      payload = JSON.parse(dataEl.textContent || "{}");
    } catch (_) {
      return;
    }

    const mountFn = REGISTRY[payload.type];
    if (typeof mountFn !== "function") return;

    figure.dataset.svBound = "1";
    mountFn(figure, stage, controls, payload);
  });
}

window.SparkInitVisuals = initSparkVisuals;
initSparkVisuals();
