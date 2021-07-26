import paho.mqtt.client as mqtt
import time

class QueueSubscriber(mqtt.Client):
    output_function = None

    def __init__(self, client_id):
        super(QueueSubscriber, self).__init__(client_id)
        print("Starting collector")
        
        print("Opening DB")

        
        #self.output_function = output_function

    def on_message(self, client, userdata, message):
        self.output_function("Funky")
        print("Collector received message: " ,str(message.payload.decode("utf-8")))

    def on_connect(self, client, userdata, flags, rc):
        print("Collector connection returned result: ", mqtt.connack_string(rc))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Collector subscribed with id "+ str(mid))

    #def on_log(self, mqttc, obj, level, buf):
    #    print("log: ", buf)

    def run(self, brokerAddress, topic_subscribe):
        self.connect(brokerAddress)
        self.subscribe(topic_subscribe)

        self.loop_forever()


    def stop(self):
        self.loop_stop()

    def message_to_string(message):
        return str(message.payload.decode("utf-8"))

