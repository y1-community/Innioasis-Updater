---
title: "Посібник із встановлення та відновлення прошивки | Innioasis Оновлення CE - Innioasis Завантаження мікропрограми"
description: "Установіть спеціальну мікропрограму або відновіть офіційну заводську мікропрограму на Innioasis Y1, Y2, G1, G3, G5, R1, PR1 і Timmkoo Q5, Q3 за допомогою Innioasis Updater CE."
language: "uk"
source: "https://innioasis.app/firmware-guide_uk.html"
---

# Посібник із встановлення та відновлення прошивки | Innioasis Оновлення CE - Innioasis Завантаження мікропрограми

Посібник із встановлення та відновлення прошивки

# Встановіть або відновіть мікропрограму на своєму пристрої

Виберіть модель, надруковану на вашому плеєрі. Потім виконайте кроки в Updater CE. Це впорається з рештою.[Отримати Updater CE](guide_uk.html#platform)[Перегляньте архів прошивки](firmware_uk.html)[Усунення несправностей](troubleshooting_uk.html)

Виберіть модель, надруковану на вашому плеєрі, і потрібне програмне забезпечення, а потім відкрийте цей посібник. [Перегляньте програмне забезпечення та стандартні мікропрограми за моделлю](firmware_uk.html).

## 

[Отримати Updater CE](guide_uk.html#download-updater)[Повний письмовий підручник](guide_uk.html)

## Отримати Innioasis Updater CE

Ось з чого почати, якщо ви ще не отримали Updater CE.Отримайте його на Updater CEз керованим встановленням

### Windows

Завантажте інсталятор, відкрийте його та дотримуйтесь підказок налаштування.[Завантажити та встановити драйвер](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[Завантажте додаток і драйвери](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[Заблоковано Edge?](#)

Якщо Windows перешкоджає запуску програми або не запускає її, будь ласка, відкрийте «Параметри», клацніть «Конфіденційність і безпека» → «Безпека Windows» → «Керування програмою та браузером» і вимкніть Smart App Control. [Windows не запускає програму? Довідка](#smart-app-control)

Вам потрібно буде перезавантажити комп’ютер після інсталяції, щоб вона запрацювала.

### macOS

Завантажте програму та перемістіть її в розділ «Програми». Якщо macOS блокує його, відкрийте «Параметри системи», потім «Конфіденційність і безпека» та натисніть «Усе одно відкрити». [Як це працює](https://support.apple.com/en-gb/102445#openanyway)[Завантажити Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

Завантажте AppImage для систем Intel і AMD, зробіть його виконуваним і запустіть.[Завантажте AppImage для Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[Примітки щодо налаштування Linux](drivers_uk.html#linux)Ще одна платформа?

Потрібні довші примітки щодо налаштування комп’ютера? Відкрийте [Windows](drivers_uk.html#windows) або [Linux](drivers_uk.html#linux) посібник із налаштування.

## Повертаючись до оригінального програмного забезпечення

Щоб повернутися назад, виберіть свою модель, виберіть Заводське ПЗ, потім біжіть Встановити / Відновити. Ось і все. Оновлення замінює системне програмне забезпечення замість вас.[Посібник з відновлення Y1](guides/restore-original-y1.html)[Посібник з відновлення Y2](guides/restore-original-y2.html)

## Посібники програмного забезпечення за моделями

Виберіть свою модель і відкрийте посібник для свого програмного забезпечення.

### Innioasis Y1

Програмне забезпечення для Y1:

### Innioasis Y2

Програмне забезпечення для Y2:

Примітка щодо двох інструментів

## Який інструмент я повинен використовувати?

Innioasis Оновлення CE це найбезпечніший спосіб оновити плеєр. Він зберігає вашу музику, відео та сполучення Bluetooth. Він повідомляє вам, коли оновлення готові. Він працює на Windows, macOS і Linux. Innioasis Universal Flash Tool стирає ваш плеєр і працює на меншій кількості комп’ютерів.[Відкрийте повне порівняння](updater-comparison_uk.html)

### Windows не запускає програму? Як вимкнути Smart App Control

Windows Defender SmartScreen або Smart App Control можуть блокувати щойно завантажені програми спільноти до того, як пошириться репутація підпису. Smart App Control наразі впливає на такі популярні програми, як Epic Overlay Service (використовується Fortnite) — Updater CE безпечний і перевірений у використанні. Якщо вимкнути Smart App Control, програма Updater CE зможе відкриватися та працювати нормально.
  - відкритий Налаштування на ПК з Windows (натисніть Win + I).
  - Натисніть Конфіденційність і безпека на лівій бічній панелі, а потім натисніть Windows Security.
  - Натисніть Керування додатком і браузером.
  - Під Smart App Control, натисніть Налаштування Smart App Control.
  - Установіть перемикач у положення Вимкнено щоб дозволити запуск Updater CE.

Заблоковано Edge? Якщо Microsoft Edge блокує саме завантаження, натисніть кнопку Додаткові параметри (…) → Тримайте → Показати більше → Все одно зберігайте.

Повторне ввімкнення Smart App Control пізніше: Якщо ви хочете знову ввімкнути Smart App Control, ви можете знову ввімкнути його через реєстр Windows у розділі `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` шляхом встановлення `VerifiedAndReputablePolicyState` для `1` (Увімкнено) або `2` (Режим оцінки) і перезапуск.Закрити допомогу

## Це було корисно?

Ваша відповідь допоможе покращити цей посібник.Так, я знайшов це кориснимще ні[Дайте нам знати, як ми можемо покращити](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
