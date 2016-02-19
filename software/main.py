from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import SimpleHTTPServer
from dbHandler import dbHandler

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
	#Handle GET requests
	def do_GET(self):
		self.send_response(200)

try:
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	server.serve_forever()

except KeyboardInterrupt:
	server.socket.close()