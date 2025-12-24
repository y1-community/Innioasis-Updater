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

    footerRoot.innerHTML = `
    <footer class="site-footer">
        <div class="footer-grid">

            <div class="footer-col">
                <h4>Links</h4>
                <a href="https://innioasis.app/index.html#home">Home</a>
                <a href="https://innioasis.app/guide.html">Guide</a>
                <a href="https://themes.innioasis.app/">Themes</a>
                <a href="https://innioasis.app/index.html#versions">Versions</a>
                <a href="https://innioasis.app/index.html#donate">Donate</a>
            </div>

            <div class="footer-col">
                <h4>Credits</h4>

                <div class="footer-person">
                    <strong>Ryan Specter</strong>
                    <div style="display:flex;gap:15px;justify-content:center;">
                        <a href="https://github.com/ryan-specter/" target="_blank"><i class="fab fa-github"></i></a>
                        <a href="https://reddit.com/u/RespectYarn" target="_blank"><i class="fab fa-reddit"></i></a>
                        <a href="#donate"><i class="fas fa-donate"></i></a>
                    </div>
                </div>

                <div class="footer-person">
                    <strong>sipped</strong>
                    <div style="display:flex;gap:15px;justify-content:center;">
                        <a href="https://github.com/sippedaway" target="_blank"><i class="fab fa-github"></i></a>
                        <a href="https://sipped.org" target="_blank"><i class="fas fa-globe"></i></a>
                        <a href="#donate"><i class="fas fa-donate"></i></a>
                    </div>
                </div>
            </div>

            <div class="footer-col" style="display:flex;flex-direction:column;justify-content:space-between;">   
                <div>
                    <h4>In collaboration with</h4>
                    <a href="https://www.innioasis.com" target="_blank">
                        <img src="innioasis.png" class="footer-logo" alt="Innioasis">
                    </a>
                </div>
            </div>

        </div>

        <div class="footer-bottom">
            © 2025 innioasis Community
        </div>
    </footer>`

    const footerBottom = footerRoot.querySelector('.footer-bottom')

    const PUNCH_URL = 'https://counter.sipped.org/punch/innioasisupdater-counter/12336c13dc3fd1c8ddfbe1953149debc/website'
    const GET_URL = 'https://counter.sipped.org/get/innioasisupdater-counter/12336c13dc3fd1c8ddfbe1953149debc/website'

    async function fetchCounter(url) {
        try {
            const res = await fetch(url, {
                cache: 'no-store'
            })
            if (!res.ok) throw new Error('Failed to fetch counter')

            try {
                const data = await res.json()
                if (typeof data.count === 'number') return data.count
                if (typeof data.value === 'number') return data.value
            } catch {}

            const text = await res.text()
            const num = parseInt(text, 10)
            if (!isNaN(num)) return num

            return null
        } catch {
            return null
        }
    }

    async function initCounter() {
        const hasRun = localStorage.getItem("hasrun")
        const urlToUse = hasRun ? GET_URL : PUNCH_URL

        const count = await fetchCounter(urlToUse)

        if (!hasRun) localStorage.setItem("hasrun", 'true')

        const span = document.createElement('span')
        span.style.marginLeft = '20px'
        span.innerHTML = `<i class="fas fa-eye" style="font-size: 11px; margin-right: 6px;"></i>${
    count !== null ? count.toLocaleString() + ' views' : '... views'
  }`
        footerBottom.appendChild(span)
    }

    initCounter()

})();