# Tiểu luận cuối kỳ – Rủi ro khi MQTT không mã hóa

## 1. Thông tin đề tài

**Tên đề tài:** Rủi ro khi MQTT không mã hóa

**Sinh viên:** Nguyễn Xuân Duy Tấn

**Môn học:** Bảo mật trong IoT

## 2. Giới thiệu

MQTT (Message Queuing Telemetry Transport) là một giao thức truyền thông phổ biến trong các hệ thống Internet of Things (IoT), sử dụng mô hình Publish/Subscribe để trao đổi dữ liệu giữa các thiết bị thông qua MQTT Broker.

Tuy nhiên, khi MQTT được triển khai trên kết nối không mã hóa, dữ liệu truyền giữa Client và Broker có thể đối mặt với nguy cơ bị quan sát trên đường truyền.

Đề tài tập trung nghiên cứu và đánh giá các rủi ro phát sinh khi MQTT không sử dụng cơ chế mã hóa cho kênh truyền.

## 3. Mục tiêu

- Tìm hiểu kiến trúc và nguyên lý hoạt động của MQTT.
- Tìm hiểu các thành phần Publisher, Subscriber và Broker.
- Phân tích rủi ro khi MQTT truyền dữ liệu không mã hóa.
- Xây dựng môi trường thực nghiệm MQTT.
- Quan sát quá trình truyền dữ liệu trên kết nối MQTT không mã hóa.
- Đánh giá mức độ ảnh hưởng đối với tính bí mật của dữ liệu.
- Tìm hiểu các biện pháp có thể sử dụng để giảm thiểu rủi ro.

## 4. Mô hình thực nghiệm

Mô hình thực nghiệm được xây dựng theo kiến trúc:

```text
MQTT Publisher
      |
      | Publish
      v
MQTT Broker
      |
      | Subscribe
      v
MQTT Subscriber
