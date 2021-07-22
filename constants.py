from grove import temperature
from readTemperature import read_temperature


brokerAddress = "192.168.178.44"
clientPublishName = "PlantData"
clientSubscribeName = "PlantReader"
topic_air_temperature = "AIR_TEMP"
topic_moisture = "MOISTURE"
read_sensor_interval =2
air_temp_pin = 0 #int
moisture_pin = 2 #int
now_string_format = "%H:%M:%S:%f"
moisture_dry_voltage = 2048
moisture_wet_voltage = 1250
temperature_label = "temperature"
moisture_label = "moisture"
read_temperature = False
read_moisture = True