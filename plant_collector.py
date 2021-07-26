import constants
import comms.queueSubscriber 
import lib.packageJSON 
import paho.mqtt.client as mqtt
import time
import datalayer.dbConnection
import signal
import sys

class PlantCollector(mqtt.Client):
    db_connection = None

    def __init__(self, client_id):
        super(PlantCollector, self).__init__(client_id)
        print("Starting collector")
        
        print("Opening DB")

        db_file = datalayer.dbConnection.get_config_parameter(
            datalayer.dbConnection.get_config_json(constants.dbConfigFilename),
            constants.dbFilenameConfigParameter
        )

        self.db_connection = datalayer.dbConnection.get_db_connection(self.db_connection, db_file)

    def on_message(self, client, userdata, message):
        print("Here")
        print("Collector received message: " ,str(message.payload.decode("utf-8")))

    def on_connect(self, client, userdata, flags, rc):
        print("Collector connection returned result: ", mqtt.connack_string(rc))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Collector subscribed with id "+ str(mid))

    #def on_log(self, mqttc, obj, level, buf):
    #    print("log: ", buf)

    def run(self):

        self.connect(constants.brokerAddress)
        self.subscribe(constants.topic_subscribe)

        self.loop_start()

    def stop(self):
        self.loop_stop()


def signal_handler(sig, frame):
    pc.stop()
    print("Exiting")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
pc = PlantCollector(constants.clientSubscribeName)
pc.run()