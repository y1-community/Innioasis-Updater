---
title: "Wi-Fi, Bluetooth och FM-radioinställningar för Reborn (Y2Linux) - Innioasis Updater"
description: "Kort efterinstallationsguide för Reborn (Y2Linux / Y2Reborn) på Innioasis Y2: kopiera system.img, ställ sedan in Wi-Fi, Bluetooth och FM-radio."
language: "sv"
source: "https://innioasis.app/y2reborn_wifibt_sv.html"
---

# Wi-Fi, Bluetooth och FM-radioinställningar för Reborn (Y2Linux) - Innioasis Updater

Innioasis Y2 · Reborn Efterinstallation

# Konfigurera Wi-Fi, Bluetooth och FM-radio.

Kopiera en fil till din spelare. Reborn sköter resten.[Ladda ner system.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Installationsguide](guides/reborn-y2linux-y2.html)[Varför Y2Reborn?](reborn-y2linux-benefits_sv.html)

## Varför denna fil?

Wi-Fi, Bluetooth och FM-radio behöver fem MediaTek firmwaremoduler som Reborn inte kan levereras. De är inne på den officiella Y2 `system.img`. Reborn extraherar dem en gång, kontrollerar dem och tar bort filen.

## Inställning
  - Ladda ner system.img

Ladda ner v3.2.0 FM `system.img` till din dator.[ Ladda ner system.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Starta Reborn en gång

Slå på spelaren. Vänta på Konfigurera lagring för att avsluta och starta om den en gång.
  - Anslut till din dator

Använd en USB datakabel. Spelaren visas som Intern lagring.På en Mac?

Installera [ÖppnaMTP](https://openmtp.ganeshrvel.com/) för att bläddra i spelaren. Windows och Linux monterar den automatiskt.
  - Kopiera system.img till Firmware

Skapa en mapp som heter `Firmware` vid roten av intern lagring. Kopiera `system.img` in i den.
  - Vänta tills installationen är klar

Reborn installerar radions firmware automatiskt och tar bort `system.img`. Detta tar cirka 10–20 sekunder. Vänta på Wi-Fi och Bluetooth är redo.
  - Anslut Wi-Fi, Bluetooth och FM-radio
    - Wi-Fi: Inställningar → System → Nätverk → Wi-Fi. Välj ditt 2,4 GHz-nätverk.
    - Bluetooth: Sätt dina hörlurar i parningsläge. Inställningar → Bluetooth → välj dem.
    - FM-radio: Anslut trådbundna hörlurar som antenn och öppna sedan FM-radio.

  - Uppdatera via Wi-Fi

Framtida Reborn uppdateringar installeras från Inställningar → System → Programuppdatering. Din radiofirmware förblir kvar.

## Var den här guiden till hjälp?

Tyckte du att den här installationsguiden efter installation var användbar? Ja, det hjälpte! [ Behöver hjälp med Discord ](https://discord.gg/zHrT2zrcek) Tack för din feedback! Njut av din trådlösa lyssning på Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
