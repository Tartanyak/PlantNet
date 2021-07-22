from grove.adc import ADC
import time

class GroveCapMoistureSensor:
    def __init__(self, channel, dry_voltage, wet_voltage):
            self.channel = channel
            self.adc = ADC()
            self.dry_voltage = dry_voltage
            self.wet_voltage = wet_voltage

    @property
    def moisture_percent(self):
        v = self.voltage
        normalised_value = abs(self.dry_voltage-v)
        print("dry-v = {}".format(normalised_value))
        dif = float(abs(self.dry_voltage - self.wet_voltage))
        print("diff = {}".format(dif))
        print(normalised_value/dif)
        percent = (normalised_value/dif)*100
        return percent
    
    @property
    def voltage(self):
        value = self.adc.read_voltage(self.channel)
        return value

def get_sensor(pin, dry_voltage, wet_voltage):
    sensor = GroveCapMoistureSensor(pin, dry_voltage, wet_voltage)
    return sensor

def read_moisture(sensor):
    return '{}'.format(sensor.moisture_percent)

    