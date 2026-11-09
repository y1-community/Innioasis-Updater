---
title: "Rockbox-Y1 temi: trasferimento di temi con Updater CE, 240p vs 360p e applicazione di un tema"
description: "Come trasferire temi su Innioasis Y1 con Updater CE (push automatico quando disponibile o trasferimento guidato passo dopo passo dopo un flash MTKClient su macOS e Linux), oltre alla compatibilità 240p vs 360p e all&#39;applicazione di un tema."
language: "it"
source: "https://innioasis.app/rockbox-y1-themes_it.html"
---

# Rockbox-Y1 temi: trasferimento di temi con Updater CE, 240p vs 360p e applicazione di un tema

[← Rockbox-Y1mozzo](rockbox-y1/)

Rockbox-Y1 · temi e aggiornamento CE

# Rockbox-Y1 temi: trasferisci con Updater CE, scegli la build, quindi l'aspetto

Updater CE gestisce Rockbox-Y1 temi e caratteri per te, trasferendoli automaticamente su Y1 ogni volta che può e guidandoti attraverso il trasferimento passo dopo passo quando non può avvenire senza supervisione (ad esempio, subito dopo l'installazione del firmware MTKClient su macOS o Linux).[Ottieni Rockbox e l'aggiornamento CE](guides/rockbox-y1.html)[Sfoglia i temi della community](https://themes.innioasis.app/)[240p contro 360p](rockbox-y1/resolution.html)

## Trasferimento di temi su Y1 con Updater CE

Rockbox memorizza il firmware nella flash interna di Y1, mentre temi, caratteri e impostazioni utente risiedono all'interno della memoria nascosta `.rockbox` cartella nella memoria del lettore (scheda MicroSD). Poiché il flashing di un ROM e la copia dei file nell'archivio utilizzano due connessioni diverse, Programma di aggiornamento CE si adatta automaticamente al tuo sistema operativo e al tuo metodo di installazione:
  - Trasferimento automatico quando Updater CE può raggiungere il lettore: Quando installi una build 360p Rockbox-Y1 (o abiliti la sincronizzazione automatica del tema in Impostazioni), Updater CE scarica e unisce il tema 360p selezionato e il pacchetto di caratteri in background. Non appena il Y1 sarà raggiungibile ADB (Android Debug Bridge) o montato come file USB unità con a `.rockbox` cartella, Updater CE invia i temi e i caratteri direttamente al lettore senza che sia necessaria l'estrazione manuale del zip.
  - Trasferimento guidato passo dopo passo quando non può avvenire senza supervisione (ad esempio MTKClient su macOS e Linux): Quando esegui il flashing di Rockbox utilizzando un MTKClient metodo di installazione su macOS o Linux, il flash avviene mentre Y1 è spento in modalità Preloader/BROM di basso livello, prima che Rockbox si sia avviato per la prima volta per creare `.rockbox` e prima che la memoria del lettore venga montata sul computer. Ogni volta che Updater CE non riesce a completare il trasferimento senza supervisione durante il flash, apre automaticamente il file assistente per temi e caratteri post-installazione e ti guida attraverso il completamento: 
    - Avvia prima Rockbox: Updater CE richiede di scollegare il cavo USB, se necessario, e di accendere Y1 in modo che Rockbox si avvii una volta e inizializzi il `.rockbox` cartella sulla scheda.
    - Riconnettiti tramite USB: Ricollega Y1 al tuo PC Mac o Linux. Se ADB è disponibile, Updater CE rileva il lettore avviato e invia automaticamente i pacchetti di temi e caratteri.
    - Oppure utilizza la modalità di archiviazione USB con il selettore di cartelle guidato: Se ADB non è attivo o preferisci il trasferimento di archiviazione diretto, Updater CE ti guida ad accedere alla modalità di archiviazione USB su Y1, fai clic su Seleziona la cartella .rockbox, rivela le cartelle nascoste (Cmd+Shift+. nella finestra di dialogo dei file di macOS o Ctrl+H su Linux) e selezionare `.rockbox` sull'unità Y1: Updater CE unirà per te tutti i temi e i caratteri.

  - Aggiungi o aggiorna temi in qualsiasi momento su richiesta: Puoi eseguire lo stesso trasferimento automatizzato o guidato in qualsiasi momento senza eseguire nuovamente il flashing del firmware: apri Updater CE e scegli Impostazioni → Installa Rockbox Temi 360p (Cmd+T su macOS, Ctrl+T su Windows e Linux) oppure trascinare un singolo tema `.zip` si inserisce negli Updater CE Goccia intelligente finestra.

## 240p, 360p e perché l'etichetta è sulla build

Y1 le build della community vengono pubblicate con un'etichetta di risoluzione e le raccolte di temi portano la stessa etichetta. Le build a 240p hanno la più ampia compatibilità con i pacchetti di temi più vecchi; Le build a 360p sono realizzate per il percorso tematico più recente Y1. Installarne uno e applicare l'altro non è pericoloso: sembra semplicemente sbagliato, con testo troncato, elementi mancanti o un'interfaccia non leggibile.

Se non hai ancora preferenze sul tema, prendi la build stabile più recente e il suo tema predefinito, quindi scegli i temi che corrispondono alla sua etichetta. IL [pagina di risoluzione](rockbox-y1/resolution.html) va più in profondità; la regola pratica è semplice: l'etichetta di build e l'etichetta del tema devono concordare.

## Dove vivono i temi

I temi sono file sulla scheda MicroSD, all'interno del file `.rockbox` cartella: la stessa cartella che contiene le impostazioni e la cache. Il firmware stesso è su flash interno, quindi aggiungere, modificare o rimuovere un tema non richiede mai il reflash.
  - Copia la cartella del tema in `.rockbox/themes` sulla carta.
  - Quindi sceglilo nelle impostazioni del tema del lettore e riavvia per vederlo applicato.
  - Conserva una copia di un tema che ti piace prima di aggiornare la build: è un file, non un'installazione.

Attiva prima i file nascosti se non riesci a vedere la cartella: macOS Cmd+Shift+., Visualizza Windows → Oggetti nascosti, Linux Ctrl+H.

## Applicazione di un tema, in ordine
  - Installa e avvia prima Rockbox-Y1; un tema necessita di una build in esecuzione.
  - Copia la cartella del tema in `.rockbox/themes` sulla carta.
  - Apri le impostazioni del tema e seleziona il tema.
  - Riavvia in modo che l'intera interfaccia, non solo il menu, lo riprenda.
  - Se sembra rotto, seleziona un altro tema; i file sono ancora lì se vuoi riprovare più tardi.

## Annullamento di un tema che ha danneggiato l'interfaccia

Se il lettore si avvia in modo inutilizzabile, non è necessario reinstallare il firmware. Rinominare o eliminare il `.rockbox` cartella sulla scheda e avvia il lettore: la build ricrea la cartella con le impostazioni predefinite e un tema predefinito. La tua musica rimane intatta e puoi copiare i temi che desideri in seguito.[La cartella .rockbox](rockbox-y1/sd-card.html)[Primo avvio](rockbox-y1/first-start.html)[Aggiornamento della build](rockbox-y1/update.html)

## Domande che le persone fannoPerché Updater CE mi guida attraverso il trasferimento dei temi dopo un'installazione di MTKClient su macOS o Linux?

MTKClient esegue il flashing di Rockbox ROM nella memoria interna mentre Y1 è spento in modalità Preloader/BROM di basso livello, prima che Rockbox si sia avviato per inizializzare il `.rockbox` cartella e prima che la scheda MicroSD venga montata sul computer. Ogni volta che Updater CE riesce a raggiungere direttamente il lettore avviato (tramite ADB o un'unità USB montata), trasferisce i temi automaticamente; quando non può farlo da solo durante il flash, apre il passaggio guidato di temi e caratteri subito dopo il flashing per aiutarti ad accendere Y1 e completare il trasferimento tramite ADB o USB Modalità di archiviazione.Un tema Y2 funzionerà su Y1?

No. I port sono separati e il supporto dei temi su Y2 segue le build beta. Vedere [Rockbox-Y2 temi](rockbox-y2-themes_it.html).I temi sopravvivono a un aggiornamento?

Di solito sì, perché vivono sulla scheda e la flash scrive il ROM. Se una nuova build modifica il percorso del tema, riapplica un tema che corrisponda alla sua etichetta.Perché il tema è applicato solo a metà?

Un riavvio normalmente lo risolve. In caso contrario, i file del tema sono incompleti: copia nuovamente la cartella anziché modificare i singoli file.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
