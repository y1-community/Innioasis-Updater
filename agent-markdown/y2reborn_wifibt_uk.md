---
title: "Налаштування Wi-Fi, Bluetooth і FM-радіо для Reborn (Y2Linux) - Innioasis Updater"
description: "Короткий посібник після встановлення для Reborn (Y2Linux / Y2Reborn) на Innioasis Y2: скопіюйте system.img, потім налаштуйте Wi-Fi, Bluetooth і FM-радіо."
language: "uk"
source: "https://innioasis.app/y2reborn_wifibt_uk.html"
---

# Налаштування Wi-Fi, Bluetooth і FM-радіо для Reborn (Y2Linux) - Innioasis Updater

Innioasis Y2 · Reborn Після інсталяції

# Налаштуйте Wi-Fi, Bluetooth і FM-радіо.

Скопіюйте один файл на плеєр. Reborn обробляє решту.[Завантажити system.img (860 МБ)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Посібник із встановлення](guides/reborn-y2linux-y2.html)[Чому Y2Reborn?](reborn-y2linux-benefits_uk.html)

## Чому цей файл?

Wi-Fi, Bluetooth і FM-радіо потребують п’яти MediaTek модулів мікропрограми, які Reborn не можуть бути надіслані. Вони знаходяться всередині офіційного Y2 `system.img`. Reborn витягує їх один раз, перевіряє та видаляє файл.

## Налаштування
  - Завантажте system.img

Завантажте v3.2.0 FM `system.img` на ваш комп'ютер.[ Завантажте system.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Завантажте Reborn один раз

Увімкніть плеєр. Зачекайте Налаштування сховища щоб завершити, потім перезапустіть його один раз.
  - Підключіться до комп'ютера

Використовуйте кабель передачі даних USB. Гравець виглядає як Внутрішня пам'ять.На Mac?

встановити [OpenMTP](https://openmtp.ganeshrvel.com/) для перегляду програвача. Windows і Linux монтують його автоматично.
  - Скопіюйте system.img до мікропрограми

Створіть папку під назвою `Firmware` у корені внутрішньої пам’яті. Копія `system.img` в нього.
  - Дочекайтеся завершення налаштування

Reborn автоматично встановлює та видаляє прошивку радіо `system.img`. Це займає приблизно 10–20 секунд. Зачекайте Wi-Fi і Bluetooth готові.
  - Підключіть Wi-Fi, Bluetooth і FM-радіо
    - Wi-Fi: Налаштування → Система → Мережа → Wi-Fi. Виберіть свою мережу 2,4 ГГц.
    - Bluetooth: Переведіть навушники в режим сполучення. Налаштування → Bluetooth → виберіть їх.
    - FM радіо: Підключіть дротові навушники як антену, а потім відкрийте FM-радіо.

  - Оновлення через Wi-Fi

Майбутні Reborn оновлення встановлюються з Налаштувань → Система → Оновлення ПЗ. Прошивка вашого радіо залишається на місці.

## Чи був цей посібник корисним?

Чи знайшов цей посібник із налаштування після інсталяції корисним? Так, допомогло! [ Потрібна допомога щодо Discord ](https://discord.gg/zHrT2zrcek) Дякуємо за відгук! Насолоджуйтесь бездротовим прослуховуванням на Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
