document.querySelectorAll(".project-browser").forEach((browser) => {
  const filters = browser.querySelector(".filters");
  filters.hidden = false;
  filters.addEventListener("click", (event) => {
    const button = event.target.closest("button[data-filter]");
    if (!button) return;
    filters.querySelectorAll("button").forEach((item) => {
      item.setAttribute("aria-pressed", String(item === button));
    });
    browser.querySelectorAll("[data-category]").forEach((project) => {
      project.hidden = button.dataset.filter !== "all"
        && project.dataset.category !== button.dataset.filter;
    });
  });
});

const motion = window.matchMedia("(prefers-reduced-motion: reduce)");
if (!motion.matches && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("revealed");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });
  document.querySelectorAll(".panel, .position, .project-browser").forEach((element) => {
    element.classList.add("reveal");
    observer.observe(element);
  });
  motion.addEventListener("change", () => {
    if (motion.matches) {
      document.querySelectorAll(".reveal").forEach((element) => element.classList.add("revealed"));
      observer.disconnect();
    }
  });
}

document.querySelectorAll('.explorer').forEach((explorer) => {
  explorer.querySelector('.module-controls').addEventListener('click', (event) => {
    const selected = event.target.closest('button[data-module]');
    if (!selected) return;
    explorer.querySelectorAll('button[data-module]').forEach((button) => {
      button.setAttribute('aria-pressed', String(button === selected));
    });
    explorer.querySelectorAll('.module-panel').forEach((panel) => {
      panel.hidden = panel.id !== selected.getAttribute('aria-controls');
    });
  });
});
