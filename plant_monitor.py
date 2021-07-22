import constants
from comms.queueHandler import get_client, publish_message
from lib.packageJSON import package_temperature, get_now_string, get_hostname
from sensors.readTemperature import get_sensor, read_temperature
import time

def main():
    host_name = get_hostname()
    temperature_sensor = get_sensor()
    client = get_client(constants.clientPublishName, constants.topic_air_temperature)

    while True:
        try:

            current_temperature = read_temperature(temperature_sensor, constants.air_temp_pin)
            message_json = package_temperature(current_temperature, 
                get_now_string(constants.now_string_format),
                host_name)
            publish_message(client, message_json, constants.topic_air_temperature)
            time.sleep(10)
            break
        except KeyboardInterrupt:
            print("Exiting...")
        except:
            print("not connected yet, trying again....")


if __name__ == "__main__":
    main()