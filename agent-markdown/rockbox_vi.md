---
title: "Cách cài đặt Rockbox trên Innioasis Y1 hoặc Y2 - Innioasis Trình cập nhật của bạn"
description: "Cài đặt Rockbox trên Innioasis Y1 hoặc Y2 với Trình cập nhật: chủ đề, bản phát hành ổn định, ghi chú Type A và Type B cũng như cách khôi phục Phần mềm gốc sau đó."
language: "vi"
source: "https://innioasis.app/rockbox_vi.html"
---

# Cách cài đặt Rockbox trên Innioasis Y1 hoặc Y2 - Innioasis Trình cập nhật của bạn

Rockbox tài liệu tham khảo

# Nhận Rockbox trên Y1 hoặc Y2 của bạn

Rockbox thay đổi phần mềm trình phát và mở ra giao diện trình phát nhạc sâu hơn, các điều khiển phát lại, sắp xếp và tùy chọn chủ đề. Quá trình cài đặt được hướng dẫn, nhưng Y1 và Y2 là các hành trình riêng biệt.[Rockbox trên Y1](guides/rockbox-y1.html)[Rockbox trên Y2](guides/rockbox-y2.html)[Tại sao Rockbox?](rockbox-benefits_vi.html)

## Cài đặt thay đổi gì

Rockbox là phần mềm tùy chỉnh. Nó không loại bỏ khả năng quay lại giao diện gốc của bạn khi có sẵn gói Phần mềm gốc phù hợp. Nó có thể cải thiện khả năng duyệt và tùy chỉnh nhạc nhưng các tính năng, độ phân giải, thời lượng pin và khả năng tương thích chủ đề đều phụ thuộc vào bản dựng.Không trộn lẫn các mô hình. Chọn Y1 cho người chơi Y1 và Y2 cho người chơi Y2. Tên phát hành trông giống nhau không đủ bằng chứng cho thấy một gói tương thích.

## Xem video

Video của Frawgeeys. Nó hiển thị lộ trình Trình cập nhật Innioasis; hãy sử dụng các bước viết dành riêng cho từng mẫu bên dưới cho Y1 hoặc Y2 của bạn.

