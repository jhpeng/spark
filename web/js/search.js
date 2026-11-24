// Spark Web Portal — Offline Client-Side Search (supports flash-free PJAX navigation)

(function initSearch() {
  const backdrop = document.getElementById("sp-search-backdrop");
  const input = document.getElementById("sp-search-input");
  const resultsEl = document.getElementById("sp-search-results");
  if (!backdrop || !input || !resultsEl) return;

  const indexCache = {};

  function getContext() {
    return {
      lang: document.body.getAttribute("data-lang") || "en",
      rootPrefix: document.body.getAttribute("data-root") || "",
      noResultsText: backdrop.getAttribute("data-empty-text") || "No matching entries found."
    };
  }

  async function loadIndex(lang, rootPrefix) {
    if (indexCache[lang]) return indexCache[lang];
    const file = lang === "zh-tw" ? "search-index-zh-tw.json" : "search-index-en.json";
    try {
      const resp = await fetch(rootPrefix + file);
      indexCache[lang] = resp.ok ? await resp.json() : [];
    } catch (_) {
      indexCache[lang] = [];
    }
    return indexCache[lang];
  }

  function escapeHtml(str) {
    return str
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  async function renderResults(query) {
    const { lang, rootPrefix, noResultsText } = getContext();
    const indexData = await loadIndex(lang, rootPrefix);
    const q = query.trim().toLowerCase();
    const matches = !q
      ? indexData.slice(0, 12)
      : indexData
          .map((item) => {
            const title = (item.title || "").toLowerCase();
            const text = (item.text || "").toLowerCase();
            const meta = `${item.section || ""} ${item.kind || ""} ${item.status || ""} ${item.grounding || ""}`.toLowerCase();
            let score = 0;
            if (title.includes(q)) score += 10;
            if (meta.includes(q)) score += 4;
            if (text.includes(q)) score += 2;
            return { item, score };
          })
          .filter((x) => x.score > 0)
          .sort((a, b) => b.score - a.score)
          .slice(0, 18)
          .map((x) => x.item);

    if (!matches.length) {
      resultsEl.innerHTML = `<li class="sp-search-empty">${escapeHtml(noResultsText)}</li>`;
      return;
    }

    resultsEl.innerHTML = matches
      .map((item) => {
        const metaParts = [item.section, item.kind, item.status, item.grounding].filter(Boolean);
        return `<li>
          <a class="sp-search-item" href="${escapeHtml(rootPrefix + item.url)}">
            <div class="sp-search-item-title">${escapeHtml(item.title)}</div>
            <div class="sp-search-item-meta">${escapeHtml(metaParts.join(" · "))}</div>
            <div class="sp-search-item-excerpt">${escapeHtml(item.excerpt || "")}</div>
          </a>
        </li>`;
      })
      .join("");
  }

  async function openSearch() {
    backdrop.hidden = false;
    input.focus();
    input.select();
    await renderResults(input.value);
  }

  function closeSearch() {
    backdrop.hidden = true;
  }

  // Event delegation so dynamically swapped headers stay wired
  document.addEventListener("click", (e) => {
    const trigger = e.target.closest('[data-action="open-search"]');
    if (trigger) {
      openSearch();
      return;
    }
    if (e.target === backdrop || e.target.closest(".sp-search-item")) {
      closeSearch();
    }
  });

  input.addEventListener("input", () => renderResults(input.value));

  document.addEventListener("keydown", (e) => {
    if ((e.key === "k" || e.key === "K") && (e.metaKey || e.ctrlKey)) {
      e.preventDefault();
      if (backdrop.hidden) openSearch();
      else closeSearch();
    } else if (e.key === "/" && backdrop.hidden && !["INPUT", "TEXTAREA", "SELECT"].includes(document.activeElement?.tagName)) {
      e.preventDefault();
      openSearch();
    } else if (e.key === "Escape" && !backdrop.hidden) {
      closeSearch();
    }
  });
})();
