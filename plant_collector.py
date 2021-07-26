import constants
import comms.queueSubscriber 
import lib.helpers
import paho.mqtt.client as mqtt
import time
import datalayer.dbConnection
import signal
import sys

def signal_handler(sig, frame):
    pc.stop()
    print("Exiting")
    sys.exit(0)

def test_theory(client, userdata, message):
    print(lib.helpers.message_to_string(message))

signal.signal(signal.SIGINT, signal_handler)

db_file = datalayer.dbConnection.get_config_parameter(
            datalayer.dbConnection.get_config_json(constants.dbConfigFilename),
            constants.dbFilenameConfigParameter
        )
db_connection = None
db_connection = datalayer.dbConnection.get_db_connection(db_connection, db_file)

pc = comms.queueSubscriber.QueueSubscriber(constants.clientSubscribeName)
pc.on_message = test_theory
pc.run(constants.brokerAddress, constants.topic_subscribe)