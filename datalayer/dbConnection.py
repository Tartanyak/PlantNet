import sqlite3
import json
from sqlite3 import Error
import os


#dbFilenameConfigParameter = "dbfilename"
#dbConfigFilename = "dbconfig.json"

connection = None

def get_db_connection(connection, dbFile):
	if connection is None:
		try:
			connection = sqlite3.connect(dbFile)
			print(sqlite3.version)
			return connection
		except Error as e:
			print(e)
	else:
		return connection

def get_config_parameter(config_json, parameter):
	value = config_json[parameter]
	print(value)
	return value

def get_config_json(filename):
	with open(filename) as dbConfigFile:
		dbConfig = json.load(dbConfigFile)
		return dbConfig

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

