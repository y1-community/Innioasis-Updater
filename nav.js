(function () {
  "use strict";
  var root = document.getElementById("nav-root");
  if (root) {
    root.innerHTML = '<nav aria-label="Primary navigation"><div class="nav-container"><div class="logo"><a href="/"><img class="lumen-nav-icon" src="/mtkclient/gui/images/icon.png" width="26" height="26" alt="" aria-hidden="true">Updater</a></div><div class="nav-tools"><label class="lumen-theme-control"><span>Theme</span><select id="lumen-theme-select" aria-label="Choose site colour theme"><option value="auto">Auto</option><option value="light">Light</option><option value="dark">Dark</option><option value="high-contrast">High contrast</option><option value="2077">2077</option></select></label><button class="hamburger" id="hamburger" type="button" aria-label="Open navigation menu" aria-controls="navLinks" aria-expanded="false"><span></span><span></span><span></span></button></div><ul class="nav-links" id="navLinks"><li><a href="/guide.html">Guide</a></li><li><a href="/firmware.html">Software Downloads</a></li><li><a href="/firmware-faq.html">Help me choose</a></li><li><a href="/developers.html">Developers</a></li><li><a href="/rockbox.html">Rockbox</a></li><li><a href="https://themes.innioasis.app/" target="_blank" rel="noopener noreferrer">Themes</a></li><li><a href="https://discord.gg/zHrT2zrcek" target="_blank" rel="noopener noreferrer">Community</a></li></ul></div></nav>';
  }
  var themeSelect = document.getElementById("lumen-theme-select");
  var storedTheme = "auto";
  try { storedTheme = localStorage.getItem("lumen-theme") || "auto"; } catch (_) {}
  if (themeSelect) {
    themeSelect.value = ["auto", "light", "dark", "high-contrast", "2077"].indexOf(storedTheme) >= 0 ? storedTheme : "auto";
    themeSelect.addEventListener("change", function () {
      var value = themeSelect.value;
      document.documentElement.setAttribute("data-lumen-theme", value);
      try { localStorage.setItem("lumen-theme", value); } catch (_) {}
    });
  }
  var menu = document.getElementById("navLinks");
  var toggle = document.getElementById("hamburger");
  function setOpen(open) {
    if (!menu || !toggle) return;
    menu.classList.toggle("active", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? "Close navigation menu" : "Open navigation menu");
  }
  if (toggle) toggle.addEventListener("click", function () { setOpen(!menu.classList.contains("active")); });
  if (menu) menu.querySelectorAll("a").forEach(function (link) { link.addEventListener("click", function () { setOpen(false); }); });
  document.addEventListener("keydown", function (event) { if (event.key === "Escape") setOpen(false); });
  var footerRoot = document.getElementById("footer-root");
  if (!footerRoot) return;
  footerRoot.innerHTML = '<footer class="site-footer site-footer--updater"><div class="footer-grid"><div class="footer-col"><h4>Innioasis Updater</h4><a href="/guide.html">Installation guide</a><a href="/firmware.html">Software Downloads</a><a href="/troubleshooting.html">Troubleshooting</a><a href="/developers.html">Developer guide</a><a href="/support_devs.html#donations">Support Updater and the Themes Gallery</a></div><div class="footer-col"><h4>Community</h4><a href="https://themes.innioasis.app/" target="_blank" rel="noopener noreferrer">Themes Gallery</a><a href="https://discord.gg/zHrT2zrcek" target="_blank" rel="noopener noreferrer">Discord</a><a href="https://github.com/y1-community/Innioasis-Updater" target="_blank" rel="noopener noreferrer">Updater source code</a><a href="/developers.html">Add software to Updater</a><a href="https://ko-fi.com/teamslide" target="_blank" rel="noopener noreferrer">Blog</a></div></div><div class="footer-bottom">Copyleft · Innioasis users and contributors, for the community.</div></footer>';
})();
