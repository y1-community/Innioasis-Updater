---
title: "trình điều khiển Innioasis Y1 và Y2 USB | Trình điều khiển Windows và quyền Linux - Innioasis Trình cập nhật"
description: "Thiết lập máy tính của bạn để có Trình cập nhật Innioasis: Quyền của trình điều khiển Windows MediaTek và Linux USB — cùng với các bản sửa lỗi về cáp và thời gian."
language: "vi"
source: "https://innioasis.app/drivers_vi.html"
---

# trình điều khiển Innioasis Y1 và Y2 USB | Trình điều khiển Windows và quyền Linux - Innioasis Trình cập nhật

Cài đặt máy tính

# Chuẩn bị sẵn sàng máy tính trước người chơi.

Hầu hết các sự cố kết nối đều đến từ trình điều khiển, quyền, cáp hoặc thời gian. Windows cần cài đặt trình điều khiển MediaTek. Linux cần có quyền USB phù hợp. Tìm nền tảng của bạn dưới đây.[Tải Updater CE](guide_vi.html#platform)[Khắc phục sự cố](troubleshooting_vi.html)

## Windows
  - Tải xuống trình cài đặt trình điều khiển MediaTek bên dưới.
  - Chạy trình cài đặt và cho phép Windows cài đặt trình điều khiển.
  - Khởi động lại máy tính.
  - Mở Updater CE và đợi lời nhắc kết nối trước khi cắm đầu phát đã tắt nguồn.

Một số hệ thống Windows chặn trình điều khiển thông qua cách ly Core (Tính toàn vẹn của bộ nhớ). Nếu Trình cập nhật CE vẫn không thể thấy trình phát sau khi khởi động lại, hãy tắt tính toàn vẹn của bộ nhớ trong Bảo mật Windows, khởi động lại và cài đặt lại trình điều khiển. Bật lại cài đặt khi bạn hoàn tất nếu hệ thống của bạn cho phép.

Windows sẽ không khởi chạy ứng dụng? Nếu Bảo mật Windows hoặc Kiểm soát ứng dụng thông minh ngăn Trình cập nhật CE mở, hãy mở Cài đặt (nhấn Win + I) → Quyền riêng tư và bảo mật → Windows Security → Kiểm soát ứng dụng và trình duyệt → Cài đặt Kiểm soát ứng dụng thông minh và đặt nó thành Tắt. Kiểm soát ứng dụng thông minh hiện đang tác động đến các ứng dụng phổ biến như Dịch vụ lớp phủ sử thi (được sử dụng bởi Fortnite) - Trình cập nhật CE an toàn và đã được xác minh để sử dụng. Để kích hoạt lại sau, hãy đặt `VerifiedAndReputablePolicyState` để `1` (Bật) hoặc `2` (Chế độ đánh giá) trong `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` trong Trình chỉnh sửa sổ đăng ký.[Tải xuống trình điều khiển Windows](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Quay lại hướng dẫn chính](guide_vi.html#windows) · [Tải xuống phần mềm](firmware_vi.html)

## Quyền của Linux USB

Linux cần tài khoản người dùng của bạn để được phép giao tiếp với chip MediaTek USB bên trong trình phát. Trình cập nhật CE thường sắp xếp vấn đề này trong quá trình cài đặt và quyền tương tự bao gồm SP Flash Tool, vì vậy hãy coi đây là bước khắc phục chứ không phải là giai đoạn bình thường.
  - Chạy Updater CE với tư cách người dùng bình thường, không phải với quyền root. Trình cài đặt chỉ yêu cầu quyền truy cập của quản trị viên khi cần.
  - Kiểm tra xem người chơi có nhìn thấy gì không. Tắt nguồn đầu phát, kết nối cáp và chạy lệnh lsusb trong thiết bị đầu cuối. Trình phát được kết nối hiển thị dưới dạng thiết bị MediaTek có ID nhà cung cấp 0e8d.
`lsusb`
  - Nếu nó xuất hiện trong lsusb nhưng Innioasis Updater CE hoặc SP Flash Tool cho biết quyền bị từ chối hoặc không thể mở cổng, thì người dùng của bạn không có quyền truy cập vào thiết bị USB. Quy tắc udev giống nhau áp dụng cho cả hai công cụ, vì vậy hãy thêm một quy tắc cho phép nhóm người dùng đọc nó.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Lưu dòng đó vào một tệp mới có tên /etc/udev/rules.d/51-innioasis.rules, sau đó chạy:`sudo udevadm control --reload && sudo udevadm trigger`
  - Hãy rút phích cắm hoàn toàn của trình phát, cắm lại và thử cài đặt lại.
  - Nếu SP Flash Tool báo cáo quyền nối tiếp hoặc xung đột cổng, hãy rút phích cắm hoàn toàn và chỉ kết nối lại khi được nhắc.
Đừng ứng biến độ lệch flash.Nếu bạn chuyển sang công cụ khôi phục thủ công, hãy sử dụng các tệp và cấu hình dành riêng cho kiểu máy được cung cấp cùng với dự án.

[Quay lại hướng dẫn chính](guide_vi.html#linux) · [Tải xuống phần mềm](firmware_vi.html) · [SP Flash Tool hướng dẫn](sp-flash-tool_vi.html)

## Cáp và thời gian
  - Sử dụng cáp dữ liệu USB đã biết.
  - Tránh các trung tâm trong khi khắc phục sự cố.
  - Tắt nguồn hoàn toàn đúng mẫu.
  - Chỉ kết nối khi được nhắc.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
