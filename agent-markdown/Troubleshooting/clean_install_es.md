---
title: "Reparar Innioasis Actualizador y Y1 Ayudante con una instalación limpia - Innioasis Actualizador"
description: "Instalación limpia paso a paso para Innioasis Updater y Y1 Helper: elimine los archivos sobrantes, reinstale y vuelva a actualizar el firmware."
language: "es"
source: "https://innioasis.app/Troubleshooting/clean_install_es.html"
---

# Reparar Innioasis Actualizador y Y1 Ayudante con una instalación limpia - Innioasis Actualizador

## Confirme que necesita una instalación limpia

Se recomienda la reinstalación manual cuando observe alguno de los siguientes síntomas:
  - El actualizador tarda unos minutos en iniciarse o se detiene mientras busca actualizaciones.
  - Las actualizaciones dejan de llegar aunque existan versiones más nuevas.
  - Las actualizaciones de firmware del dispositivo no se descargan ni se aplican aunque estén disponibles.
  - Te saltaste varias versiones y no has usado el Actualizador en mucho tiempo.

## Windows: realice una reinstalación limpia

Utilice el instalador oficial de Windows para actualizar el Actualizador en Windows 10 o Windows 11 (64 bits). Esto reemplaza completamente las versiones anteriores y restaura el canal de actualización automática.

Antes de ejecutar el instalador, abra Configuración › Aplicaciones › Aplicaciones instaladas (o el legado Agregar o quitar programas panel) y desinstale cualquier copia existente de Innioasis Updater. Comenzar limpio evita conflictos de archivos.[ Descargar el instalador limpio para Windows ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/installer.exe)Paso 1

### Descargue el instalador más reciente

Guarde el instalador en su carpeta de Descargas. Cierre Innioasis Actualizador si se está ejecutando actualmente.Paso 2

### Eliminar cualquier instalación existente

Abierto Configuración › Aplicaciones › Aplicaciones instaladas (o el legado Panel de control › Agregar o quitar programas) y desinstale Innioasis Updater para que la reinstalación comience desde cero.Paso 3

### Instalar y reiniciar

Ejecute el instalador que descargó; Windows le pedirá permiso. Cuando finalice la instalación, inicie Innioasis Updater; Ahora debería detectar 1.8.2.8 automáticamente y recibir actualizaciones nuevamente.

 Esto también corrige los inicios lentos y hace que el Actualizador vuelva a buscar versiones de firmware directamente de los desarrolladores. 

## macOS: actualice con el instalador DMG

El instalador de macOS borra los archivos antiguos e instala 1.8.2.8.[ Descargar Innioasis Actualizador DMG ](https://github.com/y1-community/supplemental-apks/releases/download/1.0/Innioasis.Updater.for.Mac.dmg)
  - Abra el DMG descargado y expanda la ventana del Finder para que pueda ver el Reinstalar opción.
  - Ejecute el comando Reinstalar para actualizar la copia existente de Updater. Esto elimina archivos auxiliares más antiguos que pueden bloquear nuevas funciones.
  - Inicie Innioasis Updater nuevamente desde Aplicaciones. Confirme la versión de las listas del panel Acerca de 1.8.2.8.
 Si ve "Innioasis No se puede abrir el actualizador" después de la reinstalación, vaya a Configuración del sistema › Privacidad y seguridad y elige Abierto de todos modos para aprobar la aplicación. 

## Después de actualizar a 1.8.2.8

Una vez que esté en la última versión, obtendrá acceso a las funciones siguientes. Estos solo están disponibles en las versiones actuales.
  - Instalaciones con un clic para firmware original, versiones comunitarias y compilaciones Rockbox descargadas directamente de las versiones de los desarrolladores.
  - Pasos guiados claros que le indican cuándo conectar el reproductor y cuándo es seguro desconectarlo.
  - Mejoras generales de estabilidad y tiempos de lanzamiento dramáticamente más rápidos en ambas plataformas.

 ¿Necesita ayuda para verificar su versión? Abra Innioasis Actualizador, elija Ayuda › Acerca dey confirme que la compilación se muestra 1.8.2.8. 

## ¿Aún necesitas ayuda?

Si la instalación limpia falla, capture cualquier mensaje de error y comuníquese con los canales de soporte de la comunidad Innioasis. Incluya la versión de su sistema operativo, la compilación del actualizador (si está disponible) y los pasos que ya ha probado.

Mantener su instalación actualizada garantiza que siempre reciba los paquetes de firmware y las herramientas más recientes a medida que se implementan.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
