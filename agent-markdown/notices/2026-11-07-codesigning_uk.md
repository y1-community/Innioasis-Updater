---
title: "Проблеми із запуском програми Windows 10/11 і обхідний шлях Smart App Control – Innioasis Updater"
description: "Якщо Windows 10/11 або Smart App Control не дозволяє вам запустити програму, виконайте обхідний шлях тут."
language: "uk"
source: "https://innioasis.app/notices/2026-11-07-codesigning_uk.html"
---

# Проблеми із запуском програми Windows 10/11 і обхідний шлях Smart App Control – Innioasis Updater

З 2026-10-25 · до 2026-12-31 · Моделі: Y1,Y2

# Проблеми із запуском програми Windows 10/11 і обхідний шлях Smart App Control

Якщо Windows 10/11 або Smart App Control не дозволяє вам запустити програму, виконайте обхідний шлях тут.

З 2026-10-25 · до 2026-12-31 · Моделі: Y1,Y2

Помилково-позитивні звіти були надіслані до Microsoft для `installer.exe` і `InnioasisUpdater.exe` і вжито заходів, але якщо Windows Endpoint Protection або Smart App Control все ще блокують програму на вашому комп’ютері, скористайтеся цим обхідним шляхом:

### Тимчасове вирішення проблеми: вимкніть Smart App Control
  - Відкрийте Windows Налаштування (прес `Win + I`).
  - Перейти до Конфіденційність і безпека > Безпека Windows > Керування додатком і браузером.
  - Під Smart App Control, натисніть Налаштування Smart App Control.
  - Установіть Smart App Control на Вимкнено. Це негайно дозволить програмі відкрити та запустити.

Якщо Windows або Edge не дозволяє завантажити Updater CE, натисніть додаткові параметри (…) тоді Тримайте > Показати більше > Все одно зберігайте.

### Повторне ввімкнення Smart App Control

Коли хибнопозитивні визначення завершать оновлення на вашому комп’ютері, ви зможете повторно ввімкнути Smart App Control через реєстр Windows:
  - Прес Клавіша Windows + R, вид `regedit`, і натисніть Enter, щоб відкрити редактор реєстру від імені адміністратора.
  - Перейдіть до: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` (або `Policies`).
  - Знайдіть `VerifiedAndReputablePolicyState` на правій панелі.
  - Двічі клацніть `VerifiedAndReputablePolicyState` і змініть його значення на:

  - `1` = Увімкнено (вимушено)
  - `2` = Режим оцінювання

  - Натисніть OK, закрийте редактор реєстру та перезавантажте комп’ютер.

[Перегляньте звіт installer.exe для Microsoft](https://www.microsoft.com/en-us/wdsi/submission/45d25b9c-0dd6-4d01-afd2-f0ea6b224dfd)[Перегляньте звіт InnioasisUpdater.exe для Microsoft](https://www.microsoft.com/en-us/wdsi/submission/1aef842b-3fda-44e7-bcfb-1a64af3ea661)

[Відкрийте сторінку за посиланням](https://innioasis.app/notices.html)

[← Усі повідомлення](index_uk.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
