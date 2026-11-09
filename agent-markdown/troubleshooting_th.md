---
title: "Innioasis Updater การแก้ไขปัญหา | Innioasis และ Timmkoo ปัญหาการติดตั้ง - Innioasis Updater"
description: "แก้ไขการติดตั้ง Innioasis Updater บนเครื่องเล่น Innioasis หรือ Timmkoo ตรวจสอบรุ่น สายเคเบิล ไดรเวอร์ เวลาในการปิดเครื่อง และตำแหน่งที่การติดตั้งหยุดลง จากนั้นให้แฟลชอีกครั้ง"
language: "th"
source: "https://innioasis.app/troubleshooting_th.html"
---

# Innioasis Updater การแก้ไขปัญหา | Innioasis และ Timmkoo ปัญหาการติดตั้ง - Innioasis Updater

การแก้ไขปัญหา

# ค้นหาจุดที่การติดตั้งหยุดลง

มันหยุดตรงไหน? นั่นจะบอกคุณว่าต้องแก้ไขอะไร[กลับสู่คำแนะนำปกติ](guide_th.html)[ตรวจสอบเฟิร์มแวร์](firmware_th.html)

## มันหยุดก่อนข้อความแจ้ง USB

นี่เป็นปัญหาของคอมพิวเตอร์ ไม่ใช่ปัญหาเกี่ยวกับสายเคเบิล ตรวจสอบรุ่นของคุณ แตกไฟล์อีกครั้ง จากนั้นลอง ติดตั้ง / คืนค่า. หากรายการเผยแพร่ว่างเปล่า ให้เปิด [ไดเร็กทอรีเฟิร์มแวร์](firmware_th.html).

## ไม่สามารถเชื่อมต่อกับเครื่องเล่นได้
  - ปิด Y1 หรือ Y2 ที่ถูกต้องจนสุด
  - ถอดสายเคเบิล ปิดแฟลชหรือเครื่องมือ Android อื่นๆ แล้วเริ่มการติดตั้งอีกครั้ง
  - เชื่อมต่อเฉพาะเมื่อ Updater บอกว่าพร้อมแล้ว
  - ใช้สายเคเบิลข้อมูลสั้น USB โดยตรงในคอมพิวเตอร์ ไม่ใช่ฮับ หากเป็นไปได้
  - บน Windows ให้ติดตั้งไดรเวอร์ MediaTek ใหม่แล้วรีสตาร์ท บน Linux ให้ตรวจสอบสิทธิ์ USB/serial
พรอมต์การเชื่อมต่อตัวอัปเดตพรอมต์ Live Updater นั้นเชื่อถือได้สำหรับรุ่นและแพลตฟอร์มปัจจุบัน

## ตรวจพบเครื่องเล่นแต่แฟลชล้มเหลว

หยุดที่นี่ อย่าลองใช้รุ่นอื่น ปิดเครื่องมืออื่นๆ ตรวจสอบว่าคุณเลือก Y1 หรือ Y2 ที่ถูกต้อง และใช้ซอฟต์แวร์ต้นฉบับที่ตรงกันหากเครื่องเล่นไม่เริ่มทำงาน [SP Flash Tool](sp-flash-tool_th.html) และ MTKClient จะรวมอยู่ด้วยหากคุณต้องการ และไฟล์จะอยู่ใน [หน้าเฟิร์มแวร์](firmware_th.html).

## หมายเหตุไดรเวอร์ Windows

การติดตั้ง Windows บางอย่างบล็อกไดรเวอร์ MediaTek เนื่องจากการแยกคอร์ ปฏิบัติตามคำแนะนำด้านความปลอดภัยของ Windows ปัจจุบันก่อนที่จะเปลี่ยนความสมบูรณ์ของหน่วยความจำ และเปิดอีกครั้งเมื่อคุณดำเนินการเสร็จสิ้นหากระบบของคุณอนุญาต[เปิดคู่มือผู้ขับขี่](drivers_th.html)[คู่มือการติดตั้งใหม่ทั้งหมด](Troubleshooting/clean_install.html)

## วงล้อไม่ทำงาน หรือผู้เล่นจะไม่สตาร์ท

ข้อผิดพลาดด้านอินพุตและกำลังไฟต้องมีขั้นตอนที่แตกต่างจากแฟลชที่ล้มเหลว คำแนะนำเหล่านี้ครอบคลุมกรณีทั่วไปของ Y1 และ Y2[Y1 ล้อเลื่อน](guides/y1-scroll-wheel-not-working.html)[Y2 ล้อเลื่อน](guides/y2-scroll-wheel-not-working.html)[Y1 เปิดไม่ติด](guides/y1-wont-turn-on.html)[Y2 เปิดไม่ติด](guides/y2-wont-turn-on.html)[คู่มือการกู้คืน](guides/recovery.html)

## ยังติดอยู่เหรอ?

เมื่อขอความช่วยเหลือ ให้ระบุรุ่น ระบบปฏิบัติการ ข้อความ Updater ที่แน่นอน ตรวจพบเครื่องเล่นหรือไม่ และแพ็คเกจ/โปรเจ็กต์ที่คุณเลือก ห้ามโพสต์โทเค็นส่วนตัวหรือไฟล์ระบบที่ไม่เกี่ยวข้อง[ขอความช่วยเหลือ](https://discord.gg/zHrT2zrcek)[รองรับการบำรุงรักษา](support_devs_th.html#donations)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
