# Tiểu luận Bảo mật IoT

## Đề tài: Rủi ro khi MQTT không mã hóa

### 1. Thông tin đề tài

- **Môn học:** Bảo mật IoT (INT4410)
- **Mã đề tài:** 13
- **Hướng:** B
- **Sinh viên:** Nguyễn Xuân Duy Tấn
- **MSSV:** 231A010141
- **Giảng viên:** Hồ Nhựt Minh
- **Năm học:** 2026

---

## 2. Giới thiệu đề tài

MQTT (Message Queuing Telemetry Transport) là một giao thức truyền thông nhẹ được sử dụng phổ biến trong các hệ thống Internet of Things (IoT).

Đề tài tập trung nghiên cứu các rủi ro bảo mật khi MQTT được triển khai mà không sử dụng cơ chế mã hóa cho kênh truyền.

Nội dung nghiên cứu bao gồm kiến trúc MQTT, mô hình Publish/Subscribe, MQTT Broker, MQTT Client, cơ chế xác thực, mã hóa TLS và các rủi ro liên quan đến việc truyền dữ liệu không được bảo vệ.

---

## 3. Mục tiêu

- Tìm hiểu kiến trúc và nguyên lý hoạt động của MQTT.
- Phân tích rủi ro khi MQTT không sử dụng mã hóa.
- Xây dựng môi trường lab MQTT để thực nghiệm.
- Thực hiện các kịch bản kiểm thử trong môi trường được kiểm soát.
- Đánh giá kết quả và đề xuất biện pháp giảm thiểu rủi ro.

---

## 4. Nội dung thực hiện

### Chương 1

Tổng quan đề tài.

### Chương 2

Cơ sở lý thuyết và tài liệu liên quan.

### Chương 3

Phương pháp và thiết kế hệ thống.

### Chương 4

Triển khai lab và kết quả thực nghiệm.

### Chương 5

Đánh giá và phân tích rủi ro bảo mật.

### Chương 6

Kết luận và hướng phát triển.

---

## 5. Cấu trúc thư mục

- `01-Tai-lieu-tham-khao/` – Tài liệu tham khảo.
- `02-Ly-thuyet/` – Nội dung lý thuyết.
- `03-Lab/` – Các thành phần và cấu hình lab.
- `04-Ket-qua/` – Kết quả thực nghiệm.
- `05-Hinh-anh/` – Hình ảnh minh chứng.
- `06-Bao-cao/` – Báo cáo tiểu luận.

---

## 6. Môi trường dự kiến

Môi trường thực nghiệm sẽ được xây dựng trong phạm vi lab nhằm phục vụ nghiên cứu và kiểm thử an toàn.

Các thành phần dự kiến:

- MQTT Broker
- MQTT Publisher/Client
- MQTT Subscriber/Client
- Công cụ quan sát lưu lượng mạng
- Môi trường máy tính/ảo hóa phục vụ thực nghiệm

---

## 7. Tài liệu tham khảo

Các tài liệu chính thức và nguồn tham khảo sẽ được cập nhật trong quá trình thực hiện đề tài.

- OASIS MQTT Specification
- NIST
- OWASP IoT Security
- Tài liệu chính thức của các công cụ được sử dụng

---

## 8. Lưu ý an toàn

Các thử nghiệm trong repository này chỉ được thực hiện trên môi trường lab do sinh viên kiểm soát hoặc được phép sử dụng.

Không thực hiện kiểm thử trái phép trên hệ thống, thiết bị hoặc mạng của bên thứ ba.
