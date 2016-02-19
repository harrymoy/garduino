import serial
import sqlite3 as sqlite
import json
from time import gmtime, strftime

ser = serial.Serial('/dev/cu.usbmodem1421', 9600) #Getting connection to Serial port
conn = sqlite.connect('soil.db') #Accessing Database
cur = conn.cursor() #Allowing us to do stuff to database

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

				dataList = [timeStamp, soilMoisture, airQuality, humidity, temperature, light] #Putting parsed JSON data into a list
				
				# Executing the query
				cur.execute('INSERT INTO GARDEN VALUES (?, ?, ?, ?, ?, ?)', dataList) #Executing SQL query, ? represents placeholder values, the nth item in list goes into the corresponding nth placeholder
				conn.commit() #Saving changes to database
except Exception, e:
	print "Serial closed"
	print e
	ser.close() #If we get an error, close the connection to serial
	conn.close() #If we get an error, close the connection to the database