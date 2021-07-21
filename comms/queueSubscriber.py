import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

brokerAddress = "mqtt.eclipseprojects.io"
clientSubscribeName = "MoistureReader"
topic = "TIMESTAMP"


clientSubscribe = mqtt.Client(clientSubscribeName)
clientSubscribe.connect(brokerAddress) 

clientSubscribe.loop_start()
clientSubscribe.subscribe(topic)

clientSubscribe.on_message = on_message 

time.sleep(30)
clientSubscribe.loop_stop()