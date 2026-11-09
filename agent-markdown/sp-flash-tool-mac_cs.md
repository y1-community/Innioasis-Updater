---
title: "SP Flash Tool pro Mac · MediaTek Scatter Flashing Guide &amp; Alternatives"
description: "Jak používat SP Flash Tool na Macu pomocí Updater CE a procházet rozptýlené soubory pro flashování MediaTek zařízení, jako jsou Mechen H1, Innioasis Y1/Y2, Timmkoo a MP3 přehrávače a telefony MT6580/MT6572."
language: "cs"
source: "https://innioasis.app/sp-flash-tool-mac_cs.html"
---

# SP Flash Tool pro Mac · MediaTek Scatter Flashing Guide &amp; Alternatives

MediaTek Nástroje a multiplatformní blikání

# SP Flash Tool pro Mac: Kompletní průvodce a Scatter Browser

Funguje oficiální MediaTek SP Flash Tool na macOS? Zde je přesný stav, jak Aktualizátor CE poskytuje nativní MediaTek flashování na Mac a jak flashovat libovolný MediaTek MP3 přehrávač nebo chytrý telefon založený na rozptylu.

## Pravda o SP Flash Tool na macOS

MediaTek nikdy nevydal oficiální sestavení macOS Smart Phone Flash Tool (SP Flash Tool). Tento nástroj vždy existoval pouze jako 32bitová/64bitová aplikace pro Windows a binární x86_64 Linux. Emulace SP Flash Tool na macOS přes Wine nebo CrossOver se nezdaří, protože rozšíření jádra USB macOS neumožňují USB sériové předávání s přesností požadovanou během navázání spojení BROM.

Řešení:Aktualizátor CE překlenuje tuto propast spojením nativních flashovacích knihoven Apple Silicon a Intel macOS (prostřednictvím nízkoúrovňového protokolu MTKclient) spolu s automatickým zjišťováním rozptylu!

## Blikání libovolného MediaTek zařízení pomocí „Instalovat ze souboru“ (rozptylový prohlížeč)

Updater CE není omezen na Innioasis hráče. Můžete jej použít jako výkonný univerzální MediaTek rozptylový blikač pro jakékoli zařízení, které to vyžaduje SP Flash Tool v5 nebo starší:
  - Mechen H1 & H11: Přenosné HiFi přehrávače Android MT6580.
  - Timmkoo Q3, Q5, G1, A5: MediaTek digitální audio přehrávače s dotykovou obrazovkou.
  - Oilsky, Phueut, Luoran: MediaTek Hudební přehrávače MT6572 / MT6582.
  - Starší MediaTek chytré telefony a běžné telefony: Zařízení se systémem MT6572, MT6580, MT6582, MT6735, MT6737, MT6739, MT6753 a MT8163.

### Jak načíst vlastní soubory Scatter v Updater CE:
  - Stáhněte si archiv továrního firmwaru (`.zip` nebo `.rar`) nebo extrahujte jeho složku obsahující `*scatter*.txt` soubor.
  - V Updater CE vyberte Procházet soubory… na obrazovce výběru firmwaru.
  - Vyberte soubor bodového textu (např. `MT6580_Android_scatter.txt`) nebo balíček zip firmwaru.
  - Updater CE analyzuje offsety paměti, adresy oddílů (preloader, boot, recovery, systém, uživatelská data) a ověřuje integritu rozptylu.
  - Postupujte podle pokynů na obrazovce: vypněte zařízení a připojte kabel USB k blesku.

## Když potřebujete x64 počítač pro Unbricking

Zatímco macOS zvládá standardní flashování a vlastní ROM instalace čistě přes MTKclient, obnova po hlubokých selháních bootloop (kde byl oddíl s preloaderem vymazán nebo se neshodoval) vyžaduje úplné znovu sestavení tabulky oddílů SP Flash Tool.

Pokud na Macu narazíte na zasekávání chyb, přejděte na 64bitový Windows PC nebo x86_64 Linux pracovní stanici, vyberte Nastavení > Zobrazit pokročilá nastavení > Metoda blesku > SP Flash Toola flashujte tovární rozptylový balíček.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
