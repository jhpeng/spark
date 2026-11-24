// Spark Declarative Visual Engine: phase-progression
// Interactive step-by-step milestone evolution with optional auto-play.

export function mountPhaseProgression(figure, stage, controls, payload) {
  const params = payload.params || {};
  const labels = payload.labels || {};
  const stages = Array.isArray(params.stages) ? params.stages : [];
  if (!stages.length) return;

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let activeIdx = 0;
  let timer = null;

  const playBtn = document.createElement("button");
  playBtn.type = "button";
  playBtn.className = "sp-btn";
  const resetBtn = document.createElement("button");
  resetBtn.type = "button";
  resetBtn.className = "sp-btn";
  resetBtn.textContent = labels.reset || "Reset";
  controls.append(playBtn, resetBtn);

  stage.innerHTML = "";
  const track = document.createElement("div");
  track.className = "sp-pp-track";

  const detail = document.createElement("div");
  detail.className = "sp-pp-detail";
  detail.setAttribute("aria-live", "polite");
  detail.innerHTML = `
    <div class="sp-eyebrow" data-pp="metric"></div>
    <h4 data-pp="heading"></h4>
    <p data-pp="summary"></p>
  `;

  const stepBtns = stages.map((st, idx) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "sp-pp-step";
    btn.innerHTML = `
      <div class="sp-pp-code">${st.code || `0${idx + 1}`}</div>
      <div class="sp-pp-name">${st.label || ""}</div>
    `;
    btn.addEventListener("click", () => {
      stopAuto();
      setActive(idx);
    });
    track.appendChild(btn);
    return btn;
  });

  stage.append(track, detail);

  const elMetric = detail.querySelector('[data-pp="metric"]');
  const elHeading = detail.querySelector('[data-pp="heading"]');
  const elSummary = detail.querySelector('[data-pp="summary"]');

  function setActive(idx) {
    activeIdx = idx % stages.length;
    stepBtns.forEach((b, i) => b.classList.toggle("sp-pp-step--active", i === activeIdx));
    const cur = stages[activeIdx];
    elMetric.textContent = cur.metric ? `${cur.code || ""} · ${cur.metric}` : (cur.code || "");
    elHeading.textContent = cur.label || "";
    elSummary.textContent = cur.summary || "";
  }

  function syncBtn() {
    playBtn.textContent = timer ? (labels.pause || "Pause") : (labels.play || "Play");
  }

  function stopAuto() {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
    syncBtn();
  }

  function startAuto() {
    if (timer || reducedMotion) return;
    timer = setInterval(() => {
      if (!figure.isConnected) {
        stopAuto();
        return;
      }
      setActive(activeIdx + 1);
    }, 3200);
    syncBtn();
  }

  playBtn.addEventListener("click", () => {
    if (timer) stopAuto();
    else {
      timer = setInterval(() => {
        if (!figure.isConnected) {
          stopAuto();
          return;
        }
        setActive(activeIdx + 1);
      }, 3200);
      syncBtn();
    }
  });

  resetBtn.addEventListener("click", () => {
    stopAuto();
    setActive(0);
  });

  setActive(0);
  syncBtn();
  if (!reducedMotion) startAuto();
}
