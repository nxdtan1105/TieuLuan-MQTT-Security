import paho.mqtt.client as mqtt

# Hàm này chạy khi kết nối thành công tới Broker
def on_connect(client, userdata, flags, rc):
    print("Đã kết nối với Broker thành công! Mã trạng thái: " + str(rc))
    # Đăng ký nhận dữ liệu từ topic này
    client.subscribe("iot/sensor/temperature")

# Hàm này chạy khi có dữ liệu gửi đến
def on_message(client, userdata, msg):
    print("Bắt được dữ liệu từ topic " + msg.topic + " ---> " + str(msg.payload.decode("utf-8")))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Kết nối tới Broker đang chạy trên chính máy của bạn (localhost) ở port 1883
client.connect("127.0.0.1", 1883, 60)

print("Đang chờ nhận dữ liệu...")
client.loop_forever()
