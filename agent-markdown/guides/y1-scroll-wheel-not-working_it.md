---
title: "Innioasis Y1 La rotella di scorrimento non funziona dopo l'aggiornamento | Innioasis Archivio firmware - Innioasis Download firmware"
description: "Innioasis Y1 la rotellina di scorrimento o la ghiera cliccabile non funzionano dopo un aggiornamento? Reinstallare il software originale Y1, controllare l&#39;anello e separare il firmware dai guasti hardware."
language: "it"
source: "https://innioasis.app/guides/y1-scroll-wheel-not-working_it.html"
---

# Innioasis Y1 La rotella di scorrimento non funziona dopo l'aggiornamento | Innioasis Archivio firmware - Innioasis Download firmware

Recupero del giocatore · Innioasis Y1

# Innioasis Y1 la rotella di scorrimento non funziona dopo un aggiornamento

La rotella gira ma non si muove nulla oppure la ghiera cliccabile ha smesso di rispondere subito dopo un lampo. Ecco come separare un errore del firmware da uno dell'hardware e cosa fare prima.[Ottieni Updater CE](../guide_it.html#platform)[Y1 download di software](../firmware_it.html?model=Y1&software=original-y1)[Guida al recupero](recovery_it.html)

## Scopri se il problema è il volante o il firmware

Su un Y1 la ruota è un input fisico, ma il firmware decide cosa fa ogni giro e clic. Se il volante si è fermato nel momento in cui hai aggiornato o flashato il lettore, la causa probabile è il software, non una parte rotta. Se ignora tutti i software che provi (stock, Rockbox o una schermata di ripristino), trattalo come hardware.
  - Funziona in un software, è morto in un altro: guasto del firmware.
  - Morto su ogni schermata, incluso il ripristino: ruota, nastro o tavola.
  - Manca solo una direzione: solitamente detriti sotto l'anello o usura.
  - La ruota gira ma non si evidenzia nulla: il lettore potrebbe essere bloccato: forza prima il riavvio.

## Controlli rapidi prima di reinstallare il firmware
  - Tieni premuto il pulsante di accensione per circa 15 secondi per forzare lo spegnimento del lettore, quindi avvialo normalmente.
  - Prova il volante nella schermata iniziale, in Impostazioni e nel lettore musicale.
  - Premi i pulsanti fisici. Se la potenza e la parte posteriore rispondono ma la ruota no, la colpa è della ruota stessa.
  - Carica il lettore per 30 minuti con un cavo dati noto: una batteria scarica può far sì che gli input si comportino in modo irregolare.
  - Se hai installato Rockbox o un'altra build personalizzata, torna al software originale ed esegui nuovamente il test.

## Reinstallare il firmware Y1 corrispondente al tuo lettore

Poiché il volante è azionato dal firmware, un errore relativo all'aggiornamento viene risolto reinserendo sul lettore il software originale Y1 corretto. Non utilizzare un pacchetto Y2 e non scegliere una versione "abbastanza simile": i pacchetti Y1 sono creati per l'hardware Y1 e una build Y2 su un Y1 può lasciare i controlli mappati in modo errato.
  - Aperto [Programma di aggiornamento CE](../guide_it.html#platform) sul tuo computer
  - Impostato Modello del dispositivo a Y1.
  - Scegli Software originale dentro Software e scegli una versione stabile Y1: il pacchetto manuale lo è `rom.zip`.
  - Fare clic Installa / Ripristina e lascia che il pacchetto venga estratto.
  - Spegnere completamente Y1, collegare il cavo dati USB solo quando l'Updater lo richiede e lasciarlo fino al messaggio di successo.
Abbina il modello e la versione. Se l'elenco delle versioni è simile a Y2 software, interrompere e selezionare nuovamente Y1. I passaggi completi sono in [Guida al ripristino Y1](restore-original-y1_it.html).

## Controllare l'anello della ruota per eventuali detriti o danni

Se la ruota è rigida, si attacca o si rompe solo in una direzione, possono rimanere residui di polvere e sabbia tra l'anello e la custodia. Spegnere il lettore e pulire l'anello con un panno in microfibra asciutto. Non gocciolare detergenti o alcol nella fessura e non fare leva sull'anello.

Se l'anello è allentato, rotto o non fa più clic, il lettore necessita di assistenza. La reinstallazione del firmware non riparerà una ruota danneggiata, un nastro scollegato o danni dovuti a liquidi.

## Se anche il lettore non si avvia

Un aggiornamento non riuscito può impedire l'avvio di Y1, il che sembra un problema alla ruota perché non risponde nulla. Lavora attraverso il [Y1 non attiva la guida](y1-wont-turn-on_it.html) per le fasi di ricarica, riavvio forzato e ripristino manuale.

## Innioasis Y1 Domande frequenti sulla rotella di scorrimento

### Perché la mia rotella di scorrimento Innioasis Y1 ha smesso di funzionare dopo un aggiornamento?

Un aggiornamento può lasciare il driver del volante fuori passo rispetto al resto del firmware, soprattutto se il flash è stato interrotto o è stato utilizzato un pacchetto Y2. Reinstalla la versione originale del software Y1 per il tuo modello e prova il volante nella schermata iniziale di serie.

### Come posso sapere se la ghiera cliccabile Y1 è rotta o il firmware è difettoso?

Prova il volante in più di un software. Se funziona nel software stock ma non in Rockbox, si tratta di un problema di mappatura del firmware. Se non fa nulla su nessuna schermata, incluso un menu di ripristino, sospetta la ruota, il suo nastro o il tabellone.

### Il ripristino del software originale risolverà la rotella di scorrimento Y1?

Risolve gli errori causati da un aggiornamento o da un pacchetto non corrispondente ed è la prima cosa da provare. Non riparerà una ruota danneggiata fisicamente, un nastro allentato o danni liquidi.

### Posso utilizzare un pacchetto firmware Y2 per risolvere un problema alla ruota Y1?

No. I pacchetti Y1 e Y2 non sono intercambiabili e far lampeggiare il modello sbagliato può peggiorare i controlli. Abbina il modello e rilascialo prima di eseguire Installa/Ripristina.

## Correzioni correlate
  - [La rotella di scorrimento Y2 non funziona](y2-scroll-wheel-not-working_it.html) — gli stessi controlli per Y2
  - [Y1 non si accende](y1-wont-turn-on_it.html) — ripristino dell'alimentazione e dell'avvio
  - [Innioasis guida al recupero](recovery_it.html) - tutte le guide sui sintomi in un unico posto
  - [Risoluzione dei problemi di installazione](../troubleshooting_it.html) - che aspetto ha un flash non riuscito
  - [Ripristina Y1 software originale](restore-original-y1_it.html) - la procedura dettagliata completa per il ripristino

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
