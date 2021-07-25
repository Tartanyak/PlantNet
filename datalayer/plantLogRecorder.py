import sqlite3
import json
from sqlite3 import Error

insert_sql = """insert into {0} ({1}) values {2}"""

def create_log_sql(connection, log_details):
    json_timestamp = log_details["timestamp"]
    json_variable = log["variable"]
    json_value = log["value"]
    print("{0}, {1}, {2}".format(json_timestamp, json_variable, json_value))
    log_table = """"""
    log_columns = """"""
    log_values = """"""