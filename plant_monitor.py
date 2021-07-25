import constants
import comms.queueHandler 
import lib.packageJSON 
import sensors.readTemperature 
import sensors.readMoisture
import sensors.readLight
#import paho.mqtt.client as mqtt
import time

def record_temperature(client, temperature_sensor, host_name):
    current_temperature = sensors.readTemperature.read_temperature(temperature_sensor)
    message_json = lib.packageJSON.package_value(constants.temperature_label,
        current_temperature, 
        lib.packageJSON.get_now_string(constants.now_string_format),
        host_name)
    comms.queueHandler.publish_message(client, message_json, constants.topic_air_temperature)

def record_moisture(client, moisture_sensor, host_name):
    current_moisture = sensors.readMoisture.read_moisture(moisture_sensor)
    current_moisture_voltage = sensors.readMoisture.read_voltage(moisture_sensor)

    message_json = lib.packageJSON.package_value(constants.moisture_label,
        current_moisture, 
        lib.packageJSON.get_now_string(constants.now_string_format),
        host_name)
    comms.queueHandler.publish_message(client, message_json, constants.topic_moisture)
    
    message_json = lib.packageJSON.package_value(constants.moisture_voltage_label,
        current_moisture_voltage, 
        lib.packageJSON.get_now_string(constants.now_string_format),
        host_name)
    comms.queueHandler.publish_message(client, message_json, constants.topic_moisture)

def record_light(client, light_sensor, host_name):
    current_light = sensors.readLight.read_light(light_sensor)
    message_json = lib.packageJSON.package_value(constants.light_label,
        current_light, 
        lib.packageJSON.get_now_string(constants.now_string_format),
        host_name)
    comms.queueHandler.publish_message(client, message_json, constants.topic_light)

def main():
    host_name = lib.packageJSON.get_hostname()

    if(constants.read_temperature):
        temperature_sensor = sensors.readTemperature.get_sensor(constants.air_temp_pin)
    if(constants.read_moisture):
        moisture_sensor = sensors.readMoisture.get_sensor(constants.moisture_pin, constants.moisture_dry_voltage, constants.moisture_wet_voltage)
    if(constants.read_light):
        light_sensor = sensors.readLight.get_sensor(constants.light_pin)

    client =  comms.queueHandler.get_client(constants.clientPublishName, constants.brokerAddress)

    while True:
        if(constants.read_temperature):
            record_temperature(client, temperature_sensor, host_name)

        if(constants.read_moisture):
            record_moisture(client, moisture_sensor, host_name)

        if(constants.read_light):
            record_light(client, light_sensor, host_name)

        time.sleep(constants.read_sensor_interval)
        


if __name__ == "__main__":
    main()