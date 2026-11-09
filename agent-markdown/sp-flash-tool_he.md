---
title: "SP Flash Tool עבור שחקנים Innioasis ו-Timmkoo"
description: "מצא את SP Flash Tool המצורף עם Innioasis Updater ב-Windows ו-Linux, חלץ את rom.zip או rom_y2.zip, והבזק Innioasis Y1 או Y2 עם קובץ הפיזור התואם."
language: "he"
source: "https://innioasis.app/sp-flash-tool_he.html"
---

# SP Flash Tool עבור שחקנים Innioasis ו-Timmkoo

מהבהב ידני

# כלי פלאש עבור שחקנים Innioasis ו-Timmkoo

SP Flash Tool נכנס ל-Innioasis Updater מופעל [Windows](drivers_he.html#windows) ו [Linux](drivers_he.html#linux). כבר יש לך את זה. מדריך זה מציג את הדרך הבטוחה להשתמש בו ב-Innioasis Y1 או Y2, ואת מסלול העדכון עבור שחקנים Timmkoo.[חזור למדריך העדכון](guide_he.html)[הורדות קושחה](firmware_he.html)[פתרון תקלות](troubleshooting_he.html)

התחל עם Innioasis Updater

## Updater עושה את כל העבודה במעבר אחד

Updater מבצע את רוב ההתקנות במעבר אחד. בחר את התוכנה, בצע את השלבים, וסיימת. זה גם אומר לך מתי נוחת תיקון או מהדורה חדשה. SP Flash Tool נמצא בתוך ערכת הכלים של Updater למקרים נדירים של Updater לא יכול לסיים. השלבים שלהלן הם היוצאים מן הכלל.

## למה מיועד הכלי הזה

Updater מהבהב את הנגן עבורך. SP Flash Tool הוא אותו מנוע, ללא מעקות ההגנה. השתמש בו כאשר Updater לא יופעל, כאשר הנגן לא יתחבר, או כאשר אתה יודע את דרכך בקובץ פיזור.נסה קודם את Updater. עבור רוב ההתקנות ורוב השחזורים, המדריך המודרך [מסלול עדכון](guide_he.html) היא הבחירה הבטוחה יותר. השתמש ב-SP Flash Tool כאשר אתה יודע למה אתה צריך את זה, ושמור סוללה טעונה בתוספת כבל נתונים USB מוכן.

## כלי פלאש עבור שחקנים Innioasis

Innioasis Updater הוא כלי הבזק עבור שחקנים Innioasis. הוא מתקין תוכנה רשמית, מעדכן ומשחזר חבילות באמצעות הזרימה התואמת לדגם, והוא שומר על המוזיקה וההגדרות שלך.

### Innioasis Y1 כלי פלאש

בחר את המהדורה Y1 ב-Updater, ולאחר מכן חבר את הנגן הכבוי כאשר האפליקציה מבקשת. אותן חבילות Y1 עובדות עם SP Flash Tool כאשר אתה צריך את המסלול הידני.

### Innioasis Y2 כלי פלאש

בחר מהדורה הרשומה עבור Y2. Y2 חבילות אינן ניתנות להחלפה עם Y1 חבילות, אז בדוק את הדגם לפני שתתחיל.

## כלי פלאש עבור שחקנים Timmkoo

שחקנים Timmkoo משתמשים באותה זרימת התקנת Updater. הוא קורא את חבילות ה-ZIP וה-RAR של Timmkoo ישירות, כך שאינך צריך כלי פלאש נפרד או קובץ פיזור.

### Timmkoo Q5 כלי פלאש

בחר את הדגם Q5 ב-Updater, בחר בחבילת Timmkoo, ולאחר מכן הפעל את ההתקנה / שחזור וחבר את הנגן בהנחיה.

### Timmkoo Q3 ו-Q3E כלי הבזק

הערך Q3 מכסה את Q3 ו-Q3E כאחד. Updater בוחר את הקבצים התואמים מהחבילה שהפרויקט מפרסם.

### Timmkoo A5 כלי פלאש

בחר את הדגם A5 לפני בחירת חבילה, ולאחר מכן עקוב אחר אותה הנחיה להתקנה.

## איפה Updater מציב את זה

SP Flash Tool נשלח עם תיקיית ההתקנה של Updater, לא כהורדה נפרדת. פתח אותו משם כשאתה צריך את זה.

### Windows

פתח את תיקיית ההתקנה של Updater והפעל `flash_tool.exe`. התיקיה נמצאת בדרך כלל מתחת `%LOCALAPPDATA%\Innioasis Updater`. תיקיית Toolkit עם קיצור SP Flash Tool כלולה בחלק מההגדרות.

### Linux

הפעל את החבילה `flash_tool` בינארי בתוך תיקיית אפליקציית Updater ב-x86 / x86_64. מתקין הפרויקט מכין הרשאות USB עם חוקי udev, כך שהנגן אמור להופיע כאשר הוא מחובר.

### macOS

SP Flash Tool אינו מאגד ב-macOS. Updater משתמש במסלול MTKClient לשם במקום זאת. השתמש ב- [התקנה מודרכת](guide_he.html) ב-Mac ושמור על SP Flash Tool עבור מחשב Windows או Linux.

הכלי נשלח עם סוכן ההורדה MediaTek ותצורה ספציפית לדגם, כך שאינך צריך לאסוף DA או לפזר קבצים ממקומות אחרים.

## הכן את הקושחה
  - תפוס את השחרור ממנו אתה רוצה [הורדות קושחה](firmware_he.html). בחר `rom.zip` עבור Y1 או `rom_y2.zip` עבור Y2.
  - חלץ את ה-ZIP לתיקיה משלו. Windows יכול להשתמש ב-Extract All. ב-Linux, השתמש במנהל הארכיון שלך או `unzip` בטרמינל.
  - בדוק שקובץ הפיזור נמצא בתיקייה שחולצה. בדרך כלל זה נקרא בשם `MT6572_Android_scatter.txt` עבור Y1 חבילות ו `MT6582_Android_scatter_def.txt` עבור Y2 חבילות, אם כי מהדורה עשויה לקרוא לה על שם הפרויקט שלה.
שמור את הדגמים נפרדים. הפיזור Y1 מתאר מכשיר MT6572 והפיזור Y2 מתאר התקן MT6582. מהבהב עם אחד הלא נכון הוא איך שחקנים מקבלים לבנים. אם הפיזור בתוך ה-ZIP אינו תואם לדגם שלך, עצור והשתמש במקום זאת בחבילה הרשומה עבור הדגם שלך.

## טען את הפיזור והבזק
  - פתח את SP Flash Tool מתיקיית ההתקנה של Updater.
  - בכרטיסייה הורדה, לחץ על בחר ליד פיזור טעינת קובץ ובחר את קובץ הפיזור מהתיקייה שחולצה. רשימת המחיצות תתמלא.
  - השאר את מצב הפלאש דולק הורדה בלבד אלא אם כן אתה עושה בכוונה החלמה מלאה, מה שצריך שדרוג קושחה.
  - לחץ הורדה. הכלי ימתין לשחקן.
  - כבה את הנגן לחלוטין, ולאחר מכן חבר את כבל הנתונים USB. הנח את הנגן ואל תזיז אותו.
  - המתן לסימון הביקורת הירוק. רק אז נתק את הכבל והפעל את הנגן.

שמור על אותם כללי כבל ותזמון USB כמו המסלול המודרך: כבל נתונים, ללא רכזת, והתחבר רק כשהכלי מוכן.

## אם זה לא מהבהב
  - בדוק שהפיזור וה-ZIP תואמים לדגם המודפס על הנגן.
  - ודא שהנגן כבוי לחלוטין לפני החיבור.
  - ב-Windows, אשר את מנהל ההתקן MediaTek המותקן עם הגדרת העדכון; ב-Linux, אשר את כללי udev מתקין הפרויקט.
  - חבר מחדש את הכבל רק כאשר הכלי ממתין. מרוץ נמל יכול להזדקק לניתוק מלא ורענן הורדה לחץ.

לכל דבר מעבר לזה, פתח [פתרון בעיות](troubleshooting_he.html). וזכור: Updater הוא עדיין המסלול הרגיל, ו [Y1](guides/restore-original-y1.html) ו [Y2](guides/restore-original-y2.html) מדריכי שחזור משתמשים בו גם כן.

## האם זה היה שימושי?

התשובה שלך עוזרת לשפר את המדריך הזה.כן, מצאתי את זה שימושיעדיין לא[ספר לנו איך אנחנו יכולים להשתפר](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
