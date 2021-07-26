import constants
import comms.queueSubscriber 
import lib.helpers
import datalayer.dbConnection
import datalayer.plantLogRecorder
import signal
import sys

def signal_handler(sig, frame):
    #Clean exit
    print("Stopping MQTT client")
    pc.stop()
    print("Test details")
    datalayer.dbConnection.testPrintSql(db_connection, "select * from plant_logs where log_variable = 'light'")
    print("Closing DB connection")
    db_connection.close()
    sys.exit(0)

def record_log(client, userdata, message):
    message_json = lib.helpers.message_to_string(message) 
    insert_sql = datalayer.plantLogRecorder.create_log_sql(db_connection, message_json)
    datalayer.dbConnection.runSql(db_connection, insert_sql)
    db_connection.commit()

#Starting here

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
db_file = datalayer.dbConnection.get_config_parameter(
            datalayer.dbConnection.get_config_json(constants.dbConfigFilename),
            constants.dbFilenameConfigParameter
        )
db_connection = None
db_connection = datalayer.dbConnection.get_db_connection(db_connection, db_file)

pc = comms.queueSubscriber.QueueSubscriber(constants.clientSubscribeName)
pc.on_message = record_log
pc.run(constants.brokerAddress, constants.topic_subscribe)