import paho.mqtt.client as mqtt
import time
import random

broker_address = "localhost"  # Change this to SCADA-LTS IP if needed
client = mqtt.Client("SensorNode")

client.connect(broker_address, 1883, 60)

print("[Sensor] Publishing data to SCADA-LTS MQTT broker...")

while True:
    temp = random.randint(20, 30)  # Generate random temperature data
    client.publish("SCADA/Sensor/Temperature", temp)
    print(f"[Sensor] Sent Temperature: {temp} °C")
    time.sleep(5)  # Send data every 5 seconds
