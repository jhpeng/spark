// Spark Web Portal — Full Interactive Forecast Mind-Map Engine (Phase 4)
// Consumes enriched JSON embedded by web/build.py (tree + fork metadata, rationale, signals).

const NS = "http://www.w3.org/2000/svg";

export function initForecastMindMaps() {
  document.querySelectorAll('[data-component="forecast-tree"]').forEach((container) => {
    if (container.dataset.mmBound === "1") return;
    const dataEl = container.querySelector("script.sp-forecast-data");
    const canvas = container.querySelector(".sp-forecast-canvas");
    if (!dataEl || !canvas) return;

    let payload;
    try {
      payload = JSON.parse(dataEl.textContent || "{}");
    } catch (_) {
      return;
    }
    const nodes = payload.nodes || [];
    if (!nodes.length) return;
    container.dataset.mmBound = "1";

    const labels = payload.labels || {};
    const resLabels = labels.res_labels || {};

    // Build parent-child hierarchy and compute tidy horizontal mind-map coordinates
    const byId = Object.fromEntries(nodes.map((n) => [n.id, { ...n, children: [] }]));
    let root = null;
    nodes.forEach((n) => {
      const node = byId[n.id];
      if (n.parent && byId[n.parent]) {
        byId[n.parent].children.push(node);
      } else if (!root) {
        root = node;
      }
    });
    if (!root) return;

    const NODE_W = 200;
    const NODE_H = 66;
    const COL_GAP = 42;
    const ROW_GAP = 24;
    const PAD_X = 16;
    const HEADER_H = 34;
    const PAD_Y = 18;

    // Collect nodes per depth column in DFS order (preserves non-crossing parent-child ordering)
    const columns = [];
    function collectColumns(node, depth) {
      node.depth = depth;
      if (!columns[depth]) columns[depth] = [];
      columns[depth].push(node);
      node.children.forEach((ch) => collectColumns(ch, depth + 1));
    }
    collectColumns(root, 0);

    const numCols = columns.length;
    const maxColCount = Math.max(1, ...columns.map((c) => c.length));
    const usableH = Math.max(3, maxColCount) * (NODE_H + ROW_GAP);
    const baseW = PAD_X * 2 + numCols * NODE_W + Math.max(0, numCols - 1) * COL_GAP;
    const baseH = HEADER_H + PAD_Y * 2 + usableH;

    // Evenly distribute each column's nodes across the full height independent of parent Y
    const colHeaders = columns.map((colNodes, depth) => {
      const k = colNodes.length;
      const step = usableH / k;
      const x = PAD_X + depth * (NODE_W + COL_GAP);
      colNodes.forEach((node, idx) => {
        node.x = x;
        node.y = HEADER_H + PAD_Y + step * (idx + 0.5);
      });
      // Infer period/year header label for this column
      const sample = colNodes[0];
      const yrMatch = (sample.eyebrow + " " + sample.label + " " + sample.deadline).match(/\b(20\d{2}|21\d{2}|30\d{2})\b/);
      return {
        x,
        label: yrMatch ? yrMatch[1] : `L${depth}`
      };
    });

    const allNodes = Object.values(byId);

    function getAncestorSet(id) {
      const set = new Set();
      let cur = byId[id];
      while (cur) {
        set.add(cur.id);
        cur = cur.parent ? byId[cur.parent] : null;
      }
      return set;
    }

    canvas.innerHTML = "";

    // Toolbar: Resolution filters + Leaf sum check + Zoom controls
    const toolbar = document.createElement("div");
    toolbar.className = "sp-mm-toolbar";

    const filterGroup = document.createElement("div");
    filterGroup.className = "sp-mm-controls-group";
    const presentRes = ["all", ...Array.from(new Set(allNodes.filter((n) => n.parent).map((n) => n.resolution)))];
    let activeFilter = "all";

    presentRes.forEach((rk) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "sp-btn" + (rk === "all" ? " sp-btn--active" : "");
      btn.textContent = rk === "all" ? (labels.filter_all || "All") : (resLabels[rk] || rk);
      btn.addEventListener("click", () => {
        activeFilter = rk;
        filterGroup.querySelectorAll("button").forEach((b) => b.classList.toggle("sp-btn--active", b === btn));
        render();
      });
      filterGroup.appendChild(btn);
    });

    const rightGroup = document.createElement("div");
    rightGroup.className = "sp-mm-controls-group";

    if (typeof payload.leaf_sum === "number") {
      const sumBadge = document.createElement("span");
      sumBadge.className = "sp-badge sp-badge--occurred";
      sumBadge.textContent = `${labels.leaf_sum_check || "Leaf Sum"}: ${payload.leaf_sum.toFixed(1)}%`;
      rightGroup.appendChild(sumBadge);
    }

    let zoom = 1;
    const zoomOutBtn = document.createElement("button");
    zoomOutBtn.type = "button";
    zoomOutBtn.className = "sp-btn";
    zoomOutBtn.textContent = "−";
    zoomOutBtn.title = labels.zoom_out || "Zoom Out";

    const zoomFitBtn = document.createElement("button");
    zoomFitBtn.type = "button";
    zoomFitBtn.className = "sp-btn";
    zoomFitBtn.textContent = labels.zoom_reset || "Fit";

    const zoomInBtn = document.createElement("button");
    zoomInBtn.type = "button";
    zoomInBtn.className = "sp-btn";
    zoomInBtn.textContent = "+";
    zoomInBtn.title = labels.zoom_in || "Zoom In";

    rightGroup.append(zoomOutBtn, zoomFitBtn, zoomInBtn);
    toolbar.append(filterGroup, rightGroup);
    canvas.appendChild(toolbar);

    // SVG Mind-Map Stage
    const scrollWrap = document.createElement("div");
    scrollWrap.className = "sp-mm-scroll";

    const svg = document.createElementNS(NS, "svg");
    svg.setAttribute("class", "sp-mm-svg");
    svg.setAttribute("viewBox", `0 0 ${baseW} ${baseH}`);
    svg.setAttribute("role", "img");
    svg.setAttribute("aria-label", payload.title || "Forecast Mind-Map");
    scrollWrap.appendChild(svg);
    canvas.appendChild(scrollWrap);

    function applyZoom() {
      svg.style.width = `${Math.round(zoom * 100)}%`;
      svg.style.minWidth = `${Math.round(baseW * 0.85 * zoom)}px`;
    }
    zoomInBtn.addEventListener("click", () => { zoom = Math.min(1.6, zoom + 0.15); applyZoom(); });
    zoomOutBtn.addEventListener("click", () => { zoom = Math.max(0.75, zoom - 0.15); applyZoom(); });
    zoomFitBtn.addEventListener("click", () => { zoom = 1; svg.style.width = ""; svg.style.minWidth = ""; });

    // Rich Fork & Evidence Inspector
    const inspector = document.createElement("div");
    inspector.className = "sp-mm-inspector";
    inspector.setAttribute("aria-live", "polite");
    inspector.innerHTML = `
      <div>
        <div class="sp-eyebrow" data-ins="path"></div>
        <h3 data-ins="title"></h3>
        <p data-ins="question"></p>
        <p data-ins="rationale"></p>
        <div class="sp-mm-inspector-extra" data-ins="signals-wrap" hidden>
          <strong>${labels.signals_label || "Validation & Revision Signals"}:</strong>
          <span data-ins="signals"></span>
        </div>
        <div class="sp-mm-inspector-actions">
          <a class="sp-btn" data-ins="jump" hidden>${labels.jump_to_fork || "Jump to Fork ↓"}</a>
        </div>
      </div>
      <div class="sp-mm-inspector-stats">
        <div class="sp-metric">
          <div class="sp-metric-value" data-ins="cond">—</div>
          <div class="sp-metric-label">${labels.conditional_prob || "Conditional"}</div>
        </div>
        <div class="sp-metric">
          <div class="sp-metric-value" data-ins="cum">—</div>
          <div class="sp-metric-label">${labels.path_prob || "Cumulative Path"}</div>
        </div>
        <div class="sp-metric">
          <div class="sp-metric-value" data-ins="conf">—</div>
          <div class="sp-metric-label">${labels.confidence || "Confidence"}</div>
        </div>
        <div class="sp-metric">
          <div class="sp-metric-value" data-ins="res">—</div>
          <div class="sp-metric-label">${labels.resolution || "Resolution"}</div>
        </div>
      </div>
    `;
    canvas.appendChild(inspector);

    const insPath = inspector.querySelector('[data-ins="path"]');
    const insTitle = inspector.querySelector('[data-ins="title"]');
    const insQuestion = inspector.querySelector('[data-ins="question"]');
    const insRationale = inspector.querySelector('[data-ins="rationale"]');
    const insSignalsWrap = inspector.querySelector('[data-ins="signals-wrap"]');
    const insSignals = inspector.querySelector('[data-ins="signals"]');
    const insJump = inspector.querySelector('[data-ins="jump"]');
    const insCond = inspector.querySelector('[data-ins="cond"]');
    const insCum = inspector.querySelector('[data-ins="cum"]');
    const insConf = inspector.querySelector('[data-ins="conf"]');
    const insRes = inspector.querySelector('[data-ins="res"]');

    // Start with all columns brightly visible (no branch dimmed until user clicks a node)
    let selectedId = null;

    function updateInspector(node) {
      const chain = [];
      let cur = node;
      while (cur) {
        chain.unshift(cur.id);
        cur = cur.parent ? byId[cur.parent] : null;
      }
      insPath.textContent = `${labels.inherited_path || "Path"}: ${chain.join(" → ")}`;
      insTitle.textContent = `${node.eyebrow} · ${node.label}`;
      const dlPart = node.deadline ? ` (${labels.deadline || "Deadline"}: ${node.deadline})` : "";
      insQuestion.textContent = node.question ? `${node.question}${dlPart}` : "";
      insRationale.textContent = node.rationale || "";
      if (node.signals) {
        insSignals.textContent = " " + node.signals;
        insSignalsWrap.hidden = false;
      } else {
        insSignalsWrap.hidden = true;
      }
      if (node.fork_anchor) {
        insJump.setAttribute("href", `#${node.fork_anchor}`);
        insJump.hidden = false;
      } else {
        insJump.hidden = true;
      }
      insCond.textContent = node.cond || "100%";
      insCum.textContent = typeof node.cum === "number" ? `${node.cum.toFixed(1)}%` : "100.0%";
      insConf.textContent = node.confidence || "—";
      insRes.textContent = resLabels[node.resolution] || node.resolution || "active";
    }

    // Visual-width aware truncation (CJK wide chars count as 2 units so text never overflows card)
    function truncateVisual(str, maxUnits) {
      let units = 0;
      let out = "";
      for (const ch of str) {
        const w = ch.charCodeAt(0) > 0x2e7f ? 2 : 1;
        if (units + w > maxUnits) {
          return out.trimEnd() + "…";
        }
        out += ch;
        units += w;
      }
      return out;
    }

    function render() {
      svg.innerHTML = "";
      const activeSet = selectedId ? getAncestorSet(selectedId) : null;

      // Subtle column period headers & vertical alignment guides
      colHeaders.forEach((col) => {
        const cx = col.x + NODE_W / 2;
        const guide = document.createElementNS(NS, "line");
        guide.setAttribute("x1", String(cx));
        guide.setAttribute("y1", String(HEADER_H));
        guide.setAttribute("x2", String(cx));
        guide.setAttribute("y2", String(baseH - PAD_Y / 2));
        guide.setAttribute("stroke", "var(--border-subtle)");
        guide.setAttribute("stroke-dasharray", "3 6");
        svg.appendChild(guide);

        const hdr = document.createElementNS(NS, "text");
        hdr.setAttribute("x", String(cx));
        hdr.setAttribute("y", "20");
        hdr.setAttribute("text-anchor", "middle");
        hdr.setAttribute("class", "sp-mm-year");
        hdr.textContent = col.label;
        svg.appendChild(hdr);
      });

      allNodes.forEach((n) => {
        if (!n.parent || !byId[n.parent]) return;
        const p = byId[n.parent];
        const x1 = p.x + NODE_W;
        const y1 = p.y;
        const x2 = n.x;
        const y2 = n.y;
        const cx = (x1 + x2) / 2;

        const path = document.createElementNS(NS, "path");
        path.setAttribute("d", `M ${x1} ${y1} C ${cx} ${y1}, ${cx} ${y2}, ${x2} ${y2}`);
        const cumVal = typeof n.cum === "number" ? n.cum : 50;
        const strokeW = Math.max(1.2, Math.min(5.2, 1 + (cumVal / 100) * 5));
        path.setAttribute("stroke-width", strokeW.toFixed(2));
        const matchesFilter = activeFilter === "all" || n.resolution === activeFilter;
        const isActive = activeSet && activeSet.has(n.id) && activeSet.has(p.id);
        const isDim = !matchesFilter || (activeSet && !isActive);
        path.setAttribute("class", "sp-mm-edge" + (isActive ? " sp-mm-edge--active" : isDim ? " sp-mm-edge--dim" : ""));
        svg.appendChild(path);
      });

      allNodes.forEach((n) => {
        const g = document.createElementNS(NS, "g");
        const matchesFilter = activeFilter === "all" || !n.parent || n.resolution === activeFilter;
        const isActive = activeSet && activeSet.has(n.id);
        const isDim = !matchesFilter || (activeSet && !isActive);
        g.setAttribute("class", "sp-mm-node" + (isActive ? " sp-mm-node--active" : isDim ? " sp-mm-node--dim" : ""));
        g.setAttribute("transform", `translate(${n.x}, ${n.y - NODE_H / 2})`);
        g.setAttribute("tabindex", "0");
        g.setAttribute("role", "button");
        g.setAttribute("aria-label", `${n.label} (${n.cond || "100%"}, ${n.cum ?? 100}%)`);

        const rect = document.createElementNS(NS, "rect");
        rect.setAttribute("width", NODE_W);
        rect.setAttribute("height", NODE_H);
        rect.setAttribute("class", "sp-mm-node-box");
        g.appendChild(rect);

        const eyebrow = document.createElementNS(NS, "text");
        eyebrow.setAttribute("x", 12);
        eyebrow.setAttribute("y", 17);
        eyebrow.setAttribute("class", "sp-mm-year");
        eyebrow.textContent = truncateVisual(n.eyebrow || "NODE", 24);
        g.appendChild(eyebrow);

        const title = document.createElementNS(NS, "text");
        title.setAttribute("x", 12);
        title.setAttribute("y", 36);
        title.setAttribute("class", "sp-mm-title");
        title.textContent = truncateVisual(n.label, 21);
        g.appendChild(title);

        const sub = document.createElementNS(NS, "text");
        sub.setAttribute("x", 12);
        sub.setAttribute("y", 52);
        sub.setAttribute("class", "sp-mm-sub");
        const cumText = typeof n.cum === "number" ? `${n.cum.toFixed(1)}%` : "100.0%";
        sub.textContent = n.parent ? `${n.cond || "—"} · path ${cumText}` : `baseline · 100.0%`;
        g.appendChild(sub);

        const barBg = document.createElementNS(NS, "rect");
        barBg.setAttribute("x", 12);
        barBg.setAttribute("y", 58);
        barBg.setAttribute("width", NODE_W - 24);
        barBg.setAttribute("height", 2.5);
        barBg.setAttribute("class", "sp-mm-bar-bg");
        g.appendChild(barBg);

        const cumPct = typeof n.cum === "number" ? n.cum : 100;
        const barFill = document.createElementNS(NS, "rect");
        barFill.setAttribute("x", 12);
        barFill.setAttribute("y", 58);
        barFill.setAttribute("width", Math.max(4, ((NODE_W - 24) * cumPct) / 100));
        barFill.setAttribute("height", 2.5);
        barFill.setAttribute("class", "sp-mm-bar-fill");
        g.appendChild(barFill);

        const select = () => {
          selectedId = n.id;
          render();
          updateInspector(n);
        };
        g.addEventListener("click", select);
        g.addEventListener("keydown", (e) => {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            select();
          }
        });
        svg.appendChild(g);
      });
    }

    const resetBtn = container.querySelector('[data-action="reset-tree"]');
    if (resetBtn) {
      resetBtn.addEventListener("click", () => {
        selectedId = null;
        activeFilter = "all";
        filterGroup.querySelectorAll("button").forEach((b, i) => b.classList.toggle("sp-btn--active", i === 0));
        render();
        updateInspector(root);
      });
    }

    render();
    updateInspector(byId[selectedId] || root);
  });
}

window.SparkInitForecastTrees = initForecastMindMaps;
initForecastMindMaps();
