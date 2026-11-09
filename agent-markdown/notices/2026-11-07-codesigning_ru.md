---
title: "Проблемы с запуском приложений Windows 10/11 и обходной путь Smart App Control - Innioasis Updater"
description: "Если Windows 10/11 или Smart App Control не позволяют вам запустить приложение, следуйте обходному пути здесь."
language: "ru"
source: "https://innioasis.app/notices/2026-11-07-codesigning_ru.html"
---

# Проблемы с запуском приложений Windows 10/11 и обходной путь Smart App Control - Innioasis Updater

С 25 октября 2026 г. · до 31 декабря 2026 г. · Модели: Y1, Y2

# Проблемы с запуском приложений Windows 10/11 и обходной путь Smart App Control

Если Windows 10/11 или Smart App Control не позволяют вам запустить приложение, следуйте обходному пути здесь.

С 25 октября 2026 г. · до 31 декабря 2026 г. · Модели: Y1, Y2

Ложноположительные отчеты были отправлены в Microsoft для `installer.exe` и `InnioasisUpdater.exe` и принято действие, но если Windows Endpoint Protection или Smart App Control по-прежнему блокируют приложение на вашем компьютере, воспользуйтесь этим обходным решением:

### Временное решение: отключите интеллектуальное управление приложениями
  - Открыть Windows Настройки (нажимать `Win + I`).
  - Перейти к Конфиденциальность и безопасность > Безопасность Windows > Управление приложениями и браузерами.
  - Под Интеллектуальное управление приложениями, нажмите Настройки смарт-контроля приложений.
  - Установите для Smart App Control значение Выключенный. Это немедленно позволит приложению открыться и запуститься.

Если Windows или Edge не позволяют вам загрузить Updater CE, выберите дополнительные параметры (…) затем Держать > Показать больше > Сохранить в любом случае.

### Повторное включение Smart App Control

Когда ложноположительные определения завершат обновление на вашем компьютере, вы можете повторно включить Smart App Control через реестр Windows:
  - Нажимать Клавиша Windows + Р, тип `regedit`и нажмите Enter, чтобы открыть редактор реестра от имени администратора.
  - Перейдите к: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (или `Policies`).
  - Найдите `VerifiedAndReputablePolicyState` на правой панели.
  - Дважды щелкните `VerifiedAndReputablePolicyState` и измените его данные Value на:

  - `1` = Вкл. (принудительно)
  - `2` = Режим оценки

  - Нажмите «ОК», закройте редактор реестра и перезагрузите компьютер.

[См. отчет installer.exe для Microsoft.](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[См. отчет InnioasisUpdater.exe для Microsoft.](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[Откройте связанную страницу](https://innioasis.app/notices.html)

[← Все уведомления](index_ru.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
