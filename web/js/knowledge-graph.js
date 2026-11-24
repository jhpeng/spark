// Spark Web Portal — Interactive Orbital Knowledge Dependency Graph (Phase 4)
// Consumes dist/graph.json and renders an observatory star-chart of entries & dependencies.

const NS = "http://www.w3.org/2000/svg";

function cssToken(name, fallback) {
  const val = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  return val || fallback;
}

export async function initKnowledgeGraphs() {
  const containers = document.querySelectorAll('[data-component="knowledge-graph"]');
  for (const container of containers) {
    if (container.dataset.kgBound === "1") continue;
    const cfgEl = container.querySelector("script.sp-kg-config");
    const mount = container.querySelector(".sp-kg-mount");
    if (!cfgEl || !mount) continue;
    container.dataset.kgBound = "1";

    let cfg;
    try {
      cfg = JSON.parse(cfgEl.textContent || "{}");
    } catch (_) {
      continue;
    }

    const rootPrefix = cfg.root || "";
    const lang = cfg.lang || "en";
    const labels = cfg.labels || {};
    const navLabels = cfg.nav_labels || {};
    const statusLabels = cfg.status_labels || {};
    const groundingLabels = cfg.grounding_labels || {};
    const kindLabels = cfg.kind_labels || {};

    let rawGraph;
    try {
      const resp = await fetch(`${rootPrefix}graph.json`);
      rawGraph = resp.ok ? await resp.json() : { nodes: [], edges: [] };
    } catch (_) {
      rawGraph = { nodes: [], edges: [] };
    }

    // Filter nodes for current language (exclude sessions for clean conceptual graph)
    const nodes = (rawGraph.nodes || []).filter((n) => n.lang === lang && n.section !== "sessions");
    const nodeIds = new Set(nodes.map((n) => n.id));
    const edges = (rawGraph.edges || []).filter((e) => nodeIds.has(e.source) && nodeIds.has(e.target));

    if (!nodes.length) continue;

    // Assign nodes to concentric observatory rings by category
    const CX = 480;
    const CY = 330;
    const RINGS = [
      { key: "canon", radius: 68, label: navLabels.canon || "Canon" },
      { key: "concept", radius: 162, label: navLabels.concepts || "Concepts" },
      { key: "tech-society", radius: 242, label: `${navLabels.tech || "Tech"} & ${navLabels.society || "Society"}` },
      { key: "outer", radius: 300, label: `${navLabels.forecasts || "Forecasts"} & ${navLabels.open_questions || "Open Q"}` }
    ];

    function bucketOf(n) {
      if (n.section === "canon") return 0;
      if (n.kind === "concept") return 1;
      if (n.kind === "tech" || n.kind === "society" || n.kind === "place" || n.kind === "era") return 2;
      return 3;
    }

    const buckets = [[], [], [], []];
    nodes.forEach((n) => buckets[bucketOf(n)].push(n));

    const pos = {};
    buckets.forEach((list, ringIdx) => {
      const r = RINGS[ringIdx].radius;
      const offsetAngle = -Math.PI / 2 + ringIdx * 0.35;
      list.forEach((n, idx) => {
        const angle = offsetAngle + (2 * Math.PI * idx) / Math.max(1, list.length);
        pos[n.id] = {
          x: CX + r * Math.cos(angle),
          y: CY + r * Math.sin(angle),
          angle
        };
      });
    });

    const byId = Object.fromEntries(nodes.map((n) => [n.id, n]));

    function nodeColorToken(n) {
      if (n.section === "canon") return "--status-canon-fg";
      if (n.section === "forecasts") return "--accent-primary";
      if (n.kind === "concept") return "--kind-concept-fg";
      if (n.kind === "tech") return "--kind-tech-fg";
      if (n.kind === "society") return "--kind-society-fg";
      return "--text-muted";
    }

    // Build toolbar
    mount.innerHTML = "";
    const toolbar = document.createElement("div");
    toolbar.className = "sp-kg-toolbar";

    const catGroup = document.createElement("div");
    catGroup.className = "sp-kg-filters";
    const categories = [
      ["all", labels.filter_all || "All"],
      ["canon", navLabels.canon || "Canon"],
      ["concept", navLabels.concepts || "Concepts"],
      ["tech", navLabels.tech || "Tech"],
      ["society", navLabels.society || "Society"],
      ["forecasts", navLabels.forecasts || "Forecasts"]
    ];

    let activeCat = "all";
    let showRefs = false;
    let selectedId = nodes.find((n) => n.src_rel?.includes("orbital-transportation-network") || n.id.includes("lunar-expansion"))?.id || nodes[0].id;

    categories.forEach(([key, label]) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "sp-btn" + (key === "all" ? " sp-btn--active" : "");
      btn.textContent = label;
      btn.addEventListener("click", () => {
        activeCat = key;
        catGroup.querySelectorAll("button").forEach((b) => b.classList.toggle("sp-btn--active", b === btn));
        render();
      });
      catGroup.appendChild(btn);
    });

    const edgeToggle = document.createElement("button");
    edgeToggle.type = "button";
    edgeToggle.className = "sp-btn";
    edgeToggle.textContent = labels.edge_depends || "Dependencies Only";
    edgeToggle.addEventListener("click", () => {
      showRefs = !showRefs;
      edgeToggle.classList.toggle("sp-btn--active", showRefs);
      edgeToggle.textContent = showRefs ? (labels.edge_all || "Dependencies + References") : (labels.edge_depends || "Dependencies Only");
      render();
    });

    toolbar.append(catGroup, edgeToggle);
    mount.appendChild(toolbar);

    // SVG Stage
    const stage = document.createElement("div");
    stage.className = "sp-kg-stage";
    const svg = document.createElementNS(NS, "svg");
    svg.setAttribute("class", "sp-kg-svg");
    svg.setAttribute("viewBox", "0 0 960 660");
    svg.setAttribute("role", "img");
    svg.setAttribute("aria-label", labels.title || "Knowledge Dependency Graph");
    stage.appendChild(svg);
    mount.appendChild(stage);

    // Legend
    const legend = document.createElement("div");
    legend.className = "sp-kg-legend";
    legend.innerHTML = `
      <span class="sp-kg-legend-item"><span class="sp-kg-swatch sp-kg-swatch--canon"></span>${navLabels.canon || "Canon"}</span>
      <span class="sp-kg-legend-item"><span class="sp-kg-swatch sp-kg-swatch--concept"></span>${navLabels.concepts || "Concepts"}</span>
      <span class="sp-kg-legend-item"><span class="sp-kg-swatch sp-kg-swatch--tech"></span>${navLabels.tech || "Tech"}</span>
      <span class="sp-kg-legend-item"><span class="sp-kg-swatch sp-kg-swatch--society"></span>${navLabels.society || "Society"}</span>
      <span class="sp-kg-legend-item"><span class="sp-kg-swatch sp-kg-swatch--forecasts"></span>${navLabels.forecasts || "Forecasts"}</span>
    `;
    mount.appendChild(legend);

    // Inspector
    const inspector = document.createElement("div");
    inspector.className = "sp-kg-inspector";
    inspector.setAttribute("aria-live", "polite");
    inspector.innerHTML = `
      <div>
        <div class="sp-eyebrow" data-kg="eyebrow"></div>
        <h3 data-kg="title"></h3>
        <div class="sp-meta" data-kg="badges"></div>
        <p data-kg="excerpt"></p>
        <a class="sp-btn sp-btn--primary" data-kg="open">${labels.open_entry || "Open Entry →"}</a>
      </div>
      <div class="sp-kg-rel-grid">
        <div>
          <h4 class="sp-rail-title">${labels.upstream || "Depends On"}</h4>
          <ul class="sp-rel-list" data-kg="upstream"></ul>
        </div>
        <div>
          <h4 class="sp-rail-title">${labels.downstream || "Referenced By"}</h4>
          <ul class="sp-rel-list" data-kg="downstream"></ul>
        </div>
      </div>
    `;
    mount.appendChild(inspector);

    const elEyebrow = inspector.querySelector('[data-kg="eyebrow"]');
    const elTitle = inspector.querySelector('[data-kg="title"]');
    const elBadges = inspector.querySelector('[data-kg="badges"]');
    const elExcerpt = inspector.querySelector('[data-kg="excerpt"]');
    const elOpen = inspector.querySelector('[data-kg="open"]');
    const elUp = inspector.querySelector('[data-kg="upstream"]');
    const elDown = inspector.querySelector('[data-kg="downstream"]');

    function matchesCategory(n) {
      if (activeCat === "all") return true;
      if (activeCat === "canon" || activeCat === "forecasts") return n.section === activeCat;
      return n.kind === activeCat;
    }

    function activeEdges() {
      return showRefs ? edges : edges.filter((e) => e.type === "depends_on");
    }

    function updateInspector(node) {
      const curEdges = activeEdges();
      const upIds = Array.from(new Set(curEdges.filter((e) => e.source === node.id).map((e) => e.target)));
      const downIds = Array.from(new Set(curEdges.filter((e) => e.target === node.id).map((e) => e.source)));

      elEyebrow.textContent = node.id;
      elTitle.textContent = node.title;
      elExcerpt.textContent = node.excerpt || labels.select_hint || "";
      elOpen.setAttribute("href", `${rootPrefix}${node.url}`);

      const badges = [];
      if (node.kind && kindLabels[node.kind]) {
        badges.push(`<span class="sp-badge">${kindLabels[node.kind]}</span>`);
      }
      if (node.status) {
        badges.push(`<span class="sp-badge sp-badge--${node.status}">${statusLabels[node.status] || node.status}</span>`);
      }
      if (node.grounding) {
        badges.push(`<span class="sp-badge sp-badge--${node.grounding}">${groundingLabels[node.grounding] || node.grounding}</span>`);
      }
      elBadges.innerHTML = badges.join("");

      const makeRelList = (ids, targetEl) => {
        targetEl.innerHTML = "";
        if (!ids.length) {
          targetEl.innerHTML = `<li class="sp-mono">—</li>`;
          return;
        }
        ids.forEach((tid) => {
          const tNode = byId[tid];
          if (!tNode) return;
          const li = document.createElement("li");
          const a = document.createElement("a");
          a.href = `${rootPrefix}${tNode.url}`;
          a.textContent = tNode.title;
          li.appendChild(a);
          targetEl.appendChild(li);
        });
      };
      makeRelList(upIds, elUp);
      makeRelList(downIds, elDown);
    }

    function truncate(str, max) {
      return str.length > max ? str.slice(0, max - 1) + "…" : str;
    }

    function render() {
      svg.innerHTML = "";
      const curEdges = activeEdges();
      const upstreamSet = new Set(curEdges.filter((e) => e.source === selectedId).map((e) => e.target));
      const downstreamSet = new Set(curEdges.filter((e) => e.target === selectedId).map((e) => e.source));
      const relatedSet = new Set([selectedId, ...upstreamSet, ...downstreamSet]);

      // Concentric observatory orbit rings
      RINGS.forEach((ring) => {
        const c = document.createElementNS(NS, "circle");
        c.setAttribute("cx", CX);
        c.setAttribute("cy", CY);
        c.setAttribute("r", ring.radius);
        c.setAttribute("class", "sp-kg-ring");
        svg.appendChild(c);

        const lbl = document.createElementNS(NS, "text");
        lbl.setAttribute("x", CX + 6);
        lbl.setAttribute("y", CY - ring.radius + 12);
        lbl.setAttribute("class", "sp-kg-ring-label");
        lbl.textContent = ring.label;
        svg.appendChild(lbl);
      });

      // Curved edges
      curEdges.forEach((e) => {
        const p1 = pos[e.source];
        const p2 = pos[e.target];
        if (!p1 || !p2) return;
        const mx = (p1.x + p2.x) / 2;
        const my = (p1.y + p2.y) / 2;
        const qx = mx + (CX - mx) * 0.22;
        const qy = my + (CY - my) * 0.22;

        const path = document.createElementNS(NS, "path");
        path.setAttribute("d", `M ${p1.x.toFixed(1)} ${p1.y.toFixed(1)} Q ${qx.toFixed(1)} ${qy.toFixed(1)} ${p2.x.toFixed(1)} ${p2.y.toFixed(1)}`);

        let cls = "sp-kg-edge";
        if (e.type === "reference") cls += " sp-kg-edge--ref";
        const catVisible = matchesCategory(byId[e.source]) && matchesCategory(byId[e.target]);
        if (e.source === selectedId) cls += " sp-kg-edge--upstream";
        else if (e.target === selectedId) cls += " sp-kg-edge--downstream";
        else if (!catVisible || selectedId) cls += " sp-kg-edge--dim";

        path.setAttribute("class", cls);
        svg.appendChild(path);
      });

      // Orbital nodes
      nodes.forEach((n) => {
        const p = pos[n.id];
        const g = document.createElementNS(NS, "g");
        const isActive = n.id === selectedId;
        const isRelated = relatedSet.has(n.id);
        const isVisible = matchesCategory(n);
        g.setAttribute("class", "sp-kg-node" + (isActive ? " sp-kg-node--active" : !isVisible || !isRelated ? " sp-kg-node--dim" : ""));
        g.setAttribute("transform", `translate(${p.x.toFixed(1)}, ${p.y.toFixed(1)})`);
        g.setAttribute("tabindex", "0");
        g.setAttribute("role", "button");
        g.setAttribute("aria-label", n.title);

        const dot = document.createElementNS(NS, "circle");
        dot.setAttribute("r", isActive ? "8.5" : n.section === "canon" ? "7.5" : "6");
        dot.setAttribute("class", "sp-kg-dot");
        dot.setAttribute("fill", `var(${nodeColorToken(n)})`);
        g.appendChild(dot);

        const label = document.createElementNS(NS, "text");
        const onLeft = Math.cos(p.angle) < -0.15;
        label.setAttribute("x", onLeft ? -12 : 12);
        label.setAttribute("y", 4);
        label.setAttribute("text-anchor", onLeft ? "end" : "start");
        label.setAttribute("class", "sp-kg-label");
        label.textContent = truncate(n.title, 20);
        g.appendChild(label);

        const selectNode = () => {
          selectedId = n.id;
          render();
          updateInspector(n);
        };
        g.addEventListener("click", selectNode);
        g.addEventListener("keydown", (ev) => {
          if (ev.key === "Enter" || ev.key === " ") {
            ev.preventDefault();
            selectNode();
          }
        });
        svg.appendChild(g);
      });
    }

    render();
    if (byId[selectedId]) updateInspector(byId[selectedId]);
  }
}

window.SparkInitKnowledgeGraphs = initKnowledgeGraphs;
initKnowledgeGraphs();
