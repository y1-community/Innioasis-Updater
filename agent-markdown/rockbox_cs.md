---
title: "Jak nainstalovat Rockbox na váš Innioasis Y1 nebo Y2 - Innioasis Updater"
description: "Nainstalujte Rockbox na Innioasis Y1 nebo Y2 pomocí Updater: témata, stabilní vydání, Type A a Type B poznámky a jak poté obnovit původní software."
language: "cs"
source: "https://innioasis.app/rockbox_cs.html"
---

# Jak nainstalovat Rockbox na váš Innioasis Y1 nebo Y2 - Innioasis Updater

Rockbox odkaz

# Získání Rockbox na Y1 nebo Y2

Rockbox mění software přehrávače a otevírá hlubší rozhraní hudebního přehrávače, ovládání přehrávání, řazení a možnosti motivů. Instalace je vedena, ale Y1 a Y2 jsou samostatné cesty.[Rockbox dne Y1](guides/rockbox-y1.html)[Rockbox dne Y2](guides/rockbox-y2.html)[Proč Rockbox?](rockbox-benefits_cs.html)

## Co změní instalace

Rockbox je zakázkový software. Neodstraňuje to vaši možnost vrátit se do rozhraní akcií, když je k dispozici odpovídající originální softwarový balíček. Může zlepšit procházení hudby a přizpůsobení, ale funkce, rozlišení, výdrž baterie a kompatibilita témat závisí na sestavení.Nemíchejte modely. Vyberte Y1 pro přehrávač Y1 a Y2 pro přehrávač Y2. Podobně vypadající název vydání není dostatečným důkazem, že je balíček kompatibilní.

## Podívejte se na video

Video od Frawgeeyse. Zobrazuje cestu Innioasis Updater; použijte níže uvedené písemné kroky specifické pro model pro vaše Y1 nebo Y2.

Autor videa [Cristian Plaza](https://www.youtube.com/@CristianPlaza) (španělština), zobrazující Rockbox na Y1. Pro váš přehrávač použijte níže uvedené kroky specifické pro model.

## Sdílená trasa Updater
  - Nainstalujte Updater a nic nepřipojujte, dokud se zeptá.
  - Vyberte model vytištěný na přehrávači Model zařízení.
  - Vyberte si Rockbox v Software.
  - Vyberte si stabilní verzi, pokud záměrně netestujete noční sestavení.
  - Klikněte Nainstalovat / Obnovit, poté postupujte podle pokynů k vypnutí a připojení USB.
  - Odpojte se až po zprávě o úspěchu.

## 240p, 360p a motivy

Starší kolekce témat Rockbox mohou být vytvořeny pro 240p. Y1 komunitní sestavení také používá štítky kompatibility 360p. Před výběrem sestavení si přečtěte poznámky k vydání a zdroj motivu. Motiv vytvořený pro jedno rozlišení nebo softwarovou rodinu nemusí fungovat na jiném.[Procházejte témata komunity](https://themes.innioasis.app/?lang=cs)[Tématické nástroje](https://themes.innioasis.app/?lang=cs)

## Návrat k původnímu softwaru

Vyberte znovu stejný model, vyberte Původní software, vyberte stabilní verzi a použijte Nainstalovat / Obnovit. Pokud k chybě došlo před výzvou USB, zkontrolujte počítač a extrahované soubory. Pokud byl přehrávač detekován, ale blesk selhal, začněte s [odstraňování problémů](troubleshooting_cs.html).[Y1 obnovit](guides/restore-original-y1.html)[Y2 obnovit](guides/restore-original-y2.html)

## Časté dotazyPřeinstaloval jsem Rockbox a nic to nevyřešilo.

Přeinstalování Rockbox zapíše stejné sestavení přes stejné soubory, takže nemůže resetovat věci, které Rockbox uchovává na MicroSD. Pokud je problém v nefunkčním nastavení, motivu, seznamu skladeb nebo databázi na kartě, přeinstalací se to nevymaže. Spolehlivý reset vymaže `.rockbox` složka z MicroSD — Rockbox vytvoří novou složku při příštím spuštění.
  - Úplně vypněte přehrávač a vyjměte kartu MicroSD nebo připojte přehrávač jako jednotku USB.
  - Zobrazte skryté soubory v počítači, aby byla složka viditelná. Jak zobrazit skryté souboryZobrazte soubory dot na vašem počítačiWindows: v Průzkumníku souborů otevřete Zobrazit karta a zaškrtnutí Skryté položky.macOS: ve Finder pressu Cmd+Shift+. pro přepínání skrytých souborů.Linux · Soubory GNOME: stiskněte Ctrl+Hnebo otevřete nabídku a vyberte Zobrazit skryté soubory.Linux · KDE Dolphin: stiskněte Ctrl+H, nebo použít Zobrazit → Zobrazit skryté soubory.
  - Smazat `.rockbox` složku z kořene karty.
  - Znovu vložte kartu a spusťte přehrávač. Rockbox znovu vytvoří složku s výchozími hodnotami.
  - Znovu použijte svůj motiv a nastavení. Pokud se problém vrátí pouze po určitém tématu, je příčinou toto téma.

Mazání `.rockbox` neodinstaluje Rockbox a nedotkne se vaší hudby – složka obsahuje nastavení, motivy a mezipaměti a je automaticky znovu vytvořena. Pokud chcete motivy zachovat, zkopírujte složku mimo `.rockbox` před jejím odstraněním nebo složku přejmenujte na `.rockbox-old` první.Proč nevidím složku .rockbox na mém MicroSD?

Složky, jejichž název začíná tečkou, jsou na většině počítačů ve výchozím nastavení skryté. K instalaci Rockbox ji nemusíte vidět — Updater zpracovává soubory. Pokud řešíte potíže a chcete je odstranit, nejprve zapněte skryté soubory. Jak zobrazit skryté souboryZobrazte soubory dot na vašem počítačiWindows: v Průzkumníku souborů otevřete Zobrazit karta a zaškrtnutí Skryté položky.macOS: ve Finder pressu Cmd+Shift+. pro přepínání skrytých souborů.Linux · Soubory GNOME: stiskněte Ctrl+Hnebo otevřete nabídku a vyberte Zobrazit skryté soubory.Linux · KDE Dolphin: stiskněte Ctrl+H, nebo použít Zobrazit → Zobrazit skryté soubory.Vymaže smazání .rockbox můj motiv a nastavení?

ano — `.rockbox` obsahuje nastavení, téma, seznamy skladeb a databázi uloženou v mezipaměti Rockbox. Smazáním se Rockbox vrátí do čistého výchozího stavu. Zálohujte celou složku (nebo ji přejmenujte na `.rockbox-old`), pokud něco z toho budete chtít zpět, spusťte přehrávač a Rockbox vytvoří novou složku.

## Další příručky Rockbox-Y1 a Rockbox-Y2

Prozkoumejte podrobné příručky pro instalaci, stahování, tématiku, obnovu a odstraňování problémů Rockbox na obou modelech:[Rockbox-Y1 náboj](rockbox-y1/)[Rockbox-Y2 náboj](rockbox-y2/)[Rockbox stahování ROM](rockbox-rom-download_cs.html)[Rockbox pro Y1](rockbox-for-y1_cs.html)[Rockbox pro Y2](rockbox-for-y2_cs.html)[Rockbox-Y1 vs. Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1 motivy](rockbox-y1-themes.html)[Rockbox-Y2 motivy](rockbox-y2-themes.html)

## Byla tato reference užitečná?

Vaše odpověď pomáhá zlepšit tuto příručku.AnoJeště ne[Dejte nám vědět, jak se můžeme zlepšit](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
