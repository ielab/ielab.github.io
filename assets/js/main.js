/* ielab.io — site interactions (no dependencies) */
(function () {
  "use strict";

  /* ---------- Theme toggle ---------- */
  var themeBtn = document.querySelector(".theme-toggle");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var current = document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
      var next = current === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      try { localStorage.setItem("ielab-theme", next); } catch (e) { /* private mode */ }
    });
  }

  /* ---------- Mobile nav ---------- */
  var burger = document.querySelector(".nav-burger");
  var nav = document.querySelector(".site-nav");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") nav.classList.remove("open");
    });
  }

  /* ---------- Scroll reveal ---------- */
  var revealEls = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("revealed");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -40px 0px", threshold: 0.05 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("revealed"); });
  }

  /* ---------- Back to top ---------- */
  var backTop = document.querySelector(".back-top");
  if (backTop) {
    var onScroll = function () {
      backTop.classList.toggle("show", window.scrollY > 600);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    backTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---------- Hero search: typing placeholder + submit to /publications ---------- */
  var heroForm = document.querySelector(".hero-search");
  if (heroForm) {
    var heroInput = heroForm.querySelector("input");
    var queries = [
      "how can large language models rank documents?",
      "dense retrievers for systematic reviews",
      "does Dr Google give good health advice?",
      "are neural rankers robust to typos?",
      "how should we evaluate generative IR?",
      "conversational search with relevance feedback"
    ];
    var qi = 0, ci = 0, deleting = false;

    var type = function () {
      if (document.activeElement === heroInput && heroInput.value) return; // don't fight the user
      var q = queries[qi];
      ci = deleting ? ci - 1 : ci + 1;
      heroInput.setAttribute("placeholder", q.slice(0, ci));
      var delay = deleting ? 22 : 48;
      if (!deleting && ci === q.length) { deleting = true; delay = 2200; }
      else if (deleting && ci === 0) { deleting = false; qi = (qi + 1) % queries.length; delay = 350; }
      window.setTimeout(type, delay);
    };

    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduceMotion) {
      heroInput.setAttribute("placeholder", "Search our publications…");
    } else {
      window.setTimeout(type, 800);
    }

    heroForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var q = heroInput.value.trim() || heroInput.getAttribute("placeholder") || "";
      window.location.href = "/publications/" + (q ? "?q=" + encodeURIComponent(q) : "");
    });
  }

  /* ---------- Publications: live search + year filter ---------- */
  var pubSearch = document.getElementById("pub-search");
  if (pubSearch) {
    var items = Array.prototype.slice.call(document.querySelectorAll(".pub-item"));
    var groups = Array.prototype.slice.call(document.querySelectorAll(".pub-year-group"));
    var chips = Array.prototype.slice.call(document.querySelectorAll(".filter-chip[data-year]"));
    var countEl = document.querySelector(".results-count");
    var emptyEl = document.querySelector(".pubs-empty");
    var activeYear = "all";

    var normalise = function (s) { return (s || "").toLowerCase(); };

    var apply = function () {
      var terms = normalise(pubSearch.value).split(/\s+/).filter(Boolean);
      var hasQuery = terms.length > 0;
      var visible = 0;

      items.forEach(function (item) {
        var hay = normalise(item.getAttribute("data-search"));
        var matchText = terms.every(function (t) { return hay.indexOf(t) !== -1; });
        var matchYear = activeYear === "all" || item.getAttribute("data-year") === activeYear;
        // Works authored only by alumni/external members (data-core="0")
        // stay hidden until the visitor actively searches.
        var isCore = item.getAttribute("data-core") !== "0";
        var show = matchText && matchYear && (isCore || hasQuery);
        item.style.display = show ? "list-item" : "none";
        if (show) visible++;
      });

      groups.forEach(function (group) {
        var any = group.querySelector(".pub-item:not([style*='display: none'])");
        group.style.display = any ? "" : "none";
      });

      if (countEl) {
        countEl.textContent = visible + " publication" + (visible === 1 ? "" : "s") +
          (terms.length || activeYear !== "all" ? " matching" : "");
      }
      if (emptyEl) emptyEl.style.display = visible === 0 ? "block" : "none";
    };

    pubSearch.addEventListener("input", apply);

    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        activeYear = chip.getAttribute("data-year");
        chips.forEach(function (c) { c.classList.toggle("active", c === chip); });
        apply();
      });
    });

    // Prefill from ?q= (e.g. arriving from the homepage hero search)
    try {
      var params = new URLSearchParams(window.location.search);
      var q = params.get("q");
      if (q) {
        pubSearch.value = q;
        apply();
        pubSearch.focus();
      } else {
        apply();
      }
    } catch (e) { apply(); }
  }

  /* ---------- Copy citation buttons ---------- */
  document.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-cite]");
    if (!btn) return;
    var text = btn.getAttribute("data-cite");
    var done = function () {
      var label = btn.querySelector(".cite-label");
      if (!label) return;
      var original = label.textContent;
      label.textContent = "Copied!";
      window.setTimeout(function () { label.textContent = original; }, 1600);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, done);
    } else {
      var ta = document.createElement("textarea");
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand("copy"); } catch (err) { /* noop */ }
      document.body.removeChild(ta);
      done();
    }
  });
})();
