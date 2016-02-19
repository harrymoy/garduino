import sqlite3 as sqlite
conn = sqlite.connect('soil.db')
cur = conn.cursor()

class dbHandler():

	def getAll(self):
		for row in cur.execute("SELECT * FROM GARDEN"):
			print row

	def getSoil(self):
		for row in cur.execute("SELECT TIME, SOIL_MOISTURE FROM GARDEN"):
			print row

	def getAirQuality(self):
		for row in cur.execute("SELECT TIME, AIR_QUALITY FROM GARDEN"):
			print row

	def getLight(self):
		for row in cur.execute("SELECT TIME, LIGHT FROM GARDEN"):
			print row

	def getHumidity(self):
		for row in cur.execute("SELECT TIME, HUMIDITY FROM GARDEN"):
			print row

	def getTemp(self):
		for row in cur.execute("SELECT TIME, TEMPERATURE FROM GARDEN"):
			print row
