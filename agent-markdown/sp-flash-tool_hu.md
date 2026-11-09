---
title: "SP Flash Tool Innioasis és Timmkoo játékosok számára"
description: "Keresse meg a Innioasis Updater-hez mellékelt SP Flash Tool-ot Windows és Linux rendszeren, csomagolja ki a rom.zip vagy rom_y2.zip elemet, és flashelje meg a Innioasis Y1 vagy Y2 fájlt a megfelelő szórófájllal."
language: "hu"
source: "https://innioasis.app/sp-flash-tool_hu.html"
---

# SP Flash Tool Innioasis és Timmkoo játékosok számára

Kézi villogás

# Flash eszköz Innioasis és Timmkoo játékosokhoz

SP Flash Tool bekerül a Innioasis Frissítés bekapcsolva [Windows](drivers_hu.html#windows) és [Linux](drivers_hu.html#linux). Már megvan. Ez az útmutató bemutatja a biztonságos használat módját Innioasis Y1 vagy Y2, valamint az Updater útvonalat Timmkoo játékosok számára.[Térjen vissza a Frissítő útmutatóhoz](guide_hu.html)[Firmware letöltések](firmware_hu.html)[Hibaelhárítás](troubleshooting_hu.html)

Kezdje a Innioasis Frissítővel

## A Frissítő egy lépésben elvégzi az egész munkát

Az Updater a legtöbb telepítést egy menetben végzi el. Válassza ki a szoftvert, kövesse a lépéseket, és kész. Azt is jelzi, ha javítás vagy új kiadás érkezik. SP Flash Tool az Updater's Toolkitben található azon ritka esetekben, amikor az Updater nem tudja befejezni. Az alábbi lépések kivételek.

## Mire való ez az eszköz

Az Updater villogtatja helyetted a lejátszót. SP Flash Tool ugyanaz a motor, védőkorlát nélkül. Használja, ha az Updater nem indul el, ha a lejátszó nem csatlakozik, vagy ha ismeri az utat egy szórófájlban.Először próbáld ki az Updater-t. A legtöbb telepítéshez és helyreállításhoz az útmutatót [Frissítő útvonal](guide_hu.html) a biztonságosabb választás. Használja a SP Flash Tool-t, ha tudja, miért van rá szüksége, és tartson készenlétben egy feltöltött akkumulátort és egy USB adatkábelt.

## Flash eszköz Innioasis játékosok számára

Innioasis Az Updater a Innioasis játékosok flash eszköze. Telepíti a hivatalos szoftvereket, frissíti és visszaállítja a csomagokat a modellnek megfelelő folyamaton keresztül, valamint megőrzi a zenét és a beállításokat.

### Innioasis Y1 flash eszköz

Válassza ki a Y1 kiadást az Updaterben, majd csatlakoztassa a kikapcsolt lejátszót, amikor az alkalmazás kéri. Ugyanazok az Y1 csomagok működnek a SP Flash Tool-al, amikor manuális útvonalra van szüksége.

### Innioasis Y2 flash eszköz

Válasszon egy kiadást a Y2 számára. A Y2 csomagok nem cserélhetők fel a Y1 csomagokkal, ezért mielőtt elkezdené, ellenőrizze a modellt.

## Flash eszköz Timmkoo játékosok számára

A Timmkoo játékos ugyanazt az Updater telepítési folyamatot használja. Közvetlenül olvassa Timmkoo ZIP és RAR csomagjait, így nincs szüksége külön flash eszközre vagy szórófájlra.

### Timmkoo Q5 flash eszköz

Válassza ki a Q5 modellt az Updaterben, válassza ki a Timmkoo csomagot, majd futtassa a Telepítés/Visszaállítás parancsot, és a felszólításra csatlakoztassa a lejátszót.

### Timmkoo Q3 és Q3E flash eszköz

A Q3 bejegyzés a Q3-re és a Q3E-ra egyaránt vonatkozik. A frissítő kiválasztja a megfelelő fájlokat a projekt által közzétett csomagból.

### Timmkoo A5 flash eszköz

A csomag kiválasztása előtt válassza ki a A5 modellt, majd kövesse ugyanazt a telepítési utasítást.

## Ahova az Updater teszi

A SP Flash Tool az Updater telepítési mappájával együtt érkezik, nem külön letöltésként. Nyissa ki onnan, amikor szüksége van rá.

### Windows

Nyissa meg az Updater telepítési mappáját, és futtassa `flash_tool.exe`. A mappa általában alatta van `%LOCALAPPDATA%\Innioasis Updater`. Néhány beállítás tartalmaz egy Toolkit mappát egy SP Flash Tool parancsikonnal.

### Linux

Futtassa a kötegelt `flash_tool` bináris fájl az Updater alkalmazás mappájában az x86 / x86_64 rendszeren. A projekttelepítő udev szabályokkal készíti elő a USB engedélyeket, így a lejátszónak meg kell jelennie, amikor csatlakozik.

### macOS

SP Flash Tool nincs csomagolva macOS rendszeren. Az Updater inkább az MTKClient útvonalat használja ott. Használja a [irányított telepítés](guide_hu.html) Mac számítógépen, és tartsa meg a SP Flash Tool-t Windows vagy Linux rendszerű gépen.

Az eszközt a MediaTek letöltési ügynökkel és modellspecifikus konfigurációval szállítjuk, így nem kell máshonnan gyűjtenie a DA-t vagy szétszórnia a fájlokat.

## Készítse elő a firmware-t
  - Fogja meg a kívánt kiadást [Firmware letöltések](firmware_hu.html). Válasszon `rom.zip` egy Y1 vagy `rom_y2.zip` egy Y2 számára.
  - Bontsa ki a ZIP-fájlt a saját mappájába. A Windows képes az Összes kibontása funkcióra. Linuxon használja az archívumkezelőt vagy `unzip` egy terminálban.
  - Ellenőrizze, hogy a szórófájl a kicsomagolt mappában van-e. Általában elnevezték `MT6572_Android_scatter.txt` Y1 csomagokhoz és `MT6582_Android_scatter_def.txt` Y2 csomagokhoz, bár egy kiadás a projektje után nevezheti el.
Tartsa külön a modelleket. A Y1 szórás egy MT6572 eszközt, a Y2 szórást pedig egy MT6582 eszközt ír le. Ha a rosszat villogtatjuk, akkor a játékosok falazzák. Ha a ZIP-en belüli szóródás nem egyezik az Ön modelljével, álljon meg, és használja helyette a modellhez tartozó csomagot.

## Töltse be a szórást és a vakut
  - Nyissa meg a SP Flash Tool fájlt az Updater telepítési mappájából.
  - A Letöltés lapon kattintson a gombra Válasszon a Scatter-loading File mellett, és válassza ki a szórófájlt a kibontott mappából. A partíciók listája kitöltődik.
  - Hagyja bekapcsolva a vaku módot Csak letöltés kivéve, ha szándékosan teljes gyógyulást végez, amire szüksége van Firmware frissítés.
  - Kattintson Letöltés. Az eszköz megvárja a játékost.
  - Kapcsolja ki teljesen a lejátszót, majd csatlakoztassa a USB adatkábelt. Tedd le a lejátszót, és ne mozgasd.
  - Várja meg a zöld pipát. Csak ezután húzza ki a kábelt, és indítsa el a lejátszót.

Tartsa be ugyanazokat a USB kábel- és időzítési szabályokat, mint az irányított útvonalon: adatkábel, hub nélkül, és csak akkor csatlakoztassa, ha a szerszám készen áll.

## Ha nem villog
  - Ellenőrizze, hogy a szórás és a ZIP egyezik-e a lejátszóra nyomtatott modellel.
  - A csatlakoztatás előtt győződjön meg arról, hogy a lejátszó teljesen ki van kapcsolva.
  - Windows rendszeren ellenőrizze a MediaTek illesztőprogram telepítését az Updater telepítésével; Linuxon erősítse meg az udev szabályokat a projekttelepítőből.
  - Csak akkor csatlakoztassa újra a kábelt, ha a szerszám várakozik. Egy kikötői versenyhez szükség lehet egy teljes áramtalanításra és egy frissre Letöltés kattintson.

Bármire ezen túlmenően, nyissa meg [hibaelhárítás](troubleshooting_hu.html). És ne feledje: az Updater továbbra is a normál útvonal, és [Y1](guides/restore-original-y1.html) és [Y2](guides/restore-original-y2.html) visszaállítási útmutatók is használják.

## Ez hasznos volt?

Válasza segít továbbfejleszteni ezt az útmutatót.Igen, hasznosnak találtamMég nem[Tudassa velünk, hogyan javíthatunk](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
