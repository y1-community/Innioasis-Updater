---
title: "SP Flash Tool สำหรับ Mac · MediaTek คำแนะนำและทางเลือกในการกะพริบกระจาย"
description: "วิธีใช้ SP Flash Tool บน Mac โดยใช้ Updater CE และเรียกดูไฟล์กระจายเพื่อแฟลชอุปกรณ์ MediaTek เช่น Mechen H1, Innioasis Y1/Y2, Timmkoo และ MT6580/MT6572 เครื่องเล่น MP3 และโทรศัพท์"
language: "th"
source: "https://innioasis.app/sp-flash-tool-mac_th.html"
---

# SP Flash Tool สำหรับ Mac · MediaTek คำแนะนำและทางเลือกในการกะพริบกระจาย

MediaTek เครื่องมือและการกะพริบข้ามแพลตฟอร์ม

# SP Flash Tool สำหรับ Mac: คู่มือฉบับสมบูรณ์และเบราว์เซอร์ Scatter

MediaTek SP Flash Tool อย่างเป็นทางการทำงานบน macOS หรือไม่ นี่คือสถานะที่แน่นอนอย่างไร ตัวอัพเดต CE ให้การแฟลชดั้งเดิม MediaTek บน Mac และวิธีแฟลชเครื่องเล่น MP3 หรือสมาร์ทโฟนแบบกระจาย MediaTek

## ความจริงเกี่ยวกับ SP Flash Tool บน macOS

MediaTek ไม่เคยเปิดตัวรุ่น macOS อย่างเป็นทางการของ เครื่องมือแฟลชสมาร์ทโฟน (SP Flash Tool). เครื่องมือนี้เคยมีอยู่ในแอปพลิเคชัน Windows 32 บิต/64 บิตและไบนารี x86_64 Linux เท่านั้น การจำลอง SP Flash Tool บน macOS ผ่าน Wine หรือ CrossOver ล้มเหลวเนื่องจากส่วนขยายเคอร์เนล macOS USB ไม่อนุญาตให้ส่งผ่านอนุกรม USB ด้วยความแม่นยำที่จำเป็นระหว่างการแฮนด์เชคการบูต BROM

แนวทางแก้ไข:ตัวอัพเดต CE เชื่อมช่องว่างนี้ด้วยการรวม Apple Silicon ดั้งเดิมและไลบรารีแฟลช Intel macOS (ผ่านกลไกโปรโตคอลระดับต่ำ MTKclient) ควบคู่ไปกับการค้นพบกระจายอัตโนมัติ!

## การกะพริบอุปกรณ์ MediaTek ใด ๆ ด้วย 'ติดตั้งจากไฟล์' (Scatter Browser)

Updater CE ไม่จำกัดเฉพาะผู้เล่น Innioasis คุณสามารถใช้เป็นเครื่องกระจายสัญญาณสากล MediaTek อันทรงพลังสำหรับอุปกรณ์ใดๆ ที่ต้องการ SP Flash Tool v5 หรือก่อนหน้า:
  - Mechen H1 & H11: เครื่องเล่น Android ไฮไฟแบบพกพา MT6580
  - Timmkoo Q3, Q5, G1, A5: MediaTek เครื่องเล่นเสียงดิจิตอลหน้าจอสัมผัส
  - ออยสกี้, พืออุต, ลัวราน: MediaTek เครื่องเล่นเพลง MT6572 / MT6582
  - สมาร์ทโฟนและฟีเจอร์โฟนรุ่นเก่า MediaTek: อุปกรณ์ที่ใช้ MT6572, MT6580, MT6582, MT6735, MT6737, MT6739, MT6753 และ MT8163

### วิธีโหลดไฟล์ Scatter แบบกำหนดเองใน Updater CE:
  - ดาวน์โหลดไฟล์เก็บถาวรเฟิร์มแวร์จากโรงงาน (`.zip` หรือ `.rar`) หรือแยกโฟลเดอร์ที่มีไฟล์ `*scatter*.txt` ไฟล์.
  - ใน Updater CE เลือก เรียกดูไฟล์... บนหน้าจอการเลือกเฟิร์มแวร์
  - เลือกไฟล์ข้อความกระจาย (เช่น `MT6580_Android_scatter.txt`) หรือแพ็คเกจ zip เฟิร์มแวร์
  - Updater CE แยกวิเคราะห์ออฟเซ็ตหน่วยความจำ ที่อยู่พาร์ติชัน (ตัวโหลดล่วงหน้า บูต การกู้คืน ระบบ ข้อมูลผู้ใช้) และตรวจสอบความสมบูรณ์ของการกระจาย
  - ปฏิบัติตามข้อความแจ้งสดบนหน้าจอ: ปิดอุปกรณ์และเชื่อมต่อสายเคเบิล USB เพื่อแฟลช

## เมื่อคุณต้องการคอมพิวเตอร์ x64 สำหรับการปลดอิฐ

แม้ว่า macOS จะจัดการการแฟลชมาตรฐานและการติดตั้ง ROM แบบกำหนดเองอย่างสมบูรณ์ผ่าน MTKclient แต่การกู้คืนจากความล้มเหลวของ bootloop แบบลึก (โดยที่พาร์ติชันตัวโหลดล่วงหน้าถูกล้างหรือไม่ตรงกัน) จำเป็นต้องสร้างตารางพาร์ติชันแบบเต็มของ SP Flash Tool ใหม่

หากคุณพบข้อผิดพลาดแผงลอยบน Mac ให้เปลี่ยนไปใช้พีซี Windows 64 บิตหรือเวิร์กสเตชัน x86_64 Linux ให้เลือก การตั้งค่า > แสดงการตั้งค่าขั้นสูง > วิธีแฟลช > SP Flash Toolและแฟลชแพ็คเกจกระจายของโรงงาน

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
