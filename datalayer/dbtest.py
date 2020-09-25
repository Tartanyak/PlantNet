import json
import sqlite3
from sqlite3 import Error

dbFilenameConfigParameter = "dbfilename"
dbConfigFilename = "dbconfig.json"

createPlantTable = ""
createPlantLogTable = ""
createClientTable = ""

def getDbFilename(configFilename):
	with open(configFilename) as dbConfigFile:
		dbConfig = json.load(dbConfigFile)

	dbFilename = dbConfig[dbFilenameConfigParameter]
	print(dbFilename)
	return dbFilename

def createDbConnection(dbFile):
	connection = None
	try:
		conn = sqlite3.connect(dbFile)
		print(sqlite3.version)
	except Error as e:
		print(e)
	finally:
		if connection:
			connection.close()

if __name__ == '__main__':
	dbFilename = getDbFilename(dbConfigFilename)
	createDbConnection(dbFilename)
 
