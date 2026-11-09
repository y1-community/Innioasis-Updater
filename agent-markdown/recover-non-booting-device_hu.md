---
title: "Nem induló MediaTek lejátszó helyreállítása MTK-kliens meghibásodása után · Innioasis Közösség"
description: "Útmutató lépésről lépésre a nem induló Innioasis Y1, Y2, G1, Timmkoo és MediaTek lejátszók leállításához és helyreállításához, miután az MTKclient megszakította a flash-eket Linuxon vagy macOS-en."
language: "hu"
source: "https://innioasis.app/recover-non-booting-device_hu.html"
---

# Nem induló MediaTek lejátszó helyreállítása MTK-kliens meghibásodása után · Innioasis Közösség

Hibaelhárítás és eszköz-helyreállítás

# Nem rendszerindító eszköz helyreállítása az MTKclient villogása után

Ha a Innioasis Y1, Y2 vagy MediaTek eszköz nem kapcsol be, vagy fekete képernyőt mutat, miután az MTKclienttel villogott macOS vagy Linux rendszeren, ne essen pánikba. A hardveres BootROM (BROM) állandó és nem semmisíthető meg.

## Miért akadhat el vagy hagyhat el fekete képernyőt az MTKclient?

Az MTKclient szoftveres hasznos terhelésekre (kamakiri / amonet) támaszkodik, hogy megkerülje a DA hitelesítést és a libusb-n keresztüli nyers USB kommunikációt. MacOS és Linux ARM64 rendszereken:
  - USB A kézfogási késleltetés vagy a port időtúllépései a macOS rendszeren leállíthatják a DA hasznos terhelés beadását az átvitel közben.
  - A hiányzó vagy hiányos partíciófejlécek a rendszerbetöltőt (preloader / lk) nem reagáló állapotban hagyják.
  - A lejátszó teljesen halottnak tűnik – nincs LED, nincs töltési ikon, nincs képernyő háttérvilágítása.

Még ebben az állapotban is visszaesik a MediaTek lapkakészlet BROM mód (USB VID 0e8d, PID 0003), készen áll a hivatalos alacsony szintű helyreállításra.

## A végleges helyreállítási módszer: SP Flash Tool Motor az Updater CE-ben

A legbiztonságosabb és legmegbízhatóbb módja annak, hogy helyreállítsd a tégla lejátszód Frissítő CE a tisztviselővel konfigurálva SP Flash Tool backend.

### Pontos lépések az Updater CE-ben:
  - Nyissa meg Frissítő CE.
  - Kattintson Beállítások elemre a bal oldali navigációs oldalsávban.
  - Görgessen le a Speciális részhez, és engedélyezze Speciális beállítások megjelenítése.
  - alatt Telepítési módszer (vagy Villogó motor a MediaTek telepítő számára), keresse meg a Flash-módszer legördülő menüt.
  - Módosítsa a kijelölést innen Automatikus (ajánlott) vagy MTKClient hogy SP Flash Tool.
  - Erősítse meg a felszólítást, és térjen vissza a fő telepítési folyamathoz.

## Platformarchitektúra és operációs rendszer követelményei a következőhöz: SP Flash Tool

MediaTek tisztviselője `SP Flash Tool` bináris natív módon, mint an x86_64 ELF bináris Linuxhoz és a PE32+ futtatható Windows x64-hez.Fontos hardver megjegyzés macOS és ARM64 Linux felhasználók számára:
 Mivel a MediaTek nem fordítja le a SP Flash Tool-et macOS-re (Darwin) vagy Linux ARM64-re (aarch64), a macOS-felhasználók és az ARM64 Linux-felhasználók (például az Asahi Linuxot futtató Raspberry Pi vagy az Apple Silicon), ha kockával rendelkeznek, a lejátszójukat a következőhöz kell csatlakoztatniuk: 
  - An x64 Windows PC (Windows 10/11 64 bites), vagy
  - An x86_64 Linux PC (Ubuntu, Debian, Fedora, Arch 64 bites).

## Lépésről lépésre a hardver feloldási folyamata
  - A lejátszó leválasztása: Húzza ki teljesen a USB kábelt a lejátszóból és a számítógépből.
  - Erős kikapcsolás: Tartsa lenyomva a bekapcsológombot (vagy a bekapcsológombot + a hangerő csökkentése) 15 másodpercig, hogy megbizonyosodjon arról, hogy a lapkakészlet teljesen ki van kapcsolva, és ne ragadjon be az alacsony fogyasztású USB hurokba.
  - Indítsa el az Updater CE-t SP Flash Tool móddal: Válassza ki a készülék modelljét (pl. Innioasis Y1 vagy Innioasis Y2), és válassza ki Eredeti szoftver az állománypartíciók visszaállításához.
  - Telepítés/visszaállítás indítása: Kattintson Telepítés / visszaállítás az Updater CE-ben. Várja meg, amíg az állapotjelző üzenet meg nem jelenik Játékosra várva...
  - Helyezze be a USB kábelt a BROM indításához: Amíg az eszköz KI van kapcsolva, csatlakoztassa a USB kábelt közvetlenül a nagy sebességű alaplap USB portjához (kerülje a tápellátás nélküli USB hubokat).
  - A rendszer észleli a MediaTek VCOM portot, lenyomja a letöltési ügynököt (DA), átírja a partíciós táblákat, és tisztán visszaállítja az összes firmware lemezképet.

## Permutációk modell és operációs rendszer szerint

| Modell | Sikertelen platform | Javasolt helyreállítási beállítások | Motor és üzemmód |
| --- | --- | --- | --- |
| Innioasis Y1 | macOS (Apple Silicon / Intel) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y1 Részvény ROM |
| Innioasis Y1 | Linux ARM64 / x86_64 | Linux x86_64 vagy Windows x64 PC | SP Flash Tool + Közösségi DA |
| Innioasis Y2 | macOS (MTK-kliens leállt) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y2 Scatter Recovery |
| Innioasis G1 / G3 / G5 | macOS / Linux MTKclient | Windows x64 PC VCOM illesztőprogramokkal | SP Flash Tool + Gyári firmware |
| Mechen H1 / Timmkoo A5 | Bármilyen platform | Windows x64 vagy Linux x86_64 PC | SP Flash Tool + Scatter fájl |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
