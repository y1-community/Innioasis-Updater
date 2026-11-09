---
title: "Configurazione Wi-Fi, Bluetooth e radio FM per Reborn (Y2Linux) - Innioasis Aggiornamento"
description: "Breve guida post-installazione per Reborn (Y2Linux / Y2Reborn) su Innioasis Y2: copia system.img, quindi configura Wi-Fi, Bluetooth e radio FM."
language: "it"
source: "https://innioasis.app/y2reborn_wifibt_it.html"
---

# Configurazione Wi-Fi, Bluetooth e radio FM per Reborn (Y2Linux) - Innioasis Aggiornamento

Innioasis Y2 · Reborn Post-installazione

# Configura Wi-Fi, Bluetooth e radio FM.

Copia un file sul tuo lettore. Reborn si occupa del resto.[Scarica system.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Guida all'installazione](guides/reborn-y2linux-y2.html)[Perché Y2Reborn?](reborn-y2linux-benefits_it.html)

## Perchè questo fascicolo?

Wi-Fi, Bluetooth e radio FM richiedono cinque MediaTek moduli firmware che Reborn non può spedire. Sono all'interno del funzionario Y2 `system.img`. Reborn li estrae una volta, li controlla ed elimina il file.

## Impostare
  - Scarica system.img

Scarica la versione 3.2.0 FM `system.img` al tuo computer.[ Scarica system.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Avvia Reborn una volta

Accendi il lettore. Aspetta Configurazione dell'archiviazione per terminare, quindi riavviarlo una volta.
  - Collegati al tuo computer

Utilizzare un cavo dati USB. Il giocatore appare come Archiviazione interna.Su un Mac?

Installa [OpenMTP](https://openmtp.ganeshrvel.com/) per sfogliare il lettore. Windows e Linux lo montano automaticamente.
  - Copia system.img nel firmware

Crea una cartella chiamata `Firmware` alla radice della memoria interna. Copia `system.img` in esso.
  - Attendi il completamento della configurazione

Reborn installa automaticamente il firmware della radio ed elimina `system.img`. L'operazione richiede circa 10-20 secondi. Aspetta Wi-Fi e Bluetooth sono pronti.
  - Connetti Wi-Fi, Bluetooth e radio FM
    - Wifi: Impostazioni → Sistema → Rete → Wi-Fi. Scegli la tua rete a 2,4 GHz.
    - Bluetooth: Metti le cuffie in modalità di accoppiamento. Impostazioni → Bluetooth → selezionali.
    - Radio FM: Collega le cuffie cablate come antenna, quindi apri la radio FM.

  - Aggiornamento tramite Wi-Fi

Gli aggiornamenti futuri Reborn vengono installati da Impostazioni → Sistema → Aggiornamento software. Il firmware della radio rimane inserito.

## Questa guida è stata utile?

Hai trovato utile questa guida alla configurazione post-installazione? Sì, ha aiutato! [ Hai bisogno di aiuto su Discord ](https://discord.gg/zHrT2zrcek) Grazie per il tuo feedback! Goditi l'ascolto wireless su Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
