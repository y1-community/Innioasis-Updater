---
title: "Руководство по установке и восстановлению прошивки | Innioasis Updater CE - Innioasis Загрузка прошивки"
description: "Установите пользовательскую прошивку или восстановите официальную заводскую прошивку на Innioasis Y1, Y2, G1, G3, G5, R1, PR1 и Timmkoo Q5, Q3 с помощью Innioasis Updater CE."
language: "ru"
source: "https://innioasis.app/firmware-guide_ru.html"
---

# Руководство по установке и восстановлению прошивки | Innioasis Updater CE - Innioasis Загрузка прошивки

Руководство по установке прошивки и восстановлению стока

# Установите или восстановите прошивку на вашем устройстве

Выберите модель, напечатанную на вашем плеере. Затем следуйте инструкциям в Updater CE. Остальное он обрабатывает.[Скачать Updater CE](guide_ru.html#platform)[Просмотр архива прошивок](firmware_ru.html)[Устранение неполадок](troubleshooting_ru.html)

Выберите модель, указанную на вашем плеере, и необходимое программное обеспечение, а затем откройте это руководство. [Просмотр программного обеспечения и стоковой прошивки по модели](firmware_ru.html).

## 

[Скачать Updater CE](guide_ru.html#download-updater)[Полное письменное руководство](guide_ru.html)

## Получить Innioasis Обновление CE

Вот с чего начать, если у вас еще нет Updater CE.Получите его на Updater CEс управляемой установкой

### Windows

Загрузите установщик, откройте его и следуйте инструкциям по установке.[Загрузите и установите драйвер](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Загрузите приложение и драйверы](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Заблокировано Edge?](#)

Если Windows не позволяет вам запустить приложение или не запускает его, откройте «Настройки», нажмите «Конфиденциальность и безопасность» → «Безопасность Windows» → «Управление приложениями и браузером» и отключите Smart App Control. [Windows не запускает приложение? Помощь](#smart-app-control)

После установки вам потребуется перезагрузить компьютер, чтобы все заработало.

### macOS

Загрузите приложение и переместите его в Приложения. Если macOS блокирует его, откройте «Системные настройки», затем «Конфиденциальность и безопасность» и нажмите «Все равно открыть». [Как это работает](https://support.apple.com/en-gb/102445#openanyway)[Скачать программу обновления CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Загрузите AppImage для систем Intel и AMD, сделайте его исполняемым и запустите.[Загрузите AppImage для Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Замечания по настройке Linux](drivers_ru.html#linux)Другая платформа?

Нужны более подробные заметки по настройке компьютера? Откройте [Windows](drivers_ru.html#windows) или [Linux](drivers_ru.html#linux) руководство по настройке.

## Возврат к оригинальному программному обеспечению

Чтобы вернуться назад, выберите свою модель, выберите Заводское ПО, затем беги Установить / Восстановить. Вот и все. Программа обновлений заменит системное программное обеспечение за вас.[Y1 руководство по восстановлению](guides/restore-original-y1.html)[Y2 руководство по восстановлению](guides/restore-original-y2.html)

## Руководства по программному обеспечению по моделям

Выберите свою модель и откройте руководство для вашего программного обеспечения.

### Innioasis Y1

Программное обеспечение для Y1:

### Innioasis Y2

Программное обеспечение для Y2:

Примечание о двух инструментах

## Какой инструмент мне следует использовать?

Innioasis Средство обновления CE это самый безопасный способ обновить ваш плеер. Он сохраняет вашу музыку, видео и соединения Bluetooth. Он сообщает вам, когда обновления готовы. Он работает на Windows, macOS и Linux. Innioasis Universal Flash Tool стирает ваш плеер и работает на меньшем количестве компьютеров.[Открыть полное сравнение](updater-comparison_ru.html)

### Windows не запускает приложение? Как отключить Smart App Control

SmartScreen Защитника Windows или Smart App Control могут блокировать недавно загруженные приложения сообщества до распространения репутации подписи. Smart App Control в настоящее время влияет на популярные приложения, такие как Epic Overlay Service (используется Fortnite) — Updater CE безопасен и проверен для использования. Отключение Smart App Control позволяет Updater CE открываться и работать в обычном режиме.
  - Открыть Настройки на вашем ПК с Windows (нажмите Win + I).
  - Нажмите Конфиденциальность и безопасность на левой боковой панели, затем нажмите Windows Security.
  - Нажмите Управление приложениями и браузерами.
  - Под Интеллектуальное управление приложениями, нажмите Настройки смарт-контроля приложений.
  - Установите переключатель в положение Выключенный чтобы разрешить запуск Updater CE.

Заблокировано Edge? Если Microsoft Edge блокирует загрузку, нажмите кнопку «Дополнительные параметры» (…) → Держать → Показать больше → Сохранить в любом случае.

Повторное включение Smart App Control позже: Если вы хотите снова включить Smart App Control, вы можете снова включить его через реестр Windows в разделе `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` установив `VerifiedAndReputablePolicyState` в адрес `1` (Вкл.) или `2` (Режим оценки) и перезапуск.Закрыть справку

## Было ли это полезно?

Ваш ответ поможет улучшить это руководство.Да, я нашел это полезнымЕще нет[Дайте нам знать, как мы можем улучшить](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
