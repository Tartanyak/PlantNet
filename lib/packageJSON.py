import json

def package_value(label, value, time, host_id):
    message = {
        "timestamp": time,
        "source":"testPi1",
        "variable":label,
        "value":value,
        "host_id":host_id
        }
    jsonDump = json.dumps(message)
    print(jsonDump)
    return jsonDump    
