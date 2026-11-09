---
title: "Rockbox for Y1 (Rockbox-Y1): áttekintés, összeállítások és telepítési útmutató"
description: "A Rockbox Y1, Rockbox-Y1 és rockbox-y1 mind a Innioasis Y1 közösségi Rockbox firmware-ére utalnak. Ismerje meg, mit ad hozzá, melyik buildet válassza, és hogyan telepítheti az Innioasis Updater CE segítségével."
language: "hu"
source: "https://innioasis.app/rockbox-for-y1_hu.html"
---

# Rockbox for Y1 (Rockbox-Y1): áttekintés, összeállítások és telepítési útmutató

[← Firmware letöltések](firmware_hu.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox – Y1 (Rockbox-Y1)

A „Rockbox”, „Rockbox-Y1” és „Rockbox for Y1” mind ugyanarra a közösségi Rockbox firmware-re utalnak a Innioasis Y1 számára. Íme, mit ad hozzá a lejátszóhoz, melyik buildet válassza, és hogyan telepítse az Innioasis Updater CE-vel.[Rockbox-Y1 telepítése](rockbox-y1/install.html)[Töltse le a ROM](rockbox-y1/download.html)[Írott oktatóanyag](guides/rockbox-y1.html)[Rockbox-Y1 központ](rockbox-y1/)

## Egy firmware, több név

A Innioasis Updater CE-ben ez a firmware a következőképpen jelenik meg: Rockbox amikor kiválasztja az eszköz modelljét Y1. Útmutatók, videók és kiadási megjegyzések is hívják Rockbox-Y1 vagy Rockbox – Y1 így egyértelmű, hogy a build a Y1-ra vonatkozik és nem a Y2-re.

Mindig ellenőrizze a lejátszóra nyomtatott modellt a telepítés előtt: a Y1 és Y2 firmware-csomagok nem cserélhetők fel.

## Mit ad hozzá Rockbox-Y1 a Y1

A Rockbox-Y1 a nyílt forráskódú Rockbox zenelejátszó firmware közösségi portja a Innioasis Y1 számára:
  - Címke alapú zenei könyvtár — böngészhet előadó, album, műfaj és év szerint hangcímkék segítségével, vagy böngészhet közvetlenül a mappákban.
  - Speciális hanglejátszás - hézagmentes lejátszás, keresztfade, ReplayGain és teljes hangszínszabályzó.
  - Egyéni témák – több száz 240p és 360p közösségi téma közül választhat, beleértve a klasszikus iPod-stílusú elrendezéseket.
  - FM rádió - beépített FM rádió támogatás.
  - Opcionális extrák — podcast letöltések Wi-Fi és Last.fm / ListenBrainz / Maloja segítségével a támogatott buildeken való scrollozással.
  - Kettős rendszerindítás — váltson vissza a gyári Eredeti szoftverre anélkül, hogy újra kellene frissítenie a támogatott buildeken.

## Melyik Y1 buildet válasszam?
  - 240p vs. 360p — 240p buildek klasszikus 320×240 Rockbox témákkal dolgoznak; A 360p-s buildek élesebb, 480×360 Y1-es témákat használnak. Párosítsa a felépítési felbontást a használni kívánt témákhoz ([240p vs. 360p útmutató](rockbox-y1/resolution.html)).
  - Type A kontra Type B — a Type A Y1 lejátszókhoz való, amelyek gyári szoftvere 2.0.0 vagy újabb; Type B a korábbi Y1 egységekre vonatkozik. Válassza a Type A lehetőséget, hacsak nem tudja, hogy a Y1 Type B.
  - Stabil vs. Nightly — Válasszon egy stabil felépítést a mindennapi zenehallgatáshoz, vagy egy éjszakai összeállítást a legújabb változások teszteléséhez.

## Közvetlen letöltések a közösségi fejlesztőktől

Innioasis Az Updater CE mindig közvetlenül a közösségi firmware-fejlesztőktől tölti le a firmware-csomagokat ([rockbox-y1/rockbox](firmware_hu.html?model=Y1&software=rockbox-y1)), és kizárólag maguk a fejlesztők felelősek szoftverkiadásaik listázásáért az Updater CE-ben.

Engedheti, hogy az Updater CE automatikusan letöltse és telepítse a firmware-t, vagy letöltheti a ROM csomagokat tőlünk [Rockbox-Y1 letöltési oldal](rockbox-y1/download.html) és [Rockbox ROM letöltési oldal](rockbox-rom-download_hu.html).[Rockbox-Y1 letöltés](rockbox-y1/download.html)[Telepítés helyi ZIP-ből](rockbox-y1/portable-zip.html)

## Hogyan kell telepíteni Rockbox-Y1
  - Nyissa meg a Innioasis Updater CE-t, és állítsa be Eszköz modell hogy Y1.
  - Válassza ki Rockbox be Szoftver.
  - Válasszon egy stabil kiadást (vagy engedélyezze az éjszakai összeállításokat az előnézet teszteléséhez).
  - Kattintson Telepítés / visszaállítás így az Updater CE közvetlenül a fejlesztőtől tölti le a csomagot.
  - Kapcsolja ki teljesen a Y1 készüléket, és csatlakoztassa egy USB adatkábellel, amikor az Updater CE kéri.
  - Várja meg a befejezés üzenetét, majd válassza le és kapcsolja be a lejátszót.

Képernyőképekért és részletes beállítási tippekért olvassa el a [teljes Rockbox-Y1 oktatóanyag](guides/rockbox-y1.html).

## Az eredeti Y1 szoftver visszaállítása

Bármikor visszatérhet a gyári szoftverhez: válassza ki Y1 és Eredeti szoftver az Updater CE-ben válasszon egy stabil kiadást, és kattintson a gombra Telepítés / visszaállítás. A MicroSD kártyán lévő zenék megmaradnak. Lásd a [visszaállítási útmutató](rockbox-y1/restore-stock.html) és [Y1 Eredeti szoftver oldal](original-software-y1_hu.html).

## Gyakran ismételt kérdésekA Rockbox Y1 ugyanaz, mint Rockbox-Y1?

Igen. Rockbox, Rockbox-Y1, Rockbox Y1 esetén, és `rockbox-y1` mindegyik ugyanarra a közösségi Rockbox portra vonatkozik a Innioasis Y1 számára.Honnan tölti le az Updater CE a Rockbox-Y1 alkalmazást?

Az Updater CE mindig közvetlenül a közösségi firmware-fejlesztők saját kiadásaiból tölti le a firmware-csomagokat (`rockbox-y1/rockbox`). Kizárólag a fejlesztők felelősek szoftverkiadásaik listázásáért az Updater CE-ben.Telepíthetem a Rockbox-Y1-t Y2-re?

Nem. A Y2 különálló firmware-felépítéssel rendelkezik. Használja [Rockbox – Y2](rockbox-for-y2_hu.html) helyette.A Rockbox-Y1 telepítése törli a zenémet?

Nem. A zene a MicroSD kártyán tárolódik, és a lejátszó belső firmware-ének felvillantása nem érinti.

## Kapcsolódó útmutatók

### [Rockbox-Y1 központ](rockbox-y1/)

Minden Y1 útmutató: telepítés, letöltések, témák, visszaállítás, kettős rendszerindítás és hibaelhárítás.

### [Rockbox-Y1 vs Rockbox-Y2](rockbox-y1-vs-y2.html)

Hogyan különbözik a Y1 és a Y2 Rockbox build.

### [Rockbox-Y1 témák](rockbox-y1-themes.html)

240p és 360p témák átvitele az Updater CE segítségével.

### [Rockbox áttekintése](rockbox_hu.html)

A Rockbox bemutatása Innioasis Y1 és Y2 lejátszókon.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
