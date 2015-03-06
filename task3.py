import BaseHTTPServer
import SimpleHTTPServer
from string import ascii_uppercase

FILE = 'task3.html'
PORT = 8080

#encoded and decoded lists
encrypted = ascii_uppercase
plain = encrypted[3:] + encrypted[:3]

def encrypt(text):
    """Caesar cipher encrypting
    text : plain text to encrypt
    returns : encoded text
    """
    t = []
    for l in text.upper():
        if l in plain:  t.append(encrypted[plain.index(l)])     #decrypt letter if it's not punctuation 
        else:           t.append(l)                             #else: keep punctuation
    return  ''.join(t)

def decrypt(text):
    """Caesar cipher decrypting
    text : encrypted text to decrypt
    returns : decrypted text
    """
    t = []
    for l in text.upper():
        if l in plain:  t.append(plain[encrypted.index(l)])     #decrypt letter if it's not punctuation 
        else:           t.append(l)                             #else: keep punctuation
    return  ''.join(t)


class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """Handler - handle post request from task2.html"""

    def do_POST(self):
        """Handle the plain/encrypted text - return the encrypted/decrypted text"""
        length = int(self.headers.getheader('content-length'))        
        data = self.rfile.read(length)
        way, txt = data.split('_')[0], data.split('_')[1]
        try:
            result = eval(way.lower())(txt)
        except:
            result = 'ERROR in the process'
        self.wfile.write(result)

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, Handler)
    server.serve_forever()

if __name__ == "__main__":
    start_server()