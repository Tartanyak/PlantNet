#Collector
dbFilenameConfigParameter = "dbfilename"
dbConfigFilename = "dbconfig.json"
read_temperature = True
read_moisture = True
read_light = True
clientSubscribeName = "PlantReader"

#Common
brokerAddress = "192.168.178.44"
topic_air_temperature = "PLANTNET/AIR_TEMP"
topic_moisture = "PLANTNET/MOISTURE"
topic_light = "PLANTNET/LIGHT"
topic_subscribe = "PLANTNET/+"
now_string_format = "%Y-%m-%d %H:%M:%S:%f"
temperature_label = "temperature"
moisture_label = "moisture"
moisture_voltage_label = "moisturevoltage"
light_label = "light"

#Monitor
plant_id = "1"
moisture_dry_voltage = 2048
moisture_wet_voltage = 1250
read_sensor_interval = 300
air_temp_pin = 2 #int
moisture_pin = 0 #int
light_pin = 4 #int
clientPublishName = "PlantData"