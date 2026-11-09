---
title: "Innioasis Y1 No enciende | Innioasis Archivo de firmware - Innioasis Descargas de firmware"
description: "¿Innioasis Y1 no enciende ni carga? Fuerce un reinicio, verifique si una computadora lo ve y luego restaure el firmware Y1 o use la recuperación manual SP Flash Tool."
language: "es"
source: "https://innioasis.app/guides/y1-wont-turn-on_es.html"
---

# Innioasis Y1 No enciende | Innioasis Archivo de firmware - Innioasis Descargas de firmware

Recuperación del jugador · Innioasis Y1

# Innioasis Y1 no enciende

Una pantalla negra no siempre significa un jugador muerto. Trabaje mediante la carga, un reinicio forzado y la detección en una computadora antes de intentar un flash manual.[Obtener Updater CE](../guide_es.html#platform)[Descargas de firmware](../firmware_es.html)[Guía de recuperación](recovery_es.html)

## Cargue el Y1 correctamente antes que nada

La mayoría de los informes de "Y1 no enciende" son una batería descargada, un cable de solo carga o un cargador que no puede suministrar suficiente corriente. Un Y1 profundamente agotado puede tardar entre 20 y 30 minutos en encenderse antes de que la pantalla muestre algo, así que dale tiempo antes de decir que está muerto.
  - Utilice un USB conocido datos Cable, no un cable de sólo carga.
  - Pruebe con un cargador de pared, luego directamente con un puerto USB de computadora, no con un concentrador.
  - Déjelo conectado durante 30 a 60 minutos y observe si aparece un ícono de carga o una luz de fondo.
  - Pruebe con un segundo cable y cargador antes de continuar.

## Forzar un reinicio

Mantenga presionado el botón de encendido durante unos 15 segundos, suéltelo, espere cinco segundos y luego presione el botón de encendido una vez. Esto elimina un maletero colgado y es seguro repetirlo.

Si la pantalla muestra el logotipo y luego se vuelve negra, el reproductor se está iniciando y falla; pase a la restauración del firmware a continuación. Si no pasa nada, mantenlo cargado y vuelve a intentarlo después de media hora.

## Compruebe si una computadora puede ver el reproductor.

Conecte el Y1 apagado con un cable de datos y abra el Administrador de dispositivos en Windows, `lsusb` en Linux, o MTKClient en macOS. Un reproductor en funcionamiento aparece como un dispositivo MediaTek con ID de proveedor `0e8d`. Si aparece, el hardware está lo suficientemente vivo como para volver a flashear incluso cuando la pantalla permanece oscura.

Si no aparece nada, primero instale el controlador MediaTek en Windows: el [guía del conductor](../drivers_es.html) Cubre los permisos de Windows y Linux.

## Restaurar el firmware original Y1

Si se detecta el reproductor pero no arranca, reinstale el software original Y1. Utilice únicamente un paquete Y1; una compilación Y2 no se iniciará en el hardware Y1.
  - Abierto [Actualizador CE](../guide_es.html#platform) en tu computadora.
  - conjunto Modelo del dispositivo a Y1.
  - elegir Software original en Software y elija una versión estable Y1: el paquete manual es `rom.zip`.
  - Haga clic Instalar / Restaurar y dejar que el paquete se extraiga.
  - Apague completamente el Y1, conecte el cable de datos USB solo cuando el Actualizador lo solicite y déjelo hasta que aparezca el mensaje de éxito.
Mantenga la energía estable. Un flash que pierde potencia puede dejar al reproductor inutilizable. Cárgalo primero y conéctalo directamente a la computadora.

## Recuperación manual cuando el actualizador no puede ver el reproductor

Updater CE incluye herramientas de recuperación manual para los casos en que la instalación guiada no puede finalizar. [SP Flash Tool](../sp-flash-tool_es.html) está incluido en Windows y Linux x86, y la ruta MTKClient cubre macOS. Ambos necesitan un paquete de firmware compatible con el modelo del [Descargas de firmware](../firmware_es.html) página.

Siga la guía de herramientas de su plataforma en lugar de improvisar archivos dispersos o compensaciones. Si ninguna herramienta detecta el reproductor, es probable que la falla sea la batería, el puerto de carga o la placa.

## Si todavía no arranca

Deja de flashear y trátalo como hardware. No abra la carcasa ni presione la batería. Pregúntale a la comunidad sobre el modelo, qué hace la pantalla, si una computadora la detecta y qué paquetes probaste: el [Discord comunidad](https://discord.gg/zHrT2zrcek) puede ayudar a identificar una ruta de servicio.

Una restauración de stock reemplaza el sistema, así que haga una copia de seguridad de todo lo almacenado en la memoria interna del reproductor antes de actualizarlo. La restauración no modifica la música de una tarjeta MicroSD.

## Innioasis Y1 Preguntas frecuentes sobre energía

### ¿Por qué no se enciende mi Innioasis Y1?

Las causas habituales son una batería completamente agotada, un cable de sólo carga o un cargador débil, una falla del firmware que detiene el arranque o una falla de hardware. Cárguelo durante 30 minutos con un cable de datos conocido antes de asumir que el reproductor está muerto.

### ¿Cómo fuerzo el reinicio de un Innioasis Y1?

Mantenga presionado el botón de encendido durante unos 15 segundos, suéltelo, espere cinco segundos y luego presione el botón de encendido una vez. Si no aparece nada, déjalo cargando y vuelve a intentarlo después de 30 minutos.

### ¿Puedo recuperar un Y1 que no enciende?

Muchas veces sí. Si una computadora aún detecta el dispositivo MediaTek, reinstale el paquete de software original Y1 con Updater CE. Si no se detecta, utilice la recuperación SP Flash Tool o MTKClient incluida con Updater CE y un archivo de firmware Y1 que coincida con el modelo.

### ¿Es necesario cargar un Y1 antes de parpadear?

Sí. Un flash que pierde potencia puede dejar al reproductor inutilizable. Cárguelo primero y conéctelo directamente a la computadora en lugar de a través de un concentrador.

## Correcciones relacionadas
  - [Y2 no enciende](y2-wont-turn-on_es.html) — los mismos controles para el Y2
  - [La rueda de desplazamiento Y1 no funciona](y1-scroll-wheel-not-working_es.html) — si arranca pero la rueda no
  - [Innioasis guía de recuperación](recovery_es.html) — todas las guías de síntomas en un solo lugar
  - [SP Flash Tool guía](../sp-flash-tool_es.html) — flasheo manual en Windows y Linux
  - [Solución de problemas de una instalación](../troubleshooting_es.html) — cómo se ve un flash fallido

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
