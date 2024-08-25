import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTMessage
import json
from datetime import datetime
import time
from typing import Any, Dict

# MQTT broker details
broker_address = ""  # Replace with your Synology NAS IP
port = 1883
username = ""  # Replace with your MQTT username
password = ""  # Replace with your MQTT password

# Log file path
log_file_path = "mqtt_messages.jsonl"


# Callback function when connection is established
def on_connect(
    _client: mqtt.Client, _userdata: Any, _flags: Dict[str, int], rc: int
) -> None:
    if rc == 0:
        print("Connected to MQTT broker")
        # Subscribe to all topics
        _client.subscribe("#")
    else:
        print(f"Connection failed with code {rc}")


# Callback function when a message is received
def on_message(_client: mqtt.Client, _userdata: Any, msg: MQTTMessage) -> None:
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "topic": msg.topic,
        "payload": msg.payload.decode(),
    }
    print(f"Received: {log_entry}")

    # Append the log entry to the JSON Lines file
    with open(log_file_path, "a") as log_file:
        json.dump(log_entry, log_file)
        log_file.write("\n")


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
    print(f"Logging MQTT messages to {log_file_path}")
    print("Press CTRL+C to stop...")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...")
    client.loop_stop()
    client.disconnect()
