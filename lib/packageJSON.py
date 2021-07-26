import json

def package_value(source_plant, label, value, time, host_id):
    message = {
        "timestamp": time,
        "source":source_plant,
        "variable":label,
        "value":value,
        "host_id":host_id
        }
    jsonDump = json.dumps(message)
    print(jsonDump)
    return jsonDump    
