import sqlite3
from xlsxwriter import Workbook
workbook = Workbook('fileHere')
worksheet = workbook.add_worksheet()

conn = sqlite3.connect('soil.db')
c = conn.cursor( )
c.execute('SELECT * FROM GARDEN')
mysel=c.execute('SELECT * FROM GARDEN')
for i, row in enumerate(mysel):
	for j, value in enumerate(row):
		worksheet.write(i, j item)
workbook.close()