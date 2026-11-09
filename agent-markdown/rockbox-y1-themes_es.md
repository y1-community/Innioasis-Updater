---
title: "Rockbox-Y1 temas: transferir temas con Updater CE, 240p vs 360p y aplicar un tema"
description: "Cómo transferir temas al Innioasis Y1 con Updater CE (envío automático cuando esté disponible o transferencia guiada paso a paso después de un flash MTKClient en macOS y Linux), además de compatibilidad de 240p frente a 360p y aplicación de un tema."
language: "es"
source: "https://innioasis.app/rockbox-y1-themes_es.html"
---

# Rockbox-Y1 temas: transferir temas con Updater CE, 240p vs 360p y aplicar un tema

[← Rockbox-Y1 centro](rockbox-y1/)

Rockbox-Y1 · temas y actualizador CE

# Rockbox-Y1 temas: transferir con Updater CE, elegir la compilación y luego el aspecto

Updater CE maneja Rockbox-Y1 temas y fuentes por usted: transfiriéndolos a Y1 automáticamente siempre que puede y guiándolo a través de la transferencia paso a paso cuando no puede realizarse sin supervisión (por ejemplo, justo después de una instalación de firmware MTKClient en macOS o Linux).[Obtenga Rockbox y actualizador CE](guides/rockbox-y1.html)[Explorar temas de la comunidad](https://themes.innioasis.app/)[240p frente a 360p](rockbox-y1/resolution.html)

## Transferir temas al Y1 con Updater CE

Rockbox almacena su firmware en la memoria flash interna de Y1, mientras que los temas, fuentes y configuraciones de usuario se encuentran dentro de la memoria oculta. `.rockbox` carpeta en el almacenamiento del reproductor (tarjeta MicroSD). Debido a que actualizar un ROM y copiar archivos al almacenamiento utilizan dos conexiones diferentes, Actualizador CE se adapta automáticamente a su sistema operativo y método de instalación:
  - Transferencia automática cuando Updater CE puede llegar al reproductor: Cuando instala una compilación de 360p Rockbox-Y1 (o habilita la sincronización automática de temas en Configuración), Updater CE descarga y fusiona el tema de 360p seleccionado y el paquete de fuentes en segundo plano. Tan pronto como se pueda acceder a Y1 BAsD (Android Debug Bridge) o montado como un USB conducir con un `.rockbox` carpeta, Updater CE envía los temas y fuentes directamente al reproductor sin necesidad de extracción manual del zip.
  - Transferencia guiada paso a paso cuando no puede realizarse sin supervisión (por ejemplo, MTKClient en macOS y Linux): Cuando haces parpadear Rockbox usando un MTKClient método de instalación en macOS o Linux, el flash ocurre mientras el Y1 está apagado en el modo Precargador/BROM de bajo nivel, antes de que Rockbox se haya iniciado por primera vez para crear `.rockbox` y antes de que el almacenamiento del reproductor esté montado en su computadora. Siempre que Updater CE no pueda completar la transferencia sin supervisión durante el flash, abre automáticamente la asistente de fuentes y temas posteriores a la instalación y te guía para terminarlo: 
    - Arranque Rockbox primero: Updater CE le solicita que desconecte el cable USB si es necesario y encienda el Y1 para que Rockbox arranque una vez e inicialice el `.rockbox` carpeta en la tarjeta.
    - Vuelva a conectarse a través de USB: Vuelva a conectar el Y1 a su PC Mac o Linux. Si ADB está disponible, Updater CE detecta el reproductor iniciado y envía automáticamente los paquetes de temas y fuentes.
    - O utilice el modo de almacenamiento USB con el selector de carpetas guiado: Si ADB no está activo o prefiere la transferencia de almacenamiento directa, Updater CE lo guía para ingresar al modo de almacenamiento USB en Y1, haga clic en Seleccione la carpeta .rockbox, revela carpetas ocultas (Cmd+Shift+. en el cuadro de diálogo del archivo de macOS o Ctrl+H en Linux) y seleccione `.rockbox` en la unidad Y1; luego, Updater CE fusionará todos los temas y fuentes en su lugar.

  - Agregue o actualice temas en cualquier momento a pedido: Puede ejecutar la misma transferencia automatizada o guiada en cualquier momento sin necesidad de actualizar el firmware: abra Updater CE y elija Configuración → Instalar Rockbox Temas 360p (Cmd+T en MacOS, Ctrl+T en Windows y Linux), o arrastre el tema individual `.zip` paquetes en Updater CE Gota inteligente ventana.

## 240p, 360p y por qué la etiqueta está en la compilación

Y1 las compilaciones de la comunidad se publican con una etiqueta de resolución y las colecciones de temas llevan la misma etiqueta. Las versiones de 240p tienen la más amplia compatibilidad con paquetes de temas más antiguos; Se crean compilaciones de 360p para la ruta del tema Y1 más nueva. Instalar uno y aplicar el otro no es peligroso; simplemente se ve mal, con texto recortado, elementos faltantes o una interfaz que no puede leer.

Si aún no tiene preferencias de tema, elija la versión estable más nueva y su tema predeterminado, luego elija temas que coincidan con su etiqueta. El [página de resolución](rockbox-y1/resolution.html) va más profundo; La regla general es simple: la etiqueta de compilación y la etiqueta del tema deben coincidir.

## donde viven los temas

Los temas son archivos en la tarjeta MicroSD, dentro del `.rockbox` carpeta: la misma carpeta que contiene configuraciones y cachés. El firmware en sí está en la memoria flash interna, por lo que agregar, cambiar o eliminar un tema nunca requiere volver a actualizarlo.
  - Copie la propia carpeta del tema en `.rockbox/themes` en la tarjeta.
  - Luego selecciónelo en la configuración del tema del reproductor y reinicie para verlo aplicado.
  - Guarde una copia de un tema que le guste antes de actualizar la compilación; es un archivo, no una instalación.

Primero active los archivos ocultos si no puede ver la carpeta: macOS Cmd+Shift+., Vista de Windows → Elementos ocultos, Linux Ctrl+H.

## Aplicar un tema, en orden
  - Instale e inicie Rockbox-Y1 primero; un tema necesita una compilación en ejecución.
  - Copie la carpeta del tema a `.rockbox/themes` en la tarjeta.
  - Abra la configuración del tema y seleccione el tema.
  - Reinicie para que toda la interfaz, no solo el menú, la seleccione.
  - Si parece roto, seleccione otro tema; Los archivos todavía están allí si desea volver a intentarlo más tarde.

## Deshacer un tema que rompió la interfaz

Si el reproductor arranca con algo inutilizable, no es necesario reinstalar el firmware. Cambiar el nombre o eliminar el `.rockbox` carpeta en la tarjeta e inicie el reproductor: la compilación recrea la carpeta con la configuración predeterminada y un tema predeterminado. Tu música está intacta y puedes copiar los temas que quieras después.[La carpeta .rockbox](rockbox-y1/sd-card.html)[primer comienzo](rockbox-y1/first-start.html)[Actualizando la compilación](rockbox-y1/update.html)

## Preguntas que hace la gente¿Por qué Updater CE me guía en la transferencia de temas después de una instalación MTKClient en macOS o Linux?

MTKClient envía el Rockbox ROM al almacenamiento interno mientras su Y1 está apagado en modo Precargador/BROM de bajo nivel, antes de que Rockbox haya iniciado para inicializar el `.rockbox` carpeta y antes de que la tarjeta MicroSD esté montada en su computadora. Siempre que Updater CE puede llegar directamente al reproductor iniciado (a través de ADB o una unidad USB montada), transfiere los temas automáticamente; cuando no puede hacerlo sin supervisión durante la actualización, abre el paso de temas y fuentes guiados justo después de la actualización para ayudarlo a encender el Y1 y completar la transferencia a través de ADB o el modo de almacenamiento USB.¿Funcionará un tema Y2 en Y1?

No. Los ports están separados y el soporte de temas en Y2 sigue sus versiones beta. Ver [Rockbox-Y2 temas](rockbox-y2-themes_es.html).¿Los temas sobreviven a una actualización?

Generalmente sí, porque viven en la tarjeta y el flash escribe el ROM. Si una nueva compilación cambia la ruta del tema, vuelva a aplicar un tema que coincida con su etiqueta.¿Por qué el tema se aplica sólo a medias?

Un reinicio normalmente lo resuelve. De lo contrario, los archivos del tema están incompletos; vuelva a copiar su carpeta en lugar de editar archivos individuales.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
