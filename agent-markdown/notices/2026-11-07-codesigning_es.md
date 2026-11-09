---
title: "Problemas de inicio de aplicaciones de Windows 10/11 y solución alternativa para el control inteligente de aplicaciones - Innioasis Actualizador"
description: "Si Windows 10/11 o Smart App Control le impide iniciar la aplicación, siga la solución aquí."
language: "es"
source: "https://innioasis.app/notices/2026-11-07-codesigning_es.html"
---

# Problemas de inicio de aplicaciones de Windows 10/11 y solución alternativa para el control inteligente de aplicaciones - Innioasis Actualizador

Desde 2026-10-25 · hasta 2026-12-31 · Modelos: Y1,Y2

# Problemas de inicio de aplicaciones de Windows 10/11 y solución alternativa de Smart App Control

Si Windows 10/11 o Smart App Control le impide iniciar la aplicación, siga la solución aquí.

Desde 2026-10-25 · hasta 2026-12-31 · Modelos: Y1,Y2

Se enviaron informes falsos positivos a Microsoft para `installer.exe` y `InnioasisUpdater.exe` y se tomó acción, pero si Windows Endpoint Protection o Smart App Control aún bloquean la aplicación en su computadora, use esta solución alternativa:

### Solución temporal: desactive el control inteligente de aplicaciones
  - Abrir ventanas Configuración (prensa `Win + I`).
  - Ir a Privacidad y seguridad > Seguridad de Windows > Control de aplicaciones y navegador.
  - Bajo Control inteligente de aplicaciones, haga clic Configuración de control de aplicaciones inteligentes.
  - Configure el Control de aplicaciones inteligentes en Apagado. Esto permite que la aplicación se abra y se ejecute inmediatamente.

Si Windows o Edge le impide descargar Updater CE, haga clic en más opciones (…) entonces Mantener > Mostrar más > Mantener de todos modos.

### Reactivación del control inteligente de aplicaciones

Cuando las definiciones de falsos positivos terminen de actualizarse en su computadora, puede volver a habilitar Smart App Control a través del Registro de Windows:
  - prensa Tecla Windows + R, tipo `regedit`y presione Entrar para abrir el Editor del Registro como administrador.
  - Navega a: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (o `Policies`).
  - Localizar `VerifiedAndReputablePolicyState` en el panel derecho.
  - Haga doble clic `VerifiedAndReputablePolicyState` y cambie sus datos de Valor a:

  - `1` = Activado (impuesto)
  - `2` = Modo de evaluación

  - Haga clic en Aceptar, cierre el Editor del Registro y reinicie su computadora.

[Ver el informe installer.exe a Microsoft](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[Consulte el informe InnioasisUpdater.exe para Microsoft](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[Abra la página vinculada](https://innioasis.app/notices.html)

[← Todos los avisos](index_es.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
