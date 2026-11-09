---
title: "Rockbox для Y2 (Rockbox-Y2): обзор, сборка и руководство по установке"
description: "Rockbox для Y2, Rockbox-Y2 и rockbox-y2 относятся к порту прошивки сообщества Rockbox для Innioasis Y2. Узнайте, что он включает в себя и как его установить с помощью Innioasis Updater CE."
language: "ru"
source: "https://innioasis.app/rockbox-for-y2_ru.html"
---

# Rockbox для Y2 (Rockbox-Y2): обзор, сборка и руководство по установке

[← Загрузка прошивки](firmware_ru.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox для Y2 (Rockbox-Y2)

Rockbox-Y2 (также называемый «Rockbox для Y2») — это выделенный порт прошивки сообщества Rockbox для Innioasis Y2. Он использует собственный пакет ROM (`rom_y2.zip`) и устанавливается непосредственно через Innioasis Updater CE.[Установить Rockbox-Y2](rockbox-y2/install.html)[Загрузите ROM](rockbox-y2/download.html)[Письменное руководство](guides/rockbox-y2.html)[Rockbox-Y2 концентратор](rockbox-y2/)

## Создан специально для Innioasis Y2

В Innioasis Updater CE эта прошивка указана как Rockbox когда Y2 выбран. Его релизы публикуются [spycemagic/y2-rockbox](firmware_ru.html?model=Y2&software=rockbox-y2) проект с именем пакета `rom_y2.zip`.

Никогда не устанавливайте пакет прошивки Y1 на Y2. Выбор Y2 в Updater CE автоматически фильтрует список выпусков только до Y2-совместимых сборок.

## Что предлагает Rockbox-Y2
  - Музыкальная библиотека на основе тегов — просматривайте альбомы, исполнителей и жанры по тегам аудиофайлов или просматривайте папки напрямую.
  - Элементы управления воспроизведением — воспроизведение без пауз, кроссфейд, ReplayGain и настройки эквалайзера.
  - Пользовательские темы — установите темы, совместимые с вашей сборкой Rockbox-Y2 ([Y2 руководство по темам](rockbox-y2-themes.html)).
  - 100% офлайн — воспроизводит локальные файлы с вашей карты MicroSD без учетных записей и подписок.
  - Простое восстановление заводских настроек — вернуться к Y2 исходному программному обеспечению в любое время в Updater CE.

## Выбор релиза Rockbox-Y2
  - Всегда выбирать Y2 в Модель устройства первый.
  - Выбирайте последнюю версию, если вы не тестируете конкретную версию.
  - Прочтите [Rockbox-Y2 примечания к выпуску](release-notes/rockbox-y2/index_ru.html) чтобы увидеть, что изменилось в каждой сборке.

## Прямые загрузки от разработчиков сообщества.

Innioasis Программа обновлений CE всегда загружает пакеты прошивок непосредственно от разработчиков прошивок сообщества ([spycemagic/y2-rockbox](firmware_ru.html?model=Y2&software=rockbox-y2)), и эти разработчики несут единоличную ответственность за размещение выпусков своего программного обеспечения в Updater CE.

Вы можете позволить Updater CE загружать и прошивать `rom_y2.zip` автоматически или загрузите пакет с нашего [Rockbox-Y2 страница загрузок](rockbox-y2/download.html) и [Rockbox ROM страница загрузки](rockbox-rom-download_ru.html).[Rockbox-Y2 скачиваний](rockbox-y2/download.html)[Установить из локального ZIP-архива](rockbox-y2/portable-zip.html)

## Как установить Rockbox-Y2
  - Откройте Innioasis Updater CE и установите Модель устройства в адрес Y2.
  - Выбирать Rockbox в Программное обеспечение.
  - Выберите Y2 релиз из списка.
  - Нажмите Установить / Восстановить поэтому Updater CE загружает пакет непосредственно от разработчика.
  - Полностью выключите Y2 и подключите его с помощью кабеля для передачи данных USB по запросу Updater CE.
  - Дождитесь сообщения о завершении, затем отключите и включите Y2.

Полное пошаговое руководство читайте в [Rockbox-Y2 учебник](guides/rockbox-y2.html).

## Восстановление исходного программного обеспечения Y2

Чтобы вернуться к заводской прошивке, выберите Y2 и Заводское ПО в Updater CE выберите стабильную версию и нажмите Установить / Восстановить. См. [руководство по восстановлению](rockbox-y2/restore-stock.html) и [Y2 Страница оригинального программного обеспечения](original-software-y2_ru.html).

## Часто задаваемые вопросыОткуда Updater CE загружает Rockbox-Y2?

Программа обновлений CE всегда загружает пакеты встроенного ПО непосредственно из собственных выпусков разработчиков встроенного ПО сообщества (`spycemagic/y2-rockbox`). Разработчики несут единоличную ответственность за размещение выпусков своего программного обеспечения в Updater CE.Почему пакет называется rom_y2.zip?

Разработчик называет архив прошивки Y2 `rom_y2.zip` поэтому его нельзя спутать с Y1 `rom.zip`.Работают ли темы Y1 на Y2?

Не всегда. Ознакомьтесь с примечаниями к выпуску для вашей сборки Y2 и посмотрите [Rockbox-Y2 руководство по темам](rockbox-y2-themes.html).

## Связанные руководства

### [Rockbox-Y2 концентратор](rockbox-y2/)

Все руководства Y2: установка, загрузка, темы, восстановление, двойная загрузка и устранение неполадок.

### [Rockbox-Y1 против Rockbox-Y2](rockbox-y1-vs-y2.html)

Чем отличаются сборки Y1 и Y2 Rockbox.

### [Rockbox-Y2 темы](rockbox-y2-themes.html)

Установка и сброс тем на Rockbox-Y2.

### [Rockbox для Y1](rockbox-for-y1_ru.html)

Обзор и руководство по установке порта Innioasis Y1.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
