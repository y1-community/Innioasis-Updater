---
title: "Innioasis Y1 og Y2 USB drivere | Windows-driver og Linux-tilladelser - Innioasis Updater"
description: "Konfigurer din computer til Innioasis Updater: Windows MediaTek driver og Linux USB tilladelser – plus kabel- og timing rettelser."
language: "da"
source: "https://innioasis.app/drivers_da.html"
---

# Innioasis Y1 og Y2 USB drivere | Windows-driver og Linux-tilladelser - Innioasis Updater

Computer opsætning

# Gør computeren klar før afspilleren.

De fleste forbindelsesproblemer kommer fra driveren, tilladelser, kabel eller timing. Windows skal have MediaTek-driveren installeret. Linux har brug for de rigtige USB tilladelser. Find din platform nedenfor.[Få Updater CE](guide_da.html#platform)[Fejlfinding](troubleshooting_da.html)

## Windows
  - Download MediaTek driverinstallationsprogrammet nedenfor.
  - Kør installationsprogrammet, og lad Windows installere driveren.
  - Genstart computeren.
  - Åbn Updater CE, og vent på tilslutningsprompten, før du tilslutter den slukkede afspiller.

Nogle Windows-systemer blokerer driveren gennem Core-isolation (hukommelsesintegritet). Hvis Updater CE stadig ikke kan se afspilleren efter en genstart, skal du slå Hukommelsesintegritet fra i Windows Security, genstarte og geninstallere driveren. Slå indstillingen til igen, når du er færdig, hvis dit system tillader det.

Vil Windows ikke starte appen? Hvis Windows Security eller Smart App Control forhindrer Updater CE i at åbne, skal du åbne Indstillinger (tryk Win + I) → Privatliv og sikkerhed → Windows Security → App og browser kontrol → Indstillinger for Smart App Control og sæt den til Slukket. Smart App Control påvirker i øjeblikket populære applikationer som Epic Overlay Service (brugt af Fortnite) - Updater CE er sikker og verificeret at bruge. Indstil for at genaktivere senere `VerifiedAndReputablePolicyState` til `1` (Til) eller `2` (Evalueringstilstand) under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` i Registreringseditor.[Download Windows-driver](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Tilbage til hovedguiden](guide_da.html#windows) · [Software downloads](firmware_da.html)

## Linux USB tilladelser

Linux har brug for din brugerkonto for at få lov til at tale med MediaTek USB chippen inde i afspilleren. Updater CE ordner normalt dette under installationen, og den samme tilladelse dækker SP Flash Tool, så behandl dette som et fix-it-trin frem for et normalt trin.
  - Kør Updater CE som din normale bruger, ikke som root. Installationsprogrammet beder kun om administratoradgang, når det har brug for det.
  - Tjek, at afspilleren overhovedet er set. Sluk for afspilleren, tilslut kablet, og kør lsusb-kommandoen i en terminal. En tilsluttet afspiller vises som en MediaTek-enhed med leverandør-id'et 0e8d.
`lsusb`
  - Hvis det vises i lsusb, men Innioasis Updater CE eller SP Flash Tool siger tilladelse nægtet eller kan ikke åbne porten, mangler din bruger adgang til USB-enheden. Den samme udev-regel dækker begge værktøjer, så tilføj en, der lader brugergruppen læse den.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Gem den linje i en ny fil med navnet /etc/udev/rules.d/51-innioasis.rules, og kør derefter:`sudo udevadm control --reload && sudo udevadm trigger`
  - Tag afspilleren helt ud, sæt den i igen, og prøv at installere igen.
  - Hvis SP Flash Tool rapporterer en seriel tilladelse eller portrace, skal du trække stikket helt ud og kun tilslutte igen, når du bliver bedt om det.
Undlad at improvisere flash offsets.Hvis du flytter til et manuel gendannelsesværktøj, skal du bruge de filer og den modelspecifikke konfiguration, der blev leveret med projektet.

[Tilbage til hovedguiden](guide_da.html#linux) · [Software downloads](firmware_da.html) · [SP Flash Tool guide](sp-flash-tool_da.html)

## Kabel og timing
  - Brug et kendt USB datakabel.
  - Undgå hubs under fejlfinding.
  - Sluk helt for den korrekte model.
  - Tilslut kun ved prompten.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
