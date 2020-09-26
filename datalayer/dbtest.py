import json
import sqlite3
from sqlite3 import Error

dbFilenameConfigParameter = "dbfilename"
dbConfigFilename = "dbconfig.json"

createPlantTable = """CREATE TABLE IF NOT EXISTS plants (
id integer PRIMARY KEY,
name text NOT NULL,
acquired_date text,
location integer
);
"""
createPlantLogTable = """CREATE TABLE IF NOT EXISTS plant_log (
id integer PRIMARY KEY,
log_date PRIMARY KEY,
log_detail text
);
"""
createLocationTable = """CREATE TABLE IF NOT EXISTS locations (
id integer PRIMARY KEY,
name text not null,
floor integer not null
);
"""
createClientTable = ""

def getDbFilename(configFilename):
	with open(configFilename) as dbConfigFile:
		dbConfig = json.load(dbConfigFile)

	dbFilename = dbConfig[dbFilenameConfigParameter]
	print(dbFilename)
	return dbFilename

def getDbConnection(dbFile):
	connection = None
	try:
		connection = sqlite3.connect(dbFile)
		print(sqlite3.version)
		return connection
	except Error as e:
		print(e)
#	finally:
#		if connection:
#			connection.close()

def createDatabaseTables(connection):
	if connection is not None:
		createDatabaseTable(connection, createPlantTable)
#		createDatabaseTable(connection, createPlantTable)
#		createDatabaseTable(connection, createPlantTable)
#		createDatabaseTable(connection, createPlantTable)
	else:
		print("No DB connection")

def createDatabaseTable(connection, tableSql):
	try:
		cursor = connection.cursor()
		cursor.execute(tableSql)
	except Error as e:
		print(e)

def closeDbConnection(connection):
	if connection:
		connection.close()

def main():
	dbFilename = getDbFilename(dbConfigFilename)
	connection = getDbConnection(dbFilename)
	createDatabaseTables(connection)
	closeDbConnection(connection)

if __name__ == '__main__':
	main() 
