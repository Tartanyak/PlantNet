from grove.factory import Factory

def read_temperature(sensor):
    return sensor.temperature

def get_sensor(pin):
    sensor = Factory.getTemper("NTC-ADC", pin)
    return sensor