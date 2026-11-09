---
title: "Innioasis Y1 และ Y2 USB ไดรเวอร์ | ไดรเวอร์ Windows และการอนุญาต Linux - Innioasis Updater"
description: "ตั้งค่าคอมพิวเตอร์ของคุณสำหรับ Innioasis Updater: ไดรเวอร์ Windows MediaTek และสิทธิ์ Linux USB - พร้อมการแก้ไขสายเคเบิลและกำหนดเวลา"
language: "th"
source: "https://innioasis.app/drivers_th.html"
---

# Innioasis Y1 และ Y2 USB ไดรเวอร์ | ไดรเวอร์ Windows และการอนุญาต Linux - Innioasis Updater

การตั้งค่าคอมพิวเตอร์

# เตรียมคอมพิวเตอร์ให้พร้อมก่อนเครื่องเล่น

ปัญหาการเชื่อมต่อส่วนใหญ่มาจากไดรเวอร์ สิทธิ์อนุญาต สายเคเบิล หรือไทม์มิ่ง Windows จำเป็นต้องติดตั้งไดรเวอร์ MediaTek Linux ต้องการสิทธิ์ USB ที่ถูกต้อง ค้นหาแพลตฟอร์มของคุณด้านล่าง[รับ Updater CE](guide_th.html#platform)[การแก้ไขปัญหา](troubleshooting_th.html)

## Windows
  - ดาวน์โหลดตัวติดตั้งไดรเวอร์ MediaTek ด้านล่าง
  - เรียกใช้โปรแกรมติดตั้งและอนุญาตให้ Windows ติดตั้งไดรเวอร์
  - รีสตาร์ทคอมพิวเตอร์
  - เปิด Updater CE และรอข้อความแจ้งการเชื่อมต่อก่อนที่คุณจะเสียบปลั๊กเครื่องเล่นที่ปิดอยู่

ระบบ Windows บางระบบบล็อกไดรเวอร์ผ่านการแยกคอร์ (ความสมบูรณ์ของหน่วยความจำ) หาก Updater CE ยังคงไม่เห็นเครื่องเล่นหลังจากรีสตาร์ท ให้ปิด Memory Integrity ใน Windows Security จากนั้นรีสตาร์ท และติดตั้งไดรเวอร์ใหม่ เปิดการตั้งค่าอีกครั้งเมื่อคุณดำเนินการเสร็จสิ้นหากระบบของคุณอนุญาต

Windows จะไม่เปิดแอปใช่ไหม หาก Windows Security หรือ Smart App Control หยุด Updater CE ไม่ให้เปิด ให้เปิด การตั้งค่า (กด Win + I) → ความเป็นส่วนตัวและความปลอดภัย → Windows Security → การควบคุมแอปและเบราว์เซอร์ → การตั้งค่าการควบคุมแอปอัจฉริยะ และตั้งค่าเป็น ปิด. ขณะนี้การควบคุมแอปอัจฉริยะกำลังส่งผลกระทบต่อแอปพลิเคชันยอดนิยม เช่น Epic Overlay Service (ใช้โดย Fortnite) — Updater CE ปลอดภัยและตรวจสอบแล้วว่าใช้งานได้ หากต้องการเปิดใช้งานอีกครั้งในภายหลัง ให้ตั้งค่า `VerifiedAndReputablePolicyState` ถึง `1` (เปิด) หรือ `2` (โหมดการประเมินผล) ภายใต้ `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` ในตัวแก้ไขรีจิสทรี[ดาวน์โหลดไดรเวอร์ Windows](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[กลับไปที่คำแนะนำหลัก](guide_th.html#windows) · [ดาวน์โหลดซอฟต์แวร์](firmware_th.html)

## สิทธิ์ลินุกซ์ USB

Linux ต้องการให้บัญชีผู้ใช้ของคุณได้รับอนุญาตให้พูดคุยกับชิป MediaTek USB ภายในเครื่องเล่น Updater CE มักจะเรียงลำดับสิ่งนี้ระหว่างการติดตั้ง และการอนุญาตเดียวกันครอบคลุม SP Flash Tool ดังนั้นให้ถือว่านี่เป็นขั้นตอนการแก้ไขแทนที่จะเป็นขั้นตอนปกติ
  - เรียกใช้ Updater CE ในฐานะผู้ใช้ปกติของคุณ ไม่ใช่ในฐานะรูท โปรแกรมติดตั้งจะขอสิทธิ์การเข้าถึงของผู้ดูแลระบบเมื่อจำเป็นเท่านั้น
  - ตรวจสอบผู้เล่นว่ามองเห็นได้เลย ปิดเครื่องเล่น เชื่อมต่อสายเคเบิล และรันคำสั่ง lsusb ในเทอร์มินัล เครื่องเล่นที่เชื่อมต่อจะแสดงเป็นอุปกรณ์ MediaTek โดยมี ID ผู้จำหน่าย 0e8d
`lsusb`
  - หากปรากฏใน lsusb แต่ Innioasis Updater CE หรือ SP Flash Tool ระบุว่าสิทธิ์ถูกปฏิเสธหรือไม่สามารถเปิดพอร์ตได้ แสดงว่าผู้ใช้ของคุณไม่สามารถเข้าถึงอุปกรณ์ USB กฎ udev เดียวกันครอบคลุมเครื่องมือทั้งสอง ดังนั้นให้เพิ่มกฎที่ช่วยให้กลุ่มผู้ใช้อ่านได้
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

บันทึกบรรทัดนั้นลงในไฟล์ใหม่ชื่อ /etc/udev/rules.d/51-innioasis.rules จากนั้นรัน:`sudo udevadm control --reload && sudo udevadm trigger`
  - ถอดปลั๊กเครื่องเล่นออกจนสุด เสียบกลับเข้าไปใหม่ แล้วลองติดตั้งอีกครั้ง
  - หาก SP Flash Tool รายงานการอนุญาตแบบอนุกรมหรือการแข่งขันของพอร์ต ให้ถอดปลั๊กออกจนสุดแล้วเชื่อมต่อใหม่เมื่อได้รับแจ้งเท่านั้น
อย่าทำการชดเชยแฟลชแบบด้นสดหากคุณเปลี่ยนไปใช้เครื่องมือการกู้คืนด้วยตนเอง ให้ใช้ไฟล์และการกำหนดค่าเฉพาะรุ่นที่มาพร้อมกับโปรเจ็กต์

[กลับไปที่คำแนะนำหลัก](guide_th.html#linux) · [ดาวน์โหลดซอฟต์แวร์](firmware_th.html) · [SP Flash Tool คำแนะนำ](sp-flash-tool_th.html)

## สายเคเบิลและไทม์มิ่ง
  - ใช้สายเคเบิลข้อมูล USB ที่รู้จัก
  - หลีกเลี่ยงฮับขณะแก้ไขปัญหา
  - ปิดเครื่องรุ่นที่ถูกต้องจนสุด
  - เชื่อมต่อเมื่อได้รับแจ้งเท่านั้น

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
