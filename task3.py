import BaseHTTPServer
import SimpleHTTPServer

FILE = 'task2.html'
PORT = 8080

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """Handler - handle post request from task2.html"""

    def do_POST(self):
        """Handle the plain/encrypted text - return the encrypted/decrypted text"""
        length = int(self.headers.getheader('content-length'))        
        data = self.rfile.read(length)
        self.wfile.write(data)

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, Handler)
    server.serve_forever()

if __name__ == "__main__":
    start_server()