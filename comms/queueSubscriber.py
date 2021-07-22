import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: "+mqtt.connack_string(rc))

def get_client(clientName, brokerAddress):
    client = mqtt.Client(clientName)
    client.connect(brokerAddress) 

def start_loop(client, subscription_name, on_message_function=on_message, on_connect_function=on_connect):
    client.loop_start()
    client.subscribe(subscription_name)
    client.on_message = on_message_function 
    client.on_connect = on_connect_function

def stop_loop(client):
    client.loop_stop()


