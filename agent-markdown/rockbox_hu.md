---
title: "A Rockbox telepítése Innioasis Y1 vagy Y2 - Innioasis frissítőre"
description: "Telepítse a Rockbox-t Innioasis Y1-re vagy Y2-ra Frissítővel: témák, stabil kiadások, Type A és Type B megjegyzések, valamint az Eredeti Szoftver visszaállítása ezek után."
language: "hu"
source: "https://innioasis.app/rockbox_hu.html"
---

# A Rockbox telepítése Innioasis Y1 vagy Y2 - Innioasis frissítőre

Rockbox hivatkozás

# A Rockbox elérése a Y1 vagy Y2

Rockbox megváltoztatja a lejátszó szoftverét, és mélyebb zenelejátszó felületet, lejátszásvezérlőket, rendezést és témabeállításokat nyit meg. A telepítés irányított, de Y1 és Y2 külön utakat jelentenek.[Rockbox, Y1](guides/rockbox-y1.html)[Rockbox, Y2](guides/rockbox-y2.html)[Miért Rockbox?](rockbox-benefits_hu.html)

## Mit változtat a telepítés

A Rockbox egyedi szoftver. Ez nem szünteti meg a lehetőségét, hogy visszatérjen a készletfelületre, ha a megfelelő Eredeti szoftvercsomag elérhető. Javíthatja a zeneböngészést és a testreszabást, de a funkciók, a felbontás, az akkumulátor élettartama és a téma kompatibilitása a felépítéstől függ.Ne keverje össze a modelleket. Válassza a Y1 lehetőséget Y1 lejátszóhoz és a Y2 lehetőséget Y2 lejátszóhoz. A hasonló megjelenésű kiadásnév nem elegendő bizonyíték arra, hogy egy csomag kompatibilis.

## Nézze meg a videót

Videó: Frawgeeys. Megmutatja a Innioasis Updater útvonalat; használja az alábbi, modellspecifikus írásos lépéseket Y1 vagy Y2 esetén.