Video của [Cristian Plaza](https://www.youtube.com/@CristianPlaza) (Tiếng Tây Ban Nha), hiển thị Rockbox trên Y1. Hãy sử dụng các bước dành riêng cho từng mẫu máy bên dưới cho trình phát của bạn.

## Lộ trình cập nhật được chia sẻ
  - Cài đặt Trình cập nhật và không kết nối gì cho đến khi được yêu cầu.
  - Chọn mẫu in trên máy nghe nhạc Mẫu thiết bị.
  - chọn Rockbox trong Phần mềm.
  - Chọn bản phát hành ổn định trừ khi bạn cố tình thử nghiệm bản dựng hàng đêm.
  - nhấp chuột Cài đặt / Khôi phục, sau đó làm theo lời nhắc tắt nguồn và kết nối USB.
  - Chỉ ngắt kết nối sau khi có thông báo thành công.

## 240p, 360p và chủ đề

Bộ sưu tập chủ đề Rockbox cũ hơn có thể được tạo trong 240p. Y1 bản dựng cộng đồng cũng sử dụng nhãn tương thích 360p. Đọc ghi chú phát hành và nguồn chủ đề trước khi chọn bản dựng. Chủ đề được tạo cho một độ phân giải hoặc dòng phần mềm có thể không hoạt động trên một độ phân giải hoặc dòng phần mềm khác.[Duyệt qua các chủ đề cộng đồng](https://themes.innioasis.app/?lang=vi)[Công cụ chủ đề](https://themes.innioasis.app/?lang=vi)

## Quay lại phần mềm gốc

Chọn lại cùng một mô hình, chọn Phần mềm gốc, chọn bản phát hành ổn định và sử dụng Cài đặt / Khôi phục. Nếu lỗi xảy ra trước dấu nhắc USB, hãy kiểm tra máy tính và giải nén các tập tin. Nếu phát hiện được trình phát nhưng flash không thành công, hãy bắt đầu với [khắc phục sự cố](troubleshooting_vi.html).[Y1 khôi phục](guides/restore-original-y1.html)[Y2 khôi phục](guides/restore-original-y2.html)

## Câu hỏi thường gặpTôi đã cài đặt lại Rockbox và nó không khắc phục được gì.

Việc cài đặt lại Rockbox ghi cùng một bản dựng trên cùng một tệp, vì vậy nó không thể đặt lại những thứ Rockbox lưu trên MicroSD. Nếu sự cố là do cài đặt, chủ đề, danh sách phát hoặc cơ sở dữ liệu nằm trên thẻ bị hỏng thì việc cài đặt lại sẽ không xóa được sự cố đó. Việc thiết lập lại đáng tin cậy đang xóa `.rockbox` thư mục từ MicroSD — Rockbox tạo một thư mục mới vào lần khởi động tiếp theo.
  - Tắt nguồn hoàn toàn đầu phát và tháo thẻ MicroSD hoặc kết nối đầu phát dưới dạng ổ USB.
  - Hiển thị các tập tin ẩn trên máy tính của bạn để hiển thị thư mục. Cách hiện file ẩnHiển thị dotfiles trên máy tính của bạnWindows: trong File Explorer mở Xem tab và đánh dấu Mục ẩn.macOS: trong Finder nhấn Cmd+Shift+. để chuyển đổi các tập tin ẩn.Linux · Tệp Gnome: nhấn Ctrl+H, hoặc mở menu và chọn Hiển thị tập tin ẩn.Linux · Cá heo KDE: nhấn Ctrl+H, hoặc sử dụng Xem → Hiển thị tập tin ẩn.
  - Xóa `.rockbox` thư mục từ thư mục gốc của thẻ.
  - Lắp lại thẻ và khởi động trình phát. Rockbox tạo lại thư mục có giá trị mặc định.
  - Áp dụng lại chủ đề và cài đặt của bạn. Nếu sự cố chỉ tái diễn sau một chủ đề cụ thể thì chủ đề đó chính là nguyên nhân.

Đang xóa `.rockbox` không gỡ cài đặt Rockbox và không chạm vào nhạc của bạn — thư mục chứa các cài đặt, chủ đề và bộ nhớ đệm, đồng thời được xây dựng lại tự động. Nếu bạn muốn giữ chủ đề của mình, hãy sao chép thư mục ra khỏi `.rockbox` trước khi xóa nó hoặc đổi tên thư mục thành `.rockbox-old` đầu tiên.Tại sao tôi không thể thấy thư mục .rockbox trên MicroSD của mình?

Theo mặc định, các thư mục có tên bắt đầu bằng dấu chấm sẽ bị ẩn trên hầu hết các máy tính. Bạn không cần phải xem nó để cài đặt Rockbox — Trình cập nhật sẽ xử lý các tệp. Nếu bạn đang khắc phục sự cố và muốn xóa nó, trước tiên hãy bật các tập tin ẩn. Cách hiện file ẩnHiển thị dotfiles trên máy tính của bạnWindows: trong File Explorer mở Xem tab và đánh dấu Mục ẩn.macOS: trong Finder nhấn Cmd+Shift+. để chuyển đổi các tập tin ẩn.Linux · Tệp Gnome: nhấn Ctrl+H, hoặc mở menu và chọn Hiển thị tập tin ẩn.Linux · Cá heo KDE: nhấn Ctrl+H, hoặc sử dụng Xem → Hiển thị tập tin ẩn.Việc xóa .rockbox có đặt lại chủ đề và cài đặt của tôi không?

Vâng - `.rockbox` chứa các cài đặt, chủ đề, danh sách phát và cơ sở dữ liệu được lưu trong bộ nhớ cache của Rockbox. Xóa nó sẽ trả Rockbox về trạng thái mặc định rõ ràng. Sao lưu toàn bộ thư mục (hoặc đổi tên thành `.rockbox-old`) nếu bạn muốn lấy lại bất kỳ thứ gì trong số đó, hãy khởi động trình phát và Rockbox tạo một thư mục mới.

## Hướng dẫn khác về Rockbox-Y1 và Rockbox-Y2

Khám phá hướng dẫn từng bước để cài đặt, tải xuống, tạo chủ đề, khôi phục và khắc phục sự cố Rockbox trên cả hai kiểu máy:[Rockbox-Y1 trung tâm](rockbox-y1/)[Rockbox-Y2 trung tâm](rockbox-y2/)[Rockbox bản tải xuống ROM](rockbox-rom-download_vi.html)[Rockbox cho Y1](rockbox-for-y1_vi.html)[Rockbox cho Y2](rockbox-for-y2_vi.html)[Rockbox-Y1 vs Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1 chủ đề](rockbox-y1-themes.html)[Rockbox-Y2 chủ đề](rockbox-y2-themes.html)

## Tài liệu tham khảo này có hữu ích không?

Câu trả lời của bạn giúp cải thiện hướng dẫn này.CóChưa[Hãy cho chúng tôi biết cách chúng tôi có thể cải thiện](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
