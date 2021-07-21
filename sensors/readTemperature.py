import time
from grove.factory import Factory
# connect to alalog pin 2(slot A2)
PIN = 2
sensor = Factory.getTemper("NTC-ADC", PIN)
print('Detecting temperature...')
while True:
    print('{} Celsius'.format(sensor.temperature))
    time.sleep(2)