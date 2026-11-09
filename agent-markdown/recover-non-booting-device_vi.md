---
title: "Cách khôi phục trình phát không khởi động MediaTek sau khi MTKclient bị lỗi · Innioasis Cộng đồng"
description: "Hướng dẫn từng bước để unbrick và khôi phục các trình phát không khởi động Innioasis Y1, Y2, G1, Timmkoo và MediaTek sau khi MTKclient bị gián đoạn flash trên Linux hoặc macOS."
language: "vi"
source: "https://innioasis.app/recover-non-booting-device_vi.html"
---

# Cách khôi phục trình phát không khởi động MediaTek sau khi MTKclient bị lỗi · Innioasis Cộng đồng

Khắc phục sự cố & Khôi phục thiết bị

# Khôi phục thiết bị không khởi động được sau khi flash MTKclient

Nếu thiết bị Innioasis Y1, Y2 hoặc MediaTek của bạn không bật nguồn hoặc hiển thị màn hình đen sau khi flash bằng MTKclient trên macOS hoặc Linux, đừng hoảng sợ. BootROM phần cứng (BROM) là vĩnh viễn và không thể bị phá hủy.

## Tại sao MTKclient có thể bị treo hoặc để lại màn hình đen

MTKclient dựa vào tải trọng khai thác phần mềm (kamakiri/amonet) để vượt qua xác thực DA và giao tiếp thô USB qua libusb. Trên hệ thống macOS và Linux ARM64:
  - USB độ trễ bắt tay hoặc thời gian chờ cổng trên macOS có thể cản trở việc tiêm tải trọng DA vào giữa quá trình truyền.
  - Các tiêu đề phân vùng bị thiếu hoặc không đầy đủ khiến bộ nạp khởi động (preloader/lk) ở trạng thái không phản hồi.
  - Đầu phát dường như đã chết hoàn toàn—không có đèn LED, không có biểu tượng sạc, không có đèn nền màn hình.

Ngay cả ở trạng thái này, chipset MediaTek vẫn rơi vào trạng thái Chế độ BROM (USB VID 0e8d, PID 0003), sẵn sàng phục hồi mức độ thấp chính thức.

## Phương pháp khôi phục dứt khoát: SP Flash Tool Engine trong Updater CE

Cách an toàn nhất, đáng tin cậy nhất để khôi phục trình phát bricked của bạn là sử dụng Trình cập nhật CE được cấu hình với chính thức SP Flash Tool phụ trợ.

### Các bước chính xác trong Trình cập nhật CE:
  - Mở Trình cập nhật CE.
  - nhấp chuột Cài đặt trong thanh bên điều hướng bên trái.
  - Cuộn xuống phần Nâng cao và bật Hiển thị cài đặt nâng cao.
  - Dưới Phương pháp cài đặt (hoặc Công cụ nhấp nháy cho trình cài đặt MediaTek), xác định vị trí Phương pháp chớp nhoáng thả xuống.
  - Thay đổi lựa chọn từ Tự động (được khuyến nghị) hoặc MTKClient để SP Flash Tool.
  - Xác nhận lời nhắc và quay lại quy trình cài đặt chính.

## Kiến trúc nền tảng & Yêu cầu hệ điều hành cho SP Flash Tool

MediaTek chính thức `SP Flash Tool` nhị phân được biên dịch nguyên bản dưới dạng x86_64 ELF nhị phân cho Linux và một PE32+ có thể thực thi được cho Windows x64.Lưu ý phần cứng quan trọng dành cho người dùng macOS và ARM64 Linux:
 Vì MediaTek không biên dịch SP Flash Tool cho macOS (Darwin) hoặc Linux ARM64 (aarch64), nên người dùng macOS và người dùng ARM64 Linux (chẳng hạn như Raspberry Pi hoặc Apple Silicon chạy Asahi Linux) gặp phải cục gạch phải kết nối trình phát của họ với: 
  - Một Máy tính Windows x64 (Windows 10/11 64-bit), hoặc
  - Một Máy tính Linux x86_64 (Ubuntu, Debian, Fedora, Arch 64-bit).

## Quy trình tháo gỡ phần cứng từng bước
  - Ngắt kết nối Trình phát: Rút hoàn toàn cáp USB khỏi đầu phát và PC.
  - Tắt nguồn cứng: Giữ nút Nguồn (hoặc Nguồn + Giảm âm lượng) trong 15 giây để đảm bảo chipset đã tắt nguồn hoàn toàn và không bị kẹt trong vòng lặp USB năng lượng thấp.
  - Khởi chạy Updater CE với Chế độ SP Flash Tool: Chọn kiểu thiết bị của bạn (ví dụ: Innioasis Y1 hoặc Innioasis Y2) và chọn Phần mềm gốc để khôi phục phân vùng chứng khoán.
  - Bắt đầu cài đặt/khôi phục: nhấp chuột Cài đặt / Khôi phục trong Trình cập nhật CE. Đợi cho đến khi lời nhắc trạng thái nói Đang chờ người chơi...
  - Cắm cáp USB vào Trigger BROM: Khi thiết bị TẮT, hãy cắm trực tiếp cáp USB vào cổng USB bo mạch chủ tốc độ cao (tránh các hub USB không được cấp nguồn).
  - Hệ thống sẽ phát hiện cổng VCOM MediaTek, đẩy Tác nhân tải xuống (DA), viết lại bảng phân vùng và khôi phục sạch sẽ tất cả hình ảnh chương trình cơ sở.

## Hoán vị theo mô hình và hệ điều hành

| người mẫu | Nền tảng thất bại | Thiết lập khôi phục được đề xuất | Động cơ & Chế độ |
| --- | --- | --- | --- |
| Innioasis Y1 | macOS (Apple Silicon / Intel) | Máy tính Windows x64 / Linux x86_64 | SP Flash Tool + Y1 Cổ phiếu ROM |
| Innioasis Y1 | Linux ARM64 / x86_64 | Máy tính Linux x86_64 hoặc Windows x64 | SP Flash Tool + DA cộng đồng |
| Innioasis Y2 | macOS (MTKclient bị đình trệ) | Máy tính Windows x64 / Linux x86_64 | SP Flash Tool + Y2 Phục hồi phân tán |
| Innioasis G1 / G3 / G5 | máy khách macOS / Linux MTK | PC Windows x64 có trình điều khiển VCOM | SP Flash Tool + Firmware gốc |
| Mechen H1 / Timmkoo A5 | Bất kỳ nền tảng nào | Máy tính Windows x64 hoặc Linux x86_64 | SP Flash Tool + Tệp phân tán |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
