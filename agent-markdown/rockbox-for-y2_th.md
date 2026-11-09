---
title: "Rockbox สำหรับ Y2 (Rockbox-Y2): ภาพรวม บิลด์ และคู่มือการติดตั้ง"
description: "Rockbox สำหรับ Y2, Rockbox-Y2 และ rockbox-y2 หมายถึงพอร์ตเฟิร์มแวร์ชุมชน Rockbox สำหรับ Innioasis Y2 เรียนรู้ว่ามีอะไรบ้างและจะติดตั้งอย่างไรด้วย Innioasis Updater CE"
language: "th"
source: "https://innioasis.app/rockbox-for-y2_th.html"
---

# Rockbox สำหรับ Y2 (Rockbox-Y2): ภาพรวม บิลด์ และคู่มือการติดตั้ง

[← ดาวน์โหลดเฟิร์มแวร์](firmware_th.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox สำหรับ Y2 (Rockbox-Y2)

Rockbox-Y2 (เรียกอีกอย่างว่า "Rockbox สำหรับ Y2") คือพอร์ตเฟิร์มแวร์ชุมชน Rockbox เฉพาะสำหรับ Innioasis Y2 มันใช้แพ็คเกจ ROM ของตัวเอง (`rom_y2.zip`) และติดตั้งโดยตรงผ่าน Innioasis Updater CE[ติดตั้ง Rockbox-Y2](rockbox-y2/install.html)[ดาวน์โหลด ROM](rockbox-y2/download.html)[กวดวิชาเขียน](guides/rockbox-y2.html)[Rockbox-ฮับ Y2](rockbox-y2/)

## สร้างขึ้นโดยเฉพาะสำหรับ Innioasis Y2

ใน Innioasis Updater CE เฟิร์มแวร์นี้แสดงเป็น Rockbox เมื่อไร Y2 ถูกเลือก การเผยแพร่ได้รับการเผยแพร่โดย [spycemagic/y2-rockbox](firmware_th.html?model=Y2&software=rockbox-y2) โครงการที่มีชื่อแพ็คเกจ `rom_y2.zip`.

ห้ามติดตั้งแพ็คเกจเฟิร์มแวร์ Y1 บน Y2 การเลือก Y2 ใน Updater CE จะกรองรายการรีลีสโดยอัตโนมัติเป็น Y2 - บิลด์ที่เข้ากันได้เท่านั้น

## สิ่งที่ Rockbox-Y2 นำเสนอ
  - คลังเพลงตามแท็ก — เรียกดูอัลบั้ม ศิลปิน และแนวเพลงจากแท็กไฟล์เสียงของคุณ หรือเรียกดูโฟลเดอร์โดยตรง
  - การควบคุมการเล่น - การเล่นแบบไม่มีช่องว่าง, ครอสเฟด, ReplayGain และการตั้งค่าอีควอไลเซอร์
  - ธีมที่กำหนดเอง — ติดตั้งธีมที่เข้ากันได้กับบิลด์ Rockbox-Y2 ของคุณ ([Y2 คำแนะนำธีม](rockbox-y2-themes.html)).
  - ออฟไลน์ 100% — เล่นไฟล์ในเครื่องจากการ์ด MicroSD ของคุณโดยไม่มีบัญชีหรือการสมัครรับข้อมูล
  - คืนค่าโรงงานได้ง่าย — กลับสู่ Y2 ซอฟต์แวร์ต้นฉบับเมื่อใดก็ได้ใน Updater CE

## การเลือกรุ่น Rockbox-Y2
  - เลือกอยู่เสมอ Y2 ใน รุ่นอุปกรณ์ ก่อน
  - เลือกรุ่นล่าสุด เว้นแต่ว่าคุณกำลังทดสอบเวอร์ชันเฉพาะ
  - อ่าน [Rockbox-บันทึกประจำรุ่น Y2](release-notes/rockbox-y2/index_th.html) เพื่อดูว่ามีอะไรเปลี่ยนแปลงไปบ้างในแต่ละรุ่น

## ดาวน์โหลดโดยตรงจากนักพัฒนาชุมชน

Innioasis Updater CE ดาวน์โหลดแพ็คเกจเฟิร์มแวร์โดยตรงจากผู้พัฒนาเฟิร์มแวร์ชุมชนเสมอ ([spycemagic/y2-rockbox](firmware_th.html?model=Y2&software=rockbox-y2)) และนักพัฒนาเหล่านั้นมีหน้าที่รับผิดชอบแต่เพียงผู้เดียวในการแสดงรายการซอฟต์แวร์ของตนใน Updater CE

คุณสามารถให้ Updater CE ดาวน์โหลดและแฟลชได้ `rom_y2.zip` อัตโนมัติหรือดาวน์โหลดแพ็คเกจจากเรา [Rockbox-Y2 หน้าดาวน์โหลด](rockbox-y2/download.html) และ [Rockbox ROM หน้าดาวน์โหลด](rockbox-rom-download_th.html).[Rockbox-Y2 ดาวน์โหลด](rockbox-y2/download.html)[ติดตั้งจาก ZIP ในเครื่อง](rockbox-y2/portable-zip.html)

## วิธีการติดตั้ง Rockbox-Y2
  - เปิด Innioasis Updater CE และตั้งค่า รุ่นอุปกรณ์ ถึง Y2.
  - เลือก Rockbox ใน ซอฟต์แวร์.
  - เลือกรุ่น Y2 จากรายการ
  - คลิก ติดตั้ง / คืนค่า ดังนั้น Updater CE จึงดาวน์โหลดแพ็คเกจโดยตรงจากผู้พัฒนา
  - ปิด Y2 โดยสมบูรณ์แล้วเชื่อมต่อด้วยสายเคเบิลข้อมูล USB เมื่อ Updater CE ถาม
  - รอข้อความแจ้งเสร็จสิ้น จากนั้นถอดปลั๊กแล้วเปิด Y2

สำหรับคำแนะนำแบบทีละขั้นตอนทั้งหมด โปรดอ่าน [Rockbox-Y2 บทช่วยสอน](guides/rockbox-y2.html).

## การกู้คืนซอฟต์แวร์ Y2 ดั้งเดิม

หากต้องการกลับไปใช้เฟิร์มแวร์จากโรงงาน ให้เลือก Y2 และ ซอฟต์แวร์ดั้งเดิม ใน Updater CE เลือกรุ่นที่เสถียร แล้วคลิก ติดตั้ง / คืนค่า. ดู [คู่มือการคืนค่า](rockbox-y2/restore-stock.html) และ [Y2 หน้าซอฟต์แวร์ต้นฉบับ](original-software-y2_th.html).

## คำถามที่พบบ่อยUpdater CE ดาวน์โหลด Rockbox-Y2 จากที่ไหน

Updater CE ดาวน์โหลดแพ็คเกจเฟิร์มแวร์โดยตรงจากรีลีสของผู้พัฒนาเฟิร์มแวร์ชุมชนเสมอ (`spycemagic/y2-rockbox`). นักพัฒนามีหน้าที่รับผิดชอบแต่เพียงผู้เดียวในการแสดงรายการซอฟต์แวร์ของตนใน Updater CEเหตุใดแพ็คเกจจึงมีชื่อว่า rom_y2.zip

นักพัฒนาตั้งชื่อไฟล์เก็บถาวรเฟิร์มแวร์ Y2 `rom_y2.zip` ดังนั้นจึงไม่สามารถสับสนกับของ Y1 ได้ `rom.zip`.ธีม Y1 ใช้งานได้บน Y2 หรือไม่

ไม่เสมอไป ตรวจสอบบันทึกประจำรุ่นสำหรับบิลด์ Y2 ของคุณและดู [Rockbox-Y2 คำแนะนำธีม](rockbox-y2-themes.html).

## คำแนะนำที่เกี่ยวข้อง

### [Rockbox-ฮับ Y2](rockbox-y2/)

คำแนะนำ Y2 ทั้งหมด: การติดตั้ง ดาวน์โหลด ธีม การคืนค่า การบู๊ตคู่ และการแก้ไขปัญหา

### [Rockbox-Y1 กับ Rockbox-Y2](rockbox-y1-vs-y2.html)

การสร้าง Y1 และ Y2 Rockbox แตกต่างกันอย่างไร

### [Rockbox-ธีม Y2](rockbox-y2-themes.html)

การติดตั้งและการรีเซ็ตธีมบน Rockbox-Y2

### [Rockbox สำหรับ Y1](rockbox-for-y1_th.html)

ภาพรวมและคำแนะนำในการติดตั้งสำหรับพอร์ต Innioasis Y1

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
