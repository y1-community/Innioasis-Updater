---
title: "Innioasis Y2 La molette de défilement ne fonctionne pas après la mise à jour | Innioasis Archives du micrologiciel - Innioasis Téléchargements du micrologiciel"
description: "Innioasis Y2 la molette de défilement ou la molette cliquable ne fonctionnent pas après une mise à jour ? Réinstallez le logiciel d&#39;origine Y2, vérifiez l&#39;anneau et séparez le micrologiciel des défauts matériels."
language: "fr"
source: "https://innioasis.app/guides/y2-scroll-wheel-not-working_fr.html"
---

# Innioasis Y2 La molette de défilement ne fonctionne pas après la mise à jour | Innioasis Archives du micrologiciel - Innioasis Téléchargements du micrologiciel

Récupération du joueur · Innioasis Y2

# Innioasis Y2 la molette de défilement ne fonctionne pas après une mise à jour

La roue tourne mais le joueur l'ignore, ou la molette cliquable s'arrête juste après un flash. Voici comment distinguer une erreur de firmware d'une erreur matérielle sur le Y2.[Obtenir Updater CE](../guide_fr.html#platform)[Y2 téléchargements de logiciels](../firmware_fr.html?model=Y2&software=original-y2)[Guide de récupération](recovery_fr.html)

## Déterminez si la roue ou le firmware est en cause

Sur un Y2, la roue est une entrée physique, mais le micrologiciel décide de l'effet de chaque tour et clic. Une roue qui s'arrêtait dès que vous mettiez à jour ou flashiez des points sur le logiciel. Une roue qui ignore tous les logiciels (stock, Rockbox ou écran de récupération) pointe vers la pièce.
  - Fonctionne dans un logiciel, mort dans un autre : défaut du micrologiciel.
  - Mort sur tous les écrans, y compris la récupération : roue, ruban ou planche.
  - Une seule direction manque : généralement des débris sous la bague ou de l'usure.
  - La roue tourne mais rien ne ressort : le lecteur peut être gelé – forcez d’abord un redémarrage.

## Vérifications rapides avant de réinstaller le firmware
  - Maintenez le bouton d'alimentation enfoncé pendant environ 15 secondes pour forcer l'arrêt du lecteur, puis démarrez-le normalement.
  - Testez la molette sur l'écran d'accueil, dans Paramètres et dans le lecteur de musique.
  - Appuyez sur les boutons physiques. Si la puissance et le retour répondent mais que la roue ne le fait pas, la faute vient de la roue elle-même.
  - Chargez le lecteur pendant 30 minutes avec un câble de données connu.
  - Si vous avez installé Rockbox pour Y2 ou une autre version personnalisée, revenez au logiciel d'origine et testez à nouveau.

## Réinstallez le firmware Y2 correspondant à votre lecteur

La roue est entraînée par le micrologiciel, donc un échec lié à la mise à jour est corrigé en remettant le logiciel d'origine Y2 correct sur le lecteur. N'utilisez jamais un package Y1 sur un Y2 et ne choisissez pas une version "assez proche" - les packages Y2 sont conçus pour le matériel Y2.
  - Ouvert [Programme de mise à jour CE](../guide_fr.html#platform) sur votre ordinateur.
  - Ensemble Modèle d'appareil à Y2.
  - Choisissez Logiciel d'origine dans Logiciel et choisissez une version stable Y2 - le package manuel est `rom_y2.zip`.
  - Cliquez Installer / Restaurer et laissez le paquet extraire.
  - Éteignez complètement le Y2, connectez le câble de données USB uniquement lorsque le programme de mise à jour le demande et laissez-le jusqu'au message de réussite.
Faites correspondre le modèle et la version. Si la liste des versions ressemble à Y1 logiciel, arrêtez et resélectionnez Y2. Les étapes complètes sont dans le [Guide de restauration Y2](restore-original-y2_fr.html).

## Vérifiez l'anneau de roue pour déceler des débris ou des dommages

Si la roue est rigide, colle ou ne tombe en panne que dans une direction, des peluches et des graviers peuvent se trouver entre l'anneau et le boîtier. Éteignez le lecteur et essuyez autour de l'anneau avec un chiffon en microfibre sec. Ne faites pas couler de nettoyants ou d'alcool dans l'espace et ne soulevez pas l'anneau.

Si l'anneau est desserré, fissuré ou ne clique plus, le joueur a besoin d'une réparation. Le micrologiciel ne peut pas réparer une roue endommagée, un ruban déconnecté ou un liquide endommagé.

## Si le joueur ne démarre pas non plus

Un échec de mise à jour peut empêcher le Y2 de démarrer, ce qui ressemble à une panne de roue car aucune entrée ne répond. Travailler à travers le [Y2 n'active pas le guide](y2-wont-turn-on_fr.html) pour le chargement, le redémarrage forcé et la récupération manuelle.

## Innioasis Y2 FAQ sur la molette de défilement

### Pourquoi ma molette de défilement Innioasis Y2 a-t-elle cessé de fonctionner après une mise à jour ?

Une mise à jour peut laisser le pilote de roue déphasé par rapport au reste du firmware, surtout si le flash a été interrompu ou si un package Y1 a été utilisé. Réinstallez la version Y2 du logiciel d'origine pour votre modèle et testez la roue sur l'écran d'accueil d'origine.

### Comment puis-je savoir si la molette cliquable Y2 est cassée ou si le micrologiciel est défectueux ?

Testez la roue dans plusieurs logiciels. Si cela fonctionne dans le logiciel d'origine mais pas dans Rockbox, il s'agit d'un problème de mappage du micrologiciel. S'il ne fait rien sur aucun écran, y compris un menu de récupération, suspectez la roue, son ruban ou le tableau.

### La restauration du logiciel d'origine corrigera-t-elle la molette de défilement Y2 ?

Il corrige les échecs causés par une mise à jour ou un package incompatible, et c'est la première chose à essayer. Il ne réparera pas une roue physiquement endommagée, un ruban lâche ou un dommage liquide.

### Puis-je utiliser un progiciel Y1 pour résoudre un problème de roue Y2 ?

Non. Les packages Y1 et Y2 ne sont pas interchangeables, et flasher le mauvais modèle peut aggraver les commandes. Faites correspondre le modèle et la version avant d'exécuter l'installation/restauration.

## Correctifs associés
  - [La molette de défilement Y1 ne fonctionne pas](y1-scroll-wheel-not-working_fr.html) — les mêmes contrôles pour le Y1
  - [Y2 ne s'allume pas](y2-wont-turn-on_fr.html) - récupération de l'alimentation et du démarrage
  - [Innioasis guide de récupération](recovery_fr.html) - tous les guides de symptômes en un seul endroit
  - [Dépannage d'une installation](../troubleshooting_fr.html) — à quoi ressemble un flash défaillant
  - [Restaurer Y2 logiciel d'origine](restore-original-y2_fr.html) - la procédure pas à pas de restauration complète

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
