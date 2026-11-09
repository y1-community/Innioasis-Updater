---
title: "Guía de instalación de firmware y restauración de stock | Innioasis Actualizador CE - Innioasis Descargas de firmware"
description: "Instale firmware personalizado o restaure el firmware oficial de fábrica en Innioasis Y1, Y2, G1, G3, G5, R1, PR1 y Timmkoo Q5, Q3 con Innioasis Updater CE."
language: "es"
source: "https://innioasis.app/firmware-guide_es.html"
---

# Guía de instalación de firmware y restauración de stock | Innioasis Actualizador CE - Innioasis Descargas de firmware

Guía de instalación de firmware y restauración de stock

# Instale o restaure el firmware en su dispositivo

Elija el modelo impreso en su reproductor. Luego siga los pasos en Updater CE. Él se encarga del resto.[Obtener Updater CE](guide_es.html#platform)[Explorar el archivo de firmware](firmware_es.html)[Solución de problemas](troubleshooting_es.html)

Elija el modelo impreso en su reproductor y el software que desee, luego abra esta guía. [Busque software y firmware de stock por modelo](firmware_es.html).

## 

[Obtener Updater CE](guide_es.html#download-updater)[Tutorial escrito completo](guide_es.html)

## Obtener Innioasis Updater CE

Aquí es por dónde empezar si aún no tienes Updater CE.Consíguelo en Updater CEcon instalación guiada

### Windows

Descargue el instalador, ábralo y siga las instrucciones de configuración.[Descargar e instalar el controlador](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Descargar aplicaciones y controladores](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[¿Bloqueado por Edge?](#)

Si Windows le impide ejecutar la aplicación o no la inicia, abra Configuración, haga clic en Privacidad y seguridad → Seguridad de Windows → Control de aplicaciones y navegador y desactive el Control inteligente de aplicaciones. [¿Windows no inicia la aplicación? Ayuda](#smart-app-control)

Deberá reiniciar su PC después de la instalación para que funcione.

### macOS

Descarga la aplicación y muévela a Aplicaciones. Si macOS lo bloquea, abra Configuración del sistema, luego Privacidad y seguridad y haga clic en Abrir de todos modos. [¿Cómo funciona esto?](https://support.apple.com/en-gb/102445#openanyway)[Descargar Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Descargue AppImage para sistemas Intel y AMD, hágalo ejecutable y ejecútelo.[Descargar AppImage para Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Notas de configuración de Linux](drivers_es.html#linux)¿Otra plataforma?

¿Necesita notas más extensas sobre la configuración de la computadora? Abre el [Windows](drivers_es.html#windows) o [Linux](drivers_es.html#linux) guía de configuración.

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

Innioasis Actualizador CE es la forma más segura de actualizar tu reproductor. Mantiene tu música, vídeos y emparejamientos Bluetooth. Le indica cuándo están listas las actualizaciones. Se ejecuta en Windows, macOS y Linux. El Innioasis Universal Flash Tool borra tu reproductor y funciona en menos computadoras.[Abrir la comparación completa](updater-comparison_es.html)

### ¿Windows no inicia la aplicación? Cómo desactivar el control inteligente de aplicaciones

Windows Defender SmartScreen o Smart App Control pueden bloquear aplicaciones comunitarias recién descargadas antes de que se propague la reputación de las firmas. Smart App Control está afectando actualmente a aplicaciones populares como Epic Overlay Service (utilizado por Fortnite): Updater CE es seguro y su uso está verificado. Desactivar Smart App Control permite que Updater CE se abra y se ejecute normalmente.
  - Abierto Configuración en su PC con Windows (presione Win + I).
  - Haga clic Privacidad y seguridad en la barra lateral izquierda, luego haga clic Windows Security.
  - Haga clic Control de aplicaciones y navegador.
  - Bajo Control inteligente de aplicaciones, haga clic Configuración de control de aplicaciones inteligentes.
  - Establezca el interruptor en Apagado para permitir que se inicie Updater CE.

¿Bloqueado por Edge? Si Microsoft Edge bloquea la descarga, haga clic en el botón Más opciones (…) → Mantener → Mostrar más → Mantener de todos modos.

Volver a habilitar Smart App Control más tarde: Cuando desee volver a activar Smart App Control, puede volver a habilitarlo a través del Registro de Windows en `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` estableciendo `VerifiedAndReputablePolicyState` a `1` (Activado) o `2` (Modo de evaluación) y reiniciar.Cerrar ayuda

## ¿Fue esto útil?

Su respuesta ayuda a mejorar esta guía.Sí, lo encontré útil.todavía no[Háganos saber cómo podemos mejorar](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
