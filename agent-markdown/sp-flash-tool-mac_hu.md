---
title: "SP Flash Tool Machez · MediaTek Scatter Flashing Guide &amp; Alternatives"
description: "A SP Flash Tool használata Mac rendszeren az Updater CE segítségével, és a szétszórt fájlok böngészése az MediaTek eszközökhöz, például Mechen H1, Innioasis Y1/Y2, Timmkoo és MT6580/MT6572 MP3 lejátszókhoz és telefonokhoz."
language: "hu"
source: "https://innioasis.app/sp-flash-tool-mac_hu.html"
---

# SP Flash Tool Machez · MediaTek Scatter Flashing Guide &amp; Alternatives

MediaTek Eszközök és platformok közötti villogás

# SP Flash Tool Mac-hez: A teljes útmutató és a Scatter Browser

A hivatalos MediaTek SP Flash Tool fut macOS-en? Itt van a pontos állapot, hogyan Frissítő CE natív MediaTek flashinget biztosít Mac rendszeren, és hogyan lehet flashelni bármilyen szórt alapú MediaTek MP3-lejátszót vagy okostelefont.

## Az igazság a SP Flash Tool-ról a macOS rendszeren

MediaTek soha nem adott ki hivatalos macOS buildet Smart Phone Flash Tool (SP Flash Tool). Az eszköz csak 32 bites/64 bites Windows alkalmazásként és x86_64 Linux binárisként létezett. A SP Flash Tool emulálása macOS rendszeren a Wine vagy CrossOver segítségével meghiúsul, mert a macOS kernel USB bővítményei nem teszik lehetővé a USB soros áthaladását a BROM rendszerindítási kézfogások során szükséges pontossággal.

A megoldás:Frissítő CE áthidalja ezt a szakadékot azáltal, hogy natív Apple Silicon és Intel macOS villogó könyvtárakat köt össze (az MTKclient alacsony szintű protokollmotorján keresztül) az automatizált szórásfelderítés mellett!

## Bármely MediaTek eszköz villogása „Telepítés fájlból” (Scatter Browser)

A Updater CE nem korlátozódik Innioasis játékosokra. Használhatja erőteljes univerzális MediaTek szórási villogóként minden olyan eszközhöz, amelyre szüksége van SP Flash Tool v5 vagy korábbi:
  - Mechen H1 és H11: MT6580 hordozható HiFi Android lejátszók.
  - Timmkoo Q3, Q5, G1, A5: MediaTek érintőképernyős digitális audiolejátszók.
  - Oilsky, Phueut, Luoran: MediaTek MT6572 / MT6582 zenelejátszók.
  - Korábbi MediaTek okostelefonok és speciális telefonok: MT6572, MT6580, MT6582, MT6735, MT6737, MT6739, MT6753 és MT8163 rendszert futtató eszközök.

### Egyéni szórási fájlok betöltése az Updater CE-ben:
  - Töltse le a gyári firmware archívumot (`.zip` vagy `.rar`), vagy bontsa ki a mappát, amely tartalmazza a `*scatter*.txt` fájlt.
  - Az Updater CE-ben válassza a lehetőséget Tallózás a fájlok között… a firmware-választó képernyőn.
  - Válassza ki a szórt szövegfájlt (pl. `MT6580_Android_scatter.txt`) vagy firmware zip csomagot.
  - Az Updater CE elemzi a memóriaeltolásokat, a partíciók címeit (előtöltő, rendszerindítás, helyreállítás, rendszer, felhasználói adatok), és ellenőrzi a szóródás integritását.
  - Kövesse a képernyőn megjelenő élő utasítást: kapcsolja ki az eszközt, és csatlakoztassa a USB kábelt a vakuhoz.

## Ha x64-es számítógépre van szüksége a tiltás megszüntetéséhez

Míg a macOS tisztán kezeli a szabványos flashinget és az egyéni ROM telepítéseket az MTKclient segítségével, a mély rendszerindítási hibák (ahol az előbetöltő partíció törlődött vagy nem egyezik) helyreállításához az SP Flash Tool teljes partíciós tábla újraépítése szükséges.

Ha hibaleállást tapasztal Mac számítógépen, váltson 64 bites Windows PC-re vagy x86_64 Linux munkaállomásra, és válassza Beállítások > Speciális beállítások megjelenítése > Flash-módszer > SP Flash Tool, és villogtassa a gyári szórócsomagot.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
