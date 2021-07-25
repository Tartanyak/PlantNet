import constants
import comms.queueSubscriber 
import lib.packageJSON 
import paho.mqtt.client as mqtt
import time
import datalayer.dbConnection

def main():
    print("Starting collector")
    client =  comms.queueSubscriber.get_client(constants.clientPublishName, constants.brokerAddress)
    print("Opening DB")

    db_file = datalayer.dbConnection.get_config_parameter(
        datalayer.dbConnection.get_config_json(constants.dbConfigFilename),
        constants.dbFilenameConfigParameter
    )
    db_connection = None
    db_connection = datalayer.dbConnection.get_db_connection(db_connection, db_file)
    

def on_message(client, userdata, message):
    print("Collector received message: " ,str(message.payload.decode("utf-8")))

def on_connect(client, userdata, flags, rc):
    print("Collector connection returned result: " + mqtt.connack_string(rc))

if __name__ == "__main__":
    main()