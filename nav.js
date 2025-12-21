(function() {
    const root = document.getElementById('nav-root');
    if (!root) return;

    root.innerHTML = `
    <nav>
      <div class="nav-container">
        <div class="logo" onclick="window.location.href='index.html#home'">Innioasis Updater</div>
        <ul class="nav-links" id="navLinks">
  <li><a href="index.html#home"><i class="fa-solid fa-house" style="margin-right: 3px;"></i> Home</a></li>
  <li><a href="guide.html#guide"><i class="fa-solid fa-book" style="margin-right: 3px;"></i> Guide</a></li>
  <li><a href="index.html#versions"><i class="fa-solid fa-code-branch" style="margin-right: 3px;"></i> Versions</a></li>
  <li><a href="themes.html"><i class="fa-solid fa-palette" style="margin-right: 3px;"></i> Themes</a></li>
</ul>

        <div class="hamburger" id="hamburger">
          <span></span><span></span><span></span>
        </div>
      </div>
    </nav>`;

    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => navLinks.classList.toggle('active'));
    }

    navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => navLinks.classList.remove('active')));

    document.addEventListener('click', function(e) {
        const t = e.target.closest('a');
        if (!t) return;
        const href = t.getAttribute('href') || '';
        if (href.startsWith('#')) {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) window.scrollTo({
                top: target.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });

    window.addEventListener('scroll', () => {
        const nav = document.querySelector('#nav-root nav');
        if (!nav) return;
        if (window.scrollY > 100) nav.style.boxShadow = '0 4px 20px rgba(0,0,0,0.3)';
        else nav.style.boxShadow = 'none';
    });
})();