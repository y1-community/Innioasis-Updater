/* Windows on ARM64 compatibility guidance & download confirmation modal.
 *
 * macOS ARM64 (Apple Silicon) and Linux ARM64 are both supported by Updater CE,
 * but Windows on ARM64 PCs (for example Snapdragon or RTX Spark machines) do
 * not currently have a known working MediaTek USB flashing driver. Visitors on
 * Windows ARM64 can still open Updater CE and install Rockbox themes normally,
 * so rather than hard-blocking downloads we:
 *   1. Show a clear, friendly banner on Updater CE and firmware archive pages
 *      steering most visitors toward another computer (an Intel/AMD PC, Mac,
 *      or Linux machine — or installing ARM64 Linux on the same ARM64 PC).
 *   2. Show a confirmation modal whenever a Windows ARM64 visitor tries to
 *      download Updater CE (or Windows drivers / Windows portable firmware
 *      bundles), explaining that firmware installs won't work here (nor will
 *      SP Flash Tool or MTKClient) and confirming they still want to download
 *      to install Rockbox themes or experiment with Zadig / UsbDk and report
 *      back a working Windows ARM64 driver setup.
 *
 * Non-Windows-ARM64 visitors (Windows Intel/AMD, macOS Intel/Apple Silicon,
 * Linux x86_64/ARM64, phones/tablets) never see this banner or modal.
 */
