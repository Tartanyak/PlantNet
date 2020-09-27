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
createPlantLogTable = """CREATE TABLE IF NOT EXISTS plant_logs (
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
createClientTable = """CREATE TABLE IF NOT EXISTS clients
name text PRIMARY KEY,
description text
"""

dropPlantTable = "drop table if exists plants"
dropPlantLogTable = "drop table if exists plant_log"
dropLocationTable = "drop table id exists locations"
dropClientTable = "drop table if exists clients"

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
		runSql(connection, createPlantTable)
		runSql(connection, createPlantLogTable)
		runSql(connection, createLocationTable)
		runSql(connection, createClientTable)
	else:
		print("No DB connection")

def removeDbTables(connection):
	if connection is not None
		runSql(connection, dropPlantsTable)
		runSql(connection, dropPlantLogsTable)
		runSql(connection, dropLocationsTable)
		runSql(connection, dropClientsTable)


def runSql(connection, sql):
	try:
		cursor = connection.cursor()
		cursor.execute(sql)
	except Error as e:
		print(e)

def closeDbConnection(connection):
	if connection:
		connection.close()

def main():
	dbFilename = getDbFilename(dbConfigFilename)
	connection = getDbConnection(dbFilename)
	removeDbTables(connection)
	createDatabaseTables(connection)
	closeDbConnection(connection)

if __name__ == '__main__':
	main() 
