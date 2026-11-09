---
title: "Controladores Innioasis Y1 y Y2 USB | Controlador de Windows y permisos de Linux - Innioasis Actualizador"
description: "Configure su computadora para Innioasis Updater: permisos del controlador de Windows MediaTek y de Linux USB, además de correcciones de cables y sincronización."
language: "es"
source: "https://innioasis.app/drivers_es.html"
---

# Controladores Innioasis Y1 y Y2 USB | Controlador de Windows y permisos de Linux - Innioasis Actualizador

Configuración de la computadora

# Prepare la computadora antes que el reproductor.

La mayoría de los problemas de conexión provienen del controlador, los permisos, el cable o la sincronización. Windows necesita tener instalado el controlador MediaTek. Linux necesita los permisos USB correctos. Encuentre su plataforma a continuación.[Obtener Updater CE](guide_es.html#platform)[Solución de problemas](troubleshooting_es.html)

## Windows
  - Descargue el instalador del controlador MediaTek a continuación.
  - Ejecute el instalador y permita que Windows instale el controlador.
  - Reinicie la computadora.
  - Abra Updater CE y espere el mensaje de conexión antes de enchufar el reproductor apagado.

Algunos sistemas Windows bloquean el controlador mediante el aislamiento del núcleo (integridad de la memoria). Si Updater CE aún no puede ver el reproductor después de reiniciar, desactive la integridad de la memoria en Seguridad de Windows, reinicie y reinstale el controlador. Vuelva a activar la configuración cuando haya terminado si su sistema lo permite.

¿Windows no inicia la aplicación? Si Windows Security o Smart App Control impiden que Updater CE se abra, abra Configuración (prensa Win + I) → Privacidad y seguridad → Windows Security → Control de aplicaciones y navegador → Configuración de control de aplicaciones inteligentes y configúrelo en Apagado. El Control inteligente de aplicaciones afecta actualmente a aplicaciones conocidas como Epic Overlay Service (utilizado por Fortnite) — Updater CE es seguro y verificado. Para volver a activarlo más tarde, establece `VerifiedAndReputablePolicyState` a `1` (Activado) o `2` (Modo de evaluación) en `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` en el Editor del Registro.[Descargar el controlador de Windows](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Volver a la guía principal](guide_es.html#windows) · [Descargas de software](firmware_es.html)

## Permisos de Linux USB

Linux necesita que su cuenta de usuario pueda comunicarse con el chip MediaTek USB dentro del reproductor. Updater CE generalmente soluciona esto durante la instalación, y el mismo permiso cubre SP Flash Tool, así que trátelo como un paso de reparación en lugar de una etapa normal.
  - Ejecute Updater CE como usuario normal, no como root. El instalador solicita acceso de administrador sólo cuando lo necesita.
  - Compruebe que el reproductor se vea en absoluto. Apague el reproductor, conecte el cable y ejecute el comando lsusb en una terminal. Un reproductor conectado aparece como un dispositivo MediaTek con el ID de proveedor 0e8d.
`lsusb`
  - Si aparece en lsusb pero Innioasis Updater CE o SP Flash Tool dice permiso denegado o no puede abrir el puerto, su usuario no tiene acceso al dispositivo USB. La misma regla udev cubre ambas herramientas, así que agregue una que permita al grupo de usuarios leerla.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Guarde esa línea en un nuevo archivo llamado /etc/udev/rules.d/51-innioasis.rules, luego ejecute:`sudo udevadm control --reload && sudo udevadm trigger`
  - Desenchufe completamente el reproductor, vuelva a enchufarlo e intente la instalación nuevamente.
  - Si SP Flash Tool informa un permiso de serie o una carrera de puerto, desconéctelo completamente y vuelva a conectarse solo cuando se le solicite.
No improvises compensaciones de flash.Si pasa a una herramienta de recuperación manual, utilice los archivos y la configuración específica del modelo que se incluyen con el proyecto.

[Volver a la guía principal](guide_es.html#linux) · [Descargas de software](firmware_es.html) · [SP Flash Tool guía](sp-flash-tool_es.html)

## Cable y sincronización
  - Utilice un cable de datos USB conocido.
  - Evite los concentradores mientras soluciona problemas.
  - Apague completamente el modelo correcto.
  - Conéctese solo cuando se le indique.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
