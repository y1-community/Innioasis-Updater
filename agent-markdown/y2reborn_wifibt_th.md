---
title: "การตั้งค่า Wi-Fi, Bluetooth และวิทยุ FM สำหรับ Reborn (Y2Linux) - Innioasis Updater"
description: "คำแนะนำหลังการติดตั้งแบบสั้นสำหรับ Reborn (Y2Linux / Y2Reborn) บน Innioasis Y2: คัดลอก system.img จากนั้นตั้งค่า Wi-Fi, Bluetooth และวิทยุ FM"
language: "th"
source: "https://innioasis.app/y2reborn_wifibt_th.html"
---

# การตั้งค่า Wi-Fi, Bluetooth และวิทยุ FM สำหรับ Reborn (Y2Linux) - Innioasis Updater

Innioasis Y2 · Reborn หลังการติดตั้ง

# ตั้งค่า Wi-Fi, บลูทูธ และวิทยุ FM

คัดลอกไฟล์หนึ่งไฟล์ไปยังเครื่องเล่นของคุณ Reborn จัดการส่วนที่เหลือ[ดาวน์โหลด system.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[คู่มือการติดตั้ง](guides/reborn-y2linux-y2.html)[ทำไมต้อง Y2Reborn?](reborn-y2linux-benefits_th.html)

## ทำไมไฟล์นี้?

Wi-Fi, บลูทูธ และวิทยุ FM ต้องใช้โมดูลเฟิร์มแวร์ MediaTek ห้าโมดูลซึ่ง Reborn ไม่สามารถจัดส่งได้ พวกเขาอยู่ข้างในอย่างเป็นทางการ Y2 `system.img`. Reborn แยกไฟล์เหล่านั้นหนึ่งครั้ง ตรวจสอบ และลบไฟล์

## ตั้งค่า
  - ดาวน์โหลด system.img

ดาวน์โหลด v3.2.0 เอฟเอ็ม `system.img` ไปยังคอมพิวเตอร์ของคุณ[ ดาวน์โหลด system.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - บูต Reborn หนึ่งครั้ง

เปิดเครื่องเล่น รอก่อน กำลังตั้งค่าพื้นที่เก็บข้อมูล ให้เสร็จสิ้นแล้วรีสตาร์ทอีกครั้ง
  - เชื่อมต่อกับคอมพิวเตอร์ของคุณ

ใช้สายเคเบิลข้อมูล USB ผู้เล่นจะปรากฏเป็น ที่จัดเก็บข้อมูลภายใน.บน Mac?

ติดตั้ง [OpenMTP](https://openmtp.ganeshrvel.com/) เพื่อเรียกดูเครื่องเล่น Windows และ Linux ติดตั้งโดยอัตโนมัติ
  - คัดลอก system.img ไปยังเฟิร์มแวร์

สร้างโฟลเดอร์ชื่อ `Firmware` ที่รากของที่จัดเก็บข้อมูลภายใน สำเนา `system.img` เข้าไปในนั้น
  - รอให้การตั้งค่าเสร็จสิ้น

Reborn จะติดตั้งเฟิร์มแวร์วิทยุโดยอัตโนมัติและลบออก `system.img`. ขั้นตอนนี้จะใช้เวลาประมาณ 10–20 วินาที รอก่อน Wi-Fi และ Bluetooth พร้อมใช้งาน.
  - เชื่อมต่อ Wi-Fi, Bluetooth และวิทยุ FM
    - ไวไฟ: การตั้งค่า → ระบบ → เครือข่าย → Wi-Fi เลือกเครือข่าย 2.4 GHz ของคุณ
    - บลูทูธ: ให้หูฟังของคุณอยู่ในโหมดจับคู่ การตั้งค่า → บลูทูธ → เลือก
    - วิทยุเอฟเอ็ม: เสียบหูฟังแบบมีสายเป็นเสาอากาศ จากนั้นเปิดวิทยุ FM

  - อัปเดตผ่าน Wi-Fi

การอัปเดต Reborn ในอนาคตจะติดตั้งจากการตั้งค่า → ระบบ → การอัปเดตซอฟต์แวร์ เฟิร์มแวร์วิทยุของคุณยังคงอยู่

## คู่มือนี้มีประโยชน์หรือไม่?

คุณพบว่าคู่มือการตั้งค่าหลังการติดตั้งนี้มีประโยชน์หรือไม่ ใช่ มันช่วยได้! [ ต้องการความช่วยเหลือใน Discord ](https://discord.gg/zHrT2zrcek) ขอบคุณสำหรับคำติชมของคุณ! เพลิดเพลินกับการฟังแบบไร้สายบน Y2Reborn

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
