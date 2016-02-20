import sqlite3 as sqlite
conn = sqlite.connect('soil.db')
cur = conn.cursor()

class dbHandler():

	def getAll(self):
		list = []
		for row in cur.execute("SELECT TIME, SOIL_MOISTURE, AIR_QUALITY, LIGHT, HUMIDITY, TEMPERATURE FROM GARDEN"):
			print row
			list.append(row)
			return list

	def getSoil(self):
		list = []
		for row in cur.execute("SELECT TIME, SOIL_MOISTURE FROM GARDEN"):
			print row
			list.append(row)
			return list

	def getAirQuality(self):
		for row in cur.execute("SELECT TIME, AIR_QUALITY FROM GARDEN"):
			print row
			return row

	def getLight(self):
		for row in cur.execute("SELECT TIME, LIGHT FROM GARDEN"):
			print row

	def getHumidity(self):
		for row in cur.execute("SELECT TIME, HUMIDITY FROM GARDEN"):
			print row

	def getTemp(self):
		for row in cur.execute("SELECT TIME, TEMPERATURE FROM GARDEN"):
			print row
