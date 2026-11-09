---
title: "SP Flash Tool dành cho Innioasis &amp; Timmkoo Người chơi"
description: "Tìm SP Flash Tool đi kèm với Innioasis Trình cập nhật trên Windows và Linux, giải nén rom.zip hoặc rom_y2.zip và flash Innioasis Y1 hoặc Y2 bằng tệp phân tán phù hợp."
language: "vi"
source: "https://innioasis.app/sp-flash-tool_vi.html"
---

# SP Flash Tool dành cho Innioasis &amp; Timmkoo Người chơi

Nhấp nháy thủ công

# Công cụ Flash dành cho người chơi Innioasis và Timmkoo

SP Flash Tool nằm bên trong Innioasis Trình cập nhật đang bật [Windows](drivers_vi.html#windows) và [Linux](drivers_vi.html#linux). Bạn đã có nó rồi. Hướng dẫn này chỉ ra cách an toàn để sử dụng nó trên Innioasis Y1 hoặc Y2 và lộ trình Trình cập nhật cho người chơi Timmkoo.[Quay lại hướng dẫn Cập nhật](guide_vi.html)[Tải xuống chương trình cơ sở](firmware_vi.html)[Khắc phục sự cố](troubleshooting_vi.html)

Bắt đầu với Innioasis Updater

## Trình cập nhật thực hiện toàn bộ công việc trong một lần

Trình cập nhật thực hiện hầu hết các lượt cài đặt trong một lần. Chọn phần mềm, làm theo các bước và bạn đã hoàn tất. Nó cũng cho bạn biết khi nào có bản sửa lỗi hoặc bản phát hành mới. SP Flash Tool nằm trong Bộ công cụ của Trình cập nhật dành cho một số trường hợp hiếm hoi Trình cập nhật không thể hoàn tất. Các bước dưới đây là ngoại lệ.

## Công cụ này dùng để làm gì

Trình cập nhật flash trình phát cho bạn. SP Flash Tool là cùng một động cơ, không có thanh chắn bảo vệ. Sử dụng nó khi Trình cập nhật không khởi động, khi trình phát không kết nối hoặc khi bạn biết cách xử lý một tệp phân tán.Hãy thử Trình cập nhật trước. Đối với hầu hết các lượt cài đặt và hầu hết các lần khôi phục, hướng dẫn [Lộ trình cập nhật](guide_vi.html) là sự lựa chọn an toàn hơn. Sử dụng SP Flash Tool khi bạn biết lý do mình cần và chuẩn bị sẵn pin đã sạc cùng với cáp dữ liệu USB.

## Công cụ flash dành cho Innioasis người chơi

Innioasis Trình cập nhật là công cụ flash dành cho người chơi Innioasis. Nó cài đặt phần mềm chính thức, cập nhật và khôi phục các gói thông qua quy trình phù hợp với mô hình, đồng thời lưu giữ nhạc và cài đặt của bạn.

### Innioasis Y1 công cụ flash

Chọn bản phát hành Y1 trong Trình cập nhật, sau đó kết nối trình phát đã tắt nguồn khi ứng dụng yêu cầu. Các gói Y1 tương tự hoạt động với SP Flash Tool khi bạn cần lộ trình thủ công.

### Innioasis Y2 công cụ flash

Chọn bản phát hành được liệt kê cho Y2. Các gói Y2 không thể thay thế được với các gói Y1, vì vậy hãy kiểm tra mô hình trước khi bắt đầu.

## Công cụ flash dành cho Timmkoo người chơi

Timmkoo người chơi sử dụng cùng một quy trình cài đặt Trình cập nhật. Nó đọc trực tiếp các gói ZIP và RAR của Timmkoo, do đó bạn không cần công cụ flash hoặc tệp phân tán riêng.

### Timmkoo Q5 công cụ flash

Chọn mô hình Q5 trong Trình cập nhật, chọn gói Timmkoo, sau đó chạy Cài đặt / Khôi phục và kết nối trình phát tại dấu nhắc.

### Công cụ flash Timmkoo Q3 và Q3E

Mục Q3 bao gồm Q3 và Q3E như nhau. Trình cập nhật chọn các tệp phù hợp từ gói mà dự án xuất bản.

### Timmkoo A5 công cụ flash

Chọn kiểu máy A5 trước khi chọn gói, sau đó làm theo lời nhắc cài đặt tương tự.

## Trình cập nhật đặt nó ở đâu

SP Flash Tool đi kèm với thư mục cài đặt Trình cập nhật, không phải dưới dạng bản tải xuống riêng biệt. Mở nó từ đó khi bạn cần nó.

### Windows

Mở thư mục cài đặt Updater và chạy `flash_tool.exe`. Thư mục này thường ở dưới `%LOCALAPPDATA%\Innioasis Updater`. Thư mục Bộ công cụ có phím tắt SP Flash Tool được bao gồm trong một số thiết lập.

### Linux

Chạy gói `flash_tool` nhị phân bên trong thư mục ứng dụng Trình cập nhật trên x86/x86_64. Trình cài đặt dự án chuẩn bị các quyền USB với các quy tắc udev, do đó trình phát sẽ xuất hiện khi được kết nối.

### macOS

SP Flash Tool không được gói trên macOS. Thay vào đó, trình cập nhật sử dụng tuyến MTKClient ở đó. Sử dụng [hướng dẫn cài đặt](guide_vi.html) trên máy Mac và giữ SP Flash Tool cho máy Windows hoặc Linux.

Công cụ này đi kèm với tác nhân tải xuống MediaTek và cấu hình dành riêng cho từng mô hình, do đó bạn không cần phải thu thập DA hoặc phân tán các tệp từ nơi khác.

## Chuẩn bị phần sụn
  - Lấy bản phát hành bạn muốn từ [Tải xuống chương trình cơ sở](firmware_vi.html). chọn `rom.zip` cho Y1 hoặc `rom_y2.zip` cho Y2.
  - Giải nén ZIP vào thư mục riêng của nó. Windows có thể sử dụng Extract All. Trên Linux, hãy sử dụng trình quản lý lưu trữ của bạn hoặc `unzip` trong một thiết bị đầu cuối.
  - Kiểm tra xem tệp phân tán có trong thư mục được giải nén hay không. Nó thường được đặt tên `MT6572_Android_scatter.txt` cho các gói Y1 và `MT6582_Android_scatter_def.txt` đối với các gói Y2, mặc dù bản phát hành có thể đặt tên nó theo tên dự án của nó.
Giữ các mô hình riêng biệt. Phân tán Y1 mô tả thiết bị MT6572 và phân tán Y2 mô tả thiết bị MT6582. Nhấp nháy sai là cách người chơi bị brick. Nếu phân tán bên trong ZIP không khớp với mô hình của bạn, hãy dừng lại và sử dụng gói được liệt kê cho mô hình của bạn để thay thế.

## Tải phân tán và flash
  - Mở SP Flash Tool từ thư mục cài đặt Trình cập nhật.
  - Trong tab Tải xuống, bấm vào chọn bên cạnh Tệp tải phân tán và chọn tệp phân tán từ thư mục được giải nén. Danh sách phân vùng sẽ điền vào.
  - Để chế độ đèn flash bật Chỉ tải xuống trừ khi bạn đang cố tình khôi phục hoàn toàn, điều này cần Nâng cấp chương trình cơ sở.
  - nhấp chuột Tải xuống. Công cụ sẽ chờ người chơi.
  - Tắt nguồn đầu phát hoàn toàn, sau đó kết nối cáp dữ liệu USB. Đặt máy nghe nhạc xuống và không di chuyển nó.
  - Đợi dấu kiểm màu xanh lá cây. Chỉ sau đó ngắt kết nối cáp và khởi động máy nghe nhạc.

Giữ nguyên các quy tắc về thời gian và cáp USB như lộ trình được hướng dẫn: cáp dữ liệu, không có hub và chỉ kết nối khi công cụ đã sẵn sàng.

## Nếu nó không nhấp nháy
  - Kiểm tra xem phân tán và ZIP có khớp với mô hình được in trên đầu phát hay không.
  - Xác nhận đầu phát đã tắt nguồn hoàn toàn trước khi kết nối.
  - Trên Windows, hãy xác nhận trình điều khiển MediaTek được cài đặt bằng thiết lập Trình cập nhật; trên Linux, hãy xác nhận các quy tắc udev từ trình cài đặt dự án.
  - Chỉ kết nối lại cáp khi công cụ đang chờ. Một cuộc đua cổng có thể cần một phích cắm hoàn toàn và một cái mới Tải xuống bấm vào.

Đối với bất cứ điều gì ngoài điều đó, hãy mở [khắc phục sự cố](troubleshooting_vi.html). Và hãy nhớ: Trình cập nhật vẫn là con đường bình thường và [Y1](guides/restore-original-y1.html) và [Y2](guides/restore-original-y2.html) hướng dẫn khôi phục cũng sử dụng nó.

## Điều này có hữu ích không?

Câu trả lời của bạn giúp cải thiện hướng dẫn này.Vâng, tôi thấy nó hữu íchChưa[Hãy cho chúng tôi biết cách chúng tôi có thể cải thiện](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
