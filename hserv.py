from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import argparse
import logging
import sys

parser = argparse.ArgumentParser(allow_abbrev=False, description='Simple Python Server SSRF')
parser.add_argument('-p', '--port',required=True, help='port number to listen on')
args = parser.parse_args()

PORT = int(args.port)
logging.basicConfig(level=logging.INFO)

class Handler(SimpleHTTPRequestHandler):

    #response to client
    def sen_response(self):
        self.send_response(200)
        self.send_header('Content-Type','text/html')
        self.end_headers()

    #redirect client with /redirect path
    def Redirect(self,location):
        self.send_response(302)
        self.send_header('Location', location)
        self.end_headers()

    def do_GET(self):
        #check path to redirect
        if '/redirect' in self.path :
            location = self.path.split('=')
            logging.info(f'\nGET {self.path} {self.request_version}\n{self.headers}')
            self.Redirect(location[1])
        else :
            logging.info(f'\nGET {self.path} {self.request_version}\n{self.headers}')
            self.sen_response()
            self.wfile.write("abcdefghijklmnopqrstivwxyz")

    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len)

        logging.info(f'\nPOST {self.path} {self.request_version}\n{self.headers}')
        print(post_body.decode('utf-8'))

        self.sen_response()
        self.wfile.write("abcdefghijklmnopqrstivwxyz")

httpd = TCPServer(("", PORT), Handler)

try :
    print(f'Listening on ::{PORT}')
    httpd.serve_forever()
except KeyboardInterrupt :
    pass

httpd.server_close()
print('Server is closed')