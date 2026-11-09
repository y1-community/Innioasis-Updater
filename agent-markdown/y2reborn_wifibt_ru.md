---
title: "Настройка Wi-Fi, Bluetooth и FM-радио для Reborn (Y2Linux) - Innioasis Updater"
description: "Краткое руководство после установки для Reborn (Y2Linux / Y2Reborn) на Innioasis Y2: скопируйте system.img, затем настройте Wi-Fi, Bluetooth и FM-радио."
language: "ru"
source: "https://innioasis.app/y2reborn_wifibt_ru.html"
---

# Настройка Wi-Fi, Bluetooth и FM-радио для Reborn (Y2Linux) - Innioasis Updater

Innioasis Y2 · Reborn После установки

# Настройте Wi-Fi, Bluetooth и FM-радио.

Скопируйте один файл в плеер. Reborn обрабатывает все остальное.[Скачать system.img (860 МБ)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Руководство по установке](guides/reborn-y2linux-y2.html)[Почему Y2Reborn?](reborn-y2linux-benefits_ru.html)

## Почему этот файл?

Для Wi-Fi, Bluetooth и FM-радио требуется пять MediaTek модулей прошивки, которые Reborn не могут быть поставлены. Они внутри официального Y2 `system.img`. Reborn извлекает их один раз, проверяет и удаляет файл.

## Настраивать
  - Скачать system.img

Загрузите v3.2.0 FM `system.img` к вашему компьютеру.[ Скачать system.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Загрузите Reborn один раз

Включите плеер. Подождите Настройка хранилища чтобы закончить, затем перезапустите его один раз.
  - Подключитесь к компьютеру

Используйте кабель для передачи данных USB. Игрок выглядит как Внутреннее хранилище.На Маке?

Установить [OpenMTP](https://openmtp.ganeshrvel.com/) для просмотра плеера. Windows и Linux монтируют его автоматически.
  - Копируем system.img в прошивку

Создайте папку с названием `Firmware` в корне внутреннего хранилища. Копировать `system.img` в это.
  - Дождитесь завершения настройки

Reborn автоматически устанавливает прошивку радио и удаляет `system.img`. Это занимает около 10–20 секунд. Подождите Wi-Fi и Bluetooth готовы..
  - Подключите Wi-Fi, Bluetooth и FM-радио.
    - Wi-Fi: Настройки → Система → Сеть → Wi-Fi. Выберите свою сеть 2,4 ГГц.
    - Bluetooth: Переведите наушники в режим сопряжения. Настройки → Bluetooth → выберите их.
    - FM-радио: Подключите проводные наушники в качестве антенны, затем откройте FM-радио.

  - Обновление через Wi-Fi

Будущие Reborn обновления устанавливаются из меню «Настройки» → «Система» → «Обновление программного обеспечения». Прошивка радио остается прежней.

## Было ли это руководство полезным?

Считаете ли вы это руководство по настройке после установки полезным? Да, это помогло! [ Нужна помощь по Discord ](https://discord.gg/zHrT2zrcek) Спасибо за ваш отзыв! Наслаждайтесь беспроводным прослушиванием на Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
