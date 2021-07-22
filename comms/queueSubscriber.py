import paho.mqtt.client as mqtt
import time
import constants

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))



clientSubscribe = mqtt.Client(constants.clientSubscribeName)
clientSubscribe.connect(constants.brokerAddress) 

clientSubscribe.loop_start()
clientSubscribe.subscribe(constants.topic_air_temperature)

clientSubscribe.on_message = on_message 

time.sleep(30)
clientSubscribe.loop_stop()