---
title: "Network, clock and entropy contract v1 - Innioasis Updater"
description: "Network, clock and entropy contract v1 <!-- knowledge-base-scope: source-contract -- Source-contract scope. This page describes software ownership and interface behavior."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-architecture-platform-network-time-v1.html"
---

# Network, clock and entropy contract v1 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Network, clock and entropy contract v1

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Network, clock and entropy contract v1 > **Source-contract scope.** This page describes software ownership and > interface behavior. See [current state](../CURRENT_PLATFORM_STATE.md) for the exact latest image > and physical limits; implemented or enabled does not mean qualified. 

wpa_supplicant remains the only saved-network association/reconnect owner. The platform's action hook owns one udhcpc process. Every connection, loss or service restart changes the lease epoch. The DHCP hook accepts only wlan0 and the current epoch; a lock serializes late callbacks against a new connection. It validates IPv4 fields, applies interface-scoped addresses/routes, supports RFC3442 classless routes and publishes resolver configuration without untrusted search strings. Disconnect/NAK/lease failure flush only Wi-Fi addresses/routes/DNS. USB retains its fixed address and no default route. DHCP alone is not Online.

Online requires authenticated link, global address, default route and a successful recent libc DNS query on that connection's BSSID/address. The default probe is pool.ntp.org, configurable as dns_probe_host in /etc/y2linux/network-policy.json. It is a resolver check, not proof of unrestricted Internet or captive-portal absence. DNS callbacks are bounded and rejected after a peer/address/epoch change. A passive supplicant monitor records sanitized wrong-credential, rejected-auth and AP-unavailable events; it never connects a device. Association exceeding 30 seconds reports timeout; udhcpc leasefail reports DHCP timeout. Native supplicant/DHCP retain retry ownership. /run/y2/network.json contains boot/monotonic freshness; Reborn treats it as stale after 15 seconds and distinguishes authentication from usable Online. The supervised readiness process is separate from battery deadlines.

The same maintenance service reconciles SD insertion/removal independently of Reborn and samples storage admission/cleanup policy. A failed unmount is retried at most five times per insertion generation; no lazy/forced unmount or mount stack. A retained platform claim permits unmounting the exact removed card after its sysfs node vanishes. Explicit eject is not automatically undone. Reborn validates the claim's sysfs device instance as well as boot/mount/UUID.

Standard BusyBox ntpd starts only after Online, queries three pool.ntp.org names, and has no server listener. It does not use DHCP-provided time peers. Build commit time is a reproducible lower bound; an implausible boot clock (including the retained 2082 observation) is corrected to a plausible retained floor/build time, which alone does NOT enable TLS readiness. A valid NTP callback establishes a current-boot monotonic/wall anchor. A previously established time plus plausible RTC can establish a retained anchor on next boot. Readiness expires after 24 hours without a valid anchor, and unexpected wall-clock steps invalidate it.

NTP here is unauthenticated. This is a reasonable-clock strategy for TLS validity, not cryptographic time authentication. Signed update metadata and monotonic release policy must remain independently enforced. No RTC alarm or wake occurs at boot. RTC writes require an explicit owner qualification reference in /data/system/platform/rtc-policy.json (write_enabled=true). RTC retention and alarm/deep-wake operation remain PHYSICAL_GATE. `rtcwake` is included as standard owner qualification tooling; it must not be run before a scoped wake procedure.

BusyBox seedrng persists unique device seeds under private /data/system/entropy after data validation, never in the distributable root image. Its standard credit handling is preserved. Pinned Dropbear 2026.94 config has HAVE_GETRANDOM=1 and src/dbrandom.c retries blocking getrandom after EAGAIN; key generation cannot fall back to weak early urandom on this kernel. Status probes getrandom(GRND_NONBLOCK) and reports CRNG readiness separately from entropy_avail. No custom RNG is added. First-boot initialization latency still requires measurement on Y2.

Owner network qualification: after configuring an authorized AP in Reborn, capture `y2-status wifi`, `y2-platform time` and `y2-health`. On a controlled peer, start iperf3 -s; on Y2 explicitly run `y2-platform network-check --peer PEER_IP --throughput --seconds 30`(maximum 600 seconds). Stream`collect` concurrently to the owner host for CPU/thermal/XRUN/coexistence context. Repeat with wrong password, DHCP denied/restored, DNS denied/restored, AP loss/reappearance, service restart, reboot reconnect and screen off. Record actual observed counters; none are inferred as wireless packet loss. These actions are preparation, not executed physical tests.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
