---
title: "Innioasis Updater dépannage | Problèmes d'installation de Innioasis et Timmkoo - Innioasis Updater"
description: "Correction de Innioasis Updater installations sur n&#39;importe quel lecteur Innioasis ou Timmkoo. Vérifiez le modèle, le câble, le pilote, le moment de la mise hors tension et l&#39;endroit où l&#39;installation s&#39;est arrêtée, puis faites-le clignoter à nouveau."
language: "fr"
source: "https://innioasis.app/troubleshooting_fr.html"
---

# Innioasis Updater dépannage | Problèmes d'installation de Innioasis et Timmkoo - Innioasis Updater

Dépannage

# Recherchez le point où l'installation s'est arrêtée.

Où est-ce que ça s’est arrêté ? Cela vous indique quoi réparer.[Retour au guide normal](guide_fr.html)[Vérifier le micrologiciel](firmware_fr.html)

## Il s'est arrêté avant l'invite USB

Il s'agit d'un problème informatique et non d'un problème de câble. Vérifiez votre modèle. Décompressez à nouveau le fichier. Alors essaye Installer / Restaurer. Si la liste des versions est vide, ouvrez le [répertoire du micrologiciel](firmware_fr.html).

## Il ne peut pas se connecter au lecteur
  - Éteignez complètement le bon Y1 ou Y2.
  - Débranchez le câble, fermez les autres outils Flash ou Android et relancez l'installation.
  - Connectez-vous uniquement lorsque le programme de mise à jour indique qu'il est prêt.
  - Utilisez un câble de données court USB directement dans l'ordinateur, pas un hub si possible.
  - Sous Windows, réinstallez le pilote MediaTek et redémarrez. Sous Linux, vérifiez les autorisations USB/serial.
Invite de connexion du programme de mise à jourL’invite Live Updater fait autorité pour le modèle et la plate-forme actuels.

## Il a détecté le lecteur mais le flash a échoué

Arrêtez ici. N'essayez pas un autre modèle. Fermez les autres outils, vérifiez que vous avez choisi le bon Y1 ou Y2 et utilisez le logiciel d'origine correspondant si le lecteur ne démarre pas. [SP Flash Tool](sp-flash-tool_fr.html) et MTKClient sont inclus si vous en avez besoin, et les fichiers sont sur le [page du micrologiciel](firmware_fr.html).

## Notes sur le pilote Windows

Certaines installations Windows bloquent le pilote MediaTek en raison de l'isolation du noyau. Suivez les conseils de sécurité Windows actuels avant de modifier l'intégrité de la mémoire et réactivez-la lorsque vous avez terminé si votre système le permet.[Ouvrir le guide du conducteur](drivers_fr.html)[Guide d'installation propre](Troubleshooting/clean_install.html)

## La roue ne fonctionne pas ou le lecteur ne démarre pas

Les défauts d’entrée et d’alimentation nécessitent des étapes différentes d’un flash défaillant. Ces guides couvrent les cas courants Y1 et Y2.[Y1 molette de défilement](guides/y1-scroll-wheel-not-working.html)[Y2 molette de défilement](guides/y2-scroll-wheel-not-working.html)[Y1 ne s'allume pas](guides/y1-wont-turn-on.html)[Y2 ne s'allume pas](guides/y2-wont-turn-on.html)[Guide de récupération](guides/recovery.html)

## Toujours bloqué ?

Lorsque vous demandez de l'aide, indiquez le modèle, le système d'exploitation, le message exact du programme de mise à jour, si le lecteur a été détecté et le package/projet que vous avez sélectionné. Ne publiez pas de jetons privés ou de fichiers système sans rapport.[Demander de l'aide](https://discord.gg/zHrT2zrcek)[Entretien du support](support_devs_fr.html#donations)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
