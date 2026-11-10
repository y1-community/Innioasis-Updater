/* In-page downloads for Innioasis.

   A click on a firmware zip, a portable package, an installer, a driver or a
   file linked from a guide normally hands the reader to the browser's own
   download shelf: no progress on the page, no speed, no way to see how long a
   1.5 GB image will take. This module takes those clicks, streams the file,
   and draws progress directly beside the button that was clicked — the same
   inline pattern the Themes Gallery uses.

   There is deliberately no corner tray, no download sheet and no footer dock
   button. Progress belongs to the control the reader just pressed: an inline
   card that opens under it with percent, transferred bytes, speed and time
   left, and scrolls itself into view so the reader sees it start.

   Every job is tied to its own link, so two downloads run side by side
   without any global list to get out of step. While a download is running the
   page warns before it is closed or reloaded.

   Where the File System Access API exists the bytes are written straight to a
   file the reader picks, so a 1.5 GB image never sits in a JavaScript array.
   Without it, files up to 128 MB are buffered into a blob; larger or
   unmeasured responses are handed to the browser once, with an inline note
   that the browser has taken over. A blocked CORS response must never turn a
   download into a dead click — and never into a second click of its own.
*/
(function (global) {
    "use strict";
    if (global.InnioasisDownloads) return;

    var doc = global.document;
    if (!doc || !global.addEventListener) return;

    var VERSION = "20261110inline3";
    /* Only archive packages get the in-page treatment. Installers and app
       images always go to the browser's own downloader: a page must never
       stand between a reader and the app they are installing. */
    var STREAMABLE = /\.(zip|7z)(\?|#|$)/i;
    var NEVER_STREAM = /\.(exe|dmg|appimage|msi|pkg|apk|img|bin|iso|jar|ipa)(\?|#|$)/i;
    /* rom_y1-windows.zip is a portable build of rom_y1.zip, so a portable
       download saves under the mother package's name. */
    var PORTABLE_SUFFIX = /[-_.](windows|win32|win64|win|macos|mac|osx|darwin|linux|android|portable|x64|amd64|x86_64|x86-64|x86|arm64|aarch64)(?:[-_.](x64|amd64|x86_64|x86-64|x86|arm64|aarch64))?(\.zip)$/i;
    /* A blob that big is the most a phone can hold while still rendering. */
    var BLOB_LIMIT = 128 * 1024 * 1024;
    var MAX_JOBS = 2;
    var TICK = 150;

    var jobs = [];
    var seq = 0;
    var jobByAnchor = typeof WeakMap === "function" ? new WeakMap() : null;
    var stylesInjected = false;

    /* ------------------------------------------------------------- wording

       Download wording is the one part of the site a reader sees while the
       page is busy, so it has to match the language they picked. The published
       catalogs answer first; the table below covers the languages where the
       UI sentence has not made it into a catalog yet. A miss is still shown in
       English rather than blank. */
    var WORDING = {
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
        "Keep this tab open": {
            de: "Diesen Tab geöffnet lassen", fr: "Gardez cet onglet ouvert",
            es: "Mantén esta pestaña abierta", it: "Tieni aperta questa scheda",
            pt: "Mantenha este separador aberto", "pt-BR": "Mantenha esta aba aberta",
            nl: "Houd dit tabblad open", pl: "Pozostaw tę kartę otwartą",
            ru: "Не закрывайте эту вкладку", uk: "Не закривайте цю вкладку",
            ja: "このタブを開いたままにしてください", ko: "이 탭을 열어 두세요",
            "zh-CN": "请保持此标签页打开", "zh-TW": "請保持此分頁開啟",
            tr: "Bu sekmeyi açık tutun", ar: "اترك هذا التبويب مفتوحًا",
            hi: "यह टैब खुला रखें", id: "Biarkan tab ini terbuka",
            vi: "Giữ tab này mở", th: "เปิดแท็บนี้ไว้", sv: "Håll fliken öppen",
            da: "Behold denne fane", fi: "Pidä tämä välilehti auki",
            cs: "Nechte tuto kartu otevřenou", el: "Κρατήστε αυτή την καρτέλα ανοιχτή",
            he: "השאירו כרטיסייה זו פתוחה", hu: "Tartsa nyitva ezt a lapot",
            ro: "Ține acest tab deschis", bg: "Оставете този раздел отворен"
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
            ".site-dl-progress{display:grid;gap:.45rem;box-sizing:border-box;width:100%;max-width:540px;margin:.55rem 0 .25rem;padding:.7rem .8rem;border:1px solid var(--lumen-line-strong,rgba(255,255,255,.22));border-radius:12px;background:var(--lumen-panel-soft,var(--lumen-panel,#161a24));color:var(--lumen-text,#f4f6fb);box-shadow:0 8px 22px rgba(0,0,0,.24);font:500 12.5px/1.4 var(--lumen-body,system-ui,sans-serif);text-align:start;}",
            ".site-dl-progress[hidden]{display:none!important;}",
            ".site-dl-progress__head{display:flex;align-items:center;gap:.55rem;min-width:0;}",
            ".site-dl-progress__icon{display:inline-flex;align-items:center;justify-content:center;flex:0 0 auto;width:22px;height:22px;border-radius:999px;background:color-mix(in oklab,var(--lumen-accent,#6b9fff) 20%,transparent);color:var(--lumen-accent,#6b9fff);}",
            ".site-dl-progress__name{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:750;}",
            ".site-dl-progress__pct{flex:0 0 auto;font-variant-numeric:tabular-nums;font-weight:800;color:var(--lumen-accent,#6b9fff);}",
            ".site-dl-progress__bar{position:relative;height:6px;border-radius:999px;background:color-mix(in oklab,var(--lumen-text,#fff) 14%,transparent);overflow:hidden;}",
            ".site-dl-progress__fill{height:100%;width:0;border-radius:inherit;background:var(--lumen-accent,#6b9fff);transition:width .2s linear;}",
            ".site-dl-progress__stats{display:flex;flex-wrap:wrap;align-items:center;gap:.3rem .75rem;color:var(--lumen-muted,#9aa3b5);font-size:11px;font-variant-numeric:tabular-nums;}",
            ".site-dl-progress__state{flex:1 1 auto;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}",
            ".site-dl-progress__cancel{flex:0 0 auto;border:0;background:none;padding:0;color:inherit;font:inherit;font-size:11px;text-decoration:underline;text-underline-offset:2px;cursor:pointer;}",
            ".site-dl-progress__cancel:hover{color:var(--lumen-text,#fff);}",
            ".site-dl-progress.is-indeterminate .site-dl-progress__fill{width:34%!important;animation:site-dl-drift 1.15s ease-in-out infinite alternate;}",
            "@keyframes site-dl-drift{from{transform:translateX(-16%);}to{transform:translateX(190%);}}",
            ".site-dl-progress.is-done .site-dl-progress__fill{background:#43c98b;}",
            ".site-dl-progress.is-done .site-dl-progress__pct{color:#43c98b;}",
            ".site-dl-progress.is-done .site-dl-progress__icon{background:rgba(67,201,139,.18);color:#43c98b;}",
            ".site-dl-progress.is-failed .site-dl-progress__fill{background:#e2564f;}",
            ".site-dl-progress.is-handoff .site-dl-progress__fill{width:100%!important;background:color-mix(in oklab,var(--lumen-accent,#6b9fff) 55%,transparent);}",
            ".site-dl-progress-item{list-style:none;}",
            "@media (prefers-reduced-motion: reduce){.site-dl-progress__fill{transition:none;}.site-dl-progress.is-indeterminate .site-dl-progress__fill{animation:none;}}"
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

    function buildPanel(job) {
        var panel = element("div", "site-dl-progress");
        panel.setAttribute("role", "status");
        panel.setAttribute("aria-live", "polite");

        var head = element("div", "site-dl-progress__head");
        var icon = element("span", "site-dl-progress__icon");
        icon.setAttribute("aria-hidden", "true");
        icon.innerHTML = '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11"/><path d="m7 11 5 5 5-5"/><path d="M5 20h14"/></svg>';
        head.appendChild(icon);
        head.appendChild(element("span", "site-dl-progress__name", job.name));
        head.appendChild(element("span", "site-dl-progress__pct", "0%"));
        panel.appendChild(head);

        var bar = element("div", "site-dl-progress__bar");
        bar.appendChild(element("div", "site-dl-progress__fill"));
        panel.appendChild(bar);

        var stats = element("div", "site-dl-progress__stats");
        var state = element("span", "site-dl-progress__state", t("Preparing…"));
        stats.appendChild(state);
        stats.appendChild(element("span", "site-dl-progress__size", ""));
        stats.appendChild(element("span", "site-dl-progress__speed", ""));
        stats.appendChild(element("span", "site-dl-progress__eta", ""));
        var cancel = element("button", "site-dl-progress__cancel", t("Cancel"));
        cancel.type = "button";
        cancel.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation();
            cancelJob(job);
        });
        stats.appendChild(cancel);
        panel.appendChild(stats);

        panel.hidden = false;
        return panel;
    }

    /* The card belongs beside the button that was pressed, not floating over
       the page. A button row keeps its own layout; the card follows it. */
    function mount(job, link) {
        var panel = buildPanel(job);
        job.panel = panel;
        var host = null;
        if (!link || !link.closest || !link.parentNode) {
            if (doc.body) doc.body.appendChild(panel);
            return panel;
        }
        try {
            host = link.closest(".lumen-actions, .lumen-release-details, .firmware-list-actions, .lumen-hero-actions, .lumen-button-row, .hero-actions, .btn-row, .actions, li, p, td");
        } catch (_) {}
        if (!host) host = link.parentElement;
        if (!host || !host.parentNode) {
            if (doc.body) doc.body.appendChild(panel);
            return panel;
        }
        if (host.tagName === "TD" || host === link.parentElement) {
            host.appendChild(panel);
            return panel;
        }
        if (host.tagName === "LI") {
            var item = element("li", "site-dl-progress-item");
            item.appendChild(panel);
            host.parentNode.insertBefore(item, host.nextSibling);
            job.holder = item;
            return panel;
        }
        host.parentNode.insertBefore(panel, host.nextSibling);
        return panel;
    }

    function removePanel(job) {
        if (job.panel && job.panel.parentNode) job.panel.parentNode.removeChild(job.panel);
        if (job.holder && job.holder.parentNode) job.holder.parentNode.removeChild(job.holder);
        job.panel = null;
        job.holder = null;
    }

    function inView(node) {
        var rect = node.getBoundingClientRect();
        var viewH = global.innerHeight || 0;
        return rect.top >= 0 && rect.bottom <= viewH;
    }

    /* Show the reader the progress they just started: the card opens where the
       button is, and if that is off screen the page scrolls back to it. */
    function reveal(job) {
        if (!job.panel || !inView(job.panel)) return;
        var reduce = false;
        try {
            reduce = global.matchMedia && global.matchMedia("(prefers-reduced-motion: reduce)").matches;
        } catch (_) {}
        try {
            job.panel.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center", inline: "nearest" });
        } catch (_) {
            try { job.panel.scrollIntoView(); } catch (__) {}
        }
    }

    /* ---------------------------------------------------------------- painting */
    function paint(job) {
        if (!job.panel) return;
        var overrun = job.total && job.loaded > job.total;
        var percent = job.total && !overrun ? (job.loaded / job.total) * 100 : 0;
        var pctText = job.total && !overrun ? Math.round(percent) + "%" : "";
        var speed = speedOf(job);
        var eta = etaOf(job);

        job.panel.classList.toggle("is-done", job.status === "done");
        job.panel.classList.toggle("is-failed", job.status === "failed");
        job.panel.classList.toggle("is-handoff", job.status === "handoff");
        job.panel.classList.toggle("is-indeterminate", (!job.total || overrun) && (job.status === "running" || job.status === "starting"));

        var fill = job.panel.querySelector(".site-dl-progress__fill");
        if (fill) fill.style.width = (job.total && !overrun ? percent : 0) + "%";

        var pct = job.panel.querySelector(".site-dl-progress__pct");
        if (pct) pct.textContent = pctText;

        var size = job.panel.querySelector(".site-dl-progress__size");
        if (size) {
            if (job.total && !overrun) size.textContent = bytes(job.loaded) + " / " + bytes(job.total);
            else if (job.loaded) size.textContent = bytes(job.loaded);
            else size.textContent = "";
        }

        var speedNode = job.panel.querySelector(".site-dl-progress__speed");
        if (speedNode) speedNode.textContent = job.status === "running" && speed > 0 ? bytes(speed) + "/s" : "";

        var etaNode = job.panel.querySelector(".site-dl-progress__eta");
        if (etaNode) etaNode.textContent = eta && !overrun ? t("Time left") + " " + seconds(eta) : "";

        var state = job.panel.querySelector(".site-dl-progress__state");
        if (state) {
            var wording = job.status === "done" ? t("Saved")
                : job.status === "failed" ? t("Failed")
                : job.status === "handoff" ? t("Your browser takes over")
                : job.status === "running" ? t("Keep this tab open")
                : t("Preparing…");
            if (state.textContent !== wording) state.textContent = wording;
        }

        var cancel = job.panel.querySelector(".site-dl-progress__cancel");
        if (cancel) cancel.hidden = job.status === "done" || job.status === "handoff";
    }

    /* ------------------------------------------------------------------- jobs */
    function motherName(name) {
        var base = String(name || "").split(/[?#]/)[0].split(/[\\/]/).pop() || "";
        base = base.replace(/^portable[-_.]/i, "");
        var previous;
        do {
            previous = base;
            base = base.replace(PORTABLE_SUFFIX, "$3");
        } while (base !== previous);
        return base;
    }

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

    function activeJobs() {
        return jobs.filter(function (job) {
            return job.status === "starting" || job.status === "running";
        });
    }

    function cancelJob(job) {
        job.cancelled = true;
        if (job.controller) {
            try { job.controller.abort(); } catch (_) {}
        }
        if (job.writer) {
            try { job.writer.abort(); } catch (_) {}
        }
        if (job.anchor && jobByAnchor) jobByAnchor.delete(job.anchor);
        removePanel(job);
        var index = jobs.indexOf(job);
        if (index !== -1) jobs.splice(index, 1);
    }

    function saveBlob(blob, name) {
        var href = global.URL.createObjectURL(blob);
        var link = element("a");
        link.href = href;
        link.download = name;
        link.rel = "noopener";
        link.setAttribute("data-site-download-direct", "1");
        doc.body.appendChild(link);
        link.click();
        setTimeout(function () {
            if (link.parentNode) link.parentNode.removeChild(link);
            global.URL.revokeObjectURL(href);
        }, 30000);
    }

    /* The one and only path to the browser's own downloader. Marked so the
       click interceptor never claims it: a synthetic anchor click used to come
       straight back through this module and start another copy of the file. */
    function clickDirect(url, name) {
        var link = doc.createElement("a");
        link.href = url;
        if (name) link.download = name;
        link.rel = "noopener";
        link.setAttribute("data-site-download-direct", "1");
        link.style.display = "none";
        doc.body.appendChild(link);
        link.click();
        setTimeout(function () {
            if (link.parentNode) link.parentNode.removeChild(link);
        }, 1500);
    }

    function handOff(job, url) {
        job.status = "handoff";
        paint(job);
        clickDirect(url || job.url, job.name);
        setTimeout(function () {
            if (job.status === "handoff") finish(job, 4000);
        }, 5000);
    }

    function finish(job, delay) {
        if (job.anchor && jobByAnchor) jobByAnchor.delete(job.anchor);
        setTimeout(function () {
            removePanel(job);
            var index = jobs.indexOf(job);
            if (index !== -1) jobs.splice(index, 1);
        }, delay == null ? 12000 : delay);
    }

    async function start(job, url) {
        job.status = "starting";
        paint(job);

        var controller = typeof AbortController === "function" ? new AbortController() : null;
        job.controller = controller;

        /* Chromium can write the response straight to a file: no 1.5 GB blob
           in memory, and progress that matches what the disk is receiving. The
           picker must be opened while the click still counts as a gesture, so
           it comes before the request. */
        /* A 1.8 GB portable package never fits in a JavaScript array, so the
           reader picks a file once and the bytes go straight to disk. A
           small measured package is buffered instead, and a blocked or
           unreadable response falls back to the browser's downloader. */
        var writer = null;
        if (typeof global.showSaveFilePicker === "function") {
            try {
                var extension = "." + ((job.name.split(".").pop() || "bin").toLowerCase());
                var handle = await global.showSaveFilePicker({
                    suggestedName: job.name,
                    types: [{ description: "Download", accept: { "application/octet-stream": [extension] } }]
                });
                writer = await handle.createWritable();
                job.writer = writer;
            } catch (error) {
                if (error && error.name === "AbortError") {
                    cancelJob(job);
                    return;
                }
                writer = null;
            }
        }
        if (job.cancelled) {
            if (writer) { try { await writer.abort(); } catch (_) {} }
            return;
        }

        var response;
        try {
            response = await fetch(url, {
                mode: "cors",
                credentials: "omit",
                redirect: "follow",
                signal: controller ? controller.signal : undefined
            });
        } catch (error) {
            if (job.cancelled) return;
            handOff(job, url);
            return;
        }
        if (!response || !response.ok) {
            if (writer) { try { await writer.abort(); } catch (_) {} }
            handOff(job, url);
            return;
        }

        job.name = motherName(job.name || filenameOf(url, response));
        var length = Number(response.headers.get("content-length") || 0);
        job.total = Number.isFinite(length) && length > 0 ? length : 0;
        job.status = "running";
        paint(job);

        /* Without a file handle, only a measured, small response is worth
           reading: streaming a huge or unmeasured one would download it twice
           or hold it all in memory. Those go to the browser once. */
        if (!writer && (!job.total || job.total > BLOB_LIMIT)) {
            try { if (response.body && response.body.cancel) await response.body.cancel(); } catch (_) {}
            handOff(job, url);
            return;
        }

        var chunks = writer ? null : [];
        var reader = null;
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
                else chunks.push(chunk);
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
                    if (writer) { try { await writer.abort(); } catch (_) {} }
                    return;
                }
            }
        } catch (error) {
            if (writer) { try { await writer.abort(); } catch (_) {} }
            if (job.cancelled) return;
            handOff(job, url);
            return;
        }

        job.status = "done";
        if (!job.total) job.total = job.loaded;
        if (writer) {
            try { await writer.close(); } catch (_) {}
        } else {
            saveBlob(new Blob(chunks, { type: response.headers.get("content-type") || "application/octet-stream" }), job.name);
        }
        paint(job);
        finish(job);
    }

    function queue(url, anchor, name) {
        injectStyles();
        if (anchor && jobByAnchor && jobByAnchor.get(anchor)) return true;
        if (activeJobs().length >= MAX_JOBS) {
            /* The browser can still take it; the page just will not run a third
               stream beside two the reader is already watching. */
            clickDirect(url, name || "");
            return true;
        }
        var job = {
            id: ++seq,
            url: url,
            name: motherName(name || filenameOf(url)),
            anchor: anchor || null,
            status: "starting",
            loaded: 0,
            total: 0,
            lastSpeed: 0,
            samples: [],
            dismissed: false,
            cancelled: false,
            writer: null,
            panel: null
        };
        jobs.push(job);
        if (anchor && jobByAnchor) jobByAnchor.set(anchor, job);
        mount(job, anchor || doc.body);
        paint(job);
        if (job.panel) {
            setTimeout(function () { reveal(job); }, 60);
        }
        start(job, url);
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
        if (!link) return false;
        if (link.hasAttribute("data-no-inpage-download")) return false;
        if (link.hasAttribute("data-site-download-direct")) return false;
        var href = link.getAttribute("href") || "";
        if (!href || href.charAt(0) === "#" || /^(mailto|tel|javascript):/i.test(href)) return false;
        /* Installers and app images belong to the browser, always. */
        if (NEVER_STREAM.test(href)) return false;
        var explicit = link.hasAttribute("data-inpage-download");
        if (!explicit && !STREAMABLE.test(href)) return false;
        return true;
    }

    function onClick(event) {
        /* A scripted anchor click is how this module hands a file to the
           browser. Claiming it again restarted the same download, which is the
           loop that filled the old tray with copies of one file. Only real
           reader clicks may start a job. */
        if (event.isTrusted === false) return;
        if (event.defaultPrevented || event.button !== 0) return;
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        var link = anchorOf(event.target);
        if (!streamable(link)) return;
        if (link.target && link.target !== "_self") return;
        var href = link.href || link.getAttribute("href");
        if (/^(blob|data):/i.test(href)) return;
        var started = queue(href, link, link.getAttribute("data-download-name") || link.getAttribute("download") || "");
        if (started === false) return;
        event.preventDefault();
    }

    function boot() {
        if (!doc.body) return;
        injectStyles();
        doc.addEventListener("click", onClick, true);
        doc.addEventListener("keydown", function (event) {
            if (event.key !== "Escape") return;
            jobs.forEach(function (job) {
                if (job.status === "running" || job.status === "starting") {
                    if (job.panel) job.panel.focus();
                }
            });
        });
        global.addEventListener("y1-locale-change", function () {
            jobs.forEach(paint);
        });

        /* Closing or reloading takes the transfer with it; the reader gets the
           browser's own confirmation while a download is still running. */
        global.addEventListener("beforeunload", function (event) {
            if (!activeJobs().length) return undefined;
            event.preventDefault();
            event.returnValue = t("Keep this tab open");
            return event.returnValue;
        });
    }

    global.InnioasisDownloads = {
        version: VERSION,
        start: function (url, anchor, name) { return queue(url, anchor, name); },
        jobs: function () { return jobs.slice(); }
    };

    if (doc.readyState === "loading") doc.addEventListener("DOMContentLoaded", boot);
    else boot();
})(typeof window !== "undefined" ? window : globalThis);
