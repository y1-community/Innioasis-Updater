---
title: "Desarrolladores | Agregue firmware personalizado a Innioasis Updater CE - Innioasis Descargas de firmware"
description: "Documentación del desarrollador para agregar un firmware personalizado Innioasis Y1 o Y2 al Updater CE: bifurcar el repositorio, publicar rom.zip activos, editar slidia_manifest.xml, probar y abrir una solicitud de extracción."
language: "es-419"
source: "https://innioasis.app/developers_es-419.html"
---

# Desarrolladores | Agregue firmware personalizado a Innioasis Updater CE - Innioasis Descargas de firmware

Para desarrolladores de firmware

# Agregue su firmware al Updater CE.

Updater CE es el catálogo comunitario y el instalador de firmware personalizado. Desarrolle su proyecto desde una base ROM, publíquelo como un repositorio público con los activos de lanzamiento correctos, agregue las entradas del modelo a `slidia_manifest.xml`, pruebe los filtros del modelo y abra una solicitud de extracción. Un repositorio puede servir a todos los modelos que admite.[Ver la fuente del Actualizador CE](https://github.com/y1-community/Innioasis-Updater)[Explorar descargas de software](firmware_es-419.html)

## Empezar desde una base ROM

Las ROM base brindan a los desarrolladores de firmware personalizados una base de Android limpia con los chips de radio inalámbricos habilitados. En el Y1 habilitan Wi-Fi y GPS junto con Bluetooth y FM de fábrica; en el Y2 habilitan Wi-Fi, GPS y FM junto con el Bluetooth de fábrica.Descargas base ROM para desarrollo de firmware personalizado, con la versión de Android y funciones inalámbricas que cada una habilita[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Descargar | Dispositivo | Androide | Funciones inalámbricas |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Agrega Wi-Fi y GPS al Bluetooth y FM de fábrica (FM ya funciona en el Y1 de fábrica). Para Y1 reproductores que se enviaron con OS 2.0.0 o posterior. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Agrega Wi-Fi y GPS al Bluetooth y FM de fábrica (FM ya funciona en el Y1 de fábrica). Para Y1 reproductores que se enviaron con un sistema operativo anterior a 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Agrega Wi-Fi, GPS y FM al Bluetooth de fábrica. El chip de radio Y2 está completamente habilitado, por lo que FM también está disponible aquí. |

Estas imágenes son la base estándar de Android (AOSP) con las radios inalámbricas del dispositivo habilitadas, por lo que un firmware personalizado puede agregar funciones de red en lugar de reemplazar la pila de radio. Son el punto de partida práctico para los siguientes pasos de publicación.

## Utilice estos nombres de activos de lanzamiento

El nombre del archivo es parte de la señal de compatibilidad. Mantenga los nombres exactos y coloque los archivos ZIP en los activos de lanzamiento del proyecto, no solo en el árbol de fuentes del repositorio.Nombres de activos ZIP de firmware y dispositivos compatibles``````

| Activo | Dispositivo | Ferretería | Significado |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 dispositivos que se enviaron con OS 2.0.0 o posterior. |
| rom_type_b.zip | Y1 | Type B | Y1 dispositivos que se enviaron con un sistema operativo anterior a 2.0.0. |
| rom_y2.zip | Y2 | Y2 | El paquete de instalación completa Y2. Manténgalo separado de los activos Y1. |
No cambie el nombre de un paquete para que se ajuste a otro modelo. Y1 y Y2 usan diferentes archivos de plataforma MediaTek y configuración de actualización. Publique el paquete para el hardware que realmente admite.

## Cómo funciona la conexión

Updater CE lee el manifiesto como su catálogo. Cada `<package>` La línea le dice el nombre del proyecto, el repositorio, el modelo y el controlador. Cuando un usuario elige ese proyecto, Updater verifica las versiones publicadas del repositorio y busca una `rom*.zip` activo.

### Manifiesto

Nombra el proyecto y lo asigna a un modelo. Y1 y Y2 necesitan líneas separadas, incluso cuando comparten un repositorio.

### Lanzamiento publicado

Contiene los recursos ZIP instalables. Una única versión puede contener los paquetes Y1 Type A, Y1 Type B y Y2 juntos.

### Instalación del actualizador CE

Utiliza el modelo seleccionado para elegir el paquete correspondiente y la ruta de flasheo específica del modelo. El usuario no debería tener que adivinar el nombre de un archivo.

## Publicar un proyecto en cinco pasos
  - Bifurque el repositorio de Updater CE. Crea tu propio tenedor de [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), luego clona tu bifurcación localmente.
  - Prepare un repositorio de firmware público. Asegúrese de que el repositorio sea público y que su versión contenga los recursos ZIP correctos. puedes poner `rom.zip`, `rom_type_b.zip`, y `rom_y2.zip` en la misma versión cuando pertenecen a la misma versión.
  - Edite el manifiesto. Abierto `slidia_manifest.xml` en la raíz de su bifurcación Updater CE. Agregue una línea para cada modelo que admita la versión (Y1 y Y2 son ​​el par común). El `repo` El valor es el del repositorio. `owner/repository`; `url` es la página pública del proyecto.
  - Prueba el catálogo. Ejecute Updater desde la caja editada. Seleccione Y1 y confirme que el proyecto muestra los activos Y1. Seleccione Y2 y confirme que muestra la versión Y2. Marque Type A y Type B por separado cuando ambos estén publicados.
  - Abra una solicitud de extracción. Envíe el cambio de manifiesto a su bifurcación y abra una solicitud de extracción en el repositorio ascendente de Updater CE. Incluya el enlace del proyecto, los modelos compatibles, la etiqueta de lanzamiento, los nombres de los activos y los dispositivos que probó.

## Genera tus líneas de manifiesto

Complete el repositorio y marque todos los modelos que admite la versión. El generador escribe uno. `<package>` línea por modelo y solo incluye los atributos que usted establece, por lo que el resultado coincide con el actual `slidia_manifest.xml` formato. Cada atributo que lee Updater CE está disponible a continuación; los opcionales están en Más opciones.URL del repositorioEl repositorio público GitHub. El generador extrae `owner/repository` desde la URL.Nombre del programaSe muestra en la aplicación y en el catálogo del sitio.URL del proyectoPágina orientada a humanos para el proyecto o sus notas de la versión.MarcaBorre esto para usar la marca predeterminada del modelo. SR1, Q3, Q5 y Q3e son modelos Timmkoo.Dispositivos (una línea cada uno)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eOtros modelosPara un modelo que no aparece en la lista anterior. Los modelos conocidos mantienen la ortografía de su catálogo.Banderas`do_not_keep_data` — nunca ofrezca Conservar datos para este firmwareCreado a partir del software original: agrega `derivative="y1-community/y1-stock-rom"`

Keep Data solo se ofrece cuando el firmware entrante y el firmware instalado son iguales o comparten un `derivative` raíz. Utilice la bandera sólo cuando los datos del usuario realmente no puedan transferirse.Más opciones: icono, material gráfico, recursos de lanzamiento, postinstalación y mirrors

#### Icono y obra de arteArchivo de iconoElija la imagen que enviará al repositorio. Esto lo previsualiza y crea su URL sin formato; no sube nada.Ruta del icono en el repositorioRuta a la imagen confirmada, relativa a la raíz del repositorio.Rama de iconoURL del iconoUna URL de imagen directa. Cuando está vacía, la aplicación utiliza la versión `updater.png` o un icono generado.Vista previa del icono seleccionado

URL del icono de modo oscuroÍcono de tema oscuro opcional. `image_dark` es un alias aceptado.URL de obra de arte ligeraArte secundario, probado después de la imagen de lanzamiento y `icon`.URL de ilustraciones oscuras

#### Liberar activosNombre del activo de liberaciónUn nombre para cada modelo seleccionado. Dejar vacío para usar `rom.zip` en Y1 y `rom_<model>.zip` en otra parte.Patrón de activosGlobo usado cuando los zips de la versión no tienen nombre `rom*.zip`.Type A activoGlobo para el paquete Y1 Type A cuando su nombre no lo dice.Type B activoGlobo para el paquete Y1 Type B cuando su nombre no lo dice.Versión mínima de la aplicaciónOculte la entrada de versiones anteriores de Updater CE.

#### Enlaces, mirrors y familia Keep DataPágina posterior a la instalaciónAbierto después de una instalación exitosa.Segunda página posterior a la instalaciónSegundo paso opcional para una guía de configuración de varias páginas.Espejos portátiles con cremalleraSeparados por comas `*-mirror` repositorios que crean paquetes Zip intermitentes portátiles.repositorio de derivadosEl firmware a partir del cual se creó esta versión. Los firmwares relacionados comparten una partición de datos, que es lo que comprueba Keep Data.repositorio de informaciónRepositorio de aplicaciones cuyas versiones describen las aplicaciones de este firmware. También necesita una página posterior a la instalación.APK repositorioRepositorio de aplicaciones cuyo APK la aplicación descarga e instala después del firmware.

#### Extras del catálogoBabosaIdentificador estable para enlaces y registros de instalación guardados. El modelo se agrega automáticamente cuando se seleccionan varios modelos.Descripción`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Copiar líneas

Cargando el último manifiesto...Obtenga una vista previa del último manifiesto con sus líneas agregadas

El generador trajo la corriente. `slidia_manifest.xml` desde este repositorio e insertó sus líneas generadas justo antes `</slidia>`.

Una línea no es suficiente para un repositorio compartido. Si falta la línea Y2, los usuarios Y2 no obtendrán una entrada que coincida con el modelo incluso cuando `rom_y2.zip` existe en la versión del proyecto. Lo mismo ocurre con todos los demás modelos compatibles con su versión.

### Cada atributo que lee el manifiesto

Estos son los atributos que comprenden las compilaciones actuales de Updater CE. El generador escribe sólo los que usted completa; la aplicación recurre a valores predeterminados sensatos para el resto.Atributos del paquete slidedia_manifest.xml y su significado``````````````````````````````````````````````````````````````````````````````````````````````

| Atributo | Necesario | que hace |
| --- | --- | --- |
| name | si | Nombre del software que se muestra en el catálogo y en las tarjetas de instalación. |
| repo | si | owner/repo. La aplicación lee las versiones GitHub de ese repositorio. |
| device | si | Modelo de destino, mayúsculas (Y1, Y2, G1, Q3e,…). Mantenga una entrada por modelo. |
| url | Recomendado | Página del proyecto o notas de la versión abiertas desde el catálogo. |
| type, handler | Si en la practica | type="img" y handler="Custom Firmware". Se omiten otros tipos y controladores que no son de firmware. |
| brand | Opcional | Marca del catálogo (Innioasis, Timmkoo). Vacío utiliza la marca predeterminada del modelo. |
| package_name | Opcional | Liberar nombre de archivo del activo. El valor predeterminado es rom.zip en Y1 y rom_<model>.zip en otros modelos. |
| asset_pattern | Opcional | Globo que no distingue entre mayúsculas y minúsculas para versiones cuyos zips de firmware no tienen nombre rom*.zip (Por ejemplo my-firmware-*.zip). |
| type_a_asset, type_b_asset | Opcional | Globos que identifican los zips Y1 Type A y Type B cuando sus nombres de archivo no contienen los marcadores habituales. |
| icon | Opcional | URL del logotipo. Usado después del propio lanzamiento. updater.png / updater.jpgy como alternativa para cada lanzamiento. |
| icon_dark | Opcional | Logotipo de tema oscuro. image_dark es un alias aceptado. |
| image | Opcional | Ilustración de luz secundaria, probada después icon. |
| post_install, post_install2 | Opcional | Páginas abiertas después de una instalación exitosa. El segundo cubre una guía de varios pasos. |
| portable_zips | Opcional | Separados por comas *-mirror repositorios que publican paquetes portátiles listos para ejecutar. |
| derivative | Opcional | Repositorio desde el que se construye el firmware. El firmware con la misma raíz derivada puede conservar los datos del usuario. |
| info_repo | Opcional | Repositorio de aplicaciones cuyas versiones describen lo que implementa el firmware. Requiere post_install o post_install2. |
| apk_repo | Opcional | Repositorio de aplicaciones cuyo APK instala la aplicación después del firmware. |
| min_version | Opcional | Oculte la entrada cuando Updater CE sea anterior a esta versión. |
| do_not_keep_data | Opcional | true (también 1 / yes) bloquea completamente la conservación de datos para este firmware. |
| slug | Opcional | Identificador estable para enlaces y registros de instalación guardados. Generado a partir del nombre y modelo cuando está vacío. |
| description | Opcional | Breve descripción del catálogo. Puede ser el valor del atributo o el texto del elemento. |

Los nombres heredados todavía se leen por compatibilidad: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` y `image_dark`. Las nuevas entradas deben utilizar los nombres actuales anteriores.

### Envíe las líneas como una solicitud de extracción
  - Copie las líneas generadas arriba. Ya coinciden con el último formato de manifiesto.
  - Editar `slidia_manifest.xml` en el repositorio. Utilice el enlace de edición a continuación; el host del repositorio crea una bifurcación y una rama automáticamente.
  - Pega las líneas justo antes `</slidia>`, manteniendo las entradas existentes sin cambios.
  - Comprométete con una nueva sucursal (Por ejemplo `add-your-firmware`), luego abra una solicitud de extracción en el repositorio de Updater CE.
  - En el PR, incluir el enlace del proyecto, los modelos compatibles, la etiqueta de lanzamiento, los nombres de los activos y los dispositivos que probó.
[Editar el manifiesto CE del actualizador](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Ver el último manifiesto](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Mantenga los nombres de los modelos en mayúsculas, use la URL exacta de su repositorio público y mantenga `type="img"` y `handler="Custom Firmware"` para una entrada de firmware.

## Haga que la publicación sea fácil de verificar

Dale al lanzamiento una etiqueta clara y una nota de lanzamiento. La etiqueta es útil para las personas, pero los nombres de los activos ZIP son los que utiliza Updater CE para identificar los paquetes de instalación.

### Lista de verificación de liberación
  - Publicar el comunicado públicamente.
  - Adjunte los archivos ZIP como activos de lanzamiento.
  - Indique el modelo admitido y Type A o Type B en las notas.
  - Enumere cualquier preparación requerida o límites conocidos.

### Una versión, tres activos

Una versión compartida puede contener `rom.zip`, `rom_type_b.zip`, y `rom_y2.zip`. Updater los clasifica por separado y elige entre los filtros de modelo y hardware.

### No hagas conjeturas

No incluya un paquete Y1 bajo el nombre de archivo Y2, ni agregue datos de dispersión, precargador o partición no probados solo para que aparezca un activo.

## Por qué son importantes las entradas del modelo durante el flasheo

El manifiesto no es sólo un menú de descarga. Después de la extracción, Updater CE utiliza el modelo resuelto para preparar la ruta de instalación correspondiente. Y1 y Y2 tienen diferentes archivos de plataforma, precargadores, configuración de dispersión y diseños de dispositivos.
  - Y1: el actualizador prepara la ruta Y1 y usa las particiones con nombre del dispositivo cuando se usa MTKClient.
  - Y2: el actualizador prepara la ruta Y2 y utiliza la configuración Y2 MT6582. La recuperación completa puede utilizar direcciones físicas de los datos dispersos correctos del modelo.
  - Soporte multiplataforma: Updater CE maneja la actualización nativa directamente en Windows, Linux y macOS (compatible con Intel y Apple Silicon Macs) sin herramientas de actualización adicionales.
Los contribuyentes deben proporcionar archivos de firmware correctos, no compensaciones de flash. No edite direcciones dispersas, precargadores, archivos DA ni comandos de partición para solucionar un paquete defectuoso. Corrija el recurso de lanzamiento y pruébelo en el modelo previsto.

## Antes de solicitar una fusión
  - Valide el XML con un analizador XML. Una cotización o cierre faltante `/>` Puede ocultar todas las entradas posteriores.
  - Inicie el actualizador desde su caja para que cargue el manifiesto local antes de la actualización remota.
  - Marque Y1 y Y2 de forma independiente. Confirme que el proyecto aparece solo donde su paquete es compatible.
  - Consulte la lista de lanzamientos para `rom.zip`, `rom_type_b.zip`, y `rom_y2.zip` según corresponda.
  - Pruebe la instalación real en el dispositivo deseado, con un cable de datos USB confiable y un plan de recuperación para regresar al software original.
  - En la solicitud de extracción, explique lo que probó. No describa un modelo no probado como compatible.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Para una verificación local, ejecute ese comando desde la raíz del repositorio. Verifica únicamente la sintaxis XML; no prueba que una versión contenga firmware válido o que sea seguro flashear un dispositivo.

## Enlaces útiles para proyectos[Actualizador de horquilla CE](https://github.com/y1-community/Innioasis-Updater/fork)[Ver el manifiesto](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Notas de contribución comunitaria](support_devs_es-419.html)[Solución de problemas](troubleshooting_es-419.html)

## Habilidades de modificación para agentes de IA

el repositorio `skills/` El directorio es una base de conocimientos basada en fuentes para agentes que trabajan en hardware, firmware, temas y aplicaciones Y1 y Y2. Cada habilidad nombra los archivos del proyecto de los que provienen sus reclamos, para que un agente pueda verificar un hecho antes de cambiar un dispositivo.Empieza aquí

### [Índice de habilidades y reglas de seguridad.](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Cómo cargar una habilidad, a qué modelo se aplica un hecho y las particiones que ningún paquete debería escribir.Ferretería

### [Y1 equipo](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, la rueda como eventos clave, pantalla de 480x360, rutas de audio/FM, almacenamiento y el mapa de partición Type A/B.Ferretería

### [Y2 equipo](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

Placa MT6582, árbol de dispositivos, paneles GC9503V/ST7701S, rieles PMIC/DAC, particiones e imagen de arranque.firmware

### [Paquetes de firmware](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip anatomía, archivos dispersos, contratos de actualización de Clase A y la lista de verificación de lanzamiento.Temas

### [Creación de temas y aspectos](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 temas config.json, Rockbox WPS/SBS, Reborn máscaras y Y2Player formato de máscara v2.todas las habilidades

### [Explorar la carpeta de habilidades](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, ROM estándar de Android, Y2Linux, aplicaciones de Android, lanzadores, notas de versión y publicación de sitios.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
