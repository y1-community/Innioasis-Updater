---
title: "SP Flash Tool for Innioasis og Timmkoo spillere"
description: "Finn SP Flash Tool sammen med Innioasis Updater på Windows og Linux, pakk ut rom.zip eller rom_y2.zip, og flash en Innioasis Y1 eller Y2 med den matchende scatter-filen."
language: "no"
source: "https://innioasis.app/sp-flash-tool_no.html"
---

# SP Flash Tool for Innioasis og Timmkoo spillere

Manuell blinking

# Flash-verktøy for Innioasis og Timmkoo spillere

SP Flash Tool kommer i Innioasis Updater på [Windows](drivers_no.html#windows) og [Linux](drivers_no.html#linux). Du har det allerede. Denne veiledningen viser den sikre måten å bruke den på en Innioasis Y1 eller Y2, og Updater-ruten for Timmkoo spillere.[Gå tilbake til Updater-veiledningen](guide_no.html)[Fastvarenedlastinger](firmware_no.html)[Feilsøking](troubleshooting_no.html)

Start med Innioasis Updater

## Updater gjør hele jobben i ett pass

Updater gjør de fleste installasjoner i ett pass. Velg programvaren, følg trinnene, og du er ferdig. Den forteller deg også når en reparasjon eller en ny utgivelse lander. SP Flash Tool er inne i Updater's Toolkit for de sjeldne tilfellene Updater ikke kan fullføre. Trinnene nedenfor er unntaket.

## Hva er dette verktøyet til

Updater blinker spilleren for deg. SP Flash Tool er den samme motoren, uten rekkverk. Bruk den når Updater ikke starter, når spilleren ikke vil koble til, eller når du kjenner deg rundt i en scatter-fil.Prøv Updater først. For de fleste installasjoner og de fleste gjenopprettinger, veiledet [Oppdateringsrute](guide_no.html) er det tryggere valget. Bruk SP Flash Tool når du vet hvorfor du trenger det, og hold et oppladet batteri pluss en USB datakabel klar.

## Flash-verktøy for Innioasis spillere

Innioasis Updater er flashverktøyet for Innioasis spillere. Den installerer offisiell programvare, oppdaterer og gjenoppretter pakker gjennom modelltilpasset flyt, og den beholder musikken og innstillingene dine.

### Innioasis Y1 flashverktøy

Velg Y1-versjonen i Updater, og koble deretter til den avslåtte spilleren når appen spør. De samme Y1-pakkene fungerer med SP Flash Tool når du trenger den manuelle ruten.

### Innioasis Y2 flashverktøy

Velg en utgivelse som er oppført for Y2. Y2-pakker kan ikke byttes ut med Y1-pakker, så sjekk modellen før du starter.

## Flash-verktøy for Timmkoo spillere

Timmkoo spillere bruker samme installasjonsflyt for Updater. Den leser Timmkoos ZIP- og RAR-pakker direkte, så du trenger ikke et separat flashverktøy eller scatter-fil.

### Timmkoo Q5 blitsverktøy

Velg Q5-modellen i Updater, velg Timmkoo-pakken, kjør deretter Installer / Gjenopprett og koble til spilleren når du blir bedt om det.

### Timmkoo Q3 og Q3E blitsverktøy

Q3-oppføringen dekker både Q3 og Q3E. Updater velger de samsvarende filene fra pakken prosjektet publiserer.

### Timmkoo A5 blitsverktøy

Velg A5-modellen før du velger en pakke, og følg deretter den samme installasjonsmeldingen.

## Hvor Updater sier det

SP Flash Tool leveres med Updater-installasjonsmappen, ikke som en separat nedlasting. Åpne den derfra når du trenger den.

### Windows

Åpne Updater-installasjonsmappen og kjør `flash_tool.exe`. Mappen er vanligvis under `%LOCALAPPDATA%\Innioasis Updater`. En Toolkit-mappe med en SP Flash Tool-snarvei er inkludert i noen oppsett.

### Linux

Kjør den medfølgende `flash_tool` binær i Updater-appmappen på x86 / x86_64. Prosjektinstallasjonsprogrammet forbereder USB-tillatelser med udev-regler, så spilleren skal vises når den er tilkoblet.

### macOS

SP Flash Tool er ikke samlet på macOS. Updater bruker MTKClient-ruten dit i stedet. Bruk [veiledet installasjon](guide_no.html) på en Mac og behold SP Flash Tool for en Windows- eller Linux-maskin.

Verktøyet leveres med MediaTek nedlastingsagent og modellspesifikk konfigurasjon, slik at du ikke trenger å samle inn DA eller spre filer fra andre steder.

## Klargjør fastvaren
  - Ta tak i utgivelsen du vil ha fra [Fastvarenedlastinger](firmware_no.html). Velg `rom.zip` for en Y1 eller `rom_y2.zip` for en Y2.
  - Pakk ut ZIP i sin egen mappe. Windows kan bruke Extract All. På Linux bruker du arkivbehandlingen eller `unzip` i en terminal.
  - Sjekk at scatter-filen er i den utpakkede mappen. Det er vanligvis navngitt `MT6572_Android_scatter.txt` for Y1 pakker og `MT6582_Android_scatter_def.txt` for Y2-pakker, selv om en utgivelse kan navngi den etter prosjektet.
Hold modellene adskilt. Y1-spredningen beskriver en MT6572-enhet og Y2-spredningen beskriver en MT6582-enhet. Å blinke med feil er hvordan spillere blir murt. Hvis spredningen i ZIP-en ikke samsvarer med modellen din, stopp og bruk en pakke som er oppført for modellen din i stedet.

## Last inn scatter og blits
  - Åpne SP Flash Tool fra Updater-installasjonsmappen.
  - I kategorien Last ned klikker du Velg ved siden av Scatter-loading File og velg scatter-filen fra den utpakkede mappen. Partisjonslisten vil fylles ut.
  - La blitsmodusen være på Kun nedlasting med mindre du bevisst gjør en full restitusjon, som trenger Fastvareoppgradering.
  - Klikk Last ned. Verktøyet vil vente på spilleren.
  - Slå spilleren helt av, og koble deretter til USB-datakabelen. Sett ned spilleren og ikke flytt den.
  - Vent på det grønne merket. Først da kobler du fra kabelen og starter spilleren.

Behold de samme USB kabel- og tidsreglene som den guidede ruten: en datakabel, ingen hub, og koble til bare når verktøyet er klart.

## Hvis den ikke blinker
  - Sjekk at scatter og ZIP samsvarer med modellen som er trykt på spilleren.
  - Bekreft at spilleren er helt slått av før du kobler til.
  - På Windows, bekreft at MediaTek-driveren er installert med Updater-oppsettet; på Linux, bekreft udev-reglene fra prosjektinstallasjonsprogrammet.
  - Koble til kabelen bare når verktøyet venter. Et havneløp kan trenge en full plugg og en fresh Last ned klikk.

For alt utover det, åpen [feilsøking](troubleshooting_no.html). Og husk: Updater er fortsatt normal rute, og [Y1](guides/restore-original-y1.html) og [Y2](guides/restore-original-y2.html) gjenopprettingsguider bruker det også.

## Var dette nyttig?

Svaret ditt bidrar til å forbedre denne veiledningen.Ja, jeg fant det nyttigIkke ennå[Fortell oss hvordan vi kan forbedre oss](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
