import sqlite3
import json
from sqlite3 import Error

insert_sql = """insert into {0} ({1}) values ({2})"""

def create_log_sql(connection, log_details):
    log_json = json.loads(log_details)
    json_timestamp = log_json["timestamp"]
    json_variable = log_json["variable"]
    json_value = log_json["value"]
    log_table = """plant_logs"""
    log_columns = """log_date, log_json, log_variable, log_value"""
    log_values = "'{0}', '{1}', '{2}', '{3}'".format(json_timestamp, log_details, json_variable, json_value)
    return insert_sql.format(log_table, log_columns, log_values)