---
title: "Innioasis Y1 és Y2 USB illesztőprogramok | Windows illesztőprogram és Linux engedélyek - Innioasis Frissítő"
description: "Állítsa be számítógépét a Innioasis Updater: Windows MediaTek illesztőprogram és Linux USB engedélyek használatára – valamint kábel- és időzítési javításokra."
language: "hu"
source: "https://innioasis.app/drivers_hu.html"
---

# Innioasis Y1 és Y2 USB illesztőprogramok | Windows illesztőprogram és Linux engedélyek - Innioasis Frissítő

Számítógép beállítása

# Készítse elő a számítógépet a lejátszó előtt.

A legtöbb csatlakozási probléma az illesztőprogramból, az engedélyekből, a kábelből vagy az időzítésből ered. A Windowsnak telepítenie kell a MediaTek illesztőprogramot. A Linuxnak a megfelelő USB engedélyekre van szüksége. Keresse meg platformját alább.[Szerezze be az Updater CE-t](guide_hu.html#platform)[Hibaelhárítás](troubleshooting_hu.html)

## Windows
  - Töltse le az alábbi MediaTek illesztőprogram-telepítőt.
  - Futtassa a telepítőt, és hagyja, hogy a Windows telepítse az illesztőprogramot.
  - Indítsa újra a számítógépet.
  - Nyissa meg az Updater CE alkalmazást, és várja meg a csatlakozási felszólítást, mielőtt csatlakoztatja a kikapcsolt lejátszót.

Egyes Windows rendszerek blokkolják az illesztőprogramot a Core elkülönítés (memóriaintegritás) révén. Ha az Updater CE az újraindítás után sem látja a lejátszót, kapcsolja ki a Memória integritását a Windows Security alkalmazásban, indítsa újra, és telepítse újra az illesztőprogramot. Ha végzett, kapcsolja vissza a beállítást, ha a rendszer lehetővé teszi.

A Windows nem indítja el az alkalmazást? Ha a Windows Security vagy a Smart App Control megakadályozza az Updater CE megnyitását, nyissa meg Beállítások elemre (nyomja meg Win + I) → Adatvédelem és biztonság → Windows Security → Alkalmazások és böngészők vezérlése → Smart App Control beállításai és állítsa be Le. Az intelligens alkalmazásvezérlés jelenleg olyan népszerű alkalmazásokat érint, mint az Epic Overlay Service (a Fortnite által használt) – Az Updater CE biztonságos és ellenőrzött használata. Ha később szeretné újra engedélyezni, állítsa be `VerifiedAndReputablePolicyState` hogy `1` (Be) vagy `2` (Értékelési mód) alatt `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` a Rendszerleíróadatbázis-szerkesztőben.[Windows illesztőprogram letöltése](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Vissza a fő útmutatóhoz](guide_hu.html#windows) · [Szoftverletöltések](firmware_hu.html)

## Linux USB engedélyek

A Linuxnak szüksége van arra, hogy a felhasználói fiókod beszélhessen a lejátszóban található MediaTek USB chippel. Az Updater CE rendszerint ezt a telepítés során rendezi, és ugyanaz az engedély vonatkozik a SP Flash Tool-ra is, ezért ezt tekintsd inkább javítási lépésnek, mint normál szakasznak.
  - Az Updater CE-t normál felhasználóként futtassa, ne rootként. A telepítő csak akkor kér rendszergazdai hozzáférést, ha szüksége van rá.
  - Ellenőrizze, hogy a lejátszó látható-e egyáltalán. Kapcsolja ki a lejátszót, csatlakoztassa a kábelt, és futtassa az lsusb parancsot egy terminálon. A csatlakoztatott lejátszó MediaTek eszközként jelenik meg a 0e8d gyártói azonosítóval.
`lsusb`
  - Ha megjelenik az lsusb-ben, de a Innioasis Updater CE vagy SP Flash Tool azt mondja, hogy az engedély megtagadva, vagy nem tudja megnyitni a portot, akkor a felhasználónak nincs hozzáférése a USB eszközhöz. Ugyanaz az udev-szabály mindkét eszközre vonatkozik, ezért adjunk hozzá egyet, amely lehetővé teszi, hogy a felhasználói csoport elolvassa.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Mentse el ezt a sort egy új /etc/udev/rules.d/51-innioasis.rules nevű fájlba, majd futtassa:`sudo udevadm control --reload && sudo udevadm trigger`
  - Húzza ki teljesen a lejátszót, dugja vissza, és próbálja meg újra a telepítést.
  - Ha SP Flash Tool sorozatos engedélyt vagy port versenyt jelent, húzza ki teljesen, és csak akkor csatlakoztassa újra, ha a rendszer kéri.
Ne improvizáljon vaku eltolásokat.Ha kézi helyreállítási eszközre vált, használja a projekthez mellékelt fájlokat és modellspecifikus konfigurációt.

[Vissza a fő útmutatóhoz](guide_hu.html#linux) · [Szoftverletöltések](firmware_hu.html) · [SP Flash Tool útmutató](sp-flash-tool_hu.html)

## Kábel és időzítés
  - Használjon ismert USB adatkábelt.
  - A hibaelhárítás során kerülje a hubokat.
  - Kapcsolja ki teljesen a megfelelő modellt.
  - Csak a felszólításra csatlakozzon.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
