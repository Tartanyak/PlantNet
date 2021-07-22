import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))



clientSubscribe = mqtt.Client("PlantReader")
clientSubscribe.connect("192.168.178.44") 

clientSubscribe.loop_start()
clientSubscribe.subscribe("MOISTURE")

clientSubscribe.on_message = on_message 

time.sleep(30)
clientSubscribe.loop_stop()