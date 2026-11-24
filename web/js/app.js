// Spark Web Portal — Core UI & Zero-Flash Client-Side Navigation (PJAX)

const STORAGE_KEY = "spark-theme";

function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  const meta = document.querySelector('meta[name="color-scheme"]');
  if (meta) meta.setAttribute("content", theme);
  try {
    localStorage.setItem(STORAGE_KEY, theme);
  } catch (_) {}
}

async function hydratePageWidgets() {
  if (typeof window.SparkInitScience === "function") {
    window.SparkInitScience();
  }
  if (typeof window.SparkInitVisuals === "function") {
    window.SparkInitVisuals();
  }
  if (document.querySelector('[data-component="forecast-tree"]')) {
    if (typeof window.SparkInitForecastTrees === "function") {
      window.SparkInitForecastTrees();
    } else {
      try {
        const mod = await import("./forecast-tree.js");
        if (mod && typeof mod.initForecastMindMaps === "function") {
          mod.initForecastMindMaps();
        }
      } catch (_) {}
    }
  }
  if (document.querySelector('[data-component="knowledge-graph"]')) {
    if (typeof window.SparkInitKnowledgeGraphs === "function") {
      window.SparkInitKnowledgeGraphs();
    } else {
      try {
        const mod = await import("./knowledge-graph.js");
        if (mod && typeof mod.initKnowledgeGraphs === "function") {
          mod.initKnowledgeGraphs();
        }
      } catch (_) {}
    }
  }
}

async function navigateSmooth(url, pushHistory = true) {
  try {
    const targetUrl = new URL(url, window.location.href);
    const resp = await fetch(targetUrl.href, { credentials: "same-origin" });
    if (!resp.ok) {
      window.location.href = targetUrl.href;
      return;
    }
    const htmlText = await resp.text();
    const doc = new DOMParser().parseFromString(htmlText, "text/html");

    const newHeader = doc.querySelector("header.sp-header");
    const curHeader = document.querySelector("header.sp-header");
    const newShell = doc.querySelector(".sp-shell");
    const curShell = document.querySelector(".sp-shell");

    if (!newHeader || !curHeader || !newShell || !curShell) {
      window.location.href = targetUrl.href;
      return;
    }

    const prevSidebar = curShell.querySelector(".sp-sidebar");
    const prevSidebarScroll = prevSidebar ? prevSidebar.scrollTop : 0;

    if (pushHistory) {
      window.history.pushState({ sparkUrl: targetUrl.href }, "", targetUrl.href);
    }

    // Swap header and page shell without tearing down the document or repainting white
    curHeader.replaceWith(newHeader);
    curShell.replaceWith(newShell);

    const nextSidebar = document.querySelector(".sp-sidebar");
    if (nextSidebar && prevSidebarScroll > 0) {
      nextSidebar.scrollTop = prevSidebarScroll;
    }

    document.title = doc.title;
    document.documentElement.lang = doc.documentElement.lang || "en";
    ["data-archetype", "data-lang", "data-root"].forEach((attr) => {
      const val = doc.body.getAttribute(attr);
      if (val !== null) document.body.setAttribute(attr, val);
    });

    // Sync localized search modal labels
    const newBackdrop = doc.getElementById("sp-search-backdrop");
    const curBackdrop = document.getElementById("sp-search-backdrop");
    const newInput = doc.getElementById("sp-search-input");
    const curInput = document.getElementById("sp-search-input");
    if (newBackdrop && curBackdrop) {
      curBackdrop.setAttribute("data-empty-text", newBackdrop.getAttribute("data-empty-text") || "");
    }
    if (newInput && curInput) {
      curInput.setAttribute("placeholder", newInput.getAttribute("placeholder") || "");
    }

    await hydratePageWidgets();

    if (targetUrl.hash) {
      const targetEl = document.getElementById(decodeURIComponent(targetUrl.hash.slice(1)));
      if (targetEl) {
        targetEl.scrollIntoView({ behavior: "instant" });
      } else {
        window.scrollTo(0, 0);
      }
    } else {
      window.scrollTo(0, 0);
    }
  } catch (_) {
    window.location.href = url;
  }
}

(function initApp() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved === "light" || saved === "dark") {
      applyTheme(saved);
    }
  } catch (_) {}

  // Delegated click handler for theme toggle, mobile nav, and zero-flash internal links
  document.addEventListener("click", (e) => {
    const themeBtn = e.target.closest('[data-action="toggle-theme"]');
    if (themeBtn) {
      const current = document.documentElement.getAttribute("data-theme") || "dark";
      applyTheme(current === "dark" ? "light" : "dark");
      return;
    }

    const navBtn = e.target.closest('[data-action="toggle-nav"]');
    const sidebar = document.querySelector(".sp-sidebar");
    if (navBtn && sidebar) {
      sidebar.classList.toggle("sp-sidebar--open");
      return;
    }
    if (sidebar && sidebar.classList.contains("sp-sidebar--open") && !sidebar.contains(e.target)) {
      sidebar.classList.remove("sp-sidebar--open");
    }

    // Intercept same-origin internal HTML links for zero-flash navigation
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) {
      return;
    }
    const anchor = e.target.closest("a[href]");
    if (!anchor) return;
    if (anchor.hasAttribute("download") || anchor.getAttribute("target") === "_blank") return;

    const rawHref = anchor.getAttribute("href");
    if (!rawHref || rawHref.startsWith("#") || rawHref.startsWith("mailto:")) return;

    // Only use fetch-based PJAX over http/https (not file://)
    if (window.location.protocol !== "http:" && window.location.protocol !== "https:") return;

    const dest = new URL(anchor.href, window.location.href);
    if (dest.origin !== window.location.origin) return;
    if (dest.pathname === window.location.pathname && dest.search === window.location.search) {
      return;
    }

    e.preventDefault();
    navigateSmooth(dest.href, true);
  });

  window.addEventListener("popstate", () => {
    if (window.location.protocol === "http:" || window.location.protocol === "https:") {
      navigateSmooth(window.location.href, false);
    }
  });

  // Exclusive accordion behavior for sidebar <details> groups (cross-browser fallback)
  document.addEventListener(
    "toggle",
    (e) => {
      const target = e.target;
      if (!(target instanceof HTMLDetailsElement) || !target.classList.contains("sp-nav-group") || !target.open) {
        return;
      }
      const sidebar = target.closest(".sp-sidebar");
      if (!sidebar) return;
      sidebar.querySelectorAll("details.sp-nav-group[open]").forEach((other) => {
        if (other !== target) other.open = false;
      });
    },
    true
  );
})();
