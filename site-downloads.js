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
   Where it does not (Safari, Firefox), the ZIP is staged in the browser's own
   origin storage and saved to Downloads only once every byte has arrived. The
   reader therefore watches the whole transfer in the inline card; the browser
   never takes an archive over mid-transfer.
*/
(function (global) {
    "use strict";
    if (global.InnioasisDownloads) return;

    var doc = global.document;
    if (!doc || !global.addEventListener) return;

    var VERSION = "20261117fallback3";
    /* Archives, installers and app images all stream in-page. A driver or app
       download is often the one a reader most wants a speed and time-left for,
       so it deserves the same progress card as a firmware ZIP. Phone packages
       and disk images stay with the browser. */
    var STREAMABLE = /\.(zip|7z|tar\.gz|tgz|tar\.xz|txz|tar\.bz2|tbz2|exe|msi|dmg|pkg|appimage)(\?|#|$)/i;
    var NEVER_STREAM = /\.(apk|img|bin|iso|jar|ipa)(\?|#|$)/i;
    /* The app and driver repositories whose "latest" download links may name
       an asset the newest release does not carry. Those links are resolved
       against the release list before the transfer starts. */
    var RELEASE_RESOLVED_REPO = /(^|\/)(innioasis-updater|supplemental-apks)$/i;
    /* App and driver packages keep their published filename. The portable
       suffix rule below exists for firmware zips, where a mirror adds the
       platform to the name and the saved file must match the release. */
    var APP_DOWNLOAD_URL = /^https:\/\/github\.com\/[^/]+\/(?:innioasis-updater|supplemental-apks|updater-ce-neo)\//i;
    /* rom_y1-windows.zip is a portable build of rom_y1.zip, so a portable
       download saves under the mother package's name. */
    var PORTABLE_SUFFIX = /[-_.](windows-legacy|linux-legacy|windows|win32|win64|win|macos|mac|osx|darwin|linux|android|portable|legacy|x64|amd64|x86_64|x86-64|x86|arm64|aarch64)(?:[-_.](x64|amd64|x86_64|x86-64|x86|arm64|aarch64))?(\.zip)$/i;
    var TICK = 150;

    var jobs = [];
    var seq = 0;
    var jobByAnchor = typeof WeakMap === "function" ? new WeakMap() : null;
    /* Jobs started from the same button row share one card, so an app and a
       driver download running together show two bars with their own speed and
       time left instead of two cards fighting for the same space. */
    var groups = [];
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
        "Download started": {
            de: "Download gestartet", fr: "Téléchargement lancé", es: "Descarga iniciada",
            it: "Download avviato", pt: "Transferência iniciada", "pt-BR": "Download iniciado",
            nl: "Download gestart", pl: "Pobieranie rozpoczęte", ru: "Загрузка началась",
            uk: "Завантаження почалося", ja: "ダウンロードを開始しました", ko: "다운로드가 시작되었습니다",
            "zh-CN": "下载已开始", "zh-TW": "下載已開始", tr: "İndirme başladı",
            ar: "بدأ التنزيل", hi: "डाउनलोड शुरू हो गया", id: "Unduhan dimulai",
            vi: "Đã bắt đầu tải xuống", th: "เริ่มดาวน์โหลดแล้ว", sv: "Nedladdning startad",
            da: "Download startet", fi: "Lataus aloitettu", cs: "Stahování zahájeno",
            el: "Η λήψη ξεκίνησε", he: "ההורדה החלה", hu: "A letöltés elindult",
            ro: "Descărcarea a început", bg: "Изтеглянето започна"
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
        var table = WORDING[english] || (english === "Saved to PC" ? WORDING["Saved"] : null);
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
            ".site-dl-progress-group{position:absolute;z-index:80;display:flex;flex-direction:column;gap:.5rem;width:min(360px,calc(100vw - 1.5rem));}",
            ".site-dl-progress-group .site-dl-progress{max-width:none;margin:0;}",
            ".site-dl-progress[hidden]{display:none!important;}",
            ".site-dl-progress--notice{display:block;position:fixed;left:50%;bottom:1.25rem;transform:translateX(-50%);z-index:90;width:auto;max-width:calc(100vw - 2rem);margin:0;padding:.6rem .95rem;text-align:center;pointer-events:none;font-weight:750;box-shadow:0 10px 28px rgba(0,0,0,.35);}",
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

    function buildGroup() {
        return element("div", "site-dl-progress-group");
    }

    function groupFor(container) {
        for (var i = 0; i < groups.length; i += 1) {
            if (groups[i].container === container) return groups[i].group;
        }
        return null;
    }

    function forgetGroup(group) {
        groups = groups.filter(function (entry) { return entry.group !== group; });
    }

    function anchorContainer(link) {
        if (!link) return null;
        if (link.closest) {
            var row = link.closest(".lumen-actions") || link.closest(".lumen-download-option");
            if (row) return row;
        }
        return link.parentNode;
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
    /* A control that is already a button shows the transfer on itself, so the
       reader never has to look away from the thing they pressed. A plain text
       link keeps the card beside it. */
    function buttonLike(link) {
        if (!link || typeof link.className !== "string") return false;
        return /(^|\s)(lumen-button|lumen-zip-download-button)(\s|$)/.test(link.className);
    }

    function buttonText(job) {
        if (job.status === "done") return t("Saved to PC");
        if (job.status === "failed") return t("Failed");
        var overrun = job.total && job.loaded > job.total;
        var parts = [];
        if (job.total && !overrun) parts.push(Math.round((job.loaded / job.total) * 100) + "%");
        var speed = speedOf(job);
        if (speed > 512) parts.push(bytes(speed) + "/s");
        var eta = etaOf(job);
        /* seconds() returns "" once the estimate rounds below a second, and a
           blank entry would leave a dangling separator on the button. */
        var etaText = eta && !overrun ? seconds(eta) : "";
        if (etaText) parts.push(etaText);
        if (!parts.length) parts.push(t(job.status === "starting" ? "Preparing…" : "Downloading…"));
        return parts.join(" · ");
    }

    function paintButton(job) {
        if (!job.buttonEl) return;
        job.buttonEl.textContent = buttonText(job);
        job.buttonEl.setAttribute("aria-busy", job.status === "running" || job.status === "starting" ? "true" : "false");
    }

    function restoreButton(job) {
        if (job.anchor && job.anchor.removeAttribute) job.anchor.removeAttribute("data-save-busy");
        if (!job.buttonEl) return;
        /* innerHTML, not textContent: a catalog button carries an icon, and a
           finished download must leave the control exactly as it found it. */
        job.buttonEl.innerHTML = job.buttonHtml || job.buttonLabel || "";
        job.buttonEl.removeAttribute("aria-busy");
        job.buttonEl = null;
    }

    function mount(job, link) {
        var row = buildPanel(job);
        job.panel = row;
        if (!doc.body) return row;
        if (!link) {
            var detached = buildGroup();
            detached.style.position = "fixed";
            detached.style.right = "1rem";
            detached.style.bottom = "1rem";
            detached.appendChild(row);
            doc.body.appendChild(detached);
            job.group = detached;
            return row;
        }
        var container = anchorContainer(link);
        var group = container ? groupFor(container) : null;
        if (!group) {
            group = buildGroup();
            doc.body.appendChild(group);
            if (container) groups.push({ container: container, group: group });
        }
        group.appendChild(row);
        job.group = group;
        job.container = container;
        placePanel(job);
        return row;
    }

    /* The card sits over the page beside the pressed link, clear of the table
       cell, and flips above the link when it would fall below the viewport. */
    function placePanel(job) {
        var node = job && (job.group || job.panel);
        var target = job && (job.container || job.anchor);
        if (!node || !target || !target.getBoundingClientRect) return;
        var rect = target.getBoundingClientRect();
        var width = node.offsetWidth || 360;
        var height = node.offsetHeight || 150;
        var gap = 10;
        var viewW = global.innerWidth || 0;
        var viewH = global.innerHeight || 0;
        var left = rect.left + (global.pageXOffset || 0);
        left = Math.max(gap, Math.min(left, viewW - width - gap));
        var top = rect.bottom + (global.pageYOffset || 0) + gap;
        if (rect.bottom + height + gap * 2 > viewH) {
            top = rect.top + (global.pageYOffset || 0) - height - gap;
            if (top < (global.pageYOffset || 0) + gap) {
                top = (global.pageYOffset || 0) + gap;
            }
        }
        node.style.left = Math.round(left) + "px";
        node.style.top = Math.round(top) + "px";
    }

    function removePanel(job) {
        if (job.panel && job.panel.parentNode) job.panel.parentNode.removeChild(job.panel);
        if (job.holder && job.holder.parentNode) job.holder.parentNode.removeChild(job.holder);
        var group = job.group;
        if (group && !group.querySelector(".site-dl-progress")) {
            if (group.parentNode) group.parentNode.removeChild(group);
            forgetGroup(group);
        }
        job.panel = null;
        job.holder = null;
        job.group = null;
        job.container = null;
    }

    function reposition(job) {
        placePanel(job);
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
        job.panel.classList.toggle("is-indeterminate", (!job.total || overrun) && (job.status === "running" || job.status === "starting"));

        var fill = job.panel.querySelector(".site-dl-progress__fill");
        if (fill) fill.style.width = (job.total && !overrun ? percent : 0) + "%";

        var pct = job.panel.querySelector(".site-dl-progress__pct");
        if (pct) {
            pct.hidden = false;
            pct.textContent = pctText;
        }

        var size = job.panel.querySelector(".site-dl-progress__size");
        if (size) {
            if (job.total && !overrun) size.textContent = bytes(job.loaded) + " / " + bytes(job.total);
            else if (job.loaded) size.textContent = bytes(job.loaded);
            else size.textContent = "";
        }

        var speedNode = job.panel.querySelector(".site-dl-progress__speed");
        if (speedNode) {
            speedNode.hidden = false;
            speedNode.textContent = job.status === "running" && speed > 0 ? bytes(speed) + "/s" : "";
        }

        var etaNode = job.panel.querySelector(".site-dl-progress__eta");
        if (etaNode) {
            etaNode.hidden = false;
            etaNode.textContent = eta && !overrun ? t("Time left") + " " + seconds(eta) : "";
        }

        var state = job.panel.querySelector(".site-dl-progress__state");
        if (state) {
            var wording = job.status === "done" ? t("Saved to PC")
                : job.status === "failed" ? t("Failed")
                : job.status === "running" ? t("Keep this tab open")
                : t("Preparing…");
            if (state.textContent !== wording) state.textContent = wording;
        }

        var icon = job.panel.querySelector(".site-dl-progress__icon");
        if (icon) {
            icon.innerHTML = job.status === "done"
                ? '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m5 13 4 4L19 7"/></svg>'
                : job.status === "failed"
                    ? '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="m6 6 12 12M18 6 6 18"/></svg>'
                    : '<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11"/><path d="m7 11 5 5 5-5"/><path d="M5 20h14"/></svg>';
        }

        var cancel = job.panel.querySelector(".site-dl-progress__cancel");
        if (cancel) cancel.hidden = job.status === "done";
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

    function fileNameOf(url) {
        try {
            var parsed = new global.URL(url, global.location.href);
            /* The download proxy carries the name the file must be saved
               under, so a same-origin proxy link still knows its filename. */
            var declared = parsed.searchParams.get("filename");
            if (declared) return decodeURIComponent(declared);
            return decodeURIComponent(parsed.pathname.split("/").pop() || "");
        } catch (_) {
            return "";
        }
    }

    function headerFileName(response) {
        var header = "";
        try { header = response.headers.get("content-disposition") || ""; } catch (_) {}
        var match = /filename\*?=(?:UTF-8''|")?([^";]+)/i.exec(header);
        if (!match) return "";
        try { return decodeURIComponent(match[1]); } catch (_) { return match[1]; }
    }

    /* GitHub serves release assets without CORS headers, so a page cannot read
       one. The site's own proxy streams the same bytes from this origin: real
       progress, a real Content-Length, and the mother package's name. */
    function downloadProxyUrl() {
        var meta = doc.querySelector('meta[name="innioasis-download-proxy"]');
        var value = meta ? (meta.getAttribute("content") || "").trim() : "";
        if (value) return value;
        if (/^https?:$/.test(global.location.protocol)) return "/download-proxy";
        return "";
    }

    function proxiedUrl(url, saveName) {
        if (!/^https:\/\/github\.com\/[^/]+\/[^/]+\/releases\/(?:latest\/)?download\//i.test(String(url || ""))) return url;
        var proxy = downloadProxyUrl();
        if (!proxy) return url;
        var fallback = APP_DOWNLOAD_URL.test(String(url || "")) ? fileNameOf(url) : motherName(fileNameOf(url));
        return proxy + (proxy.indexOf("?") === -1 ? "?" : "&") +
            "url=" + encodeURIComponent(url) +
            "&filename=" + encodeURIComponent(saveName || fallback || "firmware.zip");
    }

    function cancelJob(job) {
        job.cancelled = true;
        clearStall(job);
        if (job.controller) {
            try { job.controller.abort(); } catch (_) {}
        }
        abortSink(job);
        if (job.anchor && jobByAnchor) jobByAnchor.delete(job.anchor);
        restoreButton(job);
        removePanel(job);
        var index = jobs.indexOf(job);
        if (index !== -1) jobs.splice(index, 1);
    }

    /* A completed file is the only thing this module gives to the browser's
       downloader. By the time this runs every byte is already on the computer,
       so the browser merely saves it under the release's own name. */
    function saveBlob(blob, name) {
        var href = global.URL.createObjectURL(blob);
        var link = element("a");
        link.href = href;
        link.download = name;
        link.rel = "noopener";
        link.setAttribute("data-site-download-direct", "1");
        link.setAttribute("data-direct-download", "1");
        doc.body.appendChild(link);
        link.click();
        setTimeout(function () {
            if (link.parentNode) link.parentNode.removeChild(link);
            global.URL.revokeObjectURL(href);
        }, 120000);
    }

    function finish(job, delay) {
        if (job.anchor && jobByAnchor) jobByAnchor.delete(job.anchor);
        setTimeout(function () {
            restoreButton(job);
            removePanel(job);
            var index = jobs.indexOf(job);
            if (index !== -1) jobs.splice(index, 1);
        }, delay == null ? 12000 : delay);
    }

    /* An in-page failure must never strand the reader. Close the card, abort
       the private stream, and hand the direct asset URL to the browser once.
       The job flag keeps a rejected fetch, a writer abort and a stall timer
       from starting a second copy. */
    function failJob(job) {
        if (!job || job.cancelled || job.fallbackStarted || job.status === "done") return;
        fallbackToBrowser(job, job.directUrl || job.url || "");
    }

    var startedNotice = null;

    function showStarted() {
        if (!doc.body) return;
        if (startedNotice && startedNotice.parentNode) startedNotice.parentNode.removeChild(startedNotice);
        startedNotice = element("div", "site-dl-progress site-dl-progress--notice", t("Download started"));
        startedNotice.setAttribute("role", "status");
        startedNotice.setAttribute("aria-live", "polite");
        doc.body.appendChild(startedNotice);
        setTimeout(function () {
            if (startedNotice && startedNotice.parentNode) startedNotice.parentNode.removeChild(startedNotice);
            if (startedNotice && !startedNotice.parentNode) startedNotice = null;
        }, 5000);
    }

    function fallbackToBrowser(job, direct) {
        if (!job || job.fallbackStarted) return;
        job.fallbackStarted = true;
        job.status = "failed";
        clearStall(job);
        if (job.controller) {
            try { job.controller.abort(); } catch (_) {}
        }
        abortSink(job);
        if (job.anchor && jobByAnchor) jobByAnchor.delete(job.anchor);
        restoreButton(job);
        removePanel(job);
        var index = jobs.indexOf(job);
        if (index !== -1) jobs.splice(index, 1);
        if (!direct) return;
        var link = element("a");
        link.href = direct;
        if (job.name) link.download = job.name;
        link.rel = "noopener";
        link.setAttribute("data-site-download-direct", "1");
        link.setAttribute("data-direct-download", "1");
        doc.body.appendChild(link);
        var triggered = false;
        try { link.click(); triggered = true; }
        catch (_) { try { global.location.assign(direct); triggered = true; } catch (__) {} }
        if (triggered) showStarted();
        setTimeout(function () {
            if (link.parentNode) link.parentNode.removeChild(link);
        }, 60000);
    }

    /* Abort a write and remove any private copy. The delay lets the writer
       release its lock before the entry is deleted. */
    function dropStaging(job, when) {
        var staging = job.staging;
        if (!staging) return;
        job.staging = null;
        setTimeout(function () {
            try {
                var pending = staging.dir.removeEntry(staging.name);
                if (pending && typeof pending.catch === "function") pending.catch(function () {});
            } catch (_) {}
        }, when == null ? 0 : when);
    }

    function abortSink(job) {
        var writer = job.writer;
        job.writer = null;
        if (writer) {
            try {
                var pending = writer.abort();
                if (pending && typeof pending.catch === "function") pending.catch(function () {});
            } catch (_) {}
        }
        dropStaging(job, 1500);
    }

    function clearStall(job) {
        if (!job || !job.stallTimer) return;
        clearTimeout(job.stallTimer);
        job.stallTimer = null;
    }

    /* Safari and Firefox have no save picker, but they do have origin-private
       file storage. Streaming there keeps the progress card honest without
       holding a 1.5 GB ZIP in memory; the finished file is handed to the
       browser only when it is whole. */
    function openStaging(job) {
        var storage = global.navigator && global.navigator.storage;
        if (!storage || typeof storage.getDirectory !== "function") {
            return Promise.resolve({ writer: null });
        }
        var dir = null;
        var name = "download-" + job.id + "-" + Date.now() + ".part";
        return storage.getDirectory().then(function (root) {
            return root.getDirectoryHandle("innioasis-downloads", { create: true });
        }).then(function (directory) {
            dir = directory;
            return directory.getFileHandle(name, { create: true });
        }).then(function (handle) {
            return handle.createWritable().then(function (writer) {
                job.staging = { dir: dir, name: name, handle: handle };
                job.writer = writer;
                return { writer: writer };
            });
        }).catch(function () {
            if (dir) {
                try {
                    var pending = dir.removeEntry(name);
                    if (pending && typeof pending.catch === "function") pending.catch(function () {});
                } catch (_) {}
            }
            return { writer: null };
        });
    }

    /* The picker must be opened synchronously from the click: Chromium only
       grants a writable while the reader's gesture is live. If the browser
       cannot provide one, stage the bytes privately and save the finished
       file instead of abandoning the transfer to the download shelf. */
    function openSink(job) {
        /* App installers and drivers are the mission-critical downloads. They
           stage privately instead of opening a save picker first, so a broken
           proxy falls straight through to one direct browser download rather
           than making the reader dismiss a picker for a transfer that fails. */
        if (APP_DOWNLOAD_URL.test(String(job.url || "")) || APP_DOWNLOAD_URL.test(String(job.directUrl || ""))) {
            return openStaging(job);
        }
        if (typeof global.showSaveFilePicker !== "function") return openStaging(job);
        var extension = "." + ((String(job.name || "download.bin").split(".").pop() || "bin").toLowerCase());
        try {
            return global.showSaveFilePicker({
                suggestedName: job.name,
                types: [{ description: "Download", accept: { "application/octet-stream": [extension] } }]
            }).then(function (handle) {
                return handle.createWritable();
            }).then(function (writer) {
                job.writer = writer;
                return { writer: writer };
            }).catch(function (error) {
                if (error && error.name === "AbortError") return { cancelled: true };
                return openStaging(job);
            });
        } catch (_) {
            return openStaging(job);
        }
    }

    async function start(job, source) {
        try {
            await runJob(job, source);
        } catch (_) {
            if (!job.cancelled) failJob(job);
        }
    }

    async function runJob(job, source) {
        job.status = "starting";
        paint(job);

        var controller = typeof AbortController === "function" ? new AbortController() : null;
        job.controller = controller;

        /* Open the picker before awaiting anything; the resolver runs while the
           dialog is up, so choosing a folder costs no transfer time. */
        var sink = await openSink(job);
        if (sink.cancelled) {
            cancelJob(job);
            return;
        }
        var writer = sink.writer;
        if (job.cancelled) {
            abortSink(job);
            return;
        }

        var resolved = source;
        if (typeof source === "function") {
            try { resolved = await source(); }
            catch (_) { resolved = null; }
        }
        if (job.cancelled) {
            abortSink(job);
            return;
        }
        if (resolved && typeof resolved === "object") {
            if (resolved.cancel) { cancelJob(job); return; }
            /* A resolver returns the release's own asset name; it is already
               the filename the reader should get. */
            if (resolved.name) job.name = resolved.name;
            resolved = resolved.url || "";
        }
        var targetUrl = String(resolved || job.url || "");
        if (!targetUrl) {
            abortSink(job);
            failJob(job);
            return;
        }
        job.url = targetUrl;
        job.directUrl = targetUrl;
        var requestUrl = proxiedUrl(targetUrl, job.name);

        /* A proxy that never answers should not hold the reader in the card.
           After the timeout the direct asset URL is handed to the browser. */
        var connectTimer = setTimeout(function () {
            if (job.controller) {
                try { job.controller.abort(); } catch (_) {}
            }
        }, 20000);
        var response;
        try {
            response = await fetch(requestUrl, {
                mode: "cors",
                credentials: "omit",
                redirect: "follow",
                signal: controller ? controller.signal : undefined
            });
        } catch (error) {
            if (job.cancelled) return;
            abortSink(job);
            failJob(job);
            return;
        } finally {
            clearTimeout(connectTimer);
        }
        if (!response || !response.ok) {
            abortSink(job);
            failJob(job);
            return;
        }

        /* The response knows the real name: the proxy answers with
           Content-Disposition, and a portable build resolves to its mother
           package (rom_y1-windows.zip saves as rom_y1.zip). */
        var headerName = headerFileName(response);
        job.name = APP_DOWNLOAD_URL.test(targetUrl)
            ? (headerName || job.name || "download.bin")
            : motherName(headerName || job.name || "download.bin");
        var length = Number(response.headers.get("content-length") || 0);
        job.total = Number.isFinite(length) && length > 0 ? length : 0;
        job.status = "running";
        paint(job);

        var chunks = writer ? null : [];
        var reader = null;
        try {
            reader = response.body && typeof response.body.getReader === "function" ? response.body.getReader() : null;
        } catch (_) {
            reader = null;
        }
        if (!reader) {
            abortSink(job);
            failJob(job);
            return;
        }

        /* A truncated proxy stream can leave read() pending forever. Abort
           after a minute without bytes so the browser fallback can start. */
        var armStall = function () {
            clearStall(job);
            job.stallTimer = setTimeout(function () {
                if (job.controller) {
                    try { job.controller.abort(); } catch (_) {}
                }
            }, 60000);
        };
        armStall();

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
                armStall();
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
                    abortSink(job);
                    return;
                }
            }
            clearStall(job);
        } catch (error) {
            clearStall(job);
            abortSink(job);
            if (job.cancelled) return;
            failJob(job);
            return;
        }

        if (!job.total) job.total = job.loaded;
        if (writer) {
            try { await writer.close(); }
            catch (_) {
                abortSink(job);
                failJob(job);
                return;
            }
            job.writer = null;
            if (job.staging) {
                try {
                    var saved = await job.staging.handle.getFile();
                    saveBlob(saved, job.name);
                    dropStaging(job, 120000);
                } catch (_) {
                    dropStaging(job, 0);
                    failJob(job);
                    return;
                }
            }
        } else {
            saveBlob(new Blob(chunks, { type: response.headers.get("content-type") || "application/octet-stream" }), job.name);
        }
        job.status = "done";
        paint(job);
        finish(job);
    }

    /* ------------------------------------------------------- release assets

       A "releases/latest/download/installer.exe" link only works while the
       newest release happens to carry that exact file. The app and driver
       repositories publish staggered releases, so the newest one can omit a
       platform build that an older release still has. Before the transfer
       starts, the release list is read and the newest release carrying the
       requested kind of asset wins; when no release names it, the newest
       release's closest file is used, and the original link is the last
       resort. */
    var releaseListCache = {};

    function releaseRepo(url) {
        var match = String(url || "").match(/^https:\/\/github\.com\/([^/]+)\/([^/]+)\/releases\/latest\/download\//i);
        if (!match) return "";
        var repo = match[1] + "/" + match[2];
        return RELEASE_RESOLVED_REPO.test(repo) ? repo : "";
    }

    function releaseOrderKey(release) {
        var tag = String((release && release.tag_name) || "");
        var stamp = 0;
        var match = tag.match(/(^|[^0-9])((?:19|20)\d{2})(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(?:[-_.]?(\d{2})(\d{2}))?(?!\d)/);
        if (match) {
            var year = Number(match[2]);
            var month = Number(match[3]);
            var day = Number(match[4]);
            var value = Date.UTC(year, month - 1, day, Number(match[5] || 0), Number(match[6] || 0));
            var check = new Date(value);
            if (check.getUTCFullYear() === year && check.getUTCMonth() === month - 1 && check.getUTCDate() === day) stamp = value;
        }
        var semver = [];
        if (!stamp) {
            var version = tag.match(/(?:^|[^0-9A-Za-z])v?(\d+(?:\.\d+)+)(?![0-9A-Za-z])/i);
            if (version) semver = version[1].split(".").map(Number);
        }
        return [stamp || semver.length ? 1 : 0, stamp, semver,
            Date.parse((release && release.published_at) || "") || 0, tag.toLowerCase()];
    }

    function compareReleaseOrder(a, b) {
        for (var index = 0; index < 4; index += 1) {
            var left = a[index];
            var right = b[index];
            if (Array.isArray(left) && Array.isArray(right)) {
                var length = Math.max(left.length, right.length);
                for (var part = 0; part < length; part += 1) {
                    var l = part < left.length ? left[part] : 0;
                    var r = part < right.length ? right[part] : 0;
                    if (l !== r) return l - r;
                }
            } else if (left !== right) {
                return left - right;
            }
        }
        return a[4].localeCompare(b[4]);
    }

    function newestReleases(list) {
        return (list || []).slice().sort(function (a, b) {
            return compareReleaseOrder(releaseOrderKey(b), releaseOrderKey(a));
        });
    }

    function assetExtension(name) {
        var lower = String(name || "").toLowerCase();
        if (/\.tar\.gz$/.test(lower)) return ".tar.gz";
        if (/\.tar\.xz$/.test(lower)) return ".tar.xz";
        var match = lower.match(/(\.[a-z0-9]+)$/);
        return match ? match[1] : "";
    }

    /* How well an asset in a release answers the link the reader pressed.
       Exact name wins; otherwise the extension names the platform for an
       installer or app image, while an archive has to name it. */
    function assetMatch(name, wantedName) {
        var lower = String(name || "").toLowerCase();
        var wanted = String(wantedName || "").toLowerCase();
        var extension = assetExtension(wanted);
        if (!extension || assetExtension(lower) !== extension) return -1;
        if (/source|sha256|checksum|licen[cs]e|legal/i.test(lower)) return -1;
        if (lower === wanted) return 1000;
        var archive = /\.(zip|7z|tar\.gz|tgz|tar\.xz|txz|tar\.bz2|tbz2)$/.test(lower);
        var score = archive ? 100 : 300;
        if (archive) {
            var tokens = [];
            if (/mac|osx|darwin/.test(wanted)) tokens = ["mac", "osx", "darwin"];
            else if (/linux/.test(wanted)) tokens = ["linux"];
            else if (/win/.test(wanted)) tokens = ["win"];
            if (tokens.length) {
                score += tokens.some(function (token) { return lower.indexOf(token) !== -1; }) ? 200 : -150;
            }
        }
        var arm = wanted.indexOf("arm64") !== -1 || wanted.indexOf("aarch64") !== -1;
        if (arm) score += /arm64|aarch64/.test(lower) ? 100 : -400;
        return score;
    }

    function releaseAssetFor(releases, wantedName) {
        var list = newestReleases((releases || []).filter(function (release) {
            return release && !release.draft;
        }));
        for (var index = 0; index < list.length; index += 1) {
            var chosen = null;
            var score = 249;
            (list[index].assets || []).forEach(function (asset) {
                var value = assetMatch(asset.name, wantedName);
                if (value > score) { score = value; chosen = asset; }
            });
            if (chosen) return chosen;
        }
        if (list.length) {
            var fallback = null;
            var best = 0;
            (list[0].assets || []).forEach(function (asset) {
                var value = assetMatch(asset.name, wantedName);
                if (value > best) { best = value; fallback = asset; }
            });
            if (fallback) return fallback;
        }
        return null;
    }

    function releaseList(repo) {
        var key = repo.toLowerCase();
        if (releaseListCache[key]) return releaseListCache[key];
        releaseListCache[key] = fetch("https://api.github.com/repos/" + repo + "/releases?per_page=100", {
            mode: "cors",
            credentials: "omit",
            cache: "no-store",
            headers: { Accept: "application/vnd.github+json" }
        }).then(function (response) {
            if (!response.ok) throw new Error("release list");
            return response.json();
        }).catch(function () {
            delete releaseListCache[key];
            return [];
        });
        return releaseListCache[key];
    }

    function releaseResolver(url) {
        var repo = releaseRepo(url);
        var wanted = fileNameOf(url);
        if (!repo || !wanted) return null;
        return function () {
            return releaseList(repo).then(function (releases) {
                var asset = releaseAssetFor(releases, wanted);
                return asset ? { url: asset.browser_download_url, name: asset.name } : null;
            });
        };
    }

    function queue(url, anchor, name, resolver) {
        injectStyles();
        if (anchor && jobByAnchor && jobByAnchor.get(anchor)) return true;
        var saveName = APP_DOWNLOAD_URL.test(String(url || ""))
            ? (name || fileNameOf(url) || "download.bin")
            : motherName(name || fileNameOf(url) || "download.bin");
        var job = {
            id: ++seq,
            url: url,
            name: saveName,
            anchor: anchor || null,
            resolver: resolver || null,
            status: "starting",
            loaded: 0,
            total: 0,
            lastSpeed: 0,
            samples: [],
            dismissed: false,
            cancelled: false,
            writer: null,
            staging: null,
            directUrl: url,
            fallbackStarted: false,
            stallTimer: null,
            panel: null,
            group: null,
            container: null
        };
        jobs.push(job);
        if (anchor && jobByAnchor) jobByAnchor.set(anchor, job);
        mount(job, anchor || null);
        paint(job);
        if (job.panel) {
            setTimeout(function () { placePanel(job); }, 60);
        }
        start(job, resolver || url);
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
        /* Phone packages and disk images still belong to the browser. */
        if (NEVER_STREAM.test(href)) return false;
        /* A rendered document names the package it links to. When that name is
           an archive, the link is a package download even if the asset URL
           carries no extension of its own. */
        var declared = link.getAttribute("data-save-as") || link.getAttribute("data-download-name") || "";
        if (NEVER_STREAM.test(declared)) return false;
        var explicit = link.hasAttribute("data-inpage-download") || STREAMABLE.test(declared);
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
        /* The firmware catalog owns these: it resolves the mirror's package
           for this computer before starting the transfer. Claiming the link
           here would fetch the release's own rom.zip instead. */
        if (link.closest("[data-portable-zips]")) return;
        if (link.target && link.target !== "_self") return;
        var href = link.href || link.getAttribute("href");
        if (/^(blob|data):/i.test(href)) return;
        /* A Download inside the download-figures breakdown is a page download
           too. Close the overlay before asking for the save picker, and put
           the card under the control that opened the breakdown; its link is
           removed with the modal. */
        var anchor = link;
        if (link.closest && link.closest(".dl-stats-overlay")) {
            var stats = global.InnioasisDownloadStats;
            if (stats && typeof stats.dismissForDownload === "function") {
                try { anchor = stats.dismissForDownload() || null; } catch (_) { anchor = null; }
            }
        }
        /* data-save-as is what a rendered document uses to name the package
           it links to; it outranks the asset's own filename. */
        var started = queue(href, anchor,
            link.getAttribute("data-download-name") ||
            link.getAttribute("data-save-as") ||
            link.getAttribute("download") ||
            "", releaseResolver(href));
        if (started === false) return;
        /* A stale copy of docs-viewer.js also claims this click and would
           fetch a second copy. It skips a link marked busy, so the mark is
           what keeps one click to one transfer whichever copy is cached. */
        link.setAttribute("data-save-busy", "1");
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

        /* Keep the card beside its link while the reader scrolls or turns the
           phone; the page itself is never blocked from unloading. */
        global.addEventListener("scroll", function () {
            jobs.forEach(reposition);
        }, { passive: true });
        global.addEventListener("resize", function () {
            jobs.forEach(reposition);
        });
    }

    global.InnioasisDownloads = {
        version: VERSION,
        start: function (url, anchor, name) { return queue(url, anchor, name); },
        /* Resolve a portable package after the picker has been opened on the
           click. The resolver returns {url, name} or {cancel:true}. */
        startResolved: function (resolver, fallbackUrl, anchor, name) {
            return queue(fallbackUrl || "", anchor, name || "", resolver);
        },
        jobs: function () { return jobs.slice(); },
        /* Exposed so a page, a test or the firmware catalog can ask the same
           questions the click handler asks without starting a download. */
        name: motherName,
        proxy: proxiedUrl,
        /* Whether this module would stream a URL at all: archive packages yes,
           installers and app images never. Callers use this instead of
           repeating the rules and drifting from them. */
        eligible: function (url, name) {
            var href = String(url || "");
            var declared = String(name || "");
            if (NEVER_STREAM.test(href) || NEVER_STREAM.test(declared)) return false;
            return STREAMABLE.test(href) || STREAMABLE.test(declared);
        }
    };

    if (doc.readyState === "loading") doc.addEventListener("DOMContentLoaded", boot);
    else boot();
})(typeof window !== "undefined" ? window : globalThis);
