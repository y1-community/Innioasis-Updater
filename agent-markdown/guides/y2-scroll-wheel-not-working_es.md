---
title: "Innioasis Y2 La rueda de desplazamiento no funciona después de la actualización | Innioasis Archivo de firmware - Innioasis Descargas de firmware"
description: "¿Innioasis Y2 la rueda de desplazamiento o la rueda de clic no funcionan después de una actualización? Reinstale el software original Y2, verifique el anillo y separe el firmware de las fallas de hardware."
language: "es"
source: "https://innioasis.app/guides/y2-scroll-wheel-not-working_es.html"
---

# Innioasis Y2 La rueda de desplazamiento no funciona después de la actualización | Innioasis Archivo de firmware - Innioasis Descargas de firmware

Recuperación del jugador · Innioasis Y2

# Innioasis Y2 la rueda de desplazamiento no funciona después de una actualización

La rueda gira pero el jugador la ignora, o la rueda de clic se detiene justo después de un destello. A continuación se explica cómo diferenciar un fallo de firmware de uno de hardware en Y2.[Obtener Updater CE](../guide_es.html#platform)[Y2 descargas de software](../firmware_es.html?model=Y2&software=original-y2)[Guía de recuperación](recovery_es.html)

## Averigüe si la culpa es del volante o del firmware

En Y2 la rueda es una entrada física, pero el firmware decide qué hace cada giro y clic. Una rueda que se detuvo tan pronto como actualizaste o parpadeaste apunta al software. Una rueda que ignora cada software (stock, Rockbox o una pantalla de recuperación) apunta a la pieza.
  - Funciona en un software, muerto en otro: fallo de firmware.
  - Muerto en todas las pantallas, incluida la recuperación: rueda, cinta o tabla.
  - Sólo falta una dirección: generalmente escombros debajo del anillo o desgaste.
  - La rueda gira pero no resalta nada: Es posible que el reproductor esté congelado; primero fuerce un reinicio.

## Comprobaciones rápidas antes de reinstalar el firmware
  - Mantenga presionado el botón de encendido durante unos 15 segundos para forzar el apagado del reproductor y luego inícielo normalmente.
  - Pruebe el volante en la pantalla de inicio, en Configuración y en el reproductor de música.
  - Pulsa los botones físicos. Si la potencia y el respaldo responden pero la rueda no, la falla es la rueda misma.
  - Cargue el reproductor durante 30 minutos con un cable de datos conocido.
  - Si instaló Rockbox para Y2 u otra compilación personalizada, regrese al software original y vuelva a realizar la prueba.

## Reinstale el firmware Y2 que coincida con su reproductor

La rueda es impulsada por el firmware, por lo que una falla relacionada con la actualización se soluciona volviendo a colocar el software original Y2 correcto en el reproductor. Nunca utilice un paquete Y1 en un Y2 y no elija una versión que sea "lo suficientemente parecida": los paquetes Y2 están diseñados para hardware Y2.
  - Abierto [Actualizador CE](../guide_es.html#platform) en tu computadora.
  - conjunto Modelo del dispositivo a Y2.
  - elegir Software original en Software y elija una versión estable Y2: el paquete manual es `rom_y2.zip`.
  - Haga clic Instalar / Restaurar y dejar que el paquete se extraiga.
  - Apague completamente el Y2, conecte el cable de datos USB solo cuando el Actualizador lo solicite y déjelo hasta que aparezca el mensaje de éxito.
Coincide con el modelo y la versión. Si la lista de versiones parece software Y1, deténgase y vuelva a seleccionar Y2. Los pasos completos están en el [guía de restauración Y2](restore-original-y2_es.html).

## Revise el anillo de la rueda en busca de residuos o daños.

Si la rueda está rígida, se pega o solo falla en una dirección, la pelusa y la arena pueden acumularse entre el anillo y la caja. Apague el reproductor y limpie alrededor del anillo con un paño de microfibra seco. No vierta limpiadores ni alcohol en el espacio y no levante el anillo.

Si el anillo está suelto, agrietado o ya no hace clic, el reproductor necesita servicio. El firmware no puede reparar una rueda dañada, una cinta desconectada o daños por líquidos.

## Si el jugador tampoco comienza

Una actualización fallida puede hacer que Y2 no pueda arrancar, lo que parece una falla en la rueda porque ninguna entrada responde. Trabajar a través del [Y2 no enciende la guía](y2-wont-turn-on_es.html) para carga, reinicio forzado y recuperación manual.

## Innioasis Y2 Preguntas frecuentes sobre la rueda de desplazamiento

### ¿Por qué mi rueda de desplazamiento Innioasis Y2 dejó de funcionar después de una actualización?

Una actualización puede hacer que el controlador del volante no esté sincronizado con el resto del firmware, especialmente si se interrumpió el flash o se utilizó un paquete Y1. Reinstale la versión del software original Y2 para su modelo y pruebe el volante en la pantalla de inicio original.

### ¿Cómo puedo saber si la rueda de clic Y2 está rota o si el firmware está defectuoso?

Pruebe la rueda en más de un software. Si funciona en el software original pero no en Rockbox, es un problema de asignación de firmware. Si no hace nada en ninguna pantalla, incluido un menú de recuperación, sospeche de la rueda, su cinta o el tablero.

### ¿La restauración del software original solucionará la rueda de desplazamiento Y2?

Soluciona fallos causados ​​por una actualización o un paquete no coincidente, y es lo primero que hay que probar. No reparará una rueda físicamente dañada, una cinta suelta o daños por líquidos.

### ¿Puedo usar un paquete de firmware Y1 para solucionar un problema de rueda Y2?

No. Los paquetes Y1 y Y2 no son intercambiables y mostrar el modelo incorrecto puede empeorar los controles. Haga coincidir el modelo y libere antes de ejecutar Instalar/Restaurar.

## Correcciones relacionadas
  - [La rueda de desplazamiento Y1 no funciona](y1-scroll-wheel-not-working_es.html) — las mismas comprobaciones para el Y1
  - [Y2 no enciende](y2-wont-turn-on_es.html) — recuperación de energía y arranque
  - [Innioasis guía de recuperación](recovery_es.html) — todas las guías de síntomas en un solo lugar
  - [Solución de problemas de una instalación](../troubleshooting_es.html) — cómo se ve un flash fallido
  - [Restaurar Y2 software original](restore-original-y2_es.html) — el tutorial de restauración completo

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
