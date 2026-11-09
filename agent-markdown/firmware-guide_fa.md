---
title: "راهنمای نصب و بازیابی سیستم عامل | Innioasis به‌روزرسانی CE - Innioasis بارگیری‌های میان‌افزار"
description: "با Innioasis Y1، Y2، G1، G3، G5، R1، PR1 و Timmkoo Q5، Q3 با Innioasis Updater CE، میان‌افزار سفارشی را نصب کنید یا میان‌افزار رسمی موجود در کارخانه را بازیابی کنید."
language: "fa"
source: "https://innioasis.app/firmware-guide_fa.html"
---

# راهنمای نصب و بازیابی سیستم عامل | Innioasis به‌روزرسانی CE - Innioasis بارگیری‌های میان‌افزار

راهنمای نصب سیستم عامل و بازیابی سهام

# سیستم عامل را روی دستگاه خود نصب یا بازیابی کنید

مدل چاپ شده روی پخش کننده خود را انتخاب کنید. سپس مراحل موجود در Updater CE را دنبال کنید. بقیه را اداره می کند.[دریافت Updater CE](guide_fa.html#platform)[بایگانی سیستم عامل را مرور کنید](firmware_fa.html)[عیب‌یابی](troubleshooting_fa.html)

مدل چاپ شده روی پخش کننده و نرم افزار مورد نظر خود را انتخاب کنید، سپس این راهنما را باز کنید. [نرم افزار و سیستم عامل موجودی را بر اساس مدل مرور کنید](firmware_fa.html).

## 

[دریافت Updater CE](guide_fa.html#download-updater)[آموزش کامل کتبی](guide_fa.html)

## Innioasis Updater CE دریافت کنید

اگر قبلاً Updater CE را دریافت نکرده اید، در اینجا باید از کجا شروع کنید.آن را در Updater CE دریافت کنیدبا نصب هدایت شده

### Windows

نصب کننده را دانلود کنید، آن را باز کنید و دستورات راه اندازی را دنبال کنید.[دانلود و نصب درایور](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[دانلود برنامه و درایورها](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[توسط Edge مسدود شده است؟](#)

اگر ویندوز شما را از اجرای برنامه باز می دارد یا آن را راه اندازی نمی کند، لطفاً تنظیمات را باز کنید، روی حریم خصوصی و امنیت → امنیت ویندوز → کنترل برنامه و مرورگر کلیک کنید و Smart App Control را خاموش کنید. [ویندوز برنامه را راه اندازی نمی کند؟ کمک کنید](#smart-app-control)

برای اینکه کار کند باید کامپیوتر خود را پس از نصب مجدد راه اندازی کنید.

### macOS

برنامه را دانلود کرده و به برنامه ها منتقل کنید. اگر macOS آن را مسدود کرد، System Settings، سپس Privacy & Security را باز کنید و روی Open Anyway کلیک کنید. [چگونه این کار می کند](https://support.apple.com/en-gb/102445#openanyway)[دانلود Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

AppImage را برای سیستم های Intel و AMD دانلود کنید، آن را قابل اجرا کنید و اجرا کنید.[دانلود AppImage برای Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[یادداشت های راه اندازی لینوکس](drivers_fa.html#linux)پلتفرم دیگه؟

به یادداشت های راه اندازی کامپیوتر طولانی تری نیاز دارید؟ را باز کنید [Windows](drivers_fa.html#windows) یا [Linux](drivers_fa.html#linux) راهنمای راه اندازی

## بازگشت به نرم افزار اصلی

برای بازگشت، مدل خود را انتخاب کنید، انتخاب کنید نرم‌افزار اصلی، سپس اجرا کنید نصب / بازگردانی. این همه است. Updater جایگزین نرم افزار سیستم برای شما می شود.[راهنمای بازیابی Y1](guides/restore-original-y1.html)[راهنمای بازیابی Y2](guides/restore-original-y2.html)

## راهنمای نرم افزار بر اساس مدل

مدل خود را انتخاب کنید، سپس راهنمای نرم افزار خود را باز کنید.

### Innioasis Y1

نرم افزار برای Y1:

### Innioasis Y2

نرم افزار برای Y2:

یادداشتی در مورد دو ابزار

## از کدام ابزار استفاده کنم؟

Innioasis به‌روزرسان CE امن ترین راه برای به روز رسانی پخش کننده شما است. این موسیقی، ویدیوها و جفت‌های بلوتوث شما را حفظ می‌کند. به شما می گوید چه زمانی به روز رسانی ها آماده هستند. روی ویندوز، macOS و لینوکس اجرا می شود. Innioasis Universal Flash Tool پخش کننده شما را پاک می کند و روی رایانه های کمتری کار می کند.[مقایسه کامل را باز کنید](updater-comparison_fa.html)

### ویندوز برنامه را راه اندازی نمی کند؟ نحوه خاموش کردن Smart App Control

Windows Defender SmartScreen یا Smart App Control می‌تواند برنامه‌های تازه دانلود شده انجمن را قبل از انتشار شهرت امضا مسدود کند. Smart App Control در حال حاضر روی برنامه‌های محبوبی مانند Epic Overlay Service (که توسط Fortnite استفاده می‌شود) تأثیر می‌گذارد - Updater CE ایمن و تأیید شده برای استفاده است. خاموش کردن Smart App Control به Updater CE اجازه می دهد تا به طور عادی باز و اجرا شود.
  - باز کنید تنظیمات در رایانه ویندوزی خود (فشار دهید Win + I).
  - کلیک کنید حریم خصوصی و امنیت در نوار کناری سمت چپ، سپس کلیک کنید Windows Security.
  - کلیک کنید کنترل برنامه و مرورگر.
  - زیر کنترل برنامه هوشمند، کلیک کنید تنظیمات کنترل برنامه هوشمند.
  - ضامن را روی خاموش اجازه می دهد تا به روز رسانی CE راه اندازی شود.

توسط Edge مسدود شده است؟ اگر Microsoft Edge خود دانلود را مسدود کرد، روی دکمه گزینه های بیشتر کلیک کنید (…) → نگه دارید → نمایش بیشتر → به هر حال نگه دار.

فعال کردن مجدد Smart App Control بعدا: هنگامی که می خواهید Smart App Control را دوباره فعال کنید، می توانید آن را از طریق رجیستری ویندوز در زیر فعال کنید `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` با تنظیم `VerifiedAndReputablePolicyState` به `1` (روشن) یا `2` (حالت ارزیابی) و راه اندازی مجدد.بستن راهنما

## این مفید بود؟

پاسخ شما به بهبود این راهنما کمک می کند.بله، من آن را مفید یافتمهنوز نه[به ما اطلاع دهید که چگونه می توانیم پیشرفت کنیم](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
