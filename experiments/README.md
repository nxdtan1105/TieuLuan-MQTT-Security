# Experiments – MQTT không mã hóa

## 1. Mục đích

Thư mục này lưu trữ các nội dung liên quan đến quá trình thực nghiệm của đề tài "Rủi ro khi MQTT không mã hóa".

Mục tiêu của thực nghiệm là quan sát quá trình trao đổi dữ liệu giữa MQTT Publisher, MQTT Broker và MQTT Subscriber khi sử dụng kết nối MQTT không mã hóa.

## 2. Mô hình thực nghiệm

Mô hình thực nghiệm gồm:

- MQTT Publisher: gửi message đến MQTT Broker.
- MQTT Broker: tiếp nhận và phân phối message.
- MQTT Subscriber: đăng ký Topic và nhận message.
- Kết nối MQTT sử dụng TCP port 1883.

## 3. Kịch bản thực nghiệm

Quá trình thực nghiệm được thực hiện theo các bước:

1. Khởi động MQTT Broker.
2. Kết nối Publisher và Subscriber đến Broker.
3. Publisher gửi message thử nghiệm đến Topic.
4. Subscriber nhận message từ Broker.
5. Quan sát lưu lượng mạng trong quá trình truyền dữ liệu.
6. Ghi nhận các thông tin có thể quan sát trên đường truyền.
7. Phân tích và đánh giá rủi ro khi MQTT không sử dụng cơ chế mã hóa.

## 4. Dữ liệu thử nghiệm

Dữ liệu sử dụng trong thực nghiệm là các message mẫu, không chứa thông tin cá nhân hoặc dữ liệu nhạy cảm thực tế.

## 5. Tiêu chí đánh giá

Các tiêu chí đánh giá được xây dựng dựa trên:

- Khả năng kết nối và truyền message.
- Khả năng quan sát lưu lượng MQTT.
- Khả năng quan sát nội dung message.
- Số lượng thông tin có thể quan sát trên đường truyền.
- Mức giảm rủi ro khi áp dụng cơ chế bảo vệ.
