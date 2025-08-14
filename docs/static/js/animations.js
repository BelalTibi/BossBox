// Reveal .fade-in elements when they enter the screen
document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".fade-in");
  if (!("IntersectionObserver" in window)) {
    items.forEach(el => el.classList.add("show"));
    return;
  }
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("show");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });
  items.forEach(el => observer.observe(el));
});
// Light/Dark toggle using Bootstrap 5.3 data attribute
(function () {
  const key = "bb-theme";
  const btn = document.getElementById("themeToggle");
  const root = document.documentElement;

  function apply(theme) {
    root.setAttribute("data-bs-theme", theme);
    if (btn) btn.textContent = theme === "dark" ? "Light" : "Dark";
  }

  // Load saved preference (default light)
  const saved = localStorage.getItem(key);
  apply(saved || "light");

  if (btn) {
    btn.addEventListener("click", () => {
      const now = root.getAttribute("data-bs-theme") === "dark" ? "light" : "dark";
      apply(now);
      localStorage.setItem(key, now);
    });
  }
})();