(function (global) {
    "use strict";
    if (global.InnioasisWinArm64) return;

    var doc = global.document;
    if (!doc) return;

    var VERSION = "20261124arm64v1";
    var MODAL_ID = "win-arm64-confirm-modal";
    var BANNER_ATTR = "data-win-arm64-banner";
    var STYLE_ID = "site-win-arm64-styles";

    var APP_WIN_URL = /^https:\/\/github\.com\/[^/]+\/(?:innioasis-updater|supplemental-apks|updater-ce-neo)\/releases\/(?:latest\/)?download\/.*\.(?:exe|msi)(?:[?#]|$)/i;
    var ANY_WIN_EXE_URL = /(?:^|\/)(?:installer|DriverInstall|Innioasis[._-]?Updater[^/]*)\.(?:exe|msi)(?:[?#]|$)/i;
    var NON_WIN_URL = /\.(?:dmg|pkg|appimage|deb|rpm|tar\.gz|tgz)(?:[?#]|$)|UpdaterCE-Linux-Portable|Innioasis\.Updater\.for\.Mac/i;
    var ZADIG_URL = "https://zadig.akeo.ie/";
    var USBDK_URL = "https://github.com/daynix/UsbDk";
    var DISCORD_URL = "https://discord.gg/zHrT2zrcek";
    var ISSUES_URL = "https://github.com/y1-community/updater-ce-neo/issues";
    var ROCKBOX_THEMES_URL = "https://themes.innioasis.app/rockbox-themes.html";

    var state = {
        isWindowsArm64: false,
        source: ""
    };

    var pendingAction = null;
    var lastTrigger = null;

    function t(str) {
        if (!str) return "";
        try {
            if (global.InnioasisLocale && typeof global.InnioasisLocale.translate === "function") {
                var tr = global.InnioasisLocale.translate(str);
                if (tr) return tr;
            }
        } catch (_) {}
        return str;
    }

    function escapeHtml(str) {
        return String(str == null ? "" : str)
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;");
    }

    function siteRoot() {
        try {
            var scripts = doc.getElementsByTagName("script");
            for (var i = 0; i < scripts.length; i++) {
                var src = scripts[i].src || "";
                if (src.indexOf("site-windows-arm64.js") !== -1 || src.indexOf("site-init.js") !== -1) {
                    return src.replace(/[?#].*$/, "").replace(/[^/]*$/, "");
                }
            }
        } catch (_) {}
        return "";
    }

    function guideLinuxHref() {
        var path = String((global.location && global.location.pathname) || "");
        var m = /_([a-z]{2}(?:-[A-Za-z0-9]+)?)\.html$/i.exec(path);
        var qs = state.source === "query" ? "?win_arm64=1" : "";
        var file = m ? ("guide_" + m[1] + ".html" + qs + "#linux") : ("guide.html" + qs + "#linux");
        return siteRoot() + file;
    }

    function isLegacyWindows() {
        try {
            if (doc.documentElement && doc.documentElement.getAttribute("data-windows-legacy") === "true") return true;
            return Boolean(global.INNIOASIS_LEGACY && global.INNIOASIS_LEGACY.isLegacy);
        } catch (_) {
            return false;
        }
    }

    function hasPreviewParam() {
        try {
            var params = new URLSearchParams((global.location && global.location.search) || "");
            var flag = (params.get("win_arm64") || "").toLowerCase();
            if (flag === "1" || flag === "true") return true;
            if ((params.get("platform") || "").toLowerCase() === "windows-arm64") return true;
        } catch (_) {}
        return false;
    }

    function isWindowsDesktopUa(ua) {
        if (!/windows/i.test(ua)) return false;
        if (/windows phone|iemobile|mobile|android|iphone|ipad|ipod|macintosh|mac os x|linux|cros|chrome os/i.test(ua)) return false;
        return true;
    }

    function detectSync() {
        if (hasPreviewParam()) return { isWindowsArm64: true, source: "query" };
        if (global.INNIOASIS_WIN_ARM64 && global.INNIOASIS_WIN_ARM64.isWindowsArm64) {
            return {
                isWindowsArm64: true,
                source: String(global.INNIOASIS_WIN_ARM64.source || "init")
            };
        }
        if (isLegacyWindows()) return { isWindowsArm64: false, source: "" };
        var nav = global.navigator || {};
        var ua = String(nav.userAgent || "");
        if (!isWindowsDesktopUa(ua)) return { isWindowsArm64: false, source: "" };
        var plat = String((nav.userAgentData && nav.userAgentData.platform) || nav.platform || "");
        if (/mac|linux|android|cros|ios|iphone|ipad/i.test(plat)) return { isWindowsArm64: false, source: "" };
        if (/\b(?:arm64|aarch64|woa64)\b|windows\s+on\s+arm/i.test(ua + " " + plat)) {
            return { isWindowsArm64: true, source: "ua" };
        }
        return { isWindowsArm64: false, source: "" };
    }

    function publish(next) {
        var changed = Boolean(next.isWindowsArm64) !== Boolean(state.isWindowsArm64);
        state.isWindowsArm64 = Boolean(next.isWindowsArm64);
        state.source = next.source || "";
        global.INNIOASIS_WIN_ARM64 = {
            isWindowsArm64: state.isWindowsArm64,
            source: state.source
        };
        if (state.isWindowsArm64 && doc.documentElement) {
            doc.documentElement.setAttribute("data-windows-arm64", "true");
        }
        if (changed) {
            try {
                global.dispatchEvent(new CustomEvent("innioasis-win-arm64-change", {
                    detail: { isWindowsArm64: state.isWindowsArm64, source: state.source }
                }));
            } catch (_) {}
        }
    }

    /* Chromium browsers on Windows 11 ARM64 freeze navigator.userAgent to
       "Win64; x64" and only reveal the ARM processor through User-Agent
       Client Hints. Strictly verify platform === Windows so macOS Apple
       Silicon and ARM64 Linux are never matched. */
    function probeClientHints() {
        if (state.isWindowsArm64 || isLegacyWindows()) return;
        var nav = global.navigator || {};
        var ua = String(nav.userAgent || "");
        if (!isWindowsDesktopUa(ua)) return;
        var uad = nav.userAgentData;
        if (!uad || typeof uad.getHighEntropyValues !== "function") return;
        try {
            uad.getHighEntropyValues(["architecture", "bitness", "platform"]).then(function (hints) {
                if (!hints || isLegacyWindows()) return;
                var hintPlatform = String(hints.platform || uad.platform || "");
                if (!/win/i.test(hintPlatform) || /mac|linux|android|cros|ios/i.test(hintPlatform)) return;
                var arch = String(hints.architecture || "").toLowerCase();
                if (arch === "arm" || arch === "arm64" || arch === "aarch64") {
                    publish({ isWindowsArm64: true, source: "uach" });
                    activatePageUi();
                }
            }).catch(function () {});
        } catch (_) {}
    }

    function injectStyles() {
        if (doc.getElementById(STYLE_ID)) return;
        var style = doc.createElement("style");
        style.id = STYLE_ID;
        style.textContent = [
            ".win-arm64-banner{margin:1.15rem 0 1.4rem;padding:1.15rem 1.25rem;border-radius:var(--lumen-radius-md,14px);background:var(--lumen-panel,#0f1621);border:1px solid color-mix(in oklab,var(--lumen-amber,#e8c56a) 55%,var(--lumen-line-strong,#2b394d));box-shadow:0 10px 28px color-mix(in oklab,var(--lumen-ink,#04070e) 24%,transparent);color:var(--lumen-text,#e8edf2);}",
            ".win-arm64-banner__kicker{margin:0 0 .35rem;font-size:.76rem;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--lumen-amber,#e8c56a);}",
            ":root[data-theme=\"light\"] .win-arm64-banner__kicker,:root[data-lumen-theme=\"light\"] .win-arm64-banner__kicker{color:#8a5a00;}",
            ".win-arm64-banner__heading{margin:0 0 .5rem;font-size:1.15rem;line-height:1.3;font-weight:700;color:var(--lumen-text,#e8edf2);}",
            ".win-arm64-banner__p{margin:.45rem 0;font-size:.94rem;line-height:1.58;color:var(--lumen-muted,#b4bfca);}",
            ".win-arm64-banner__p strong{color:var(--lumen-text,#e8edf2);}",
            ".win-arm64-banner__actions{display:flex;flex-wrap:wrap;gap:.55rem;margin-top:.85rem;}",
            ".win-arm64-inline-note{margin:.65rem 0 .85rem;padding:.75rem .9rem;border-radius:var(--lumen-radius-sm,10px);background:var(--lumen-panel-soft,#17202d);border:1px solid color-mix(in oklab,var(--lumen-amber,#e8c56a) 45%,var(--lumen-line,#233042));font-size:.88rem;line-height:1.5;color:var(--lumen-muted,#b4bfca);}",
            ".win-arm64-inline-note strong{color:var(--lumen-text,#e8edf2);}",
            ".win-arm64-modal{position:fixed;inset:0;z-index:1100;display:grid;place-items:center;padding:1rem;background:color-mix(in oklab,var(--lumen-ink,#04070e) 68%,transparent);-webkit-backdrop-filter:blur(4px);backdrop-filter:blur(4px);}",
            ".win-arm64-modal[hidden]{display:none;}",
            ".win-arm64-modal__card{max-width:36rem;width:100%;max-height:calc(100dvh - 2rem);overflow-y:auto;background:var(--lumen-panel,#0f1621);border:1px solid var(--lumen-line-strong,#2b394d);border-radius:var(--lumen-radius-md,14px);padding:1.35rem 1.4rem;color:var(--lumen-text,#e8edf2);box-shadow:0 22px 60px color-mix(in oklab,var(--lumen-ink,#04070e) 50%,transparent);}",
            ".win-arm64-modal__head{display:flex;align-items:flex-start;justify-content:space-between;gap:.75rem;margin-bottom:.5rem;}",
            ".win-arm64-modal__kicker{margin:0 0 .25rem;font-size:.75rem;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--lumen-amber,#e8c56a);}",
            ":root[data-theme=\"light\"] .win-arm64-modal__kicker,:root[data-lumen-theme=\"light\"] .win-arm64-modal__kicker{color:#8a5a00;}",
            ".win-arm64-modal__title{margin:0;font-size:1.18rem;line-height:1.3;font-weight:700;color:var(--lumen-text,#e8edf2);}",
            ".win-arm64-modal__x{flex:0 0 auto;min-width:2rem;min-height:2rem;border-radius:8px;border:1px solid var(--lumen-line-strong,#2b394d);background:var(--lumen-panel-soft,#17202d);color:var(--lumen-text,#e8edf2);font:700 1.05rem/1 system-ui,sans-serif;cursor:pointer;}",
            ".win-arm64-modal__x:hover,.win-arm64-modal__x:focus-visible{border-color:var(--lumen-accent,#6fb8f5);outline:none;}",
            ".win-arm64-modal__body{margin:.5rem 0;font-size:.93rem;line-height:1.58;color:var(--lumen-muted,#b4bfca);}",
            ".win-arm64-modal__body strong{color:var(--lumen-text,#e8edf2);}",
            ".win-arm64-modal__callout{margin:.8rem 0;padding:.85rem 1rem;border-radius:var(--lumen-radius-sm,10px);background:var(--lumen-panel-soft,#17202d);border-left:3px solid var(--lumen-amber,#e8c56a);font-size:.91rem;line-height:1.55;color:var(--lumen-text,#e8edf2);}",
            ".win-arm64-modal__callout p{margin:0;}",
            ".win-arm64-modal__callout p+p{margin-top:.45rem;color:var(--lumen-muted,#b4bfca);}",
            ".win-arm64-modal__list{margin:.65rem 0 .85rem;padding-left:1.2rem;display:grid;gap:.48rem;font-size:.9rem;line-height:1.55;color:var(--lumen-muted,#b4bfca);}",
            ".win-arm64-modal__list strong{color:var(--lumen-text,#e8edf2);}",
            ".win-arm64-modal__list a{color:var(--lumen-accent,#6fb8f5);text-decoration:underline;text-underline-offset:.16em;}",
            ".win-arm64-modal__actions{display:grid;gap:.55rem;margin-top:1rem;}",
            ".win-arm64-modal__row{display:flex;flex-wrap:wrap;gap:.55rem;}",
            ".win-arm64-modal__row>*{flex:1 1 12rem;}",
            ".win-arm64-modal__primary{display:inline-flex;align-items:center;justify-content:center;padding:.65rem 1rem;border-radius:999px;border:1px solid var(--lumen-accent,#6fb8f5);background:var(--lumen-accent,#6fb8f5);color:var(--lumen-on-accent,var(--lumen-ink,#04070e));font:700 .92rem/1.3 var(--lumen-body,system-ui,sans-serif);text-decoration:none;cursor:pointer;}",
            ".win-arm64-modal__primary:hover,.win-arm64-modal__primary:focus-visible{background:var(--lumen-accent-strong,#8bcaf9);border-color:var(--lumen-accent-strong,#8bcaf9);color:var(--lumen-on-accent-strong,var(--lumen-on-accent,var(--lumen-ink,#04070e)));outline:2px solid var(--lumen-text,#fff);outline-offset:2px;}",
            ".win-arm64-modal__secondary{display:inline-flex;align-items:center;justify-content:center;padding:.62rem 1rem;border-radius:999px;border:1px solid var(--lumen-line-strong,#2b394d);background:var(--lumen-panel-soft,#17202d);color:var(--lumen-text,#e8edf2);font:600 .9rem/1.3 var(--lumen-body,system-ui,sans-serif);text-decoration:none;cursor:pointer;}",
            ".win-arm64-modal__secondary:hover,.win-arm64-modal__secondary:focus-visible{border-color:var(--lumen-accent,#6fb8f5);color:var(--lumen-text,#e8edf2);outline:2px solid var(--lumen-accent,#6fb8f5);outline-offset:2px;}",
            ".win-arm64-modal__proceed{display:inline-flex;align-items:center;justify-content:center;padding:.62rem 1rem;border-radius:999px;border:1px dashed var(--lumen-line-strong,#3b4c63);background:transparent;color:var(--lumen-muted,#b4bfca);font:600 .88rem/1.35 var(--lumen-body,system-ui,sans-serif);text-align:center;cursor:pointer;}",
            ".win-arm64-modal__proceed:hover,.win-arm64-modal__proceed:focus-visible{border-color:var(--lumen-accent,#6fb8f5);color:var(--lumen-text,#e8edf2);background:var(--lumen-panel-soft,#17202d);outline:2px solid var(--lumen-accent,#6fb8f5);outline-offset:2px;}"
        ].join("");
        (doc.head || doc.documentElement).appendChild(style);
    }

    function shouldShowPageBanner() {
        var path = String((global.location && global.location.pathname) || "").toLowerCase();
        if (doc.querySelector("[data-platform-detect]") || doc.querySelector("#lumen-firmware-table")) return true;
        if (/(?:^|\/)(?:index|firmware|firmware-list|firmware-guide|guide|drivers|installguide|updater-comparison|sp-flash-tool|troubleshooting|all_versions|release_notes|portable-builds)(?:_[a-z0-9-]+)?\.html$/i.test(path)) return true;
        if (/\/(?:install|guides|firmware-info)\//i.test(path)) return true;
        if (path === "/" || path === "") return true;
        return false;
    }

    function revealLinuxArm64() {
        var linuxCard = doc.getElementById("linux");
        if (linuxCard) {
            var group = linuxCard.closest("[data-platform-detect]");
            if (group) {
                group.classList.remove("lumen-download-options--single");
                Array.prototype.forEach.call(group.querySelectorAll(".lumen-download-option[data-platform]"), function (card) {
                    card.hidden = false;
                });
                var toggle = group.querySelector("[data-another-platform]");
                if (toggle) toggle.hidden = true;
            }
            linuxCard.hidden = false;
            var armBtn = linuxCard.querySelector('[data-linux-arch="arm64"]');
            if (armBtn) armBtn.hidden = false;
            var details = linuxCard.closest("details");
            if (details) details.open = true;
            linuxCard.scrollIntoView({ behavior: "smooth", block: "start" });
            return true;
        }
        global.location.href = guideLinuxHref();
        return false;
    }

    function bannerHtml() {
        var kicker = escapeHtml(t("Windows on ARM64 detected"));
        var heading = escapeHtml(t("We recommend using a different computer to install firmware"));
        var p1 = t("It looks like you're browsing from a Windows ARM64 computer (for example, a PC running a Snapdragon or RTX Spark processor). You can still install and open Updater CE here — and Rockbox theme installation works as normal — but there are currently no known working USB flashing drivers for Windows on ARM64, which means firmware installs and restores won't work on this PC.");
        var p2 = t("Trying a different Windows flashing app won't get around this either: SP Flash Tool and MTKClient are unlikely to work on a Windows ARM64 computer for the same reason. For firmware updates or restores, you'll really need to use another computer — like a standard Intel or AMD Windows PC, a Mac, or a Linux computer (macOS and Linux are both supported on ARM64).");
        var p3 = t("Staying on this ARM64 PC? It may be possible to install an ARM64 Linux distribution on this computer and run the supported ARM64 Linux version of Updater CE. If you'd like to experiment on Windows instead, you're free to try Zadig and USB Development Kit (UsbDk) to see if you can get a generic driver working and report back to the community.");
        var btnLinux = escapeHtml(t("See ARM64 Linux option"));
        var btnDetails = escapeHtml(t("Driver tips & details"));
        var btnThemes = escapeHtml(t("Browse Rockbox themes"));

        return '' +
            '<p class="win-arm64-banner__kicker">' + kicker + '</p>' +
            '<h2 class="win-arm64-banner__heading">' + heading + '</h2>' +
            '<p class="win-arm64-banner__p">' + escapeHtml(p1) + '</p>' +
            '<p class="win-arm64-banner__p"><strong>' + escapeHtml(t("Use another computer instead:")) + '</strong> ' + escapeHtml(p2) + '</p>' +
            '<p class="win-arm64-banner__p">' + escapeHtml(p3) + '</p>' +
            '<div class="win-arm64-banner__actions">' +
            '<button type="button" class="lumen-button lumen-button--primary" data-win-arm64-linux>' + btnLinux + '</button>' +
            '<button type="button" class="lumen-button" data-win-arm64-info>' + btnDetails + '</button>' +
            '<a class="lumen-button" href="' + ROCKBOX_THEMES_URL + '">' + btnThemes + '</a>' +
            '</div>';
    }

    function mountBanner() {
        if (!state.isWindowsArm64 || !shouldShowPageBanner()) return;
        var main = doc.querySelector("main") || doc.getElementById("main");
        if (!main) return;
        var existing = main.querySelector("[" + BANNER_ATTR + "]");
        if (!existing) {
            existing = doc.createElement("section");
            existing.className = "win-arm64-banner";
            existing.setAttribute(BANNER_ATTR, "1");
            existing.setAttribute("role", "region");
            existing.setAttribute("aria-label", t("Windows on ARM64 compatibility notice"));
            var anchor = main.querySelector("header, .lumen-hero");
            if (anchor && anchor.parentNode === main) {
                main.insertBefore(existing, anchor.nextSibling);
            } else {
                main.insertBefore(existing, main.firstChild);
            }
        }
        existing.innerHTML = bannerHtml();
        var linuxBtn = existing.querySelector("[data-win-arm64-linux]");
        if (linuxBtn) {
            linuxBtn.addEventListener("click", function () {
                revealLinuxArm64();
            });
        }
        var infoBtn = existing.querySelector("[data-win-arm64-info]");
        if (infoBtn) {
            infoBtn.addEventListener("click", function () {
                openModal({ infoOnly: true, trigger: infoBtn });
            });
        }
    }

    function mountWindowsCardNote() {
        if (!state.isWindowsArm64) return;
        Array.prototype.forEach.call(doc.querySelectorAll('[data-platform-detect] [data-platform="windows"]'), function (card) {
            var note = card.querySelector("[data-win-arm64-inline]");
            if (!note) {
                note = doc.createElement("div");
                note.className = "win-arm64-inline-note";
                note.setAttribute("data-win-arm64-inline", "1");
                var actions = card.querySelector(".lumen-actions");
                if (actions && actions.parentNode === card) {
                    card.insertBefore(note, actions);
                } else {
                    card.appendChild(note);
                }
            }
            note.innerHTML =
                '<strong>' + escapeHtml(t("Windows on ARM64:")) + '</strong> ' +
                escapeHtml(t("You can install Updater CE for Rockbox themes or driver testing, but firmware installs won't work on this PC because there are no known ARM64 Windows flashing drivers (SP Flash Tool and MTKClient are unlikely to work either). We recommend using an Intel/AMD PC, a Mac, or Linux — including installing ARM64 Linux on this PC."));
        });
    }

    function ensureAllPlatformsVisible() {
        if (!state.isWindowsArm64) return;
        Array.prototype.forEach.call(doc.querySelectorAll("[data-platform-detect]"), function (group) {
            group.classList.remove("lumen-download-options--single");
            Array.prototype.forEach.call(group.querySelectorAll(".lumen-download-option[data-platform]"), function (card) {
                card.hidden = false;
            });
            var toggle = group.querySelector("[data-another-platform]");
            if (toggle) toggle.hidden = true;
            var otherBtn = group.nextElementSibling;
            if (otherBtn && otherBtn.classList && otherBtn.classList.contains("lumen-other-downloads")) {
                otherBtn.hidden = true;
            }
            var armLinux = group.querySelector('[data-linux-arch="arm64"]');
            if (armLinux) armLinux.hidden = false;
        });
    }

    function ensureModal() {
        var modal = doc.getElementById(MODAL_ID);
        if (modal) return modal;
        modal = doc.createElement("div");
        modal.id = MODAL_ID;
        modal.className = "win-arm64-modal";
        modal.hidden = true;
        modal.setAttribute("aria-hidden", "true");
        modal.setAttribute("role", "dialog");
        modal.setAttribute("aria-modal", "true");
        modal.setAttribute("aria-labelledby", "win-arm64-modal-title");
        doc.body.appendChild(modal);
        modal.addEventListener("click", function (event) {
            if (event.target === modal) closeModal();
        });
        doc.addEventListener("keydown", function (event) {
            if (event.key === "Escape" && !modal.hidden) closeModal();
        });
        return modal;
    }

    function renderModal(modal, opts) {
        var infoOnly = Boolean(opts && opts.infoOnly);
        var fileName = (opts && opts.fileName) ? String(opts.fileName) : "";

        var kicker = escapeHtml(t(infoOnly ? "Windows on ARM64 compatibility" : "Windows on ARM64 · Before you download"));
        var title = escapeHtml(t("Firmware installs won't work on this Windows ARM64 PC"));
        var intro = t("It looks like you're on a Windows ARM64 computer (for example, one with a Snapdragon or RTX Spark processor). You can install and open Updater CE here, and Rockbox theme installation will work as normal — however, there are currently no known working USB flashing drivers for Windows on ARM64, which means firmware installs won't work on this PC.");
        var steerLead = t("Please use a different computer for firmware updates or restores.");
        var steerDetail = t("Switching to another Windows flashing app won't solve this — SP Flash Tool and MTKClient are unlikely to work on a Windows ARM64 computer either. You'll really need another computer such as an Intel or AMD Windows PC, a Mac, or a Linux PC (both macOS and Linux are supported on ARM64).");
        var linuxHeading = t("Option 1 — Run ARM64 Linux on this PC:");
        var linuxBody = t("It may be possible to install an ARM64 Linux distribution on this same ARM64 computer so you can run the supported ARM64 Linux version of Updater CE.");
        var driverHeading = t("Option 2 — Experiment with generic drivers (advanced):");
        var driverIntro = t("If you still want to download Updater CE to experiment, you're free to try");
        var driverMid = t("and");
        var driverOutro = t("to see if you can get a generic USB driver working on Windows ARM64. If you find a working driver setup method, please report back on");
        var driverOr = t("or");
        var driverEnd = t("so other Windows ARM64 users can benefit.");
        var closeLabel = escapeHtml(t(infoOnly ? "Got it, close" : "I'll use another computer"));
        var linuxBtnLabel = escapeHtml(t("See ARM64 Linux version"));
        var proceedText = fileName
            ? (t("Yes, still download") + " " + fileName + " (" + t("Rockbox themes or driver testing") + ")")
            : t("Yes, still download Updater CE (Rockbox themes or driver testing)");

        modal.innerHTML = '' +
            '<div class="win-arm64-modal__card">' +
            '  <div class="win-arm64-modal__head">' +
            '    <div>' +
            '      <p class="win-arm64-modal__kicker">' + kicker + '</p>' +
            '      <h3 id="win-arm64-modal-title" class="win-arm64-modal__title">' + title + '</h3>' +
            '    </div>' +
            '    <button type="button" class="win-arm64-modal__x" data-win-arm64-close aria-label="' + escapeHtml(t("Close")) + '">&times;</button>' +
            '  </div>' +
            '  <p class="win-arm64-modal__body">' + escapeHtml(intro) + '</p>' +
            '  <div class="win-arm64-modal__callout">' +
            '    <p><strong>' + escapeHtml(steerLead) + '</strong></p>' +
            '    <p>' + escapeHtml(steerDetail) + '</p>' +
            '  </div>' +
            '  <ul class="win-arm64-modal__list">' +
            '    <li><strong>' + escapeHtml(linuxHeading) + '</strong> ' + escapeHtml(linuxBody) + '</li>' +
            '    <li><strong>' + escapeHtml(driverHeading) + '</strong> ' +
                 escapeHtml(driverIntro) + ' ' +
                 '<a href="' + ZADIG_URL + '" target="_blank" rel="noopener noreferrer" translate="no" data-i18n-skip>Zadig</a> ' +
                 escapeHtml(driverMid) + ' ' +
                 '<a href="' + USBDK_URL + '" target="_blank" rel="noopener noreferrer" translate="no" data-i18n-skip>USB Development Kit (UsbDk)</a> ' +
                 escapeHtml(driverOutro) + ' ' +
                 '<a href="' + DISCORD_URL + '" target="_blank" rel="noopener noreferrer" translate="no" data-i18n-skip>Discord</a> ' +
                 escapeHtml(driverOr) + ' ' +
                 '<a href="' + ISSUES_URL + '" target="_blank" rel="noopener noreferrer" translate="no" data-i18n-skip>GitHub</a> ' +
                 escapeHtml(driverEnd) +
            '    </li>' +
            '  </ul>' +
            '  <div class="win-arm64-modal__actions">' +
            '    <div class="win-arm64-modal__row">' +
            '      <button type="button" class="win-arm64-modal__primary" data-win-arm64-close>' + closeLabel + '</button>' +
            '      <button type="button" class="win-arm64-modal__secondary" data-win-arm64-linux>' + linuxBtnLabel + '</button>' +
            '    </div>' +
                 (infoOnly ? '' : '<button type="button" class="win-arm64-modal__proceed" data-win-arm64-proceed>' + escapeHtml(proceedText) + '</button>') +
            '  </div>' +
            '</div>';

        Array.prototype.forEach.call(modal.querySelectorAll("[data-win-arm64-close]"), function (btn) {
            btn.addEventListener("click", closeModal);
        });
        var linuxBtn = modal.querySelector("[data-win-arm64-linux]");
        if (linuxBtn) {
            linuxBtn.addEventListener("click", function () {
                closeModal();
                revealLinuxArm64();
            });
        }
        var proceedBtn = modal.querySelector("[data-win-arm64-proceed]");
        if (proceedBtn) {
            proceedBtn.addEventListener("click", function () {
                var action = pendingAction;
                pendingAction = null;
                closeModal();
                if (typeof action === "function") action();
            });
        }
    }

    function openModal(opts) {
        injectStyles();
        var modal = ensureModal();
        pendingAction = (opts && typeof opts.onProceed === "function") ? opts.onProceed : null;
        lastTrigger = (opts && opts.trigger) || doc.activeElement || null;
        renderModal(modal, opts || {});
        modal.hidden = false;
        modal.setAttribute("aria-hidden", "false");
        var primary = modal.querySelector(".win-arm64-modal__primary");
        if (primary) {
            try { primary.focus(); } catch (_) {}
        }
    }

    function closeModal() {
        var modal = doc.getElementById(MODAL_ID);
        if (!modal) return;
        modal.hidden = true;
        modal.setAttribute("aria-hidden", "true");
        pendingAction = null;
        if (lastTrigger && typeof lastTrigger.focus === "function") {
            try { lastTrigger.focus(); } catch (_) {}
        }
        lastTrigger = null;
    }

    function linkTargetOf(node) {
        if (!node || !node.closest) return null;
        return node.closest("a[href], a[data-zip-url], button[data-zip-url], .lumen-zip-download-button");
    }

    function isWindowsUpdaterDownload(el) {
        if (!el || !el.getAttribute) return false;
        if (el.closest && el.closest("#" + MODAL_ID)) return false;
        if (el.hasAttribute("data-win-arm64-confirmed")) return false;
        if (el.hasAttribute("data-site-download-direct")) return false;

        var href = String(el.getAttribute("href") || "");
        var zipUrl = String(el.getAttribute("data-zip-url") || "");
        var explicitPlatform = String(el.getAttribute("data-platform") || "").toLowerCase();

        /* Never intercept explicit macOS or Linux downloads — Windows ARM64
           visitors may intentionally grab an ARM64 Linux or Mac build. */
        if (explicitPlatform === "macos" || explicitPlatform === "linux" || explicitPlatform === "linux-arm64" || explicitPlatform === "linux-legacy") {
            return false;
        }
        if (NON_WIN_URL.test(href)) return false;
        if (el.closest && el.closest('[data-platform="macos"], [data-platform="linux"]')) return false;

        /* 1. Direct Windows Updater CE / MediaTek driver installers */
        if (APP_WIN_URL.test(href) || ANY_WIN_EXE_URL.test(href)) return true;

        /* 2. Download links inside the Windows card */
        if (el.hasAttribute("download") && el.closest && el.closest('[data-platform="windows"]')) return true;

        /* 3. Portable Windows firmware installer bundles on the Firmware Archive
              (on Windows ARM64 these resolve to a Windows Updater CE bundle). */
        if (zipUrl && /\.zip(?:[?#]|$)/i.test(zipUrl)) return true;
        if (el.classList && (el.classList.contains("lumen-zip-download-button") || el.classList.contains("lumen-zip-text-link"))) return true;

        return false;
    }

    function fileNameFor(el) {
        var declared = el.getAttribute("data-zip-name") || el.getAttribute("data-download-name") || el.getAttribute("data-save-as") || el.getAttribute("download") || "";
        if (declared && declared !== "true") return declared;
        var href = el.getAttribute("data-zip-url") || el.getAttribute("href") || "";
        var seg = String(href).split(/[?#]/)[0].split("/").pop() || "";
        return seg;
    }

    function proceedWithDownload(el) {
        if (!el) return;
        var href = el.href || el.getAttribute("href") || "";
        var zipUrl = el.getAttribute("data-zip-url") || "";
        var name = fileNameFor(el);

        /* Portable firmware ZIP links handled by lumen-site.js / portable-zip-links.js */
        if (zipUrl || (el.classList && (el.classList.contains("lumen-zip-download-button") || el.classList.contains("lumen-zip-text-link")))) {
            try {
                var custom = new CustomEvent("innioasis-confirmed-zip-download", {
                    bubbles: true,
                    cancelable: true,
                    detail: { element: el, url: zipUrl || href, name: name }
                });
                if (!el.dispatchEvent(custom)) return;
            } catch (_) {}
        }

        /* Standard Updater CE / Driver downloads through site-downloads.js */
        if (href && global.InnioasisDownloads && typeof global.InnioasisDownloads.start === "function") {
            global.InnioasisDownloads.start(href, el, name);
            return;
        }

        /* Fallback direct browser download */
        if (href) {
            var a = doc.createElement("a");
            a.href = href;
            if (name) a.download = name;
            a.rel = "noopener";
            a.setAttribute("data-site-download-direct", "1");
            a.setAttribute("data-direct-download", "1");
            a.setAttribute("data-win-arm64-confirmed", "1");
            (doc.body || doc.documentElement).appendChild(a);
            a.click();
            setTimeout(function () {
                if (a.parentNode) a.parentNode.removeChild(a);
            }, 3000);
        }
    }

    function onWindowClickCapture(event) {
        if (!state.isWindowsArm64) return;
        if (event.isTrusted === false) return;
        if (event.defaultPrevented || event.button !== 0) return;
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;

        var el = linkTargetOf(event.target);
        if (!isWindowsUpdaterDownload(el)) return;

        event.preventDefault();
        event.stopImmediatePropagation();

        openModal({
            infoOnly: false,
            fileName: fileNameFor(el),
            trigger: el,
            onProceed: function () {
                proceedWithDownload(el);
            }
        });
    }

    function activatePageUi() {
        if (!state.isWindowsArm64 || !doc.body) return;
        injectStyles();
        mountBanner();
        mountWindowsCardNote();
        ensureAllPlatformsVisible();
    }

    function boot() {
        /* Register click capture on window so it always runs BEFORE
           document-level capture handlers in site-downloads.js and
           portable-zip-links.js. */
        global.addEventListener("click", onWindowClickCapture, true);
        global.addEventListener("site-locale-ready", activatePageUi);
        global.addEventListener("y1-locale-change", activatePageUi);
        if (state.isWindowsArm64) {
            activatePageUi();
            global.setTimeout(activatePageUi, 350);
            global.setTimeout(activatePageUi, 1200);
        }
    }

    publish(detectSync());
    probeClientHints();

    global.InnioasisWinArm64 = {
        version: VERSION,
        isWindowsArm64: function () { return state.isWindowsArm64; },
        openModal: openModal,
        closeModal: closeModal,
        revealLinuxArm64: revealLinuxArm64
    };

    if (doc.readyState === "loading") {
        doc.addEventListener("DOMContentLoaded", boot);
    } else {
        boot();
    }
})(typeof window !== "undefined" ? window : globalThis);
