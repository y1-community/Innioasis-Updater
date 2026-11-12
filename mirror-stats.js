/* Mirror download statistics.
 *
 * Parses the stats.txt file published beside every portable mirror release.
 * Each release file is a cumulative ledger: source firmware downloads, mirror
 * original copies and portable packages. Retired or replaced mirror assets are
 * not firmware installs and are left out. The site sums those ledgers across
 * releases to answer two questions:
 *
 *   - how many times was each original_name.zip downloaded?
 *   - how many times was the portable Windows / Linux / macOS build used?
 *
 * The total deliberately counts firmware ZIP downloads only. Images, JSON,
 * checksums and other release paperwork are not firmware installs.
 */
(function (root, factory) {
    "use strict";
    var api = factory();
    if (typeof module === "object" && module.exports) module.exports = api;
    if (root) root.InnioasisMirrorStats = api;
})(typeof window !== "undefined" ? window : globalThis, function () {
    "use strict";

    var PLATFORM_ORDER = [
        "windows",
        "windows-arm64",
        "windows-legacy",
        "linux",
        "linux-arm64",
        "macos"
    ];

    var PLATFORM_LABELS = {
        windows: "Portable zip for Windows",
        "windows-arm64": "Portable zip for Windows arm64",
        "windows-legacy": "Portable zip for Windows 32-bit (legacy)",
        linux: "Portable zip for Linux",
        "linux-arm64": "Portable zip for Linux arm64",
        macos: "Portable zip for macOS"
    };

    var PORTABLE_SUFFIXES = [
        ["-windows-arm64.zip", "windows-arm64"],
        ["-linux-arm64.zip", "linux-arm64"],
        ["-windows-legacy.zip", "windows-legacy"],
        ["-windows.zip", "windows"],
        ["-linux.zip", "linux"],
        ["-macos.zip", "macos"]
    ];

    function platformFor(name) {
        var lower = String(name || "").toLowerCase();
        for (var i = 0; i < PORTABLE_SUFFIXES.length; i++) {
            if (lower.slice(-PORTABLE_SUFFIXES[i][0].length) === PORTABLE_SUFFIXES[i][0]) {
                return PORTABLE_SUFFIXES[i][1];
            }
        }
        return "";
    }

    function isZip(name) {
        return /\.zip$/i.test(String(name || ""));
    }

    function friendlyPlatform(key) {
        var name = String(key || "").trim().toLowerCase();
        return PLATFORM_LABELS[name] || ("Portable zip for " + name.replace(/-/g, " "));
    }

    function parseCount(value) {
        var digits = String(value == null ? "" : value).replace(/[^0-9]/g, "");
        return digits ? Number(digits) : 0;
    }

    /* Parse one release's stats.txt. Sections are the headings the packager
       writes; the [Totals] block is the machine-readable duplicate. */
    function parseStats(text) {
        var result = {
            source: {},
            mirror: {},
            portable: {},
            originals: {},
            totals: {}
        };
        var section = "";

        String(text || "").split(/\r?\n/).forEach(function (line) {
            var heading = line.match(/^\s*\[([^\]]+)\]\s*$/);
            if (heading) {
                section = heading[1].trim().toLowerCase();
                return;
            }
            if (/^\s*Source downloads\b/i.test(line)) {
                section = "source";
                return;
            }
            if (/^\s*Mirror downloads\b/i.test(line)) {
                section = "mirror";
                return;
            }
            if (/^\s*Portable packages by platform\b/i.test(line)) {
                section = "portable";
                return;
            }
            if (/^\s*Original files\b/i.test(line)) {
                section = "originals";
                return;
            }
            if (/^\s*Coverage and estimate\b/i.test(line)) {
                section = "note";
                return;
            }

            if (section === "totals") {
                var total = line.match(/^\s*([a-z0-9_-]+)\s*=\s*([0-9,]+)\s*$/i);
                if (total) result.totals[total[1].toLowerCase()] = parseCount(total[2]);
                return;
            }

            /* Human-readable rows look like:
                   rom_y2.zip                               585
                   Portable zip for Windows                   9
               Names can contain spaces, so split on the final run of 2+ spaces. */
            var row = line.match(/^\s{2,}(.+?)\s{2,}([0-9][0-9,]*)\s*$/);
            if (!row) return;
            var name = row[1].trim();
            var value = parseCount(row[2]);
            if (!name) return;

            if (section === "source") result.source[name] = value;
            else if (section === "mirror") result.mirror[name] = value;
            else if (section === "portable") result.portable[name] = value;
            else if (section === "originals") result.originals[name] = value;
        });

        return result;
    }

    function add(map, key, value) {
        if (!key) return;
        map[key] = (map[key] || 0) + (Number(value) || 0);
    }

    function addSourceReleases(originals, releases) {
        (releases || []).forEach(function (release) {
            if (!release || release.draft) return;
            (release.assets || []).forEach(function (asset) {
                var name = String(asset && asset.name || "");
                if (!isZip(name) || platformFor(name)) return;
                add(originals, name, Number(asset.download_count) || 0);
            });
        });
    }

    /* Aggregate one or more stats.txt documents.
       documents: string[] or [{ tag, text }]
       options.sourceReleases: release API objects used when no stats exist yet. */
    function aggregate(documents, options) {
        options = options || {};
        var docs = Array.isArray(documents) ? documents : [];
        var originals = {};
        var portable = {};
        var releases = 0;
        var sawStats = false;
        var sawOriginalsSection = false;
        var sourceFromReleases = {};
        var hasSourceReleases = false;

        if (Array.isArray(options.sourceReleases) && options.sourceReleases.length) {
            addSourceReleases(sourceFromReleases, options.sourceReleases);
            hasSourceReleases = Object.keys(sourceFromReleases).length > 0;
        }

        docs.forEach(function (entry) {
            var text = typeof entry === "string" ? entry : (entry && entry.text) || "";
            if (!String(text).trim()) return;
            releases++;
            sawStats = true;
            var parsed = parseStats(text);

            if (Object.keys(parsed.originals).length) {
                sawOriginalsSection = true;
                Object.keys(parsed.originals).forEach(function (name) {
                    if (isZip(name)) add(originals, name, parsed.originals[name]);
                });
            } else {
                /* Source counts in a per-release ledger only cover releases that
                   have a mirror. When the source API is available it is the
                   complete source count, so use it instead of the ledger copy. */
                if (!hasSourceReleases) {
                    Object.keys(parsed.source).forEach(function (name) {
                        if (isZip(name)) add(originals, name, parsed.source[name]);
                    });
                }
                Object.keys(parsed.mirror).forEach(function (name) {
                    if (isZip(name) && !platformFor(name)) add(originals, name, parsed.mirror[name]);
                });
            }

            var portableTotals = Object.keys(parsed.totals).filter(function (key) {
                return /^portable_.+_downloads$/.test(key) && key !== "portable_total_downloads";
            });
            if (portableTotals.length) {
                portableTotals.forEach(function (key) {
                    var platform = key.slice("portable_".length, -"_downloads".length);
                    add(portable, platform, parsed.totals[key]);
                });
            } else {
                Object.keys(parsed.portable).forEach(function (key) {
                    if (key.toLowerCase() === "portable total") return;
                    add(portable, key, parsed.portable[key]);
                });
            }

        });

        if (hasSourceReleases && !sawOriginalsSection) {
            Object.keys(sourceFromReleases).forEach(function (name) {
                add(originals, name, sourceFromReleases[name]);
            });
        } else if (!sawStats && Array.isArray(options.sourceReleases)) {
            addSourceReleases(originals, options.sourceReleases);
        }

        var originalRows = Object.keys(originals).map(function (name) {
            return { name: name, count: originals[name] };
        }).filter(function (row) {
            return row.count > 0;
        }).sort(function (a, b) {
            return b.count - a.count || a.name.localeCompare(b.name);
        });

        var portableKeys = PLATFORM_ORDER.slice();
        Object.keys(portable).forEach(function (key) {
            if (portableKeys.indexOf(key) === -1) portableKeys.push(key);
        });
        var portableRows = portableKeys.map(function (key) {
            return {
                key: key,
                label: friendlyPlatform(key),
                count: portable[key] || 0
            };
        });

        var originalTotal = originalRows.reduce(function (sum, row) { return sum + row.count; }, 0);
        var portableTotal = portableRows.reduce(function (sum, row) { return sum + row.count; }, 0);

        return {
            total: originalTotal + portableTotal,
            originalTotal: originalTotal,
            portableTotal: portableTotal,
            originals: originalRows,
            portable: portableRows,
            releases: releases,
            hasStats: sawStats
        };
    }

    return {
        parseStats: parseStats,
        aggregate: aggregate,
        platformFor: platformFor,
        friendlyPlatform: friendlyPlatform,
        isZip: isZip,
        PLATFORM_ORDER: PLATFORM_ORDER
    };
});
