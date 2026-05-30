(function() {
    const navRoot = document.getElementById('nav-root')
    if (navRoot) {
        navRoot.innerHTML = `
        <nav>
          <div class="nav-container">
            <div class="logo"><a href='https://innioasis.app/index.html#home' style="text-decoration: none; color: var(--accent)">Innioasis Updater</a></div>
            <ul class="nav-links" id="navLinks">
              <li><a href="https://innioasis.app/index.html#home"><i class="fa-solid fa-house" style="margin-right:3px;"></i> Home</a></li>
              <li><a href="https://innioasis.app/guide.html"><i class="fa-solid fa-book" style="margin-right:3px;"></i> Guide</a></li>
              <li><a href="https://innioasis.app/index.html#versions"><i class="fa-solid fa-code-branch" style="margin-right:3px;"></i> Versions</a></li>
              <li><a href="https://themes.innioasis.app/"><i class="fa-solid fa-palette" style="margin-right:3px;"></i> Themes</a></li>
              <li><a href="https://discord.gg/u95pr8XfN" target="_blank" rel="noopener noreferrer"><i class="fa-brands fa-discord" style="margin-right:3px;"></i> Discord</a></li>
            </ul>
            <div class="hamburger" id="hamburger">
              <span></span><span></span><span></span>
            </div>
          </div>
        </nav>`
    }

    const hamburger = document.getElementById('hamburger')
    const navLinks = document.getElementById('navLinks')

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => navLinks.classList.toggle('active'))
        navLinks.querySelectorAll('a').forEach(a =>
            a.addEventListener('click', () => navLinks.classList.remove('active'))
        )
    }

    document.addEventListener('click', e => {
        const t = e.target.closest('a')
        if (!t) return
        const href = t.getAttribute('href') || ''
        if (t.classList.contains('open-donate-toolbar') || href === '#donate') {
            e.preventDefault()
            if (typeof window.openY1DonatePanel === 'function') {
                window.openY1DonatePanel()
                return
            }
            const donateToggle = document.getElementById('donate-toggle')
            if (donateToggle) {
                donateToggle.click()
                return
            }
        }
        if (href.startsWith('#')) {
            e.preventDefault()
            const target = document.querySelector(href)
            if (target) window.scrollTo({
                top: target.offsetTop - 80,
                behavior: 'smooth'
            })
        }
    })

    window.addEventListener('scroll', () => {
        const nav = document.querySelector('#nav-root nav')
        if (!nav) return
        nav.style.boxShadow = window.scrollY > 100 ?
            '0 4px 20px rgba(0,0,0,0.3)' :
            'none'
    })

    const footerRoot = document.getElementById('footer-root')
    if (!footerRoot) return

    let luciLogoSrc = 'luci-alt.svg'
    try {
        luciLogoSrc = new URL('luci-alt.svg', document.baseURI || window.location.href).href
    } catch (_) {}

    footerRoot.innerHTML = `
    <footer class="site-footer site-footer--updater">
        <div class="footer-grid">

            <div class="footer-col">
                <h4>Links</h4>
                <a href="https://innioasis.app/index.html#home">Home</a>
                <a href="https://innioasis.app/guide.html">Guide</a>
                <a href="https://innioasis.app/index.html#versions">Versions</a>
                <a href="https://themes.innioasis.app/">Themes</a>
                <a href="https://discord.gg/u95pr8XfN" target="_blank" rel="noopener noreferrer">Discord</a>
                <a href="#donate" class="open-donate-toolbar">Donate</a>
            </div>

            <div class="footer-col footer-col-powered">
                <p class="footer-powered-label">This site is powered by</p>
                <a href="https://www.luci.ltd" target="_blank" rel="noopener noreferrer" class="footer-luci-link">
                    <img src="${luciLogoSrc}" class="footer-logo footer-logo-luci" alt="Luci Ltd web hosting — powers innioasis.app (luci.ltd)" title="Luci hosting and domains — www.luci.ltd" decoding="async">
                </a>
            </div>

        </div>

        <div class="footer-bottom">
            <a href="https://en.wikipedia.org/wiki/Copyleft" class="footer-copyleft" target="_blank" rel="noopener noreferrer" title="Copyleft — Wikipedia">🄯</a> - Ryan Specter — Made with ❤️ by Y1 users, for Y1 users
        </div>
    </footer>`

})();