A videót készítette [Cristian Plaza](https://www.youtube.com/@CristianPlaza) (spanyol), a Rockbox megjelenítése egy Y1-on. Használja az alábbi, modellspecifikus lépéseket a lejátszójához.

## A megosztott Updater útvonal
  - Telepítse az Updater programot, és ne csatlakoztasson semmit, amíg nem kéri.
  - Válassza ki a lejátszóra nyomtatott modellt Eszköz modell.
  - Válasszon Rockbox be Szoftver.
  - Válasszon stabil kiadást, hacsak nem szándékosan tesztel egy éjszakai összeállítást.
  - Kattintson Telepítés / visszaállítás, majd kövesse a kikapcsolás és a USB csatlakozási utasítást.
  - Csak a sikerüzenet után szakítsa meg a kapcsolatot.

## 240p, 360p és témák

A régebbi Rockbox témagyűjtemények 240p-re készülhetnek. A Y1 közösségi buildek is használnak 360p kompatibilitási címkéket. A build kiválasztása előtt olvassa el a kiadási megjegyzéseket és a téma forrását. Előfordulhat, hogy az egyik felbontáshoz vagy szoftvercsaládhoz készült téma nem működik egy másikon.[Böngésszen a közösségi témák között](https://themes.innioasis.app/?lang=hu)[Témaeszközök](https://themes.innioasis.app/?lang=hu)

## Visszatérés az eredeti szoftverhez

Válassza újra ugyanazt a modellt, válassza ki Eredeti szoftver, válasszon egy stabil kiadást, és használja Telepítés / visszaállítás. Ha a hiba a USB üzenet előtt történt, ellenőrizze a számítógépet és a kicsomagolt fájlokat. Ha a lejátszót észlelték, de a vaku nem sikerült, kezdje a következővel [hibaelhárítás](troubleshooting_hu.html).[Y1 visszaállítás](guides/restore-original-y1.html)[Y2 visszaállítás](guides/restore-original-y2.html)

## GYIKÚjratelepítettem a Rockbox-t, és nem javított semmit.

A Rockbox újratelepítése ugyanazt a buildet írja ugyanarra a fájlra, így nem tudja visszaállítani azokat a dolgokat, amelyeket Rockbox a MicroSD-on tárol. Ha a probléma egy hibás beállítás, téma, lejátszási lista vagy adatbázis, amely a kártyán található, az újratelepítés nem törli azt. A megbízható visszaállítás törli a `.rockbox` mappából a MicroSD - Rockbox a következő rendszerindításkor újat épít.
  - Kapcsolja ki teljesen a lejátszót, és távolítsa el a MicroSD kártyát, vagy csatlakoztassa a lejátszót USB meghajtóként.
  - Jelenítse meg a rejtett fájlokat a számítógépén, hogy a mappa látható legyen. Hogyan lehet megjeleníteni a rejtett fájlokatPontfájlok megjelenítése a számítógépenWindows: a File Explorerben nyissa meg a Megtekintés fület és pipát Rejtett elemek.macOS: a Finder sajtóban Cmd+Shift+. a rejtett fájlok váltásához.Linux · GNOME fájlok: nyomja meg Ctrl+H, vagy nyissa meg a menüt, és válassza ki Rejtett fájlok megjelenítése.Linux · KDE Dolphin: nyomja meg Ctrl+H, vagy használja Nézet → Rejtett fájlok megjelenítése.
  - Törölje a `.rockbox` mappát a kártya gyökeréből.
  - Helyezze vissza a kártyát, és indítsa el a lejátszót. Rockbox újra létrehozza a mappát az alapértelmezett beállításokkal.
  - Alkalmazza újra a témát és a beállításokat. Ha a probléma csak egy adott téma után tér vissza, akkor ez a téma az oka.

Törlés `.rockbox` nem távolítja el a Rockbox alkalmazást, és nem érinti meg a zenét – a mappa a beállításokat, a témákat és a gyorsítótárakat tartalmazza, és automatikusan újraépül. Ha meg szeretné tartani a témákat, másolja ki a mappát `.rockbox` törlés előtt, vagy nevezze át a mappát erre `.rockbox-old` először.Miért nem látom a .rockbox mappát a MicroSD-on?

A ponttal kezdődő mappák alapértelmezés szerint a legtöbb számítógépen rejtve vannak. Nem kell látnia a Rockbox telepítéséhez — A frissítő kezeli a fájlokat. Ha hibaelhárítást végez, és törölni szeretné, először kapcsolja be a rejtett fájlokat. Hogyan lehet megjeleníteni a rejtett fájlokatPontfájlok megjelenítése a számítógépenWindows: a File Explorerben nyissa meg a Megtekintés fület és pipát Rejtett elemek.macOS: a Finder sajtóban Cmd+Shift+. a rejtett fájlok váltásához.Linux · GNOME fájlok: nyomja meg Ctrl+H, vagy nyissa meg a menüt, és válassza ki Rejtett fájlok megjelenítése.Linux · KDE Dolphin: nyomja meg Ctrl+H, vagy használja Nézet → Rejtett fájlok megjelenítése.A .rockbox törlése visszaállítja a témát és a beállításaimat?

igen — `.rockbox` tartalmazza Rockbox beállításait, témáját, lejátszási listáit és gyorsítótárazott adatbázisát. Ha törli, az Rockbox tiszta alapértelmezett állapotba kerül. Készítsen biztonsági másolatot a teljes mappáról (vagy nevezze át erre `.rockbox-old`), ha esetleg vissza szeretné kapni, indítsa el a lejátszót, és Rockbox létrehoz egy új mappát.

## További Rockbox-Y1 és Rockbox-Y2 útmutatók

Fedezze fel a lépésenkénti útmutatókat a telepítéshez, letöltéshez, tematikához, visszaállításhoz és hibaelhárításhoz Rockbox mindkét modellen:[Rockbox-Y1 központ](rockbox-y1/)[Rockbox-Y2 központ](rockbox-y2/)[Rockbox ROM letöltés](rockbox-rom-download_hu.html)[Rockbox – Y1](rockbox-for-y1_hu.html)[Rockbox – Y2](rockbox-for-y2_hu.html)[Rockbox-Y1 vs Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1 témák](rockbox-y1-themes.html)[Rockbox-Y2 témák](rockbox-y2-themes.html)

## Hasznos volt ez a hivatkozás?

Válasza segít továbbfejleszteni ezt az útmutatót.IgenMég nem[Tudassa velünk, hogyan javíthatunk](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
