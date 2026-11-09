---
title: "Innioasis Y1 Non si accende | Innioasis Archivio firmware - Innioasis Download firmware"
description: "Innioasis Y1 non si accende o non si carica? Forza un riavvio, controlla se un computer lo vede, quindi ripristina il firmware Y1 o utilizza il ripristino manuale SP Flash Tool."
language: "it"
source: "https://innioasis.app/guides/y1-wont-turn-on_it.html"
---

# Innioasis Y1 Non si accende | Innioasis Archivio firmware - Innioasis Download firmware

Recupero del giocatore · Innioasis Y1

# Innioasis Y1 non si accende

Uno schermo nero non significa sempre un giocatore morto. Effettua la ricarica, il riavvio forzato e il rilevamento su un computer prima di provare un flash manuale.[Ottieni Updater CE](../guide_it.html#platform)[Download del firmware](../firmware_it.html)[Guida al recupero](recovery_it.html)

## Carica correttamente il Y1 prima di ogni altra cosa

La maggior parte dei rapporti "Y1 non si accende" riguarda una batteria scarica, un cavo di sola ricarica o un caricabatterie che non può fornire corrente sufficiente. Un Y1 profondamente scarico può impiegare dai 20 ai 30 minuti prima che lo schermo mostri qualcosa, quindi dagli tempo prima di chiamarlo morto.
  - Utilizza un USB noto dati cavo, non un cavo di sola ricarica.
  - Prova un caricabatterie da muro, quindi direttamente una porta USB del computer, non un hub.
  - Lascialo collegato per 30-60 minuti e controlla l'icona di ricarica o la retroilluminazione.
  - Prova un secondo cavo e caricabatterie prima di proseguire.

## Forza un riavvio

Tieni premuto il pulsante di accensione per circa 15 secondi, rilascialo, attendi cinque secondi, quindi premi il pulsante di accensione una volta. Questo cancella uno stivale bloccato ed è sicuro ripeterlo.

Se lo schermo mostra il logo e poi diventa nero, il lettore si avvia e non funziona correttamente: passa al ripristino del firmware di seguito. Se non succede nulla, tienilo in carica e riprova dopo mezz'ora.

## Controlla se un computer può vedere il lettore

Collega il Y1 spento con un cavo dati e apri Gestione dispositivi su Windows, `lsusb` su Linux o MTKClient su macOS. Un lettore funzionante appare come un dispositivo MediaTek con ID fornitore `0e8d`. Se appare, l'hardware è abbastanza attivo da eseguire il reflash anche quando lo schermo rimane scuro.

Se non viene visualizzato nulla, installare prima il driver MediaTek su Windows: il file [guida dell'autista](../drivers_it.html) copre le autorizzazioni Windows e Linux.

## Ripristina il firmware originale Y1.

Se il lettore viene rilevato ma non si avvia, reinstallare il software originale Y1. Utilizzare solo un pacchetto Y1; una build Y2 non verrà avviata sull'hardware Y1.
  - Aperto [Programma di aggiornamento CE](../guide_it.html#platform) sul tuo computer
  - Impostato Modello del dispositivo a Y1.
  - Scegli Software originale dentro Software e scegli una versione stabile Y1: il pacchetto manuale lo è `rom.zip`.
  - Fare clic Installa / Ripristina e lascia che il pacchetto venga estratto.
  - Spegnere completamente Y1, collegare il cavo dati USB solo quando l'Updater lo richiede e lasciarlo fino al messaggio di successo.
Mantieni la potenza stabile. Un flash che perde potenza può rendere il lettore inutilizzabile. Caricalo prima e collegalo direttamente al computer.

## Ripristino manuale quando Updater non riesce a vedere il lettore

Updater CE include strumenti di ripristino manuale per i casi in cui l'installazione guidata non può essere completata. [SP Flash Tool](../sp-flash-tool_it.html) è in bundle su Windows e Linux x86 e il percorso MTKClient copre macOS. Entrambi necessitano di un pacchetto firmware corrispondente al modello da [Download del firmware](../firmware_it.html) pagina.

Segui la guida agli strumenti per la tua piattaforma invece di improvvisare file scatter o offset. Se il lettore non viene rilevato da nessuno strumento, il guasto è probabilmente dovuto alla batteria, alla porta di ricarica o alla scheda.

## Se ancora non si avvia

Smetti di lampeggiare e trattalo come hardware. Non aprire la custodia né premere sulla batteria. Chiedi alla community il modello, cosa fa lo schermo, se un computer lo rileva e quali pacchetti hai provato: il [Discord comunità](https://discord.gg/zHrT2zrcek) può aiutare a identificare un percorso di servizio.

Un ripristino stock sostituisce il sistema, quindi esegui il backup di tutto ciò che è archiviato nella memoria interna del lettore prima di eseguire il flashing. La musica su una scheda MicroSD non viene interessata dal ripristino.

## Innioasis Y1 Domande frequenti sull'alimentazione

### Perché il mio Innioasis Y1 non si accende?

Le cause più comuni sono una batteria completamente scarica, un cavo di sola ricarica o un caricabatterie debole, un arresto anomalo del firmware che interrompe l'avvio o un guasto hardware. Caricalo per 30 minuti con un cavo dati conosciuto prima di dare per scontato che il lettore sia morto.

### Come posso forzare il riavvio di un Innioasis Y1?

Tieni premuto il pulsante di accensione per circa 15 secondi, rilascialo, attendi cinque secondi, quindi premi il pulsante di accensione una volta. Se non viene visualizzato nulla, lascialo in carica e riprova dopo 30 minuti.

### Posso recuperare un Y1 che non si accende?

Spesso sì. Se un computer rileva ancora il dispositivo MediaTek, reinstallare il pacchetto software originale Y1 con Updater CE. Se non viene rilevato, utilizzare il ripristino SP Flash Tool o MTKClient incluso con Updater CE e un file firmware Y1 corrispondente al modello.

### È necessario caricare un Y1 prima di lampeggiare?

SÌ. Un flash che perde potenza può rendere il lettore inutilizzabile. Caricalo prima e collegalo direttamente al computer anziché tramite un hub.

## Correzioni correlate
  - [Y2 non si accende](y2-wont-turn-on_it.html) — gli stessi controlli per Y2
  - [La rotella di scorrimento Y1 non funziona](y1-scroll-wheel-not-working_it.html) - se si avvia ma il volante no
  - [Innioasis guida al recupero](recovery_it.html) - tutte le guide sui sintomi in un unico posto
  - [SP Flash Tool guida](../sp-flash-tool_it.html) — flashing manuale su Windows e Linux
  - [Risoluzione dei problemi di installazione](../troubleshooting_it.html) - che aspetto ha un flash non riuscito

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
