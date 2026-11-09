---
title: "Guía de recuperación de Innioasis Y1 y Y2 | Innioasis Archivo de firmware - Innioasis Descargas de firmware"
description: "Guía de recuperación para reproductores Innioasis Y1 y Y2 que no encienden o tienen una rueda de desplazamiento que dejó de funcionar después de una actualización. Pasos de reinicio y firmware."
language: "es"
source: "https://innioasis.app/guides/recovery_es.html"
---

# Guía de recuperación de Innioasis Y1 y Y2 | Innioasis Archivo de firmware - Innioasis Descargas de firmware

Recuperación del reproductor · Y1 y Y2

# Guía de recuperación de Innioasis Y1 y Y2

No enciende, la rueda no funciona o la instalación se detuvo a mitad de camino. Comience con el síntoma y luego siga los pasos en orden en lugar de saltar directamente a un flash manual.[Obtener Updater CE](../guide_es.html#platform)[Descargas de firmware](../firmware_es.html)[Solución de problemas](../troubleshooting_es.html)

Empezar con Innioasis Updater

## La instalación guiada soluciona la mayoría de estos

El actualizador lo hace de una sola vez. Elija el software, siga los pasos que aparecen en pantalla y listo. También le indica cuándo llega una solución o una nueva versión.

## Comience con el síntoma

Estas guías cubren los dos fallos que la gente encuentra con más frecuencia después de una actualización o un flash. Elija el que coincida con lo que ve y luego trabaje en orden.

### La rueda de desplazamiento no funciona

La rueda gira pero el jugador la ignora o se detiene justo después de una actualización.

[Y1 guía de rueda de desplazamiento](y1-scroll-wheel-not-working_es.html) · [Y2 guía de rueda de desplazamiento](y2-scroll-wheel-not-working_es.html)

### El reproductor no enciende

Una pantalla negra, luz sin carga o un logo que aparece y desaparece.

[Y1 guía de energía](y1-wont-turn-on_es.html) · [Y2 guía de energía](y2-wont-turn-on_es.html)

### Instalación detenida a medio camino

El actualizador falló antes o después del mensaje USB o la lista de versiones parece incorrecta.

[Guía de solución de problemas](../troubleshooting_es.html)

### Necesito los archivos

Software Original y paquetes personalizados para cada modelo.

[Descargas de firmware](../firmware_es.html)

## Los paquetes Y1 y Y2 no son intercambiablesNunca haga flash cruzado en un modelo. Un Y1 `rom.zip` no es un paquete Y2 y un Y2 `rom_y2.zip` no se ejecutará en un Y1. Mostrar el modelo incorrecto es una de las razones más comunes por las que un jugador termina con controles inactivos o un bucle de arranque.

Verifique el modelo impreso en el reproductor, luego compárelo en Updater CE antes de elegir una versión.

## Restaure primero el software original correspondiente

Antes de cualquier herramienta manual, vuelva a colocar el firmware original para el modelo correcto en el reproductor. Esto soluciona la mayoría de los fallos de arranque y ruedas relacionados con las actualizaciones.

Y1: seleccione Y1, elija Software original, elija una versión estable Y1 y luego ejecute Instalar/Restaurar. [Guía completa de restauración de Y1](restore-original-y1_es.html).

Y2: seleccione Y2, elija Software original, elija una versión estable Y2 y luego ejecute Instalar/Restaurar. [Guía completa de restauración de Y2](restore-original-y2_es.html).

Apague el reproductor y conecte el cable de datos USB solo cuando el Actualizador lo solicite. Déjelo conectado hasta que aparezca el mensaje de éxito.

## Recuperación manual que se envía con Updater CE

Cuando Updater no puede finalizar el trabajo, la misma instalación incluye las herramientas manuales. [SP Flash Tool](../sp-flash-tool_es.html) está incluido en máquinas Windows y Linux x86, y la ruta MTKClient cubre macOS. Ambos necesitan un paquete de firmware que coincida con el modelo, disponible en el [Descargas de firmware](../firmware_es.html) página.

Utilice la guía para su plataforma y mantenga el reproductor cargado. Si ninguna herramienta detecta el reproductor, es probable que la falla sea de hardware y no de firmware.

## Qué incluir cuando pides ayuda
  - El modelo, Y1 o Y2, impreso en el reproductor.
  - Qué hace la pantalla: nada, un logotipo, un bucle de inicio o la pantalla de inicio.
  - Si una computadora detecta el reproductor como un dispositivo MediaTek.
  - El mensaje exacto del actualizador y el paquete que seleccionó.
  - Lo que ya probaste, incluida cualquier herramienta manual.

No publique tokens privados ni archivos del sistema no relacionados. El [comunidad Discord](https://discord.gg/zHrT2zrcek) y [r/innioasis](https://reddit.com/r/innioasis) son los lugares más rápidos para comparar notas.

## Innioasis preguntas frecuentes sobre recuperación

### ¿Cómo soluciono un reproductor Innioasis que no enciende?

Cárguelo durante 30 minutos con un cable de datos conocido, fuerce un reinicio manteniendo la energía durante 15 segundos y luego verifique si una computadora lo detecta. Si es así, restaure el software original compatible con el modelo; de lo contrario, utilice las herramientas de recuperación manual incluidas con Updater CE.

### ¿Por qué no funciona mi rueda de desplazamiento Y1 o Y2?

Si el volante se detuvo después de una actualización, generalmente se debe a una discrepancia de firmware. Vuelva a instalar el software original del modelo correspondiente y vuelva a realizar la prueba. Si el volante está muerto en todos los firmware, trátelo como una falla de hardware.

### ¿Dónde descargo el firmware para la recuperación?

La página de Descargas de firmware en innioasis.app/firmware.html alberga paquetes originales y personalizados para cada modelo. Elija siempre el paquete Y1 o Y2 que coincida con el reproductor.

### ¿Qué herramientas de recuperación se incluyen con Updater CE?

Updater CE incluye SP Flash Tool en Windows y Linux, y la ruta MTKClient que incluye macOS, para la recuperación manual cuando la instalación normal no puede finalizar.

## Correcciones relacionadas
  - [La rueda de desplazamiento Y1 no funciona](y1-scroll-wheel-not-working_es.html) — la rueda de clic no responde después de una actualización
  - [La rueda de desplazamiento Y2 no funciona](y2-scroll-wheel-not-working_es.html) — los mismos controles para el Y2
  - [Y1 no enciende](y1-wont-turn-on_es.html) — carga, reinicio y recuperación manual
  - [Y2 no enciende](y2-wont-turn-on_es.html) — los mismos controles para el Y2
  - [SP Flash Tool guía](../sp-flash-tool_es.html) — flasheo manual en Windows y Linux

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
