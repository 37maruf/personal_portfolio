(function () {
  "use strict";

  /* ---- Light / dark theme ---- */
  var root = document.documentElement;
  var toggle = document.getElementById("themeToggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  }

  /* ---- Reveal cards: hover with a mouse, click or tap to pin open ---- */
  document.querySelectorAll(".rc").forEach(function (card) {
    var pinned = false;

    function setOpen(open) {
      card.classList.toggle("open", open);
      card.setAttribute("aria-expanded", open ? "true" : "false");
    }

    card.addEventListener("mouseenter", function () { setOpen(true); });
    card.addEventListener("mouseleave", function () { if (!pinned) setOpen(false); });
    card.addEventListener("click", function (e) {
      if (e.target.closest("a")) return;          // let links work normally
      pinned = !pinned;
      setOpen(pinned);
    });
    card.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        pinned = !pinned;
        setOpen(pinned);
      }
    });
    card.addEventListener("blur", function () { if (!pinned) setOpen(false); });
    card.addEventListener("focus", function () { setOpen(true); });
  });

  /* ---- Typing effect on the home page ---- */
  var typed = document.getElementById("typed");
  if (typed && typed.dataset.roles) {
    var roles = typed.dataset.roles.split(",").map(function (r) { return r.trim(); }).filter(Boolean);
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (roles.length > 1 && !reduce) {
      var r = 0, c = roles[0].length, deleting = true;
      (function tick() {
        var word = roles[r];
        typed.textContent = word.slice(0, c);
        var delay = deleting ? 45 : 85;
        if (deleting) {
          c--;
          if (c < 0) { deleting = false; r = (r + 1) % roles.length; c = 0; delay = 300; }
        } else {
          c++;
          if (c > roles[r].length) { deleting = true; c = roles[r].length; delay = 1500; }
        }
        setTimeout(tick, delay);
      })();
    }
  }
})();
