import paho.mqtt.client as mqtt
from datetime import datetime
import time

brokerAddress = "mqtt.eclipseprojects.io"
clientPublishName = "MoistureTimestamp"
topic = "TIMESTAMP"

clientPublish = mqtt.Client(clientPublishName)
clientPublish.connect(brokerAddress)

while True:
    now = datetime.now().strftime("%H:%M:%S")
    print("Just published " + now + " to topic " + topic + " timestamp")
    clientPublish.publish(topic, now)
    time.sleep(2)