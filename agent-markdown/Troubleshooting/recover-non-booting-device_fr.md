---
title: "Comment récupérer un lecteur MediaTek qui ne démarre pas après un échec du client MTK · Innioasis Communauté"
description: "Guide étape par étape pour débloquer et récupérer les lecteurs Innioasis Y1, Y2, G1, Timmkoo et MediaTek qui ne démarrent pas après que MTKclient ait interrompu les flashs sous Linux ou macOS."
language: "fr"
source: "https://innioasis.app/Troubleshooting/recover-non-booting-device_fr.html"
---

# Comment récupérer un lecteur MediaTek qui ne démarre pas après un échec du client MTK · Innioasis Communauté

Dépannage et récupération de périphérique

# Récupération d'un périphérique qui ne démarre pas après le clignotement du client MTK

Si votre appareil Innioasis Y1, Y2 ou MediaTek ne parvient pas à s'allumer ou affiche un écran noir après avoir flashé avec MTKclient sur macOS ou Linux, ne paniquez pas. La BootROM matérielle (BROM) est permanente et ne peut pas être détruite.

## Pourquoi MTKclient peut bloquer ou laisser un écran noir

MTKclient s'appuie sur des charges utiles d'exploit logiciel (kamakiri / amonet) pour contourner l'authentification DA et la communication brute USB via libusb. Sur les systèmes macOS et Linux ARM64 :
  - USB la latence de la prise de contact ou les délais d'attente des ports sur macOS peuvent bloquer l'injection de la charge utile DA en cours de transfert.
  - Les en-têtes de partition manquants ou incomplets laissent le chargeur de démarrage (preloader / lk) dans un état qui ne répond pas.
  - Le lecteur semble complètement mort : pas de LED, pas d'icône de chargement, pas de rétroéclairage de l'écran.

Même dans cet état, le chipset MediaTek retombe dans Mode BROM (USB VID 0e8d, PID 0003), prêt pour la récupération officielle de bas niveau.

## La méthode de récupération définitive : SP Flash Tool Moteur dans Updater CE

Le moyen le plus sûr et le plus fiable de récupérer votre lecteur brické consiste à utiliser Programme de mise à jour CE configuré avec le fonctionnaire SP Flash Tool back-end.

### Étapes exactes dans Updater CE :
  - Ouvert Programme de mise à jour CE.
  - Cliquez Paramètres dans la barre latérale de navigation de gauche.
  - Faites défiler jusqu'à la section Avancé et activez Afficher les paramètres avancés.
  - Sous Méthode d'installation (ou Moteur clignotant pour le programme d'installation de MediaTek), localisez le Méthode Flash dérouler.
  - Changer la sélection de Automatique (recommandé) ou MTKClient à SP Flash Tool.
  - Confirmez l'invite et revenez au flux d'installation principal.

## Architecture de plate-forme et exigences du système d'exploitation pour SP Flash Tool

Officiel de MediaTek `SP Flash Tool` Le binaire est compilé nativement en tant que x86_64 binaire ELF pour Linux et un Exécutable PE32+ pour Windows x64.Remarque importante sur le matériel pour les utilisateurs de macOS et ARM64 Linux :
 Étant donné que MediaTek ne compile pas SP Flash Tool pour macOS (Darwin) ou Linux ARM64 (aarch64), les utilisateurs de macOS et les utilisateurs de Linux ARM64 (tels que Raspberry Pi ou Apple Silicon exécutant Asahi Linux) confrontés à une brique doivent connecter leur lecteur à : 
  - Un PC Windows x64 (Windows 10/11 64 bits), ou
  - Un PC Linux x86_64 (Ubuntu, Debian, Fedora, Arch 64 bits).

## Processus de déblocage du matériel étape par étape
  - Déconnectez le lecteur : Débranchez complètement le câble USB du lecteur et du PC.
  - Mise hors tension matérielle : Maintenez le bouton d'alimentation (ou Power + Volume Down) pendant 15 secondes pour vous assurer que le chipset est complètement éteint et n'est pas coincé dans une boucle USB à faible consommation.
  - Lancez Updater CE avec le mode SP Flash Tool : Sélectionnez le modèle de votre appareil (par ex. Innioasis Y1 ou Innioasis Y2) et choisissez Logiciel d'origine pour restaurer les partitions d'origine.
  - Lancer l'installation/restauration : Cliquez Installer / Restaurer dans Updater CE. Attendez que l'invite d'état indique En attendant le joueur...
  - Insérez le câble USB pour déclencher le BROM : Lorsque l'appareil est éteint, branchez le câble USB directement sur un port USB de la carte mère haute vitesse (évitez les hubs USB non alimentés).
  - Le système détectera le port VCOM MediaTek, poussera l'agent de téléchargement (DA), réécrira les tables de partition et restaurera proprement toutes les images du micrologiciel.

## Permutations par modèle et système d'exploitation

| Modèle | Plateforme en échec | Configuration de récupération recommandée | Moteur et modes |
| --- | --- | --- | --- |
| Innioasis Y1 | macOS (Apple Silicon/Intel) | PC Windows x64 / Linux x86_64 | SP Flash Tool + Y1 Actions ROM |
| Innioasis Y1 | LinuxARM64/x86_64 | PC Linux x86_64 ou Windows x64 | SP Flash Tool + DA de la communauté |
| Innioasis Y2 | macOS (MTKclient bloqué) | PC Windows x64 / Linux x86_64 | SP Flash Tool + Y2 Récupération de dispersion |
| Innioasis G1 / G3 / G5 | Client MTK macOS / Linux | PC Windows x64 avec pilotes VCOM | SP Flash Tool + Micrologiciel d'usine |
| Mechen H1 / Timmkoo A5 | N'importe quelle plateforme | PC Windows x64 ou Linux x86_64 | SP Flash Tool + Fichier scatter |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
