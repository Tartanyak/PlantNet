from grove.grove_light_sensor_v1_2 import GroveLightSensor

def get_sensor(pin):
    sensor = GroveLightSensor(pin)
    return sensor

def read_light(sensor):
    return '{0}'.format(sensor.light)