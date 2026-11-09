---
title: "SP Flash Tool para Innioasis y Timmkoo jugadores"
description: "Busque SP Flash Tool incluido con Innioasis Updater en Windows y Linux, extraiga rom.zip o rom_y2.zip y actualice un Innioasis Y1 o Y2 con el archivo de dispersión correspondiente."
language: "es-419"
source: "https://innioasis.app/sp-flash-tool_es-419.html"
---

# SP Flash Tool para Innioasis y Timmkoo jugadores

Flasheo manual

# Herramienta Flash para reproductores Innioasis y Timmkoo

SP Flash Tool viene dentro de Innioasis Actualizador en [Windows](drivers_es-419.html#windows) y [linux](drivers_es-419.html#linux). Ya lo tienes. Esta guía muestra la forma segura de usarlo en un Innioasis Y1 o Y2, y la ruta de actualización para jugadores Timmkoo.[Volver a la guía del actualizador](guide_es-419.html)[Descargas de firmware](firmware_es-419.html)[Solución de problemas](troubleshooting_es-419.html)

Empezar con Innioasis Updater

## El actualizador hace todo el trabajo de una sola vez

El actualizador realiza la mayoría de las instalaciones de una sola vez. Elija el software, siga los pasos y listo. También le indica cuándo llega una solución o una nueva versión. SP Flash Tool está dentro del kit de herramientas del Actualizador para los raros casos en que el Actualizador no puede finalizar. Los pasos siguientes son la excepción.

## Para qué sirve esta herramienta

El actualizador muestra el reproductor por usted. SP Flash Tool es el mismo motor, sin las barandillas. Úselo cuando el Actualizador no se inicie, cuando el reproductor no se conecte o cuando conozca un archivo disperso.Pruebe primero el Actualizador. Para la mayoría de las instalaciones y la mayoría de las recuperaciones, la guía [Ruta del actualizador](guide_es-419.html) es la opción más segura. Utilice SP Flash Tool cuando sepa por qué lo necesita y tenga a mano una batería cargada y un cable de datos USB.

## Herramienta flash para Innioasis jugadores

Innioasis Updater es la herramienta flash para Innioasis jugadores. Instala software oficial, actualiza y restaura paquetes a través del flujo compatible con el modelo y conserva su música y configuración.

### Innioasis Y1 herramienta flash

Elija la versión Y1 en Updater, luego conecte el reproductor apagado cuando la aplicación lo solicite. Los mismos paquetes Y1 funcionan con SP Flash Tool cuando necesita la ruta manual.

### Innioasis Y2 herramienta flash

Elija una versión listada para Y2. Los paquetes Y2 no son intercambiables con los paquetes Y1, así que verifique el modelo antes de comenzar.

## Herramienta flash para Timmkoo jugadores

Los jugadores Timmkoo usan el mismo flujo de instalación del Actualizador. Lee los paquetes ZIP y RAR de Timmkoo directamente, por lo que no necesita una herramienta flash o un archivo disperso por separado.

### Timmkoo Q5 herramienta flash

Seleccione el modelo Q5 en Updater, elija el paquete Timmkoo, luego ejecute Instalar/Restaurar y conecte el reproductor cuando se le solicite.

### Herramienta flash Timmkoo Q3 y Q3E

La entrada Q3 cubre Q3 y Q3E por igual. El actualizador selecciona los archivos coincidentes del paquete que publica el proyecto.

### Timmkoo A5 herramienta flash

Seleccione el modelo A5 antes de elegir un paquete, luego siga el mismo mensaje de instalación.

## Donde lo pone Updater

SP Flash Tool se envía con la carpeta de instalación del Actualizador, no como una descarga separada. Ábrelo desde allí cuando lo necesites.

### Windows

Abra la carpeta de instalación del Actualizador y ejecute `flash_tool.exe`. La carpeta suele estar debajo `%LOCALAPPDATA%\Innioasis Updater`. En algunas configuraciones se incluye una carpeta Toolkit con un acceso directo SP Flash Tool.

### linux

Ejecute el paquete `flash_tool` binario dentro de la carpeta de la aplicación Updater en x86/x86_64. El instalador del proyecto prepara USB permisos con reglas udev, por lo que el reproductor debería aparecer cuando esté conectado.

### macos

SP Flash Tool no está incluido en macOS. El actualizador usa la ruta MTKClient allí en su lugar. Utilice el [instalación guiada](guide_es-419.html) en una Mac y mantenga SP Flash Tool para una máquina con Windows o Linux.

La herramienta se envía con el agente de descarga MediaTek y la configuración específica del modelo, por lo que no es necesario recopilar DA ni archivos dispersos de ningún otro lugar.

## Prepara el firmware
  - Toma el lanzamiento que deseas [Descargas de firmware](firmware_es-419.html). Elegir `rom.zip` para un Y1 o `rom_y2.zip` para un Y2.
  - Extraiga el ZIP en su propia carpeta. Windows puede utilizar Extraer todo. En Linux, utilice su administrador de archivos o `unzip` en una terminal.
  - Compruebe que el archivo de dispersión esté en la carpeta extraída. Generalmente se nombra `MT6572_Android_scatter.txt` para Y1 paquetes y `MT6582_Android_scatter_def.txt` para paquetes Y2, aunque una versión puede nombrarlo según su proyecto.
Mantenga los modelos separados. La dispersión Y1 describe un dispositivo MT6572 y la dispersión Y2 describe un dispositivo MT6582. Parpadear con el incorrecto es la forma en que los jugadores quedan bloqueados. Si la dispersión dentro del ZIP no coincide con su modelo, deténgase y utilice un paquete listado para su modelo.

## Cargue el scatter y flash
  - Abra SP Flash Tool desde la carpeta de instalación del Actualizador.
  - En la pestaña Descargar, haga clic en elegir junto a Archivo de carga de dispersión y seleccione el archivo de dispersión de la carpeta extraída. La lista de particiones se completará.
  - Deja el modo flash activado Descargar sólo a menos que esté haciendo deliberadamente una recuperación completa, lo cual necesita Actualización de firmware.
  - Haga clic Descargar. La herramienta esperará al jugador.
  - Apague el reproductor por completo y luego conecte el cable de datos USB. Deja el reproductor en el suelo y no lo muevas.
  - Espere a que aparezca la marca de verificación verde. Solo entonces desconecte el cable e inicie el reproductor.

Mantenga las mismas reglas USB de cable y sincronización que en la ruta guiada: un cable de datos, sin concentrador y conéctese solo cuando la herramienta esté lista.

## Si no parpadea
  - Comprueba que el scatter y el ZIP coincidan con el modelo impreso en el reproductor.
  - Confirme que el reproductor esté completamente apagado antes de conectarlo.
  - En Windows, confirme el controlador MediaTek instalado con la configuración del Actualizador; en Linux, confirme las reglas de udev desde el instalador del proyecto.
  - Vuelva a conectar el cable sólo cuando la herramienta esté esperando. Una regata portuaria puede necesitar una desconexión total y una nueva Descargar hacer clic.

Para cualquier cosa más allá de eso, abre [solución de problemas](troubleshooting_es-419.html). Y recuerde: el actualizador sigue siendo la ruta normal y [Y1](guides/restore-original-y1.html) y [Y2](guides/restore-original-y2.html) Las guías de restauración también lo utilizan.

## ¿Fue esto útil?

Su respuesta ayuda a mejorar esta guía.Sí, lo encontré útil.todavía no[Háganos saber cómo podemos mejorar](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
