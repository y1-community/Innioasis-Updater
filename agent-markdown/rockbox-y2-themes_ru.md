---
title: "Rockbox-Y2 темы: установка и сброс тем на Y2"
description: "Как устанавливать, управлять и сбрасывать Rockbox-Y2 темы на Innioasis Y2: где темы находятся в папке .rockbox и как проверить совместимость сборок."
language: "ru"
source: "https://innioasis.app/rockbox-y2-themes_ru.html"
---

# Rockbox-Y2 темы: установка и сброс тем на Y2

[← Rockbox-Y2 концентратор](rockbox-y2/)

Rockbox-Y2 · темы

# Rockbox-Y2 темы

Как установить темы на Rockbox-Y2, проверить совместимость темы с установленной сборкой и сбросить тему, если она отображается неправильно.[Rockbox-Y2 примечания к выпуску](release-notes/rockbox-y2/index.html)[Просмотр тем сообщества](https://themes.innioasis.app/)[Установить Rockbox-Y2](rockbox-y2/install.html)

## Проверьте совместимость темы для вашей сборки

Rockbox-Y2 разрабатывается отдельно от порта Y1, поэтому совместимость тем соответствует версии сборки Y2, которую вы установили. Проверьте [Rockbox-Y2 примечания к выпуску](release-notes/rockbox-y2/index.html) для вашей версии перед установкой пакета тем.

Видеть [Rockbox-Y1 против Rockbox-Y2](rockbox-y1-vs-y2_ru.html) для полного сравнения двух портов.

## Как установить темы на Y2

Темы хранятся на вашей карте MicroSD внутри скрытого `.rockbox` папка.
  - Запустите Rockbox-Y2 хотя бы один раз, чтобы создать `.rockbox` папку на вашей карте MicroSD.
  - Извлеките или скопируйте файлы темы в `.rockbox/` (так `themes`, `wps`, `fonts`, и `backdrops` сливаться в `.rockbox/`).
  - На плеере откройте Настройки → Настройки темы → Просмотр файлов тем. и выберите свою тему.

Чтобы просмотреть скрытые папки на вашем компьютере: нажмите Cmd+Shift+. в macOS включите Вид → Скрытые элементы в Windows или нажмите Ctrl+H на Линуксе.

## Как сбросить сломанную тему

Если из-за темы экран становится трудночитаемым, переименуйте или удалите `.rockbox` папку на карте MicroSD и перезапустите плеер. Rockbox-Y2 создаст новый `.rockbox` папку с темой по умолчанию, сохраняя при этом вашу музыку.[Папка .rockbox](rockbox-y2/sd-card.html)[Обновление Rockbox-Y2](rockbox-y2/update.html)[Rockbox-Y2 примечания к сборке](rockbox-y2/resolution.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
