---
title: "Innioasis Y1 La rueda de desplazamiento no funciona después de la actualización | Innioasis Archivo de firmware - Innioasis Descargas de firmware"
description: "¿Innioasis Y1 la rueda de desplazamiento o la rueda de clic no funcionan después de una actualización? Reinstale el software original Y1, verifique el anillo y separe el firmware de las fallas de hardware."
language: "es"
source: "https://innioasis.app/guides/y1-scroll-wheel-not-working_es.html"
---

# Innioasis Y1 La rueda de desplazamiento no funciona después de la actualización | Innioasis Archivo de firmware - Innioasis Descargas de firmware

Recuperación del jugador · Innioasis Y1

# Innioasis Y1 la rueda de desplazamiento no funciona después de una actualización

La rueda gira pero nada se mueve, o la rueda de clic dejó de responder justo después de un destello. A continuación se explica cómo separar un fallo de firmware de uno de hardware y qué hacer primero.[Obtener Updater CE](../guide_es.html#platform)[Y1 descargas de software](../firmware_es.html?model=Y1&software=original-y1)[Guía de recuperación](recovery_es.html)

## Averigüe si la culpa es del volante o del firmware

En Y1 la rueda es una entrada física, pero el firmware decide qué hace cada giro y clic. Si la rueda se detuvo en el momento en que actualizó o actualizó el reproductor, la causa probable es el software, no una pieza rota. Si ignora todos los programas que prueba (stock, Rockbox o una pantalla de recuperación), trátelo como hardware.
  - Funciona en un software, muerto en otro: fallo de firmware.
  - Muerto en todas las pantallas, incluida la recuperación: rueda, cinta o tabla.
  - Sólo falta una dirección: generalmente escombros debajo del anillo o desgaste.
  - La rueda gira pero no resalta nada: Es posible que el reproductor esté congelado; primero fuerce un reinicio.

## Comprobaciones rápidas antes de reinstalar el firmware
  - Mantenga presionado el botón de encendido durante unos 15 segundos para forzar el apagado del reproductor y luego inícielo normalmente.
  - Pruebe el volante en la pantalla de inicio, en Configuración y en el reproductor de música.
  - Pulsa los botones físicos. Si la potencia y el respaldo responden pero la rueda no, la falla es la rueda misma.
  - Cargue el reproductor durante 30 minutos con un cable de datos conocido; una batería baja puede hacer que las entradas se comporten de forma errática.
  - Si instaló Rockbox u otra compilación personalizada, regrese al software original y vuelva a realizar la prueba.

## Reinstale el firmware Y1 que coincida con su reproductor

Debido a que la rueda es impulsada por el firmware, una falla relacionada con la actualización se soluciona volviendo a colocar el software original Y1 correcto en el reproductor. No utilice un paquete Y2 y no elija una versión que sea "lo suficientemente parecida": los paquetes Y1 están creados para hardware Y1, y una compilación Y2 sobre un Y1 puede dejar los controles mal asignados.
  - Abierto [Actualizador CE](../guide_es.html#platform) en tu computadora.
  - conjunto Modelo del dispositivo a Y1.
  - elegir Software original en Software y elija una versión estable Y1: el paquete manual es `rom.zip`.
  - Haga clic Instalar / Restaurar y dejar que el paquete se extraiga.
  - Apague completamente el Y1, conecte el cable de datos USB solo cuando el Actualizador lo solicite y déjelo hasta que aparezca el mensaje de éxito.
Coincide con el modelo y la versión. Si la lista de versiones parece software Y2, deténgase y vuelva a seleccionar Y1. Los pasos completos están en el [Guía de restauración de Y1](restore-original-y1_es.html).

## Revise el anillo de la rueda en busca de residuos o daños.

Si la rueda está rígida, se pega o solo falla en una dirección, la pelusa y la arena pueden acumularse entre el anillo y la caja. Apague el reproductor y limpie alrededor del anillo con un paño de microfibra seco. No vierta limpiadores ni alcohol en el espacio y no levante el anillo.

Si el anillo está suelto, agrietado o ya no hace clic, el reproductor necesita servicio. Reinstalar el firmware no reparará una rueda dañada, una cinta desconectada o daños por líquidos.

## Si el jugador tampoco comienza

Una actualización fallida puede hacer que Y1 no pueda arrancar, lo que parece un problema con la rueda porque nada responde. Trabajar a través del [Y1 no enciende la guía](y1-wont-turn-on_es.html) para los pasos de carga, reinicio forzado y recuperación manual.

## Innioasis Y1 Preguntas frecuentes sobre la rueda de desplazamiento

### ¿Por qué mi rueda de desplazamiento Innioasis Y1 dejó de funcionar después de una actualización?

Una actualización puede hacer que el controlador del volante no esté sincronizado con el resto del firmware, especialmente si se interrumpió el flash o se utilizó un paquete Y2. Reinstale la versión del software original Y1 para su modelo y pruebe el volante en la pantalla de inicio original.

### ¿Cómo puedo saber si la rueda de clic Y1 está rota o si el firmware está defectuoso?

Pruebe la rueda en más de un software. Si funciona en el software original pero no en Rockbox, es un problema de asignación de firmware. Si no hace nada en ninguna pantalla, incluido un menú de recuperación, sospeche de la rueda, su cinta o el tablero.

### ¿La restauración del software original solucionará la rueda de desplazamiento Y1?

Soluciona fallos causados ​​por una actualización o un paquete no coincidente, y es lo primero que hay que probar. No reparará una rueda físicamente dañada, una cinta suelta o daños por líquidos.

### ¿Puedo usar un paquete de firmware Y2 para solucionar un problema de rueda Y1?

No. Los paquetes Y1 y Y2 no son intercambiables y mostrar el modelo incorrecto puede empeorar los controles. Haga coincidir el modelo y libere antes de ejecutar Instalar/Restaurar.

## Correcciones relacionadas
  - [La rueda de desplazamiento Y2 no funciona](y2-scroll-wheel-not-working_es.html) — los mismos controles para el Y2
  - [Y1 no enciende](y1-wont-turn-on_es.html) — recuperación de energía y arranque
  - [Innioasis guía de recuperación](recovery_es.html) — todas las guías de síntomas en un solo lugar
  - [Solución de problemas de una instalación](../troubleshooting_es.html) — cómo se ve un flash fallido
  - [Restaurar Y1 software original](restore-original-y1_es.html) — el tutorial de restauración completo

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
