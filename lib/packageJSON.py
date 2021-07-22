import json
from datetime import datetime
import socket

def package_temperature(temperature, time, host_id):
    message = {
        "timestamp": time,
        "source":"testPi1",
        "temperature":temperature,
        "host_id":host_id
        }
    jsonDump = json.dumps(message)
    print(jsonDump)
    return jsonDump    

def get_now_string(now_string_format):
    return datetime.now().strftime(now_string_format)

def get_hostname():
    return socket.gethostname()