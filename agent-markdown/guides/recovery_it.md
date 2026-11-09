---
title: "Innioasis Y1 e Y2 Guida al ripristino | Innioasis Archivio firmware - Innioasis Download firmware"
description: "Guida al ripristino per lettori Innioasis Y1 e Y2 che non si accendono o che hanno una rotella di scorrimento che ha smesso di funzionare dopo un aggiornamento. Ripristino e passaggi del firmware."
language: "it"
source: "https://innioasis.app/guides/recovery_it.html"
---

# Innioasis Y1 e Y2 Guida al ripristino | Innioasis Archivio firmware - Innioasis Download firmware

Recupero del giocatore · Y1 e Y2

# Innioasis Y1 e Y2 guida al ripristino

Non si accende, la ruota non funziona o l'installazione si è interrotta a metà. Inizia con il sintomo, quindi segui i passaggi in ordine invece di passare direttamente al flash manuale.[Ottieni Updater CE](../guide_it.html#platform)[Download del firmware](../firmware_it.html)[Risoluzione dei problemi](../troubleshooting_it.html)

Inizia con Innioasis Updater

## L'installazione guidata risolve la maggior parte di questi problemi

Updater lo fa in un solo passaggio. Scegli il software, segui i passaggi sullo schermo e il gioco è fatto. Ti dice anche quando arriva una correzione o una nuova versione.

## Inizia dal sintomo

Queste guide trattano i due errori che gli utenti riscontrano più spesso dopo un aggiornamento o un flash. Scegli quello che corrisponde a ciò che vedi, quindi esaminalo in ordine.

### La rotella di scorrimento non funziona

La ruota gira ma il giocatore la ignora oppure si ferma subito dopo un aggiornamento.

[Y1 rotella di scorrimento della guida](y1-scroll-wheel-not-working_it.html) · [Y2 rotella di scorrimento della guida](y2-scroll-wheel-not-working_it.html)

### Il lettore non si accende

Uno schermo nero, una spia di carica assente o un logo che appare e scompare.

[Y1 guida di potenza](y1-wont-turn-on_it.html) · [Y2 guida di potenza](y2-wont-turn-on_it.html)

### L'installazione è stata interrotta a metà

L'aggiornamento non è riuscito prima o dopo la richiesta USB oppure l'elenco delle versioni sembra errato.

[Guida alla risoluzione dei problemi](../troubleshooting_it.html)

### Servono i file

Software originale e pacchetti personalizzati per ogni modello.

[Download del firmware](../firmware_it.html)

## I pacchetti Y1 e Y2 non sono intercambiabiliNon eseguire mai il cross-flash di un modello. Un Y1 `rom.zip` non è un pacchetto Y2 e un Y2 `rom_y2.zip` non verrà eseguito su un Y1. Far lampeggiare il modello sbagliato è uno dei motivi più comuni per cui un giocatore si ritrova con controlli inattivi o un ciclo di avvio.

Controllare il modello stampato sul lettore, quindi abbinarlo nell'Updater CE prima di scegliere una versione.

## Ripristinare prima il software originale corrispondente

Prima di qualsiasi strumento manuale, reinserire sul lettore il firmware originale per il modello corretto. Ciò risolve la maggior parte degli errori di avvio e volante relativi all'aggiornamento.

Y1: seleziona Y1, scegli Software originale, scegli una versione stabile Y1, quindi esegui Installa/Ripristina. [Guida completa al ripristino Y1.](restore-original-y1_it.html).

Y2: seleziona Y2, scegli Software originale, scegli una versione stabile Y2, quindi esegui Installa/Ripristina. [Guida completa al ripristino Y2.](restore-original-y2_it.html).

Spegnere il lettore e collegare il cavo dati USB solo quando richiesto dall'Updater. Lascialo connesso fino al messaggio di successo.

## Ripristino manuale fornito con Updater CE

Quando Updater non riesce a completare il lavoro, la stessa installazione include gli strumenti manuali. [SP Flash Tool](../sp-flash-tool_it.html) è in bundle su macchine Windows e Linux x86 e il percorso MTKClient copre macOS. Entrambi necessitano di un pacchetto firmware corrispondente al modello, disponibile su [Download del firmware](../firmware_it.html) pagina.

Utilizza la guida per la tua piattaforma e mantieni carico il giocatore. Se nessuno strumento rileva il lettore, è probabile che il problema sia dell'hardware piuttosto che del firmware.

## Cosa includere quando chiedi aiuto
  - Il modello — Y1 o Y2 — stampato sul lettore.
  - Cosa fa lo schermo: niente, un logo, un ciclo di avvio o la schermata iniziale.
  - Se un computer rileva il lettore come dispositivo MediaTek.
  - L'esatto messaggio di aggiornamento e il pacchetto selezionato.
  - Quello che hai già provato, incluso qualsiasi strumento manuale.

Non pubblicare token privati ​​o file di sistema non correlati. IL [comunità Discord](https://discord.gg/zHrT2zrcek) e [r/innioasis](https://reddit.com/r/innioasis) sono i posti più veloci per confrontare le note.

## Innioasis Domande frequenti sul ripristino

### Come posso riparare un Innioasis lettore che non si accende?

Caricalo per 30 minuti con un cavo dati noto, forza il riavvio mantenendo l'alimentazione per 15 secondi, quindi controlla se un computer lo rileva. In tal caso, ripristinare il software originale corrispondente al modello; in caso contrario, utilizzare gli strumenti di ripristino manuale inclusi con Updater CE.

### Perché la rotella di scorrimento Y1 o Y2 non funziona?

Se il volante si ferma dopo un aggiornamento, solitamente si tratta di una mancata corrispondenza del firmware. Reinstallare il software originale corrispondente al modello ed eseguire nuovamente il test. Se il volante è guasto in ogni firmware, trattalo come un guasto hardware.

### Dove posso scaricare il firmware per il ripristino?

La pagina Download del firmware su innioasis.app/firmware.html ospita pacchetti originali e personalizzati per ciascun modello. Scegli sempre il pacchetto Y1 o Y2 che corrisponde al giocatore.

### Quali strumenti di ripristino sono inclusi in Updater CE?

Updater CE include SP Flash Tool su Windows e Linux e il percorso MTKClient che include macOS, per il ripristino manuale quando la normale installazione non può essere completata.

## Correzioni correlate
  - [La rotella di scorrimento Y1 non funziona](y1-scroll-wheel-not-working_it.html) - la ghiera cliccabile non risponde dopo un aggiornamento
  - [La rotella di scorrimento Y2 non funziona](y2-scroll-wheel-not-working_it.html) — gli stessi controlli per Y2
  - [Y1 non si accende](y1-wont-turn-on_it.html) — ricarica, riavvio e ripristino manuale
  - [Y2 non si accende](y2-wont-turn-on_it.html) — gli stessi controlli per Y2
  - [SP Flash Tool guida](../sp-flash-tool_it.html) — flashing manuale su Windows e Linux

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
