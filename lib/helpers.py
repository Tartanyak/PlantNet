from datetime import datetime
import socket

def get_now_string(now_string_format):
    return datetime.now().strftime(now_string_format)

def get_hostname():
    return socket.gethostname()

def message_to_string(message):
    return str(message.payload.decode("utf-8"))