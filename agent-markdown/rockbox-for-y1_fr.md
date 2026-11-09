---
title: "Rockbox pour Y1 (Rockbox-Y1) : présentation, builds et guide d'installation"
description: "Rockbox pour Y1, Rockbox-Y1 et rockbox-y1 font tous référence au micrologiciel communautaire Rockbox pour le Innioasis Y1. Découvrez ce qu&#39;il ajoute, quelle version choisir et comment l&#39;installer avec Innioasis Updater CE."
language: "fr"
source: "https://innioasis.app/rockbox-for-y1_fr.html"
---

# Rockbox pour Y1 (Rockbox-Y1) : présentation, builds et guide d'installation

[← Téléchargements de micrologiciels](firmware_fr.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox pour Y1 (Rockbox-Y1)

« Rockbox », « Rockbox-Y1 » et « Rockbox pour Y1 » font tous référence au même firmware communautaire Rockbox pour le Innioasis Y1. Voici ce qu'il ajoute à votre lecteur, quelle build choisir et comment l'installer avec Innioasis Updater CE.[Installer Rockbox-Y1](rockbox-y1/install.html)[Téléchargez le ROM](rockbox-y1/download.html)[Tutoriel écrit](guides/rockbox-y1.html)[Rockbox-Concentrateur Y1](rockbox-y1/)

## Un firmware, plusieurs noms

Dans Innioasis Updater CE, ce firmware apparaît comme Rockbox lorsque vous sélectionnez le modèle de l'appareil Y1. Les guides, vidéos et notes de version l'appellent également Rockbox-Y1 ou Rockbox pour l'année 1 il est donc clair que la construction est pour le Y1 et non pour le Y2.

Vérifiez toujours le modèle imprimé sur votre lecteur avant l'installation : les packages de micrologiciels Y1 et Y2 ne sont pas interchangeables.

## Ce que Rockbox-Y1 ajoute à votre Y1

Rockbox-Y1 est un port communautaire du micrologiciel du lecteur de musique open source Rockbox pour le Innioasis Y1 :
  - Bibliothèque musicale basée sur des tags - parcourez par artiste, album, genre et année à l'aide de balises audio, ou parcourez directement les dossiers.
  - Lecture audio avancée - lecture sans interruption, fondu enchaîné, ReplayGain et un égaliseur complet.
  - Thèmes personnalisés - choisissez parmi des centaines de thèmes communautaires 240p et 360p, y compris des mises en page classiques de style iPod.
  - Radio FM — prise en charge radio FM intégrée.
  - Suppléments optionnels - téléchargements de podcasts via Wi-Fi et Last.fm / ListenBrainz / Maloja scrobbling sur les versions prises en charge.
  - Double démarrage - revenez au logiciel d'origine d'usine sans reflasher sur les versions prises en charge.

## Quelle version Y1 dois-je choisir ?
  - 240p contre 360p — Les builds 240p fonctionnent avec les thèmes classiques 320×240 Rockbox ; Les versions 360p utilisent des thèmes 480×360 Y1 plus nets. Faites correspondre la résolution de build aux thèmes que vous souhaitez utiliser ([Guide 240p contre 360p](rockbox-y1/resolution.html)).
  - Type A contre Type B — Type A concerne les lecteurs Y1 livrés avec le logiciel d'usine 2.0.0 ou plus récent ; Type B concerne les unités Y1 antérieures. Choisissez Type A sauf si vous savez que votre Y1 est Type B.
  - Stable ou nocturne — Choisissez une version stable pour une écoute quotidienne ou une version nocturne pour tester les dernières modifications.

## Téléchargements directs des développeurs de la communauté

Innioasis Updater CE télécharge toujours les packages de micrologiciels directement auprès des développeurs de micrologiciels de la communauté ([rockbox-y1/rockbox](firmware_fr.html?model=Y1&software=rockbox-y1)), et les développeurs eux-mêmes sont seuls responsables de répertorier leurs versions logicielles dans Updater CE.

Vous pouvez laisser Updater CE télécharger et installer le micrologiciel automatiquement, ou télécharger les packages ROM depuis notre [Rockbox-Y1 page de téléchargement](rockbox-y1/download.html) et [Rockbox ROM page de téléchargement](rockbox-rom-download_fr.html).[Rockbox-Y1 téléchargements](rockbox-y1/download.html)[Installer à partir d'un ZIP local](rockbox-y1/portable-zip.html)

## Comment installer Rockbox-Y1
  - Ouvrez Innioasis Updater CE et définissez Modèle d'appareil à Y1.
  - Sélectionnez Rockbox dans Logiciel.
  - Choisissez une version stable (ou activez les builds nocturnes pour tester un aperçu).
  - Cliquez Installer / Restaurer donc Updater CE télécharge le package directement depuis le développeur.
  - Éteignez complètement le Y1 et connectez-le avec un câble de données USB lorsque Updater CE vous y invite.
  - Attendez le message de fin, puis déconnectez et allumez votre lecteur.

Pour des captures d'écran et des conseils de configuration détaillés, lisez le [tutoriel Rockbox-Y1 complet](guides/rockbox-y1.html).

## Restauration du logiciel Y1 d'origine

Vous pouvez revenir au logiciel d'usine à tout moment : sélectionnez Y1 et Logiciel d'origine dans Updater CE, choisissez une version stable et cliquez sur Installer / Restaurer. Votre musique sur la carte MicroSD est préservée. Voir le [guide de restauration](rockbox-y1/restore-stock.html) et [Y1 Page du logiciel d'origine](original-software-y1_fr.html).

## Questions fréquemment poséesRockbox pour Y1 est-il identique à Rockbox-Y1 ?

Oui. Rockbox, Rockbox-Y1, Rockbox pour Y1 et `rockbox-y1` tous font référence au même port de communauté Rockbox pour le Innioasis Y1.D'où Updater CE télécharge-t-il Rockbox-Y1 ?

Updater CE télécharge toujours les packages de micrologiciels directement à partir des propres versions des développeurs de micrologiciels de la communauté (`rockbox-y1/rockbox`). Les développeurs sont seuls responsables de répertorier leurs versions logicielles dans Updater CE.Puis-je installer Rockbox-Y1 sur un Y2 ?

Non. Le Y2 possède sa propre version de micrologiciel distincte. Utiliser [Rockbox pour l'an 2](rockbox-for-y2_fr.html) plutôt.L'installation de Rockbox-Y1 effacera-t-elle ma musique ?

Non. La musique est stockée sur la carte MicroSD et n'est pas affectée lors du flashage du micrologiciel interne du lecteur.

## Guides associés

### [Rockbox-Concentrateur Y1](rockbox-y1/)

Tous les guides Y1 : installation, téléchargements, thèmes, restauration, double démarrage et dépannage.

### [Rockbox-Y1 contre Rockbox-Y2](rockbox-y1-vs-y2.html)

En quoi les builds Y1 et Y2 Rockbox diffèrent.

### [Rockbox-Thèmes Y1](rockbox-y1-themes.html)

Comment transférer des thèmes 240p et 360p avec Updater CE.

### [Rockbox aperçu](rockbox_fr.html)

Introduction à Rockbox sur les joueurs Innioasis Y1 et Y2.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
