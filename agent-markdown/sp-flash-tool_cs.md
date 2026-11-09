---
title: "SP Flash Tool pro Innioasis a Timmkoo hráče"
description: "Najděte SP Flash Tool dodávaný s Innioasis Updater na Windows a Linux, extrahujte rom.zip nebo rom_y2.zip a flashujte Innioasis Y1 nebo Y2 s odpovídajícím rozptylovým souborem."
language: "cs"
source: "https://innioasis.app/sp-flash-tool_cs.html"
---

# SP Flash Tool pro Innioasis a Timmkoo hráče

Manuální blikání

# Nástroj Flash pro hráče Innioasis a Timmkoo

SP Flash Tool je součástí Innioasis Updater je zapnutý [Windows](drivers_cs.html#windows) a [Linux](drivers_cs.html#linux). Už to máš. Tato příručka ukazuje bezpečný způsob použití na Innioasis Y1 nebo Y2 a cestu Updater pro Timmkoo hráče.[Vraťte se k příručce Updater](guide_cs.html)[Firmware ke stažení](firmware_cs.html)[Řešení problémů](troubleshooting_cs.html)

Začít s Innioasis Updater

## Updater provede celou práci v jednom průchodu

Updater provede většinu instalací v jednom průchodu. Vyberte software, postupujte podle kroků a máte hotovo. Také vám řekne, kdy dojde k opravě nebo novému vydání. SP Flash Tool je součástí Updater's Toolkit pro výjimečné případy, kdy Updater nemůže dokončit. Níže uvedené kroky jsou výjimkou.

## K čemu je tento nástroj

Updater za vás flashne přehrávač. SP Flash Tool je stejný motor bez ochranných lišt. Použijte jej, když se Updater nespustí, když se přehrávač nepřipojí, nebo když se zorientujete v rozptylovém souboru.Nejprve zkuste Updater. Pro většinu instalací a většinu obnovení platí průvodce [Trasa aktualizace](guide_cs.html) je bezpečnější volba. Použijte SP Flash Tool, když víte, proč jej potřebujete, a mějte připravenou nabitou baterii a datový kabel USB.

## Flash nástroj pro Innioasis hráče

Innioasis Updater je flashový nástroj pro Innioasis hráče. Instaluje oficiální software, aktualizuje a obnovuje balíčky prostřednictvím toku přizpůsobeného modelu a uchovává vaši hudbu a nastavení.

### Innioasis Y1 flash nástroj

Vyberte vydání Y1 v Updater a poté připojte vypnutý přehrávač, až se aplikace zeptá. Stejné Y1 balíčky fungují s SP Flash Tool, když potřebujete ruční cestu.

### Innioasis Y2 flash nástroj

Vyberte vydání uvedené pro Y2. Balíčky Y2 nejsou zaměnitelné s balíky Y1, takže než začnete, zkontrolujte model.

## Flash nástroj pro Timmkoo hráče

Timmkoo hráči používají stejný postup instalace Updater. Čte balíky ZIP a RAR Timmkoo přímo, takže nepotřebujete samostatný flash nástroj nebo rozptylový soubor.

### Timmkoo Q5 flash nástroj

Vyberte model Q5 v Updater, vyberte balíček Timmkoo, poté spusťte Install / Restore a po výzvě připojte přehrávač.

### Timmkoo Q3 a Q3E blesk

Záznam Q3 pokrývá Q3 a Q3E podobně. Updater vybere odpovídající soubory z balíčku, který projekt publikuje.

### Timmkoo A5 flash nástroj

Před výběrem balíčku vyberte model A5 a poté postupujte podle stejné výzvy k instalaci.

## Kam to Updater dává

SP Flash Tool se dodává s instalační složkou Updater, nikoli jako samostatný soubor ke stažení. Otevřete ji odtud, když ji budete potřebovat.

### Windows

Otevřete instalační složku Updater a spusťte `flash_tool.exe`. Složka je obvykle pod `%LOCALAPPDATA%\Innioasis Updater`. Některá nastavení obsahují složku Toolkit se zástupcem SP Flash Tool.

### Linux

Spusťte balíček `flash_tool` binární ve složce aplikace Updater na x86 / x86_64. Instalační program projektu připraví USB oprávnění s pravidly udev, takže přehrávač by se měl objevit po připojení.

### macOS

SP Flash Tool není součástí balíčku pro macOS. Updater tam místo toho používá cestu MTKClient. Použijte [řízená instalace](guide_cs.html) na počítači Mac a ponechte SP Flash Tool pro počítač se systémem Windows nebo Linux.

Nástroj je dodáván s agentem stahování MediaTek a konfigurací specifickou pro model, takže nemusíte shromažďovat DA nebo rozhazovat soubory odjinud.

## Připravte firmware
  - Uchopte vydání, které chcete [Firmware ke stažení](firmware_cs.html). Vyberte si `rom.zip` pro Y1 nebo `rom_y2.zip` pro Y2.
  - Extrahujte ZIP do vlastní složky. Windows může použít Extrahovat vše. V systému Linux použijte správce archivu nebo `unzip` v terminálu.
  - Zkontrolujte, zda je rozptylový soubor v extrahované složce. Obvykle se jmenuje `MT6572_Android_scatter.txt` pro Y1 balíčky a `MT6582_Android_scatter_def.txt` pro Y2 balíčky, i když vydání jej může pojmenovat podle svého projektu.
Udržujte modely odděleně. Bod Y1 popisuje zařízení MT6572 a bod Y2 popisuje zařízení MT6582. Blikání se špatnou je způsob, jak se hráči zhroutí. Pokud rozptyl uvnitř ZIP neodpovídá vašemu modelu, zastavte se a použijte místo toho balíček uvedený pro váš model.

## Vložte rozptylku a blesk
  - Otevřete SP Flash Tool z instalační složky Updater.
  - Na kartě Stáhnout klikněte na Vyberte si vedle položky Scatter-loading File a vyberte bodový soubor z extrahované složky. Seznam oddílů se vyplní.
  - Ponechte režim blesku zapnutý Pouze ke stažení pokud záměrně neprovádíte úplné zotavení, které potřebuje Upgrade firmwaru.
  - Klikněte Stáhnout. Nástroj počká na hráče.
  - Úplně vypněte přehrávač a poté připojte datový kabel USB. Položte přehrávač a nehýbejte s ním.
  - Počkejte na zelenou značku zaškrtnutí. Teprve poté odpojte kabel a spusťte přehrávač.

Dodržujte stejná USB pravidla pro kabel a časování jako u naváděné trasy: datový kabel, žádný rozbočovač a připojte se, až bude nástroj připraven.

## Pokud nebliká
  - Zkontrolujte, zda rozptyl a ZIP odpovídají modelu vytištěnému na přehrávači.
  - Před připojením se ujistěte, že je přehrávač zcela vypnutý.
  - V systému Windows potvrďte nainstalovaný ovladač MediaTek s nastavením Updater; na Linuxu potvrďte pravidla udev z instalačního programu projektu.
  - Kabel znovu připojte, až když nástroj čeká. Port race může vyžadovat úplné odpojení a obnovení Stáhnout klikněte.

Pro cokoliv nad rámec toho otevřete [odstraňování problémů](troubleshooting_cs.html). A pamatujte: Updater je stále normální cesta a [Y1](guides/restore-original-y1.html) a [Y2](guides/restore-original-y2.html) používají to také průvodci obnovení.

## Bylo to užitečné?

Vaše odpověď pomáhá zlepšit tuto příručku.Ano, přišlo mi to užitečnéJeště ne[Dejte nám vědět, jak se můžeme zlepšit](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
