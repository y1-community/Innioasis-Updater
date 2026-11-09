---
title: "Cómo instalar Rockbox en tu Innioasis Y1 o Y2 - Innioasis Actualizador"
description: "Instale Rockbox en un Innioasis Y1 o Y2 con Updater: temas, versiones estables, notas Type A y Type B y cómo restaurar el software original después."
language: "es"
source: "https://innioasis.app/rockbox_es.html"
---

# Cómo instalar Rockbox en tu Innioasis Y1 o Y2 - Innioasis Actualizador

Rockbox referencia

# Obteniendo Rockbox en tu Y1 o Y2

Rockbox cambia el software del reproductor y abre una interfaz de reproductor de música más profunda, controles de reproducción, clasificación y opciones de temas. La instalación es guiada, pero Y1 y Y2 son ​​recorridos separados.[Rockbox en Y1](guides/rockbox-y1.html)[Rockbox en Y2](guides/rockbox-y2.html)[¿Por qué Rockbox?](rockbox-benefits_es.html)

## Qué cambia la instalación

Rockbox es un software personalizado. No elimina su capacidad de regresar a la interfaz original cuando el paquete de software original correspondiente esté disponible. Puede mejorar la navegación y personalización de música, pero las funciones, la resolución, la duración de la batería y la compatibilidad de temas dependen de la compilación.No mezcle modelos. Seleccione Y1 para un jugador Y1 y Y2 para un jugador Y2. Un nombre de versión similar no es prueba suficiente de que un paquete sea compatible.

## Mira el vídeo

Vídeo de Frawgeeys. Muestra la ruta del Actualizador Innioasis; utilice los pasos escritos específicos del modelo a continuación para su Y1 o Y2.

Vídeo de [cristian plaza](https://www.youtube.com/@CristianPlaza) (Español), mostrando Rockbox sobre un Y1. Utilice los pasos específicos del modelo a continuación para su reproductor.

## La ruta del actualizador compartido
  - Instale Updater y no conecte nada hasta que se lo solicite.
  - Elija el modelo impreso en el reproductor en Modelo del dispositivo.
  - elegir Rockbox en Software.
  - Elija una versión estable a menos que esté probando deliberadamente una versión nocturna.
  - Haga clic Instalar / Restaurar, luego siga las indicaciones de apagado y conexión USB.
  - Desconéctese solo después del mensaje de éxito.

## 240p, 360p y temas

Se pueden crear colecciones de temas Rockbox más antiguas a 240p. Y1 Las compilaciones de la comunidad también utilizan etiquetas de compatibilidad de 360p. Lea las notas de la versión y la fuente del tema antes de elegir una compilación. Es posible que un tema creado para una resolución o familia de software no funcione en otra.[Explorar temas de la comunidad](https://themes.innioasis.app/?lang=es)[Herramientas temáticas](https://themes.innioasis.app/?lang=es)

## Regresar al software original

Elija nuevamente el mismo modelo, seleccione Software original, elija una versión estable y utilice Instalar / Restaurar. Si la falla ocurrió antes del mensaje USB, verifique la computadora y los archivos extraídos. Si se detectó el reproductor pero el flash falló, comience con [solución de problemas](troubleshooting_es.html).[Y1 restaurar](guides/restore-original-y1.html)[Y2 restaurar](guides/restore-original-y2.html)

## Preguntas frecuentesReinstalé Rockbox y no solucionó nada.

Al reinstalar Rockbox se escribe la misma compilación en los mismos archivos, por lo que no puede restablecer las cosas que Rockbox mantiene en MicroSD. Si el problema es una configuración, tema, lista de reproducción o base de datos rotos que se encuentra en la tarjeta, la reinstalación no lo borrará. El reinicio confiable es eliminar el `.rockbox` La carpeta de MicroSD — Rockbox crea una nueva en el siguiente arranque.
  - Apague el reproductor por completo y retire la tarjeta MicroSD, o conecte el reproductor como una unidad USB.
  - Muestre los archivos ocultos en su computadora para que la carpeta sea visible. Cómo mostrar archivos ocultosMuestra archivos de puntos en tu computadoraWindows: en el Explorador de archivos abra el Vista tabular y marcar Objetos ocultos.macOS: en Finder presione Cmd+Shift+. para alternar archivos ocultos.Linux · Archivos GNOME: prensa Ctrl+H, o abra el menú y elija Mostrar archivos ocultos.Linux · KDE Delfín: prensa Ctrl+H, o usar Ver → Mostrar archivos ocultos.
  - Eliminar el `.rockbox` carpeta desde la raíz de la tarjeta.
  - Vuelva a insertar la tarjeta e inicie el reproductor. Rockbox recrea la carpeta con los valores predeterminados.
  - Vuelva a aplicar su tema y configuración. Si el problema sólo vuelve después de un tema específico, ese tema es la causa.

Eliminando `.rockbox` no desinstala Rockbox y no toca tu música: la carpeta contiene configuraciones, temas y cachés, y se reconstruye automáticamente. Si desea conservar sus temas, copie la carpeta fuera de `.rockbox` antes de eliminarla, o cambie el nombre de la carpeta a `.rockbox-old` primero.¿Por qué no puedo ver la carpeta .rockbox en mi MicroSD?

Las carpetas cuyo nombre comienza con un punto están ocultas de forma predeterminada en la mayoría de las computadoras. No es necesario verlo para instalar Rockbox: el actualizador maneja los archivos. Si está solucionando un problema y desea eliminarlo, primero active los archivos ocultos. Cómo mostrar archivos ocultosMuestra archivos de puntos en tu computadoraWindows: en el Explorador de archivos abra el Vista tabular y marcar Objetos ocultos.macOS: en Finder presione Cmd+Shift+. para alternar archivos ocultos.Linux · Archivos GNOME: prensa Ctrl+H, o abra el menú y elija Mostrar archivos ocultos.Linux · KDE Delfín: prensa Ctrl+H, o usar Ver → Mostrar archivos ocultos.¿Eliminar .rockbox restablecerá mi tema y mi configuración?

Sí - `.rockbox` contiene la configuración, el tema, las listas de reproducción y la base de datos en caché de Rockbox. Al eliminarlo, Rockbox vuelve a un estado limpio predeterminado. Haga una copia de seguridad de toda la carpeta (o cámbiele el nombre a `.rockbox-old`) si desea recuperar algo, inicie el reproductor y Rockbox crea una nueva carpeta.

## Más guías Rockbox-Y1 y Rockbox-Y2

Explore guías paso a paso para instalar, descargar, crear temas, restaurar y solucionar problemas Rockbox en ambos modelos:[Rockbox-concentrador Y1](rockbox-y1/)[Rockbox-concentrador Y2](rockbox-y2/)[Rockbox Descargas de ROM](rockbox-rom-download_es.html)[Rockbox para Y1](rockbox-for-y1_es.html)[Rockbox para Y2](rockbox-for-y2_es.html)[Rockbox-Y1 frente a Y2](rockbox-y1-vs-y2.html)[Rockbox-Temas Y1](rockbox-y1-themes.html)[Rockbox-Temas Y2](rockbox-y2-themes.html)

## ¿Fue útil esta referencia?

Su respuesta ayuda a mejorar esta guía.sitodavía no[Háganos saber cómo podemos mejorar](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
