---
title: "Comenzando con Innioasis Actualizador CE | Instale o restaure el firmware en cualquier reproductor Innioasis o Timmkoo - Innioasis Actualizador"
description: "Descargue Innioasis Updater CE para Windows, macOS o Linux, luego instale o restaure el firmware en cualquier reproductor Innioasis o Timmkoo en unos pocos pasos guiados."
language: "es-419"
source: "https://innioasis.app/guide_es-419.html"
---

# Comenzando con Innioasis Actualizador CE | Instale o restaure el firmware en cualquier reproductor Innioasis o Timmkoo - Innioasis Actualizador

Inicio rápido

# Comenzando con Innioasis Updater CE

Funciona con todos los reproductores de audio Innioasis y Timmkoo. Instale Innioasis Updater CE en su computadora, elija su modelo y el software que desee, luego siga las instrucciones.

## 

[Obtener Updater CE](guide_es-419.html#download-updater)[Tutorial escrito completo](guide_es-419.html)

## Obtener Innioasis Updater CE

Innioasis Actualizador CE es la aplicación que instala actualizaciones oficiales y software comunitario en tu reproductor. Conserva tu música y tu configuración y se ejecuta en Windows, macOS y Linux.

### Windows

Descargue el instalador, ejecútelo y luego reinicie su PC cuando finalice.[Obtener controladores](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Descargar Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)

If Windows stops you from running the app or won't launch it, please open Settings, click Privacy & security → Windows Security → App & browser control, and turn Smart App Control off. [Windows won't launch the app? Help](#smart-app-control)

Reinicie su PC después de la instalación. La ayuda al conductor está en el [Notas de configuración de Windows](drivers_es-419.html#windows).

### macos[Descargar Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

Si su Mac le impide ejecutar la aplicación por primera vez, abra Configuración del sistema, haga clic en Privacidad y seguridad, desplácese hacia abajo y haga clic [Abierto de todos modos.](https://support.apple.com/en-gb/102445#openanyway)

Funciona en Mac Intel y Apple Silicon con macOS Monterey y versiones posteriores.

### linux

Descargue AppImage para sistemas Intel y AMD, hágalo ejecutable y ejecútelo.[Descargar AppImage para Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)

[Notas de configuración de Linux](drivers_es-419.html#linux)¿Otra plataforma?

Necesitas tu reproductor, un cable de datos USB que transporte datos (no se puede instalar un cable de solo carga) y unos minutos. Mantenga el cable conectado hasta que Updater CE indique que está listo.

## Elija su modelo y software
  - Modelo de dispositivo: elige el modelo impreso en el reproductor, Y1 o Y2. El software creado para un modelo no se puede instalar en el otro.
  - Software y lanzamiento: elija Software original, Rockbox, Solar, JJ Launcher, Inniclassic, Y2Player o Koensayr cuando aparezca en la lista para su modelo, luego elija una versión. Estable es la opción segura.
  - Instalar: hacer clic Instalar / Restaurar, apague el reproductor por completo y conecte el cable USB solo cuando Updater CE lo solicite.
  - Finalizar: deje el reproductor y el cable en paz hasta que aparezca el mensaje de éxito, luego desconecte e inicie el reproductor.

Y1 los reproductores que se enviaron con software original anterior a 2.0.0 necesitan Dispositivo Type B. Todos los demás mantienen el valor predeterminado Type A.Instrucciones de conexión del actualizador para conectar un reproductor apagadoSiga las indicaciones en vivo del Updater CE para su modelo.

## Volver al software original

El software personalizado es reversible. En Updater CE, elija su modelo, seleccione Software original, elija una versión estable y luego ejecute Instalar / Restaurar de la misma manera. No hay nada que borrar a mano.[Guía de restauración de Y1](guides/restore-original-y1.html)[guía de restauración Y2](guides/restore-original-y2.html)

Si el flash se detiene antes del mensaje USB, verifique primero el cable, la configuración de la plataforma y el modelo. Ver [solución de problemas](troubleshooting_es-419.html) para correcciones, el [Guía de recuperación de Y1 y Y2](guides/recovery.html) por fallas de potencia y ruedas, y [SP Flash Tool](sp-flash-tool_es-419.html) para una recuperación avanzada.

## Guías de software por modelo.

Abra la guía para su modelo y el software que eligió.

### Innioasis Y1

Software para Y1:

### Innioasis Y2

Software para Y2:

## ¿Qué herramienta debo utilizar?

Esta guía utiliza Innioasis Actualizador 2.5.1, también llamado Actualizador CE. Mantiene seguros sus canciones, vídeos y emparejamientos de Bluetooth. Le indica cuándo están listas las actualizaciones. El Innioasis Universal Flash Tool borra tu reproductor y necesita pasos manuales. [Compara las herramientas →](updater-comparison_es-419.html)

## Windows won't launch the app? Smart App Control workaround

Windows Defender SmartScreen or Smart App Control can block newly downloaded community applications before signature reputations propagate. Turning Smart App Control off allows Updater CE to open and run normally.
  - Abierto Configuración on your Windows PC (press Win + I).
  - Haga clic Privacy & security in the left sidebar, then click Windows Security.
  - Haga clic App & browser control.
  - Bajo Smart App Control, click Smart App Control settings.
  - Set the toggle to Off to allow Updater CE to launch.

Downloaded via Edge? If Edge blocks the download itself, click the More options button (…) → Keep → Show more → Keep anyway.

Re-enabling Smart App Control later: When you want to turn Smart App Control back on, you can re-enable it via the Windows Registry under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` by setting `VerifiedAndReputablePolicyState` a `1` (On) or `2` (Evaluation Mode) and restarting.

### Windows won't launch the app? How to turn off Smart App Control

Windows Defender SmartScreen or Smart App Control can block newly downloaded community applications before signature reputations propagate. Turning Smart App Control off allows Updater CE to open and run normally.
  - Abierto Configuración on your Windows PC (press Win + I).
  - Haga clic Privacy & security in the left sidebar, then click Windows Security.
  - Haga clic App & browser control.
  - Bajo Smart App Control, click Smart App Control settings.
  - Set the toggle to Off to allow Updater CE to launch.

¿Bloqueado por Edge? If Microsoft Edge blocks the download itself, click the More options button (…) → Keep → Show more → Keep anyway.

Re-enabling Smart App Control later: When you want to turn Smart App Control back on, you can re-enable it via the Windows Registry under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` by setting `VerifiedAndReputablePolicyState` a `1` (On) or `2` (Evaluation Mode) and restarting.Close help

## ¿Fue esto útil?

Su respuesta ayuda a mejorar esta guía.Sí, lo encontré útil.todavía no[Háganos saber cómo podemos mejorar](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
