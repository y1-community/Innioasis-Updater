---
title: "Problèmes de lancement d'application Windows 10/11 et solution de contournement Smart App Control - Innioasis Updater"
description: "Si Windows 10/11 ou Smart App Control vous empêche de lancer l&#39;application, suivez la solution de contournement ici."
language: "fr"
source: "https://innioasis.app/notices/2026-11-07-codesigning_fr.html"
---

# Problèmes de lancement d'application Windows 10/11 et solution de contournement Smart App Control - Innioasis Updater

Du 2026-10-25 · jusqu'au 2026-12-31 · Modèles : Y1,Y2

# Problèmes de lancement d'application Windows 10/11 et solution de contournement Smart App Control

Si Windows 10/11 ou Smart App Control vous empêche de lancer l'application, suivez la solution de contournement ici.

Du 2026-10-25 · jusqu'au 2026-12-31 · Modèles : Y1,Y2

Des rapports de faux positifs ont été soumis à Microsoft pour `installer.exe` et `InnioasisUpdater.exe` et actionné, mais si Windows Endpoint Protection ou Smart App Control bloque toujours l'application sur votre ordinateur, utilisez cette solution de contournement :

### Solution de contournement temporaire : désactivez le contrôle des applications intelligentes
  - Ouvrir Windows Paramètres (presse `Win + I`).
  - Aller à Confidentialité et sécurité > Sécurité Windows > Contrôle des applications et du navigateur.
  - Sous Contrôle intelligent des applications, cliquez Paramètres de contrôle des applications intelligentes.
  - Réglez le contrôle des applications intelligentes sur Désactivé. Cela permet immédiatement à l'application de s'ouvrir et de s'exécuter.

Si Windows ou Edge vous empêche de télécharger Updater CE, cliquez sur plus d'options (…) alors Garder > Afficher plus > Gardez quand même.

### Réactivation du contrôle des applications intelligentes

Une fois la mise à jour des définitions de faux positifs terminée sur votre ordinateur, vous pouvez réactiver Smart App Control via le registre Windows :
  - Presse Touche Windows + R, taper `regedit`et appuyez sur Entrée pour ouvrir l'Éditeur du Registre en tant qu'administrateur.
  - Accédez à : `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (ou `Policies`).
  - Situer `VerifiedAndReputablePolicyState` dans le volet de droite.
  - Double-cliquez `VerifiedAndReputablePolicyState` et modifiez ses données de valeur en :

  - `1` = Activé (Forcé)
  - `2` = Mode d'évaluation

  - Cliquez sur OK, fermez l'éditeur de registre et redémarrez votre ordinateur.

[Voir le rapport installer.exe à Microsoft](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[Voir le rapport InnioasisUpdater.exe à Microsoft](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[Ouvrez la page liée](https://innioasis.app/notices.html)

[← Tous les avis](index_fr.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
