---
title: "Innioasis Y1 och Y2 USB förare | Windows-drivrutin och Linux-behörigheter - Innioasis Updater"
description: "Konfigurera din dator för Innioasis Updater: Windows MediaTek drivrutin och Linux USB behörigheter – plus kabel- och timingfixar."
language: "sv"
source: "https://innioasis.app/drivers_sv.html"
---

# Innioasis Y1 och Y2 USB förare | Windows-drivrutin och Linux-behörigheter - Innioasis Updater

Datorinstallation

# Gör datorn redo innan spelaren.

De flesta anslutningsproblem kommer från drivrutinen, behörigheter, kabel eller timing. Windows behöver drivrutinen MediaTek installerad. Linux behöver rätt USB behörigheter. Hitta din plattform nedan.[Hämta Updater CE](guide_sv.html#platform)[Felsökning](troubleshooting_sv.html)

## Windows
  - Ladda ner MediaTek drivrutinsinstallationsprogrammet nedan.
  - Kör installationsprogrammet och låt Windows installera drivrutinen.
  - Starta om datorn.
  - Öppna Updater CE och vänta på anslutningsprompten innan du kopplar in den avstängda spelaren.

Vissa Windows-system blockerar drivrutinen genom Core-isolering (minnesintegritet). Om Updater CE fortfarande inte kan se spelaren efter en omstart, stäng av minnesintegritet i Windows Security, starta om och installera om drivrutinen. Slå på inställningen igen när du är klar om ditt system tillåter det.

Windows startar inte appen? Om Windows Security eller Smart App Control stoppar Updater CE från att öppna, öppna Inställningar (tryck Win + I) → Sekretess & säkerhet → Windows Security → App- och webbläsarkontroll → Smart App Control-inställningar och ställ in den på Av. Smart App Control påverkar för närvarande populära applikationer som Epic Overlay Service (används av Fortnite) — Updater CE är säker och verifierad att använda. För att återaktivera senare, ställ in `VerifiedAndReputablePolicyState` till `1` (På) eller `2` (Utvärderingsläge) under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` i Registereditorn.[Ladda ner drivrutinen för Windows](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Tillbaka till huvudguiden](guide_sv.html#windows) · [Nedladdning av programvara](firmware_sv.html)

## Linux USB behörigheter

Linux behöver ditt användarkonto för att tillåtas prata med MediaTek USB-chippet inuti spelaren. Updater CE löser vanligtvis detta under installationen, och samma behörighet täcker SP Flash Tool, så behandla detta som ett fix-it-steg snarare än ett normalt steg.
  - Kör Updater CE som din vanliga användare, inte som root. Installationsprogrammet ber om administratörsåtkomst endast när det behöver det.
  - Kontrollera att spelaren överhuvudtaget syns. Stäng av spelaren, anslut kabeln och kör kommandot lsusb i en terminal. En ansluten spelare dyker upp som en MediaTek-enhet med leverantörs-ID 0e8d.
`lsusb`
  - Om det visas i lsusb men Innioasis Updater CE eller SP Flash Tool säger att behörighet nekas eller inte kan öppna porten, saknar din användare åtkomst till USB-enheten. Samma udev-regel täcker båda verktygen, så lägg till en som låter användargruppen läsa den.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Spara den raden i en ny fil som heter /etc/udev/rules.d/51-innioasis.rules och kör sedan:`sudo udevadm control --reload && sudo udevadm trigger`
  - Koppla ur spelaren helt, anslut den igen och försök installera igen.
  - Om SP Flash Tool rapporterar en serietillstånd eller portrace, koppla ur helt och anslut bara när du uppmanas att göra det.
Improvisera inte blixtförskjutningar.Om du flyttar till ett manuellt återställningsverktyg, använd filerna och den modellspecifika konfigurationen som levererades med projektet.

[Tillbaka till huvudguiden](guide_sv.html#linux) · [Nedladdning av programvara](firmware_sv.html) · [SP Flash Tool guide](sp-flash-tool_sv.html)

## Kabel och tidtagning
  - Använd en känd USB datakabel.
  - Undvik nav under felsökning.
  - Stäng av rätt modell helt.
  - Anslut endast vid uppmaningen.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
