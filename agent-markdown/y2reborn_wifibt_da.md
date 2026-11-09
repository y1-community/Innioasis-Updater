---
title: "Opsætning af Wi-Fi, Bluetooth og FM-radio for Reborn (Y2Linux) - Innioasis Updater"
description: "Kort efterinstallationsvejledning til Reborn (Y2Linux / Y2Reborn) på Innioasis Y2: kopier system.img, og opsæt derefter Wi-Fi, Bluetooth og FM-radio."
language: "da"
source: "https://innioasis.app/y2reborn_wifibt_da.html"
---

# Opsætning af Wi-Fi, Bluetooth og FM-radio for Reborn (Y2Linux) - Innioasis Updater

Innioasis Y2 · Reborn Efterinstallation

# Konfigurer Wi-Fi, Bluetooth og FM-radio.

Kopier en fil til din afspiller. Reborn klarer resten.[Download system.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Installationsvejledning](guides/reborn-y2linux-y2.html)[Hvorfor Y2Reborn?](reborn-y2linux-benefits_da.html)

## Hvorfor denne fil?

Wi-Fi, Bluetooth og FM-radio har brug for fem MediaTek firmwaremoduler, som Reborn ikke kan sendes. De er inde i den officielle Y2 `system.img`. Reborn udpakker dem én gang, kontrollerer dem og sletter filen.

## Opsætning
  - Download system.img

Download v3.2.0 FM `system.img` til din computer.[ Download system.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Boot Reborn én gang

Tænd for afspilleren. Vent på Opsætning af lager for at afslutte, og genstart den en gang.
  - Tilslut til din computer

Brug et USB datakabel. Afspilleren vises som Intern opbevaring.På en Mac?

Installer [Åbn MTP](https://openmtp.ganeshrvel.com/) for at gennemse afspilleren. Windows og Linux monterer det automatisk.
  - Kopier system.img til firmware

Opret en mappe kaldet `Firmware` i roden af ​​intern lagring. Kopiér `system.img` ind i det.
  - Vent på, at opsætningen er færdig

Reborn installerer radiofirmwaren automatisk og sletter `system.img`. Dette tager omkring 10-20 sekunder. Vent på Wi-Fi og Bluetooth er klar.
  - Tilslut Wi-Fi, Bluetooth og FM-radio
    - Wi-Fi: Indstillinger → System → Netværk → Wi-Fi. Vælg dit 2,4 GHz-netværk.
    - Bluetooth: Sæt dine hovedtelefoner i parringstilstand. Indstillinger → Bluetooth → vælg dem.
    - FM radio: Tilslut kablede hovedtelefoner som antenne, og åbn derefter FM-radio.

  - Opdater via Wi-Fi

Fremtidige Reborn-opdateringer installeres fra Indstillinger → System → Softwareopdatering. Din radiofirmware bliver siddende.

## Var denne vejledning nyttig?

Fandt du denne opsætningsvejledning efter installationen nyttig? Ja, det hjalp! [ Brug for hjælp til Discord ](https://discord.gg/zHrT2zrcek) Tak for din feedback! Nyd din trådløse lytning på Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
