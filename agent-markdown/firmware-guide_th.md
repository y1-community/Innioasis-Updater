---
title: "คู่มือการติดตั้งเฟิร์มแวร์และการเรียกคืนสต็อก | Innioasis Updater CE - Innioasis ดาวน์โหลดเฟิร์มแวร์"
description: "ติดตั้งเฟิร์มแวร์ที่กำหนดเองหรือกู้คืนเฟิร์มแวร์สต็อกจากโรงงานอย่างเป็นทางการใน Innioasis Y1, Y2, G1, G3, G5, R1, PR1 และ Timmkoo Q5, Q3 ด้วย Innioasis Updater CE"
language: "th"
source: "https://innioasis.app/firmware-guide_th.html"
---

# คู่มือการติดตั้งเฟิร์มแวร์และการเรียกคืนสต็อก | Innioasis Updater CE - Innioasis ดาวน์โหลดเฟิร์มแวร์

คู่มือการติดตั้งเฟิร์มแวร์และการกู้คืนสต็อก

# ติดตั้งหรือกู้คืนเฟิร์มแวร์บนอุปกรณ์ของคุณ

เลือกรุ่นที่พิมพ์อยู่บนเครื่องเล่นของคุณ จากนั้นทำตามขั้นตอนใน Updater CE มันจัดการส่วนที่เหลือ[รับ Updater CE](guide_th.html#platform)[เรียกดูไฟล์เก็บถาวรเฟิร์มแวร์](firmware_th.html)[การแก้ไขปัญหา](troubleshooting_th.html)

เลือกรุ่นที่พิมพ์บนเครื่องเล่นของคุณและซอฟต์แวร์ที่คุณต้องการ จากนั้นเปิดคู่มือนี้ [เรียกดูซอฟต์แวร์และเฟิร์มแวร์หุ้นตามรุ่น](firmware_th.html).

## 

[รับ Updater CE](guide_th.html#download-updater)[กวดวิชาเขียนเต็มรูปแบบ](guide_th.html)

## รับ Innioasis Updater ซีอี

ต่อไปนี้คือจุดเริ่มต้นหากคุณยังไม่มี Updater CEรับได้ที่ Updater CEพร้อมคำแนะนำในการติดตั้ง

### Windows

ดาวน์โหลดตัวติดตั้ง เปิดและปฏิบัติตามคำแนะนำในการตั้งค่า[ดาวน์โหลดและติดตั้งไดรเวอร์](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)[ดาวน์โหลดแอพและไดรเวอร์](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe)[บล็อกโดย Edge?](#)

หาก Windows หยุดคุณไม่ให้เรียกใช้แอปหรือไม่เปิดใช้งาน โปรดเปิดการตั้งค่า คลิกความเป็นส่วนตัวและความปลอดภัย → ความปลอดภัยของ Windows → การควบคุมแอปและเบราว์เซอร์ และปิดการควบคุมแอปอัจฉริยะ [Windows จะไม่เปิดแอปใช่ไหม ช่วย](#smart-app-control)

คุณจะต้องรีบูทพีซีของคุณหลังจากติดตั้งเพื่อให้ทำงานได้

### macOS

ดาวน์โหลดแอปแล้วย้ายไปที่แอปพลิเคชัน หาก macOS บล็อก ให้เปิดการตั้งค่าระบบ จากนั้นคลิกความเป็นส่วนตัวและความปลอดภัย แล้วคลิกเปิดต่อไป [วิธีการทำงานนี้](https://support.apple.com/en-gb/102445#openanyway)[ดาวน์โหลด Updater CE](https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg)

### Linux

ดาวน์โหลด AppImage สำหรับระบบ Intel และ AMD ทำให้สามารถปฏิบัติการได้ และเปิดใช้งาน[ดาวน์โหลด AppImage สำหรับ Intel/AMD](https://github.com/y1-community/innioasis-updater/releases/latest/download/UpdaterCE.AppImage)[บันทึกการตั้งค่า Linux](drivers_th.html#linux)แพลตฟอร์มอื่น?

ต้องการบันทึกการตั้งค่าคอมพิวเตอร์ที่ยาวกว่านี้หรือไม่? เปิด [Windows](drivers_th.html#windows) หรือ [Linux](drivers_th.html#linux) คู่มือการตั้งค่า

## กลับไปที่ซอฟต์แวร์ดั้งเดิม

หากต้องการย้อนกลับ เลือกรุ่นของคุณ เลือก ซอฟต์แวร์ดั้งเดิมแล้ววิ่ง ติดตั้ง / คืนค่า. นั่นคือทั้งหมดที่ Updater จะแทนที่ซอฟต์แวร์ระบบให้กับคุณ[คู่มือการคืนค่า Y1](guides/restore-original-y1.html)[คู่มือการคืนค่า Y2](guides/restore-original-y2.html)

## คำแนะนำซอฟต์แวร์ตามรุ่น

เลือกรุ่นของคุณ จากนั้นเปิดคำแนะนำสำหรับซอฟต์แวร์ของคุณ

### Innioasis Y1

ซอฟต์แวร์สำหรับ Y1:

### Innioasis Y2

ซอฟต์แวร์สำหรับ Y2:

หมายเหตุเกี่ยวกับเครื่องมือทั้งสอง

## ฉันควรใช้เครื่องมือใด

Innioasis Updater ส.ค เป็นวิธีที่ปลอดภัยที่สุดในการอัปเดตเครื่องเล่นของคุณ โดยจะเก็บเพลง วิดีโอ และการจับคู่ Bluetooth ของคุณ จะแจ้งให้คุณทราบเมื่อการอัปเดตพร้อม มันทำงานบน Windows, macOS และ Linux Innioasis Universal Flash Tool จะล้างข้อมูลเครื่องเล่นของคุณและทำงานบนคอมพิวเตอร์จำนวนน้อยลง[เปิดการเปรียบเทียบแบบเต็ม](updater-comparison_th.html)

### Windows จะไม่เปิดแอปใช่ไหม วิธีปิดการควบคุมแอปอัจฉริยะ

Windows Defender SmartScreen หรือ Smart App Control สามารถบล็อกแอปพลิเคชันชุมชนที่ดาวน์โหลดใหม่ก่อนที่จะเผยแพร่ชื่อเสียงของลายเซ็น ขณะนี้การควบคุมแอปอัจฉริยะกำลังส่งผลกระทบต่อแอปพลิเคชันยอดนิยม เช่น Epic Overlay Service (ใช้โดย Fortnite) — Updater CE ปลอดภัยและตรวจสอบแล้วว่าใช้งานได้ การปิดการควบคุมแอปอัจฉริยะทำให้ Updater CE สามารถเปิดและทำงานได้ตามปกติ
  - เปิด การตั้งค่า บนพีซี Windows ของคุณ (กด Win + I).
  - คลิก ความเป็นส่วนตัวและความปลอดภัย ในแถบด้านข้างซ้าย จากนั้นคลิก Windows Security.
  - คลิก การควบคุมแอปและเบราว์เซอร์.
  - ภายใต้ การควบคุมแอปอัจฉริยะคลิก การตั้งค่าการควบคุมแอปอัจฉริยะ.
  - ตั้งค่าสลับเป็น ปิด เพื่อให้ Updater CE สามารถเปิดใช้งานได้

บล็อกโดย Edge? หาก Microsoft Edge บล็อกการดาวน์โหลด ให้คลิกปุ่มตัวเลือกเพิ่มเติม (…) → เก็บ → แสดงเพิ่มเติม → ยังไงก็เก็บไว้.

เปิดใช้งานการควบคุมแอปอัจฉริยะอีกครั้งในภายหลัง: เมื่อคุณต้องการเปิด Smart App Control อีกครั้ง คุณสามารถเปิดใช้งานได้อีกครั้งผ่านทาง Windows Registry ที่อยู่ด้านล่าง `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` โดยการตั้งค่า `VerifiedAndReputablePolicyState` ถึง `1` (เปิด) หรือ `2` (โหมดการประเมินผล) และรีสตาร์ทปิดความช่วยเหลือ

## สิ่งนี้มีประโยชน์หรือไม่?

คำตอบของคุณช่วยปรับปรุงคู่มือนี้ใช่ ฉันพบว่ามันมีประโยชน์ยังไม่ได้[แจ้งให้เราทราบว่าเราจะปรับปรุงได้อย่างไร](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
