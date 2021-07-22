import constants
from comms.queueHandler import get_client, publish_message
from lib.packageJSON import package_value, get_now_string, get_hostname
from sensors.readTemperature import get_sensor, read_temperature as temp 
from sensors.readMoisture import get_sensor, read_moisture as moist
import paho.mqtt.client as mqtt
import time

def main():
    print("Getting hostname")
    host_name = get_hostname()
    print("Hostname:" + host_name)
    print("Getting sensor from pin {}".format(constants.air_temp_pin))
    if(constants.read_temperature):
        temperature_sensor = temp.get_sensor(constants.air_temp_pin)
    if(constants.read_moisture):
        moisture_sensor = moist.get_sensor(constants.moisture_pin, constants.moisture_dry_voltage, constants.moisture_wet_voltage)
    print("Got sensor")
    print("Getting MQTT client with " + constants.clientPublishName + " and brokerAddress " + constants.brokerAddress) 
    client = get_client(constants.clientPublishName, constants.brokerAddress)
        
    print("Got client")

    while True:
        if(constants.read_temperature):
            current_temperature = temp.read_temperature(temperature_sensor)
            message_json = package_value(constants.temperature_label,
                current_temperature, 
                get_now_string(constants.now_string_format),
                host_name)
            publish_message(client, message_json, constants.topic_air_temperature)
        if(constants.read_moisture):
            current_moisture = moist.read_moisture(moisture_sensor)
            message_json = package_value(constants.moisture_label,
                current_moisture, 
                get_now_string(constants.now_string_format),
                host_name)
            publish_message(client, message_json, constants.topic_moisture)

        time.sleep(constants.read_sensor_interval)
        
        


if __name__ == "__main__":
    main()