---
title: "Innioasis Y1 و Y2 USB درایور | مجوزهای درایور ویندوز و لینوکس - Innioasis به‌روزرسانی"
description: "رایانه خود را برای Innioasis Updater راه‌اندازی کنید: مجوزهای درایور Windows MediaTek و Linux USB - به‌علاوه رفع کابل و زمان‌بندی."
language: "fa"
source: "https://innioasis.app/drivers_fa.html"
---

# Innioasis Y1 و Y2 USB درایور | مجوزهای درایور ویندوز و لینوکس - Innioasis به‌روزرسانی

راه اندازی کامپیوتر

# قبل از پخش کننده کامپیوتر را آماده کنید.

اکثر مشکلات اتصال از درایور، مجوزها، کابل یا زمان‌بندی ناشی می‌شوند. ویندوز به درایور MediaTek نصب شده نیاز دارد. لینوکس به مجوزهای USB مناسب نیاز دارد. پلتفرم خود را در زیر پیدا کنید.[دریافت Updater CE](guide_fa.html#platform)[عیب‌یابی](troubleshooting_fa.html)

## Windows
  - نصب کننده درایور MediaTek را در زیر دانلود کنید.
  - نصب کننده را اجرا کنید و اجازه دهید ویندوز درایور را نصب کند.
  - کامپیوتر را مجددا راه اندازی کنید.
  - Updater CE را باز کنید و قبل از اینکه پخش کننده خاموش شده را وصل کنید منتظر پیام اتصال باشید.

برخی از سیستم های ویندوز از طریق Core Isolation (یکپارچگی حافظه) درایور را مسدود می کنند. اگر Updater CE هنوز بعد از راه اندازی مجدد نمی تواند پخش کننده را ببیند، یکپارچگی حافظه را در Windows Security خاموش کنید، راه اندازی مجدد کنید و درایور را دوباره نصب کنید. اگر سیستم شما اجازه می دهد، پس از پایان کار، تنظیم را دوباره فعال کنید.

ویندوز برنامه را راه اندازی نمی کند؟ اگر Windows Security یا Smart App Control مانع از باز شدن Updater CE شد، آن را باز کنید تنظیمات (فشار Win + I) → حریم خصوصی و امنیت → Windows Security → کنترل برنامه و مرورگر → تنظیمات کنترل برنامه هوشمند و آن را تنظیم کنید خاموش. Smart App Control در حال حاضر روی برنامه‌های محبوبی مانند Epic Overlay Service (که توسط Fortnite استفاده می‌شود) تأثیر می‌گذارد - Updater CE ایمن و تأیید شده برای استفاده است. برای فعال کردن مجدد بعداً، تنظیم کنید `VerifiedAndReputablePolicyState` به `1` (روشن) یا `2` (حالت ارزیابی) در زیر `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` در ویرایشگر رجیستری[درایور ویندوز را دانلود کنید](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[بازگشت به راهنمای اصلی](guide_fa.html#windows) · [دانلود نرم افزار](firmware_fa.html)

## مجوزهای لینوکس USB

لینوکس به حساب کاربری شما نیاز دارد که اجازه داشته باشد با تراشه MediaTek USB داخل پخش کننده صحبت کند. به‌روزرسانی‌کننده CE معمولاً این موضوع را در حین نصب مرتب می‌کند، و همان مجوز SP Flash Tool را پوشش می‌دهد، بنابراین این را به‌عنوان یک مرحله اصلاح به جای یک مرحله معمولی در نظر بگیرید.
  - Updater CE را به عنوان کاربر معمولی خود اجرا کنید نه به عنوان روت. نصب کننده فقط در صورت نیاز دسترسی مدیر را درخواست می کند.
  - چک کنید پخش کننده اصلا دیده می شود. پخش کننده را خاموش کنید، کابل را وصل کنید و دستور lsusb را در ترمینال اجرا کنید. پخش‌کننده متصل به‌عنوان یک دستگاه MediaTek با شناسه فروشنده 0e8d نشان داده می‌شود.
`lsusb`
  - اگر در lsusb ظاهر می‌شود اما Innioasis Updater CE یا SP Flash Tool می‌گوید مجوز رد شده است یا نمی‌تواند پورت را باز کند، کاربر شما دسترسی به دستگاه USB را ندارد. قانون udev یکسان هر دو ابزار را پوشش می دهد، بنابراین یکی را اضافه کنید که به گروه کاربران اجازه می دهد آن را بخوانند.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

آن خط را در فایل جدیدی با نام /etc/udev/rules.d/51-innioasis.rules ذخیره کنید، سپس اجرا کنید:`sudo udevadm control --reload && sudo udevadm trigger`
  - پخش‌کننده را کاملاً جدا کنید، دوباره آن را وصل کنید و دوباره نصب کنید.
  - اگر SP Flash Tool مجوز سریال یا مسابقه پورت را گزارش کرد، به طور کامل برق را جدا کنید و فقط زمانی که از شما خواسته شد دوباره وصل شوید.
افست فلاش را بداهه نسازید.اگر به ابزار بازیابی دستی منتقل می‌شوید، از فایل‌ها و پیکربندی مدل خاص که همراه پروژه ارسال می‌شوند استفاده کنید.

[بازگشت به راهنمای اصلی](guide_fa.html#linux) · [دانلود نرم افزار](firmware_fa.html) · [SP Flash Tool راهنمای](sp-flash-tool_fa.html)

## کابل و زمان بندی
  - از کابل داده شناخته شده USB استفاده کنید.
  - هنگام عیب یابی از هاب ها خودداری کنید.
  - مدل صحیح را کاملا خاموش کنید.
  - فقط در صورت درخواست وصل شوید.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
