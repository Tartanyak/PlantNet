import constants
import comms.queueSubscriber 
import lib.helpers
import datalayer.dbConnection
import datalayer.plantLogRecorder
import signal
import sys

def signal_handler(sig, frame):
    
    print("Stopping MQTT client")
    pc.stop()
    print("Test details")
    datalayer.dbConnection.testPrintSql(db_connection, "select * from plant_logs")
    print("Closing DB connection")
    db_connection.close()
    sys.exit(0)

def test_theory(client, userdata, message):
    message_json = lib.helpers.message_to_string(message) 
    
    print(datalayer.plantLogRecorder.create_log_sql(db_connection, message_json))

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