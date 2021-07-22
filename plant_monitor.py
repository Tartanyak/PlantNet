import constants
from comms.queueHandler import get_client, publish_message
from lib.packageJSON import package_temperature, get_now_string, get_hostname
from sensors.readTemperature import get_sensor, read_temperature
import paho.mqtt.client as mqtt
import time

def main():
    print("Getting hostname")
    host_name = get_hostname()
    print("Hostname:" + host_name)
    print("Getting sensor from pin {}".format(constants.air_temp_pin))
    temperature_sensor = get_sensor(constants.air_temp_pin)
    print("Got sensor")
    print("Getting MQTT client with " + constants.clientPublishName + " and brokerAddress " + constants.brokerAddress) 
    client = get_client(constants.clientPublishName, constants.brokerAddress)
        
    print("Got client")

    while True:
        current_temperature = read_temperature(temperature_sensor)
        message_json = package_temperature(current_temperature, 
            get_now_string(constants.now_string_format),
            host_name)
        publish_message(client, message_json, constants.topic_air_temperature)
        time.sleep(10)
        
        


if __name__ == "__main__":
    main()