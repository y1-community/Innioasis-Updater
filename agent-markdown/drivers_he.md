---
title: "נהגים Innioasis Y1 ו-Y2 USB | הרשאות מנהל התקן ו-Linux של Windows - Innioasis עדכון"
description: "הגדר את המחשב שלך עבור Innioasis Updater: Windows MediaTek מנהל התקן והרשאות Linux USB - בתוספת תיקוני כבלים ותזמון."
language: "he"
source: "https://innioasis.app/drivers_he.html"
---

# נהגים Innioasis Y1 ו-Y2 USB | הרשאות מנהל התקן ו-Linux של Windows - Innioasis עדכון

הגדרת מחשב

# הכינו את המחשב לפני הנגן.

רוב בעיות החיבור נובעות מהנהג, ההרשאות, הכבל או התזמון. Windows צריך להתקין את מנהל ההתקן MediaTek. לינוקס צריכה את ההרשאות הנכונות USB. מצא את הפלטפורמה שלך למטה.[הורדת Updater CE](guide_he.html#platform)[פתרון תקלות](troubleshooting_he.html)

## Windows
  - הורד את מתקין מנהל ההתקן MediaTek למטה.
  - הפעל את תוכנית ההתקנה ואפשר ל-Windows להתקין את מנהל ההתקן.
  - הפעל מחדש את המחשב.
  - פתח את Updater CE והמתן להנחיית החיבור לפני שתחבר את הנגן הכבוי.

חלק ממערכות Windows חוסמות את מנהל ההתקן באמצעות בידוד ליבה (שלמות זיכרון). אם Updater CE עדיין לא יכול לראות את הנגן לאחר הפעלה מחדש, כבה את שלמות הזיכרון באבטחת Windows, הפעל מחדש והתקן מחדש את מנהל ההתקן. הפעל שוב את ההגדרה כשתסיים אם המערכת שלך מאפשרת זאת.

Windows לא יפעיל את האפליקציה? אם Windows Security או Smart App Control עוצרים את פתיחת Updater CE, פתח הגדרות (לחץ Win + I) → פרטיות ואבטחה → Windows Security → שליטה באפליקציה ובדפדפן → הגדרות בקרת אפליקציה חכמה והגדר אותו ל כבוי. בקרת אפליקציות חכמה משפיעה כעת על יישומים פופולריים כמו שירות ה-Epic Overlay (בשימוש על ידי Fortnite) - Updater CE בטוח ומאומת לשימוש. כדי להפעיל מחדש מאוחר יותר, הגדר `VerifiedAndReputablePolicyState` ל `1` (מופעל) או `2` (מצב הערכה) תחת `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` בעורך הרישום.[הורד את מנהל ההתקן של Windows](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[חזרה למדריך הראשי](guide_he.html#windows) · [הורדות תוכנה](firmware_he.html)

## הרשאות לינוקס USB

לינוקס צריך שחשבון המשתמש שלך יורשה לדבר עם השבב MediaTek USB בתוך הנגן. Updater CE בדרך כלל מסדר את זה במהלך ההתקנה, ואותה הרשאה מכסה את SP Flash Tool, אז התייחס לזה כשלב תיקון ולא כשלב רגיל.
  - הפעל את Updater CE כמשתמש הרגיל שלך, לא כשורש. המתקין מבקש גישת מנהל רק כאשר הוא זקוק לה.
  - בדוק שהשחקן נראה בכלל. כבה את הנגן, חבר את הכבל והפעל את הפקודה lsusb במסוף. נגן מחובר מופיע כהתקן MediaTek עם מזהה הספק 0e8d.
`lsusb`
  - אם זה מופיע ב-lsusb אבל Innioasis Updater CE או SP Flash Tool אומרים שההרשאה נדחתה או לא יכול לפתוח את היציאה, למשתמש שלך חסרה גישה למכשיר USB. אותו כלל udev מכסה את שני הכלים, אז הוסף אחד שמאפשר לקבוצת המשתמשים לקרוא אותו.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

שמור את השורה בקובץ חדש בשם /etc/udev/rules.d/51-innioasis.rules, ולאחר מכן הרץ:`sudo udevadm control --reload && sudo udevadm trigger`
  - נתק את הנגן במלואו, חבר אותו בחזרה ונסה להתקין שוב.
  - אם SP Flash Tool מדווח על הרשאה טורית או מרוץ יציאה, נתק לחלוטין מהחשמל והתחבר מחדש רק כאשר תתבקש.
אין לאלתר קיזוז הבזק.אם אתה עובר לכלי שחזור ידני, השתמש בקבצים ובתצורה הספציפית לדגם שנשלחו עם הפרויקט.

[חזרה למדריך הראשי](guide_he.html#linux) · [הורדות תוכנה](firmware_he.html) · [SP Flash Tool מדריך](sp-flash-tool_he.html)

## כבל ותזמון
  - השתמש בכבל נתונים ידוע USB.
  - הימנע מרכזות בזמן פתרון בעיות.
  - כבה לחלוטין את הדגם הנכון.
  - התחבר רק בהנחיה.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
