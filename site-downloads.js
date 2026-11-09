/* In-page downloads for Innioasis.

   A click on a firmware zip, a portable package, an installer, a driver or a
   file linked from a guide normally hands the reader to the browser's own
   download shelf: no progress on the page, no speed, no way to see how long a
   1.5 GB image will take. This module takes those clicks, streams the file,
   and draws progress where the reader clicked:

     - a card directly above the link that was clicked, with percent, transfer
       speed and time left;
     - a tray in the corner once that link is scrolled out of view, so several
       downloads can run at once (themes, portable packages, runtimes);
     - a sheet opened from the tray or the footer dock that lists every job,
       because a phone has no room for a corner tray.

   Where the File System Access API exists the bytes are written straight to a
   file the reader picks, so a 1.5 GB image never sits in a JavaScript array.
   Without it, small files (<= 64 MB) are buffered into a blob; larger ones
   hand off to the browser's downloader with an indeterminate card, and every
   failure falls back to a plain navigation. A blocked CORS response must never
   turn a download into a dead click. */
(function (global) {
    "use strict";
    if (global.InnioasisDownloads) return;

    var doc = global.document;
    if (!doc || !global.addEventListener) return;

    var VERSION = "20261109dl";
    var STREAMABLE = /\.(zip|img|dmg|pkg|apk|exe|msi|7z|tar|gz|xz|bz2|tgz|iso|bin|jar|ipa|app)(\?|#|$)/i;
    var BIG_BLOB = 64 * 1024 * 1024;
    var MAX_JOBS = 3;
    var TICK = 120;

    var jobs = [];
    var seq = 0;
    var jobByAnchor = typeof WeakMap === "function" ? new WeakMap() : null;
    var stylesInjected = false;
    var trayCollapsed = false;
    var sheetOpen = false;

    /* ------------------------------------------------------------- wording

       Download wording is the one part of the site a reader sees while the
       page is busy, so it has to match the language they picked. The published
       catalogs answer first (that keeps every translated download sentence in
       one place); the small table below covers the languages where the UI
       sentence has not made it into a catalog yet. A miss is still shown in
       English rather than blank. */
    var WORDING = {
        "Downloads": {
            de: "Downloads", fr: "Téléchargements", es: "Descargas", it: "Download",
            pt: "Transferências", "pt-BR": "Downloads", nl: "Downloads", pl: "Pobierania",
            ru: "Загрузки", uk: "Завантаження", ja: "ダウンロード", ko: "다운로드",
            "zh-CN": "下载", "zh-TW": "下載", tr: "İndirmeler", ar: "التنزيلات",
            hi: "डाउनलोड", id: "Unduhan", vi: "Tải xuống", th: "ดาวน์โหลด",
            sv: "Nedladdningar", da: "Downloads", fi: "Lataukset", cs: "Stahování",
            el: "Λήψεις", he: "הורדות", hu: "Letöltések", ro: "Descărcări",
            bg: "Изтегляния"
        },
        "Downloading…": {
            de: "Wird heruntergeladen…", fr: "Téléchargement…", es: "Descargando…",
            it: "Download in corso…", pt: "A transferir…", "pt-BR": "Baixando…",
            nl: "Downloaden…", pl: "Pobieranie…", ru: "Загрузка…", uk: "Завантаження…",
            ja: "ダウンロード中…", ko: "다운로드 중…", "zh-CN": "正在下载…",
            "zh-TW": "正在下載…", tr: "İndiriliyor…", ar: "جارٍ التنزيل…",
            hi: "डाउनलोड हो रहा है…", id: "Mengunduh…", vi: "Đang tải xuống…",
            th: "กำลังดาวน์โหลด…", sv: "Laddar ner…", da: "Downloader…",
            fi: "Ladataan…", cs: "Stahování…", el: "Λήψη…", he: "מוריד…",
            hu: "Letöltés…", ro: "Se descarcă…", bg: "Изтегляне…"
        },
        "Preparing…": {
            de: "Wird vorbereitet…", fr: "Préparation…", es: "Preparando…",
            it: "Preparazione…", pt: "A preparar…", "pt-BR": "Preparando…",
            nl: "Voorbereiden…", pl: "Przygotowywanie…", ru: "Подготовка…",
            uk: "Підготовка…", ja: "準備中…", ko: "준비 중…", "zh-CN": "正在准备…",
            "zh-TW": "正在準備…", tr: "Hazırlanıyor…", ar: "جارٍ التحضير…",
            hi: "तैयार हो रहा है…", id: "Menyiapkan…", vi: "Đang chuẩn bị…",
            th: "กำลังเตรียม…", sv: "Förbereder…", da: "Forbereder…",
            fi: "Valmistellaan…", cs: "Připravuje se…", el: "Προετοιμασία…",
            he: "מכין…", hu: "Előkészítés…", ro: "Se pregătește…", bg: "Подготовка…"
        },
        "Saved": {
            de: "Gespeichert", fr: "Enregistré", es: "Guardado", it: "Salvato",
            pt: "Guardado", "pt-BR": "Salvo", nl: "Opgeslagen", pl: "Zapisano",
            ru: "Сохранено", uk: "Збережено", ja: "保存しました", ko: "저장됨",
            "zh-CN": "已保存", "zh-TW": "已儲存", tr: "Kaydedildi", ar: "تم الحفظ",
            hi: "सहेजा गया", id: "Tersimpan", vi: "Đã lưu", th: "บันทึกแล้ว",
            sv: "Sparat", da: "Gemt", fi: "Tallennettu", cs: "Uloženo",
            el: "Αποθηκεύτηκε", he: "נשמר", hu: "Mentve", ro: "Salvat", bg: "Запазено"
        },
        "Your browser takes over": {
            de: "Der Browser übernimmt", fr: "Le navigateur prend le relais",
            es: "El navegador continúa", it: "Continua il browser",
            pt: "O navegador continua", "pt-BR": "O navegador continua",
            nl: "De browser neemt het over", pl: "Przeglądarka przejmuje",
            ru: "Загружает браузер", uk: "Завантажує браузер",
            ja: "ブラウザが引き継ぎます", ko: "브라우저가 이어받습니다",
            "zh-CN": "由浏览器继续", "zh-TW": "由瀏覽器繼續", tr: "Tarayıcı devraldı",
            ar: "يتولى المتصفح", hi: "ब्राउज़र संभाल रहा है", id: "Browser melanjutkan",
            vi: "Trình duyệt tiếp tục", th: "เบราว์เซอร์ดำเนินการต่อ", sv: "Webbläsaren tar över",
            da: "Browseren overtager", fi: "Selain jatkaa", cs: "Přebírá prohlížeč",
            el: "Συνεχίζει το πρόγραμμα περιήγησης", he: "הדפדפן ממשיך",
            hu: "A böngésző folytatja", ro: "Browserul preia", bg: "Браузърът поема"
        },
        "Failed": {
            de: "Fehlgeschlagen", fr: "Échec", es: "Error", it: "Non riuscito",
            pt: "Falhou", "pt-BR": "Falhou", nl: "Mislukt", pl: "Niepowodzenie",
            ru: "Ошибка", uk: "Помилка", ja: "失敗しました", ko: "실패",
            "zh-CN": "失败", "zh-TW": "失敗", tr: "Başarısız", ar: "فشل",
            hi: "विफल", id: "Gagal", vi: "Thất bại", th: "ล้มเหลว", sv: "Misslyckades",
            da: "Mislykkedes", fi: "Epäonnistui", cs: "Selhalo", el: "Απέτυχε",
            he: "נכשל", hu: "Sikertelen", ro: "Eșuat", bg: "Неуспешно"
        },
        "Cancel": {
            de: "Abbrechen", fr: "Annuler", es: "Cancelar", it: "Annulla",
            pt: "Cancelar", "pt-BR": "Cancelar", nl: "Annuleren", pl: "Anuluj",
            ru: "Отмена", uk: "Скасувати", ja: "キャンセル", ko: "취소",
            "zh-CN": "取消", "zh-TW": "取消", tr: "İptal", ar: "إلغاء",
            hi: "रद्द करें", id: "Batal", vi: "Huỷ", th: "ยกเลิก", sv: "Avbryt",
            da: "Annuller", fi: "Peruuta", cs: "Zrušit", el: "Άκυρο",
            he: "ביטול", hu: "Mégse", ro: "Anulează", bg: "Отказ"
        },
        "Speed": {
            de: "Geschwindigkeit", fr: "Vitesse", es: "Velocidad", it: "Velocità",
            pt: "Velocidade", "pt-BR": "Velocidade", nl: "Snelheid", pl: "Prędkość",
            ru: "Скорость", uk: "Швидкість", ja: "速度", ko: "속도",
            "zh-CN": "速度", "zh-TW": "速度", tr: "Hız", ar: "السرعة",
            hi: "गति", id: "Kecepatan", vi: "Tốc độ", th: "ความเร็ว", sv: "Hastighet",
            da: "Hastighed", fi: "Nopeus", cs: "Rychlost", el: "Ταχύτητα",
            he: "מהירות", hu: "Sebesség", ro: "Viteză", bg: "Скорост"
        },
        "Time left": {
            de: "Restzeit", fr: "Temps restant", es: "Tiempo restante",
            it: "Tempo rimasto", pt: "Tempo restante", "pt-BR": "Tempo restante",
            nl: "Resterend", pl: "Pozostało", ru: "Осталось", uk: "Залишилось",
            ja: "残り時間", ko: "남은 시간", "zh-CN": "剩余时间", "zh-TW": "剩餘時間",
            tr: "Kalan süre", ar: "الوقت المتبقي", hi: "शेष समय", id: "Sisa waktu",
            vi: "Còn lại", th: "เหลืออีก", sv: "Återstår", da: "Tilbage",
            fi: "Jäljellä", cs: "Zbývá", el: "Απομένει", he: "נותר",
            hu: "Hátralévő", ro: "Rămas", bg: "Остава"
        },
        "Show downloads": {
            de: "Downloads anzeigen", fr: "Afficher les téléchargements",
            es: "Mostrar descargas", it: "Mostra download", pt: "Mostrar transferências",
            "pt-BR": "Mostrar downloads", nl: "Downloads tonen", pl: "Pokaż pobierania",
            ru: "Показать загрузки", uk: "Показати завантаження", ja: "ダウンロードを表示",
            ko: "다운로드 표시", "zh-CN": "显示下载", "zh-TW": "顯示下載",
            tr: "İndirmeleri göster", ar: "إظهار التنزيلات", hi: "डाउनलोड दिखाएँ",
            id: "Tampilkan unduhan", vi: "Hiện tải xuống", th: "แสดงการดาวน์โหลด",
            sv: "Visa nedladdningar", da: "Vis downloads", fi: "Näytä lataukset",
            cs: "Zobrazit stahování", el: "Εμφάνιση λήψεων", he: "הצג הורדות",
            hu: "Letöltések megjelenítése", ro: "Arată descărcările", bg: "Покажи изтеглянията"
        }
    };

    function localeCode() {
        try {
            var loc = global.InnioasisLocale;
            if (loc && loc.locale) return String(loc.locale);
            var html = doc.documentElement && doc.documentElement.getAttribute("lang");
            if (html) return html;
        } catch (_) {}
        return "en";
    }

    function t(english) {
        try {
            var loc = global.InnioasisLocale;
            if (loc && typeof loc.translate === "function") {
                var fromCatalog = loc.translate(english);
                if (fromCatalog && fromCatalog !== english) return fromCatalog;
            }
        } catch (_) {}
        var code = localeCode();
        var table = WORDING[english];
        if (!table) return english;
        if (table[code]) return table[code];
        var base = code.split("-")[0];
        if (table[base]) return table[base];
        var lower = base.toLowerCase();
        for (var key in table) {
            if (key.toLowerCase() === lower) return table[key];
        }
        return english;
    }

    /* ------------------------------------------------------------ formatting */
    function bytes(value) {
        var size = Number(value) || 0;
        if (size < 1024) return size + " B";
        var kb = size / 1024;
        if (kb < 1024) return kb.toFixed(kb < 10 ? 1 : 0) + " KB";
        var mb = kb / 1024;
        if (mb < 1024) return mb.toFixed(1) + " MB";
        return (mb / 1024).toFixed(2) + " GB";
    }

    function seconds(value) {
        var total = Math.max(0, Math.round(Number(value) || 0));
        if (!total) return "";
        if (total < 60) return total + "s";
        var minutes = Math.floor(total / 60);
        var rest = total % 60;
        if (minutes < 60) return minutes + "m " + (rest < 10 ? "0" + rest : rest) + "s";
        return Math.floor(minutes / 60) + "h " + (minutes % 60) + "m";
    }

    function speedOf(job) {
        var now = Date.now();
        var window = job.samples.filter(function (sample) { return now - sample.at <= 4000; });
        if (window.length < 2) return job.lastSpeed || 0;
        var first = window[0];
        var last = window[window.length - 1];
        var span = (last.at - first.at) / 1000;
        if (span < 0.25) return job.lastSpeed || 0;
        var rate = (last.bytes - first.bytes) / span;
        job.lastSpeed = rate;
        return rate;
    }

    function etaOf(job) {
        if (!job.total) return 0;
        var rate = speedOf(job);
        if (rate < 1024) return 0;
        return (job.total - job.loaded) / rate;
    }

    /* --------------------------------------------------------------- styling */
    function injectStyles() {
        if (stylesInjected || !doc.head) return;
        stylesInjected = true;
        var style = doc.createElement("style");
        style.id = "site-downloads-styles";
        style.textContent = [
            ".site-dl-card{position:fixed;z-index:10004;box-sizing:border-box;width:min(320px,calc(100vw - 24px));padding:.7rem .8rem;border:1px solid var(--lumen-line-strong,rgba(255,255,255,.24));border-radius:12px;background:var(--lumen-panel,#14161f);color:var(--lumen-text,#f4f6fb);box-shadow:0 18px 38px rgba(0,0,0,.42);font:500 12px/1.35 var(--lumen-body,system-ui,sans-serif);}",
            ".site-dl-card__top{display:flex;align-items:baseline;gap:.5rem;}",
            ".site-dl-card__name{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:700;}",
            ".site-dl-card__pct{font-variant-numeric:tabular-nums;color:var(--lumen-accent,#6b9fff);font-weight:800;}",
            ".site-dl-bar{margin:.5rem 0 .35rem;height:5px;border-radius:999px;background:color-mix(in oklab,var(--lumen-text,#fff) 14%,transparent);overflow:hidden;}",
            ".site-dl-bar__fill{height:100%;width:0;border-radius:inherit;background:var(--lumen-accent,#6b9fff);transition:width .18s linear;}",
            ".site-dl-card.is-done .site-dl-bar__fill{background:#43c98b;}",
            ".site-dl-card.is-failed .site-dl-bar__fill{background:#e2564f;}",
            ".is-indeterminate .site-dl-bar__fill{animation:site-dl-drift 1.15s ease-in-out infinite alternate;}",
            "@keyframes site-dl-drift{from{transform:translateX(-18%);}to{transform:translateX(190%);}}",
            ".site-dl-card__meta{display:flex;justify-content:space-between;gap:.6rem;color:var(--lumen-muted,#9aa3b5);font-size:11px;}",
            ".site-dl-card__row{display:flex;justify-content:space-between;gap:.6rem;}",
            ".site-dl-card__cancel{border:0;background:none;padding:0;color:inherit;text-decoration:underline;cursor:pointer;font:inherit;font-size:11px;}",
            ".site-dl-tray{position:fixed;right:14px;bottom:calc(var(--y1-dock-space,104px) + 12px);z-index:10005;box-sizing:border-box;width:min(330px,calc(100vw - 24px));max-height:min(46vh,420px);overflow:auto;padding:.6rem;border:1px solid var(--lumen-line-strong,rgba(255,255,255,.24));border-radius:14px;background:var(--lumen-panel,#14161f);color:var(--lumen-text,#f4f6fb);box-shadow:0 22px 46px rgba(0,0,0,.5);font:500 12px/1.35 var(--lumen-body,system-ui,sans-serif);}",
            ".site-dl-tray[hidden]{display:none!important;}",
            ".site-dl-tray__head{display:flex;align-items:center;gap:.5rem;margin:0 .15rem .5rem;}",
            ".site-dl-tray__title{flex:1;margin:0;font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:var(--lumen-muted,#9aa3b5);}",
            ".site-dl-tray__btn{border:1px solid var(--lumen-line,rgba(255,255,255,.16));border-radius:999px;background:transparent;color:inherit;font:inherit;font-size:11px;padding:.2rem .55rem;cursor:pointer;}",
            ".site-dl-tray__btn:hover{border-color:var(--lumen-accent,#6b9fff);}",
            ".site-dl-row{display:grid;gap:.28rem;padding:.45rem .35rem;border-radius:9px;}",
            ".site-dl-row + .site-dl-row{border-top:1px solid var(--lumen-line,rgba(255,255,255,.12));}",
            ".site-dl-row__top{display:flex;align-items:baseline;gap:.5rem;}",
            ".site-dl-row__name{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}",
            ".site-dl-row__pct{font-variant-numeric:tabular-nums;font-weight:800;}",
            ".site-dl-row__meta{display:flex;justify-content:space-between;gap:.5rem;color:var(--lumen-muted,#9aa3b5);font-size:10.5px;}",
            ".site-dl-sheet{position:fixed;inset:0;z-index:10006;display:grid;place-items:center;padding:1rem;background:rgba(4,7,14,.6);}",
            ".site-dl-sheet[hidden]{display:none!important;}",
            ".site-dl-sheet__panel{box-sizing:border-box;width:min(460px,100%);max-height:min(78vh,640px);overflow:auto;padding:.9rem;border:1px solid var(--lumen-line-strong,rgba(255,255,255,.24));border-radius:16px;background:var(--lumen-panel,#14161f);color:var(--lumen-text,#f4f6fb);box-shadow:0 30px 70px rgba(0,0,0,.55);font:500 12px/1.4 var(--lumen-body,system-ui,sans-serif);}",
            ".site-dl-dock-btn{display:inline-flex;align-items:center;gap:.35rem;}",
            ".site-dl-dock-btn__count{min-width:18px;padding:0 .25rem;border-radius:999px;background:var(--lumen-accent,#6b9fff);color:var(--lumen-on-accent,#fff);font-size:10px;font-weight:800;line-height:16px;text-align:center;}",
            ".site-dl-visually-hidden{position:absolute!important;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0;}",
            "@media (prefers-reduced-motion: reduce){.site-dl-bar__fill{transition:none;}}"
        ].join("");
        doc.head.appendChild(style);
    }

    /* ------------------------------------------------------------------- DOM */
    function element(tag, className, text) {
        var node = doc.createElement(tag);
        if (className) node.className = className;
        if (text != null) node.textContent = text;
        return node;
    }

    function buildCard(job) {
        var card = element("div", "site-dl-card");
        card.setAttribute("role", "status");
        card.setAttribute("aria-live", "polite");
        var top = element("div", "site-dl-card__top");
        top.appendChild(element("span", "site-dl-card__name", job.name));
        top.appendChild(element("span", "site-dl-card__pct", "0%"));
        card.appendChild(top);
        var bar = element("div", "site-dl-bar");
        var fill = element("div", "site-dl-bar__fill");
        bar.appendChild(fill);
        card.appendChild(bar);
        var meta = element("div", "site-dl-card__meta");
        meta.appendChild(element("span", "site-dl-card__speed", ""));
        meta.appendChild(element("span", "site-dl-card__eta", ""));
        card.appendChild(meta);
        var row = element("div", "site-dl-card__row");
        row.appendChild(element("span", "site-dl-card__state", t("Preparing…")));
        var cancel = element("button", "site-dl-card__cancel", t("Cancel"));
        cancel.type = "button";
        cancel.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation();
            cancelJob(job);
        });
        row.appendChild(cancel);
        card.appendChild(row);
        return card;
    }

    function buildRow(job) {
        var row = element("div", "site-dl-row");
        row.setAttribute("data-dl-job", job.id);
        var top = element("div", "site-dl-row__top");
        top.appendChild(element("span", "site-dl-row__name", job.name));
        top.appendChild(element("span", "site-dl-row__pct", "0%"));
        row.appendChild(top);
        var bar = element("div", "site-dl-bar");
        bar.appendChild(element("div", "site-dl-bar__fill"));
        row.appendChild(bar);
        var meta = element("div", "site-dl-row__meta");
        meta.appendChild(element("span", "site-dl-row__speed", ""));
        meta.appendChild(element("span", "site-dl-row__eta", ""));
        row.appendChild(meta);
        return row;
    }

    function tray() {
        if (ui.tray) return ui.tray;
        var node = element("section", "site-dl-tray");
        node.id = "site-dl-tray";
        node.setAttribute("aria-label", t("Downloads"));
        var head = element("div", "site-dl-tray__head");
        var title = element("p", "site-dl-tray__title", t("Downloads"));
        head.appendChild(title);
        var openAll = element("button", "site-dl-tray__btn", t("Show downloads"));
        openAll.type = "button";
        openAll.addEventListener("click", function () { openSheet(true); });
        head.appendChild(openAll);
        var hide = element("button", "site-dl-tray__btn", "×");
        hide.type = "button";
        hide.setAttribute("aria-label", t("Cancel"));
        hide.addEventListener("click", function () { trayCollapsed = true; syncUi(); });
        head.appendChild(hide);
        node.appendChild(head);
        var list = element("div", "site-dl-tray__list");
        node.appendChild(list);
        node.hidden = true;
        doc.body.appendChild(node);
        ui.tray = node;
        ui.trayList = list;
        ui.trayTitle = title;
        return node;
    }

    function sheet() {
        if (ui.sheet) return ui.sheet;
        var overlay = element("div", "site-dl-sheet");
        overlay.id = "site-dl-sheet";
        overlay.hidden = true;
        overlay.addEventListener("click", function (event) {
            if (event.target === overlay) openSheet(false);
        });
        var panel = element("div", "site-dl-sheet__panel");
        panel.setAttribute("role", "dialog");
        panel.setAttribute("aria-modal", "true");
        panel.setAttribute("aria-label", t("Downloads"));
        var head = element("div", "site-dl-tray__head");
        var title = element("p", "site-dl-tray__title", t("Downloads"));
        head.appendChild(title);
        var close = element("button", "site-dl-tray__btn", "×");
        close.type = "button";
        close.setAttribute("aria-label", t("Cancel"));
        close.addEventListener("click", function () { openSheet(false); });
        head.appendChild(close);
        panel.appendChild(head);
        var list = element("div", "site-dl-tray__list");
        panel.appendChild(list);
        overlay.appendChild(panel);
        doc.body.appendChild(overlay);
        ui.sheet = overlay;
        ui.sheetList = list;
        return overlay;
    }

    function openSheet(open) {
        var overlay = sheet();
        sheetOpen = Boolean(open);
        overlay.hidden = !sheetOpen;
        if (sheetOpen) {
            renderList(ui.sheetList, true);
            var first = overlay.querySelector("button");
            if (first && typeof first.focus === "function") first.focus();
        }
    }

    function renderList(host, expanded) {
        if (!host) return;
        host.textContent = "";
        var visible = jobs.filter(function (job) { return !job.dismissed; });
        if (!visible.length) {
            host.appendChild(element("p", "site-dl-row__meta", t("Downloads")));
            return;
        }
        visible.forEach(function (job) {
            var row = buildRow(job);
            row.setAttribute("data-dl-job", String(job.id));
            if (!expanded && job.anchorVisible) row.hidden = true;
            host.appendChild(row);
            paint(job);
        });
    }

    function dockButton() {
        if (ui.dockButton || !doc.body) return ui.dockButton;
        var host = doc.querySelector("#support-toolbar-container .y1-site-dock-bar") ||
            doc.getElementById("support-toolbar-container");
        if (!host) return null;
        var button = element("button", "y1-dock-btn site-dl-dock-btn");
        button.type = "button";
        button.id = "site-dl-dock-btn";
        var label = element("span", "site-dl-dock-btn__label", t("Downloads"));
        button.appendChild(label);
        var count = element("span", "site-dl-dock-btn__count", "0");
        count.hidden = true;
        button.appendChild(count);
        button.addEventListener("click", function () { openSheet(!sheetOpen); });
        host.appendChild(button);
        ui.dockButton = button;
        ui.dockCount = count;
        ui.dockLabel = label;
        return button;
    }

    /* ---------------------------------------------------------------- painting */
    function paint(job) {
        var percent = job.total ? Math.min(100, (job.loaded / job.total) * 100) : 0;
        var pctText = job.total ? Math.round(percent) + "%" : "";
        var speedText = job.status === "running" && job.loaded
            ? bytes(speedOf(job)) + "/s"
            : job.status === "done" ? bytes(job.loaded) : "";
        var eta = etaOf(job);
        var etaText = eta ? t("Time left") + " " + seconds(eta) : "";

        function apply(root) {
            if (!root) return;
            var fill = root.querySelector(".site-dl-bar__fill");
            if (fill) fill.style.width = (job.total ? percent : 34) + "%";
            root.classList.toggle("is-indeterminate", !job.total && job.status === "running");
            var pct = root.querySelector(".site-dl-row__pct, .site-dl-card__pct");
            if (pct) pct.textContent = pctText;
            var speed = root.querySelector(".site-dl-row__speed, .site-dl-card__speed");
            if (speed) speed.textContent = speedText;
            var left = root.querySelector(".site-dl-row__eta, .site-dl-card__eta");
            if (left) left.textContent = etaText;
            root.classList.toggle("is-done", job.status === "done");
            root.classList.toggle("is-failed", job.status === "failed");
        }

        apply(job.card);
        var rows = doc.querySelectorAll('[data-dl-job="' + job.id + '"]');
        Array.prototype.forEach.call(rows, function (row) { apply(row); });

        if (job.card) {
            var state = job.card.querySelector(".site-dl-card__state");
            if (state) {
                var wording = job.status === "done" ? t("Saved")
                    : job.status === "failed" ? t("Failed")
                    : job.status === "handoff" ? t("Your browser takes over")
                    : job.status === "running" ? t("Downloading…") : t("Preparing…");
                if (state.textContent !== wording) state.textContent = wording;
            }
            var cancel = job.card.querySelector(".site-dl-card__cancel");
            if (cancel) cancel.hidden = job.status === "done" || job.status === "failed" || job.status === "handoff";
        }
        syncDock();
    }

    function syncDock() {
        var button = dockButton();
        if (!button) return;
        var active = jobs.filter(function (job) { return !job.dismissed; });
        var running = active.filter(function (job) { return job.status === "running" || job.status === "starting"; });
        ui.dockCount.textContent = String(running.length || active.length);
        ui.dockCount.hidden = !active.length;
        button.hidden = !active.length;
    }

    /* The corner tray only speaks for downloads the reader can no longer see:
       a card is already above the link in the viewport. */
    function syncUi() {
        var trayList = ui.trayList;
        if (!jobs.length) {
            if (ui.tray) ui.tray.hidden = true;
            syncDock();
            return;
        }
        var offscreen = jobs.filter(function (job) {
            return !job.dismissed && !job.anchorVisible && job.status !== "done";
        });
        var finished = jobs.filter(function (job) { return !job.dismissed && job.status === "done"; });
        var show = offscreen.length > 0 || finished.length > 0;
        var node = tray();
        node.hidden = !show || trayCollapsed;
        if (sheetOpen) renderList(ui.sheetList, true);
        if (!trayList || node.hidden) {
            syncDock();
            return;
        }
        /* One row per job, reused across ticks so the list does not flicker. */
        var wanted = offscreen.concat(finished);
        var seen = {};
        wanted.forEach(function (job) {
            seen[job.id] = true;
            var row = trayList.querySelector('[data-dl-job="' + job.id + '"]');
            if (!row) {
                row = buildRow(job);
                row.setAttribute("data-dl-job", String(job.id));
                trayList.appendChild(row);
            }
            paint(job);
        });
        Array.prototype.forEach.call(trayList.querySelectorAll("[data-dl-job]"), function (row) {
            if (!seen[row.getAttribute("data-dl-job")]) row.parentNode.removeChild(row);
        });
        syncDock();
    }

    /* ------------------------------------------------------------- positioning */
    function placeCard(job) {
        var card = job.card;
        var anchor = job.anchor;
        if (!card) return;
        if (!anchor || !anchor.isConnected) {
            card.hidden = true;
            return;
        }
        var rect = anchor.getBoundingClientRect();
        var viewH = global.innerHeight || 0;
        var visible = rect.bottom > 8 && rect.top < viewH - 8;
        job.anchorVisible = visible;
        card.hidden = !visible;
        if (!visible) return;
        card.style.visibility = "hidden";
        card.style.left = "0px";
        card.style.top = "0px";
        var size = card.getBoundingClientRect();
        var left = Math.min(Math.max(8, rect.left), Math.max(8, (global.innerWidth || 0) - size.width - 8));
        var top = rect.top - size.height - 10;
        if (top < 8) top = Math.min(viewH - size.height - 8, rect.bottom + 10);
        card.style.left = Math.round(left) + "px";
        card.style.top = Math.round(top) + "px";
        card.style.visibility = "";
    }

    function placeCards() {
        jobs.forEach(placeCard);
        syncUi();
    }

    /* ------------------------------------------------------------------ jobs */
    function filenameOf(url, response) {
        var name = "";
        try {
            var parsed = new global.URL(url, global.location.href);
            name = decodeURIComponent(parsed.pathname.split("/").pop() || "");
        } catch (_) {}
        if (response) {
            var header = "";
            try { header = response.headers.get("content-disposition") || ""; } catch (_) {}
            var match = /filename\*?=(?:UTF-8''|")?([^";]+)/i.exec(header);
            if (match) name = decodeURIComponent(match[1]);
        }
        return name || "download.bin";
    }

    function cancelJob(job) {
        job.cancelled = true;
        if (job.controller) {
            try { job.controller.abort(); } catch (_) {}
        }
        job.dismissed = true;
        if (job.anchor && jobByAnchor) jobByAnchor.delete(job.anchor);
        if (job.card && job.card.parentNode) job.card.parentNode.removeChild(job.card);
        syncUi();
    }

    function saveBlob(blob, name) {
        var href = global.URL.createObjectURL(blob);
        var link = element("a");
        link.href = href;
        link.download = name;
        link.rel = "noopener";
        doc.body.appendChild(link);
        link.click();
        setTimeout(function () {
            if (link.parentNode) link.parentNode.removeChild(link);
            global.URL.revokeObjectURL(href);
        }, 30000);
    }

    function handOff(job, url) {
        job.status = "handoff";
        paint(job);
        var link = element("a");
        link.href = url;
        link.rel = "noopener";
        if (job.name) link.download = job.name;
        doc.body.appendChild(link);
        link.click();
        setTimeout(function () {
            if (link.parentNode) link.parentNode.removeChild(link);
            finish(job);
        }, 1200);
    }

    function finish(job) {
        job.dismissed = true;
        if (job.anchor && jobByAnchor) jobByAnchor.delete(job.anchor);
        if (job.observer) {
            try { job.observer.disconnect(); } catch (_) {}
        }
        if (job.card && job.card.parentNode) job.card.parentNode.removeChild(job.card);
        syncUi();
        setTimeout(function () {
            var index = jobs.indexOf(job);
            if (index !== -1 && job.status !== "running") jobs.splice(index, 1);
            syncDock();
        }, 8000);
    }

    function fail(job, error, url) {
        if (job.cancelled) return;
        job.status = "failed";
        paint(job);
        if (job.card) {
            var cancel = job.card.querySelector(".site-dl-card__cancel");
            if (cancel) {
                cancel.hidden = false;
                cancel.textContent = t("Cancel");
                cancel.onclick = function () {
                    if (job.card && job.card.parentNode) job.card.parentNode.removeChild(job.card);
                    job.dismissed = true;
                    syncUi();
                };
            }
        }
        /* A blocked download is still a download: let the browser have it
           rather than leaving the reader with a red bar and no file. */
        handOff(job, url || job.url);
    }

    async function start(job, url) {
        job.status = "starting";
        job.started = Date.now();
        job.startedAt = typeof performance !== "undefined" && performance.now ? performance.now() : Date.now();
        paint(job);
        var controller = typeof AbortController === "function" ? new AbortController() : null;
        job.controller = controller;
        var response;
        try {
            response = await fetch(url, {
                mode: "cors",
                credentials: "omit",
                redirect: "follow",
                signal: controller ? controller.signal : undefined
            });
        } catch (error) {
            fail(job, error, url);
            return;
        }
        if (!response || !response.ok) {
            fail(job, new Error("HTTP " + (response ? response.status : 0)), url);
            return;
        }
        job.name = job.name || filenameOf(url, response);
        var length = Number(response.headers.get("content-length") || 0);
        job.total = Number.isFinite(length) ? length : 0;
        job.status = "running";
        paint(job);

        /* Chromium can write the response straight to a file: no 1.5 GB blob
           in memory, and progress that matches what the disk is receiving. */
        var writer = null;
        /* Reading the body is only worth it when the bytes have somewhere to
           go. Without a file handle a huge or unmeasured response is handed
           to the browser untouched; streaming it first would download it
           twice. */
        var canBuffer = job.total > 0 && job.total <= BIG_BLOB;
        if (typeof global.showSaveFilePicker === "function") {
            try {
                var handle = await global.showSaveFilePicker({
                    suggestedName: job.name,
                    types: [{ description: t("Downloads"), accept: { "application/octet-stream": ["." + (job.name.split(".").pop() || "bin")] } }]
                });
                var writable = await handle.createWritable();
                writer = writable;
            } catch (error) {
                if (error && error.name === "AbortError") {
                    cancelJob(job);
                    return;
                }
                writer = null;
            }
        }
        if (!writer && !canBuffer) {
            handOff(job, url);
            return;
        }

        var chunks = canBuffer && !writer ? [] : null;
        var reader;
        try {
            reader = response.body && typeof response.body.getReader === "function" ? response.body.getReader() : null;
        } catch (_) {
            reader = null;
        }
        if (!reader) {
            if (writer) { try { await writer.abort(); } catch (_) {} }
            handOff(job, url);
            return;
        }

        var lastPaint = 0;
        var lastSample = 0;
        try {
            while (true) {
                var step = await reader.read();
                if (step.done) break;
                var chunk = step.value;
                job.loaded += chunk.byteLength;
                if (writer) await writer.write(chunk);
                else if (chunks) chunks.push(chunk);
                var now = Date.now();
                if (now - lastSample > 400) {
                    job.samples.push({ at: now, bytes: job.loaded });
                    if (job.samples.length > 24) job.samples.shift();
                    lastSample = now;
                }
                if (now - lastPaint > TICK) {
                    lastPaint = now;
                    paint(job);
                }
                if (job.cancelled) {
                    try { await reader.cancel(); } catch (_) {}
                    return;
                }
            }
        } catch (error) {
            if (writer) { try { await writer.abort(); } catch (_) {} }
            if (job.cancelled) return;
            fail(job, error, url);
            return;
        }

        job.status = "done";
        if (!job.total) job.total = job.loaded;
        if (writer) {
            try { await writer.close(); } catch (_) {}
        } else if (chunks) {
            saveBlob(new Blob(chunks, { type: response.headers.get("content-type") || "application/octet-stream" }), job.name);
        } else {
            /* No writer and no buffer: the response was read only to report
               progress, so hand the finished file to the browser. */
            handOff(job, url);
            return;
        }
        paint(job);
        setTimeout(function () { finish(job); }, 6000);
    }

    function queue(url, anchor, name) {
        injectStyles();
        dockButton();
        if (anchor && jobByAnchor && jobByAnchor.get(anchor)) return;
        var active = jobs.filter(function (job) { return job.status === "running" || job.status === "starting"; });
        if (active.length >= MAX_JOBS) {
            /* The reader asked for a fourth file; the browser can still take
               it, but the page is not going to animate four streams. */
            return false;
        }
        var job = {
            id: ++seq,
            url: url,
            name: name || filenameOf(url),
            anchor: anchor || null,
            status: "starting",
            loaded: 0,
            total: 0,
            lastSpeed: 0,
            samples: [],
            anchorVisible: true,
            dismissed: false,
            cancelled: false
        };
        trayCollapsed = false;
        jobs.push(job);
        if (anchor && jobByAnchor) jobByAnchor.set(anchor, job);
        if (anchor && anchor.parentNode) {
            job.card = buildCard(job);
            job.card.hidden = true;
            doc.body.appendChild(job.card);
        }
        if (anchor && global.IntersectionObserver) {
            try {
                job.observer = new IntersectionObserver(function (entries) {
                    entries.forEach(function (entry) {
                        job.anchorVisible = entry.isIntersecting;
                        placeCard(job);
                        syncUi();
                    });
                }, { threshold: 0.15 });
                job.observer.observe(anchor);
            } catch (_) {}
        }
        start(job, url);
        placeCards();
        return true;
    }

    /* ---------------------------------------------------------------- events */
    function anchorOf(target) {
        var node = target;
        while (node && node !== doc.body) {
            if (node.tagName && node.tagName === "A" && node.getAttribute("href")) return node;
            node = node.parentNode;
        }
        return null;
    }

    function streamable(link) {
        if (!link || link.hasAttribute("data-no-inpage-download")) return false;
        var href = link.getAttribute("href") || "";
        if (!href || href.charAt(0) === "#" || /^(mailto|tel|javascript):/i.test(href)) return false;
        var explicit = link.hasAttribute("data-inpage-download");
        if (!explicit && !STREAMABLE.test(href)) return false;
        return true;
    }

    function onClick(event) {
        if (event.defaultPrevented || event.button !== 0) return;
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        var link = anchorOf(event.target);
        if (!streamable(link)) return;
        if (link.target && link.target !== "_self") return;
        var href = link.href || link.getAttribute("href");
        /* A same-page blob or data URL is not something to stream again. */
        if (/^(blob|data):/i.test(href)) return;
        var started = queue(href, link, link.getAttribute("data-download-name") || link.getAttribute("download") || "");
        if (started === false) return;
        event.preventDefault();
    }

    function watchDownloads(scope) {
        var root = scope || doc;
        var links = root.querySelectorAll ? root.querySelectorAll("a[href]") : [];
        Array.prototype.forEach.call(links, function (link) {
            if (!streamable(link) || link.hasAttribute("data-site-download-ready")) return;
            link.setAttribute("data-site-download-ready", "1");
        });
    }

    function boot() {
        if (!doc.body) return;
        injectStyles();
        watchDownloads(doc);
        doc.addEventListener("click", onClick, true);
        global.addEventListener("scroll", placeCards, { passive: true });
        global.addEventListener("resize", placeCards);
        doc.addEventListener("keydown", function (event) {
            if (event.key === "Escape" && sheetOpen) openSheet(false);
        });
        global.addEventListener("y1-locale-change", function () {
            jobs.forEach(paint);
            syncUi();
        });
        var observer = typeof MutationObserver === "function" ? new MutationObserver(function () { watchDownloads(doc); }) : null;
        if (observer) observer.observe(doc.body, { childList: true, subtree: true });
        dockButton();

        /* The older firmware-list progress panel wrote English sentences into
           the page. Translate them in place so a reader who picked Japanese
           does not get "Preparing your download…" in the middle of Japanese. */
        var legacy = {
            "Preparing your download…": "Preparing…",
            "Downloading…": "Downloading…",
            "Firmware zip downloaded": "Saved",
            "Check your Downloads folder": "Saved"
        };
        function localizeLegacy() {
            var label = doc.getElementById("lumen-download-progress-label");
            if (!label) return;
            var source = legacy[label.textContent];
            if (!source) return;
            var translated = t(source);
            if (translated && translated !== label.textContent) label.textContent = translated;
        }
        if (typeof MutationObserver === "function") {
            new MutationObserver(localizeLegacy).observe(doc.body, {
                childList: true, subtree: true, characterData: true
            });
        }
        localizeLegacy();
    }

    global.InnioasisDownloads = {
        version: VERSION,
        start: function (url, anchor, name) { return queue(url, anchor, name); },
        jobs: function () { return jobs.slice(); },
        open: function () { openSheet(true); }
    };

    if (doc.readyState === "loading") doc.addEventListener("DOMContentLoaded", boot);
    else boot();
})(typeof window !== "undefined" ? window : globalThis);
