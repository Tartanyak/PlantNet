import json
import sqlite3
import os
from sqlite3 import Error

dbFilenameConfigParameter = "dbfilename"
dbConfigFilename = "D:\\Dev\\Projects\\PlantNet\\datalayer\\dbconfig.json"

createPlantTable = """CREATE TABLE IF NOT EXISTS plants (
id integer PRIMARY KEY,
name text NOT NULL,
acquired_date text,
location integer
);
"""
createPlantLogTable = """CREATE TABLE IF NOT EXISTS plant_logs (
id integer not null,
log_date not null,
log_detail text,
PRIMARY KEY(id, log_date)
);
"""
createLocationTable = """CREATE TABLE IF NOT EXISTS locations (
id integer PRIMARY KEY,
name text not null,
floor integer not null
);
"""
createClientTable = """CREATE TABLE IF NOT EXISTS clients (
name text PRIMARY KEY,
description text
);
"""

dropPlantsTable = "drop table plants"
dropPlantLogsTable = "drop table plant_logs"
dropLocationsTable = "drop table locations"
dropClientsTable = "drop table clients"



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
	if connection is not None:
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
