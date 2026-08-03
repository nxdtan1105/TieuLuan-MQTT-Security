# Cơ sở lý thuyết

## 1. MQTT

MQTT (Message Queuing Telemetry Transport) là giao thức truyền thông theo mô hình Publish/Subscribe, được thiết kế cho các thiết bị có tài nguyên hạn chế và môi trường mạng có băng thông thấp hoặc không ổn định.

Trong mô hình MQTT, các thành phần chính gồm Publisher, Subscriber và Broker. Publisher gửi message đến một Topic, Broker tiếp nhận và phân phối message đến các Subscriber đã đăng ký Topic tương ứng.

## 2. Mô hình hoạt động của MQTT

Quá trình trao đổi dữ liệu MQTT được thực hiện thông qua MQTT Broker.

- **Publisher:** gửi dữ liệu đến một Topic.
- **Subscriber:** đăng ký Topic và nhận dữ liệu.
- **Broker:** tiếp nhận message từ Publisher và chuyển tiếp đến Subscriber.
- **Topic:** xác định kênh hoặc chủ đề mà message được gửi đến.

Mô hình này giúp các thiết bị không cần kết nối trực tiếp với nhau mà thông qua Broker để trao đổi dữ liệu.

## 3. MQTT và kết nối TCP

MQTT thường được triển khai trên giao thức TCP nhằm bảo đảm việc truyền dữ liệu giữa Client và Broker. Trong trường hợp MQTT sử dụng kết nối không mã hóa, dữ liệu được truyền qua TCP mà không có lớp mã hóa bảo vệ nội dung.

MQTT sử dụng TCP port 1883 cho kết nối MQTT thông thường không sử dụng TLS. Khi sử dụng TLS, MQTT thường được triển khai trên port 8883.

## 4. MQTT không mã hóa

Khi MQTT được triển khai trên kết nối TCP thông thường mà không sử dụng cơ chế mã hóa, dữ liệu trao đổi giữa Client và Broker có nguy cơ bị quan sát trên đường truyền.

Rủi ro này đặc biệt liên quan đến tính bí mật của message. Nếu nội dung dữ liệu có thể được quan sát từ lưu lượng mạng, thông tin được truyền giữa các thành phần MQTT có thể bị lộ.

## 5. Rủi ro bảo mật

Một số rủi ro có thể phát sinh khi MQTT không được bảo vệ bằng cơ chế mã hóa kênh truyền gồm:

- Lộ nội dung message.
- Lộ thông tin Topic.
- Lộ thông tin liên quan đến quá trình kết nối.
- Nguy cơ ảnh hưởng đến tính bí mật của dữ liệu.
- Tăng khả năng bị theo dõi lưu lượng truyền thông.

Mức độ ảnh hưởng phụ thuộc vào loại dữ liệu được truyền và cách hệ thống MQTT được triển khai.

## 6. Bảo vệ kết nối MQTT

Một trong những hướng bảo vệ MQTT là sử dụng TLS để mã hóa kênh truyền giữa Client và Broker. Việc mã hóa giúp hạn chế khả năng quan sát trực tiếp nội dung dữ liệu khi dữ liệu được truyền trên mạng.

Ngoài mã hóa kênh truyền, hệ thống MQTT có thể kết hợp các cơ chế xác thực và kiểm soát quyền truy cập để tăng mức độ an toàn.

## 7. Phạm vi áp dụng trong đề tài

Phần cơ sở lý thuyết này được sử dụng làm nền tảng cho việc xây dựng môi trường thực nghiệm và đánh giá rủi ro khi MQTT không mã hóa.

Đề tài tập trung vào việc quan sát quá trình truyền dữ liệu MQTT trên TCP port 1883 và đánh giá khả năng lộ thông tin trên đường truyền.
