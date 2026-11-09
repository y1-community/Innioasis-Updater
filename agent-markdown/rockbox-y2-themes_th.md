---
title: "ธีม Rockbox-Y2: การติดตั้งและการรีเซ็ตธีมบน Y2"
description: "วิธีติดตั้ง จัดการ และรีเซ็ตธีม Rockbox-Y2 บน Innioasis Y2: ตำแหน่งที่ธีมอยู่ในโฟลเดอร์ .rockbox และวิธีการตรวจสอบความเข้ากันได้ของบิลด์"
language: "th"
source: "https://innioasis.app/rockbox-y2-themes_th.html"
---

# ธีม Rockbox-Y2: การติดตั้งและการรีเซ็ตธีมบน Y2

[← Rockbox-Y2 ฮับ](rockbox-y2/)

Rockbox-Y2 · ธีม

# Rockbox-Y2 ธีม

วิธีติดตั้งธีมบน Rockbox-Y2 ตรวจสอบความเข้ากันได้ของธีมกับบิลด์ที่ติดตั้งของคุณ และรีเซ็ตธีมหากแสดงไม่ถูกต้อง[Rockbox-Y2 บันทึกประจำรุ่น](release-notes/rockbox-y2/index.html)[เรียกดูธีมชุมชน](https://themes.innioasis.app/)[ติดตั้ง Rockbox-Y2](rockbox-y2/install.html)

## ตรวจสอบความเข้ากันได้ของธีมสำหรับงานสร้างของคุณ

Rockbox-Y2 ได้รับการพัฒนาแยกจากพอร์ต Y1 ดังนั้นความเข้ากันได้ของธีมจึงเป็นไปตามเวอร์ชันบิลด์ Y2 ที่คุณติดตั้งไว้ ตรวจสอบ [Rockbox-Y2 บันทึกประจำรุ่น](release-notes/rockbox-y2/index.html) สำหรับเวอร์ชันของคุณก่อนที่จะติดตั้งชุดรูปแบบ

ดู [Rockbox-Y1 กับ Rockbox-Y2](rockbox-y1-vs-y2_th.html) เพื่อการเปรียบเทียบแบบเต็มของทั้งสองพอร์ต

## วิธีติดตั้งธีมบน Y2

ธีมจะถูกจัดเก็บไว้ในการ์ด MicroSD ของคุณในส่วนที่ซ่อนอยู่ `.rockbox` โฟลเดอร์
  - เริ่ม Rockbox-Y2 อย่างน้อยหนึ่งครั้งเพื่อสร้าง `.rockbox` โฟลเดอร์บนการ์ด MicroSD ของคุณ
  - แยกหรือคัดลอกไฟล์ธีมลงไป `.rockbox/` (ดังนั้น `themes`, `wps`, `fonts`และ `backdrops` ผสานเข้ากับ `.rockbox/`).
  - บนเครื่องเล่น ให้เปิด การตั้งค่า → การตั้งค่าธีม → เรียกดูไฟล์ธีม และเลือกธีมของคุณ

หากต้องการดูโฟลเดอร์ที่ซ่อนอยู่ในคอมพิวเตอร์ของคุณ: กด Cmd+Shift+. บน macOS ให้เปิดใช้งาน ดู → รายการที่ซ่อนอยู่ บน Windows หรือกด Ctrl+H บนลินุกซ์

## วิธีรีเซ็ตธีมที่เสียหาย

หากธีมทำให้หน้าจออ่านยาก ให้เปลี่ยนชื่อหรือลบ `.rockbox` โฟลเดอร์บนการ์ด MicroSD ของคุณแล้วรีสตาร์ทเครื่องเล่น Rockbox-Y2 จะสร้างความสดชื่น `.rockbox` โฟลเดอร์ที่มีธีมเริ่มต้นในขณะที่ยังคงรักษาเพลงของคุณไว้[โฟลเดอร์ .rockbox](rockbox-y2/sd-card.html)[กำลังอัปเดต Rockbox-Y2](rockbox-y2/update.html)[Rockbox-Y2 บันทึกการสร้าง](rockbox-y2/resolution.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
