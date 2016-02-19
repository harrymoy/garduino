from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

from dbHandler import dbHandler

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
	#Handle GET requests
	def do_GET(self):
		try:
			self.send_response(200)
			self.send_header('Content-Type', 'text/html')
			self.end_headers()
			x = dbHandler()
			z = x.getAll()
			self.wfile.write(z)
		except:
			self.send_error(404)

try:
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	server.serve_forever()

except KeyboardInterrupt:
	server.socket.close()