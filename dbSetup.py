import json
import sqlite3
import os
from sqlite3 import Error

dbFilenameConfigParameter = "dbfilename"
dbConfigFilename = "dbconfig.json"

createPlantTable = """CREATE TABLE IF NOT EXISTS plants (
id integer PRIMARY KEY,
name text NOT NULL,
acquired_date text,
location text
);
"""
createPlantLogTable = """CREATE TABLE IF NOT EXISTS plant_logs (
id integer PRIMARY KEY,
log_date text not null,
log_detail text
);
"""
createLocationTable = """CREATE TABLE IF NOT EXISTS locations (
name text PRIMARY KEY,
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

insertDemoLocation = """insert into locations (name, floor) values ('Living room', 0)"""
insertDemoPlant = """insert into plants (name, acquired_date, location) values ('Big plant', '2016-05-05', 'Living room')"""
insertDemoLog = """insert into plant_logs (log_date, log_detail) values (strftime('%Y-%m-%d %H:%M:%S:%f'), 'testData')"""



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

def insertDemoData(connection):
	if connection is not None:
		runSql(connection, insertDemoLocation)
		runSql(connection, insertDemoPlant)
		runSql(connection, insertDemoLog)
		connection.commit()

def runSql(connection, sql):
	try:
		cursor = connection.cursor()
		cursor.execute(sql)
	except Error as e:
		print(e)

def testPrintSql(connection, sql):
	try:
		cursor = connection.cursor()
		cursor.execute(sql)
		rows = cursor.fetchall()
		for row in rows:
			print(row)

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
	insertDemoData(connection)
	testPrintSql(connection, "select * from plants join locations on plants.location = locations.name")
	testPrintSql(connection, "select * from plant_logs")
	closeDbConnection(connection)
	

if __name__ == '__main__':
	main() 
