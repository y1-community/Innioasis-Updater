---
title: "Rockbox для Y2 (Rockbox-Y2): огляд, збірка та посібник із встановлення"
description: "Rockbox для Y2, Rockbox-Y2 і rockbox-y2 посилаються на порт прошивки спільноти Rockbox для Innioasis Y2. Дізнайтеся, що він містить і як його встановити за допомогою Innioasis Updater CE."
language: "uk"
source: "https://innioasis.app/rockbox-for-y2_uk.html"
---

# Rockbox для Y2 (Rockbox-Y2): огляд, збірка та посібник із встановлення

[← Завантаження прошивки](firmware_uk.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox для Y2 (Rockbox-Y2)

Rockbox-Y2 (також називається «Rockbox для Y2») — це спеціальний порт прошивки спільноти Rockbox для Innioasis Y2. Він використовує власний пакет ROM (`rom_y2.zip`) і встановлюється безпосередньо через Innioasis Updater CE.[Встановіть Rockbox-Y2](rockbox-y2/install.html)[Завантажити ROM](rockbox-y2/download.html)[Письмовий підручник](guides/rockbox-y2.html)[Rockbox-Y2 концентратор](rockbox-y2/)

## Створено спеціально для Innioasis Y2

У Innioasis Updater CE ця мікропрограма вказана як Rockbox коли Y2 вибрано. Його випуски публікує [spycemagic/y2-rockbox](firmware_uk.html?model=Y2&software=rockbox-y2) проект з назвою пакета `rom_y2.zip`.

Ніколи не встановлюйте пакет мікропрограми Y1 на Y2. Вибір Y2 у Updater CE автоматично фільтрує список випусків лише до Y2-сумісних збірок.

## Що пропонує Rockbox-Y2.
  - Музична бібліотека на основі тегів — переглядайте альбоми, виконавців і жанри за тегами аудіофайлів або безпосередньо переглядайте папки.
  - Елементи керування відтворенням — налаштування безперервного відтворення, кроссфейда, ReplayGain і еквалайзера.
  - Спеціальні теми — встановити теми, сумісні з вашою збіркою Rockbox-Y2 ([Y2 тематичний посібник](rockbox-y2-themes.html)).
  - 100% офлайн — відтворює локальні файли з вашої картки MicroSD без облікових записів чи підписок.
  - Легке заводське відновлення — повернутися до Y2 Original Software у будь-який час у Updater CE.

## Вибір випуску Rockbox-Y2.
  - Завжди вибирайте Y2 в Модель пристрою перший.
  - Виберіть останню версію, якщо ви не тестуєте конкретну версію.
  - Прочитайте [Примітки до випуску Rockbox-Y2](release-notes/rockbox-y2/index_uk.html) щоб побачити, що змінилося в кожній збірці.

## Пряме завантаження від розробників спільноти

Innioasis Updater CE завжди завантажує пакети мікропрограм безпосередньо від спільноти розробників мікропрограм ([spycemagic/y2-rockbox](firmware_uk.html?model=Y2&software=rockbox-y2)), і ці розробники несуть повну відповідальність за перелік випусків свого програмного забезпечення в Updater CE.

Ви можете дозволити Updater CE завантажувати та флешувати `rom_y2.zip` автоматично або завантажте пакет із нашого [Rockbox-Y2 сторінка завантажень](rockbox-y2/download.html) і [Rockbox ROM сторінка завантаження](rockbox-rom-download_uk.html).[Rockbox-Y2 завантажень](rockbox-y2/download.html)[Встановити з локального ZIP](rockbox-y2/portable-zip.html)

## Як встановити Rockbox-Y2
  - Відкрийте Innioasis Updater CE та встановіть Модель пристрою для Y2.
  - Виберіть Rockbox в Програмне забезпечення.
  - Виберіть Y2 випуск зі списку.
  - Натисніть Встановити / Відновити тому Updater CE завантажує пакет безпосередньо від розробника.
  - Повністю вимкніть Y2 і підключіть його за допомогою кабелю передачі даних USB, коли Updater CE запитає.
  - Зачекайте повідомлення про завершення, потім від’єднайте та ввімкніть Y2.

Щоб отримати повну покрокову інструкцію, прочитайте [Rockbox-Y2 підручник](guides/rockbox-y2.html).

## Відновлення оригінального програмного забезпечення Y2.

Щоб повернутися до заводської прошивки, виберіть Y2 і Заводське ПЗ в Updater CE виберіть стабільний випуск і натисніть Встановити / Відновити. Див [керівництво по відновленню](rockbox-y2/restore-stock.html) і [Y2 Сторінка оригінального програмного забезпечення](original-software-y2_uk.html).

## Часті запитанняЗвідки Updater CE завантажує Rockbox-Y2?

Updater CE завжди завантажує пакети мікропрограм безпосередньо з власних випусків мікропрограм спільноти розробників (`spycemagic/y2-rockbox`). Розробники несуть повну відповідальність за перелік випусків свого програмного забезпечення в Updater CE.Чому пакет називається rom_y2.zip?

Розробник називає архів прошивки Y2. `rom_y2.zip` тому його не можна сплутати з Y1. `rom.zip`.Чи працюють теми Y1 на Y2?

Не завжди. Перегляньте примітки до випуску для вашої збірки Y2 і перегляньте [Rockbox-Y2 тематичний посібник](rockbox-y2-themes.html).

## Пов'язані посібники

### [Rockbox-Y2 концентратор](rockbox-y2/)

Усі Y2 посібники: встановлення, завантаження, теми, відновлення, подвійне завантаження та усунення несправностей.

### [Rockbox-Y1 проти Rockbox-Y2](rockbox-y1-vs-y2.html)

Чим відрізняються збірки Y1 і Y2 Rockbox.

### [Теми Rockbox-Y2](rockbox-y2-themes.html)

Встановлення та скидання тем на Rockbox-Y2.

### [Rockbox для Y1](rockbox-for-y1_uk.html)

Огляд і посібник зі встановлення для порту Innioasis Y1.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
