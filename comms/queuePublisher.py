import paho.mqtt.client as mqtt
import time

brokerAddress = "mqtt.eclipseprojects.io"
clientName = "Moisture"

client = mqtt.Client(clientName)
client.connect(brokerAddress)

