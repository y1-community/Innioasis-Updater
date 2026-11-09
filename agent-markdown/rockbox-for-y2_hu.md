---
title: "Rockbox for Y2 (Rockbox-Y2): áttekintés, összeállítások és telepítési útmutató"
description: "A Rockbox Y2, Rockbox-Y2 és rockbox-y2 a Innioasis Y2 közösségi Rockbox firmware portjára utal. Ismerje meg, mit tartalmaz, és hogyan telepítheti az Innioasis Updater CE segítségével."
language: "hu"
source: "https://innioasis.app/rockbox-for-y2_hu.html"
---

# Rockbox for Y2 (Rockbox-Y2): áttekintés, összeállítások és telepítési útmutató

[← Firmware letöltések](firmware_hu.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox – Y2 (Rockbox-Y2)

A Rockbox-Y2 (más néven „Rockbox for Y2”) a közösségi Rockbox firmware-portja a Innioasis Y2 számára. Saját ROM csomagját használja (`rom_y2.zip`), és közvetlenül a Innioasis Updater CE-n keresztül telepíthető.[Rockbox-Y2 telepítése](rockbox-y2/install.html)[Töltse le a ROM](rockbox-y2/download.html)[Írott oktatóanyag](guides/rockbox-y2.html)[Rockbox-Y2 központ](rockbox-y2/)

## Kifejezetten a Innioasis Y2 számára készült

A Innioasis Updater CE-ben ez a firmware a következőként szerepel Rockbox mikor Y2 van kiválasztva. Kiadványait a [spycemagic/y2-rockbox](firmware_hu.html?model=Y2&software=rockbox-y2) projekt a csomagnévvel `rom_y2.zip`.

Soha ne telepítsen Y1 firmware-csomagot Y2-re. Kiválasztás Y2 Az Updater CE automatikusan csak a Y2-kompatibilis buildekre szűri a kiadáslistát.

## Amit Rockbox-Y2 kínál
  - Címke alapú zenei könyvtár - albumok, előadók és műfajok között böngészhet az audiofájl címkéiből, vagy közvetlenül a mappák között.
  - Lejátszásvezérlők - hézagmentes lejátszás, keresztfade, ReplayGain és hangszínszabályzó beállítások.
  - Egyéni témák — telepítsen a Rockbox-Y2 builddel kompatibilis témákat ([Y2 témakalauz](rockbox-y2-themes.html)).
  - 100% offline — lejátssza a helyi fájlokat a MicroSD kártyájáról fiókok vagy előfizetések nélkül.
  - Könnyű gyári visszaállítás — bármikor visszatérhet az Y2 Eredeti szoftverhez az Updater CE-ben.

## Rockbox-Y2 kiadás kiválasztása
  - Mindig válasszon Y2 be Eszköz modell először.
  - Válassza a legújabb kiadást, hacsak nem egy adott verziót tesztel.
  - Olvassa el a [Rockbox-Y2 kiadási megjegyzések](release-notes/rockbox-y2/index_hu.html) hogy megnézze, mi változott az egyes buildekben.

## Közvetlen letöltések a közösségi fejlesztőktől

Innioasis Az Updater CE mindig közvetlenül a közösségi firmware-fejlesztőktől tölti le a firmware-csomagokat ([spycemagic/y2-rockbox](firmware_hu.html?model=Y2&software=rockbox-y2)), és kizárólag ezek a fejlesztők felelősek szoftverkiadásaik listázásáért az Updater CE-ben.

Engedélyezheti az Updater CE letöltését és villogását `rom_y2.zip` automatikusan, vagy töltse le a csomagot tőlünk [Rockbox-Y2 letöltési oldal](rockbox-y2/download.html) és [Rockbox ROM letöltési oldal](rockbox-rom-download_hu.html).[Rockbox-Y2 letöltés](rockbox-y2/download.html)[Telepítés helyi ZIP-ből](rockbox-y2/portable-zip.html)

## Hogyan kell telepíteni Rockbox-Y2
  - Nyissa meg a Innioasis Updater CE-t, és állítsa be Eszköz modell hogy Y2.
  - Válassza ki Rockbox be Szoftver.
  - Válassz egy Y2 kiadást a listáról.
  - Kattintson Telepítés / visszaállítás így az Updater CE közvetlenül a fejlesztőtől tölti le a csomagot.
  - Kapcsolja ki teljesen a Y2 készüléket, és csatlakoztassa egy USB adatkábellel, amikor az Updater CE kéri.
  - Várja meg a befejezésről szóló üzenetet, majd húzza ki és kapcsolja be Y2 készülékét.

A teljes lépésről lépésre történő áttekintéshez olvassa el a [Rockbox-Y2 oktatóanyag](guides/rockbox-y2.html).

## Az eredeti Y2 szoftver visszaállítása

A gyári firmware-hez való visszatéréshez válassza a lehetőséget Y2 és Eredeti szoftver az Updater CE-ben válasszon egy stabil kiadást, és kattintson a gombra Telepítés / visszaállítás. Lásd a [visszaállítási útmutató](rockbox-y2/restore-stock.html) és [Y2 Eredeti szoftver oldal](original-software-y2_hu.html).

## Gyakran ismételt kérdésekHonnan tölti le az Updater CE a Rockbox-Y2 alkalmazást?

Az Updater CE mindig közvetlenül a közösségi firmware-fejlesztők saját kiadásaiból tölti le a firmware-csomagokat (`spycemagic/y2-rockbox`). Kizárólag a fejlesztők felelősek szoftverkiadásaik listázásáért az Updater CE-ben.Miért a csomag neve rom_y2.zip?

A fejlesztő elnevezi a Y2 firmware archívumot `rom_y2.zip` így nem téveszthető össze a Y1-kal `rom.zip`.A Y1 témák működnek a Y2-on?

Nem mindig. Tekintse meg a Y2 build kiadási megjegyzéseit, és tekintse meg a [Rockbox-Y2 témakalauz](rockbox-y2-themes.html).

## Kapcsolódó útmutatók

### [Rockbox-Y2 központ](rockbox-y2/)

Minden Y2 útmutató: telepítés, letöltések, témák, visszaállítás, kettős rendszerindítás és hibaelhárítás.

### [Rockbox-Y1 vs Rockbox-Y2](rockbox-y1-vs-y2.html)

Hogyan különbözik a Y1 és a Y2 Rockbox build.

### [Rockbox-Y2 témák](rockbox-y2-themes.html)

Témák telepítése és visszaállítása a Rockbox-Y2 webhelyen.

### [Rockbox – Y1](rockbox-for-y1_hu.html)

Áttekintés és telepítési útmutató a Innioasis Y1 porthoz.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
