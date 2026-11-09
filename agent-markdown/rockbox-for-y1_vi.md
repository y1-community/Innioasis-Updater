---
title: "Rockbox for Y1 (Rockbox-Y1): tổng quan, hướng dẫn build và cài đặt"
description: "Rockbox cho Y1, Rockbox-Y1 và rockbox-y1 đều đề cập đến phần sụn Rockbox cộng đồng cho Innioasis Y1. Tìm hiểu những gì nó bổ sung, nên chọn bản dựng nào và cách cài đặt nó với Innioasis Updater CE."
language: "vi"
source: "https://innioasis.app/rockbox-for-y1_vi.html"
---

# Rockbox for Y1 (Rockbox-Y1): tổng quan, hướng dẫn build và cài đặt

[← Tải xuống chương trình cơ sở](firmware_vi.html?model=Y1&software=rockbox-y1)

Rockbox-Y1 · Innioasis Y1

# Rockbox cho Y1 (Rockbox-Y1)

“Rockbox”, “Rockbox-Y1”, và “Rockbox cho Y1” đều đề cập đến cùng một cộng đồng chương trình cơ sở Rockbox cho Innioasis Y1. Đây là những gì nó bổ sung vào trình phát của bạn, nên chọn bản dựng nào và cách cài đặt nó với Innioasis Updater CE.[Cài đặt Rockbox-Y1](rockbox-y1/install.html)[Tải xuống ROM](rockbox-y1/download.html)[Hướng dẫn bằng văn bản](guides/rockbox-y1.html)[Rockbox-Y1 trung tâm](rockbox-y1/)

## Một phần mềm, nhiều tên

Trong Innioasis Updater CE, phần sụn này xuất hiện dưới dạng Rockbox khi bạn chọn mẫu thiết bị Y1. Hướng dẫn, video và ghi chú phát hành cũng gọi nó là Rockbox-Y1 hoặc Rockbox cho Y1 vì vậy rõ ràng là bản dựng dành cho Y1 chứ không phải Y2.

Luôn kiểm tra mẫu máy được in trên đầu phát của bạn trước khi cài đặt: các gói chương trình cơ sở Y1 và Y2 không thể thay thế cho nhau.

## Rockbox-Y1 thêm gì vào Y1 của bạn

Rockbox-Y1 là một cổng cộng đồng của chương trình cơ sở trình phát nhạc mã nguồn mở Rockbox dành cho Innioasis Y1:
  - Thư viện nhạc dựa trên thẻ - duyệt theo nghệ sĩ, album, thể loại và năm bằng thẻ âm thanh hoặc duyệt trực tiếp các thư mục.
  - Phát lại âm thanh nâng cao — phát lại không khoảng cách, crossfade, ReplayGain và bộ cân bằng đầy đủ.
  - Chủ đề tùy chỉnh — chọn từ hàng trăm chủ đề cộng đồng 240p và 360p, bao gồm cả bố cục kiểu iPod cổ điển.
  - Đài FM - Hỗ trợ đài FM tích hợp.
  - Tính năng bổ sung tùy chọn - tải xuống podcast qua Wi-Fi và Last.fm / ListenBrainz / Maloja trên các bản dựng được hỗ trợ.
  - Khởi động kép — chuyển trở lại Phần mềm gốc của nhà sản xuất mà không cần cài đặt lại trên các bản dựng được hỗ trợ.

## Tôi nên chọn bản dựng Y1 nào?
  - 240p so với 360p — Bản dựng 240p hoạt động với chủ đề 320×240 Rockbox cổ điển; Bản dựng 360p sử dụng chủ đề 480×360 Y1 sắc nét hơn. Khớp độ phân giải bản dựng với chủ đề bạn muốn sử dụng ([Hướng dẫn 240p so với 360p](rockbox-y1/resolution.html)).
  - Type A so với Type B — Type A dành cho Y1 người chơi được cài đặt phần mềm gốc 2.0.0 trở lên; Type B dành cho các đơn vị Y1 trước đó. Chọn Type A trừ khi bạn biết Y1 của bạn là Type B.
  - Ổn định so với hàng đêm — Chọn bản dựng ổn định để nghe hàng ngày hoặc bản dựng hàng đêm để kiểm tra những thay đổi mới nhất.

## Tải xuống trực tiếp từ các nhà phát triển cộng đồng

