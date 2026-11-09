---
title: "Nhà phát triển | Thêm chương trình cơ sở tùy chỉnh vào Innioasis Trình cập nhật CE - Innioasis Tải xuống chương trình cơ sở"
description: "Tài liệu dành cho nhà phát triển về cách thêm chương trình cơ sở Innioasis Y1 hoặc Y2 tùy chỉnh vào Trình cập nhật CE: phân nhánh kho lưu trữ, xuất bản nội dung rom.zip, chỉnh sửa slideia_manifest.xml, kiểm tra và mở yêu cầu kéo."
language: "vi"
source: "https://innioasis.app/developers_vi.html"
---

# Nhà phát triển | Thêm chương trình cơ sở tùy chỉnh vào Innioasis Trình cập nhật CE - Innioasis Tải xuống chương trình cơ sở

Dành cho nhà phát triển phần mềm cơ sở

# Thêm chương trình cơ sở của bạn vào Updater CE.

Updater CE là danh mục cộng đồng và trình cài đặt cho chương trình cơ sở tùy chỉnh. Phát triển dự án của bạn từ cơ sở ROM, xuất bản nó dưới dạng kho lưu trữ công cộng với nội dung phát hành chính xác, thêm các mục mô hình vào `slidia_manifest.xml`, kiểm tra bộ lọc mô hình và mở yêu cầu kéo. Một kho lưu trữ có thể phục vụ mọi mô hình mà nó hỗ trợ.[Xem nguồn CE của Trình cập nhật](https://github.com/y1-community/Innioasis-Updater)[Duyệt tải xuống phần mềm](firmware_vi.html)

## Bắt đầu từ cơ sở ROM

ROM cơ sở cung cấp cho các nhà phát triển chương trình cơ sở tùy chỉnh một nền tảng Android sạch có bật chip vô tuyến không dây. Trên Y1, họ kích hoạt Wi-Fi và GPS cùng với Bluetooth và FM của nhà máy; trên Y2 họ kích hoạt Wi-Fi, GPS và FM cùng với Bluetooth của nhà máy.Bản tải xuống cơ sở ROM để phát triển chương trình cơ sở tùy chỉnh, với phiên bản Android và các tính năng không dây mà mỗi phiên bản đều kích hoạt[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom.zip)[``](https://github.com/y1-community/y1-ata-rom/releases/download/0.1/rom_type_b.zip)[``](https://github.com/y1-community/y2-ata-rom/releases/download/y2-ata/rom_y2.zip)

| Tải xuống | Thiết bị | Android | Tính năng không dây |
| --- | --- | --- | --- |
| rom.zip | Y1 · Type A | Android 4.2.2 | Thêm Wi-Fi và GPS vào Bluetooth và FM của nhà máy (FM đã hoạt động trên Y1 từ nhà máy). Dành cho Y1 người chơi cài đặt OS 2.0.0 trở lên. |
| rom_type_b.zip | Y1 · Type B | Android 4.2.2 | Thêm Wi-Fi và GPS vào Bluetooth và FM của nhà máy (FM đã hoạt động trên Y1 từ nhà máy). Dành cho Y1 người chơi cài đặt hệ điều hành cũ hơn 2.0.0. |
| rom_y2.zip | Y2 | Android 4.4.2 | Thêm Wi-Fi, GPS và FM vào Bluetooth gốc. Chip vô tuyến Y2 được kích hoạt hoàn toàn nên FM cũng có sẵn ở đây. |

Những hình ảnh này là nền tảng Android gốc (AOSP) đã bật sóng không dây của thiết bị, vì vậy chương trình cơ sở tùy chỉnh có thể thêm các tính năng mạng thay vì thay thế ngăn xếp sóng. Chúng là điểm khởi đầu thực tế cho các bước xuất bản dưới đây.

## Sử dụng các tên nội dung phát hành này

Tên tập tin là một phần của tín hiệu tương thích. Giữ tên chính xác và đặt các tệp ZIP vào nội dung phát hành của dự án, không chỉ trong cây nguồn kho lưu trữ.Tên nội dung ZIP của chương trình cơ sở và các thiết bị được hỗ trợ``````

| Tài sản | Thiết bị | Phần cứng | Ý nghĩa |
| --- | --- | --- | --- |
| rom.zip | Y1 | Type A | Y1 thiết bị đi kèm với OS 2.0.0 trở lên. |
| rom_type_b.zip | Y1 | Type B | Y1 thiết bị đi kèm hệ điều hành cũ hơn 2.0.0. |
| rom_y2.zip | Y2 | Y2 | Gói cài đặt đầy đủ Y2. Giữ nó tách biệt với nội dung Y1. |
Không đổi tên gói để phù hợp với mô hình khác. Y1 và Y2 sử dụng các tệp nền tảng MediaTek khác nhau và cấu hình flash. Xuất bản gói cho phần cứng mà nó thực sự hỗ trợ.

## Cách kết nối hoạt động

Trình cập nhật CE đọc bảng kê khai dưới dạng danh mục của nó. Mỗi `<package>` dòng cho nó biết tên dự án, kho lưu trữ, mô hình và trình xử lý. Khi người dùng chọn dự án đó, Trình cập nhật sẽ kiểm tra các bản phát hành đã xuất bản của kho lưu trữ và tìm kiếm `rom*.zip` tài sản.

### Bản kê khai

Đặt tên cho dự án và ánh xạ nó tới một mô hình. Y1 và Y2 cần các dòng riêng biệt, ngay cả khi chúng chia sẻ kho lưu trữ.

### Bản phát hành đã xuất bản

Chứa nội dung ZIP có thể cài đặt. Một bản phát hành có thể chứa các gói Y1 Type A, Y1 Type B và Y2 cùng nhau.

### Cài đặt bản cập nhật CE

Sử dụng mô hình đã chọn để chọn gói phù hợp và đường dẫn nhấp nháy dành riêng cho mô hình. Người dùng không cần phải đoán tên tệp.

## Xuất bản một dự án trong năm bước
  - Phân nhánh kho lưu trữ Updater CE. Tạo nhánh của riêng bạn [y1-community/Innioasis-Updater](https://github.com/y1-community/Innioasis-Updater), sau đó sao chép ngã ba của bạn cục bộ.
  - Chuẩn bị một kho lưu trữ phần mềm công cộng. Đảm bảo kho lưu trữ ở chế độ công khai và bản phát hành của nó chứa đúng nội dung ZIP. Bạn có thể đặt `rom.zip`, `rom_type_b.zip`và `rom_y2.zip` trên cùng một bản phát hành khi chúng thuộc cùng một phiên bản.
  - Chỉnh sửa bảng kê khai. Mở `slidia_manifest.xml` trong thư mục gốc của nhánh Updater CE của bạn. Thêm một dòng cho mỗi kiểu máy mà bản phát hành hỗ trợ (Y1 và Y2 là cặp chung). các `repo` giá trị là của kho lưu trữ `owner/repository`; `url` là trang dự án công cộng.
  - Kiểm tra danh mục. Chạy Trình cập nhật từ thanh toán đã chỉnh sửa. Chọn Y1 và xác nhận dự án hiển thị nội dung Y1. Chọn Y2 và xác nhận nó hiển thị bản phát hành Y2. Kiểm tra riêng Type A và Type B khi cả hai đều được xuất bản.
  - Mở một yêu cầu kéo. Đẩy thay đổi tệp kê khai tới nhánh của bạn và mở yêu cầu kéo đối với kho lưu trữ CE của Trình cập nhật ngược dòng. Bao gồm liên kết dự án, kiểu máy được hỗ trợ, thẻ phát hành, tên nội dung và thiết bị bạn đã thử nghiệm.

## Tạo dòng kê khai của bạn

Điền vào kho lưu trữ và đánh dấu vào mọi mô hình mà bản phát hành hỗ trợ. Trình tạo ghi một `<package>` dòng trên mỗi mô hình và chỉ bao gồm các thuộc tính bạn đặt, do đó kết quả khớp với hiện tại `slidia_manifest.xml` định dạng. Mọi thuộc tính mà Trình cập nhật CE đọc đều có sẵn bên dưới - các thuộc tính tùy chọn nằm bên dưới Nhiều lựa chọn hơn.URL kho lưu trữKho lưu trữ GitHub công khai. Máy phát điện chiết xuất `owner/repository` từ URL.Tên phần mềmHiển thị trong ứng dụng và danh mục trang web.URL dự ánTrang hướng tới con người dành cho dự án hoặc ghi chú phát hành của dự án.Thương hiệuXóa mục này để sử dụng nhãn hiệu mặc định của mô hình. SR1, Q3, Q5 và Q3e là các mẫu Timmkoo.Thiết bị (mỗi dòng một dòng)Y1Y2A5G1G3G5R1PR1SR1Q3Q5Q3eCác mô hình khácĐối với một mô hình không được liệt kê ở trên. Các mô hình đã biết giữ nguyên chính tả danh mục của họ.Cờ`do_not_keep_data` - không bao giờ cung cấp Keep Data cho phần sụn nàyĐược xây dựng từ phần mềm gốc - bổ sung `derivative="y1-community/y1-stock-rom"`

Keep Data chỉ được cung cấp khi chương trình cơ sở đến và chương trình cơ sở đã cài đặt giống nhau hoặc dùng chung một `derivative` gốc. Chỉ sử dụng cờ khi dữ liệu người dùng thực sự không thể được chuyển sang.Tùy chọn khác: biểu tượng, tác phẩm nghệ thuật, nội dung phát hành, cài đặt sau và phản chiếu

#### Biểu tượng và tác phẩm nghệ thuậtTệp biểu tượngChọn hình ảnh bạn sẽ cam kết với kho lưu trữ. Điều này xem trước nó và xây dựng URL thô của nó; nó không tải lên bất cứ điều gì.Đường dẫn biểu tượng trong kho lưu trữĐường dẫn đến hình ảnh đã cam kết, liên quan đến thư mục gốc của kho lưu trữ.nhánh biểu tượngURL biểu tượngURL hình ảnh trực tiếp. Khi trống, ứng dụng sẽ sử dụng bản phát hành `updater.png` hoặc một biểu tượng được tạo.Xem trước biểu tượng đã chọn

URL biểu tượng chế độ tốiBiểu tượng chủ đề tối tùy chọn. `image_dark` là bí danh được chấp nhận.URL tác phẩm nghệ thuật nhẹ nhàngTác phẩm nghệ thuật thứ cấp, đã thử sau khi phát hành hình ảnh và `icon`.URL tác phẩm nghệ thuật tối

#### Phát hành tài sảnPhát hành tên tài sảnMột tên cho mỗi mô hình được chọn. Để trống để sử dụng `rom.zip` trên Y1 và `rom_<model>.zip` ở nơi khác.Mẫu nội dungGlob được sử dụng khi các zip của bản phát hành không được đặt tên `rom*.zip`.Type A nội dungGlob cho gói Y1 Type A khi tên của nó không nói như vậy.Type B nội dungGlob cho gói Y1 Type B khi tên của nó không nói như vậy.Phiên bản ứng dụng tối thiểuẨn mục nhập khỏi các bản dựng Updater CE cũ hơn.

#### Liên kết, nhân bản và nhóm Keep DataTrang sau cài đặtĐã mở sau khi cài đặt thành công.Trang sau cài đặt thứ haiBước thứ hai tùy chọn để có hướng dẫn thiết lập nhiều trang.Gương zip di độngĐược phân tách bằng dấu phẩy `*-mirror` kho lưu trữ xây dựng các gói Zip nhấp nháy di động.Kho phái sinhPhần sụn mà bản phát hành này được xây dựng từ đó. Các chương trình cơ sở liên quan chia sẻ một phân vùng dữ liệu, đây là điều mà Keep Data sẽ kiểm tra.Kho thông tinKho ứng dụng có bản phát hành mô tả các ứng dụng trong chương trình cơ sở này. Nó cũng cần một trang cài đặt sau.kho lưu trữ APKKho ứng dụng có APK ứng dụng tải xuống và cài đặt sau chương trình cơ sở.

#### Danh mục bổ sungsênGiá trị nhận dạng ổn định cho các liên kết và bản ghi cài đặt đã lưu. Mô hình được tự động thêm vào khi một số mô hình được chọn.Mô tả`<package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y1" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" /> <package name="Your Firmware" brand="Innioasis" repo="your-account/your-firmware" device="Y2" url="https://github.com/your-account/your-firmware" type="img" handler="Custom Firmware" />`Sao chép dòng

Đang tải bản kê khai mới nhất…Xem trước tệp kê khai mới nhất có dòng của bạn được thêm vào

Máy phát điện đã lấy dòng điện `slidia_manifest.xml` từ kho lưu trữ này và chèn các dòng đã tạo của bạn ngay trước đó `</slidia>`.

Một dòng là không đủ cho một kho lưu trữ được chia sẻ. Nếu thiếu dòng Y2, người dùng Y2 sẽ không nhận được mục nhập khớp với mô hình ngay cả khi `rom_y2.zip` tồn tại trong bản phát hành của dự án. Điều này cũng đúng với mọi mô hình khác mà bản phát hành của bạn hỗ trợ.

### Mọi thuộc tính mà bảng kê khai đọc

Đây là những thuộc tính mà các bản dựng Updater CE hiện tại hiểu được. Trình tạo chỉ ghi những cái bạn điền vào; ứng dụng sẽ quay trở lại các giá trị mặc định hợp lý cho phần còn lại.Các thuộc tính của gói slideia_manifest.xml và ý nghĩa của chúng``````````````````````````````````````````````````````````````````````````````````````````````

| Thuộc tính | Cần thiết | Nó làm gì |
| --- | --- | --- |
| name | Có | Tên phần mềm hiển thị trong danh mục và trên thẻ cài đặt. |
| repo | Có | owner/repo. Ứng dụng đọc các bản phát hành GitHub của kho lưu trữ đó. |
| device | Có | Mô hình mục tiêu, chữ hoa (Y1, Y2, G1, Q3e,…). Giữ một mục cho mỗi mô hình. |
| url | Được đề xuất | Trang dự án hoặc ghi chú phát hành được mở từ danh mục. |
| type, handler | Có trong thực tế | type="img" và handler="Custom Firmware". Các loại khác và trình xử lý không phải phần sụn bị bỏ qua. |
| brand | Tùy chọn | Danh mục thương hiệu (Innioasis, Timmkoo). Empty sử dụng nhãn hiệu mặc định của mô hình. |
| package_name | Tùy chọn | Phát hành tên tệp tài sản. Mặc định là rom.zip trên Y1 và rom_<model>.zip trên các mô hình khác. |
| asset_pattern | Tùy chọn | Toàn cầu không phân biệt chữ hoa chữ thường đối với các bản phát hành có khóa phần sụn không được đặt tên rom*.zip (ví dụ my-firmware-*.zip). |
| type_a_asset, type_b_asset | Tùy chọn | Quả cầu xác định các khóa kéo Y1 Type A và Type B khi tên tệp của chúng không chứa các dấu hiệu thông thường. |
| icon | Tùy chọn | URL biểu tượng. Được sử dụng sau khi phát hành riêng updater.png / updater.jpgvà làm dự phòng cho mỗi bản phát hành. |
| icon_dark | Tùy chọn | Logo chủ đề tối. image_dark là bí danh được chấp nhận. |
| image | Tùy chọn | Tác phẩm nghệ thuật ánh sáng phụ, đã thử sau icon. |
| post_install, post_install2 | Tùy chọn | (Các) trang được mở sau khi cài đặt thành công. Phần thứ hai bao gồm một hướng dẫn gồm nhiều bước. |
| portable_zips | Tùy chọn | Được phân tách bằng dấu phẩy *-mirror repos xuất bản các gói di động sẵn sàng để chạy. |
| derivative | Tùy chọn | Kho lưu trữ phần sụn được xây dựng từ đó. Firmware có cùng gốc phái sinh có thể lưu giữ dữ liệu người dùng. |
| info_repo | Tùy chọn | Kho ứng dụng có bản phát hành mô tả những gì chương trình cơ sở triển khai. Yêu cầu post_install hoặc post_install2. |
| apk_repo | Tùy chọn | Kho ứng dụng có APK ứng dụng cài đặt sau chương trình cơ sở. |
| min_version | Tùy chọn | Ẩn mục nhập khi Updater CE cũ hơn phiên bản này. |
| do_not_keep_data | Tùy chọn | true (cũng 1 / yes) chặn hoàn toàn Keep Data cho phần sụn này. |
| slug | Tùy chọn | Giá trị nhận dạng ổn định cho các liên kết và bản ghi cài đặt đã lưu. Được tạo từ tên và kiểu máy khi trống. |
| description | Tùy chọn | Mô tả danh mục ngắn gọn. Nó có thể là giá trị thuộc tính hoặc văn bản của phần tử. |

Tên kế thừa vẫn được đọc để tương thích: `model`, `package`, `portable_zip`, `post_install_2`, `min_app_version` và `image_dark`. Các mục mới nên sử dụng tên hiện tại ở trên.

### Gửi các dòng dưới dạng yêu cầu kéo
  - Sao chép các dòng được tạo ở trên. Chúng đã khớp với định dạng tệp kê khai mới nhất.
  - Chỉnh sửa `slidia_manifest.xml` trong kho lưu trữ. Sử dụng liên kết chỉnh sửa bên dưới; máy chủ lưu trữ tự động tạo một nhánh và một nhánh cho bạn.
  - Dán các dòng ngay trước `</slidia>`, giữ nguyên các mục hiện có không thay đổi.
  - Cam kết chi nhánh mới (ví dụ `add-your-firmware`), sau đó mở yêu cầu kéo đối với kho lưu trữ của Trình cập nhật CE.
  - Trong PR, bao gồm liên kết dự án, kiểu máy được hỗ trợ, thẻ phát hành, tên nội dung và thiết bị bạn đã thử nghiệm.
[Chỉnh sửa bảng kê khai CE của Trình cập nhật](https://github.com/y1-community/Innioasis-Updater/edit/main/slidia_manifest.xml)[Xem bản kê khai mới nhất](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)

Giữ tên mô hình viết hoa, sử dụng URL chính xác của kho lưu trữ công cộng của bạn và giữ `type="img"` và `handler="Custom Firmware"` để nhập phần mềm cơ sở.

## Làm cho bản phát hành dễ dàng được xác minh

Cung cấp cho bản phát hành một thẻ rõ ràng và ghi chú phát hành. Thẻ này hữu ích với mọi người nhưng tên tài sản ZIP là tên mà Trình cập nhật CE sử dụng để xác định các gói cài đặt.

### Danh sách kiểm tra phát hành
  - Xuất bản bản phát hành một cách công khai.
  - Đính kèm tệp ZIP dưới dạng nội dung phát hành.
  - Nêu rõ model được hỗ trợ và Type A hoặc Type B trong ghi chú.
  - Liệt kê mọi sự chuẩn bị cần thiết hoặc những giới hạn đã biết.

### Một bản phát hành, ba nội dung

Một bản phát hành chia sẻ có thể chứa `rom.zip`, `rom_type_b.zip`và `rom_y2.zip`. Trình cập nhật phân loại chúng một cách riêng biệt và chọn từ các bộ lọc mô hình và phần cứng.

### Đừng gộp các dự đoán

Không bao gồm gói Y1 dưới tên tệp Y2 hoặc thêm dữ liệu phân tán, trình tải trước hoặc phân vùng chưa được kiểm tra chỉ để làm cho nội dung xuất hiện.

## Tại sao các mục mô hình lại quan trọng trong quá trình nhấp nháy

Tệp kê khai không chỉ là một menu tải xuống. Sau khi trích xuất, Updater CE sử dụng mô hình đã giải quyết để chuẩn bị đường dẫn cài đặt phù hợp. Y1 và Y2 có các tệp nền tảng, trình tải trước, cấu hình phân tán và bố cục thiết bị khác nhau.
  - Y1: trình cập nhật chuẩn bị đường dẫn Y1 và sử dụng các phân vùng được đặt tên của thiết bị khi MTKClient được sử dụng.
  - Y2: trình cập nhật chuẩn bị đường dẫn Y2 và sử dụng cấu hình Y2 MT6582. Khôi phục hoàn toàn có thể sử dụng địa chỉ vật lý từ dữ liệu phân tán phù hợp với mô hình.
  - Hỗ trợ đa nền tảng: Trình cập nhật CE xử lý quá trình flash gốc trực tiếp trên Windows, Linux và macOS (hỗ trợ cả máy Mac Intel và Apple Silicon) mà không cần thêm công cụ flash.
Những người đóng góp nên cung cấp các tập tin chương trình cơ sở chính xác, không phải các bản flash flash. Không chỉnh sửa địa chỉ phân tán, trình tải trước, tệp DA hoặc lệnh phân vùng để xử lý gói xấu. Sửa nội dung phát hành và thử nghiệm trên mô hình dự định.

## Trước khi bạn yêu cầu hợp nhất
  - Xác thực XML bằng trình phân tích cú pháp XML. Thiếu trích dẫn hoặc kết thúc `/>` có thể ẩn mọi mục sau nó.
  - Khởi chạy trình cập nhật từ quá trình thanh toán của bạn để nó tải tệp kê khai cục bộ trước khi làm mới từ xa.
  - Kiểm tra Y1 và Y2 một cách độc lập. Xác nhận rằng dự án chỉ xuất hiện ở nơi gói của nó được hỗ trợ.
  - Kiểm tra danh sách phát hành cho `rom.zip`, `rom_type_b.zip`và `rom_y2.zip` như có thể áp dụng.
  - Kiểm tra quá trình cài đặt thực tế trên thiết bị dự định bằng cáp dữ liệu USB đáng tin cậy và kế hoạch khôi phục để quay lại Phần mềm gốc.
  - Trong yêu cầu kéo, hãy giải thích những gì bạn đã thử nghiệm. Không mô tả một mô hình chưa được kiểm tra là được hỗ trợ.
`python -c "from xml.etree import ElementTree as ET; ET.parse('slidia_manifest.xml'); print('manifest ok')"`

Để kiểm tra cục bộ, hãy chạy lệnh đó từ thư mục gốc của kho lưu trữ. Nó chỉ xác minh cú pháp XML; nó không chứng minh rằng bản phát hành có chứa chương trình cơ sở hợp lệ hoặc thiết bị an toàn để flash.

## Liên kết dự án hữu ích[Trình cập nhật ngã ba CE](https://github.com/y1-community/Innioasis-Updater/fork)[Xem bảng kê khai](https://github.com/y1-community/Innioasis-Updater/blob/main/slidia_manifest.xml)[Ghi chú đóng góp của cộng đồng](support_devs_vi.html)[Khắc phục sự cố](troubleshooting_vi.html)

## Kỹ năng sửa đổi cho các tác nhân AI

Kho lưu trữ `skills/` thư mục là cơ sở kiến ​​thức dựa trên nguồn dành cho các tác nhân làm việc trên phần cứng, chương trình cơ sở, chủ đề và ứng dụng Y1 và Y2. Mỗi kỹ năng đặt tên cho các tệp dự án mà các tuyên bố của nó xuất phát từ đó, vì vậy nhân viên có thể kiểm tra thông tin thực tế trước khi thay đổi thiết bị.Bắt đầu ở đây

### [Chỉ số kỹ năng và quy tắc an toàn](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/README.md)

Cách tải một kỹ năng, thực tế áp dụng cho mô hình nào và các phân vùng mà không gói nào nên ghi.Phần cứng

### [Y1 phần cứng](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y1-hardware/SKILL.md)

MT6572, bánh xe là sự kiện quan trọng, màn hình 480x360, đường dẫn FM/âm thanh, bộ lưu trữ và bản đồ phân vùng Type A/B.Phần cứng

### [Y2 phần cứng](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/y2-hardware/SKILL.md)

Bảng MT6582, cây thiết bị, bảng GC9503V/ST7701S, đường ray PMIC/DAC, phân vùng và hình ảnh khởi động.Phần sụn

### [Gói phần mềm](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/firmware-packages/SKILL.md)

rom.zip giải phẫu, tệp phân tán, hợp đồng cập nhật Loại A và danh sách kiểm tra phát hành.Chủ đề

### [Sáng tác chủ đề và giao diện](https://github.com/y1-community/Innioasis-Updater/blob/main/skills/theme-authoring/SKILL.md)

Y1 chủ đề config.json, Rockbox WPS/SBS, Reborn giao diện và định dạng giao diện Y2Player v2.Tất cả các kỹ năng

### [Duyệt thư mục kỹ năng](https://github.com/y1-community/Innioasis-Updater/tree/main/skills)

Rockbox Y1/Y2, ROM Android gốc, Y2Linux, ứng dụng Android, trình khởi chạy, ghi chú phát hành và xuất bản trang web.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
