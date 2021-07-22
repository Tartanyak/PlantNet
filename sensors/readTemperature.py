from grove.factory import Factory

def read_temperature(sensor):
    return '{} Celsius'.format(sensor.temperature)

def get_sensor(pin):
    sensor = Factory.getTemper("NTC-ADC", pin)
    return sensor