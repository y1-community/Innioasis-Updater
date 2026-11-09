---
title: "Rockbox pour Y2 (Rockbox-Y2) : présentation, builds et guide d'installation"
description: "Rockbox pour Y2, Rockbox-Y2 et rockbox-y2 font référence au port du firmware de la communauté Rockbox pour le Innioasis Y2. Découvrez ce qu&#39;il comprend et comment l&#39;installer avec Innioasis Updater CE."
language: "fr"
source: "https://innioasis.app/rockbox-for-y2_fr.html"
---

# Rockbox pour Y2 (Rockbox-Y2) : présentation, builds et guide d'installation

[← Téléchargements de micrologiciels](firmware_fr.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox pour Y2 (Rockbox-Y2)

Rockbox-Y2 (également appelé « Rockbox pour Y2 ») est le port du micrologiciel communautaire dédié Rockbox pour le Innioasis Y2. Il utilise son propre package ROM (`rom_y2.zip`) et est installé directement via Innioasis Updater CE.[Installer Rockbox-Y2](rockbox-y2/install.html)[Téléchargez le ROM](rockbox-y2/download.html)[Tutoriel écrit](guides/rockbox-y2.html)[Rockbox-Concentrateur Y2](rockbox-y2/)

## Conçu spécifiquement pour le Innioasis Y2

Dans Innioasis Updater CE, ce firmware est répertorié comme Rockbox quand Y2 est sélectionné. Ses sorties sont publiées par le [spycemagic/y2-rockbox](firmware_fr.html?model=Y2&software=rockbox-y2) projet avec le nom du package `rom_y2.zip`.

N'installez jamais un package de micrologiciel Y1 sur un Y2. Sélection Y2 in Updater CE filtre automatiquement la liste des versions sur les versions compatibles avec Y2 uniquement.

## Ce que propose Rockbox-Y2
  - Bibliothèque musicale basée sur des tags - parcourez les albums, les artistes et les genres à partir des balises de vos fichiers audio ou parcourez directement les dossiers.
  - Commandes de lecture - Paramètres de lecture sans interruption, de fondu enchaîné, de ReplayGain et d'égaliseur.
  - Thèmes personnalisés — installez des thèmes compatibles avec votre build Rockbox-Y2 ([Y2 guide thématique](rockbox-y2-themes.html)).
  - 100% hors ligne — lit les fichiers locaux de votre carte MicroSD sans compte ni abonnement.
  - Restauration d'usine facile — revenir à Y2 Logiciel d'origine à tout moment dans Updater CE.

## Choisir une version Rockbox-Y2
  - Sélectionnez toujours Y2 dans Modèle d'appareil d'abord.
  - Choisissez la dernière version, sauf si vous testez une version spécifique.
  - Lire le [Rockbox-Notes de version Y2](release-notes/rockbox-y2/index_fr.html) pour voir ce qui a changé dans chaque build.

## Téléchargements directs des développeurs de la communauté

Innioasis Updater CE télécharge toujours les packages de micrologiciels directement auprès des développeurs de micrologiciels de la communauté ([spycemagic/y2-rockbox](firmware_fr.html?model=Y2&software=rockbox-y2)), et ces développeurs sont seuls responsables de la liste de leurs versions logicielles dans Updater CE.

Vous pouvez laisser Updater CE télécharger et flasher `rom_y2.zip` automatiquement, ou téléchargez le package depuis notre [Rockbox-Y2 page de téléchargement](rockbox-y2/download.html) et [Rockbox ROM page de téléchargement](rockbox-rom-download_fr.html).[Rockbox-Y2 téléchargements](rockbox-y2/download.html)[Installer à partir d'un ZIP local](rockbox-y2/portable-zip.html)

## Comment installer Rockbox-Y2
  - Ouvrez Innioasis Updater CE et définissez Modèle d'appareil à Y2.
  - Sélectionnez Rockbox dans Logiciel.
  - Choisissez une version Y2 dans la liste.
  - Cliquez Installer / Restaurer donc Updater CE télécharge le package directement depuis le développeur.
  - Éteignez complètement le Y2 et connectez-le avec un câble de données USB lorsque Updater CE le demande.
  - Attendez le message de fin, puis débranchez et allumez votre Y2.

Pour la procédure complète étape par étape, lisez le [Rockbox-Y2 tutoriel](guides/rockbox-y2.html).

## Restauration du logiciel Y2 d'origine

Pour revenir au firmware d'usine, sélectionnez Y2 et Logiciel d'origine dans Updater CE, choisissez une version stable et cliquez sur Installer / Restaurer. Voir le [guide de restauration](rockbox-y2/restore-stock.html) et [Y2 Page du logiciel d'origine](original-software-y2_fr.html).

## Questions fréquemment poséesD'où Updater CE télécharge-t-il Rockbox-Y2 ?

Updater CE télécharge toujours les packages de micrologiciels directement à partir des propres versions des développeurs de micrologiciels de la communauté (`spycemagic/y2-rockbox`). Les développeurs sont seuls responsables de répertorier leurs versions logicielles dans Updater CE.Pourquoi le package est-il nommé rom_y2.zip ?

Le développeur nomme l'archive du firmware Y2 `rom_y2.zip` donc il ne peut pas être confondu avec les Y1 `rom.zip`.Les thèmes Y1 fonctionnent-ils sur le Y2 ?

Pas toujours. Consultez les notes de version de votre build Y2 et consultez les [Rockbox-Y2 guide thématique](rockbox-y2-themes.html).

## Guides associés

### [Rockbox-Concentrateur Y2](rockbox-y2/)

Tous les guides Y2 : installation, téléchargements, thèmes, restauration, double démarrage et dépannage.

### [Rockbox-Y1 contre Rockbox-Y2](rockbox-y1-vs-y2.html)

En quoi les builds Y1 et Y2 Rockbox diffèrent.

### [Rockbox-Thèmes Y2](rockbox-y2-themes.html)

Installation et réinitialisation de thèmes sur Rockbox-Y2.

### [Rockbox pour l'année 1](rockbox-for-y1_fr.html)

Présentation et guide d'installation du port Innioasis Y1.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
