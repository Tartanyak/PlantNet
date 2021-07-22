import constants
from comms import queueHandler
from lib import packageJSON
from sensors import readTemperature
import time

def main():
    host_name = packageJSON.get_hostname()
    temperature_sensor = readTemperature.get_sensor()
    client = queueHandler.get_client(constants.clientPublishName, constants.topic_air_temperature)

    while True:
        try:

            current_temperature = readTemperature.read_temperature(temperature_sensor, constants.air_temp_pin)
            message_json = packageJSON.package_temperature(current_temperature, 
                packageJSON.get_now_string(constants.now_string_format),
                host_name)
            queueHandler.publish_message(client, message_json, constants.topic_air_temperature)
            time.sleep(10)
            break
        except KeyboardInterrupt:
            print("Exiting...")
        except:
            print("not connected yet, trying again....")


if __name__ == "__main__":
    main()