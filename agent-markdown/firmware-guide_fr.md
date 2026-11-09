---
title: "Guide d'installation du micrologiciel et de restauration des stocks | Innioasis Updater CE - Innioasis Téléchargements du micrologiciel"
description: "Installez un micrologiciel personnalisé ou restaurez le micrologiciel officiel d&#39;usine sur Innioasis Y1, Y2, G1, G3, G5, R1, PR1 et Timmkoo Q5, Q3 avec Innioasis Updater CE."
language: "fr"
source: "https://innioasis.app/firmware-guide_fr.html"
---

# Guide d'installation du micrologiciel et de restauration des stocks | Innioasis Updater CE - Innioasis Téléchargements du micrologiciel

Guide d'installation du micrologiciel et de restauration des stocks

# Installer ou restaurer le micrologiciel sur votre appareil

Choisissez le modèle imprimé sur votre lecteur. Suivez ensuite les étapes de Updater CE. Il gère le reste.[Obtenir Updater CE](guide_fr.html#platform)[Parcourir les archives du micrologiciel](firmware_fr.html)[Dépannage](troubleshooting_fr.html)

Choisissez le modèle imprimé sur votre lecteur et le logiciel souhaité, puis ouvrez ce guide. [Parcourir les logiciels et les micrologiciels de stock par modèle](firmware_fr.html).

## 

[Obtenir Updater CE](guide_fr.html#download-updater)[Tutoriel écrit complet](guide_fr.html)

## Obtenez Innioasis Updater CE

Voici par où commencer si vous n'avez pas déjà Updater CE.Obtenez-le sur Updater CEavec installation guidée

### Windows

Téléchargez le programme d'installation, ouvrez-le et suivez les invites de configuration.[Télécharger et installer le pilote](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Télécharger l'application et les pilotes](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Bloqué par Edge ?](#)

Si Windows vous empêche d'exécuter l'application ou ne la lance pas, veuillez ouvrir Paramètres, cliquez sur Confidentialité et sécurité → Sécurité Windows → Contrôle des applications et du navigateur, puis désactivez Smart App Control. [Windows ne lance pas l'application ? Aide](#smart-app-control)

Vous devrez redémarrer votre PC après l'installation pour que cela fonctionne.

### macOS

Téléchargez l'application et déplacez-la vers Applications. Si macOS le bloque, ouvrez Paramètres système, puis Confidentialité et sécurité, et cliquez sur Ouvrir quand même. [Comment ça marche](https://support.apple.com/en-gb/102445#openanyway)[Télécharger Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Téléchargez l'AppImage pour les systèmes Intel et AMD, rendez-la exécutable et exécutez-la.[Téléchargez AppImage pour Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Notes de configuration Linux](drivers_fr.html#linux)Une autre plateforme ?

Besoin de notes plus longues sur la configuration de l'ordinateur ? Ouvrez le [Windows](drivers_fr.html#windows) ou [Linux](drivers_fr.html#linux) guide de configuration.

## Revenir au logiciel d'origine

Pour revenir en arrière, choisissez votre modèle, choisissez Logiciel d'origine, puis exécutez Installer / Restaurer. C'est tout. Updater remplace le logiciel système pour vous.[Guide de restauration Y1](guides/restore-original-y1.html)[Guide de restauration Y2](guides/restore-original-y2.html)

## Guides logiciels par modèle

Choisissez votre modèle, puis ouvrez le guide de votre logiciel.

### Innioasis Y1

Logiciel pour Y1 :

### Innioasis Y2

Logiciel pour Y2 :

Une note sur les deux outils

## Quel outil dois-je utiliser ?

Innioasis Programme de mise à jour CE est le moyen le plus sûr de mettre à jour votre lecteur. Il conserve votre musique, vos vidéos et vos appairages Bluetooth. Il vous indique quand les mises à jour sont prêtes. Il fonctionne sous Windows, macOS et Linux. Le Innioasis Universal Flash Tool efface votre lecteur et fonctionne sur moins d'ordinateurs.[Ouvrir la comparaison complète](updater-comparison_fr.html)

### Windows ne lance pas l'application ? Comment désactiver le contrôle intelligent des applications

Windows Defender SmartScreen ou Smart App Control peut bloquer les applications communautaires nouvellement téléchargées avant que les réputations de signature ne se propagent. Smart App Control a actuellement un impact sur des applications populaires telles que Epic Overlay Service (utilisé par Fortnite) – Updater CE est sûr et vérifié à utiliser. La désactivation de Smart App Control permet à Updater CE de s’ouvrir et de fonctionner normalement.
  - Ouvert Paramètres sur votre PC Windows (appuyez sur Win + I).
  - Cliquez Confidentialité et sécurité dans la barre latérale gauche, puis cliquez sur Windows Security.
  - Cliquez Contrôle des applications et du navigateur.
  - Sous Contrôle intelligent des applications, cliquez Paramètres de contrôle des applications intelligentes.
  - Réglez la bascule sur Désactivé pour permettre à Updater CE de se lancer.

Bloqué par Edge ? Si Microsoft Edge bloque le téléchargement lui-même, cliquez sur le bouton Plus d'options (…) → Garder → Afficher plus → Gardez quand même.

Réactivation ultérieure de Smart App Control : Lorsque vous souhaitez réactiver Smart App Control, vous pouvez le réactiver via le registre Windows sous `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` en définissant `VerifiedAndReputablePolicyState` à `1` (Activé) ou `2` (Mode d'évaluation) et redémarrage.Fermer l'aide

## Était-ce utile ?

Votre réponse contribue à améliorer ce guide.Oui, je l'ai trouvé utilePas encore[Faites-nous savoir comment nous pouvons nous améliorer](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
