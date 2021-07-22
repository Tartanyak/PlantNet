import sqlite3
import json
from sqlite3 import Error

class dbConnection:
	dbFilenameConfigParameter = "dbfilename"
	dbConfigFilename = "dbconfig.json"

	connection = None

	def getConnection(self, dbFile):
		if self.connection is None:
			try:
				connection = sqlite3.connect(dbFile)
				print(sqlite3.version)
				return self.connection
			except Error as e:
				print(e)
		else:
			return self.connection
