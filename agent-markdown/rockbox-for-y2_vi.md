---
title: "Rockbox for Y2 (Rockbox-Y2): tổng quan, hướng dẫn build và cài đặt"
description: "Rockbox cho Y2, Rockbox-Y2 và rockbox-y2 tham khảo cổng phần mềm cộng đồng Rockbox cho Innioasis Y2. Tìm hiểu xem nó bao gồm những gì và cách cài đặt nó với Innioasis Updater CE."
language: "vi"
source: "https://innioasis.app/rockbox-for-y2_vi.html"
---

# Rockbox for Y2 (Rockbox-Y2): tổng quan, hướng dẫn build và cài đặt

[← Tải xuống chương trình cơ sở](firmware_vi.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox cho Y2 (Rockbox-Y2)

Rockbox-Y2 (còn được gọi là “Rockbox cho Y2”) là cổng phần mềm cộng đồng Rockbox dành riêng cho Innioasis Y2. Nó sử dụng gói ROM của riêng nó (`rom_y2.zip`) và được cài đặt trực tiếp thông qua Innioasis Updater CE.[Cài đặt Rockbox-Y2](rockbox-y2/install.html)[Tải xuống ROM](rockbox-y2/download.html)[Hướng dẫn bằng văn bản](guides/rockbox-y2.html)[Rockbox-Y2 trung tâm](rockbox-y2/)

## Được xây dựng riêng cho Innioasis Y2

Trong Innioasis Updater CE, phần sụn này được liệt kê là Rockbox khi nào Y2 được chọn. Các bản phát hành của nó được xuất bản bởi [spycemagic/y2-rockbox](firmware_vi.html?model=Y2&software=rockbox-y2) dự án với tên gói `rom_y2.zip`.

Không bao giờ cài đặt gói chương trình cơ sở Y1 trên Y2. Đang chọn Y2 trong Trình cập nhật CE tự động lọc danh sách phát hành chỉ thành các bản dựng tương thích với Y2.

## Những gì Rockbox-Y2 cung cấp
  - Thư viện nhạc dựa trên thẻ — duyệt album, nghệ sĩ và thể loại từ thẻ tệp âm thanh của bạn hoặc duyệt trực tiếp các thư mục.
  - Điều khiển phát lại — cài đặt phát lại không khoảng cách, crossfade, ReplayGain và bộ chỉnh âm.
  - Chủ đề tùy chỉnh — cài đặt các chủ đề tương thích với bản dựng Rockbox-Y2 của bạn ([Y2 hướng dẫn chủ đề](rockbox-y2-themes.html)).
  - 100% ngoại tuyến — phát các tệp cục bộ từ thẻ MicroSD của bạn mà không cần có tài khoản hoặc đăng ký.
  - Khôi phục nhà máy dễ dàng — quay lại Y2 Phần mềm gốc bất kỳ lúc nào trong Updater CE.

## Chọn bản phát hành Rockbox-Y2
  - Luôn chọn Y2 trong Mẫu thiết bị đầu tiên.
  - Chọn bản phát hành mới nhất trừ khi bạn đang thử nghiệm một phiên bản cụ thể.
  - Đọc [Rockbox-Y2 ghi chú phát hành](release-notes/rockbox-y2/index_vi.html) để xem những gì đã thay đổi trong mỗi bản dựng.

## Tải xuống trực tiếp từ các nhà phát triển cộng đồng

Innioasis Trình cập nhật CE luôn tải xuống các gói chương trình cơ sở trực tiếp từ các nhà phát triển chương trình cơ sở cộng đồng ([spycemagic/y2-rockbox](firmware_vi.html?model=Y2&software=rockbox-y2)) và những nhà phát triển đó hoàn toàn chịu trách nhiệm liệt kê các bản phát hành phần mềm của họ trong Updater CE.

Bạn có thể để Updater CE tải về và flash `rom_y2.zip` tự động hoặc tải xuống gói từ [Rockbox-Y2 trang tải xuống](rockbox-y2/download.html) và [Rockbox ROM trang tải xuống](rockbox-rom-download_vi.html).[Rockbox-Y2 lượt tải xuống](rockbox-y2/download.html)[Cài đặt từ ZIP cục bộ](rockbox-y2/portable-zip.html)

## Cách cài đặt Rockbox-Y2
  - Mở Innioasis Updater CE và thiết lập Mẫu thiết bị để Y2.
  - chọn Rockbox trong Phần mềm.
  - Chọn bản phát hành Y2 từ danh sách.
  - nhấp chuột Cài đặt / Khôi phục vì vậy Updater CE tải gói xuống trực tiếp từ nhà phát triển.
  - Tắt nguồn hoàn toàn Y2 và kết nối nó với cáp dữ liệu USB khi Trình cập nhật CE yêu cầu.
  - Đợi thông báo hoàn thành, sau đó rút phích cắm và bật Y2.

Để có hướng dẫn từng bước đầy đủ, hãy đọc phần [Rockbox-Y2 hướng dẫn](guides/rockbox-y2.html).

## Khôi phục phần mềm Y2 gốc

Để quay lại chương trình cơ sở gốc, hãy chọn Y2 và Phần mềm gốc trong Updater CE, chọn bản phát hành ổn định và nhấp vào Cài đặt / Khôi phục. Xem [hướng dẫn khôi phục](rockbox-y2/restore-stock.html) và [Y2 Trang phần mềm gốc](original-software-y2_vi.html).

## Câu hỏi thường gặpTrình cập nhật CE tải xuống Rockbox-Y2 từ đâu?

Trình cập nhật CE luôn tải xuống các gói chương trình cơ sở trực tiếp từ các bản phát hành của chính nhà phát triển chương trình cơ sở cộng đồng (`spycemagic/y2-rockbox`). Các nhà phát triển hoàn toàn chịu trách nhiệm liệt kê các bản phát hành phần mềm của họ trong Updater CE.Tại sao gói có tên rom_y2.zip?

Nhà phát triển đặt tên cho kho lưu trữ phần sụn Y2 `rom_y2.zip` vì vậy nó không thể bị nhầm lẫn với Y1's `rom.zip`.Chủ đề Y1 có hoạt động trên Y2 không?

Không phải lúc nào cũng vậy. Kiểm tra ghi chú phát hành cho bản dựng Y2 của bạn và xem [Rockbox-Y2 hướng dẫn chủ đề](rockbox-y2-themes.html).

## Hướng dẫn liên quan

### [Rockbox-Y2 trung tâm](rockbox-y2/)

Tất cả hướng dẫn Y2: cài đặt, tải xuống, chủ đề, khôi phục, khởi động kép và khắc phục sự cố.

### [Rockbox-Y1 so với Rockbox-Y2](rockbox-y1-vs-y2.html)

Bản dựng Y1 và Y2 Rockbox khác nhau như thế nào.

### [Rockbox-Y2 chủ đề](rockbox-y2-themes.html)

Cài đặt và đặt lại chủ đề trên Rockbox-Y2.

### [Rockbox cho Y1](rockbox-for-y1_vi.html)

Tổng quan và hướng dẫn cài đặt cổng Innioasis Y1.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
