import constants
import comms.queueHandler 
import lib.packageJSON 
import sensors.readTemperature 
import sensors.readMoisture
#import paho.mqtt.client as mqtt
import time


def main():
    print("Starting collector")

    client =  comms.queueSubscriber.get_client(constants.clientPublishName, constants.brokerAddress)


if __name__ == "__main__":
    main()