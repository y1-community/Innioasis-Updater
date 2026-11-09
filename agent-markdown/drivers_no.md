---
title: "Innioasis Y1 og Y2 USB drivere | Windows-driver og Linux-tillatelser - Innioasis Updater"
description: "Konfigurer datamaskinen din for Innioasis Updater: Windows MediaTek driver og Linux USB tillatelser – pluss kabel- og tidskorrigeringer."
language: "no"
source: "https://innioasis.app/drivers_no.html"
---

# Innioasis Y1 og Y2 USB drivere | Windows-driver og Linux-tillatelser - Innioasis Updater

Datamaskinoppsett

# Gjør datamaskinen klar før spilleren.

De fleste tilkoblingsproblemer kommer fra driveren, tillatelser, kabel eller timing. Windows trenger MediaTek-driveren installert. Linux trenger de riktige USB tillatelsene. Finn din plattform nedenfor.[Få Updater CE](guide_no.html#platform)[Feilsøking](troubleshooting_no.html)

## Windows
  - Last ned MediaTek driverinstallasjonsprogrammet nedenfor.
  - Kjør installasjonsprogrammet og la Windows installere driveren.
  - Start datamaskinen på nytt.
  - Åpne Updater CE og vent på tilkoblingsmeldingen før du kobler til den avslåtte spilleren.

Noen Windows-systemer blokkerer driveren gjennom kjerneisolering (minneintegritet). Hvis Updater CE fortsatt ikke kan se spilleren etter en omstart, slå av minneintegritet i Windows Security, start på nytt og installer driveren på nytt. Slå på innstillingen igjen når du er ferdig hvis systemet tillater det.

Vil ikke Windows starte appen? Hvis Windows Security eller Smart App Control stopper Updater CE fra å åpne, åpne Innstillinger (trykk Win + I) → Personvern og sikkerhet → Windows Security → App- og nettleserkontroll → Smart App Control-innstillinger og sett den til Av. Smart App Control påvirker for tiden populære applikasjoner som Epic Overlay Service (brukt av Fortnite) - Updater CE er trygg og verifisert å bruke. For å reaktivere senere, still inn `VerifiedAndReputablePolicyState` til `1` (På) eller `2` (Evalueringsmodus) under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` i Registerredigering.[Last ned Windows-driver](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Tilbake til hovedguiden](guide_no.html#windows) · [Programvarenedlastinger](firmware_no.html)

## Linux USB tillatelser

Linux trenger brukerkontoen din for å få lov til å snakke med MediaTek USB-brikken inne i spilleren. Updater CE ordner vanligvis dette under installasjonen, og den samme tillatelsen dekker SP Flash Tool, så behandle dette som et fix-it-trinn i stedet for et normalt stadium.
  - Kjør Updater CE som din vanlige bruker, ikke som root. Installasjonsprogrammet ber om administratortilgang bare når det trenger det.
  - Sjekk at spilleren er sett i det hele tatt. Slå av spilleren, koble til kabelen og kjør lsusb-kommandoen i en terminal. En tilkoblet spiller vises som en MediaTek enhet med leverandør-ID 0e8d.
`lsusb`
  - Hvis det vises i lsusb, men Innioasis Updater CE eller SP Flash Tool sier at tillatelse nektes eller ikke kan åpne porten, mangler brukeren tilgang til USB-enheten. Den samme udev-regelen dekker begge verktøyene, så legg til en som lar brukergruppen lese den.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Lagre den linjen i en ny fil som heter /etc/udev/rules.d/51-innioasis.rules, og kjør deretter:`sudo udevadm control --reload && sudo udevadm trigger`
  - Koble spilleren helt fra, koble den til igjen og prøv å installere på nytt.
  - Hvis SP Flash Tool rapporterer en serietillatelse eller portrace, koble fra helt og koble til igjen når du blir bedt om det.
Ikke improviser flash-offsets.Hvis du flytter til et manuelt gjenopprettingsverktøy, bruk filene og modellspesifikke konfigurasjonen som ble levert med prosjektet.

[Tilbake til hovedguiden](guide_no.html#linux) · [Programvarenedlastinger](firmware_no.html) · [SP Flash Tool guide](sp-flash-tool_no.html)

## Kabel og timing
  - Bruk en kjent USB datakabel.
  - Unngå nav under feilsøking.
  - Slå den riktige modellen helt av.
  - Koble kun til når du blir bedt om det.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
