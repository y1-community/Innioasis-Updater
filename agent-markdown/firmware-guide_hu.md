---
title: "Firmware telepítési és készlet-visszaállítási útmutató | Innioasis Updater CE – Innioasis Firmware letöltések"
description: "Telepítse az egyéni firmware-t, vagy állítsa vissza a hivatalos gyári firmware-t a Innioasis Y1, Y2, G1, G3, G5, R1, PR1 és Timmkoo Q5, Q3 készülékekre a Innioasis Updater CE segítségével."
language: "hu"
source: "https://innioasis.app/firmware-guide_hu.html"
---

# Firmware telepítési és készlet-visszaállítási útmutató | Innioasis Updater CE – Innioasis Firmware letöltések

Firmware telepítési és készlet-visszaállítási útmutató

# Telepítse vagy állítsa vissza a firmware-t az eszközére

Válassza ki a lejátszóra nyomtatott modellt. Ezután kövesse az Updater CE lépéseit. A többit elintézi.[Szerezze be az Updater CE-t](guide_hu.html#platform)[Böngésszen a firmware archívumában](firmware_hu.html)[Hibaelhárítás](troubleshooting_hu.html)

Válassza ki a lejátszóra nyomtatott modellt és a kívánt szoftvert, majd nyissa meg ezt az útmutatót. [Böngésszen a szoftverek és a firmware-készletek között modell szerint](firmware_hu.html).

## 

[Szerezze be az Updater CE-t](guide_hu.html#download-updater)[Teljes írásos bemutató](guide_hu.html)

## Szerezze be a Innioasis Updater CE-t

Itt kezdheti, ha még nem rendelkezik az Updater CE-vel.Szerezd meg az Updater CE-nirányított telepítéssel

### Windows

Töltse le a telepítőt, nyissa meg, és kövesse a telepítési utasításokat.[Illesztőprogram letöltése és telepítése](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Töltse le az alkalmazást és az illesztőprogramokat](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Az Edge blokkolta?](#)

Ha a Windows nem tudja futtatni az alkalmazást, vagy nem indítja el, nyissa meg a Beállításokat, kattintson az Adatvédelem és biztonság → Windows biztonság → Alkalmazások és böngészők vezérlése elemre, és kapcsolja ki az Intelligens alkalmazásvezérlést. [A Windows nem indítja el az alkalmazást? Segítség](#smart-app-control)

A telepítés után újra kell indítania a számítógépet, hogy működjön.

### macOS

Töltse le az alkalmazást, és helyezze át az Alkalmazások mappába. Ha a macOS blokkolja, nyissa meg a Rendszerbeállítások, majd az Adatvédelem és biztonság elemet, és kattintson a Megnyitás mindenképpen gombra. [Hogyan működik ez](https://support.apple.com/en-gb/102445#openanyway)[Töltse le az Updater CE-t](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Töltse le az AppImage-et Intel és AMD rendszerekhez, tegye végrehajthatóvá, és futtassa.[Az AppImage letöltése Intel/AMD-hez](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Linux beállítási megjegyzések](drivers_hu.html#linux)Egy másik platform?

Szüksége van hosszabb számítógép-beállítási megjegyzésekre? Nyissa meg a [Windows](drivers_hu.html#windows) vagy [Linux](drivers_hu.html#linux) beállítási útmutató.

## Visszatérve az eredeti szoftverhez

A visszalépéshez válassza ki a modellt, válasszon Eredeti szoftver, majd fuss Telepítés / visszaállítás. Ez minden. A Frissítő lecseréli a rendszerszoftvert.[Y1 visszaállítási útmutató](guides/restore-original-y1.html)[Y2 visszaállítási útmutató](guides/restore-original-y2.html)

## Szoftver útmutatók modellenként

Válassza ki a modellt, majd nyissa meg a szoftver útmutatóját.

### Innioasis Y1

Szoftver a Y1 számára:

### Innioasis Y2

Szoftver a Y2 számára:

Megjegyzés a két eszközről

## Melyik eszközt használjam?

Innioasis Frissítő CE a lejátszó frissítésének legbiztonságosabb módja. Megőrzi zenéit, videóit és Bluetooth-párosításait. Azt jelzi, ha a frissítések készen állnak. Windowson, macOS-en és Linuxon fut. A Innioasis Universal Flash Tool törli a lejátszót, és kevesebb számítógépen működik.[Nyissa meg a teljes összehasonlítást](updater-comparison_hu.html)

### A Windows nem indítja el az alkalmazást? A Smart App Control kikapcsolása

A Windows Defender SmartScreen vagy a Smart App Control blokkolhatja az újonnan letöltött közösségi alkalmazásokat, mielőtt az aláírás hírneve elterjedne. Az intelligens alkalmazásvezérlés jelenleg olyan népszerű alkalmazásokat érint, mint az Epic Overlay Service (a Fortnite által használt) – Az Updater CE biztonságos és ellenőrzött használata. A Smart App Control kikapcsolása lehetővé teszi az Updater CE normál megnyitását és futtatását.
  - Nyissa meg Beállítások elemre Windows PC-jén (nyomja meg a Win + I).
  - Kattintson Adatvédelem és biztonság a bal oldalsávon, majd kattintson Windows Security.
  - Kattintson Alkalmazások és böngészők vezérlése.
  - alatt Intelligens alkalmazásvezérlés, kattintson Smart App Control beállításai.
  - Állítsa a kapcsolót állásba Le hogy az Updater CE elinduljon.

Az Edge blokkolta? Ha a Microsoft Edge magát a letöltést blokkolja, kattintson a További beállítások gombra (…) → Tartsa → Mutass többet → Mindenképpen tartsa meg.

A Smart App Control későbbi újraengedélyezése: Ha vissza szeretné kapcsolni a Smart App Control funkciót, újra engedélyezheti azt a Windows Registry alatt `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` beállításával `VerifiedAndReputablePolicyState` hogy `1` (Be) vagy `2` (Értékelési mód) és újraindítás.Súgó bezárása

## Ez hasznos volt?

Válasza segít továbbfejleszteni ezt az útmutatót.Igen, hasznosnak találtamMég nem[Tudassa velünk, hogyan javíthatunk](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