Innioasis Trình cập nhật CE luôn tải xuống các gói chương trình cơ sở trực tiếp từ các nhà phát triển chương trình cơ sở cộng đồng ([rockbox-y1/rockbox](firmware_vi.html?model=Y1&software=rockbox-y1)) và bản thân các nhà phát triển hoàn toàn chịu trách nhiệm liệt kê các bản phát hành phần mềm của họ trong Updater CE.

Bạn có thể để Updater CE tải xuống và cài đặt chương trình cơ sở tự động hoặc tải xuống các gói ROM từ trang web của chúng tôi. [Rockbox-Y1 trang tải xuống](rockbox-y1/download.html) và [Rockbox ROM trang tải xuống](rockbox-rom-download_vi.html).[Rockbox-Y1 lượt tải xuống](rockbox-y1/download.html)[Cài đặt từ ZIP cục bộ](rockbox-y1/portable-zip.html)

## Cách cài đặt Rockbox-Y1
  - Mở Innioasis Updater CE và thiết lập Mẫu thiết bị để Y1.
  - chọn Rockbox trong Phần mềm.
  - Chọn bản phát hành ổn định (hoặc bật bản dựng hàng đêm để kiểm tra bản xem trước).
  - nhấp chuột Cài đặt / Khôi phục vì vậy Updater CE tải gói xuống trực tiếp từ nhà phát triển.
  - Tắt nguồn hoàn toàn Y1 và kết nối nó với cáp dữ liệu USB khi Trình cập nhật CE nhắc bạn.
  - Đợi thông báo hoàn thành, sau đó ngắt kết nối và bật trình phát của bạn.

Để biết ảnh chụp màn hình và mẹo thiết lập chi tiết, hãy đọc phần [hướng dẫn đầy đủ Rockbox-Y1](guides/rockbox-y1.html).

## Khôi phục phần mềm Y1 gốc

Bạn có thể quay lại phần mềm xuất xưởng bất cứ lúc nào: chọn Y1 và Phần mềm gốc trong Updater CE, chọn bản phát hành ổn định và nhấp vào Cài đặt / Khôi phục. Nhạc của bạn trên thẻ MicroSD sẽ được giữ nguyên. Xem [hướng dẫn khôi phục](rockbox-y1/restore-stock.html) và [Y1 Trang phần mềm gốc](original-software-y1_vi.html).

## Câu hỏi thường gặpRockbox của Y1 có giống với Rockbox-Y1 không?

Vâng. Rockbox, Rockbox-Y1, Rockbox cho Y1 và `rockbox-y1` tất cả đều đề cập đến cùng một cổng cộng đồng Rockbox cho Innioasis Y1.Trình cập nhật CE tải xuống Rockbox-Y1 từ đâu?

Trình cập nhật CE luôn tải xuống các gói chương trình cơ sở trực tiếp từ các bản phát hành của chính nhà phát triển chương trình cơ sở cộng đồng (`rockbox-y1/rockbox`). Các nhà phát triển hoàn toàn chịu trách nhiệm liệt kê các bản phát hành phần mềm của họ trong Updater CE.Tôi có thể cài đặt Rockbox-Y1 trên Y2 không?

Không. Y2 có bản dựng chương trình cơ sở riêng. sử dụng [Rockbox cho Y2](rockbox-for-y2_vi.html) thay vào đó.Việc cài đặt Rockbox-Y1 có xóa nhạc của tôi không?

Không. Nhạc được lưu trên thẻ MicroSD và không bị ảnh hưởng khi flash firmware bên trong của đầu phát.

## Hướng dẫn liên quan

### [Rockbox-Y1 trung tâm](rockbox-y1/)

Tất cả hướng dẫn Y1: cài đặt, tải xuống, chủ đề, khôi phục, khởi động kép và khắc phục sự cố.

### [Rockbox-Y1 so với Rockbox-Y2](rockbox-y1-vs-y2.html)

Bản dựng Y1 và Y2 Rockbox khác nhau như thế nào.

### [Rockbox-Y1 chủ đề](rockbox-y1-themes.html)

Cách chuyển chủ đề 240p và 360p bằng Updater CE.

### [Rockbox tổng quan](rockbox_vi.html)

Giới thiệu về Rockbox trên người chơi Innioasis Y1 và Y2.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
