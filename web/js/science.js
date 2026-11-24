// Spark Web Portal — Scientific Rendering (KaTeX math + Canon Timeline branch filters)

export function initScienceWidgets() {
  // 1. Render LaTeX math via KaTeX auto-render if available
  if (typeof window.renderMathInElement === "function") {
    const main = document.querySelector("main.sp-main");
    if (main) {
      try {
        window.renderMathInElement(main, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "\\[", right: "\\]", display: true },
            { left: "$", right: "$", display: false },
            { left: "\\(", right: "\\)", display: false }
          ],
          ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"],
          throwOnError: false
        });
      } catch (_) {}
    }
  }

  // 2. Canon Timeline branch filter buttons
  document.querySelectorAll('[data-component="timeline-filter"]').forEach((bar) => {
    if (bar.dataset.tlBound === "1") return;
    bar.dataset.tlBound = "1";
    const buttons = bar.querySelectorAll("[data-timeline-filter]");
    const items = document.querySelectorAll(".sp-timeline-item");
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const key = btn.getAttribute("data-timeline-filter");
        buttons.forEach((b) => b.classList.toggle("sp-btn--active", b === btn));
        items.forEach((item) => {
          item.hidden = key !== "all" && item.getAttribute("data-branch") !== key;
        });
      });
    });
  });
}

window.SparkInitScience = initScienceWidgets;

// Run once DOM + deferred KaTeX scripts are ready
if (document.readyState === "complete") {
  initScienceWidgets();
} else {
  window.addEventListener("load", initScienceWidgets, { once: true });
}
