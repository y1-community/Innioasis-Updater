---
title: "Wi-Fi, Bluetooth és FM rádió beállítása a következőhöz: Reborn (Y2Linux) - Innioasis Frissítő"
description: "Rövid telepítés utáni útmutató a Reborn-hoz (Y2Linux / Y2Reborn) a Innioasis Y2 webhelyen: másolja ki a system.img fájlt, majd állítsa be a Wi-Fi-t, a Bluetooth-t és az FM-rádiót."
language: "hu"
source: "https://innioasis.app/y2reborn_wifibt_hu.html"
---

# Wi-Fi, Bluetooth és FM rádió beállítása a következőhöz: Reborn (Y2Linux) - Innioasis Frissítő

Innioasis Y2 · Reborn Telepítés után

# Wi-Fi, Bluetooth és FM rádió beállítása.

Másoljon egy fájlt a lejátszóra. Reborn intézi a többit.[A system.img letöltése (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Telepítési útmutató](guides/reborn-y2linux-y2.html)[Miért Y2Reborn?](reborn-y2linux-benefits_hu.html)

## Miért ez a fájl?

A Wi-Fi-hez, Bluetooth-hoz és FM-rádióhoz öt MediaTek firmware-modulra van szükség, amelyeket Reborn nem szállíthat. Bent vannak a hivatalos Y2 `system.img`. Reborn egyszer kicsomagolja őket, ellenőrzi és törli a fájlt.

## Beállítás
  - A system.img letöltése

Töltse le a v3.2.0 FM-et `system.img` a számítógépére.[ A system.img letöltése ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Boot Reborn egyszer

Kapcsolja be a lejátszót. Várj Tárhely beállítása befejezéséhez, majd egyszer indítsa újra.
  - Csatlakoztassa a számítógéphez

Használjon USB adatkábelt. A lejátszó így jelenik meg Belső tárhely.Mac-en?

Telepítés [OpenMTP](https://openmtp.ganeshrvel.com/) a lejátszó böngészéséhez. A Windows és a Linux automatikusan csatlakoztatja.
  - Másolja a system.img fájlt a firmware-be

Hozzon létre egy mappát, melynek neve `Firmware` az Internal Storage gyökerében. Másolás `system.img` bele.
  - Várja meg, amíg a beállítás befejeződik

Reborn automatikusan telepíti a rádió firmware-ét és törli `system.img`. Ez körülbelül 10-20 másodpercet vesz igénybe. Várj A Wi-Fi és a Bluetooth készen áll.
  - Csatlakoztassa a Wi-Fi-t, a Bluetooth-ot és az FM-rádiót
    - Wi-Fi: Beállítások → Rendszer → Hálózat → Wi-Fi. Válassza ki a 2,4 GHz-es hálózatot.
    - Bluetooth: Helyezze a fejhallgatót párosítási módba. Beállítások → Bluetooth → válassza ki őket.
    - FM rádió: Csatlakoztassa a vezetékes fejhallgatót antennaként, majd nyissa meg az FM rádiót.

  - Frissítés Wi-Fi-n keresztül

A jövőbeli Reborn frissítések telepítése a Beállítások → Rendszer → Szoftverfrissítés menüpontból. A rádió firmware-je a helyén marad.

## Hasznos volt ez az útmutató?

Hasznosnak találta ezt a telepítés utáni beállítási útmutatót? Igen, segített! [ Segítségre van szüksége a következőhöz: Discord ](https://discord.gg/zHrT2zrcek) Köszönjük visszajelzését! Élvezze a vezeték nélküli zenehallgatást a Y2Reborn készüléken.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
