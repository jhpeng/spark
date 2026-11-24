// Spark Declarative Visual Engine: orbital-transfer
// Illustrates staged electromagnetic acceleration and opposite module recoil.

const NS = "http://www.w3.org/2000/svg";

export function mountOrbitalTransfer(figure, stage, controls, payload) {
  const params = payload.params || {};
  const labels = payload.labels || {};
  const originLabel = params.origin_label || "Entry";
  const targetLabel = params.target_label || "Departure";
  const deltaV = Number(params.delta_v_km_s || 10);
  const massT = Number(params.payload_mass_t || 100);
  const showRecoil = params.show_recoil !== false;

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let playing = !reducedMotion;
  let progress = reducedMotion ? 0.62 : 0; // 0..1 along the formation
  let lastTs = null;

  // Play / Pause / Reset controls
  const playBtn = document.createElement("button");
  playBtn.type = "button";
  playBtn.className = "sp-btn";
  const resetBtn = document.createElement("button");
  resetBtn.type = "button";
  resetBtn.className = "sp-btn";
  resetBtn.textContent = labels.reset || "Reset";
  controls.append(playBtn, resetBtn);

  function syncPlayLabel() {
    playBtn.textContent = playing ? (labels.pause || "Pause") : (labels.play || "Play");
  }
  syncPlayLabel();

  const W = 760;
  const H = 230;
  const TRACK_Y = 112;
  const START_X = 68;
  const END_X = 692;
  const MODULE_XS = [180, 290, 400, 510, 620];

  const svg = document.createElementNS(NS, "svg");
  svg.setAttribute("class", "sp-visual-svg");
  svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-label", payload.title || "Orbital Transfer Schematic");
  stage.innerHTML = "";
  stage.appendChild(svg);

  function el(tag, attrs = {}) {
    const node = document.createElementNS(NS, tag);
    Object.entries(attrs).forEach(([k, v]) => node.setAttribute(k, String(v)));
    return node;
  }

  // Trajectory baseline
  svg.appendChild(el("line", {
    x1: START_X, y1: TRACK_Y, x2: END_X, y2: TRACK_Y,
    stroke: "var(--border-default)", "stroke-width": 1.5, "stroke-dasharray": "4 6"
  }));

  // Endpoint labels
  const tStart = el("text", { x: START_X, y: 34, fill: "var(--text-muted)", "font-family": "var(--font-mono)", "font-size": 11 });
  tStart.textContent = originLabel;
  const tEnd = el("text", { x: END_X, y: 34, "text-anchor": "end", fill: "var(--accent-primary)", "font-family": "var(--font-mono)", "font-size": 11 });
  tEnd.textContent = targetLabel;
  svg.append(tStart, tEnd);

  // Accelerator modules (upper & lower ring halves + recoil vectors)
  const moduleGroups = MODULE_XS.map((mx, idx) => {
    const g = el("g");
    const upper = el("rect", { x: mx - 14, y: TRACK_Y - 46, width: 28, height: 14, rx: 3, fill: "var(--bg-surface-elevated)", stroke: "var(--border-strong)", "stroke-width": 1.2 });
    const lower = el("rect", { x: mx - 14, y: TRACK_Y + 32, width: 28, height: 14, rx: 3, fill: "var(--bg-surface-elevated)", stroke: "var(--border-strong)", "stroke-width": 1.2 });
    const pulse = el("ellipse", { cx: mx, cy: TRACK_Y, rx: 7, ry: 28, fill: "none", stroke: "var(--val-physics-accent)", "stroke-width": 1.5, opacity: 0.15 });
    const recoilArrow = el("line", { x1: mx, y1: TRACK_Y + 56, x2: mx - 28, y2: TRACK_Y + 56, stroke: "var(--val-open-question-accent)", "stroke-width": 2, opacity: 0 });
    const modLbl = el("text", { x: mx, y: TRACK_Y - 54, "text-anchor": "middle", fill: "var(--text-muted)", "font-family": "var(--font-mono)", "font-size": 9.5 });
    modLbl.textContent = `M${idx + 1}`;
    g.append(upper, lower, pulse, recoilArrow, modLbl);
    svg.appendChild(g);
    return { g, mx, pulse, recoilArrow, upper, lower };
  });

  // Ship glyph + velocity trail
  const trail = el("line", { x1: START_X, y1: TRACK_Y, x2: START_X, y2: TRACK_Y, stroke: "var(--accent-primary)", "stroke-width": 2.5, opacity: 0.7 });
  const ship = el("polygon", { points: "-10,-6 12,0 -10,6 -6,0", fill: "var(--accent-primary)", stroke: "var(--bg-canvas)", "stroke-width": 1 });
  svg.append(trail, ship);

  // Live telemetry HUD bar
  const hudVel = el("text", { x: START_X, y: H - 18, fill: "var(--text-primary)", "font-family": "var(--font-mono)", "font-size": 12 });
  const hudMass = el("text", { x: W / 2, y: H - 18, "text-anchor": "middle", fill: "var(--text-secondary)", "font-family": "var(--font-mono)", "font-size": 11 });
  hudMass.textContent = `m = ${massT} t · Δv = ${deltaV} km/s`;
  const hudRecoil = el("text", { x: END_X, y: H - 18, "text-anchor": "end", fill: "var(--val-open-question-accent)", "font-family": "var(--font-mono)", "font-size": 11 });
  hudRecoil.textContent = showRecoil ? (labels.recoil_note || "Opposite Module Recoil (−mΔv)") : "";
  svg.append(hudVel, hudMass, hudRecoil);

  function drawFrame(p) {
    // Ease-in quadratic motion: constant acceleration -> x proportional to t^2, v proportional to t
    const easedX = START_X + (END_X - START_X) * (p * p);
    const currentV = deltaV * p;
    ship.setAttribute("transform", `translate(${easedX.toFixed(1)}, ${TRACK_Y})`);
    trail.setAttribute("x1", String(Math.max(START_X, easedX - 24 - 65 * p)));
    trail.setAttribute("x2", easedX.toFixed(1));
    hudVel.textContent = `${labels.velocity_now || "Velocity"}: ${currentV.toFixed(2)} km/s`;

    moduleGroups.forEach(({ g, mx, pulse, recoilArrow, upper, lower }) => {
      const dist = easedX - mx;
      const near = Math.abs(dist) < 28;
      const passed = dist > 0;
      const recoilShift = showRecoil && passed ? -Math.min(18, (dist / 120) * 18) : 0;
      g.setAttribute("transform", `translate(${recoilShift.toFixed(1)}, 0)`);
      pulse.setAttribute("opacity", near ? "0.95" : passed ? "0.28" : "0.12");
      upper.setAttribute("stroke", near ? "var(--accent-primary)" : "var(--border-strong)");
      lower.setAttribute("stroke", near ? "var(--accent-primary)" : "var(--border-strong)");
      recoilArrow.setAttribute("opacity", showRecoil && passed ? "0.9" : "0");
    });
  }

  function tick(ts) {
    if (!figure.isConnected) return;
    if (playing) {
      if (lastTs !== null) {
        const dt = Math.min(0.05, (ts - lastTs) / 1000);
        progress += dt * 0.24;
        if (progress > 1.15) progress = 0;
      }
      lastTs = ts;
      drawFrame(Math.min(1, progress));
      requestAnimationFrame(tick);
    } else {
      lastTs = null;
    }
  }

  playBtn.addEventListener("click", () => {
    playing = !playing;
    syncPlayLabel();
    if (playing) {
      lastTs = null;
      requestAnimationFrame(tick);
    }
  });

  resetBtn.addEventListener("click", () => {
    progress = 0;
    lastTs = null;
    drawFrame(0);
  });

  drawFrame(Math.min(1, progress));
  if (playing) requestAnimationFrame(tick);
}
