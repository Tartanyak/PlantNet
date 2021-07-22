import paho.mqtt.client as mqtt
from datetime import datetime
import time

def get_client(clientName, brokerAddress):
    print("Getting client")
    client = mqtt.Client(clientName)
    print("Connecting client")
    client.connect(brokerAddress)
    print("Got and connected client")
    return client

def publish_message(client, message, topic):
        now = datetime.now().strftime("%H:%M:%S")
        client.publish(topic, message)
        print("Published to topic " + topic + " at " + now)




#brokerAddress = "192.168.178.44"
#clientName = "Moisture"
#clientPublishName = "MoistureTimestamp"
#topic = "AIR_TEMP"
#
#client = mqtt.Client(clientName)
#client.connect(brokerAddress)
#clientPublish = mqtt.Client(clientPublishName)
#clientPublish.connect(brokerAddress)

#while True:
#    now = datetime.now().strftime("%H:%M:%S")
#    print("Just published " + now + " to topic " + "AIR_TEMP" + " timestamp")
#    clientPublish.publish(topic, now)
#    time.sleep(2)