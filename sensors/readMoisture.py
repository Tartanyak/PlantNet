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
        dif = abs(self.dry_voltage - self.wet_voltage)
        print("diff = {}".format(dif))

        percent = normalised_value/dif
        return percent
    
    @property
    def voltage(self):
        value = self.adc.read_voltage(self.channel)
        return value

def get_sensor(pin, dry_voltage, wet_voltage):
    sensor = GroveCapMoistureSensor(pin, dry_voltage, wet_voltage)
    return sensor

PIN = 0
sensor = get_sensor(PIN, 2048, 1250)
print('Detecting temperature...')
while True:
    print('{} mV'.format(sensor.voltage))
    print('{} %'.format(sensor.moisture_percent))
    time.sleep(2)
    