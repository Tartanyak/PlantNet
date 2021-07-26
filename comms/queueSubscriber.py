import paho.mqtt.client as mqtt
import time

def get_client(clientName, brokerAddress):
    client = mqtt.Client(client_id=clientName, clean_session=True)
    client.connect(brokerAddress)
    return client

def start_loop(client, subscription_name, on_message_function, on_connect_function):
    client.loop_start()
    print(subscription_name)
    client.subscribe(subscription_name)
    client.on_message = on_message_function
    client.on_connect = on_connect_function

def stop_loop(client):
    client.loop_stop()


