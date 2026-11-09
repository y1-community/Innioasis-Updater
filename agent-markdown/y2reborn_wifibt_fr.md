---
title: "Configuration Wi-Fi, Bluetooth et radio FM pour Reborn (Y2Linux) - Innioasis Updater"
description: "Petit guide de post-installation pour Reborn (Y2Linux / Y2Reborn) sur Innioasis Y2 : copiez system.img, puis configurez le Wi-Fi, le Bluetooth et la radio FM."
language: "fr"
source: "https://innioasis.app/y2reborn_wifibt_fr.html"
---

# Configuration Wi-Fi, Bluetooth et radio FM pour Reborn (Y2Linux) - Innioasis Updater

Innioasis Y2 · Reborn Post-installation

# Configurez le Wi-Fi, le Bluetooth et la radio FM.

Copiez un fichier sur votre lecteur. Reborn gère le reste.[Télécharger system.img (860 Mo)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Guide d'installation](guides/reborn-y2linux-y2.html)[Pourquoi Y2Reborn ?](reborn-y2linux-benefits_fr.html)

## Pourquoi ce fichier ?

Le Wi-Fi, le Bluetooth et la radio FM nécessitent cinq modules de micrologiciel MediaTek que Reborn ne peut pas expédier. Ils sont à l'intérieur du Y2 `system.img`. Reborn les extrait une fois, les vérifie et supprime le fichier.

## Installation
  - Télécharger le système.img

Téléchargez la v3.2.0 FM `system.img` à votre ordinateur.[ Télécharger le système.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Démarrez Reborn une fois

Allumez le lecteur. Attendre Configuration du stockage pour terminer, puis redémarrez-le une fois.
  - Connectez-vous à votre ordinateur

Utilisez un câble de données USB. Le joueur apparaît comme Stockage interne.Sur un Mac ?

Installer [OuvrirMTP](https://openmtp.ganeshrvel.com/) pour parcourir le lecteur. Windows et Linux le montent automatiquement.
  - Copiez system.img dans le micrologiciel

Créez un dossier appelé `Firmware` à la racine du stockage interne. Copie `system.img` dedans.
  - Attendez la fin de l'installation

Reborn installe automatiquement le micrologiciel de la radio et supprime `system.img`. Cela prend environ 10 à 20 secondes. Attendre Le Wi-Fi et le Bluetooth sont prêts.
  - Connectez le Wi-Fi, le Bluetooth et la radio FM
    - Wi-Fi : Paramètres → Système → Réseau → Wi-Fi. Choisissez votre réseau 2,4 GHz.
    - Bluetooth : Mettez vos écouteurs en mode appairage. Paramètres → Bluetooth → sélectionnez-les.
    - Radio FM : Branchez un casque filaire comme antenne, puis ouvrez la radio FM.

  - Mise à jour via Wi-Fi

Les futures mises à jour Reborn seront installées à partir de Paramètres → Système → Mise à jour logicielle. Le firmware de votre radio reste en place.

## Ce guide a-t-il été utile ?

Avez-vous trouvé ce guide de configuration post-installation utile ? Oui, ça a aidé ! [ Besoin d'aide sur Discord ](https://discord.gg/zHrT2zrcek) Merci pour votre retour ! Profitez de votre écoute sans fil sur Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
