import paho.mqtt.client as mqtt
from datetime import datetime
import time

def get_client(clientName, brokerAddress):
    client = mqtt.Client(clientName)
    client.connect(brokerAddress)
    return client

def publish_message(client, message, topic):
        now = datetime.now().strftime("%H:%M:%S")
        client.publish(topic, message)
        print("Published to topic " + topic + " at " + now)


