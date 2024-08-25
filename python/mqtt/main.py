import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTMessage
import time
from typing import Any, Dict

# MQTT broker details
broker_address = ""  # Replace with your Synology NAS IP
port = 1883
username = ""  # Replace with your MQTT username
password = ""  # Replace with your MQTT password


# Callback function when connection is established
def on_connect(
    _client: mqtt.Client, _userdata: Any, _flags: Dict[str, int], rc: int
) -> None:
    if rc == 0:
        print("Connected to MQTT broker")
        # Subscribe to a topic
        _client.subscribe("test/topic")
    else:
        print(f"Connection failed with code {rc}")


# Callback function when a message is received
def on_message(_client: mqtt.Client, _userdata: Any, msg: MQTTMessage) -> None:
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")


# Create MQTT client instance
client = mqtt.Client()

# Set username and password
client.username_pw_set(username, password)

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
try:
    client.connect(broker_address, port, 60)
except Exception as e:
    print(f"Connection failed: {e}")
    exit(1)

# Start the loop
client.loop_start()

# Main program loop
try:
    while True:
        # Publish a message every 5 seconds
        client.publish("test/topic", "Hello, MQTT!")
        time.sleep(5)
except KeyboardInterrupt:
    print("Stopping...")
    client.loop_stop()
    client.disconnect()
