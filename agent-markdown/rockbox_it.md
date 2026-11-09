---
title: "Come installare Rockbox sul tuo programma di aggiornamento Innioasis Y1 o Y2 - Innioasis"
description: "Installa Rockbox su un Innioasis Y1 o Y2 con Updater: temi, versioni stabili, note Type A e Type B e come ripristinare successivamente il software originale."
language: "it"
source: "https://innioasis.app/rockbox_it.html"
---

# Come installare Rockbox sul tuo programma di aggiornamento Innioasis Y1 o Y2 - Innioasis

Rockbox riferimento

# Ottenere Rockbox sul tuo Y1 o Y2

Rockbox cambia il software del lettore e apre un'interfaccia del lettore musicale più profonda, controlli di riproduzione, ordinamento e opzioni di temi. L'installazione è guidata, ma Y1 e Y2 sono percorsi separati.[Rockbox su Y1](guides/rockbox-y1.html)[Rockbox su Y2](guides/rockbox-y2.html)[Perché Rockbox?](rockbox-benefits_it.html)

## Cosa cambia durante l'installazione

Rockbox è un software personalizzato. Ciò non impedisce la possibilità di tornare all'interfaccia originale quando è disponibile il pacchetto software originale corrispondente. Può migliorare la navigazione e la personalizzazione della musica, ma funzionalità, risoluzione, durata della batteria e compatibilità dei temi dipendono dalla build.Non mescolare i modelli. Selezionare Y1 per un giocatore Y1 e Y2 per un giocatore Y2. Un nome di rilascio dall'aspetto simile non è una prova sufficiente della compatibilità di un pacchetto.

## Guarda il video

Video di Frawgeeys. Mostra il percorso di aggiornamento Innioasis; utilizza i passaggi scritti specifici del modello riportati di seguito per il tuo Y1 o Y2.

Video di [Piazza Cristiana](https://www.youtube.com/@CristianPlaza) (Spagnolo), che mostra Rockbox su un Y1. Utilizza i passaggi specifici del modello riportati di seguito per il tuo lettore.

## Il percorso condiviso di aggiornamento
  - Installa Updater e non connettere nulla finché non viene richiesto.
  - Scegli il modello stampato sul lettore in Modello del dispositivo.
  - Scegli Rockbox dentro Software.
  - Scegli una versione stabile a meno che tu non stia testando deliberatamente una build notturna.
  - Fare clic Installa / Ripristina, quindi seguire le istruzioni di spegnimento e connessione USB.
  - Disconnettersi solo dopo il messaggio di successo.

## 240p, 360p e temi

Le raccolte di temi Rockbox meno recenti possono essere realizzate per 240p. Y1 le build della community utilizzano anche etichette di compatibilità 360p. Leggi le note di rilascio e la fonte del tema prima di scegliere una build. Un tema creato per una risoluzione o famiglia di software potrebbe non funzionare su un'altra.[Sfoglia i temi della community](https://themes.innioasis.app/?lang=it)[Strumenti a tema](https://themes.innioasis.app/?lang=it)

## Ritorno al software originale

Scegli di nuovo lo stesso modello, seleziona Software originale, scegli una versione stabile e utilizza Installa / Ripristina. Se l'errore si è verificato prima del prompt USB, controllare il computer e i file estratti. Se il lettore è stato rilevato ma il flash non è riuscito, iniziare con [risoluzione dei problemi](troubleshooting_it.html).[Y1 ripristino](guides/restore-original-y1.html)[Y2 ripristino](guides/restore-original-y2.html)

## Domande frequentiHo reinstallato Rockbox e non è stato risolto nulla.

La reinstallazione di Rockbox scrive la stessa build sugli stessi file, quindi non può ripristinare le cose che Rockbox conserva su MicroSD. Se il problema riguarda un'impostazione, un tema, una playlist o un database non funzionante presente sulla scheda, la reinstallazione non risolverà il problema. Il ripristino affidabile sta eliminando il file `.rockbox` cartella da MicroSD — Rockbox ne crea una nuova all'avvio successivo.
  - Spegnere completamente il lettore e rimuovere la scheda MicroSD oppure collegare il lettore come unità USB.
  - Mostra i file nascosti sul tuo computer in modo che la cartella sia visibile. Come mostrare i file nascostiMostra i dotfile sul tuo computerWindows: in Esplora file apri il file Visualizzazione scheda e spuntare Oggetti nascosti.macOS: nel Finder premere Cmd+Shift+. per attivare/disattivare i file nascosti.Linux · File GNOME: premere Ctrl+Hoppure apri il menu e scegli Mostra file nascosti.Linux · KDE Dolphin: premere Ctrl+Ho utilizzare Visualizza → Mostra file nascosti.
  - Elimina il `.rockbox` cartella dalla root della scheda.
  - Reinserire la scheda e avviare il lettore. Rockbox ricrea la cartella con le impostazioni predefinite.
  - Riapplica il tema e le impostazioni. Se il problema si ripresenta solo dopo un tema specifico, quel tema ne è la causa.

Eliminazione `.rockbox` non disinstalla Rockbox e non tocca la tua musica: la cartella contiene impostazioni, temi e cache e viene ricostruita automaticamente. Se vuoi conservare i tuoi temi, copia la cartella fuori `.rockbox` prima di eliminarlo o rinominare la cartella in `.rockbox-old` prima.Perché non riesco a vedere la cartella .rockbox sul mio MicroSD?

Le cartelle il cui nome inizia con un punto sono nascoste per impostazione predefinita sulla maggior parte dei computer. Non è necessario vederlo per installare Rockbox: il programma di aggiornamento gestisce i file. Se stai risolvendo il problema e desideri eliminarlo, attiva prima i file nascosti. Come mostrare i file nascostiMostra i dotfile sul tuo computerWindows: in Esplora file apri il file Visualizzazione scheda e spuntare Oggetti nascosti.macOS: nel Finder premere Cmd+Shift+. per attivare/disattivare i file nascosti.Linux · File GNOME: premere Ctrl+Hoppure apri il menu e scegli Mostra file nascosti.Linux · KDE Dolphin: premere Ctrl+Ho utilizzare Visualizza → Mostra file nascosti.L'eliminazione di .rockbox ripristinerà il tema e le impostazioni?

SÌ - `.rockbox` contiene le impostazioni, il tema, le playlist e il database memorizzato nella cache di Rockbox. L'eliminazione riporta Rockbox a uno stato predefinito pulito. Eseguire il backup dell'intera cartella (o rinominarla in `.rockbox-old`) se vuoi recuperarne qualcuno, avvia il lettore e Rockbox crea una nuova cartella.

## Altre guide Rockbox-Y1 e Rockbox-Y2.

Esplora le guide dettagliate per l'installazione, il download, la creazione di temi, il ripristino e la risoluzione dei problemi Rockbox su entrambi i modelli:[Rockbox-Mozzo Y1](rockbox-y1/)[Rockbox-Mozzo Y2](rockbox-y2/)[Rockbox Download della ROM](rockbox-rom-download_it.html)[Rockbox per Y1](rockbox-for-y1_it.html)[Rockbox per Y2](rockbox-for-y2_it.html)[Rockbox-Y1 rispetto a Y2](rockbox-y1-vs-y2.html)[Rockbox-Temi Y1](rockbox-y1-themes.html)[Rockbox-Temi Y2](rockbox-y2-themes.html)

## Questo riferimento è stato utile?

La tua risposta aiuta a migliorare questa guida.SìNon ancora[Facci sapere come possiamo migliorare](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
