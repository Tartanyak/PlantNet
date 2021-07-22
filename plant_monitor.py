import constants
import comms.queueHandler 
import lib.packageJSON 
import sensors.readTemperature 
import sensors.readMoisture
#import paho.mqtt.client as mqtt
import time

def main():
    print("Getting hostname")
    host_name = lib.packageJSON.get_hostname()
    print("Hostname:" + host_name)
    print("Getting sensor from pin {}".format(constants.air_temp_pin))
    if(constants.read_temperature):
        temperature_sensor = sensors.readTemperature.get_sensor(constants.air_temp_pin)
    if(constants.read_moisture):
        moisture_sensor = sensors.readMoisture.get_sensor(constants.moisture_pin, constants.moisture_dry_voltage, constants.moisture_wet_voltage)
    print("Got sensor")
    print("Getting MQTT client with " + constants.clientPublishName + " and brokerAddress " + constants.brokerAddress) 
    client =  comms.queueHandler.get_client(constants.clientPublishName, constants.brokerAddress)
        
    print("Got client")

    while True:
        if(constants.read_temperature):
            current_temperature = sensors.readTemperature.read_temperature(temperature_sensor)
            message_json = lib.packageJSON.package_value(constants.temperature_label,
                current_temperature, 
                lib.packageJSON.get_now_string(constants.now_string_format),
                host_name)
            comms.queueHandler.publish_message(client, message_json, constants.topic_air_temperature)
        if(constants.read_moisture):
            current_moisture = sensors.readMoisture.read_moisture(moisture_sensor)
            message_json = lib.packageJSON.package_value(constants.moisture_label,
                current_moisture, 
                lib.packageJSON.get_now_string(constants.now_string_format),
                host_name)
            comms.queueHandler.publish_message(client, message_json, constants.topic_moisture)

        time.sleep(constants.read_sensor_interval)
        
        


if __name__ == "__main__":
    main()