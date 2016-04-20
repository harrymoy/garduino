from pymongo import MongoClient
from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)
client = MongoClient()
db = client.garduino
garden = db.garden

@app.route('/data', methods=['GET'])
def getData():
	cur = db.garden.find({}, {'_id': False})
	itemList = []
	for item in cur:
		print item
		itemList.append(item)
	result = jsonify({'results': itemList})
	resp = app.make_response(resp)
	return resp

if __name__ == '__main__':
    app.run()