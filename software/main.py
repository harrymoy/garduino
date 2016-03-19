from Flask import flask, request, Response
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()

@app.route('/data', methods=['GET'])
def getData():
	soil = request.params.get('soil')
	air = request.params.get('air')
	humidity = request.params.get('humidity')
	temp = request.params.get('temp')
	light = request.params.get('light')
	if soil:
		return soil
	elif air:
		return air
	elif humidity:
		return humidity
	elif temp:
		return temp
	elif light:
		return light
	else:
		return else