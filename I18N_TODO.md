# i18n to-do and hand-off

Live document for the multilingual rollout across
`y1-community/Innioasis-Updater` (innioasis.app) and
`y1-community/InnioasisY1Themes` (themes.innioasis.app).
Read `I18N.md` first; this file is only the work list and its state.

**Owners:** claim a line by adding your name in brackets before starting.
`[Buffy]` = completed by this agent, `[AG]` = Antigravity, `[ ]` = open.

## Done and verified

- [Buffy] Runtime enabled site-wide: `install_runtime.py` `ENABLED = True`, tag on
  all 1,345 Updater pages and all gallery pages.
- [Buffy] Language control added to the bottom support dock on both sites
  (`data-locale-open`), with late-binding to the injected dock and a nav/floating
  fallback.
- [Buffy] `site-locale.js`: catalog fetch through the script base (works from
  nested pages and from `/de/` copies), `aria-controls` target id, dock label
  follows the chosen language.
- [Buffy] GA4/GTM language events: `site_language_view`, `site_language_change`,
  `site_language` user property.
- [Buffy] Public API for programmatic pages: `InnioasisLocale.translate`,
  `.refresh`, `.set`, `.label`.
- [Buffy] Generators inject the runtime, so regenerated release notes, post-install
  pages, firmware-info pages, install guides and Rockbox pages stay translated.
- [Buffy] `i18n/reviewed/core-ui.json` + `seed_catalogs.py` loader: 20 shell
  strings hand-written in 25 languages, merged without overwriting the existing
  reviewed table.
- [Buffy] `translate.py --top N` (frequency-first) and `--index-only` (publish a
  catalog to the picker without translating).
- [Buffy] Picker index rebuilt from the catalogs on disk (272 entries Updater).
- [Buffy] Daily/push/CI translation workflow replacing the one that called a
  missing script; it now extracts **core + full**, seeds reviewed copy,
  translates incrementally, rebuilds the index, reports coverage and pre-renders
  `dist/`.
- [Buffy] donors.csv sync repaired: canonical direction (Updater -> Themes),
  LF normalisation, PAT documented, no ping-pong. Themes workflow only pulls.
- [Buffy] Themes extraction scope narrowed to gallery pages; theme folders are
  excluded so creator copy is never rewritten.
- [AG] Flashcards: 270+ catalog files, `multi_provider_translate.py`,
  `auto_translate_pages.py`, `generate_multilingual_static_pages.py`, initial
  workflow drafts, runtime copied to the Themes repo.
- [AG] `i18n/locales.json` expanded from the updater-ce-neo language table.

## Open — needs a human or the next agent

- [ ] **Coverage is the main gap.** The imported catalogs hold updater-ce-neo
  app strings; only ~30 of 6,223 source strings matched at the time of writing.
  A `--top 700` pass is running for the 30 launch languages; confirm with
  `translate.py --check`. Then schedule the long tail (`--locales all`) over
  several nightly runs; each run continues where the last stopped.
- [ ] **Static locale pages are not served yet.** CI produces `dist/` and uploads
  `i18n-site`. To make `/de/...` crawlable on the live domain, either run the
  `publish` job (manual dispatch, `deploy_pages`) or point hosting at that build.
  The Themes site deploys from git through Cloudflare Pages, so its locale copies
  need the same decision.
- [ ] **GA4 measurement id.** GTM carries the property today. If a direct tag is
  wanted, add `<meta name="ga4-measurement-id" content="G-...">`; the runtime
  already supports it.
- [ ] `sitemap-i18n.xml` is not committed. Add it to `generate_sitemap.py` only
  after locale pages are actually served, otherwise it advertises 404s.
- [ ] Native-speaker review of the 25 `core-ui.json` languages: tone, formality
  (tu/vous, du/Sie, です/ます), and the safety verbs.
- [ ] Review the imported app catalogs for leaks: app-only UI strings that do not
  belong on the site should be dropped rather than translated twice.
- [ ] RTL visual pass on Arabic, Hebrew, Persian and Urdu (dock order, panel
  scrollbar, icon mirroring).
- [ ] Themes gallery: decide whether theme *tags/categories* (community taxonomy,
  not creator prose) should be translated. Currently excluded.
- [ ] Add a `repository_dispatch` sender to the Updater doc-pages workflow so a
  firmware release triggers translation immediately instead of waiting for the
  daily run.
- [ ] Confirm both workflows pass on GitHub (they reference secrets and cannot be
  executed from a local checkout).

## Sanity checks to run before shipping copy

```bash
python3 scripts/i18n/extract_strings.py --tiers core,full
python3 scripts/i18n/seed_catalogs.py
python3 scripts/i18n/translate.py --index-only
python3 scripts/i18n/translate.py --check | tail -5
python3 scripts/i18n/prerender.py --locales de,ja,ar --tiers core --out dist
```

Then open `index.html?lang=ar` and check: dock button label, panel opens, text is
Arabic, `dir="rtl"` on `<html>`, and `dataLayer` contains `site_language_view`.

## Hand-off note

If you add a page, add it in English, run extraction and translation, and tick a
line here. Do not edit `i18n/catalogs/*.json` by hand unless you are reviewing a
translation; the pipeline treats them as its cache.
