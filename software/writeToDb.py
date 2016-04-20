import serial
from pymongo import MongoClient
import json
from time import gmtime, strftime

ser = serial.Serial('/dev/cu.usbmodem1421', 9600) #Getting connection to Serial port
client = MongoClient()
db = client.garduino
garden = db.garden

try: #Using try in case of errors
	while True: #Ensuring it's constantly looping
		x = ser.readline() #Reading from serial
		if x != None: #Providing we're not getting nothing 
			# Parsing the JSON data
			print x #So we can see what data looks like
			data = json.loads(x) #Loading the serial data into JSON so we can parse keys
			timeStamp = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #Getting the current date and time
			print "data is " + str(data)
			for i in data:
				soilMoisture = data['Soil Moisture'] #Parsing JSON
				airQuality = data['Air Quality']
				humidity = data['Humidity']
				temperature = data['Temperature']
				light = data['Lux']

				data = {"Time": timeStamp, "Soil Moisture": soilMoisture, "Air Quality": airQuality, "Humidity": humidity, "Temperature": temperature, "Light": light}
				insertion = db.garden.insert_one(data)

except Exception, e:
	print "Serial closed"
	print e
	ser.close() #If we get an error, close the connection to serial
	conn.close() #If we get an error, close the connection to the database