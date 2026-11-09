---
title: "A Innioasis Updater CE | használatának megkezdése Telepítse vagy állítsa vissza a firmware-t bármely Innioasis vagy Timmkoo lejátszóra - Innioasis Frissítő"
description: "Töltse le a Innioasis Updater CE-t Windowsra, macOS-re vagy Linuxra, majd telepítse vagy állítsa vissza a firmware-t bármelyik Innioasis vagy Timmkoo lejátszóra néhány irányított lépésben."
language: "hu"
source: "https://innioasis.app/guide_hu.html"
---

# A Innioasis Updater CE | használatának megkezdése Telepítse vagy állítsa vissza a firmware-t bármely Innioasis vagy Timmkoo lejátszóra - Innioasis Frissítő

Gyors kezdés

# A Innioasis Updater CE használatának megkezdése

Működik az összes Innioasis és Timmkoo audiolejátszóval. Telepítse a Innioasis Updater CE-t a számítógépére, válassza ki a modellt és a kívánt szoftvert, majd kövesse az utasításokat.

## 

[Szerezze be az Updater CE-t](guide_hu.html#download-updater)[Teljes írásos bemutató](guide_hu.html)

## Szerezze be a Innioasis Updater CE-t

Innioasis Frissítő CE az az alkalmazás, amely hivatalos frissítéseket és közösségi szoftvereket telepít a lejátszójára. Megőrzi zenéit és beállításait, és fut Windows, macOS és Linux rendszeren.

### Windows

Töltse le a telepítőt, futtassa, majd indítsa újra a számítógépet, amikor befejezte.[Szerezzen illesztőprogramokat](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Töltse le az Updater CE-t](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)

Ha a Windows nem tudja futtatni az alkalmazást, vagy nem indítja el, nyissa meg a Beállításokat, kattintson az Adatvédelem és biztonság → Windows biztonság → Alkalmazások és böngészők vezérlése elemre, és kapcsolja ki az Intelligens alkalmazásvezérlést. Az intelligens alkalmazásvezérlés jelenleg olyan népszerű alkalmazásokat érint, mint az Epic Overlay Service (a Fortnite által használt) – az Updater CE biztonságos és ellenőrzött használata. [A Windows nem indítja el az alkalmazást? Segítség](#smart-app-control)

A telepítés után indítsa újra a számítógépet. A járművezetői segítség a [Windows beállítási megjegyzések](drivers_hu.html#windows).

### macOS[Töltse le az Updater CE-t](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

Ha a Mac gépen nem tudja először futtatni az alkalmazást, nyissa meg a Rendszerbeállításokat, kattintson az Adatvédelem és biztonság elemre, görgessen le a Biztonság elemre, és kattintson a [Nyissa meg](https://support.apple.com/en-gb/102445#openanyway). Azt is megteheti, hogy a Ctrl billentyűt lenyomva tartva (vagy jobb gombbal) az alkalmazásra kattint a Finderben, és válassza a Megnyitás lehetőséget.

Működik Intel és Apple Silicon Mac számítógépeken, macOS Monterey és újabb verziókkal.

### Linux

Töltse le az AppImage-et Intel és AMD rendszerekhez, tegye végrehajthatóvá, és futtassa.[Az AppImage letöltése Intel/AMD-hez](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)

[Linux beállítási megjegyzések](drivers_hu.html#linux)Egy másik platform?

Szüksége van a lejátszóra, egy USB adatkábelre, amely adatokat hordoz (a csak töltéses kábelt nem lehet telepíteni), és néhány percre. Tartsa csatlakoztatva a kábelt, amíg az Updater CE azt nem mondja, hogy kész.

## Válassza ki a modellt és a szoftvert
  - Eszköz modell: válassza ki a lejátszóra nyomtatott modellt, Y1 vagy Y2. Az egyik modellhez készült szoftver nem telepíthető a másikra.
  - Szoftver és kiadás: válassza az Eredeti szoftvert, Rockbox, Solar, JJ Launcher, Inniclassic, Y2Player vagy Koensayr lehetőséget, ha az szerepel a modelljéhez, majd válasszon egy kiadást. A stabil a biztonságos választás.
  - Telepítés: kattintson Telepítés / visszaállítás, kapcsolja ki teljesen a lejátszót, és csak akkor csatlakoztassa a USB kábelt, ha az Updater CE kéri.
  - Befejezés: hagyja békén a lejátszót és a kábelt a sikerüzenetig, majd válassza le és indítsa el a lejátszót.

Y1 olyan lejátszóra van szükség, amelyet eredeti szoftverrel szállítottak a 2.0.0 előtt Eszköz Type B. Mindenki más megtartja az alapértelmezett Type A értéket.Frissítő csatlakozási utasítások kikapcsolt lejátszó csatlakoztatásáhozKövesse a modelljéhez tartozó élő Updater CE utasítást.

## Visszatérve az eredeti szoftverhez

Az egyedi szoftver visszafordítható. Az Updater CE programban válassza ki a modellt, majd válassza ki Eredeti szoftver, válasszon egy stabil kiadást, majd futtassa Telepítés / visszaállítás ugyanúgy. Nincs mit kézzel törölni.[Y1 visszaállítási útmutató](guides/restore-original-y1.html)[Y2 visszaállítási útmutató](guides/restore-original-y2.html)

Ha a vaku a USB felszólítás előtt leáll, először ellenőrizze a kábelt, a platform beállítását és a modellt. Lásd [hibaelhárítás](troubleshooting_hu.html) a javításokhoz a [Y1 és Y2 helyreállítási útmutató](guides/recovery.html) teljesítmény- és kerékhibákra, ill [SP Flash Tool](sp-flash-tool_hu.html) a fejlett helyreállításhoz.

## Szoftver útmutatók modellenként

Nyissa meg a modellhez és a kiválasztott szoftverhez tartozó útmutatót.

### Innioasis Y1

Szoftver a Y1 számára:

### Innioasis Y2

Szoftver a Y2 számára:

## Melyik eszközt használjam?

Ez az útmutató azt használja Innioasis Frissítő 2.5.1, más néven Updater CE. Biztonságban tartja dalait, videóit és Bluetooth-párosításait. Azt jelzi, ha a frissítések készen állnak. A Innioasis Universal Flash Tool törli a lejátszót, és manuális lépésekre van szüksége. [Hasonlítsa össze az eszközöket →](updater-comparison_hu.html)

## A Windows nem indítja el az alkalmazást? Smart App Control megoldás

A Windows Defender SmartScreen vagy a Smart App Control blokkolhatja az újonnan letöltött közösségi alkalmazásokat, mielőtt az aláírás hírneve elterjedne. Az intelligens alkalmazásvezérlés jelenleg olyan népszerű alkalmazásokat érint, mint az Epic Overlay Service (a Fortnite által használt) – Az Updater CE biztonságos és ellenőrzött használata. A Smart App Control kikapcsolása lehetővé teszi az Updater CE normál megnyitását és futtatását.
  - Nyissa meg Beállítások elemre Windows PC-jén (nyomja meg a Win + I).
  - Kattintson Adatvédelem és biztonság a bal oldalsávon, majd kattintson Windows Security.
  - Kattintson Alkalmazások és böngészők vezérlése.
  - alatt Intelligens alkalmazásvezérlés, kattintson Smart App Control beállításai.
  - Állítsa a kapcsolót állásba Le hogy az Updater CE elinduljon.

Edge-n keresztül letöltötted? Ha az Edge magát a letöltést blokkolja, kattintson a További beállítások gombra (…) → Tartsa → Mutass többet → Mindenképpen tartsa meg.

A Smart App Control későbbi újraengedélyezése: Ha vissza szeretné kapcsolni a Smart App Control funkciót, újra engedélyezheti azt a Windows Registry alatt `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` beállításával `VerifiedAndReputablePolicyState` hogy `1` (Be) vagy `2` (Értékelési mód) és újraindítás.

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
