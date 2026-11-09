---
title: "Guía de instalación de firmware y restauración de stock | Innioasis Actualizador CE - Innioasis Descargas de firmware"
description: "Instale firmware personalizado o restaure el firmware oficial de fábrica en Innioasis Y1, Y2, G1, G3, G5, R1, PR1 y Timmkoo Q5, Q3 con Innioasis Updater CE."
language: "es-419"
source: "https://innioasis.app/firmware-guide_es-419.html"
---

# Guía de instalación de firmware y restauración de stock | Innioasis Actualizador CE - Innioasis Descargas de firmware

Guía de instalación de firmware y restauración de stock

# Instale o restaure el firmware en su dispositivo

Elija el modelo impreso en su reproductor. Luego siga los pasos en Updater CE. Él se encarga del resto.[Obtener Updater CE](guide_es-419.html#platform)[Explorar el archivo de firmware](firmware_es-419.html)[Solución de problemas](troubleshooting_es-419.html)

Elija el modelo impreso en su reproductor y el software que desee, luego abra esta guía. [Busque software y firmware de stock por modelo](firmware_es-419.html).

## 

[Obtener Updater CE](guide_es-419.html#download-updater)[Tutorial escrito completo](guide_es-419.html)

## Obtener Innioasis Updater CE

Aquí es por dónde empezar si aún no tienes Updater CE.Consíguelo en Updater CEcon instalación guiada

### Windows

Descargue el instalador, ábralo y siga las instrucciones de configuración.[Descargar e instalar el controlador](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Descargar aplicaciones y controladores](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[¿Bloqueado por Edge?](#)

If Windows stops you from running the app or won't launch it, please open Settings, click Privacy & security → Windows Security → App & browser control, and turn Smart App Control off. [Windows won't launch the app? Help](#smart-app-control)

Deberá reiniciar su PC después de la instalación para que funcione.

### macos

Descarga la aplicación y muévela a Aplicaciones. Si macOS lo bloquea, abra Configuración del sistema, luego Privacidad y seguridad y haga clic en Abrir de todos modos. [¿Cómo funciona esto?](https://support.apple.com/en-gb/102445#openanyway)[Descargar Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### linux

Descargue AppImage para sistemas Intel y AMD, hágalo ejecutable y ejecútelo.[Descargar AppImage para Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Notas de configuración de Linux](drivers_es-419.html#linux)¿Otra plataforma?

¿Necesita notas más extensas sobre la configuración de la computadora? Abre el [Windows](drivers_es-419.html#windows) o [linux](drivers_es-419.html#linux) guía de configuración.

## Volver al software original

Para volver, elige tu modelo, elige Software original, luego corre Instalar / Restaurar. Eso es todo. El actualizador reemplaza el software del sistema por usted.[Guía de restauración de Y1](guides/restore-original-y1.html)[guía de restauración Y2](guides/restore-original-y2.html)

## Guías de software por modelo.

Elija su modelo, luego abra la guía de su software.

### Innioasis Y1

Software para Y1:

### Innioasis Y2

Software para Y2:

Una nota sobre las dos herramientas.

## ¿Qué herramienta debo utilizar?

Innioasis Actualizador CE es la forma más segura de actualizar tu reproductor. Mantiene tu música, vídeos y emparejamientos Bluetooth. Le indica cuándo están listas las actualizaciones. Se ejecuta en Windows, macOS y Linux. El Innioasis Universal Flash Tool borra tu reproductor y funciona en menos computadoras.[Abrir la comparación completa](updater-comparison_es-419.html)

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
