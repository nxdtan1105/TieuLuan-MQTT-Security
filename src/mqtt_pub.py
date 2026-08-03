import paho.mqtt.client as mqtt
import time

# Tạo client và kết nối đến Broker
client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)

# Dữ liệu cần gửi
topic = "iot/sensor/temperature"
payload = "temperature=30°C"

print("Chuẩn bị gửi dữ liệu...")
print(f"Topic: {topic}")
print(f"Payload: {payload}")

# Thực hiện gửi
client.publish(topic, payload)
time.sleep(2) # Dừng 2 giây để đảm bảo tin nhắn đi đến nơi

print("Đã gửi dữ liệu thành công!")
