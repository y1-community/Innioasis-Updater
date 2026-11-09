---
title: "Pilotes Innioasis Y1 et Y2 USB | Pilote Windows et autorisations Linux - Innioasis Updater"
description: "Configurez votre ordinateur pour les autorisations Innioasis Updater : pilote Windows MediaTek et Linux USB, ainsi que des correctifs de câble et de synchronisation."
language: "fr"
source: "https://innioasis.app/drivers_fr.html"
---

# Pilotes Innioasis Y1 et Y2 USB | Pilote Windows et autorisations Linux - Innioasis Updater

Configuration de l'ordinateur

# Préparez l'ordinateur avant le joueur.

La plupart des problèmes de connexion proviennent du pilote, des autorisations, du câble ou de la synchronisation. Windows a besoin que le pilote MediaTek soit installé. Linux a besoin des autorisations USB appropriées. Trouvez votre plateforme ci-dessous.[Obtenir Updater CE](guide_fr.html#platform)[Dépannage](troubleshooting_fr.html)

## Windows
  - Téléchargez le programme d'installation du pilote MediaTek ci-dessous.
  - Exécutez le programme d'installation et autorisez Windows à installer le pilote.
  - Redémarrez l'ordinateur.
  - Ouvrez Updater CE et attendez l'invite de connexion avant de brancher le lecteur éteint.

Certains systèmes Windows bloquent le pilote via l'isolation Core (intégrité de la mémoire). Si Updater CE ne parvient toujours pas à voir le lecteur après un redémarrage, désactivez l'intégrité de la mémoire dans la sécurité Windows, redémarrez et réinstallez le pilote. Réactivez le paramètre lorsque vous avez terminé si votre système le permet.

Windows ne lance pas l'application ? Si la sécurité Windows ou Smart App Control empêche l'ouverture de Updater CE, ouvrez Paramètres (presse Win + I) → Confidentialité et sécurité → Windows Security → Contrôle des applications et du navigateur → Paramètres de contrôle des applications intelligentes et réglez-le sur Désactivé. Le Contrôle intelligent des applications affecte actuellement des applications populaires comme Epic Overlay Service (utilisé par Fortnite) — Updater CE est sûr et vérifié. Pour le réactiver ultérieurement, définissez `VerifiedAndReputablePolicyState` à `1` (Activé) ou `2` (Mode d'évaluation) sous `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` dans l'Éditeur du Registre.[Télécharger le pilote Windows](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Retour au guide principal](guide_fr.html#windows) · [Téléchargements de logiciels](firmware_fr.html)

## Autorisations Linux USB

Linux a besoin que votre compte utilisateur soit autorisé à communiquer avec la puce MediaTek USB à l'intérieur du lecteur. Updater CE règle généralement ce problème lors de l'installation, et la même autorisation couvre SP Flash Tool, alors traitez cela comme une étape de réparation plutôt que comme une étape normale.
  - Exécutez Updater CE en tant qu'utilisateur normal, pas en tant que root. Le programme d'installation demande l'accès administrateur uniquement lorsqu'il en a besoin.
  - Vérifiez que le lecteur est visible. Éteignez le lecteur, connectez le câble et exécutez la commande lsusb dans un terminal. Un lecteur connecté apparaît comme un appareil MediaTek avec l'ID de fournisseur 0e8d.
`lsusb`
  - S'il apparaît dans lsusb mais que Innioasis Updater CE ou SP Flash Tool indique une autorisation refusée ou ne peut pas ouvrir le port, votre utilisateur n'a pas accès au périphérique USB. La même règle udev couvre les deux outils, alors ajoutez-en une qui permet au groupe d'utilisateurs de la lire.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Enregistrez cette ligne dans un nouveau fichier nommé /etc/udev/rules.d/51-innioasis.rules, puis exécutez :`sudo udevadm control --reload && sudo udevadm trigger`
  - Débranchez complètement le lecteur, rebranchez-le et réessayez l'installation.
  - Si SP Flash Tool signale une autorisation série ou une course aux ports, débranchez complètement et reconnectez-vous uniquement lorsque vous y êtes invité.
N'improvisez pas les décalages de flash.Si vous passez à un outil de récupération manuelle, utilisez les fichiers et la configuration spécifique au modèle livrés avec le projet.

[Retour au guide principal](guide_fr.html#linux) · [Téléchargements de logiciels](firmware_fr.html) · [SP Flash Tool guide](sp-flash-tool_fr.html)

## Câble et synchronisation
  - Utilisez un câble de données USB connu.
  - Évitez les hubs lors du dépannage.
  - Éteignez complètement le bon modèle.
  - Connectez-vous uniquement à l'invite.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
