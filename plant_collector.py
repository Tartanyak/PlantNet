import constants
import comms.queueSubscriber 
import lib.packageJSON 
import paho.mqtt.client as mqtt
import time
import datalayer.dbConnection



class PlantCollector:
    db_connection = None
    client = None

    def __init__(self):
        print("Starting collector")
        self.client =  comms.queueSubscriber.get_client(constants.clientPublishName, constants.brokerAddress)
        
        print("Opening DB")

        db_file = datalayer.dbConnection.get_config_parameter(
            datalayer.dbConnection.get_config_json(constants.dbConfigFilename),
            constants.dbFilenameConfigParameter
        )

        self.db_connection = datalayer.dbConnection.get_db_connection(self.db_connection, db_file)

        #comms.queueSubscriber.start_loop(client, constants.topic_subscribe, self.on_message, self.on_connect)

        

    def listen(self):
        client =  comms.queueSubscriber.get_client(constants.clientPublishName, constants.brokerAddress)
        client.on_message = self.on_message
        client.on_connect = self.on_connect
        client.on_subscribe = self.on_subscribe
        client.on_log = self.on_log
        print(self.client.subscribe("PLANTNET/+"))
        client.loop_start()
        print("starting loop")
        
        
        time.sleep(20)
        comms.queueSubscriber.stop_loop(client)
        client.loop_stop()

    def on_message(self, client, userdata, message):
        print("Here")
        print("Collector received message: " ,str(message.payload.decode("utf-8")))

    def on_connect(self, client, userdata, flags, rc):
        print("Collector connection returned result: " + mqtt.connack_string(rc))

    def on_subscribe(self, client, userdata, mid, qos):
        print("Collector subscribed with id "+ str(mid))

    def on_log(client, userdata, level, buf):
        print("log: ",buf)
def main():
    pc = PlantCollector()
    pc.listen()

if __name__ == "__main__":
    main()