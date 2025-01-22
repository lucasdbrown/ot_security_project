import paho.mqtt.client as mqtt

broker_address = "localhost"  # Change this if needed
client = mqtt.Client("ActuatorNode")

def on_message(client, userdata, message):
    command = message.payload.decode("utf-8")
    print(f"[Actuator] Received command: {command}")
    
    if command == "TURN_ON":
        print("[Actuator] Activating system!")
    elif command == "TURN_OFF":
        print("[Actuator] Deactivating system!")

client.connect(broker_address, 1883, 60)
client.subscribe("SCADA/Actuator/Control")
client.on_message = on_message

print("[Actuator] Listening for control messages from SCADA-LTS...")
client.loop_forever()
