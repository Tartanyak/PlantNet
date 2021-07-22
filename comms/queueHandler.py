import paho.mqtt.client as mqtt
from datetime import datetime
import time

def get_client(clientName, brokerAddress):
    print("Getting client")
    client = mqtt.Client(clientName)
    print("Connecting client")
    client.connect(brokerAddress, port=1883)
    print("Got and connected client")
    return client

def publish_message(client, message, topic):
        now = datetime.now().strftime("%H:%M:%S")
        client.publish(topic, message)
        print("Published to topic " + topic + " at " + now)


