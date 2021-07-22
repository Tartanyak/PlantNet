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
        adjusted_voltage = abs(self.voltage - self.dry_voltage)
        percent = (self.wet_voltage/100)*adjusted_voltage
        return percent
    
    @property
    def voltage(self):
        value = self.adc.read_voltage(self.channel)
        return value

def get_sensor(pin, dry_voltage, wet_voltage):
    sensor = GroveCapMoistureSensor(pin, dry_voltage, wet_voltage)
    return sensor

PIN = 0
sensor = get_sensor(PIN, 2048, 1266)
print('Detecting temperature...')
while True:
    print('{} mV'.format(sensor.voltage))
    print('{} %'.format(sensor.moisture_percent))
    time.sleep(2)
    