---
title: "Comenzando con Innioasis Actualizador CE | Instale o restaure el firmware en cualquier reproductor Innioasis o Timmkoo - Innioasis Actualizador"
description: "Descargue Innioasis Updater CE para Windows, macOS o Linux, luego instale o restaure el firmware en cualquier reproductor Innioasis o Timmkoo en unos pocos pasos guiados."
language: "es"
source: "https://innioasis.app/guide_es.html"
---

# Comenzando con Innioasis Actualizador CE | Instale o restaure el firmware en cualquier reproductor Innioasis o Timmkoo - Innioasis Actualizador

Inicio rápido

# Comenzando con Innioasis Updater CE

Funciona con todos los reproductores de audio Innioasis y Timmkoo. Instale Innioasis Updater CE en su computadora, elija su modelo y el software que desee, luego siga las instrucciones.

## 

[Obtener Updater CE](guide_es.html#download-updater)[Tutorial escrito completo](guide_es.html)

## Obtener Innioasis Updater CE

Innioasis Actualizador CE es la aplicación que instala actualizaciones oficiales y software comunitario en tu reproductor. Conserva tu música y tu configuración y se ejecuta en Windows, macOS y Linux.

### Windows

Descargue el instalador, ejecútelo y luego reinicie su PC cuando finalice.[Obtener controladores](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Descargar Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)

Si Windows le impide ejecutar la aplicación o no la inicia, abra Configuración, haga clic en Privacidad y seguridad → Seguridad de Windows → Control de aplicaciones y navegador y desactive el Control inteligente de aplicaciones. Smart App Control actualmente afecta a aplicaciones populares como Epic Overlay Service (usado por Fortnite): Updater CE es seguro y su uso está verificado. [¿Windows no inicia la aplicación? Ayuda](#smart-app-control)

Reinicie su PC después de la instalación. La ayuda al conductor está en el [Notas de configuración de Windows](drivers_es.html#windows).

### macOS[Descargar Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

Si tu Mac te impide ejecutar la app por primera vez, abre Ajustes del Sistema, haz clic en Privacidad y seguridad, baja hasta Seguridad y haz clic en [Abierto de todos modos](https://support.apple.com/en-gb/102445#openanyway). También puedes hacer Control-clic (o clic derecho) en la aplicación en el Finder y seleccionar Abrir.

Funciona en Mac Intel y Apple Silicon con macOS Monterey y versiones posteriores.

### Linux

Descargue AppImage para sistemas Intel y AMD, hágalo ejecutable y ejecútelo.[Descargar AppImage para Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)

[Notas de configuración de Linux](drivers_es.html#linux)¿Otra plataforma?

Necesitas tu reproductor, un cable de datos USB que transporte datos (no se puede instalar un cable de solo carga) y unos minutos. Mantenga el cable conectado hasta que Updater CE indique que está listo.

## Elija su modelo y software
  - Modelo de dispositivo: elige el modelo impreso en el reproductor, Y1 o Y2. El software creado para un modelo no se puede instalar en el otro.
  - Software y lanzamiento: elija Software original, Rockbox, Solar, JJ Launcher, Inniclassic, Y2Player o Koensayr cuando aparezca en la lista para su modelo, luego elija una versión. Estable es la opción segura.
  - Instalar: hacer clic Instalar / Restaurar, apague el reproductor por completo y conecte el cable USB solo cuando Updater CE lo solicite.
  - Finalizar: deje el reproductor y el cable en paz hasta que aparezca el mensaje de éxito, luego desconecte e inicie el reproductor.

Y1 los reproductores que se enviaron con software original anterior a 2.0.0 necesitan Dispositivo Type B. Todos los demás mantienen el valor predeterminado Type A.Instrucciones de conexión del actualizador para conectar un reproductor apagadoSiga las indicaciones en vivo del Updater CE para su modelo.

## Volver al software original

El software personalizado es reversible. En Updater CE, elija su modelo, seleccione Software original, elija una versión estable y luego ejecute Instalar / Restaurar de la misma manera. No hay nada que borrar a mano.[Guía de restauración de Y1](guides/restore-original-y1.html)[guía de restauración Y2](guides/restore-original-y2.html)

Si el flash se detiene antes del mensaje USB, verifique primero el cable, la configuración de la plataforma y el modelo. Ver [solución de problemas](troubleshooting_es.html) para correcciones, el [Guía de recuperación de Y1 y Y2](guides/recovery.html) por fallas de potencia y ruedas, y [SP Flash Tool](sp-flash-tool_es.html) para una recuperación avanzada.

## Guías de software por modelo.

Abra la guía para su modelo y el software que eligió.

### Innioasis Y1

Software para Y1:

### Innioasis Y2

Software para Y2:

## ¿Qué herramienta debo utilizar?

Esta guía utiliza Innioasis Actualizador 2.5.1, también llamado Actualizador CE. Mantiene seguros sus canciones, vídeos y emparejamientos de Bluetooth. Le indica cuándo están listas las actualizaciones. El Innioasis Universal Flash Tool borra tu reproductor y necesita pasos manuales. [Compara las herramientas →](updater-comparison_es.html)

## ¿Windows no inicia la aplicación? Solución alternativa al control inteligente de aplicaciones

Windows Defender SmartScreen o Smart App Control pueden bloquear aplicaciones comunitarias recién descargadas antes de que se propague la reputación de las firmas. Smart App Control está afectando actualmente a aplicaciones populares como Epic Overlay Service (utilizado por Fortnite): Updater CE es seguro y su uso está verificado. Desactivar Smart App Control permite que Updater CE se abra y se ejecute normalmente.
  - Abierto Configuración en su PC con Windows (presione Win + I).
  - Haga clic Privacidad y seguridad en la barra lateral izquierda, luego haga clic Windows Security.
  - Haga clic Control de aplicaciones y navegador.
  - Bajo Control inteligente de aplicaciones, haga clic Configuración de control de aplicaciones inteligentes.
  - Establezca el interruptor en Apagado para permitir que se inicie Updater CE.

¿Descargado a través de Edge? Si Edge bloquea la descarga, haga clic en el botón Más opciones (…) → Mantener → Mostrar más → Mantener de todos modos.

Volver a habilitar Smart App Control más tarde: Cuando desee volver a activar Smart App Control, puede volver a habilitarlo a través del Registro de Windows en `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` estableciendo `VerifiedAndReputablePolicyState` a `1` (Activado) o `2` (Modo de evaluación) y reiniciar.

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
