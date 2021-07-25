import constants
import comms.queueSubscriber 
import lib.packageJSON 
import paho.mqtt.client as mqtt
import time
import datalayer.dbConnection



class PlantCollector:
    db_connection = None
    def __init__(self):
        print("Starting collector")
        client =  comms.queueSubscriber.get_client(constants.clientPublishName, constants.brokerAddress)
        print("Opening DB")

        db_file = datalayer.dbConnection.get_config_parameter(
            datalayer.dbConnection.get_config_json(constants.dbConfigFilename),
            constants.dbFilenameConfigParameter
        )

        self.db_connection = datalayer.dbConnection.get_db_connection(self.db_connection, db_file)

        comms.queueSubscriber.start_loop(client, constants.topic_subscribe, self.on_message, self.on_connect)

    def on_message(client, userdata, message):
        print("Collector received message: " ,str(message.payload.decode("utf-8")))

    def on_connect(client, userdata, flags, rc):
        print("Collector connection returned result: " + mqtt.connack_string(rc))


def main():
    PlantCollector()

if __name__ == "__main__":
    main()